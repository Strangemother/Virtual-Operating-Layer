---
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: graph pointer.md, graph functions.md, graph node compass.md, Procedure Graph.md, Root Fundamental apps.md
---
# Graph Subsystem Overview (Extraction Consolidation)

Purpose: Consolidate explicit statements about graph execution constructs (pointer, stepper, functions/SES, compass, naming, layering) without inventing new behaviors. Original source docs remain authoritative. This document introduces no new terms; all terms here must appear verbatim in cited sources.

## Components (Sourced Statements)
1. Pointer is a header element serving actions to the graph and the stepper; stepper walks graph and pointer executes its action (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
2. Pointer may yield a pointer, memory or other functional work (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
3. Pointer lives off the walker graph and can alter SES content of its address when executed (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
4. Pointer content may be bytes, compiled source, repointers/addresses/memory, streams or live inputs (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
5. Function or self executing source (SES) may be compiled on-the-fly; may be bytes/binary/any lang; can be executed in a sandbox; parallel or async (Source: [graph functions.md](../../docs/core/graph%20functions.md))
6. SES has visibility to concurrent frame, contiguous memory space and its local graph (Source: [graph functions.md](../../docs/core/graph%20functions.md))
7. A system has many functions; user writes linear instructions; system tokenizes to AST; execution occurs off visual thread via sockets (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
8. Fundamental application initiates two step graph A>B and repeat; acts as forever loop without loop (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
9. Lower order graph nodes maintain a special place allowing/refusing protected procedures (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
10. Protected mode analogy with security ring 0 for lower order graph nodes (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
11. Executing pointer may return redirect allowing stepper to move into another part of graph (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
12. A pointer on the graph may alter live graph state (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
13. Runtime references: Loop (walking graph/pointers), code (SES/functions), memory (runtime memory) (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
14. Primary graph executes by system demand and cannot be frozen by standard user (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
15. Stepper speed can be considered as FPS; within one upper frame a single step entered/executed (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
16. Graph may be split; parts execute remote (membrane cell / remote processor) (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
17. Graph pointer should reference its other references and be inspected upon runtime sendoff (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
18. Low-priority graph may be stored away as SES and executed on demand (graph handoff) (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
19. Multiple graphs can run asynchronously communicating through leaf nodes or membranes (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
20. Best fit inspection: sub graph should be sent to best fit hardware; pointer header references may list requirements (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
21. Graph machine: representation of a graph for entire system to acquire (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
22. Address resolver: utility to request incoming graph keys yielding paths for "apps" (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
23. Pointer class requires persistent and virtual memory (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
24. Stepper class requires graph machine subsets and address resolver to move a pointer (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
25. Stepper machine requires graph machine and ability to generate new contexts for cells (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
26. Internal compass directs path through correct chain given history (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
27. Compass uses sums of path to map to output options; invalid paths return bad path (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
28. Cascading sums through loops may require modulo; risk of collision; mitigated by primary vector concept (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
29. Naming patterns attempt to embed next key(s) into pointer name; introduces complexity and ripple (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
30. Alternative previous|current naming considered to aid iteration (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
31. Tape defines walk of keys for a stepper (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))

## Observed Entities (Names Only)
* Pointer
* Stepper / Stepper machine
* Graph machine
* Address resolver
* Function / SES (Self Executing Source)
* Tape
* Internal compass / compass of vectors
* Loop (as runtime reference)
* Memory (runtime, persistent, transient)
* Sub graph / graph handoff
* Security rings / protected mode analogy
* Forward feed / best fit inspection
* Redirect

## Structural Themes (Descriptive Aggregation)
All items below are restatements combining cited phrases without adding new claims.
* Execution comprises loop stepping pointers, executing SES, potentially altering graph state (Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md); [graph functions.md](../../docs/core/graph%20functions.md))
* Naming experiments embed traversal hints; trade-offs include address growth and complexity (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
* Compass mechanism reduces need to map all possible paths by hashing/summing history (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
* Decoupling via graph handoff enables storage and later execution of low-priority chains (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))

## Incomplete Blocks

Incomplete: Stepper Formal Definition
Needed:
- Explicit algorithm for resolving next pointer
- Error handling when redirect invalid
Candidate Sources: [graph pointer.md](../../docs/core/graph%20pointer.md), [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Pointer Naming Specification
Needed:
- Canonical format decision among variants (next-in-name, previous|current)
- Collision / maximum length rules
Candidate Sources: [graph pointer.md](../../docs/core/graph%20pointer.md)

Incomplete: Compass Collision Resolution
Needed:
- Behavior when modulo collision produces ambiguous direction
- Primary vector lifecycle definition
Candidate Sources: [graph node compass.md](../../docs/core/graph%20node%20compass.md)

Incomplete: Security Ring Enforcement
Needed:
- Criteria for protected node classification
- Mutation constraints for lower order nodes
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Graph Handoff Protocol
Needed:
- Required metadata for stored SES sub graph
- Return value reintegration sequence
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Best Fit Hardware Selection
Needed:
- Matching algorithm between pointer requirements and topology
- Fallback strategy on missing capability
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Multi-Graph Concurrency Rules
Needed:
- Synchronization of shared memory changes between parallel graphs
- Ordering guarantees for leaf node communication
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Vector Address Specification
Needed:
- Formal vector domain limits (dimensions, ranges)
- Serialization format for transport
Candidate Sources: [graph functions.md](../../docs/core/graph%20functions.md), [graph node compass.md](../../docs/core/graph%20node%20compass.md)

Incomplete: Redirect Semantics
Needed:
- Conditions under which pointer redirect permissible
- Loop detection / prevention mechanisms
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Verbatim scope: [graph pointer.md](../../docs/core/graph%20pointer.md), [graph functions.md](../../docs/core/graph%20functions.md), [graph node compass.md](../../docs/core/graph%20node%20compass.md), [Procedure Graph.md](../../docs/core/Procedure%20Graph.md), [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 1.
