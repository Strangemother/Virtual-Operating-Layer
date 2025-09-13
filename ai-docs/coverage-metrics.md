Status: Draft
Last-Touched: 2025-09-13
# Coverage Metrics Report

Purpose: Quantify reference coverage of origin markdown sources within ai-docs derivative set. Purely mechanical string scan; no semantic validation.

Summary: Total origin files: 83; Covered (≥1 ref): 63; Uncovered: 20

## Per-File Reference Counts
Format: count – relative/path (AMBIGUOUS if base name collision)

-  19 – docs/core/graph pointer.md
-  19 – docs/fs/File System.md
-  18 – docs/nodes.md
-  18 – docs/registry.md
-  16 – docs/core/graph node compass.md
-  15 – docs/boot.md AMBIGUOUS
-  15 – docs/core/boot.md AMBIGUOUS
-  14 – docs/fs/grains.md
-  14 – docs/mesh.md
-  13 – docs/Procedure Graph.md AMBIGUOUS
-  13 – docs/core/Procedure Graph.md AMBIGUOUS
-  13 – docs/core/graph stepper.md
-  13 – docs/core/zero-suite.md
-  13 – docs/display (container).md
-  12 – docs/Scaling.md
-  12 – docs/core/graph key names.md
-  11 – docs/concepts/memory-as-weights-and-biases.md
-  11 – docs/core/frame-context.md
-  11 – docs/core/graph functions.md
-  10 – docs/inputs.md
-   9 – docs/fs/File Names.md
-   9 – docs/fs/file-resolution.md
-   8 – docs/core/Root Fundamental apps.md
-   8 – docs/core/system core.md
-   8 – docs/fs/grain-iterator.md
-   7 – docs/Facade.md
-   7 – docs/the loop.md
-   6 – docs/container-manifest.md
-   6 – docs/core/os-runtime.md AMBIGUOUS
-   6 – docs/core/structure.md
-   6 – docs/fs/FS vol top level naming.md
-   6 – docs/os-runtime.md AMBIGUOUS
-   5 – docs/core/kernel.md AMBIGUOUS
-   5 – docs/core/terminology.md
-   5 – docs/first-apps.md
-   5 – docs/kernel.md AMBIGUOUS
-   5 – docs/top level.md
-   4 – docs/memory/first.md
-   4 – docs/multiprocessing.md
-   3 – docs/fs/build-assets.md
-   2 – docs/Genesis-Origin.md
-   1 – docs/Radicle.md
-   1 – docs/adding as compiled module.md AMBIGUOUS
-   1 – docs/big-ints.md
-   1 – docs/core/adding as compiled module.md AMBIGUOUS
-   1 – docs/core/core crystal updates.md
-   1 – docs/core/first moments.md
-   1 – docs/crc-service.md
-   1 – docs/fs/Key graph with a stepping graph.md
-   1 – docs/fs/Nomenclature.md
-   1 – docs/fs/Space and Space Discovery.md
-   1 – docs/fs/memory allocation table.md
-   1 – docs/fs/nonimal-vector-names.md
-   1 – docs/fs/open table.md
-   1 – docs/fs/representation.md
-   1 – docs/fs/shared mem view permissioning.md
-   1 – docs/fs/stock-coms.md
-   1 – docs/fs/synthetic-markers.md
-   1 – docs/links.md
-   1 – docs/memory/init-slots.md
-   1 – docs/references.md
-   1 – docs/self assembly vocul functions.md
-   1 – docs/tape.md
-   0 – docs/(easter)-bunny.md
-   0 – docs/core/Contigious address names.md
-   0 – docs/discussion/gnu.md
-   0 – docs/discussion/new paradigm.md
-   0 – docs/fs/readme.md AMBIGUOUS
-   0 – docs/garbage collector.md
-   0 – docs/memory/Single Identity.md
-   0 – docs/root-monolith/Frame Switching.md
-   0 – docs/root-monolith/applying-vol-runtime-libs.md
-   0 – docs/root-monolith/byte-function-load.md
-   0 – docs/root-monolith/commands.md
-   0 – docs/root-monolith/comprehensive.md
-   0 – docs/root-monolith/graph-walk.md
-   0 – docs/root-monolith/memory-module.md
-   0 – docs/root-monolith/phase-0.md
-   0 – docs/root-monolith/phases.md
-   0 – docs/root-monolith/readme.md AMBIGUOUS
-   0 – docs/root-monolith/security research.md
-   0 – docs/root-monolith/stack-processing.md
-   0 – docs/root-monolith/step addresses and layers.md

## Uncovered Files
- docs/(easter)-bunny.md
- docs/garbage collector.md
- docs/memory/Single Identity.md
- docs/fs/readme.md
- docs/root-monolith/phase-0.md
- docs/root-monolith/applying-vol-runtime-libs.md
- docs/root-monolith/graph-walk.md
- docs/root-monolith/Frame Switching.md
- docs/root-monolith/security research.md
- docs/root-monolith/phases.md
- docs/root-monolith/readme.md
- docs/root-monolith/comprehensive.md
- docs/root-monolith/commands.md
- docs/root-monolith/byte-function-load.md
- docs/root-monolith/memory-module.md
- docs/root-monolith/step addresses and layers.md
- docs/root-monolith/stack-processing.md
- docs/core/Contigious address names.md
- docs/discussion/new paradigm.md
- docs/discussion/gnu.md

Incomplete: Methodological limitations
Needed:
- Path-aware link parsing (current method may overcount plain-text mentions)
- Distinguish glossary-only citations vs deep extraction
- Weight references by document type (overview vs section)
Candidate Sources: coverage-metrics.md (this), origin-derivative-coverage-map.md, governance-index.md

Verbatim scope: File system listings only; derivative scans limited to substring presence.
