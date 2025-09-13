# Origin → Derivative Coverage Map
Status: Draft
Last-Touched: 2025-09-13
Depends-On: origin-docs-modification-report.md, governance-index.md, gap-priority-matrix.md

Purpose: Enumerate each origin `docs/` markdown source and list zero-or-more derivative `ai-docs/` files that extract, consolidate, or reference its content. No new technical assertions added; mapping only. Where coverage absent, mark explicitly.

Method: Directory listings (docs/, docs/core/, docs/fs/) plus visual inspection of derivative filenames. Does not imply completeness of extraction—only presence of at least one citing derivative artifact. Future refinement may add citation counts (TODO pending verification tooling).

## 1. Core / Runtime Cluster
- docs/core/terminology.md → Covered by: sections/glossary.md (Source: sections/glossary.md)
- docs/core/system core.md → Covered by: sections/core-runtime.md (Source: sections/core-runtime.md)
- docs/core/structure.md → Covered by: graph-overview.md (general runtime references) (Source: graph-overview.md)
- docs/core/frame-context.md → Covered by: graph-overview.md; sections/boot-loop.md (Source: graph-overview.md; sections/boot-loop.md)
- docs/core/boot.md → Covered by: boot-sequence-linear.md; sections/boot-sequence-table.md; sections/boot-loop.md; sem-tape-extraction.md (Source: boot-sequence-linear.md; sem-tape-extraction.md)
- docs/boot.md → Covered by: boot-sequence-linear.md; sem-tape-extraction.md (Source: boot-sequence-linear.md)
- docs/core/zero-suite.md → Covered by: boot-sequence-linear.md; sections/boot-loop.md (Source: boot-sequence-linear.md)
- docs/core/kernel.md → Covered by: sections/core-runtime.md (Source: sections/core-runtime.md)
- docs/kernel.md → Covered by: sections/core-runtime.md (Source: sections/core-runtime.md)
- docs/core/Procedure Graph.md → Covered by: graph-overview.md; sections/procedure-graph.md (Source: graph-overview.md; sections/procedure-graph.md)
- docs/Procedure Graph.md → Covered by: graph-overview.md; sections/procedure-graph.md (Source: graph-overview.md)
- docs/core/graph pointer.md → Covered by: graph-overview.md; graph-boundary-outline.md; graph-key-names-extraction.md (Source: graph-overview.md)
- docs/core/graph stepper.md → Covered by: graph-overview.md; graph-boundary-outline.md (Source: graph-overview.md)
- docs/core/graph node compass.md → Covered by: graph-overview.md; graph-boundary-outline.md (Source: graph-overview.md)
- docs/core/graph functions.md → Covered by: graph-overview.md (Source: graph-overview.md)
- docs/core/graph key names.md → Covered by: graph-key-names-extraction.md; vector-bits-extraction.md (Source: graph-key-names-extraction.md; vector-bits-extraction.md)
- docs/tape.md → Covered by: sem-tape-extraction.md; graph-boundary-outline.md (Source: sem-tape-extraction.md)
- docs/core/first moments.md → Covered by: sections/boot-loop.md (Source: sections/boot-loop.md)
- docs/core/core crystal updates.md → Covered by: (none) → Incomplete
- docs/core/adding as compiled module.md → Covered by: (none) → Incomplete
- docs/adding as compiled module.md → Covered by: (none) → Incomplete

Incomplete: Core coverage gaps
Needed:
- Determine whether "core crystal updates" requires extraction or is deprecated context
- Clarify whether dual instances of "adding as compiled module.md" differ materially
Candidate Sources: docs/core/core crystal updates.md, docs/core/adding as compiled module.md, docs/adding as compiled module.md

## 2. Filesystem Cluster
- docs/fs/File System.md → Covered by: fs-overview.md; sections/filesystem-overview.md (Source: fs-overview.md)
- docs/fs/file-resolution.md → Covered by: fs-overview.md; sections/filesystem-layering-outline.md (Source: fs-overview.md)
- docs/fs/grains.md → Covered by: fs-overview.md; sections/filesystem.md (Source: fs-overview.md)
- docs/fs/grain-iterator.md → Covered by: fs-overview.md (Source: fs-overview.md)
- docs/fs/File Names.md → Covered by: fs-overview.md (Source: fs-overview.md)
- docs/fs/FS vol top level naming.md → Covered by: fs-overview.md (Source: fs-overview.md)
- docs/fs/memory allocation table.md → Covered by: sections/filesystem-layering-outline.md (Source: sections/filesystem-layering-outline.md)
- docs/fs/open table.md → Covered by: sections/filesystem-layering-outline.md (Source: sections/filesystem-layering-outline.md)
- docs/fs/representation.md → Covered by: sections/filesystem.md (Source: sections/filesystem.md)
- docs/fs/Key graph with a stepping graph.md → Covered by: (none) → Incomplete
- docs/fs/Nomenclature.md → Covered by: (none) → Incomplete
- docs/fs/shared mem view permissioning.md → Covered by: (none) → Incomplete
- docs/fs/Space and Space Discovery.md → Covered by: (none) → Incomplete
- docs/fs/nonimal-vector-names.md → Covered by: vector-bits-extraction.md (Source: vector-bits-extraction.md)
- docs/fs/build-assets.md → Covered by: (none) → Incomplete
- docs/fs/stock-coms.md → Covered by: (none) → Incomplete
- docs/fs/synthetic-markers.md → Covered by: sections/filesystem-layering-outline.md (Source: sections/filesystem-layering-outline.md)

