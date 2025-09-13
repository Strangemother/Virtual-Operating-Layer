# Root Monolith – Memory Module (Extraction)
Status: Draft
Owner: VOL Extraction Agent
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/memory-module.md
Verbatim scope: docs/root-monolith/memory-module.md

## Purpose (Sourced)
The source outlines conceptual components related to acquiring, addressing, and mapping memory units, distinguishing acquisition units from non-acquisition units, and referencing functional / data graph separation. (Source: docs/root-monolith/memory-module.md)

## Sourced Elements
- Mentions three steps for acquisition units: (1) orient frame; (2) process memory block; (3) map block. (Source: docs/root-monolith/memory-module.md)
- States a separation between acquiring memory units and non-acquiring memory units, with acquisition units performing mapping/orientation tasks. (Source: docs/root-monolith/memory-module.md)
- References both "data graph" and "function graph" implying dual graph structures in memory representation. (Source: docs/root-monolith/memory-module.md)
- Notes an interaction where memory acquisition relates to block processing before mapping into a broader structure; explicit mapping data format not provided. (Source: docs/root-monolith/memory-module.md)
- Indicates presence of units that do not perform acquisition but presumably consume or reference mapped memory; details absent. (Source: docs/root-monolith/memory-module.md)

## Observed Structure
- Implied pipeline: Frame orientation → Block processing → Block mapping (for acquisition units). (Source: docs/root-monolith/memory-module.md)
- Dual graph model (data vs function) consistent with separation observed in other root-monolith materials. (Source: docs/root-monolith/memory-module.md)
- Role distinction suggests modular responsibilities but lacks lifecycle, scheduling, or error-handling semantics. (Source: docs/root-monolith/memory-module.md)

## Extracted Term Candidates (Require Glossary Stubs)
- acquisition unit (Source: docs/root-monolith/memory-module.md)
- non-acquisition unit (Source: docs/root-monolith/memory-module.md)
- frame orientation (Source: docs/root-monolith/memory-module.md)
- block mapping (Source: docs/root-monolith/memory-module.md)

## Incomplete Blocks
```
Incomplete: Acquisition unit contract
Needed: Required inputs (block size? address source?), outputs (mapping descriptor?), side effects, idempotency.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/core/structure.md, TODO: discover
```
```
Incomplete: Frame orientation semantics
Needed: Definition of "orient frame" operation; relation to frame-context; ordering guarantees relative to mapping.
Candidate Sources: docs/root-monolith/Frame Switching.md, docs/core/frame-context.md, TODO: discover
```
```
Incomplete: Block processing details
Needed: What constitutes processing (validation, transformation?); error states; retry or discard behavior.
Candidate Sources: docs/core/system core.md, docs/root-monolith/commands.md, TODO: discover
```
```
Incomplete: Data vs function graph mapping
Needed: Whether a memory block maps into one or both graphs; synchronization strategy; conflict detection.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/core/Procedure Graph.md, TODO: discover
```
```
Incomplete: Non-acquisition unit role
Needed: Responsibilities; how they reference mapped blocks; permission semantics; read vs mutate constraints.
Candidate Sources: docs/root-monolith/step addresses and layers.md, docs/fs/File System.md, TODO: discover
```

## Notes
- Source lacks quantitative or structural specification (no schema, no address format). (Source: docs/root-monolith/memory-module.md)
- Extraction preserves original separation without inferring runtime mechanics. (Source: docs/root-monolith/memory-module.md)
- Glossary stubs added: acquisition unit, non-acquisition unit, frame orientation, block mapping (See: sections/glossary.md). (Source: docs/root-monolith/memory-module.md)
