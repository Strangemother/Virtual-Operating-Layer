#!/usr/bin/env python3
"""
Combined HTTP + WebSocket server for PTY testing.

Serves the HTML viewer over HTTP and handles WebSocket connections for PTY streaming.
"""

import asyncio
import os
import pty
import sys
import struct
import termios
import fcntl
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

try:
    import websocketshttps://stunning-robot-46pw96v4p3qx6x-8000.app.github.dev/test_pty_viewer.htmlhttps://stunning-robot-46pw96v4p3qx6x-8000.app.github.dev/test_pty_viewer.html
except ImportError:
    print("ERROR: websockets module not installed")
    print("Install with: pip install websockets")
    sys.exit(1)


class SimplePTYCapture:
    """Minimal PTY capture for testing."""
    
    def __init__(self, command: list[str], rows: int = 24, cols: int = 80):
        self.command = command
        self.rows = rows
        self.cols = cols
        self.pid = None
        self.master_fd = None
        self.running = False
    
    async def start(self):
        """Fork process in PTY and start capturing."""
        self.pid, self.master_fd = pty.fork()
        
        if self.pid == 0:  # Child process
            os.execvp(self.command[0], self.command)
            os._exit(1)
        
        # Parent process
        self.running = True
        
        # Make master FD non-blocking
        flags = fcntl.fcntl(self.master_fd, fcntl.F_GETFL)
        fcntl.fcntl(self.master_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        
        # Set window size
        winsize = struct.pack('HHHH', self.rows, self.cols, 0, 0)
        fcntl.ioctl(self.master_fd, termios.TIOCSWINSZ, winsize)
        
        print(f"✓ Spawned bash (PID {self.pid})")
    
    async def read_output(self, callback):
        """Read output from PTY master."""
        loop = asyncio.get_event_loop()
        
        while self.running:
            try:
                # Wait for data
                await loop.run_in_executor(None, self._wait_for_read)
                
                # Read available data
                chunk = os.read(self.master_fd, 4096)
                if not chunk:
                    break
                
                if callback:
                    await callback(chunk)
                
            except OSError:
                break
        
        # Wait for process
        try:
            await loop.run_in_executor(None, os.waitpid, self.pid, 0)
        except:
            pass
        
        self.running = False
    
    def _wait_for_read(self):
        """Block until data is available."""
        import select
        select.select([self.master_fd], [], [])
    
    def write_input(self, data: str):
        """Write input to PTY."""
        if self.running and self.master_fd is not None:
            try:
                os.write(self.master_fd, data.encode('utf-8'))
            except OSError:
                pass
    
    def close(self):
        """Clean up resources."""
        self.running = False
        if self.master_fd is not None:
            try:
                os.close(self.master_fd)
            except OSError:
                pass


async def main():
    """Run combined HTTP + WebSocket server."""
    
    # Track connected clients
    clients = set()
    capture = None
    
    # WebSocket handler
    async def ws_handler(websocket):
        """Handle WebSocket connections."""
        print(f"✓ Client connected from {websocket.remote_address}")
        clients.add(websocket)
        
        try:
            await websocket.send("Connected to PTY stream\r\n\r\n")
            
            # Handle incoming messages (keyboard input)
            async for message in websocket:
                if capture and capture.running:
                    capture.write_input(message)
        
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            clients.remove(websocket)
            print(f"✓ Client disconnected")
    
    # Broadcast PTY output to all clients
    async def broadcast_chunk(chunk: bytes):
        """Send PTY output to all connected clients."""
        if clients:
            await asyncio.gather(
                *[client.send(chunk.decode('utf-8', errors='replace')) 
                  for client in clients],
                return_exceptions=True
            )
    
    # Start HTTP server in background thread
    def run_http_server():
        """Serve HTML files over HTTP."""
        os.chdir(Path(__file__).parent)
        
        class Handler(SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                # Suppress HTTP logs
                pass
        
        httpd = HTTPServer(('0.0.0.0', 8000), Handler)
        print(f"✓ HTTP server listening on http://0.0.0.0:8000")
        httpd.serve_forever()
    
    http_thread = threading.Thread(target=run_http_server, daemon=True)
    http_thread.start()
    
    # Start WebSocket server
    print("\n" + "=" * 80)
    print("PTY Test Server Started")
    print("=" * 80)
    print(f"✓ WebSocket server: ws://localhost:8080")
    print(f"✓ HTTP server: http://localhost:8000")
    print(f"\n📱 Open in browser: http://localhost:8000/test_pty_viewer.html")
    print("=" * 80 + "\n")
    
    async with websockets.serve(ws_handler, "0.0.0.0", 8080):
        # Start PTY capture
        capture = SimplePTYCapture(['bash'])
        await capture.start()
        
        # Read and broadcast
        await capture.read_output(callback=broadcast_chunk)
        
        capture.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")
