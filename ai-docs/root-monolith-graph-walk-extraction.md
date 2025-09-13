# Root Monolith Graph Walk (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Source Files: docs/root-monolith/graph-walk.md

Purpose: Extract statements about root monolith graph separation (data vs function), command handling in lowest frame, and frame layering. No new semantics.

## Sourced Statements
1. Root functions and internal memory assets exist on a graph-based memory layout. (Source: docs/root-monolith/graph-walk.md)
2. All data, functional execution steps, and register management handled through graph of connected key-value pairs. (Source: docs/root-monolith/graph-walk.md)
3. Each key address returns a value of bytes or an executable with access to same monolith. (Source: docs/root-monolith/graph-walk.md)
4. Data graph applies a chain of bytes producing a byte array for system digestion. (Source: docs/root-monolith/graph-walk.md)
5. Function graph steps through executable functions with side-effects via graph connections. (Source: docs/root-monolith/graph-walk.md)
6. Data graph: values in graph of keys execute an ordered chain of data; edge references stored away from data references and merged at runtime by acquisition unit. (Source: docs/root-monolith/graph-walk.md)
7. Functional call assigns interactive stepping; each chain yield returns an expected executable; returned function accepts arguments and executes via similar edge graph. (Source: docs/root-monolith/graph-walk.md)
8. Terminal input commands are string byte references for key graph. (Source: docs/root-monolith/graph-walk.md)
9. Lowest frame `0` (pre BIOS area) all commands are code references. (Source: docs/root-monolith/graph-walk.md)
10. Basic commands consist of `print`. (Source: docs/root-monolith/graph-walk.md)
11. Frame +1 layer enables throughput of data through graph reference pointers. (Source: docs/root-monolith/graph-walk.md)
12. At layer +1 root imports, com libraries, and VOL root apps become available (non C compiled builtins). (Source: docs/root-monolith/graph-walk.md)

## Observed Concept Elements (Names Only)
- Graph-based memory layout
- Key-value executable nodes
- Data graph vs function graph
- Acquisition unit (merging edges & data references)
- Terminal command graph references
- Pre BIOS frame 0
- Frame +1 enabling imports and root apps

## Incomplete Blocks
Incomplete: Acquisition Unit Semantics
Needed:
- Definition of acquisition unit responsibilities
- Merge algorithm for edges and data references
- Error handling if edge missing
Candidate Sources: docs/root-monolith/graph-walk.md

Incomplete: Command Reference Resolution
Needed:
- Mapping rules from string bytes to key graph nodes
- Namespace or scoping model in frame 0
- Security considerations for arbitrary command execution
Candidate Sources: docs/root-monolith/graph-walk.md, commands.md

Incomplete: Frame Transition Effects
Needed:
- Explicit criteria to move from frame 0 to +1
- Resources released or retained during transition
- Interaction with boot sequence (boot-sequence-linear.md)
Candidate Sources: docs/root-monolith/graph-walk.md, Frame Switching.md, boot-sequence-linear.md

Verbatim scope: docs/root-monolith/graph-walk.md only.

## Notes
- Glossary stubs added for: acquisition unit, frame 0, command lifecycle (See: sections/glossary.md). (Source: docs/root-monolith/graph-walk.md; commands.md)

Backlink: Referenced by input-lifecycle-skeleton.md and sequence-series-comparison.md
Additional Backlink: Referenced by command-frame-lifecycle-skeleton.md
