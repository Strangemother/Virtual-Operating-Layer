Status: Draft
Last-Touched: 2025-09-13
Depends-On: term-promotion-readiness-matrix.md, sections/glossary.md, policy-promotion.md
Verbatim scope: term-promotion-readiness-matrix.md, sections/glossary.md

# Promotion Candidate Checklist (Frame 0, Graph Key 0, User Tape, Capability Set)

Purpose: Enumerate readiness evidence and remaining gaps for each Ready Candidate prior to Status elevation. No new semantics introduced.

## Criteria (From policy-promotion.md)
Eligibility conditions (all must be satisfied before elevating any candidate term's host doc):
1. Status header present with Last-Touched date ≤ 60 days (Source: policy-promotion.md)
2. Every normative term in the candidate definition appears in `sections/glossary.md` (Source: policy-promotion.md)
3. All missing information isolated into explicit Incomplete blocks (Source: policy-promotion.md)
4. No unmarked speculative language (`_Speculative:` prefix required if present) (Source: policy-promotion.md)
5. At least one inbound cross-reference from an index or other section file (Source: policy-promotion.md)
6. Original source(s) retain relocation/backlink notice when consolidation occurred (Source: policy-promotion.md)
Additional Term-Specific Pre-Conditions (Working-Term → Stable Term):
- Collision-free: Not listed in `term-collisions.md` pending resolution (Source: term-collisions.md)
- Multi-source: Cited by ≥2 distinct origin-derived extraction docs unless inherently singleton (must be justified) (Source: term-promotion-readiness-matrix.md usage pattern)
- Core gap closed: Primary blocking Incomplete block for the term resolved or narrowed with explicit non-normative deferral note (Source: current checklist practice)

## Candidates

### Frame 0
Sources: sections/glossary.md (graph-walk.md; commands.md), root-monolith-graph-walk-extraction.md, root-monolith-commands-extraction.md, frame-0-privilege-boundary-extraction.md
Evidence:
- Referenced in multiple extraction docs establishing early command handling context (Source: root-monolith-graph-walk-extraction.md; root-monolith-commands-extraction.md)
Gaps (Evidence Exhausted 2025-09-13):
```
Incomplete: Frame 0 Privilege Boundary
Needed: Exclusive operations allowed only in frame 0; security model; escalation pathway rules.
Candidate Sources: docs/root-monolith/graph-walk.md, docs/root-monolith/commands.md, root-monolith-frame-switching-extraction.md
```
Blocking Issues:
- Privilege boundary elements absent; currently Evidence Exhausted pending new origin material (Source: frame-0-privilege-boundary-extraction.md)
Linked Gap Doc: frame-0-privilege-boundary-extraction.md

### Graph Key 0
Sources: sections/glossary.md (phase-0.md; readme.md), root-monolith-phase-0-extraction.md, root-monolith-monolith-readme-extraction.md, graph-key-0-enforcement-extraction.md
Evidence:
- Defined as protected start point initiating config/module installation (multi-source) (Source: sections/glossary.md)
Gaps (Evidence Exhausted 2025-09-13):
```
Incomplete: Reserved Graph Key Enforcement
Needed: Validation process for protected start key; tamper detection steps; fallback behavior on failure.
Candidate Sources: docs/root-monolith/phase-0.md, docs/root-monolith/readme.md, root-monolith-security-init-extraction.md
```
Blocking Issues:
- Enforcement workflow absent; gap Evidence Exhausted awaiting new source (Source: graph-key-0-enforcement-extraction.md)
Linked Gap Doc: graph-key-0-enforcement-extraction.md

### User Tape
Sources: sections/glossary.md (phases.md), root-monolith-phase-sequence-extraction.md, boot-security-phase-correlation.md, user-tape-validation-extraction.md
Evidence:
- Phase sequence enumerates load of first user tape after baseline preparation (Source: root-monolith-phase-sequence-extraction.md)
Gaps (Evidence Exhausted 2025-09-13):
```
Incomplete: User Tape Validation
Needed: Integrity verification steps; allowed sources precedence; failure handling semantics.
Candidate Sources: docs/root-monolith/phases.md, root-monolith-phase-sequence-extraction.md
```
Blocking Issues:
- Validation semantics & precedence rules missing; gaps Evidence Exhausted (Source: user-tape-validation-extraction.md)
Linked Gap Doc: user-tape-validation-extraction.md

### Capability Set
Sources: sections/glossary.md (nodes.md), capability-advertisement-extraction.md, mesh-roles-matrix.md, capability-set-schema-extraction.md
Evidence:
- Governs role integration when new RUNTIME meshes into existing session (Source: nodes.md; capability-advertisement-extraction.md)
Gaps (Evidence Exhausted 2025-09-13):
```
Incomplete: Capability Set Schema
Needed: Field list; mandatory vs optional attributes; matching/evaluation algorithm; disallowed field handling.
Candidate Sources: docs/nodes.md, capability-advertisement-extraction.md, mesh-roles-matrix.md
```
Blocking Issues:
- No schema fields enumerated; gaps Evidence Exhausted (Source: capability-set-schema-extraction.md)
Linked Gap Doc: capability-set-schema-extraction.md

## Summary Table (Textual)
- Frame 0: Multi-source ✅ / Collision-free ✅ / Boundary gap ❌ → Blocked
- Graph Key 0: Multi-source ✅ / Collision-free ✅ / Enforcement gap ❌ → Blocked
- User Tape: Multi-source ✅ / Collision-free ✅ / Validation gap ❌ → Blocked
- Capability Set: Multi-source ✅ / Collision-free ✅ / Schema gap ❌ → Blocked
Roadmap Reference: See gap-closure-roadmap.md (Awaiting New Source Material section) & exhausted-gaps-index.md for exhaustion status tracking.

## Next Actions (Non-Speculative)
1. Extract explicit promotion criteria from policy-promotion.md (once authored) (Source: policy-promotion.md)
2. Resolve each candidate's primary gap block before proposing status elevation.
3. Add cross-links from each extraction doc to this checklist for visibility (post gap closure).

Backlinks: Will be referenced by governance-index.md, term-promotion-readiness-matrix.md
