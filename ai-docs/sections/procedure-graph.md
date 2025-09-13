---
Status: Draft
Last-Touched: 2025-09-13
Source: restructured-notes-2025.md
---
# Procedure Graph Model

Summary:
- Procedure Graph: Linear ordered function set; every application a graph-referenced function name enabling parallel or linear chain execution across nodes via async + sockets. (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
- Security Rings: Lower order (#0) nodes provide protected execution analogous to protected mode. (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
- Loop Stepping: Root #0 cycles into #1 and nested subgraphs; traversal may redirect; graph mutable at runtime. (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
- Executable Pointers / SES: Pointers map to code units (functions) able to mutate graph state and memory; support reprogrammable kernel concept. (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
- Context Frame: Frame supplies current view (persistent store address, live graph, temp memory, functions/API, pointer knowledge) across stepper lifetime. (Source: [frame-context.md](../../docs/core/frame-context.md))
- Zero Suite: First services post-handoff (code libs/VM, pointer class, memory allocations, executor placements); pointer 0 bootstrap before wider graph exists. (Source: [zero-suite.md](../../docs/core/zero-suite.md))
- Pointer Definition: Header element executing actions; can carry code or other content forms; naming schemes may embed next/previous vector addresses. (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
- Key Naming & Vector Model: Addresses potentially computed from previous + current (A+B=C), vector components (layer, graph identity, position); names may encode direction and attributes; tape lists represent linear sequences. (Source: [graph key names.md](../../docs/core/graph%20key%20names.md))
- Stepper: Thin walker executing pointers sequentially; machine constructs context, frequency control, async allowances; separation: Root → Machine Parent → Stepper Machine → Stepper → Pointer. (Source: [graph stepper.md](../../docs/core/graph%20stepper.md))
- Graph Functions / SES Behavior: Functions can redirect execution, call other pointers, store results in context memory; may be compiled or sandboxed. (Source: [graph functions.md](../../docs/core/graph%20functions.md))
- Node Compass: Internal path resolution using summed vector history to constrain valid transitions; modulo approach considered for loops; collision concerns noted. (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))

## Cross-References
See also: [Graph Subsystem Overview](graph-overview.md) for consolidated graph execution constructs and formal definitions.

Incomplete: Formal roles separation (Pointer vs Stepper vs Stepper Machine vs Machine Parent)
Needed:
- Minimal required methods/attributes for each entity
- Lifecycle ownership & destruction order
Candidate Sources: [graph pointer.md](../../docs/core/graph%20pointer.md), [graph stepper.md](../../docs/core/graph%20stepper.md)

Incomplete: Vector address collision avoidance
Needed:
- Deterministic formula for next key without collisions under dynamic graph edits
- Handling of encrypted key names
Candidate Sources: [graph key names.md](../../docs/core/graph%20key%20names.md)

Incomplete: Security ring enforcement
Needed:
- Mechanism preventing non-ring0 nodes from altering protected graph sections
- Escalation / delegation pathway
Candidate Sources: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md), [kernel.md](../../docs/core/kernel.md)

Incomplete: Compass loop modulo policy
Needed:
- Criteria for choosing modulo ranges to avoid valid path collisions in recursive graphs
- Fallback on collision detection
Candidate Sources: [graph node compass.md](../../docs/core/graph%20node%20compass.md)

Verbatim scope: restructured-notes-2025.md Section 2 only.
