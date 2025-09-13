---
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: boot.md, core/boot.md, zero-suite.md, the loop.md, top level.md
---
# Boot Sequence Diagram (Textual Stub)

Purpose: Provide linear ordered list of explicitly referenced boot / startup stages without adding unstated transitions.

## Linear Stage List (Sourced Statements Aggregation)
1. Boot zim sem executes store using SEM TAPE into new memory reference (mcom) (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
2. mcom holds loading step values as a TAPE string (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
3. Config and kernel address written to mcom TAPE location by boot sem (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
4. Pointer 0 executable unpacked and loaded into primary allowed memory (Source: [zero-suite.md](../../docs/core/zero-suite.md))
5. Pointer steps into position 0 (default) then magic value sends pointer to first position (Source: [zero-suite.md](../../docs/core/zero-suite.md))
6. During zero state there is no graph, pointer stepper, or OS (Source: [zero-suite.md](../../docs/core/zero-suite.md))
7. Base language construct stepping from turing complete bios to +1 layer initialises first run routines (Source: [top level.md](../../docs/top%20level.md); [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
8. Loop walks a tree of pointers; each pointer executes code (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md); [the loop.md](../../docs/the%20loop.md))

## Observed Entities (Names Only)
* boot zim sem
* SEM TAPE
* mcom
* config / kernel address
* pointer 0 executable
* magic value
* zero state
* bios
* loop

## Incomplete Blocks

Incomplete: Stage Boundaries
Needed:
- Explicit delineation of when zero state ends and first run routines begin
- Criteria to declare loop start readiness
Candidate Sources: [boot.md](../../docs/boot.md), [zero-suite.md](../../docs/core/zero-suite.md), [top level.md](../../docs/top%20level.md)

Incomplete: Error / Retry Flow
Needed:
- Behavior on invalid SEM TAPE
- Fallback if pointer 0 unpack fails
Candidate Sources: [boot.md](../../docs/boot.md), [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: BIOS to Loop Handoff Markers
Needed:
- Observable marker(s) signaling transition to primary loop
- Memory sanitation steps between phases
Candidate Sources: [top level.md](../../docs/top%20level.md), [the loop.md](../../docs/the%20loop.md)

Incomplete: Timing Targets
Needed:
- Allocation of <5s target across stages (if any specified later)
- Measurement reference points
Candidate Sources: [boot.md](../../docs/boot.md)

Verbatim scope: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md), [zero-suite.md](../../docs/core/zero-suite.md), [top level.md](../../docs/top%20level.md), [Procedure Graph.md](../../docs/core/Procedure%20Graph.md), [the loop.md](../../docs/the%20loop.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 1.
