# Root Monolith – Frame Switching (Extraction)
Status: Draft
Owner: VOL Extraction Agent
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/Frame Switching.md
Verbatim scope: docs/root-monolith/Frame Switching.md

## Purpose (Sourced)
The source discusses mechanisms and conceptual states related to switching frames, including potential for a timeline transition from a frame to a linear memory or stack structure, and references to a "Quantum frame" and "Command frame" sequence. (Source: docs/root-monolith/Frame Switching.md)

## Sourced Elements
- References a transition concept: moving from one frame context into a "timeline" which becomes a linear memory / stack construct. (Source: docs/root-monolith/Frame Switching.md)
- Mentions a sequential ordering implication from "Quantum frame" to "Command frame" without defining intermediate validation or synchronization. (Source: docs/root-monolith/Frame Switching.md)
- Notes layered or staged nature of frames implying multiple distinct frame classes. (Source: docs/root-monolith/Frame Switching.md)
- Indicates frame switching affects how memory or operations are linearized but does not define address recalculation or persistence semantics. (Source: docs/root-monolith/Frame Switching.md)

## Observed Structure
- Frame switching appears to alter both execution context and memory representation (stack vs non-linear), but lacks explicit triggers or control signals. (Source: docs/root-monolith/Frame Switching.md)
- "Quantum" vs "Command" frames suggest categorization (possibly preparatory vs executable), yet no explicit roles or lifecycle hooks are stated. (Source: docs/root-monolith/Frame Switching.md)

## Extracted Term Candidates (Require Glossary Stubs)
- frame switching (Source: docs/root-monolith/Frame Switching.md)
- Quantum frame (Source: docs/root-monolith/Frame Switching.md)
- Command frame (Source: docs/root-monolith/Frame Switching.md)
- timeline (as frame transition construct) (Source: docs/root-monolith/Frame Switching.md)

## Incomplete Blocks
```
Incomplete: Frame class taxonomy
Needed: Enumeration of all frame types; required attributes per type; allowed transitions; invariants.
Candidate Sources: docs/core/frame-context.md, docs/root-monolith/graph-walk.md, TODO: discover
```
```
Incomplete: Quantum→Command transition semantics
Needed: Preconditions; failure modes; atomicity guarantees; rollback strategy.
Candidate Sources: docs/core/system core.md, docs/root-monolith/commands.md, TODO: discover
```
```
Incomplete: Timeline linearization rules
Needed: Criteria for when non-linear graph becomes linear stack; ordering resolution for concurrent nodes; memory address adjustments.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/core/Procedure Graph.md, TODO: discover
```
```
Incomplete: Persistence across frame switch
Needed: What state is preserved vs reinitialized; identity continuity; reference invalidation policy.
Candidate Sources: docs/core/structure.md, docs/root-monolith/memory-module.md, TODO: discover
```
```
Incomplete: Control signaling mechanism
Needed: How a frame switch is requested, queued, authorized; priority handling; conflict arbitration.
Candidate Sources: docs/root-monolith/commands.md, docs/core/system core.md, TODO: discover
```

## Notes
- No numerical or algorithmic detail provided; extraction limits itself to conceptual references. (Source: docs/root-monolith/Frame Switching.md)
- Pending mapping with existing frame-context core doc once cross-evidence emerges. (Source: docs/root-monolith/Frame Switching.md)
- Glossary stubs added: Quantum frame, Command frame (See: sections/glossary.md). (Source: docs/root-monolith/Frame Switching.md)

Backlink: Referenced by command-frame-lifecycle-skeleton.md
