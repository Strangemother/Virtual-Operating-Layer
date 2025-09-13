# Root Monolith – Step Addresses & Layers (Extraction)
Status: Draft
Owner: VOL Extraction Agent
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/step addresses and layers.md
Verbatim scope: docs/root-monolith/step addresses and layers.md

## Purpose (Sourced)
The source text enumerates a mapping between short alphabetic / symbolic tokens (e.g., `a`, `b`, `f`, `l`, `F`, `I`, `X`, `Y`, `Z`, `T`, `J`) and conceptual domains described as "another space of memory (tree structure)" or variation on "index space domain". (Source: docs/root-monolith/step addresses and layers.md)

## Sourced Elements
- The document presents a vertical list pairing lower-case single-letter identifiers (`a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`) with the repeated phrase: "another space of memory ( tree structure )" (punctuation and spacing as in source). (Source: docs/root-monolith/step addresses and layers.md)
- At `f` a parenthetical clarifier exists: `query access location in memory small space` preceding the repeated phrase. (Source: docs/root-monolith/step addresses and layers.md)
- After the lower-case sequence, there is a section headed `UPPER CASE` introducing capital letters and additional symbolic identifiers. (Source: docs/root-monolith/step addresses and layers.md)
- Capital identifiers include: `F`, `I`, `J`, `K`, `L`, `Q`, `T`, `X`, `Y`, `Z`. (Source: docs/root-monolith/step addresses and layers.md)
- Some capital identifiers have appended descriptors: `T time frame`, `J jump frame`, `Y sequence memory graph`, `Z series memory graph`. (Source: docs/root-monolith/step addresses and layers.md)
- The symbol set also introduces domain descriptors: `index space domain`, `expanded space domain`, `family space domain`, `extended family space domain`, `related family space domain`, `dictionary space domain`. (Source: docs/root-monolith/step addresses and layers.md)
- A repeated placeholder-like phrase "( etc resolve handling )" appears after several domain descriptors, suggesting unresolved handling semantics. (Source: docs/root-monolith/step addresses and layers.md)

## Observed Structure
- Two-tier identifier scheme: lower-case vs upper-case / symbolic appears to demarcate different semantic or hierarchical layers, but the source does not explicitly define the distinction. (Source: docs/root-monolith/step addresses and layers.md)
- Multiple domain labels (index, expanded, family, extended family, related family, dictionary) are enumerated without explicit relational or transformational rules between them. (Source: docs/root-monolith/step addresses and layers.md)
- Time and control flow concepts (`T time frame`, `J jump frame`) are interleaved with memory/graph domain concepts, implying a shared addressing namespace or multiplexing, but this is not confirmed in text. (Source: docs/root-monolith/step addresses and layers.md)

## Extracted Term Candidates (Require Glossary Stubs)
- time frame (Source: docs/root-monolith/step addresses and layers.md)
- jump frame (Source: docs/root-monolith/step addresses and layers.md)
- sequence memory graph (Source: docs/root-monolith/step addresses and layers.md)
- series memory graph (Source: docs/root-monolith/step addresses and layers.md)
- index space domain (Source: docs/root-monolith/step addresses and layers.md)
- expanded space domain (Source: docs/root-monolith/step addresses and layers.md)
- family space domain (Source: docs/root-monolith/step addresses and layers.md)
- extended family space domain (Source: docs/root-monolith/step addresses and layers.md)
- related family space domain (Source: docs/root-monolith/step addresses and layers.md)
- dictionary space domain (Source: docs/root-monolith/step addresses and layers.md)

## Incomplete Blocks
```
Incomplete: Identifier hierarchy semantics
Needed: Definition of functional difference between lower-case vs upper-case identifiers; ordering guarantees; collision or overlap rules.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/root-monolith/Frame Switching.md, TODO: discover
```
```
Incomplete: Domain transformation rules
Needed: How index/expanded/family/extended family/related family/dictionary domains relate (subset, superset, versioning, lineage?); transition triggers; resolution precedence.
Candidate Sources: docs/root-monolith/memory-module.md, docs/core/structure.md, TODO: discover
```
```
Incomplete: Temporal vs structural address multiplexing
Needed: Whether time frame (`T`) and jump frame (`J`) occupy same address class as memory graph identifiers; conflict resolution; lookup path.
Candidate Sources: docs/root-monolith/Frame Switching.md, docs/core/frame-context.md, TODO: discover
```
```
Incomplete: Sequence vs series memory graph distinction
Needed: Criteria distinguishing `sequence memory graph` from `series memory graph`; traversal semantics; lifecycle.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/core/Procedure Graph.md, TODO: discover
```
```
Incomplete: Query access location semantics (f)
Needed: Scope of "small space" referenced; latency or caching implications; mapping to broader memory graph.
Candidate Sources: docs/root-monolith/memory-module.md, docs/memory/*, TODO: discover
```
```
Incomplete: Placeholder resolution handling
Needed: Meaning of phrase "( etc resolve handling )"; indicates unimplemented handlers or variance list?; required handler categories.
Candidate Sources: docs/root-monolith/commands.md, docs/core/system core.md, TODO: discover
```

## Notes
- Source provides enumerations without normative behavioral contracts; extraction preserves enumeration and flags all implicit gaps. (Source: docs/root-monolith/step addresses and layers.md)
- No attempt has been made to unify these identifiers with existing graph pointer / compass / stepper docs pending explicit mapping evidence. (Source: docs/root-monolith/step addresses and layers.md)
- Glossary stubs created for: time frame, jump frame, sequence memory graph, series memory graph, and all *space domain labels (See: sections/glossary.md). (Source: docs/root-monolith/step addresses and layers.md)

