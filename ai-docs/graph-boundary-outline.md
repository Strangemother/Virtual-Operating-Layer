Status: Draft
Last-Touched: 2025-09-13
# Graph Concept Boundary Outline

Purpose: Consolidate sourced roles of pointer, stepper, node compass, tape, and related naming docs without synthesizing new semantics.

## Components & Roles
Pointer – Header element executing SES and graph mutations; naming variants convey previous|current or forward chaining; may return next pointer(s). (Source: docs/core/graph pointer.md)
Stepper – Walker resolving next pointer, providing context frame, executing sequential actions, may freeze pointer during async operations. (Source: docs/core/graph stepper.md)
Pointer Tape (Tape) – Ordered sequence of keys representing execution walk; recites an 'app'. (Source: docs/core/graph pointer.md)
Node Compass – Internal vector path resolution map to validate or direct path based on history vectors and sums; supports branching constraints. (Source: docs/core/graph node compass.md)
Context Frame – Current view (persistent store address, live graph, temporary memory, functions/API, pointer knowledge) supplied to pointers. (Source: docs/core/frame-context.md)

## Naming-Related Files (Not Yet Integrated Here)
- graph key names.md (Source: docs/core/graph key names.md) – NOT REVIEWED in this outline.
- graph functions.md (Source: docs/core/graph functions.md) – Reviewed only for SES presence.
- graph stepper.md – Incorporated above.

## Observed Interactions (Descriptive Only)
- Stepper supplies Context Frame to Pointer (Source: docs/core/frame-context.md, docs/core/graph stepper.md)
- Pointer may yield next pointer(s) influencing subsequent Stepper iteration (Source: docs/core/graph pointer.md)
- Compass constrains valid path transitions given historical accumulation (Source: docs/core/graph node compass.md)
- Tape is an externalized linear record of traversed keys (Source: docs/core/graph pointer.md)

## Separation vs Overlap Signals
- Pointer naming schemes embed previous and/or next keys (Source: docs/core/graph pointer.md)
- Compass uses vector sums/mod to direct path; distinct mechanism from naming scheme (Source: docs/core/graph node compass.md)
- Stepper machine role vs stepper loop separation unresolved naming (“machine” vs “stepper machine” vs “stepper”). (Source: docs/core/graph stepper.md)

## Incomplete Blocks
Incomplete: graph key names integration
Needed:
- Enumerated key naming conventions (beyond previous|current examples)
- Distinction (if any) between key naming file intent and pointer naming conventions
Candidate Sources: docs/core/graph key names.md, docs/core/graph pointer.md

Incomplete: stepper machine naming normalization
Needed:
- Canonical term for 'machine parent' vs 'stepper machine'
- Criteria for when a stepper runs inside vs outside machine
Candidate Sources: docs/core/graph stepper.md

Incomplete: compass vs tape boundary
Needed:
- Explicit statement whether compass-derived direction alters tape recording
- Mechanism (if any) for invalid path signaling into tape generation
Candidate Sources: docs/core/graph node compass.md, docs/core/graph pointer.md

Incomplete: pointer async freeze semantics
Needed:
- Conditions for freezing pointer
- Effect on context frame updates
Candidate Sources: docs/core/graph stepper.md

Verbatim scope: docs/core/graph pointer.md, docs/core/graph stepper.md, docs/core/graph node compass.md, docs/core/frame-context.md only.
