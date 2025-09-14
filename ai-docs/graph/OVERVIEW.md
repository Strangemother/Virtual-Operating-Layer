# Procedure Graph – Consolidated Overview
Status: Draft
Owner: TODO
Last-Touched: 2025-09-13
Depends-On: ../../docs/core/Procedure Graph.md, ../../docs/core/graph pointer.md, ../../docs/core/graph stepper.md, ../../docs/core/graph key names.md, ../../docs/core/graph node compass.md, ../../docs/core/graph functions.md
Supersedes: (Section-level) those individual concept definitions for high-level orientation; originals remain canonical detailed sources.

Verbatim scope: docs/core/Procedure Graph.md, docs/core/graph pointer.md, docs/core/graph stepper.md, docs/core/graph key names.md, docs/core/graph node compass.md, docs/core/graph functions.md

> All normative statements below are direct condensations. Gaps are explicitly flagged. No new behavior introduced.

## 1. Core Elements
- Pointer: A header element executed by the stepper; may yield another pointer, memory, or other functional work (Source: docs/core/graph pointer.md)
- Stepper: Walks the graph, resolving keys to next steps and executing pointer functionality each frame/step (Source: docs/core/graph stepper.md)
- Function / SES: Self executing source inside a pointer; may be bytes/binary/any language; can be compiled on-the-fly and sandboxed (Source: docs/core/graph functions.md)
- Key Name (Address): Encodes previous|current|next (or variants) enabling forward resolution without inspecting pointer content (Source: docs/core/graph key names.md)
- Internal Compass: Per‑node mechanism using summed path vectors to direct valid outbound edges based on history (Source: docs/core/graph node compass.md)

## 2. Execution Flow (High-Level)
1. Stepper loads initial address (e.g., `0x0`) (Source: docs/core/graph stepper.md)
2. Reads key (name) to determine next step without necessarily executing pointer body first (Source: docs/core/graph key names.md)
3. Executes pointer (function/SES) which may modify context, memory, graph, or return next addressing vector (Sources: docs/core/graph pointer.md, docs/core/graph functions.md)
4. Obtains next address (from name parsing or pointer return) and repeats (Sources: docs/core/graph key names.md, docs/core/graph stepper.md)

Incomplete: Ordering Guarantees
Needed:
- Explicit contract whether name-based next resolution precedes pointer execution in all cases
- Error handling semantics when name encodes invalid forward key
- Idempotency or retry behavior of pointer execution across frames
Candidate Sources: docs/core/Procedure Graph.md, docs/core/structure.md, TODO: discover additional runtime coordination docs

## 3. Addressing & Naming
- Names may include forward key(s) to avoid inspecting pointer body (Source: docs/core/graph pointer.md)
- Patterns support previous|current|next or compressed vector forms `[layer,graph,pos]` segments (Source: docs/core/graph key names.md)
- Vector components: layer bit, graph identity bit, position bit (Source: docs/core/graph key names.md)
- Names can dynamically change to reflect graph updates (Source: docs/core/graph key names.md)
- Friendly names may alias unreadable computed names (Source: docs/core/graph key names.md)

Incomplete: Collision-Free Formula
Needed:
- Stated formula for computing next key from current without collisions (open TODO noted) (Source: docs/core/graph key names.md)
- Definition of limits/thresholds for vector ranges
Candidate Sources: docs/core/graph key names.md, docs/core/Procedure Graph.md

## 4. Pointer Characteristics
- Can live off the walker graph yet alter shared execution space (SES) content (Source: docs/core/graph pointer.md)
- May contain: bytes, compiled source, other addresses, streams, or live inputs (Source: docs/core/graph pointer.md)
- Execution may be instantaneous for in‑memory content; remote/persistent services introduce delay (Source: docs/core/graph pointer.md)
- Returns may include addresses altering flow (Source: docs/core/graph pointer.md)

Incomplete: Pointer Return Contract
Needed:
- Clarify precedence: name-encoded next vs returned address when both present
- Whether multiple candidate next addresses are allowed concurrently
Candidate Sources: docs/core/graph pointer.md, docs/core/graph stepper.md

