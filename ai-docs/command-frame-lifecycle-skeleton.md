# Command & Frame Lifecycle Skeleton (Extraction Consolidation)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/commands.md, docs/root-monolith/Frame Switching.md, docs/root-monolith/graph-walk.md, docs/core/frame-context.md
Verbatim scope: Listed files only.

## Purpose
Aggregate explicit statements regarding command lifecycle hints, frame transitions (quantum → command → higher), and frame 0 privileges without adding phase definitions.

## Sourced Elements
### Frame Context
- Context frame holds memory, graph, temp data, APIs (baseline definition). (Source: docs/core/frame-context.md)

### Frame Switching
- Quantum frame precedes command frame; additional frames (time, jump, higher) enumerated elsewhere but semantics undefined. (Source: docs/root-monolith/Frame Switching.md)
- Frame switching references timeline linearization with no criteria specified. (Source: docs/root-monolith/Frame Switching.md)

### Commands
- Frame 0 identified as lowest (pre BIOS) area where all commands are code references. (Source: docs/root-monolith/graph-walk.md)
- Commands imply staged lifecycle; phase names not enumerated. (Source: docs/root-monolith/commands.md)
- Command handling tied to early frame orchestration (frame 0). (Source: docs/root-monolith/commands.md)

### Graph Interaction
- Command references may target data/function graph nodes via string byte references. (Source: docs/root-monolith/graph-walk.md)

## Observed Concept Elements (Names Only)
- Quantum frame
- Command frame
- Frame 0
- Frame switching / timeline linearization
- Command lifecycle (staged)

## Cross-References
- Related gaps: Frame Switching Authorization Model; Command Lifecycle Coupling; Frame Switcher Semantics (gap-index.md)
- See also: root-monolith-frame-switching-extraction.md; root-monolith-commands-extraction.md; root-monolith-graph-walk-extraction.md

## Incomplete Blocks
```
Incomplete: Frame Transition Preconditions
Needed: Conditions to advance from quantum to command frame; validation steps; rollback triggers.
Candidate Sources: docs/root-monolith/Frame Switching.md
```
```
Incomplete: Frame 0 Privilege Boundary
Needed: Exclusive operations allowed only in frame 0; security model; escalation pathway rules.
Candidate Sources: docs/root-monolith/commands.md, docs/root-monolith/graph-walk.md
```
```
Incomplete: Lifecycle Phase Naming
Needed: Enumerated command phase names; temporal ordering; failure propagation semantics.
Candidate Sources: docs/root-monolith/commands.md
```
```
Incomplete: Timeline Linearization Criteria
Needed: Factors that determine linearization necessity; impact on concurrency.
Candidate Sources: docs/root-monolith/Frame Switching.md
```

## Notes
- No attempt to unify frame taxonomy beyond explicit labels; semantic gaps remain open.

Backlink: Will be indexed in governance-index.md
