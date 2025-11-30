---
Status: Draft
Last-Touched: 2025-11-30
Owner: TODO
---
# VOL Documentation Index (AI Restructured Set)

Central navigation hub for the Virtual Operating Layer conceptual documentation. Each section preserves citations and Incomplete blocks with no speculative additions.

## Quick Navigation
- [Overview Index](overview-index.md) – Consolidated high-level overviews
- [Governance Index](governance-index.md) – Policy and procedure documents
- [Glossary](sections/glossary.md) – Comprehensive term definitions
- [Gap Index](gap-index.md) – All unresolved specification items
- [Term Collisions](term-collisions.md) – Naming conflict tracking

## Core Concept Sections
1. [Core Runtime & Lifecycle](sections/core-runtime.md) – Managing thread, terminology layers, kernel caveats, phase outline.
2. [Procedure Graph Model](sections/procedure-graph.md) – Graph execution entities (pointer, stepper), vector naming, compass, SES.
3. [Filesystem & Storage Layers](sections/filesystem.md) – Aggregate/Phenocryst, grains/particles, colloid resolution, header chain.
4. [Memory & Identity Model](sections/memory-identity.md) – NN-as-file concept, compression hypothesis, identity/security gaps.
5. [Mesh / Nodes / Registry / Scaling](sections/mesh-placeholder.md) – Membranes, node onboarding, distribution & scaling primitives.
6. [Mesh Role Taxonomy](sections/mesh-roles.md) – Extracted role/entity list (CORE, RUNTIME, NODE, CONTAINER, registry) with gaps.
7. [Boot & Loop Sequence](sections/boot-loop.md) – Boot SEM→MBR→Zero Suite→pointer 0 lifecycle and runtime loop walker.
8. [Boot Sequence Table](sections/boot-sequence-table.md) – Linearized phase list with explicit incomplete format gaps.
9. [Interface & Display Layer](sections/interface-placeholder.md) – Container rendering pipeline, inputs, facades, branding.
10. [Interface Input Events](sections/interface-input-events.md) – Input flow extraction (mount sources, translator role, event propagation) and gaps.
11. [Root & Foundational Apps / Containerization](sections/root-apps-placeholder.md) – Root fundamentals, manifest, first demo apps.
12. [Identity Persistence Model](sections/identity-persistence.md) – Data-as-NN concept extraction and unresolved mapping gaps.
13. [Open Questions Index](sections/open-questions.md) – Consolidated unresolved specification items.
14. [Glossary Seed](sections/glossary.md) – Expanded term set; remaining targeted gaps.
15. [SEM TAPE Extraction](sections/sem-tape-extraction.md) – Collated SEM TAPE & mcom references with field gaps.
16. [Pointer 0 Payload Extraction](sections/pointer-0-payload.md) – Executable payload statements and schema gaps.
17. [Interface Event Taxonomy](sections/interface-event-taxonomy.md) – Event category mentions & unresolved schema.
18. [Capability Advertisement](sections/capability-advertisement.md) – Onboarding capability capture statements & field gaps.
19. [Filesystem Layering Outline](sections/filesystem-layering-outline.md) – Enumerated entities (aggregate→particle) with layering gaps.
20. [Graph Subsystem Overview](sections/graph-overview.md) – Consolidated pointer/stepper/SES/compass/naming/security extraction.
21. [Graph Supersession Notes](relocations/graph-superseded-notes.md) – Mapping of original graph docs to overview.
22. [Filesystem Overview](sections/filesystem-overview.md) – Collated filesystem entities, naming & resolution references.
23. [Boot Sequence Diagram Stub](sections/boot-sequence-diagram.md) – Linear textual stage list with gaps.
24. [Identity & Memory Unification](sections/identity-memory-unification.md) – Grains/slots/identity tensor linkage gaps.
25. [Mesh Roles Matrix](sections/mesh-roles-matrix.md) – Role capability enumeration & unresolved schema.

## Document Status Legend
- **Draft**: Initial extraction; may have glossary gaps and incomplete blocks
- **Working-Spec**: Meets all promotion criteria; ready for reference
- **Meta**: Tracking/governance document not subject to promotion

## Source Integrity
All normative bullets cite original files under `../docs/`. Incomplete blocks enumerate explicit missing facts with candidate sources. No behaviors invented.

## Next Steps (Non-speculative)
1. Capture any newly surfaced explicit naming tokens (if added to original docs) for SEM TAPE, pointer 0, capability fields, event categories.
2. Cross-link overview docs inside related section files (in-document See: references) without altering originals.
3. Prepare Working-Spec readiness checklist: ensure glossary coverage, inbound links, unresolved TODO isolation.
4. Identify minimal candidate docs for status elevation (likely: graph-overview, filesystem-overview) once missing field enumerations appear in sources.
5. Maintain open-questions synchronization: mark partial resolutions only after explicit names present in source docs.

Verbatim scope: Aggregated pointers only; refer to each section file for detailed citations.
