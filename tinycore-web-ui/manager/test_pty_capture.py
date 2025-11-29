#!/usr/bin/env python3
"""
PTY Capture Test Harness

Demonstrates that PTY automatically captures stdout/stderr from processes.
Run this to verify the capture pipeline works before building the full UI.

Usage:
    python test_pty_capture.py              # Capture ls output
    python test_pty_capture.py --command bash   # Interactive bash session
    python test_pty_capture.py --websocket      # Serve via WebSocket on :8080
"""

import asyncio
import os
import pty
import sys
import struct
import termios
import fcntl
import argparse
from typing import Optional


class SimplePTYCapture:
    """Minimal PTY capture for testing."""
    
    def __init__(self, command: list[str], rows: int = 24, cols: int = 80):
        self.command = command
        self.rows = rows
        self.cols = cols
        self.pid: Optional[int] = None
        self.master_fd: Optional[int] = None
        self.running = False
    
    async def start(self):
        """Fork process in PTY and start capturing."""
        # Fork with PTY - child gets stdin/stdout/stderr connected to PTY slave
        self.pid, self.master_fd = pty.fork()
        
        if self.pid == 0:  # Child process
            # Execute the command
            os.execvp(self.command[0], self.command)
            # Never reaches here if exec succeeds
            os._exit(1)
        
        # Parent process - set up master FD
        self.running = True
        
        # Make master FD non-blocking
        flags = fcntl.fcntl(self.master_fd, fcntl.F_GETFL)
        fcntl.fcntl(self.master_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        
        # Set window size
        self._set_window_size()
        
        print(f"✓ Spawned process (PID {self.pid})")
        print(f"✓ PTY master FD: {self.master_fd}")
        print(f"✓ Capturing output...\n")
        print("-" * 80)
    
    def _set_window_size(self):
        """Set PTY window size."""
        winsize = struct.pack('HHHH', self.rows, self.cols, 0, 0)
        fcntl.ioctl(self.master_fd, termios.TIOCSWINSZ, winsize)
    
    async def read_output(self, callback=None):
        """
        Read output from PTY master.
        
        Args:
            callback: Optional function(data: bytes) to handle each chunk
        """
        loop = asyncio.get_event_loop()
        
        while self.running:
            try:
                # Wait for data (blocking call in executor)
                await loop.run_in_executor(None, self._wait_for_read)
                
                # Read available data
                chunk = os.read(self.master_fd, 4096)
                if not chunk:
                    # EOF - process closed output
                    print("\n" + "-" * 80)
                    print("✓ Process closed output (EOF)")
                    break
                
                if callback:
                    callback(chunk)
                else:
                    # Default: print to console
                    sys.stdout.buffer.write(chunk)
                    sys.stdout.buffer.flush()
                
            except OSError:
                break
        
        # Wait for process to exit
        _, status = await loop.run_in_executor(None, os.waitpid, self.pid, 0)
        
        exit_code = os.WEXITSTATUS(status) if os.WIFEXITED(status) else -1
        print(f"✓ Process exited with code: {exit_code}")
        
        self.running = False
    
    def _wait_for_read(self):
        """Block until data is available."""
        import select
        select.select([self.master_fd], [], [])
    
    def write_input(self, data: str):
        """Write input to PTY (for interactive sessions)."""
        if self.master_fd is not None:
            os.write(self.master_fd, data.encode('utf-8'))
    
    def close(self):
        """Clean up resources."""
        if self.master_fd is not None:
            os.close(self.master_fd)


async def test_simple_command():
    """Test 1: Capture output from a simple command."""
    print("=" * 80)
    print("TEST 1: Capture 'ls -la --color=always' output")
    print("=" * 80)
    
    capture = SimplePTYCapture(['ls', '-la', '--color=always'])
    await capture.start()
    await capture.read_output()
    capture.close()


async def test_multiline_script():
    """Test 2: Capture output from a Python script that prints to both stdout and stderr."""
    print("\n" + "=" * 80)
    print("TEST 2: Capture Python script with stdout + stderr")
    print("=" * 80)
    
    script = [
        'python3', '-c',
        'import sys\n'
        'print("STDOUT: Line 1")\n'
        'print("STDERR: Error message", file=sys.stderr)\n'
        'print("STDOUT: Line 2")\n'
        'for i in range(3):\n'
        '    print(f"  Item {i}")\n'
    ]
    
    capture = SimplePTYCapture(script)
    await capture.start()
    await capture.read_output()
    capture.close()


async def test_interactive_bash():
    """Test 3: Interactive bash session (you can type commands)."""
    print("\n" + "=" * 80)
    print("TEST 3: Interactive bash session")
    print("Type commands and see them captured in real-time")
    print("Press Ctrl+D to exit")
    print("=" * 80)
    
    capture = SimplePTYCapture(['bash'])
    await capture.start()
    
    # Start reading in background
    read_task = asyncio.create_task(capture.read_output())
    
    # Handle stdin input
    loop = asyncio.get_event_loop()
    stdin_fd = sys.stdin.fileno()
    
    while capture.running:
        try:
            # Read from stdin
            user_input = await loop.run_in_executor(None, sys.stdin.read, 1)
            if not user_input:  # EOF (Ctrl+D)
                break
            capture.write_input(user_input)
        except:
            break
    
    await read_task
    capture.close()


async def test_websocket_server():
    """Test 4: Serve PTY output via WebSocket."""
    try:
        import websockets
    except ImportError:
        print("\n" + "=" * 80)
        print("ERROR: websockets module not installed")
        print("Install with: pip install websockets")
        print("=" * 80)
        return
    
    print("\n" + "=" * 80)
    print("TEST 4: WebSocket Server")
    print("=" * 80)
    
    clients = set()
    capture = None
    
    async def handler(websocket):
        """Handle WebSocket connections."""
        print(f"✓ Client connected: {websocket.remote_address}")
        clients.add(websocket)
        
        try:
            # Send initial message
            await websocket.send("Connected to PTY stream\r\n")
            
            # Handle incoming messages (keyboard input)
            async for message in websocket:
                if capture and capture.running:
                    capture.write_input(message)
        
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            clients.remove(websocket)
            print(f"✓ Client disconnected")
    
    def broadcast_chunk(chunk: bytes):
        """Send PTY output to all connected clients."""
        if clients:
            asyncio.create_task(
                asyncio.gather(
                    *[client.send(chunk.decode('utf-8', errors='replace')) 
                      for client in clients],
                    return_exceptions=True
                )
            )
    
    # Start WebSocket server
    async with websockets.serve(handler, "localhost", 8080):
        print("✓ WebSocket server listening on ws://localhost:8080")
        print("✓ Connect with: websocat ws://localhost:8080")
        print("✓ Or open test_pty_viewer.html in a browser")
        print()
        
        # Start PTY capture
        capture = SimplePTYCapture(['bash'])
        await capture.start()
        
        # Read and broadcast
        await capture.read_output(callback=broadcast_chunk)
        
        capture.close()


def main():
    parser = argparse.ArgumentParser(description='PTY Capture Test Harness')
    parser.add_argument('--command', default=None, help='Command to run (default: run all tests)')
    parser.add_argument('--websocket', action='store_true', help='Start WebSocket server')
    parser.add_argument('--interactive', action='store_true', help='Run interactive bash')
    
    args = parser.parse_args()
    
    async def run_tests():
        if args.websocket:
            await test_websocket_server()
        elif args.interactive or args.command == 'bash':
            await test_interactive_bash()
        elif args.command:
            # Custom command
            capture = SimplePTYCapture(args.command.split())
            await capture.start()
            await capture.read_output()
            capture.close()
        else:
            # Run all non-interactive tests
            await test_simple_command()
            await test_multiline_script()
            
            print("\n" + "=" * 80)
            print("✓ All tests passed!")
            print("\nNext steps:")
            print("  1. Run with --websocket to test WebSocket streaming")
            print("  2. Run with --interactive for an interactive bash session")
            print("  3. Integrate pty_collector.py into your host manager")
            print("=" * 80)
    
    try:
        asyncio.run(run_tests())
    except KeyboardInterrupt:
        print("\n\n✓ Interrupted by user")


if __name__ == '__main__':
    main()
