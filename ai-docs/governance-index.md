---
Status: Draft
Last-Touched: 2025-11-30
---
# Documentation Governance Index

Central index of policy and procedure documents; no new rules introduced.

## Core Policy Documents
- [policy-promotion.md](policy-promotion.md) – Criteria and process for document promotion to Working-Spec
- [policy-alias-format.md](policy-alias-format.md) – Canonical formatting for term aliases in glossary
- [policy-archival.md](policy-archival.md) – Criteria and process for Status: Archival classification
- [collision-resolution-procedure.md](collision-resolution-procedure.md) – Steps for resolving term naming collisions

## Navigation & Index Documents
- [index.md](index.md) – Main documentation index with quick navigation
- [overview-index.md](overview-index.md) – Hub linking consolidated overviews
- [root-monolith-index.md](root-monolith-index.md) – Navigation hub for root-monolith extractions
- [governance-index.md](governance-index.md) – This document

## Consolidated Overview Documents
- [graph-overview.md](graph-overview.md) – Consolidated graph model skeleton (pointer/stepper/compass/tape)
- [fs-overview.md](fs-overview.md) – Layered filesystem conceptual synthesis
- [boot-sequence-linear.md](boot-sequence-linear.md) – Linear boot phase outline
- [memory-identity-overview.md](memory-identity-overview.md) – Consolidated memory & identity conceptual extraction
- [mesh-roles-matrix.md](mesh-roles-matrix.md) – Mesh role & capability extraction

## Consolidation Skeletons
- [frame-model-skeleton.md](frame-model-skeleton.md) – Consolidated frame/context statements
- [addressing-domain-enumeration.md](addressing-domain-enumeration.md) – Flat enumeration of addressing domains
- [input-lifecycle-skeleton.md](input-lifecycle-skeleton.md) – Consolidated input stream / command / graph walk references
- [command-frame-lifecycle-skeleton.md](command-frame-lifecycle-skeleton.md) – Consolidated command and frame transition references
- [library-exposure-pathways-matrix.md](library-exposure-pathways-matrix.md) – Enumerated library exposure mechanisms

## Gap Tracking Documents
- [gap-index.md](gap-index.md) – Central registry of all unresolved specification items
- [gap-priority-matrix.md](gap-priority-matrix.md) – Ranked gaps by criticality
- [gap-resolution-batches.md](gap-resolution-batches.md) – Thematic grouping of unresolved gaps

## Term Management Documents
- [sections/glossary.md](sections/glossary.md) – Comprehensive term definitions
- [term-collisions.md](term-collisions.md) – Naming conflict tracking and resolution
- [term-promotion-readiness-matrix.md](term-promotion-readiness-matrix.md) – Working-term readiness categorization
- [promotion-candidate-checklist.md](promotion-candidate-checklist.md) – Readiness evidence & blocking gap list for term promotion

## Extraction Documents

### Core Concept Extractions
- [graph-key-names-extraction.md](graph-key-names-extraction.md) – Pointer key naming schemes extraction
- [vector-bits-extraction.md](vector-bits-extraction.md) – Vector bit component occurrence & gap extraction
- [capability-advertisement-extraction.md](capability-advertisement-extraction.md) – Capability advertisement schema gap extraction
- [input-event-taxonomy.md](input-event-taxonomy.md) – Input translation & event gaps extraction
- [memory-identity-states.md](memory-identity-states.md) – Tensor-based memory identity extraction

### Memory & Identity Extractions
- [contigious-address-names-extraction.md](contigious-address-names-extraction.md) – Contiguous addressing algorithm & paging gaps
- [single-identity-extraction.md](single-identity-extraction.md) – Identity isolation & permission state gaps
- [garbage-collector-extraction.md](garbage-collector-extraction.md) – Quiet time cleaner scheduling & thresholds gaps

