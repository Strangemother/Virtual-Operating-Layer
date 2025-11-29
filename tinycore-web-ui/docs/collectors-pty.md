# PTY Collector Pattern

## Overview
The PTY collector enables unmodified CLI applications to run as managed resources within the TinyCore UI. It spawns processes in pseudo-terminals (PTY), captures their stdout/stderr ANSI output, and emits structured events to the resource registry.

## Architecture

```
┌─────────────────────────────────────┐
│  CLI App (vim, htop, bash)          │
│  - Writes ANSI/UTF-8 to stdout      │
│  - Reads stdin for user input       │
└─────────────┬───────────────────────┘
              │ PTY device pair (master/slave)
┌─────────────▼───────────────────────┐
│  PTY Collector                      │
│  - Monitors master FD for output    │
│  - Writes user input to master      │
│  - Tracks geometry (rows/cols)      │
│  - Handles resize events            │
└─────────────┬───────────────────────┘
              │ Emits resource events
┌─────────────▼───────────────────────┐
│  Resource Registry                  │
│  - Creates terminal:* resources     │
│  - Patches data/geometry            │
│  - Deletes on process exit          │
└─────────────┬───────────────────────┘
              │ Serialized messages
┌─────────────▼───────────────────────┐
│  Transport Layer                    │
│  - Fans out to subscribed clients   │
└─────────────┬───────────────────────┘
              │ WebSocket
┌─────────────▼───────────────────────┐
│  Web UI (xterm.js)                  │
│  - Renders ANSI sequences           │
│  - Emits keyboard/resize events     │
└─────────────────────────────────────┘
```

## Event Flow

### 1. Terminal Creation
UI requests new terminal:
```json
{
  "type": "event.input",
  "target": "system",
  "payload": {
    "action": "terminal.open",
    "command": "/bin/bash",
    "env": { "TERM": "xterm-256color" },
    "cwd": "/home/tc",
    "geometry": { "rows": 24, "cols": 80 }
  }
}
```

Collector spawns process and registers resource:
```json
{
  "type": "resource.create",
  "id": "terminal:tty-a3f2",
  "payload": {
    "pid": 1234,
    "command": "/bin/bash",
    "geometry": { "rows": 24, "cols": 80 },
    "state": "running"
  },
  "meta": {
    "component": "terminal.v1",
    "version": 1
  }
}
```

### 2. Data Stream
Process writes to PTY → collector reads chunks → emits data events:
```json
{
  "type": "terminal.data",
  "id": "terminal:tty-a3f2",
  "payload": {
    "chunk": "user@tinycore:~$ ls -la\r\n",
    "encoding": "utf-8"
  },
  "meta": { "sequence": 42 }
}
```

Key design points:
- **Chunking**: Emit on buffer availability (typically 4KB chunks) or timer (max 16ms latency)
- **Ordering**: Monotonic sequence numbers ensure correct reassembly
- **Encoding**: Always UTF-8; ANSI escape codes preserved verbatim

### 3. Input Handling
UI emits keyboard events:
```json
{
  "type": "event.input",
  "target": "terminal:tty-a3f2",
  "payload": {
    "kind": "keyboard",
    "data": "ls\r"
  }
}
```

Collector writes directly to PTY master FD; process reads from slave.

### 4. Resize
UI detects window resize:
```json
{
  "type": "event.input",
  "target": "terminal:tty-a3f2",
  "payload": {
    "kind": "resize",
    "geometry": { "rows": 40, "cols": 120 }
  }
}
```

Collector calls `ioctl(TIOCSWINSZ)` on PTY master, then emits state patch:
```json
{
  "type": "resource.patch",
  "id": "terminal:tty-a3f2",
  "payload": [
    { "op": "replace", "path": "/geometry", "value": { "rows": 40, "cols": 120 } }
  ],
  "meta": { "version": 7 }
}
```

### 5. Termination
Process exits → collector detects EOF on master FD:
```json
{
  "type": "resource.delete",
  "id": "terminal:tty-a3f2",
  "meta": {
    "reason": "exited",
    "exitCode": 0
  }
}
```

## Implementation Considerations

### PTY Library Choice
- **Python**: `pty` (stdlib) or `python-ptyprocess` (better control)
- **Nim**: `std/osproc` with custom PTY bindings via `posix` module
- **C**: `openpty()`, `forkpty()` from `<pty.h>`

### Performance Tuning
- **Coalescing**: Batch rapid output bursts (e.g., `cat large_file`) into single events
- **Backpressure**: If transport is slow, pause reading PTY to avoid memory bloat
- **Zero-copy**: Use shared memory or direct FD passing for local clients (future optimization)

### Security
- **Resource limits**: `setrlimit()` on child processes (CPU, memory, file descriptors)
- **Sandboxing**: Use `unshare()` or containers for untrusted commands
- **Authentication**: Validate that input events originate from authorized sessions

### Edge Cases
- **SIGWINCH handling**: Some apps (vim, emacs) rely on window size signals
- **Line discipline**: Ensure raw mode for full-screen apps, cooked mode for shells
- **UTF-8 boundaries**: Don't split multi-byte sequences across chunks

## Future Enhancements
- **Session persistence**: Detach/reattach via tmux-style multiplexing
- **Recording/replay**: Log all I/O for debugging or demos
- **Multiplexing**: Single PTY collector manages many terminals with distinct resource IDs
- **Wayland terminal protocol**: Native protocol for terminal widgets (no ANSI parsing overhead)
