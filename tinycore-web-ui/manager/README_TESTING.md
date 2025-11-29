# PTY Capture Testing Guide

This directory contains test harnesses to validate that PTY automatically captures stdout/stderr from processes before building the full UI system.

## Files

- `test_pty_capture.py` - Test harness with 4 different validation modes
- `test_pty_viewer.html` - Browser-based terminal viewer for WebSocket mode
- `pty_collector.py` - Full production collector (in `tinycore_manager/collectors/`)

## Quick Start

### 1. Basic Capture Test
```bash
python test_pty_capture.py
```

This runs two automated tests:
- Captures output from `ls -la --color=always`
- Captures Python script that writes to both stdout and stderr

**What you'll see:**
- Colored directory listing
- Mixed stdout/stderr output
- Proof that PTY captures everything automatically

### 2. Interactive Bash Test
```bash
python test_pty_capture.py --interactive
```

Type any commands you want:
```
ls
pwd
echo "Hello from bash"
python -c "print('test')"
```

Press `Ctrl+D` to exit.

**What this proves:**
- Bidirectional I/O works
- You can send input to PTY
- Everything appears as if in a real terminal

### 3. WebSocket Streaming Test

First, install websockets:
```bash
pip install websockets
```

Start the server:
```bash
python test_pty_capture.py --websocket
```

Then **either**:

#### Option A: Command-line client
```bash
# In another terminal
websocat ws://localhost:8080
```

#### Option B: Browser viewer
Open `test_pty_viewer.html` in your browser and type commands in the input field.

**What this proves:**
- PTY output can be streamed in real-time
- WebSocket transport works
- You have the foundation for remote terminal viewing

### 4. Custom Command Test
```bash
python test_pty_capture.py --command "python -c \"for i in range(10): print(f'Line {i}')\""
```

Run any command and see its output captured.

## What PTY Captures Automatically

When you spawn a process via PTY:
- ✅ **stdout** - All print statements, command output
- ✅ **stderr** - Error messages, warnings
- ✅ **ANSI escape codes** - Colors, cursor movements
- ✅ **Interactive prompts** - Bash PS1, password prompts
- ✅ **Full-screen apps** - vim, htop, etc. (with proper terminal emulation)

**No redirection needed!** The process's file descriptors are automatically connected to the PTY slave.

## Architecture Validation

This test harness validates the capture pipeline:

```
┌──────────────┐
│  ls/bash/etc │  Writes to what it thinks is a terminal
└──────┬───────┘
       │ stdout/stderr → PTY slave
┌──────▼───────┐
│  PTY Master  │  Your code reads here
└──────┬───────┘
       │ Read loop
┌──────▼───────┐
│  WebSocket   │  Stream to browser
└──────┬───────┘
       │
┌──────▼───────┐
│  Web UI      │  Display in browser
└──────────────┘
```

## Next Steps

Once these tests pass:

1. **Integrate `pty_collector.py`** into your host manager
   - Connect to resource registry
   - Wire up event emission
   
2. **Build transport layer**
   - WebSocket server (see `test_pty_capture.py --websocket` as example)
   - Emit `terminal.data` events per protocol

3. **Create web UI**
   - Use xterm.js for proper ANSI rendering
   - Handle resize events
   - Route keyboard input back to collector

4. **Add features**
   - Multiple terminals
   - Session persistence
   - Terminal multiplexing

## Troubleshooting

### "Permission denied" on PTY
Make sure you have permission to create PTY devices. Should work on any modern Linux system.

### "No module named 'websockets'"
```bash
pip install websockets
```

### Output looks garbled in browser
The simple HTML viewer doesn't parse ANSI codes. For full terminal emulation, use xterm.js in your actual UI.

### Interactive mode doesn't respond
Make sure stdin is a TTY. If running in an IDE, use a real terminal instead.

## Performance Notes

The test harness is intentionally simple:
- Reads in 4KB chunks (typical buffer size)
- Non-blocking I/O with async/await
- Minimal processing overhead

The production `pty_collector.py` adds:
- Proper sequence numbering
- Resource lifecycle management
- Error handling and cleanup
- Integration with resource registry
