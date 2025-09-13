---
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Open Questions Index

Consolidated from Incomplete blocks across all current section files (updated after creation of mesh-roles, boot-sequence-table, interface-input-events, identity-persistence).

Core Runtime
1. Health Doctor operational model
2. Chamber→Mantle→Magmatic→Igneous hierarchy clarification
3. Kernel vs System Core boundary definition
4. Event naming decision criteria (Extraction references exist but naming rules absent) (Source: [system core.md](../../docs/core/system%20core.md))

Procedure Graph
5. Roles separation: Pointer vs Stepper vs Machine parent construct (Partially Extracted: graph-overview.md) (Source: [graph pointer.md](../../docs/core/graph%20pointer.md); [graph stepper.md](../../docs/core/graph%20stepper.md))
6. Vector address collision avoidance strategy (Partially Extracted: graph-overview.md) (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
7. Security ring enforcement mechanism (Partially Extracted: graph-overview.md) (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
8. Compass loop modulo policy (Partially Extracted: graph-overview.md) (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
21. Multi-pointer concurrency rules (shared with Loop) (Partially Extracted: graph-overview.md) (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))

Filesystem
9. Filesystem layering distinctions (logical vs physical) (Partially Extracted: filesystem-layering-outline.md; filesystem-overview.md) (Source: [File System.md](../../docs/fs/File%20System.md))
22. File Names specification details (Source: [File Names.md](../../docs/fs/File%20Names.md))
23. Permission externalization model (Source: [File System.md](../../docs/fs/File%20System.md))
24. Particle phase transitions formalization (Source: [File System.md](../../docs/fs/File%20System.md))
25. Orphan particle recovery workflow (Source: [File System.md](../../docs/fs/File%20System.md))
26. Colloid partial fetch semantics (Source: [File System.md](../../docs/fs/File%20System.md))
27. Membrane FS interaction boundaries (Source: [File System.md](../../docs/fs/File%20System.md); [mesh.md](../../docs/mesh.md))
28. Header chain integrity / tamper model (Source: [File System.md](../../docs/fs/File%20System.md))
29. Aggregate mutation workflow (Source: [File System.md](../../docs/fs/File%20System.md))

Memory & Identity
10. Grain / slot / identity mapping (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md); [grains.md](../../docs/fs/grains.md))
11. Identity persistence vs filesystem representation linkage (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
30. Identity persistence mechanics (tensor lifecycle) (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
31. Deterministic reconstruction guarantees (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
32. Security and sandboxing model for NN files (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
33. Storage efficiency validation metrics (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
34. Model streaming protocol (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
35. Identity vs pointer addressing for NN model (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

Mesh / Roles / Registry
12. Node role taxonomy & registry semantics (capability schema) (Source: [nodes.md](../../docs/nodes.md); [registry.md](../../docs/registry.md))
Translator Selection Criteria (from mesh-roles incomplete) – NEW (Source: [nodes.md](../../docs/nodes.md))
Capability Advertisement Protocol fields – NEW (Partially Extracted: capability-advertisement.md) (Source: [nodes.md](../../docs/nodes.md))
Registry command schema (live command entry format) – NEW (Source: [registry.md](../../docs/registry.md))
Session sharing arbitration rules – NEW (Source: [nodes.md](../../docs/nodes.md))
Mesh topology representation structure – NEW (Source: [mesh.md](../../docs/mesh.md))

Boot & Loop
13. Boot phase mapping table (Partially Extracted: boot-sequence-table.md; boot-sequence-diagram.md) (Source: [boot.md](../../docs/boot.md))
14. Pointer 0 payload specification (schema) (Partially Extracted: pointer-0-payload.md) (Source: [zero-suite.md](../../docs/core/zero-suite.md))
17. Boot SEM TAPE format (Partially Extracted: sem-tape-extraction.md) (Source: [boot.md](../../docs/boot.md))
18. BIOS completion signaling criteria (Source: [boot.md](../../docs/boot.md))
19. Driver selection mapping policy (Source: [boot.md](../../docs/boot.md))
20. Loop step frequency governance (Source: [the loop.md](../../docs/the%20loop.md))
Pointer 0 memory layout / relocation – NEW (Source: [zero-suite.md](../../docs/core/zero-suite.md))
Root types load ordering constraints – NEW (Source: [boot.md](../../docs/boot.md))
Multi-phase timing allocation (<5s target breakdown) – NEW (Source: [boot.md](../../docs/boot.md))

Interface / Display / Inputs
15. Display container / input abstraction linkage (binding spec) (Source: [display (container).md](../../docs/display%20(container).md); [inputs.md](../../docs/inputs.md))
Input permission model (shared access control) – NEW (Source: [inputs.md](../../docs/inputs.md))
Canonical event taxonomy enumeration – NEW (Partially Extracted: interface-event-taxonomy.md) (Source: [inputs.md](../../docs/inputs.md); [display (container).md](../../docs/display%20(container).md))
Translator interface specification (functions & errors) – NEW (Source: [inputs.md](../../docs/inputs.md))
Event ordering guarantees – NEW (Source: [inputs.md](../../docs/inputs.md))
Stream input handling distinctions – NEW (Source: [inputs.md](../../docs/inputs.md))

Root Apps / Containerization
16. Root apps & container manifest scope boundary (Source: [container-manifest.md](../../docs/container-manifest.md); [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))

Identity Persistence (Specific Extensions)
Tensor-to-aggregate mapping point of integration – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
Training determinism requirements – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
Streaming reconstruction mechanics – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
Resource cost envelope thresholds – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
Failure & partial reconstruction signaling – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
Identity versioning (epoch/tag) scheme – NEW (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

Verbatim scope: Aggregated from: mesh-roles.md, boot-sequence-table.md, interface-input-events.md, identity-persistence.md, plus prior open question set.
