Status: Draft
Last-Touched: 2025-09-13
# Gap Normalization Plan

Purpose: Define clustering methodology to convert 384 untracked Incomplete block titles (audit snapshot 2025-09-13) into higher-order aggregated gap headings suitable for inclusion (non-normative) in a Normalization Queue section of active-gaps-index.md without prematurely asserting specifications.

Audit Reference: incomplete-block-audit-report.md (Untracked Blocks section)
Governance References: active-gaps-index.md, gap-priority-matrix.md, gap-resolution-batches.md, policy-evidence-exhaustion.md, governance-index.md

Verbatim scope: incomplete-block-audit-report.md (untracked list only), active-gaps-index.md (current domains), gap-resolution-batches.md (existing thematic groupings)

## Methodology
1. Extraction Integrity
   - Source of every gap title: direct line item from Untracked Blocks list (Source: incomplete-block-audit-report.md)
   - No title modification; aggregated cluster entries will embed original titles verbatim as bullet sub-items.
2. Thematic Clustering Criteria
   - Conceptual cohesion: titles sharing a root abstraction (e.g., capability advertisement schema / field enumeration / negotiation semantics) cluster under a neutral, umbrella label.
   - Avoid normative naming: use "Cluster: <neutral descriptor>" not implying finalized architecture semantics.
   - Minimum cluster size: 2 untracked titles (singletons remain unclustered until a second related item emerges to avoid artificial grouping).
3. Deduplication Handling
   - Duplicate semantic titles across multiple extraction skeletons (e.g., File Names specification in two section contexts) remain listed separately but annotated with "(duplicate context)" once normalization stage 2 commences. Stage 1 (this plan) does not annotate to preserve original audit fidelity.
4. Cross-Domain Overlaps
   - If a title touches two existing active domains (e.g., security + boot), assign to the higher urgency domain per gap-priority-matrix.md ranking when available; else place in "Cross-Domain" cluster.
5. Evidence Exhaustion Guardrail
   - Clustering does not change exhaustion status. Only non-exhausted, untracked items considered. (Source: policy-evidence-exhaustion.md)
6. Output Structure (Normalization Queue)
   - Domain Header → Cluster Heading → Bullet list of original untracked titles with (File: path line X) citation preserved.
   - No Needed: list authored at this stage; those emerge when (if) a cluster is promoted to an Active Gap heading.
7. Promotion Path
   - After clustering, select top clusters (criteria: breadth + architectural centrality + dependency weight) for transformation into formal Active Gap headings with new Incomplete blocks referencing original file citations.

## Preliminary Cluster Set (Stage 1)
(Note: Non-exhaustive; initial 13 clusters cover highest-density thematic areas; remaining titles to be appended iteratively.)

### Graph & Addressing Mechanics
Covers vector bits, key naming encryption, pointer/stepper/compass boundary, collision avoidance, contiguous addressing, stepper predictive computation.
(Representative Sources: graph-overview.md, graph-key-names-extraction.md, contigious-address-names-extraction.md, graph-boundary-outline.md)

### Command Lifecycle & Frame Transition
Covers command schema, lifecycle phases, frame switching authorization, frame transition preconditions, timeline linearization, command-frame coupling.
(Representative Sources: root-monolith-commands-extraction.md, command-frame-lifecycle-skeleton.md, root-monolith-frame-switching-extraction.md)

### Capability Advertisement & Set Schema
Covers capability field enumeration, negotiation/merge, update/revocation semantics, capability set algorithm/validation/versioning, advertisement protocol.
(Representative Sources: capability-advertisement-extraction.md, capability-set-schema-extraction.md, mesh-roles-matrix.md)

### Memory Identity & Persistence
Covers identity persistence mechanics, deterministic reconstruction, tensor identity schema, versioning, streaming reconstruction, security validation.
(Representative Sources: memory-identity-overview.md, memory-identity-states.md, sections/memory-identity.md)

### Filesystem Layering & Particle Model
Covers file names specification, permission externalization, particle phase transitions, orphan recovery, header chain integrity, aggregate mutation workflow, sector/permission/allocation tables.
(Representative Sources: fs-overview.md, sections/filesystem.md, File System.md)

### Boot & Phase Sequencing
Covers integrated boot-security ordering, failure handling, phase mapping tables, pointer 0 payload specification, SEM TAPE format fields, driver selection mapping, loop frequency governance.
(Representative Sources: boot-sequence-linear.md, boot-security-phase-correlation.md, sections/boot-loop.md)

### Security Initialization & Privilege Boundaries
Covers security initialization chain, CRC randomization, root.lock() operation contract, phase-0 protection mechanism, frame 0 privilege boundary enumerations (non-exhausted items only), security ring enforcement.
(Representative Sources: root-monolith-security-init-extraction.md, root-monolith-phase-0-extraction.md, frame-0-privilege-boundary-extraction.md)

