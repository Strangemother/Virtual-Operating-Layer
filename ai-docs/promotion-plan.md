Status: Draft
Last-Touched: 2025-09-13
# Promotion Plan (Working-Spec Candidates)

Purpose: List extracted docs ready or near-ready for Status elevation to Working-Spec under current criteria (see status-readiness.md). No behavioral changes introduced.

## Criteria Recap
- All referenced terms present in glossary
- Incomplete blocks isolated and not blocking baseline comprehension
- Inbound links from at least one other doc
- Current Status header with date <= 60 days old

## Candidate Set (Fully Meeting Criteria)
1. graph-overview.md – Meets glossary, inbound links, isolated gaps (Source: graph-overview.md)
2. filesystem-overview.md – Meets criteria; gaps limited to future algorithm detail (Source: filesystem-overview.md)
3. boot-sequence-diagram.md – Linear stage extraction; gaps clearly scoped (Source: boot-sequence-diagram.md)
4. mesh-roles-matrix.md – Role enumeration based solely on sources; gaps isolate schemas (Source: mesh-roles-matrix.md)
5. identity-memory-unification.md – Terminology cross-link; unresolved mapping gaps isolated (Source: identity-memory-unification.md)
6. pointer-0-payload.md – Boot pointer specifics extracted; payload schema marked incomplete (Source: pointer-0-payload.md)
7. sem-tape-extraction.md – SEM tape field gaps isolated (Source: sem-tape-extraction.md)
8. interface-event-taxonomy.md – Event categories pending; extraction stable (Source: interface-event-taxonomy.md)
9. capability-advertisement.md – Capability process summarized; gaps enumerated (Source: capability-advertisement.md)
10. filesystem-layering-outline.md – Structural layering placeholders; no invented rules (Source: filesystem-layering-outline.md)

## Former Near-Candidates (Now Promoted)
mesh-role-derivation.md – Promoted with role enumeration gap retained.
registry-capability-broker.md – Promoted acknowledging minimal scope of source.
onboarding-sequence.md – Promoted; ordering section explicitly non-normative.

## Proposed Promotion Batch 1 (Completed 2025-09-13)
Files: graph-overview.md, filesystem-overview.md, boot-sequence-diagram.md, mesh-roles-matrix.md
Rationale: Core structural visibility for graph, storage, boot, distribution roles.

## Proposed Promotion Batch 2 (Completed 2025-09-13)
Files: identity-memory-unification.md, pointer-0-payload.md, sem-tape-extraction.md, filesystem-layering-outline.md
Rationale: Foundational boot/memory/filesystem conceptual coherence.

## Proposed Promotion Batch 3 (Completed 2025-09-13)
Files: capability-advertisement.md, interface-event-taxonomy.md
Rationale: Interface & mesh onboarding concept surfaces with incomplete schemas isolated.

## Completed Promotions (2025-09-13)
- Batches 1–3 completed; all listed candidates promoted to Working-Spec.
- Status headers updated, Promotion Records appended, status-readiness.md synchronized.
- CHANGELOG-docs.md updated with promotion entries.

## Current State
All originally identified candidates have been elevated. Future promotions will follow policy-promotion.md criteria.

For detailed term-level readiness tracking (Frame 0, Graph Key 0, User Tape, Capability Set), see promotion-candidate-checklist.md. (Source: promotion-candidate-checklist.md)

## Meta Document Status
Meta documents (gap-index.md, gap-priority-matrix.md, governance-index.md, term-collisions.md) remain Draft as they track evolution rather than define specifications.

Verbatim scope: status-readiness.md, CHANGELOG-docs.md, policy-promotion.md, promotion-candidate-checklist.md.
