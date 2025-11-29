"""
PTY Collector - Manages terminal sessions for CLI applications.

Spawns processes in pseudo-terminals and streams their I/O as resource events.
"""

import asyncio
import os
import pty
import signal
import struct
import termios
from dataclasses import dataclass
from typing import Optional, Callable
import fcntl


@dataclass
class TerminalGeometry:
    """Terminal window dimensions."""
    rows: int
    cols: int
    xpixels: int = 0
    ypixels: int = 0


class PTYSession:
    """
    Represents a single PTY-backed terminal session.
    
    Manages the lifetime of a child process running in a pseudo-terminal,
    capturing its output and forwarding input from the UI.
    """
    
    def __init__(
        self,
        resource_id: str,
        command: list[str],
        geometry: TerminalGeometry,
        env: Optional[dict[str, str]] = None,
        cwd: Optional[str] = None,
        emit_callback: Optional[Callable] = None
    ):
        self.resource_id = resource_id
        self.command = command
        self.geometry = geometry
        self.env = env or {}
        self.cwd = cwd or os.getcwd()
        self.emit = emit_callback or (lambda *args: None)
        
        self.pid: Optional[int] = None
        self.master_fd: Optional[int] = None
        self.sequence = 0
        self.running = False
        
    async def start(self):
        """Fork and exec the command in a new PTY."""
        # Fork with PTY
        self.pid, self.master_fd = pty.fork()
        
        if self.pid == 0:  # Child process
            # Set environment
            os.environ.update(self.env)
            os.environ['TERM'] = os.environ.get('TERM', 'xterm-256color')
            
            # Change directory
            try:
                os.chdir(self.cwd)
            except OSError:
                pass
            
            # Execute command
            try:
                os.execvp(self.command[0], self.command)
            except Exception as e:
                print(f"Failed to exec {self.command}: {e}", file=sys.stderr)
                os._exit(1)
        
        # Parent process
        self.running = True
        
        # Set master FD to non-blocking
        flags = fcntl.fcntl(self.master_fd, fcntl.F_GETFL)
        fcntl.fcntl(self.master_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        
        # Set initial window size
        self._set_winsize(self.geometry)
        
        # Emit resource.create event
        self.emit('resource.create', {
            'id': self.resource_id,
            'payload': {
                'pid': self.pid,
                'command': ' '.join(self.command),
                'geometry': {
                    'rows': self.geometry.rows,
                    'cols': self.geometry.cols
                },
                'state': 'running'
            },
            'meta': {
                'component': 'terminal.v1',
                'version': 1
            }
        })
        
        # Start I/O loop
        asyncio.create_task(self._read_loop())
        asyncio.create_task(self._monitor_process())
        
    async def _read_loop(self):
        """Read output from PTY master and emit data events."""
        loop = asyncio.get_event_loop()
        
        while self.running:
            try:
                # Wait for data to be available
                await loop.run_in_executor(None, self._wait_for_data)
                
                # Read available data (non-blocking)
                chunk = os.read(self.master_fd, 4096)
                if not chunk:
                    # EOF - process has closed its output
                    break
                
                # Emit terminal.data event
                self.sequence += 1
                self.emit('terminal.data', {
                    'id': self.resource_id,
                    'payload': {
                        'chunk': chunk.decode('utf-8', errors='replace'),
                        'encoding': 'utf-8'
                    },
                    'meta': {
                        'sequence': self.sequence
                    }
                })
                
            except OSError:
                # Master FD closed
                break
            except Exception as e:
                print(f"PTY read error: {e}")
                break
        
        await self.stop()
    
    def _wait_for_data(self):
        """Block until data is available (runs in thread pool)."""
        import select
        select.select([self.master_fd], [], [])
    
    async def _monitor_process(self):
        """Monitor child process and handle exit."""
        loop = asyncio.get_event_loop()
        
        # Wait for process to exit
        _, status = await loop.run_in_executor(None, os.waitpid, self.pid, 0)
        
        # Extract exit code
        if os.WIFEXITED(status):
            exit_code = os.WEXITSTATUS(status)
        elif os.WIFSIGNALED(status):
            exit_code = -os.WTERMSIG(status)
        else:
            exit_code = -1
        
        # Emit resource.delete event
        self.emit('resource.delete', {
            'id': self.resource_id,
            'meta': {
                'reason': 'exited',
                'exitCode': exit_code
            }
        })
        
        self.running = False
    
    def write_input(self, data: str):
        """Write user input to PTY master."""
        if not self.running or self.master_fd is None:
            return
        
        try:
            os.write(self.master_fd, data.encode('utf-8'))
        except OSError as e:
            print(f"PTY write error: {e}")
    
    def resize(self, geometry: TerminalGeometry):
        """Resize the PTY window."""
        self.geometry = geometry
        self._set_winsize(geometry)
        
        # Emit resource.patch event
        self.emit('resource.patch', {
            'id': self.resource_id,
            'payload': [
                {
                    'op': 'replace',
                    'path': '/geometry',
                    'value': {
                        'rows': geometry.rows,
                        'cols': geometry.cols
                    }
                }
            ],
            'meta': {
                'version': self.sequence
            }
        })
    
    def _set_winsize(self, geometry: TerminalGeometry):
        """Set PTY window size via ioctl."""
        if self.master_fd is None:
            return
        
        # struct winsize { unsigned short ws_row, ws_col, ws_xpixel, ws_ypixel }
        winsize = struct.pack(
            'HHHH',
            geometry.rows,
            geometry.cols,
            geometry.xpixels,
            geometry.ypixels
        )
        
        try:
            fcntl.ioctl(self.master_fd, termios.TIOCSWINSZ, winsize)
        except OSError as e:
            print(f"Failed to set window size: {e}")
    
    async def stop(self):
        """Clean up resources."""
        self.running = False
        
        if self.master_fd is not None:
            try:
                os.close(self.master_fd)
            except OSError:
                pass
        
        if self.pid is not None:
            try:
                os.kill(self.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass


class PTYCollector:
    """
    Collector that manages multiple PTY sessions.
    
    Handles terminal.open requests from the UI and routes input events
    to the appropriate session.
    """
    
    def __init__(self, emit_callback: Callable):
        self.emit = emit_callback
        self.sessions: dict[str, PTYSession] = {}
        self.next_id = 1
    
    async def handle_event(self, event: dict):
        """Process input events from the UI."""
        event_type = event.get('type')
        target = event.get('target')
        payload = event.get('payload', {})
        
        if event_type == 'event.input' and target == 'system':
            action = payload.get('action')
            
            if action == 'terminal.open':
                await self._open_terminal(payload)
        
        elif event_type == 'event.input' and target.startswith('terminal:'):
            session = self.sessions.get(target)
            if not session:
                return
            
            kind = payload.get('kind')
            
            if kind == 'keyboard':
                session.write_input(payload.get('data', ''))
            
            elif kind == 'resize':
                geometry = payload.get('geometry', {})
                session.resize(TerminalGeometry(
                    rows=geometry.get('rows', 24),
                    cols=geometry.get('cols', 80)
                ))
            
            elif kind == 'close':
                await self._close_terminal(target)
    
    async def _open_terminal(self, config: dict):
        """Create a new PTY session."""
        resource_id = f"terminal:tty-{self.next_id:04x}"
        self.next_id += 1
        
        # Parse configuration
        command = config.get('command', '/bin/bash')
        if isinstance(command, str):
            command = [command]
        
        geometry_data = config.get('geometry', {})
        geometry = TerminalGeometry(
            rows=geometry_data.get('rows', 24),
            cols=geometry_data.get('cols', 80)
        )
        
        env = config.get('env', {})
        cwd = config.get('cwd')
        
        # Create and start session
        session = PTYSession(
            resource_id=resource_id,
            command=command,
            geometry=geometry,
            env=env,
            cwd=cwd,
            emit_callback=self.emit
        )
        
        self.sessions[resource_id] = session
        await session.start()
    
    async def _close_terminal(self, resource_id: str):
        """Close an existing PTY session."""
        session = self.sessions.pop(resource_id, None)
        if session:
            await session.stop()
    
    async def shutdown(self):
        """Clean up all sessions."""
        for session in list(self.sessions.values()):
            await session.stop()
        self.sessions.clear()


# Example usage
if __name__ == '__main__':
    import sys
    
    def print_event(event_type: str, data: dict):
        """Print events to console."""
        print(f"{event_type}: {data}")
    
    async def main():
        collector = PTYCollector(emit_callback=print_event)
        
        # Simulate terminal.open request
        await collector.handle_event({
            'type': 'event.input',
            'target': 'system',
            'payload': {
                'action': 'terminal.open',
                'command': '/bin/bash',
                'geometry': {'rows': 24, 'cols': 80}
            }
        })
        
        # Keep running
        await asyncio.sleep(30)
        await collector.shutdown()
    
    asyncio.run(main())
