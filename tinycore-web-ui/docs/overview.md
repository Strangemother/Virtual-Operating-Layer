# TinyCore UI Architecture Overview

A reference architecture for a Thin UI layer that controls TinyCore Linux through a dedicated host manager and HTML/CSS/JS clients.

## Layered System Diagram

```
┌─────────────────────────────────────────────┐
│         Web UI (HTML/CSS/JS)                │
│  - System Monitor                           │
│  - Process Manager                          │
│  - Terminal/TTY widgets                     │
│  - Settings + media panes                   │
└─────────────┬───────────────────────────────┘
              │ WebSocket / WebRTC (control)
┌─────────────▼───────────────────────────────┐
│      Host Manager (Python → Nim/C)          │
│  - Collector runtime                        │
│  - Resource registry + diff engine          │
│  - Transports (WS, gRPC, SPICE bridge)      │
│  - Stream coordinators (media/video)        │
└─────────────┬───────────────────────────────┘
              │ System calls / kernel APIs
┌─────────────▼───────────────────────────────┐
│         TinyCore Linux Kernel               │
│  /proc  /sys  /dev  syscalls  PipeWire      │
└─────────────────────────────────────────────┘
```

## Component Responsibilities

### Host Manager (`manager/`)
- Runs as a privileged service on TinyCore and exposes OS capabilities through collectors.
- Publishes canonical UI state via the resource registry and replays diffs to subscribers.
- Brokers input back to collectors (PTY, focus manager, process controls) and enforces policy.
- Coordinates auxiliary transports (PipeWire → WebRTC, DMA-BUF streaming) for heavy media.

### Web UI Clients (`clients/` in future)
- Render-only shells that consume `resource.*` events and emit `event.input` payloads.
- Maintain a lightweight component registry so state changes map directly to DOM/canvas updates.
- Support optional remote transports (WebRTC/Waypipe) without understanding kernel details.

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
              │ Subscriptions + input events  
┌─────────────▼───────────────────────────────┐
│ Web UI                                      │
│  - Dumb renderer (DOM/canvas)               │
│  - Component registry (terminal, panel)     │
│  - Input publisher                          │
└─────────────────────────────────────────────┘
```

### Resource Model Essentials
- Each visible entity (window, widget, terminal session, notification) receives a stable resource ID and `component` hint (for example `component:"terminal.v1"`).
- The host manager stores canonical state and emits idempotent ops:
  - `resource.create` – initial payload and style tokens.
  - `resource.patch` – minimal updates produced by the diff engine.
  - `resource.delete` – tear-down instructions.
- Clients subscribe only to the prefixes they require (`terminal:*`, `layout`, `notifications`) to keep bandwidth low.

### Transport Contracts
- Default transport is WebSocket (Unix sockets locally, TCP for remote). Payloads start as JSON and can later switch to MsgPack/FlatBuffers with no schema changes.
- Each message carries `version` and optional `etag` so reconnecting clients can detect divergence and request a full snapshot.
- Authentication is transport-specific: Unix-socket ACLs locally, mTLS/OAuth for remote WebSocket, DTLS-SRTP for WebRTC.

### Input Feedback
- UI components emit `event.input` messages with target resource IDs, payload details (key, pointer, resize), and timestamps.
- The host manager routes inputs to the owning collector (PTY session, compositor, etc.) and can acknowledge critical actions for determinism.

## Flow Procedures

### Startup Sequence
1. **Host Manager boot**: collectors initialize, register with the resource registry, and hydrate persisted state.
2. **Transport bring-up**: WebSocket/WebRTC services bind to sockets and expose `/subscribe` semantics.
3. **UI connect**: shell authenticates, declares resource prefixes, and requests snapshot.
4. **Snapshot replay**: registry replays `resource.create` ops followed by the most recent `patch` to rebuild the scene graph.

### Resource Lifecycle
1. Collector detects a state change (for example, new terminal session).
2. Collector posts a normalized event to the registry.
3. Registry assigns/updates the resource ID, runs the diff engine, persists the op, and queues it for transports.
4. Transports fan out the resulting `create/patch/delete` to subscribed clients.

### Input Round-Trip
1. User interaction triggers `event.input` with resource ID + payload.
2. Transport forwards to the host manager; registry routes to the owner collector.
3. Collector applies the input (write to PTY, send DBus call, etc.) and emits state changes back through the lifecycle.

### Terminal Bridging Example
1. UI requests `terminal.open` with `rows`, `cols`, optional command.
2. PTY collector spawns the process, registers the resource, and streams ANSI data as `terminal.data` events.
3. UI renders via xterm.js-equivalent; resize gestures emit `terminal.resize` which maps to PTY `setWindowSize`.
4. On process exit, collector emits `resource.delete`, and UI tears down the widget.

## Relation to Existing Protocols
- **X11** inspired the resource-table + command-stream approach (structured messages instead of raw pixels).
- **Wayland** parallels the "clients draw, compositor composites" model; here the web UI is the compositor and collectors supply buffers/metadata.
- **SPICE/RDP** informed the dual-transport idea: lightweight control channel plus optional media streams for heavy video/game content.

## Implementation Checklist
1. Finalize message schema and versioning strategy (`docs/protocol.md`).
2. Implement the resource registry/diff engine inside the new host manager service.
3. Build initial collectors (system metrics, PTY manager) and unit-test them in isolation.
4. Create a UI shell that maps `component` hints to renderers and subscribes to resource prefixes.
5. Add integration tests or a replay harness to ensure recorded event logs recreate identical UI state.
6. Layer authentication plus optional remote transports once the local WebSocket path is stable.

## Performance Tactics
- Delta-only updates with monotonically increasing versions.
- Batching/coalescing at most once per animation frame.
- Client-side caching of styles/assets; messages reference tokens rather than inline CSS.
- Selective subscriptions, binary encodings when needed, and zero-copy pipelines for terminals/media via dedicated transports.