### Root-Monolith Extractions
- [root-monolith-graph-walk-extraction.md](root-monolith-graph-walk-extraction.md) – Data/function graph separation & frame 0 tie-ins
- [root-monolith-step-addresses-layers-extraction.md](root-monolith-step-addresses-layers-extraction.md) – Layered address/domain identifier enumeration
- [root-monolith-memory-module-extraction.md](root-monolith-memory-module-extraction.md) – Acquisition vs non-acquisition unit pipeline
- [root-monolith-frame-switching-extraction.md](root-monolith-frame-switching-extraction.md) – Frame transition & timeline linearization gaps
- [root-monolith-commands-extraction.md](root-monolith-commands-extraction.md) – Command lifecycle gaps & frame 0 privileges
- [root-monolith-phase-0-extraction.md](root-monolith-phase-0-extraction.md) – Phase 0 protected start & reserved IDs extraction
- [root-monolith-libs-extraction.md](root-monolith-libs-extraction.md) – Library provision pathways extraction
- [root-monolith-security-init-extraction.md](root-monolith-security-init-extraction.md) – Security bits / CRC / root.lock() chain extraction
- [root-monolith-phase-sequence-extraction.md](root-monolith-phase-sequence-extraction.md) – Initialization ordered phase sequence extraction
- [root-monolith-monolith-readme-extraction.md](root-monolith-monolith-readme-extraction.md) – Functional inventory & input stream model extraction
- [root-monolith-comprehensive-extraction.md](root-monolith-comprehensive-extraction.md) – Capability groups & VRAM slice references extraction
- [root-monolith-byte-function-load-extraction.md](root-monolith-byte-function-load-extraction.md) – Byte sequence function reconstruction extraction

### Promotion Readiness Extractions
- [frame-0-privilege-boundary-extraction.md](frame-0-privilege-boundary-extraction.md) – Aggregated Frame 0 privilege boundary statements & gaps
- [graph-key-0-enforcement-extraction.md](graph-key-0-enforcement-extraction.md) – Aggregated Graph Key 0 enforcement & ownership gaps
- [user-tape-validation-extraction.md](user-tape-validation-extraction.md) – Aggregated User Tape load order & validation gaps
- [sequence-series-comparison.md](sequence-series-comparison.md) – Sequence vs series graph side-by-side extraction

## Meta & Coverage Documents
- [status-readiness.md](status-readiness.md) – Working-Spec readiness checklist
- [promotion-plan.md](promotion-plan.md) – Promotion batch tracking (completed)
- [origin-docs-modification-report.md](origin-docs-modification-report.md) – Meta audit of historical origin doc interactions
- [origin-derivative-coverage-map.md](origin-derivative-coverage-map.md) – Mapping origin sources to derivative extractions
- [coverage-metrics.md](coverage-metrics.md) – Quantitative origin reference coverage report
- [uncovered-triage.md](uncovered-triage.md) – Classification of remaining uncovered origin files
- [CHANGELOG-docs.md](CHANGELOG-docs.md) – Chronological log of documentation actions

## Tools
- [tools/term_occurrence.py](tools/term_occurrence.py) – Term frequency support script
- [tools/inbound_link_check.py](tools/inbound_link_check.py) – Inbound link gap report script

## Cross-Reference Recommendations
When editing a policy doc:
- Add reciprocal entry here (Source: existing governance addition pattern)
- Ensure [CHANGELOG-docs.md](CHANGELOG-docs.md) updated (Source: CHANGELOG-docs.md practice)

## Incomplete Blocks

```
Incomplete: Policy Coverage Audit
Needed:
- Identify missing governance (e.g., glossary update workflow beyond collisions)
- Determine retention policy for archived seeds
Candidate Sources: sections/glossary.md, CHANGELOG-docs.md
```

```
Incomplete: Incorporation of New Extraction Governance
Needed:
- Confirm whether capability advertisement schema warrants standalone policy doc
- Decide if vector bit semantics require formal policy vs remaining in extraction state
- Determine placement for memory identity unification once gaps resolved
Candidate Sources: capability-advertisement-extraction.md, vector-bits-extraction.md, memory-identity-overview.md, gap-priority-matrix.md
```

Verbatim scope: Listed policy files only.
