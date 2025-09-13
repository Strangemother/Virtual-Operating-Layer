# See: [graph-overview.md](graph-overview.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: interface-input-events.md
# Interface Event Taxonomy (Extraction Draft)

Purpose: List only explicitly mentioned or implied event categories without inventing new names.

## Extracted Mentions
1. Keypress (event rendered by container; heard by other nodes) (Source: [inputs.md](../../docs/inputs.md))
2. Finger presses (touch-like reference; generic) (Source: [inputs.md](../../docs/inputs.md))
3. Webcam stream (continuous input example) (Source: [inputs.md](../../docs/inputs.md))
4. Drawing events (CORE redirects drawing events to CONTAINER) (Source: [inputs.md](../../docs/inputs.md))
5. Render commands / streams (visual pipeline ingestion) (Source: [display (container).md](../../docs/display%20(container).md))
6. Audio (as additional bridged content) (Source: [display (container).md](../../docs/display%20(container).md))
7. Hardware input (Peripherals) (Source: [display (container).md](../../docs/display%20(container).md))
8. Software input (RPC feedback / session info) (Source: [display (container).md](../../docs/display%20(container).md))

## Provisional Category Labels (Directly Referring to Source Phrases)
* Keyboard (keypress) (Source: [inputs.md](../../docs/inputs.md))
* Touch (finger presses) (Source: [inputs.md](../../docs/inputs.md))
* Video Stream (webcam stream) (Source: [inputs.md](../../docs/inputs.md))
* Graphics Output Events (drawing events, render commands) (Source: [inputs.md](../../docs/inputs.md); [display (container).md](../../docs/display%20(container).md))
* Audio Input/Output (audio) (Source: [display (container).md](../../docs/display%20(container).md))
* Hardware Peripheral Input (hardware input) (Source: [display (container).md](../../docs/display%20(container).md))
* Software / RPC Feedback (software input) (Source: [display (container).md](../../docs/display%20(container).md))

## Incomplete Blocks

Incomplete: Canonical Event Category List
Needed:
- Confirmation of accepted category names vs narrative examples
- Inclusion/exclusion rules for stream vs discrete
Candidate Sources: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md)

Incomplete: Event Payload Schema
Needed:
- Field names for keypress (e.g., code, repeat?) – none listed
- Structure for webcam stream metadata (resolution, frame rate)
Candidate Sources: [inputs.md](../../docs/inputs.md), future interface specs (TODO: discover)

Incomplete: Event Translation Mapping
Needed:
- Translator normalization steps per category
- Error / fallback behaviors
Candidate Sources: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md)

Incomplete: Ordering & Timing Guarantees
Needed:
- Delivery ordering semantics across mesh nodes
- Clock sync or timestamping approach
Candidate Sources: [inputs.md](../../docs/inputs.md)

Incomplete: Security & Permission Model
Needed:
- Access control for peripheral vs software inputs
- Revocation mechanism
Candidate Sources: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md)

Verbatim scope: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 3.
