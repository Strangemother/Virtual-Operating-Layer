# TinyCore Web UI System

A web-based graphical interface for TinyCore Linux with deep OS integration.

## Architecture

```
┌─────────────────────────────────────────────┐
│         Web UI (HTML/CSS/JS)                │
│  - System Monitor                           │
│  - Process Manager                          │
│  - File Browser                             │
│  - Settings                                 │
└─────────────┬───────────────────────────────┘
              │ WebSocket (bidirectional)
┌─────────────▼───────────────────────────────┐
│      System Daemon (Node.js/Python)         │
│  - Input device handler (/dev/input/*)      │
│  - System API (processes, files, hardware)  │
│  - Event broadcaster                        │
└─────────────┬───────────────────────────────┘
              │ System calls
┌─────────────▼───────────────────────────────┐
│         Linux Kernel APIs                   │
│  /proc  /sys  /dev  syscalls                │
└─────────────────────────────────────────────┘
```

## Components

### 1. System Daemon (`daemon/`)
- Runs as privileged service
- Direct access to kernel interfaces
- WebSocket server for UI communication
- HTTP server for static UI files

### 2. Web UI (`ui/`)
- Pure HTML/CSS/JS (no framework overhead)
- Real-time system monitoring
- Event-driven architecture

### 3. Renderer
- Option A: Run in existing browser
- Option B: Embedded WebKit/Chromium (kiosk mode)
- Option C: Custom framebuffer renderer

## Design Goals
- Keep TinyCore lean while a separate UI service renders the entire desktop in HTML/CSS/JS.
- Model the UX after thin-display systems like X11, Wayland, and SPICE: send structured state updates, not frame buffers.
- Enable remote display transports (WebSocket, WebRTC, future SPICE/RDP bridge) without rewriting collectors or UI components.
- Maintain deterministic, replayable state so interfaces can reconnect, resubscribe, and rebuild the scene graph quickly.

## Messaging Architecture

```
┌─────────────────────────────────────────────┐
│ Collectors                                  │
│  - PTY manager (terminals)                  │
│  - DBus/event listeners                     │
│  - Metrics/telemetry                        │
└─────────────┬───────────────────────────────┘
                            │ Normalized events
┌─────────────▼───────────────────────────────┐
│ Resource Registry                           │
│  - Resource IDs + metadata                  │
│  - Diff engine (create/patch/delete)        │
│  - Versioning + replay log                  │
└─────────────┬───────────────────────────────┘
                            │ Serialized ops (JSON/MsgPack)
┌─────────────▼───────────────────────────────┐
│ Transports                                  │
│  - WebSocket over Unix/TCP                  │
│  - WebRTC DataChannel (future)              │
│  - SPICE/RDP bridge (future)                │
└─────────────┬───────────────────────────────┘
                            │ subscriptions + events
┌─────────────▼───────────────────────────────┐
│ Web UI                                      │
│  - Dumb renderer (DOM/canvas)               │
│  - Component registry (terminal, panel)     │
│  - Input publisher                          │
└─────────────────────────────────────────────┘
```

### Resource model
- Every visible entity (window, widget, terminal session, notification) receives a stable resource ID and component hint (`component:"terminal.v1"`).
- The daemon stores canonical state and emits idempotent ops:
    - `resource.create` – initial payload and style tokens.
    - `resource.patch` – minimal updates produced by the diff engine.
    - `resource.delete` – tear-down instructions.
- Clients request only the prefixes they care about (`terminal:*`, `layout`, `notifications`) to keep bandwidth minimal.

### Transport contracts
- Default transport is WebSocket over Unix/TCP; messages use JSON during development and can switch to MsgPack/FlatBuffers later without changing the schema.
- Each message carries `version` and optional `etag` so reconnecting clients can detect divergence and request a full snapshot.
- Authentication can be layered per transport (Unix-socket ACLs locally, mTLS/WebRTC for remote viewers).

### Input feedback
- UI components emit `event.input` messages with target resource IDs, payload details (key, pointer, resize), and timestamps.
- The daemon routes inputs to the owning collector (e.g., PTY session, focus manager) and can acknowledge critical actions to keep the UI deterministic.

## Flow Procedures

### 1. Startup sequence
1. **Daemon boot**: collectors initialize, register themselves with the resource registry, and hydrate any persisted state.
2. **Transport up**: WebSocket server binds to Unix/TCP sockets and exposes `/subscribe` semantics.
3. **UI connect**: web shell authenticates, declares the resource prefixes it needs, and requests the latest snapshot.
4. **Snapshot replay**: registry replays `resource.create` ops followed by the most recent `patch` versions so the UI reconstructs the full scene graph.

### 2. Resource lifecycle
1. Collector detects a state change (e.g., new terminal session).
2. Collector posts a normalized event to the registry.
3. Registry assigns/updates the resource ID, runs the diff engine, and persists the op in the replay log.
4. Transports fan out the resulting `create/patch/delete` to subscribed clients.

### 3. Input round-trip
1. User interacts with the web component; UI emits `event.input` with resource ID + data.
2. Transport forwards the message to the daemon; registry looks up the owner collector.
3. Collector applies the input (write to PTY, send signal, call DBus method) and, if state changes, emits a new normalized event which loops back through the lifecycle above.

### 4. Terminal bridging example
1. UI requests `terminal.open` with `rows`, `cols`, and optional command.
2. PTY collector spawns the process via `node-pty` (or equivalent), registers the resource, and streams ANSI data as `terminal.data` events.
3. UI renders data using xterm.js; resize gestures emit `terminal.resize`, which the collector maps to PTY `setWindowSize` and triggers layout patches.
4. When the process exits, collector emits `resource.delete`, and UI tears down the widget.

## Relation to Existing Protocols
- **X11** inspired the resource table + command stream approach (structured messages instead of raw pixels).
- **Wayland** parallels the “clients draw, compositor composites” model; here the web UI is the compositor, and collectors provide buffers/metadata.
- **SPICE/RDP** influenced the idea of switchable transports and display orders, enabling future remote viewers without touching business logic.

## Implementation Checklist
1. Define message schema and versioning strategy (`docs/protocol.md` recommended).
2. Implement the resource registry/diff engine in `daemon/daemon.js`.
3. Build initial collectors (system metrics, PTY manager) and unit-test them in isolation.
4. Extend `ui/app.js` with a component registry that maps `component` hints to renderers and subscribes to desired resource prefixes.
5. Add integration tests or a replay harness to validate that a recorded event log recreates identical UI state.
6. Layer authentication + optional remote transports once the local WebSocket path is stable.

## Tactics for the web messaging layer

+ Delta everything: keep the daemon’s canonical state, but only send structural changes (resource.patch) rather than full objects. Pair with monotonically increasing version numbers so the UI knows if it can skip older diffs.
+ Batch and coalesce: watch for bursts (e.g., window dragging) and coalesce multiple geometry updates into a single message per animation frame. Use a scheduler so you never emit more often than, say, 60 Hz.
+ Keep resources tiny: store only IDs + references, never full blobs. If you need rich content (images, logs), send them via secondary channels with caching or chunking.
+ Client-side caching: let the browser keep a component registry and local style sheets. Messages should reference class tokens instead of repeating CSS inline.
+ Selective subscriptions: allow the UI to subscribe to precise prefixes so unused widgets don’t trigger processing or serialization on the daemon.
+ Binary encoding later: start with JSON for clarity, but design messages so they can be packed into MsgPack/FlatBuffers once you need more throughput without changing semantics.
+ Zero-copy backends: for terminals or media, push raw data through shared memory or WebRTC data channels separate from the control bus, mirroring how Wayland uses shm buffers.