### Library Exposure & Auto-Exposure
Covers library auto-exposure rules, vol._vpt schema, module application constraints, library provision mechanisms, exposure precedence, executable exposure contract.
(Representative Sources: library-exposure-pathways-matrix.md, root-monolith-libs-extraction.md, graph-memory-loading-contracts-outline.md)

### Input / Event Taxonomy & Translation
Covers canonical event category list, translator interface specification, event ordering & propagation semantics, security/authorization for input mounting, portal interface contract.
(Representative Sources: input-event-taxonomy.md, sections/interface-event-taxonomy.md, sections/interface-input-events.md)

### Addressing Domains & Layered Space
Covers identifier hierarchy semantics, domain transformation rules, layered addressing domains mapping, vector address specification, vector address collision avoidance, address resolver specification.
(Representative Sources: root-monolith-step-addresses-layers-extraction.md, addressing-domain-enumeration.md, sections/graph-overview.md)

### Coverage & Audit Governance
Covers formal ranking validation, coverage gaps across domains, automated coverage metrics, gap matrix synchronization, batch prioritization confirmation.
(Representative Sources: gap-priority-matrix.md, origin-derivative-coverage-map.md, coverage-metrics.md, gap-resolution-batches.md)

### Evidence Pass & Monitoring Workflow
Covers adoption confirmation, pass logging automation, cluster inventory verification method, exhaustion revalidation triggers, reopened gap index section, automated monitoring triggers.
(Representative Sources: policy-evidence-exhaustion.md, policy-gap-monitoring.md, gap-closure-roadmap.md)

### Glossary & Terminology Normalization
Covers glossary completeness, candidate term formalization, collision resolution procedure dependencies, mesh role taxonomy terms, memory identity detailed enumeration, boot sequence nomenclature normalization.
(Representative Sources: sections/glossary.md, term-collisions.md, term-promotion-readiness-matrix.md)

## Next Actions
1. Extend cluster membership lists by enumerating each untracked title under the preliminary cluster headers (non-normative).
2. Insert Normalization Queue section into active-gaps-index.md referencing this plan.
3. Update governance-index.md to register this plan file.
4. Append changelog entry summarizing addition of normalization plan and queue insertion.

### Progress Log
- 2025-09-13: Graph & Addressing Mechanics cluster enumerated (40 titles) → gap-cluster-membership.md and active-gaps-index.md Normalization Queue updated. Remaining untracked titles pending clustering: 344.
 - 2025-09-13: Command Lifecycle & Frame Transition cluster enumerated (14 titles). Remaining untracked titles pending clustering: 330.
 - 2025-09-13: Capability Advertisement & Set Schema cluster enumerated (21 titles). Remaining untracked titles pending clustering: 309.
 - 2025-09-13: Memory Identity & Persistence cluster enumerated (37 titles). Remaining untracked titles pending clustering: 272.
 - 2025-09-13: Filesystem Layering & Particle Model cluster enumerated (27 titles). Remaining untracked titles pending clustering: 245.
 - 2025-09-13: Boot & Phase Sequencing cluster enumerated (38 titles). Remaining untracked titles pending clustering: 207.
 - 2025-09-13: Security Initialization & Privilege Boundaries cluster enumerated (19 titles). Remaining untracked titles pending clustering: 188.
 - 2025-09-13: Library Exposure & Auto-Exposure cluster enumerated (12 titles). Remaining untracked titles pending clustering: 176.
 - 2025-09-13: Input / Event Taxonomy & Translation cluster enumerated (21 titles). Remaining untracked titles pending clustering: 155.
 - 2025-09-13: Addressing Domains & Layered Space cluster enumerated (6 titles). Remaining untracked titles pending clustering: 149.
 - 2025-09-13: Coverage & Audit Governance cluster enumerated (17 titles). Remaining untracked titles pending clustering: 132.
 - 2025-09-13: Evidence Pass & Monitoring Workflow cluster enumerated (9 titles). Remaining untracked titles pending clustering: 123.
 - 2025-09-13: Glossary & Terminology Normalization cluster enumerated (17 titles). Remaining untracked titles pending clustering: 106.
 - 2025-09-13: Parser refinement applied (cluster_validation.py) limiting membership capture to '(File:' bullets; coverage recalculated: 281 enumerated / 384 total (72.1%), 107 currently unclustered (see: unclustered-titles.md). Prior remaining count (106) undercounted by 1 due to duplicate normalization edge case.

## Incomplete Blocks
Incomplete: Cluster Membership Enumeration
Needed:
- Full bullet listing of all 384 untracked titles mapped to exactly one cluster or marked singleton
- Identification of any titles requiring new cluster creation (beyond initial 13)
Candidate Sources: incomplete-block-audit-report.md

Incomplete: Promotion Candidate Cluster Selection Criteria
Needed:
- Weighted scoring rubric (density, architectural centrality, dependency impact)
- Threshold for elevating cluster to Active Gap domain heading
Candidate Sources: gap-priority-matrix.md, gap-resolution-batches.md

_No speculative semantics introduced. All clusters are organizational scaffolding only._
