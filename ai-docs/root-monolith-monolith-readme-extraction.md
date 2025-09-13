# Root Monolith – Readme Functional Inventory (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/readme.md
Verbatim scope: docs/root-monolith/readme.md

## Purpose
Capture enumerated functional components, input/output stream models, and graph key references.

## Sourced Functional Components
- Base language & bedrock tools: multiprocessing, async execution, REPL command entry. (Source: docs/root-monolith/readme.md)
- Root core modules: printing, UART & ping, exception handling, language preprocessor, REPL receiver, websocket REPL streaming, multi-processor allocation & source execution, runtime module loadouts, early config management, graph methods, realtime clock integration & scheduler. (Source: docs/root-monolith/readme.md)
- Container / debug output elements: text renderer (stdout), debug printing, REPL output, graphics command/response, graph render, register view, disassembler loads, top info. (Source: docs/root-monolith/readme.md)

## Input Stream Model
1. Input stream is unending for client REPL; stores results into walking register until termination. (Source: docs/root-monolith/readme.md)
2. Each char stored; input-session key stepped; termination yields next graph step, execution, or exception. (Source: docs/root-monolith/readme.md)
3. Each input char steps graph yielding data, pointer, or executor (progressive stepping analogous to forward typing). (Source: docs/root-monolith/readme.md)
4. System continuously yields information through output stream; user subscribed to both directions. (Source: docs/root-monolith/readme.md)

## Graph & Memory Notes
- Graph key 0 start description (protected start point). (Source: docs/root-monolith/readme.md)
- Data kept as flat graph; edge connections bridge grains to form readable bytes. (Source: docs/root-monolith/readme.md)
- Particle cold-store movement via age/access (entropy) with RAM reintroduction when needed. (Source: docs/root-monolith/readme.md)
- No top-level distinction between RAM and Disk memory (future methodology). (Source: docs/root-monolith/readme.md)

## Output Stream & Container
- Headless monolith: output via REPL debugger stream + fundamental text display drivers. (Source: docs/root-monolith/readme.md)
- Container drivers enumerate rendering & debug surfaces (see Functional Components). (Source: docs/root-monolith/readme.md)

## Observed Concept Elements (Names Only)
- Walking register
- Input-session key
- Forward stepping input execution
- Cold-store entropy of particles
- Headless container debug stream

## Cross-References
- Glossary stubs: Graph Key 0, User Tape (indirect via phase documents), Virtual RAM Slice (from comprehensive) (See: sections/glossary.md)
- Related gaps: Input Stream Stepping Semantics (root-monolith-triage.md)

## Incomplete Blocks
```
Incomplete: Input Termination Criteria
Needed: Specific termination key(s); multi-line or composite command framing; partial command recovery.
Candidate Sources: docs/root-monolith/readme.md, docs/root-monolith/commands.md
```
```
Incomplete: Walking Register Structure
Needed: Data fields maintained per input-session key; persistence rules; maximum size constraints.
Candidate Sources: docs/root-monolith/readme.md
```
```
Incomplete: Cold-Store Entropy Policy
Needed: Access age thresholds; rehydration triggers; collision handling for returning particles.
Candidate Sources: docs/root-monolith/readme.md, docs/fs/File System.md
```

## Notes
- Enumeration only; no structural schema introduced.
 
Backlink: Referenced by root-monolith-triage.md and root-monolith-index.md
Additional Backlink: Referenced by input-lifecycle-skeleton.md
