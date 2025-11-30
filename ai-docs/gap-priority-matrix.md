Status: Draft
Last-Touched: 2025-11-30
# Gap Priority Matrix

Purpose: Rank outstanding Incomplete blocks by criticality to core conceptual coherence. No new definitions; aggregation only.

## Scoring Dimensions
- Core Dependency: Required for interpreting other promoted docs
- Terminology Blocker: Prevents stable glossary finalization
- Cross-Cluster Impact: Touches more than one concept cluster
- Boot Path Critical: Affects boot/initialization comprehension

Scale (per dimension): 0 = none, 1 = low, 2 = moderate, 3 = high (Source: internal aggregation rule derived from existing incomplete blocks – no external invention of content beyond numeric ranking rubric.)

## Ranked Items
1. Collision Resolution Procedure
   - Core Dependency: 2
   - Terminology Blocker: 3
   - Cross-Cluster Impact: 2
   - Boot Path Critical: 0
   - Sources: term-collisions.md (incomplete), policy-alias-format.md (incomplete section)
   - Rationale: Needed to finalize alias normalization.

2. Graph Concept Boundary (pointer vs key names vs compass vs stepper)
   - Core Dependency: 3
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (graph + execution lifecycle)
   - Boot Path Critical: 1 (graph registration stage clarity)
   - Sources: term-collisions.md (additional discovery), graph-overview.md (incomplete blocks), docs/core/graph pointer.md, graph key names.md, graph node compass.md, graph stepper.md
   - Rationale: Multiple overlapping files create ambiguity in unified execution model.

3. Boot to Graph Transition Ordering Guarantees
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (boot + graph + zero-suite)
   - Boot Path Critical: 3
   - Sources: boot.md, zero-suite.md, frame-context.md, Procedure Graph.md (incomplete blocks referenced in extraction)
   - Rationale: Execution lifecycle sequencing not explicitly enumerated.

4. Filesystem Layer Permissioning Semantics
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (fs + identity)
   - Boot Path Critical: 1
   - Sources: filesystem-overview.md (incomplete blocks), docs/fs/File System.md, docs/fs/file-resolution.md
   - Rationale: Access semantics incomplete for future referencing of identity model.