## 5. Stepper & Machine Hierarchy
Hierarchy (verbatim condensation) (Source: docs/core/graph stepper.md):
- Root (primary host runtime) generates Machine Parents
  - Machine Parent builds Stepper Machines and provides facades & subset graph
    - Stepper Machine manages frequency/allowances, injects post-step routines
      - Stepper executes pointer resolution & graph walking
        - Pointer: actuator executing SES and yielding potential next addresses

Additional properties:
- Stepper functions as thin context head per step (Source: docs/core/graph stepper.md)
- Async/frozen states possible while awaiting other actions (Source: docs/core/graph stepper.md)
- Stepper Machines coexist, communicating across membranes for timing/task sharing (Source: docs/core/graph stepper.md)

Incomplete: Machine Construction Unit Naming
Needed:
- Canonical name for 'kernel synthetic cell generation unit' (placeholder cited) (Source: docs/core/graph stepper.md)
Candidate Sources: docs/core/kernel.md, docs/core/system core.md

## 6. Internal Compass (Path Validation)
- Uses summed vector of history path to map to restricted future outputs (Source: docs/core/graph node compass.md)
- Invalid sums produce bad/no path (Source: docs/core/graph node compass.md)
- Modulo strategy proposed for loops but collision risk noted (Source: docs/core/graph node compass.md)

Incomplete: Loop Vector Specification
Needed:
- Formal definition of loop vector behavior & modulo bounds
- Collision mitigation mechanism decision
Candidate Sources: docs/core/graph node compass.md, docs/core/Procedure Graph.md

## 7. Functions / SES Behavior
- Access to concurrent frame, contiguous memory space, local graph (Source: docs/core/graph functions.md)
- May call other vectors and return new addressing vector (Source: docs/core/graph functions.md)
- Can write values into context keyed by pointer identity (Source: docs/core/graph functions.md)

Incomplete: Sandbox & Compilation Details
Needed:
- Security isolation guarantees for sandbox execution
- Criteria for on-the-fly compilation triggers
- Supported language forms enumeration
Candidate Sources: docs/core/graph functions.md, docs/core/Procedure Graph.md

## 8. Security & Visibility
- Key names being visible may pose security issues; encryption of key names suggested (Source: docs/core/graph key names.md)

Incomplete: Key Name Encryption
Needed:
- Encryption method or abstraction
- Decryption authority (which component performs runtime decryption)
Candidate Sources: docs/core/graph key names.md, docs/core/kernel.md

## 9. Performance Considerations
- Pre-fetch or early access for persistent service pointers due to latency (Source: docs/core/graph pointer.md)

Incomplete: Caching Policy
Needed:
- Cache invalidation rules
- Consistency model for pointer content updates
Candidate Sources: docs/core/graph pointer.md, docs/core/Procedure Graph.md

## 10. Open TODO References (Collected)
- Compute collision-free next key formula (Source: docs/core/graph key names.md)
- Name changes dynamics & security implications (Source: docs/core/graph key names.md)
- Modulo loop collision mitigation (Source: docs/core/graph node compass.md)

## 11. Glossary Stubs (For Central Glossary Integration)
Pointer – As above (Source: docs/core/graph pointer.md)
Stepper – As above (Source: docs/core/graph stepper.md)
Stepper Machine – Frequency & allowance manager (Source: docs/core/graph stepper.md)
Machine Parent – Host providing facades & subset graph (Source: docs/core/graph stepper.md)
Internal Compass – History-sum based path selector (Source: docs/core/graph node compass.md)
SES (Self Executing Source) – Executable content within pointer (Source: docs/core/graph functions.md)

## 12. Status & Next Steps
Current: Draft consolidation for orientation.
Next:
- Fill incomplete blocks upon discovery of additional explicit source.
- Add cross-links back to originals from glossary once centralized.
- Prepare promotion criteria once all incomplete topics resolved or marked Evidence Exhausted.

_Incomplete blocks remain intentionally explicit. No speculative filling performed._
