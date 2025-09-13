# Root Monolith – Phase Sequence (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/phases.md
Verbatim scope: docs/root-monolith/phases.md

## Purpose
Capture explicit ordered initialization items from phase description without adding hierarchy beyond listed order.

## Sourced Ordered Items
1. Wake from magic number hand-off or simulated power-on event (address pointer to spawn exe process). (Source: docs/root-monolith/phases.md)
2. Perform (currently undefined) power on / pin / register tests (monolith functionality). (Source: docs/root-monolith/phases.md)
3. Run root binary and set up blank space for incoming functions (wipe runtime). (Source: docs/root-monolith/phases.md)
4. Create root language, core method and class setup (type, ints, pointer object, system/registers functions). (Source: docs/root-monolith/phases.md)
5. Load virtual-ram functions for writing to memory. (Source: docs/root-monolith/phases.md)
6. Enable/install enforced code (first-load AOP extensions/updates baked in). (Source: docs/root-monolith/phases.md)
7. Load text print, disk tools, and other fundamental functions. (Source: docs/root-monolith/phases.md)
8. Read and register house events (wake state, pin interrupts). (Source: docs/root-monolith/phases.md)
9. Perform last call changes using memory, root tools, and init config in register. (Source: docs/root-monolith/phases.md)
10. Load first user tape into memory (sources: flash SD, network, baked bin, real host file, register). (Source: docs/root-monolith/phases.md)
11. Read functions and continue tape loadout. (Source: docs/root-monolith/phases.md)
12. Prepare for loading complex tools: Event Stack, Filesystem, Graph based memory, multiprocessing, REPL, GUI. (Source: docs/root-monolith/phases.md)

## Observed Concept Elements (Names Only)
- User tape
- Enforced code
- Virtual RAM functions
- House events
- Event Stack preparation

## Cross-References
- Glossary stubs: User Tape, Enforced Code, Virtual RAM Slice (See: sections/glossary.md)
- Related gaps: Phase 0 Ordered Requirements; Module Dependency Graph (root-monolith-triage.md)

## Incomplete Blocks
```
Incomplete: Mandatory vs Optional Phase Steps
Needed: Identification of required minimal subset; recovery path if optional step fails.
Candidate Sources: docs/root-monolith/phases.md, docs/root-monolith/phase-0.md
```
```
Incomplete: User Tape Validation
Needed: Integrity checks; partial load handling; restart semantics.
Candidate Sources: docs/root-monolith/phases.md, docs/root-monolith/security research.md
```
```
Incomplete: Enforced Code Update Policy
Needed: Trigger events for protected updates; rollback conditions; signing or verification process.
Candidate Sources: docs/root-monolith/phases.md, docs/root-monolith/security research.md
```

## Notes
- Order preserved verbatim; no dependency inference beyond listed sequence.

Backlink: Referenced by root-monolith-triage.md and root-monolith-index.md
