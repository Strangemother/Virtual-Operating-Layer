# Frame Model Skeleton (Consolidated Extraction)
Status: Draft
Last-Touched: 2025-11-30
Depends-On: docs/core/frame-context.md, root-monolith-frame-switching-extraction.md, root-monolith-memory-module-extraction.md
Verbatim scope: docs/core/frame-context.md; root-monolith-frame-switching-extraction.md; root-monolith-memory-module-extraction.md

## Purpose
Consolidates explicit statements about frames, context, and frame switching from core and root-monolith sources. All unresolved mechanics documented in gap-priority-matrix.md (#17, #18).

## Sourced Statements (Frame Context)
1. A Frame acts as a stepper's current view of the system with knowledge required to run incoming pointers. (Source: docs/core/frame-context.md)
2. The Context hosts the Frame and all associated parts. (Source: docs/core/frame-context.md)
3. A Context lives across the life of the stepper as it walks a subset graph. (Source: docs/core/frame-context.md)
4. All pointers and SES may view the context as the active system and use components and stored data for tooling. (Source: docs/core/frame-context.md)
5. Mandatory context items: persistent store (memory) address; live graph; temporary (contextual) memory; functions/methods/root API; pointer knowledge. (Source: docs/core/frame-context.md)
6. A stepper provides a Context to the pointer when initialised. (Source: docs/core/frame-context.md)
7. The pointer (before execution) may utilise any information within the context and is functionally landlocked. (Source: docs/core/frame-context.md)
8. The Pointer, Stepper, and SES may alter some context elements; additional data applied is pushed to a newer frame relative to the pointer. (Source: docs/core/frame-context.md)
9. The context has purview of all frames across all pointers within its stepper machine. (Source: docs/core/frame-context.md)

## Sourced Statements (Frame Switching Extraction)
10. Frame switching references a potential transition from frame to a timeline becoming a linear memory/stack construct. (Source: root-monolith-frame-switching-extraction.md; docs/root-monolith/Frame Switching.md)
11. Quantum frame precedes Command frame; roles undefined. (Source: root-monolith-frame-switching-extraction.md; docs/root-monolith/Frame Switching.md)
12. Frame switching affects how memory or operations are linearized; address recalculation not defined. (Source: root-monolith-frame-switching-extraction.md; docs/root-monolith/Frame Switching.md)

## Sourced Statements (Memory Module Extraction)
13. Acquisition units perform: frame orientation → block processing → block mapping. (Source: root-monolith-memory-module-extraction.md; docs/root-monolith/memory-module.md)
14. Non-acquisition units exist and do not perform acquisition tasks. (Source: root-monolith-memory-module-extraction.md; docs/root-monolith/memory-module.md)

## Observed Consolidated Concepts (Names Only)
- Frame (current view)
- Context (host lifecycle)
- Stepper (provider of context)
- Acquisition Unit (pipeline includes frame orientation)
- Quantum Frame / Command Frame (sequence reference)
- Timeline (linearization construct)

## Cross-References
- See: sections/glossary.md (Frame Orientation, Quantum Frame, Command Frame, Acquisition Unit).
- Related gaps: Frame Switching Authorization (#18), Acquisition-Triggered Frame Orientation (#17), Command Invocation Lifecycle (#19) (Source: gap-priority-matrix.md)

## Incomplete Blocks (Reaffirmed Only)
```
Incomplete: Frame Type Taxonomy
Needed: Full list of frame types; attributes; allowed transitions.
Candidate Sources: docs/core/frame-context.md, docs/root-monolith/Frame Switching.md
```
```
Incomplete: Frame Linearization Criteria
Needed: Conditions turning frame context into linear timeline/stack; ordering guarantees; address impact.
Candidate Sources: docs/root-monolith/Frame Switching.md, docs/core/frame-context.md
```
```
Incomplete: Acquisition Pipeline Ordering
Needed: Whether frame orientation is prerequisite or side-effect for mapping; concurrency implications.
Candidate Sources: docs/root-monolith/memory-module.md, docs/core/frame-context.md
```

## Notes
- No synthesis beyond verbatim consolidation; unresolved semantics remain external.
- Future: If taxonomy becomes explicit, promote to Working-Spec after glossary confirmation.
