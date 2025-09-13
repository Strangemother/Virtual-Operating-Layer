# Root Monolith – Commands (Extraction)
Status: Draft
Owner: VOL Extraction Agent
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/commands.md
Verbatim scope: docs/root-monolith/commands.md

## Purpose (Sourced)
The source enumerates command-related conceptual references but lacks a formal command schema; it ties command handling to frame context (e.g., frame 0) and suggests staged or layered command processing. (Source: docs/root-monolith/commands.md)

## Sourced Elements
- Indicates a relationship between commands and an initial frame ("frame 0") context where certain operations or orchestration occur. (Source: docs/root-monolith/commands.md)
- Suggests commands interact with or traverse both data and function graphs; precise traversal mechanics are not defined. (Source: docs/root-monolith/commands.md)
- Implies staged command lifecycle but no discrete phases (parse, validate, execute, commit) are explicitly specified. (Source: docs/root-monolith/commands.md)
- References potential integration with acquisition or mapping steps indirectly (alignment with memory operations) without formal coupling contract. (Source: docs/root-monolith/commands.md)

## Observed Structure
- Commands appear to act as catalysts or triggers within an early frame, possibly setting up or initiating graph traversal or memory mapping sequences. (Source: docs/root-monolith/commands.md)
- Absence of explicit formatting, opcodes, or argument notation indicates ideation stage. (Source: docs/root-monolith/commands.md)

## Extracted Term Candidates (Require Glossary Stubs)
- command lifecycle (Source: docs/root-monolith/commands.md)
- frame 0 (Source: docs/root-monolith/commands.md)

## Incomplete Blocks
```
Incomplete: Command schema
Needed: Field list (name/opcode, arguments, idempotency flag?); serialization or in-memory representation; addressing of targets.
Candidate Sources: docs/core/system core.md, docs/root-monolith/graph-walk.md, TODO: discover
```
```
Incomplete: Frame 0 command privileges
Needed: Special capabilities vs later frames; security or isolation properties; constraints on side effects.
Candidate Sources: docs/core/frame-context.md, docs/root-monolith/Frame Switching.md, TODO: discover
```
```
Incomplete: Command lifecycle phases
Needed: Phase enumeration (parse, plan, execute, finalize?); error propagation rules; rollback semantics.
Candidate Sources: docs/core/Procedure Graph.md, docs/core/structure.md, TODO: discover
```
```
Incomplete: Graph traversal coupling
Needed: How a command selects or enumerates graph nodes; deterministic vs dynamic path selection; concurrency handling.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/core/graph pointer.md, TODO: discover
```
```
Incomplete: Memory operation integration
Needed: Whether commands can trigger acquisition/mapping; ordering with respect to acquisition units; conflict handling when memory not yet mapped.
Candidate Sources: docs/root-monolith/memory-module.md, docs/core/system core.md, TODO: discover
```

## Notes
- No attempt made to infer unmentioned structural details; all gaps explicitly surfaced. (Source: docs/root-monolith/commands.md)
- Will cross-reference with frame-switching and graph pointer materials once sufficient explicit linkage emerges. (Source: docs/root-monolith/commands.md)
- Glossary stubs added: command lifecycle, frame 0 (See: sections/glossary.md). (Source: docs/root-monolith/commands.md)

Backlink: Referenced by input-lifecycle-skeleton.md
Additional Backlink: Referenced by command-frame-lifecycle-skeleton.md
