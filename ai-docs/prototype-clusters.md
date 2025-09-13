# Prototype Clusters (Initial Reorganization Draft)

Status: Draft
Last-Touched: 2025-09-12
Owner: TODO
Depends-On: ../docs/

Purpose: Establish the initial thematic clusters for restructuring existing VOL documentation. This file is a staging area; it does not yet consolidate content. Descriptions are intentionally concise and will be expanded only with confirmed source citations. No new behaviors or terminology are introduced.

## Cluster List

1. Core Runtime & Lifecycle
2. Procedure Graph Model
3. Filesystem & Storage Layers
4. Memory & Identity Model
5. Mesh / Nodes / Registry / Scaling
6. Boot & Loop Sequence
7. Interface & Display Layer
8. Root & Foundational Apps / Containerization
9. Open Questions & Incompletion Blocks Aggregator

---

## 1. Core Runtime & Lifecycle
Focus: Fundamental operating context, kernel framing, structural abstractions, terminology anchors, and system core definitions. (Source: [terminology.md](../docs/core/terminology.md), [system core.md](../docs/core/system%20core.md), [structure.md](../docs/core/structure.md), [kernel.md](../docs/core/kernel.md), [os-runtime.md](../docs/core/os-runtime.md))

## 2. Procedure Graph Model
Focus: Execution representation via graph constructs (pointer, stepper, compass, key naming, graph functions) forming a procedural addressing and traversal semantics layer. (Source: [Procedure Graph.md](../docs/core/Procedure%20Graph.md), [graph pointer.md](../docs/core/graph%20pointer.md), [graph stepper.md](../docs/core/graph%20stepper.md), [graph node compass.md](../docs/core/graph%20node%20compass.md), [graph key names.md](../docs/core/graph%20key%20names.md), [graph functions.md](../docs/core/graph%20functions.md))

## 3. Filesystem & Storage Layers
Focus: Logical file naming, resolution, top-level volume naming, grain concept, iteration mechanics, asset build pathways, and layered abstraction between representation and access. (Source: [File System.md](../docs/fs/File%20System.md), [File Names.md](../docs/fs/File%20Names.md), [file-resolution.md](../docs/fs/file-resolution.md), [FS vol top level naming.md](../docs/fs/FS%20vol%20top%20level%20naming.md), [grains.md](../docs/fs/grains.md), [grain-iterator.md](../docs/fs/grain-iterator.md), [build-assets.md](../docs/fs/build-assets.md))

## 4. Memory & Identity Model
Focus: Conceptual treatment of memory as weights/biases (identity relationships, allocation metaphors) and potential alignment with slot / grain abstractions (pending clarification). (Source: [memory-as-weights-and-biases.md](../docs/concepts/memory-as-weights-and-biases.md))

Incomplete: Slot vs Grain relationship
Needed:
- Explicit statement whether grains map 1:1 to memory slots or are higher-level aggregations.
- Clarify identity persistence boundaries.
Candidate Sources: [grains.md](../docs/fs/grains.md), [memory-as-weights-and-biases.md](../docs/concepts/memory-as-weights-and-biases.md), TODO: discover additional memory docs.

## 5. Mesh / Nodes / Registry / Scaling
Focus: Distributed topology semantics, node roles, registry coordination, scaling considerations, multiprocessing notes. (Source: [mesh.md](../docs/mesh.md), [nodes.md](../docs/nodes.md), [registry.md](../docs/registry.md), [Scaling.md](../docs/Scaling.md), [multiprocessing.md](../docs/multiprocessing.md))

## 6. Boot & Loop Sequence
Focus: Initial genesis narrative, zero-suite initialization, transition into steady operational loop, frame-context establishment. (Source: [boot.md](../docs/boot.md), [Genesis-Origin.md](../docs/Genesis-Origin.md), [zero-suite.md](../docs/core/zero-suite.md), [frame-context.md](../docs/core/frame-context.md), [the loop.md](../docs/the%20loop.md), [top level.md](../docs/top%20level.md))

Incomplete: Ordering guarantees & error handling semantics in boot handoff
Needed:
- Defined order constraints among zero-suite init, frame-context creation, and graph registration.
- Recovery or retry policy if a stage fails.
Candidate Sources: [boot.md](../docs/boot.md), [zero-suite.md](../docs/core/zero-suite.md), [frame-context.md](../docs/core/frame-context.md), [Procedure Graph.md](../docs/core/Procedure%20Graph.md), [top level.md](../docs/top%20level.md)

## 7. Interface & Display Layer
Focus: Presentation container, input handling abstraction, façade pattern integration, branding / naming cues influencing user-facing identity. (Source: [display (container).md](../docs/display%20(container).md), [inputs.md](../docs/inputs.md), [Facade.md](../docs/Facade.md), [name.md](../docs/branding/name.md), [colour-coding.md](../docs/branding/colour-coding.md))

## 8. Root & Foundational Apps / Containerization
Focus: Foundational/root applications, container manifest notions, early application bootstrap. (Source: [Root Fundamental apps.md](../docs/core/Root%20Fundamental%20apps.md), [container-manifest.md](../docs/container-manifest.md), [first-apps.md](../docs/first-apps.md))

## 9. Open Questions & Incompletion Blocks Aggregator
Focus: Central index for unresolved specifications, naming collisions, and pending clarifications harvested from clusters. Will link outward to source docs and track resolution status. (Source: This file + referenced cluster sources)

---

## Cross-Cutting Pending Clarifications

Incomplete: Unified taxonomy for 'core', 'system core', 'kernel', 'os-runtime'
Needed:
- Explicit hierarchical relationship or synonym mapping among these terms.
- Identification of which term is canonical in normative spec sections.
Candidate Sources: [system core.md](../docs/core/system%20core.md), [kernel.md](../docs/core/kernel.md), [os-runtime.md](../docs/core/os-runtime.md), [structure.md](../docs/core/structure.md)

Incomplete: Graph addressing primitives scope overlap
Needed:
- Distinctions among pointer / stepper / compass / key naming responsibilities.
- Whether a consolidated interface spec is intended.
Candidate Sources: [graph pointer.md](../docs/core/graph%20pointer.md), [graph stepper.md](../docs/core/graph%20stepper.md), [graph node compass.md](../docs/core/graph%20node%20compass.md), [graph key names.md](../docs/core/graph%20key%20names.md), [Procedure Graph.md](../docs/core/Procedure%20Graph.md)

Incomplete: Identity persistence vs filesystem representation
Needed:
- Clarify whether identity is bound to memory constructs or file abstractions first.
- Lifecycle triggers for identity invalidation / re-binding.
Candidate Sources: [memory-as-weights-and-biases.md](../docs/concepts/memory-as-weights-and-biases.md), [File System.md](../docs/fs/File%20System.md), [grains.md](../docs/fs/grains.md)

---

Notes:
- This document intentionally avoids speculative expansion beyond cited sources.
- Future step: Convert each Incompletion block into tracked issues or a consolidated OPEN-QUESTIONS.md once validated.
