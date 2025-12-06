# TinyCore UI Protocol Draft

## Message Envelope
```jsonc
{
  "type": "resource.create",   // or resource.patch, resource.delete, event.input, stream.*
  "version": 42,
  "id": "terminal:tty1",
  "payload": { /* type-specific */ },
  "meta": {
    "component": "terminal.v1",
    "etag": "b2e1c5fa",
    "timestamp": "2025-11-17T12:00:00Z"
  }
}
```

- `version`: monotonically increasing per-resource counter.
- `etag`: hash of the canonical resource JSON to let clients detect divergence.
- `timestamp`: ISO-8601 with timezone; optional but useful for replay logs.

## Resource Operations

### `resource.create`
Introduces a new resource.
```json
{
  "type": "resource.create",
  "id": "window:process-list",
  "payload": {
    "title": "Processes",
    "frame": { "x": 64, "y": 48, "w": 640, "h": 480 },
    "style": ["panel", "theme-dark"],
    "data": {}
  },
  "meta": { "component": "panel.v1", "version": 1 }
}
```

### `resource.patch`
Delta updates encoded as RFC6902-style operations.
```json
{
  "type": "resource.patch",
  "id": "window:process-list",
  "payload": [
    { "op": "replace", "path": "/frame/x", "value": 128 },
    { "op": "replace", "path": "/data/processCount", "value": 157 }
  ],
  "meta": { "version": 12 }
}
```

### `resource.delete`
```json
{
  "type": "resource.delete",
  "id": "window:process-list",
  "meta": { "reason": "closed" }
}
```

## Input Events
UI sends inputs through the same transport.
```json
{
  "type": "event.input",
  "target": "terminal:tty1",
  "payload": {
    "kind": "keyboard",
    "key": "a",
    "code": "KeyA",
    "modifiers": { "ctrl": false, "alt": false, "shift": false }
  },
  "meta": { "sequence": 551, "timestamp": "2025-11-17T12:00:03Z" }
}
```
- Host manager validates against focus/capabilities and routes to the collector.

## Stream Negotiation
1. Control channel emits `stream.start` announcing codec + transport.
```json
{
  "type": "stream.start",
  "id": "stream:window:video-player",
  "payload": {
    "resource": "window:video-player",
    "media": {
      "kind": "video",
      "codec": "H264",
      "width": 1280,
      "height": 720,
      "fps": 60
    },
    "transport": {
      "kind": "webrtc",
      "sdp": "v=0..."
    }
  }
}
```
2. Client responds with `stream.answer` (e.g., WebRTC SDP answer) or acknowledges TCP endpoints.
3. Once the stream is active, periodic `stream.stats` events report bitrate, loss, etc.
4. `stream.stop` tears everything down.

## Subscriptions
Clients subscribe immediately after connecting.
```json
{
  "type": "control.subscribe",
  "payload": {
    "resources": ["layout", "terminal:*", "notifications"]
  }
}
```
Server responds with snapshot payloads followed by a `control.snapshot_complete` message.

## Error Handling
- Errors are reported via `control.error` with `code`, `message`, `context`.
- Fatal transport errors force clients to reconnect and replay from snapshot.

## Text Stream Notes
- PTY collectors emit `terminal.data` events that wrap UTF-8 + ANSI sequences:
```json
{
  "type": "terminal.data",
  "id": "terminal:tty1",
  "payload": {
    "chunk": "\u001b[32muser@tinycore:\u001b[0m$ ",
    "encoding": "utf-8"
  },
  "meta": { "sequence": 901 }
}
```
- Clients feed chunks directly into their terminal emulator; ordering is guaranteed by `sequence` numbers and transport delivery (WebSocket per-connection ordering).

## Future Work
- Binary framing (MsgPack) once JSON prototype hardens.
- Capability negotiation so lightweight clients can decline heavy widgets.
- Signed messages for multi-tenant or remote deployments.
