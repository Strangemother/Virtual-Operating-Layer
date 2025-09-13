Status: Draft
Last-Touched: 2025-09-13
# Input Event Taxonomy (Extraction)

Purpose: Aggregate explicit input distribution and translation statements; identify absent canonical event list.

## Sourced Statements
1. VOL aims for agnostic awareness of HID or other input mounted devices; resources shared across mesh. (Source: docs/inputs.md)
2. Input may originate from HOST driver object, CORE motherboard devices, GPIO, any NODE. (Source: docs/inputs.md)
3. Mounting can occur via CONTAINER, RUNTIME as NODE, or CORE. (Source: docs/inputs.md)
4. CONTAINER maintains a portal; inputs flow through container into connected NODE and mesh. (Source: docs/inputs.md)
5. Translator processes input (and output) data into correct format for connected CONTAINER. (Source: docs/inputs.md)
6. Example scenario includes keypress propagating as MESH event; local container may render without relying on network event. (Source: docs/inputs.md)
7. Display container may also bridge hardware input (peripherals) and software input (RPC feedback / session info). (Source: docs/display (container).md)
8. Layer assignment provides display hook for application through RPC render pipeline (implying possible input association). (Source: docs/display (container).md)
9. Facade abstracts underlying functions and logical steps; potential input-facing APIs implied (not enumerated). (Source: docs/Facade.md)

## Observed Concepts (Names Only, No Enumerated Set Provided)
- HID / input mounted devices
- Portal (container portal)
- Translator
- MESH event
- Keypress (example only)
- Peripherals (audio, hardware input, software input)

## Not Present
- Canonical list of input event types
- Event naming schema (vector, dotted path, or other)
- Priority / ordering semantics
- Latency / local echo vs remote propagation rules

## Incomplete Blocks
Incomplete: Canonical Event Type Enumeration
Needed:
- Explicit list (e.g., keypress, pointer move, touch, stream, sensor)
- Definition granularity (raw vs normalized)
Candidate Sources: docs/inputs.md, docs/display (container).md

Incomplete: Event Translation Rules
Needed:
- Mapping stages (container → translator → runtime → mesh)
- Failure / fallback behavior if translator absent
Candidate Sources: docs/inputs.md

Incomplete: Local vs Mesh Propagation Semantics
Needed:
- Guarantee (if any) for local immediate render vs eventual network confirmation
- Conflict handling for simultaneous inputs across mirrored containers
Candidate Sources: docs/inputs.md, docs/display (container).md

Incomplete: Security / Authorization for Input Mounting
Needed:
- Access control model for mounting host/GPIO devices
- Isolation boundaries per NODE
Candidate Sources: docs/inputs.md

Incomplete: Portal Interface Contract
Needed:
- Required fields or message format entering portal
- Lifecycle (open/close, suspend)
Candidate Sources: docs/inputs.md, docs/display (container).md

Verbatim scope: docs/inputs.md, docs/display (container).md, docs/Facade.md only.
