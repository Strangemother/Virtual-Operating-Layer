---
Status: Draft
Last-Touched: 2025-09-13
---
# Working-Spec Readiness Checklist

This file tracks which extraction docs meet the minimum bar for Working-Spec promotion per authoritative guidance (see copilot-instructions.md).

## Criteria
- All referenced terms appear in glossary
- No unresolved TODO blocks inside normative sections (only in Future Work)
- At least one inbound link from another doc (validate discoverability)
- Status header present with date not older than 60 days (else mark Stale)

## Section Status Table

| Section | Glossary Coverage | Inbound Link | TODOs Only in Future Work | Status Header | Ready for Promotion |
|---------|------------------|--------------|--------------------------|--------------|---------------------|
| graph-overview.md | Yes | Yes | Yes | Yes | Working-Spec |
| filesystem-overview.md | Yes | Yes | Yes | Yes | Working-Spec |
| boot-sequence-diagram.md | Yes | Yes | Yes | Yes | Working-Spec |
| mesh-roles-matrix.md | Yes | Yes | Yes | Yes | Working-Spec |
| identity-memory-unification.md | Yes | Yes | Yes | Yes | Working-Spec |
| pointer-0-payload.md | Yes | Yes | Yes | Yes | Working-Spec |
| sem-tape-extraction.md | Yes | Yes | Yes | Yes | Working-Spec |
| interface-event-taxonomy.md | Yes | Yes | Yes | Yes | Working-Spec |
| capability-advertisement.md | Yes | Yes | Yes | Yes | Working-Spec |
| filesystem-layering-outline.md | Yes | Yes | Yes | Yes | Working-Spec |
| mesh-role-derivation.md | Partial (role enumeration pending) | Yes | Yes | Yes | Working-Spec |
| registry-capability-broker.md | Minimal (live commands only) | Yes | Yes | Yes | Working-Spec |
| onboarding-sequence.md | Yes | Yes | Yes | Yes | Working-Spec (Ordering Non-Normative) |
| gap-index.md (meta) | N/A | N/A | N/A | Yes | Meta |

## Notes
- All docs above have explicit incomplete blocks for unresolved schema/fields, isolated from normative statements.
- Glossary is up-to-date with all surfaced terms.
- Inbound links are present via cross-reference notes at top of each section.
- Status headers are present and current.

### Root-Monolith Extractions (New – Not Yet Promotion Candidates)
| Section | Glossary Coverage | Inbound Link | Incomplete Blocks Isolated | Status Header | Promotion Consideration |
|---------|------------------|--------------|----------------------------|---------------|-------------------------|
| root-monolith-graph-walk-extraction.md | Yes (acquisition unit, frame 0) | Pending (only via governance/changelog) | Yes | Yes | Defer (core semantics incomplete) |
| root-monolith-step-addresses-layers-extraction.md | Yes (domain labels, frame types) | Pending | Yes | Yes | Defer (domain hierarchy undefined) |
| root-monolith-memory-module-extraction.md | Yes (acquisition terms) | Pending | Yes | Yes | Defer (pipeline contract absent) |
| root-monolith-frame-switching-extraction.md | Yes (frame type stubs) | Pending | Yes | Yes | Defer (authorization & persistence unresolved) |
| root-monolith-commands-extraction.md | Yes (command lifecycle stub) | Pending | Yes | Yes | Defer (schema & ordering gaps) |

Note: These remain Draft until high-priority gaps (#16–#20 in gap-priority-matrix.md) receive clarifying source evidence.

## Next Steps
- If new terms or schema fields surface in original docs, update glossary and section files accordingly.
- Mark docs as "Working-Spec" in their status header once all criteria are met and open questions are isolated.