Incomplete: Filesystem coverage gaps
Needed:
- Assess if uncovered files contain unique normative constructs vs historical brainstorming
- Extract permissioning specifics from shared mem view permissioning.md if present
Candidate Sources: docs/fs/Key graph with a stepping graph.md, docs/fs/shared mem view permissioning.md, docs/fs/Space and Space Discovery.md, docs/fs/Nomenclature.md

## 3. Mesh / Distribution Cluster
- docs/mesh.md → Covered by: mesh-roles-matrix.md; sections/mesh-role-derivation.md (Source: mesh-roles-matrix.md)
- docs/nodes.md → Covered by: mesh-roles-matrix.md; capability-advertisement-extraction.md; sections/onboarding-sequence.md (Source: mesh-roles-matrix.md; capability-advertisement-extraction.md)
- docs/registry.md → Covered by: mesh-roles-matrix.md; registry-capability-broker.md (Source: mesh-roles-matrix.md)
- docs/Scaling.md → Covered by: mesh-roles-matrix.md; sections/mesh-role-derivation.md (Source: mesh-roles-matrix.md)
- docs/multiprocessing.md → Covered by: (none) → Incomplete
- docs/crc-service.md → Covered by: (none) → Incomplete

Incomplete: Mesh coverage gaps
Needed:
- Determine if multiprocessing.md introduces lifecycle or role semantics
- Confirm whether crc-service.md defines a service-type requiring glossary inclusion
Candidate Sources: docs/multiprocessing.md, docs/crc-service.md

## 4. Interface / Presentation Cluster
- docs/display (container).md → Covered by: input-event-taxonomy.md; sections/interface-event-taxonomy.md (Source: input-event-taxonomy.md)
- docs/inputs.md → Covered by: input-event-taxonomy.md; sections/interface-input-events.md (Source: input-event-taxonomy.md)
- docs/Facade.md → Covered by: sections/interface-placeholder.md (Source: sections/interface-placeholder.md)
- docs/links.md → Covered by: (none) → Incomplete

Incomplete: Interface coverage gaps
Needed:
- Evaluate if links.md contains conceptual navigation elements warranting extraction
Candidate Sources: docs/links.md

## 5. Memory / Identity Cluster
- docs/concepts/memory-as-weights-and-biases.md → Covered by: memory-identity-overview.md; sections/identity-persistence.md (Source: memory-identity-overview.md)
- docs/memory/first.md → Covered by: memory-identity-overview.md (tick slots); sections/identity-memory-unification.md (Source: memory-identity-overview.md)

Incomplete: Memory coverage gaps
Needed:
- Identify additional memory/ directory files (if any) not yet inventoried
- Extract explicit persistence state taxonomy (still incomplete)
Candidate Sources: docs/memory/, memory-identity-overview.md

## 6. Boot / Genesis / Loop Cluster
- docs/top level.md → Covered by: sections/boot-loop.md (Source: sections/boot-loop.md)
- docs/the loop.md → Covered by: sections/boot-loop.md (Source: sections/boot-loop.md)
- docs/Genesis-Origin.md → Covered by: sections/boot-loop.md (Source: sections/boot-loop.md)

## 7. Root & Foundational Apps Cluster
- docs/core/Root Fundamental apps.md → Covered by: sections/root-apps-placeholder.md (Source: sections/root-apps-placeholder.md)
- docs/first-apps.md → Covered by: sections/root-apps-placeholder.md (Source: sections/root-apps-placeholder.md)
- docs/container-manifest.md → Covered by: sections/container-manifest.md (if present) / (none) → Incomplete

Incomplete: Root apps coverage gaps
Needed:
- Confirm presence/absence of container-manifest extraction file
Candidate Sources: docs/container-manifest.md, ai-docs/sections/

## 8. Misc / Other
- docs/Radicle.md → Covered by: (none) → Incomplete
- docs/big-ints.md → Covered by: (none) → Incomplete
- docs/self assembly vocul functions.md → Covered by: (none) → Incomplete
- docs/os-runtime.md → Covered by: sections/core-runtime.md (Source: sections/core-runtime.md)
- docs/core/os-runtime.md → Covered by: sections/core-runtime.md (Source: sections/core-runtime.md)
- docs/references.md → Covered by: (none) → Incomplete
- docs/links.md → (duplicate entry above)

Incomplete: Misc coverage gaps
Needed:
- Determine which of these warrant extraction vs archival only
Candidate Sources: listed files

## 9. Coverage Summary Snapshot
- Total origin markdown (approximate enumerated): Core/Runtime (20), FS (18), Mesh (6), Interface (4), Memory (2), Boot (3), Root (3), Misc (7) → ~63
- Covered (≥1 derivative reference): Marked lines excluding explicit "(none)" → Pending automated count
- Uncovered: All lines with "→ Incomplete" markers

Metrics: See coverage-metrics.md for generated quantitative counts (Source: coverage-metrics.md)

Incomplete: Automated coverage metrics
Needed:
- Script to count origin vs covered
- Optional: citation density (derivative count per origin)
Candidate Sources: tools/ (new script pending)

## 10. Integration Hooks
Once gaps triaged, add new extraction tasks for high-priority uncovered origins (cross-reference gap-priority-matrix.md for alignment). No tasks embedded here to avoid duplication.

Verbatim scope: Directory listings only; no internal parsing of origin file contents performed in this pass.