5. Memory Identity Unification (slots vs grains vs allocation table)
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (memory + fs mapping metaphors)
   - Boot Path Critical: 0
   - Sources: memory-as-weights-and-biases.md, docs/fs/grains.md, docs/memory/* (where present), glossary incomplete notes
   - Rationale: Overlapping metaphors risk inconsistent later spec writing.

6. Vector Component Definitions (layer/graph/ownership bits)
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 1 (graph naming primarily)
   - Boot Path Critical: 0
   - Sources: graph-key-names-extraction.md, docs/core/graph key names.md, vector-bits-extraction.md
   - Rationale: Undefined bit semantics hinder stable pointer addressing description.
   - Incomplete Extension: Collision handling, permission layer, and encryption indicator semantics unresolved (Source: vector-bits-extraction.md)

7. Encrypted Key Handling Semantics
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 1 (security + graph)
   - Boot Path Critical: 0
   - Sources: graph-key-names-extraction.md, docs/core/graph key names.md
   - Rationale: Security mention lacks operational boundaries.

8. Input Event Type Enumeration
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (interface + mesh + runtime)
   - Boot Path Critical: 0
   - Sources: input-event-taxonomy.md, docs/inputs.md, docs/display (container).md
   - Rationale: Missing canonical list blocks consistent interface contracts.

9. Tensor Identity Schema (NN-as-file)
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (memory + filesystem representation)
   - Boot Path Critical: 0
   - Sources: memory-identity-states.md, memory-as-weights-and-biases.md, memory-identity-overview.md
   - Rationale: Needed for integrating tensor artifacts with storage model.
   - Incomplete Extension: Persistence state taxonomy & temporal identity mapping unresolved (Source: memory-identity-overview.md)

10. Portal Event Interface Contract
    - Core Dependency: 1
    - Terminology Blocker: 1
    - Cross-Cluster Impact: 2 (interface + mesh)
    - Boot Path Critical: 0
    - Sources: input-event-taxonomy.md, docs/inputs.md, docs/display (container).md
    - Rationale: Lacking structural definition for ingress boundary.

11. Capability Advertisement Schema
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (mesh + onboarding + interface translation)
   - Boot Path Critical: 0
   - Sources: mesh-roles-matrix.md (incomplete), docs/nodes.md (capability set mention), capability-advertisement-extraction.md
   - Rationale: Without field enumeration (fields incomplete: advertised field set, versioning, update cadence), role negotiation cannot be formalized.
   - Incomplete Extension: Negotiation ordering & security validation semantics unresolved (Source: capability-advertisement-extraction.md)

12. Registry Lifecycle Ordering
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (mesh + runtime state)
   - Boot Path Critical: 1 (affects early command handling sequence)
   - Sources: mesh-roles-matrix.md (incomplete), docs/registry.md, docs/nodes.md
   - Rationale: Initialization timing vs SESSION creation unspecified.

13. Contiguous Address Space Normalization
   - Core Dependency: 2
   - Terminology Blocker: 2 (impacts glossary potential terms: virtual address, page)
   - Cross-Cluster Impact: 2 (graph execution + memory allocation)
   - Boot Path Critical: 0
   - Sources: contigious-address-names-extraction.md, docs/core/Contigious address names.md
   - Rationale: Lack of formal virtual address format and algorithm selection contract blocks stable description of stepper predictive behavior.
   - Incomplete Extension: Paging criteria & hashmap vs closed loop tradeoffs unresolved (Source: contigious-address-names-extraction.md)

14. Identity Memory Isolation Semantics
   - Core Dependency: 2
   - Terminology Blocker: 2 (permissions state structure missing)
   - Cross-Cluster Impact: 2 (memory + mesh capability linkage)
   - Boot Path Critical: 0
   - Sources: single-identity-extraction.md, docs/memory/Single Identity.md
   - Rationale: Undefined isolation boundaries hinder integration with capability advertisement and security posture.
   - Incomplete Extension: Protected area lifecycle & persistence rules unresolved (Source: single-identity-extraction.md)

15. Quiet Time GC Threshold Semantics
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 1 (system core + memory)
   - Boot Path Critical: 0
   - Sources: garbage-collector-extraction.md, docs/garbage collector.md
   - Rationale: Absence of softheader/hard peak quantitative definitions limits clarity around resource reclamation scheduling.
   - Incomplete Extension: Freeze mechanism behavior & resource classification unresolved (Source: garbage-collector-extraction.md)

16. Layered Addressing Contract (Index / Family Domains)
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (memory + graph addressing)
   - Boot Path Critical: 0
   - Sources: root-monolith-step-addresses-layers-extraction.md, docs/root-monolith/step addresses and layers.md
   - Rationale: Without formal relationships among domain labels (index, expanded, family, extended family, related family, dictionary) pointer disambiguation and future address normalization remain blocked.
   - Incomplete Extension: Collision precedence & transformation pathway rules unresolved (Source: root-monolith-step-addresses-layers-extraction.md)

17. Acquisition-Triggered Frame Orientation
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (memory acquisition + frame context)
   - Boot Path Critical: 1 (early mapping pipeline ordering risk)
   - Sources: root-monolith-memory-module-extraction.md, docs/root-monolith/memory-module.md
   - Rationale: Unclear if frame orientation precedes or follows block mapping, impeding precise boot-to-runtime mapping specification.
   - Incomplete Extension: Concurrency semantics for multiple acquisition units unresolved (Source: root-monolith-memory-module-extraction.md)

18. Frame Switching Authorization Model
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (execution control + memory linearization)
   - Boot Path Critical: 2 (transition timing influences early command execution ordering)
   - Sources: root-monolith-frame-switching-extraction.md, docs/root-monolith/Frame Switching.md
   - Rationale: Missing initiator and validation path prevents defining safe transition states or rollback boundaries.
   - Incomplete Extension: Persistence vs reinitialization state set unresolved (Source: root-monolith-frame-switching-extraction.md)

19. Command Invocation Lifecycle Coupling
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (graph traversal + frame context)
   - Boot Path Critical: 2 (frame 0 orchestration clarity)
   - Sources: root-monolith-commands-extraction.md, root-monolith-graph-walk-extraction.md
   - Rationale: Absent explicit ordering between command execution phases and graph walk initialization obstructs deterministic startup behavior.
   - Incomplete Extension: Timeout/deadlock safeguards and rollback semantics unresolved (Source: root-monolith-commands-extraction.md)

20. Sequence vs Series Graph Distinction
   - Core Dependency: 1
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 1 (graph traversal nuance)
   - Boot Path Critical: 0
   - Sources: root-monolith-step-addresses-layers-extraction.md, root-monolith-graph-walk-extraction.md
   - Rationale: Ambiguous differentiation risks glossary collision and inconsistent traversal semantics in future specs.
   - Incomplete Extension: Traversal algorithm divergence & lifecycle triggers unresolved (Source: root-monolith-step-addresses-layers-extraction.md)

21. Input Stream Stepping Semantics
   - Core Dependency: 2 (affects command ingestion modeling)
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 1 (interface → command pipeline)
   - Boot Path Critical: 1 (early REPL readiness)
   - Sources: root-monolith-monolith-readme-extraction.md, docs/root-monolith/readme.md
   - Rationale: Undefined termination & framing rules block deterministic command parsing specification.

22. Walking Register Structure
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 1
   - Boot Path Critical: 0
   - Sources: root-monolith-monolith-readme-extraction.md
   - Rationale: Needed only when formalizing state persistence across streamed input.

23. Cold-Store Entropy Policy
   - Core Dependency: 1
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 1 (memory + lifecycle aging)
   - Boot Path Critical: 0
   - Sources: root-monolith-monolith-readme-extraction.md
   - Rationale: Aging thresholds not critical to initial runtime specification.

24. Code Allocator Mechanism
   - Core Dependency: 2
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 2 (memory + execution loading)
   - Boot Path Critical: 1
   - Sources: root-monolith-comprehensive-extraction.md; root-monolith-byte-function-load-extraction.md
   - Rationale: Allocation semantics impact executable loading contract yet undefined.

25. Variation Tree Definition
   - Core Dependency: 1
   - Terminology Blocker: 2
   - Cross-Cluster Impact: 1
   - Boot Path Critical: 0
   - Sources: root-monolith-comprehensive-extraction.md
   - Rationale: Grammar augmentation non-blocking to current boot/graph specs.

26. Library Auto-Exposure Rules
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (runtime + developer tooling)
   - Boot Path Critical: 1
   - Sources: root-monolith-comprehensive-extraction.md; root-monolith-libs-extraction.md
   - Rationale: Module inclusion precedence affects deterministic environment surface.

27. Byte Function Reconstruction Ordering
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (security + execution loader)
   - Boot Path Critical: 1
   - Sources: root-monolith-byte-function-load-extraction.md
   - Rationale: Undefined boundaries hinder safe dynamic function materialization.

28. Checksum Referencing Semantics
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (security + integrity verification)
   - Boot Path Critical: 1
   - Sources: root-monolith-byte-function-load-extraction.md; root-monolith-security-init-extraction.md
   - Rationale: Integrity guarantees incomplete pending algorithm identification.

29. Execution Safety (Byte-Loaded Functions)
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (security + memory isolation)
   - Boot Path Critical: 1
   - Sources: root-monolith-byte-function-load-extraction.md; root-monolith-comprehensive-extraction.md
   - Rationale: Sandbox & permission gating absent; affects risk posture.

30. Security Initialization Chain Ordering
   - Core Dependency: 2
   - Terminology Blocker: 1
   - Cross-Cluster Impact: 2 (boot + security + graph)
   - Boot Path Critical: 2
   - Sources: root-monolith-security-init-extraction.md; root-monolith-phase-0-extraction.md; root-monolith-phase-sequence-extraction.md
   - Rationale: Precise ordering required to finalize earlier "Boot to Graph Transition" gap resolution.

## Incomplete Blocks

Incomplete: Formal Ranking Validation
Needed:
- Confirmation numeric scales acceptable for interim prioritization
- Decision if matrix requires weighting factors
Candidate Sources: gap-priority-matrix.md (this), status-readiness.md, policy-promotion.md (future) 

Verbatim scope: term-collisions.md, policy-alias-format.md, graph-overview.md, docs/core/graph pointer.md, docs/core/graph key names.md, docs/core/graph node compass.md, docs/core/graph stepper.md, boot.md, zero-suite.md, frame-context.md, Procedure Graph.md, filesystem-overview.md, docs/fs/File System.md, docs/fs/file-resolution.md, memory-as-weights-and-biases.md, docs/fs/grains.md, graph-key-names-extraction.md, input-event-taxonomy.md, memory-identity-states.md.
