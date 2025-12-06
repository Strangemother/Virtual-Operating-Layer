# Host Manager Requirements

## Purpose
The host manager is the privileged TinyCore service that centralises OS access, exposes a message-driven UI API, and coordinates auxiliary transports (remote display, media streaming). A Python prototype will ship first to validate the protocol, then be replaced by a Nim/C implementation once the interfaces stabilise.

## Functional Requirements (MVP)
1. **Messaging Core**
   - WebSocket server (Unix + TCP) with authentication hooks.
   - Subscription protocol for `resource.*` ops and `event.input` messages.
   - Replay log so reconnecting clients can request snapshots + deltas.
2. **Resource Registry**
   - Canonical state store with unique resource IDs and component metadata.
   - Diff engine producing `create/patch/delete` ops, plus versioning (`version`, `etag`).
   - Persistence of last-known state to disk for deterministic restarts.
3. **Collector Runtime**
   - Plugin system to register collectors with lifecycle hooks (`start`, `stop`, `on_input`).
   - Initial collectors: system metrics, PTY manager, process control, DBus signal tap.
   - Event normalisation into schema defined in `docs/protocol.md`.
4. **Input Router**
   - Validates input payloads, enforces focus, rate-limit per resource, and forwards to the owning collector.
   - Optional acknowledgements for critical commands (kill process, mount device).
5. **Observability + Admin**
   - Structured logs, metrics (message rate, collector health), and trace IDs per request.
   - Minimal CLI/HTTP endpoint for diagnostics and hot reloads.
6. **Stream Coordination (stub in MVP)**
   - Ability to register `resource.stream` metadata and negotiate transport (WebRTC/RTP) even if the actual encoder is mocked initially.

## Non-Functional Requirements
- **Performance**: <2% idle CPU, <10 MB RSS on TinyCore. Cap message burst at 60 Hz per resource unless flagged as high-priority.
- **Security**: run as dedicated user with CAP_SYS_ADMIN only when necessary; enforce ACLs per collector. All remote transports must support TLS/mTLS.
- **Reliability**: collectors should survive crashes via supervisor restarts; registry must rebuild from snapshot + WAL.
- **Extensibility**: schemas defined via reusable IDL (JSON Schema/Protocol Buffers) so rewrites in Nim/C remain wire-compatible.

## Python Prototype Scope
- Asyncio service with structured config (YAML/TOML) and hot-reload support.
- Skeleton WebSocket transport, resource registry, metrics + PTY collectors.
- Integration tests that replay fixture logs to guarantee deterministic state.

## Migration Path to Nim/C
1. Finalise schemas and fixtures; publish conformance tests.
2. Port hot paths (registry, collectors) to Nim/C while keeping Python harness for reference + fuzz tests.
3. Share transport code via sockets/protocol libs to avoid reimplementation.
4. Deprecate Python runtime only after Nim/C passes conformance and burn-in tests on actual TinyCore hardware.

## Deliverables
- `manager/pyproject.toml` + package skeleton for the prototype.
- Collector and transport interfaces with docstrings + unit tests.
- Updated documentation in `docs/protocol.md` and `docs/overview.md` as capabilities expand.
