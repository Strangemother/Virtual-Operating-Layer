---
Status: Draft
Last-Touched: 2025-09-13
Depends-On: interface-placeholder.md
---
# Interface Input Events (Extraction Draft)

Purpose: Catalog explicitly mentioned input flow concepts and container translation concerns without inventing event names.

## Extracted Concepts

1. Input Mounting Sources – HOST driver object, CORE motherboard devices, GPIO, any NODE (Source: [inputs.md](../../docs/inputs.md))
2. Shared Resource Model – Inputs shared across mesh without distinction (Source: [inputs.md](../../docs/inputs.md))
3. Container Portal – Container acts as portal for viewing and relaying inputs (Source: [inputs.md](../../docs/inputs.md))
4. Translator Role – Translates input (and output) data between RUNTIME and CONTAINER formats (Source: [inputs.md](../../docs/inputs.md))
5. Input Types (Narrative Mentions) – Key presses, finger presses, webcam stream (Source: [inputs.md](../../docs/inputs.md))
6. Mesh Event Propagation – Keypress event heard by container and other nodes (Source: [inputs.md](../../docs/inputs.md))
7. Visual Output Redirection – CORE redirects drawing events to container when ready (Source: [inputs.md](../../docs/inputs.md))
8. Bi-directional Graphics & Input – Container may bridge hardware and return data from inputs (Source: [display (container).md](../../docs/display%20(container).md))
9. Facade Mapping – Logical remapping of underlying functions for mesh/state/file interactions (Source: [Facade.md](../../docs/Facade.md))

## Flow Summary (Textual)
NODE/Device → (Driver/GPIO) → RUNTIME → Translator → CONTAINER Portal → Mesh Event Broadcast → Other RUNTIME / NODE listeners (Source: [inputs.md](../../docs/inputs.md))

## Incomplete Blocks

Incomplete: Canonical Event Taxonomy
Needed:
- Enumerated list of event categories (keyboard, pointer, touch, stream, etc.) – only examples given
- Naming conventions for event payloads
Candidate Sources: [inputs.md](../../docs/inputs.md), future input spec docs (TODO: discover)

Incomplete: Translator Interface Specification
Needed:
- Required functions (e.g., normalize(), encode(), dispatch()) – not defined
- Error handling / fallback pathways
Candidate Sources: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md)

Incomplete: Input Permission Model
Needed:
- Access control rules when sharing inputs across mesh
- Revocation / isolation procedures
Candidate Sources: [inputs.md](../../docs/inputs.md), [Facade.md](../../docs/Facade.md)

Incomplete: Event Ordering Guarantees
Needed:
- Statement of ordering (if any) for simultaneous events across nodes
- Conflict resolution strategy
Candidate Sources: [inputs.md](../../docs/inputs.md)

Incomplete: Stream Input Handling
Needed:
- Distinction between continuous (webcam) vs discrete (key press) events
- Buffering or rate control guidelines
Candidate Sources: [inputs.md](../../docs/inputs.md)

Verbatim scope: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md), [Facade.md](../../docs/Facade.md) only.
