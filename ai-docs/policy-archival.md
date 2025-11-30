# Policy: Archival Classification
Status: Draft
Last-Touched: 2025-11-30
Depends-On: governance-index.md, uncovered-triage.md, policy-promotion.md

Purpose: Define criteria and tagging conventions for marking origin or derivative documents as `Status: Archival` without deleting historical content. No new technical primitives introduced; policy procedural only.

## Scope
Applies to:
- Origin files in `docs/` deemed historical narrative, exploratory, or superseded.
- Derivative extraction files in `ai-docs/` that become fully replaced by consolidated overviews.

Does NOT apply to:
- Active Working-Spec or Decision documents.
- Files containing unresolved Incomplete blocks critical to core semantics.

## Archival Status Tag
Front-Matter Field: `Status: Archival`
Associated Optional Fields:
- `Superseded-By:` (relative path to replacement doc)
- `Archive-Reason:` (concise phrase: e.g., exploratory narrative, superseded by overview)
- `Last-Reviewed:` YYYY-MM-DD (date archival decision reaffirmed)

## Criteria for Archival
A document MAY be marked Archival if ALL are true:
1. Content is not the most precise or consolidated source for any active glossary term. (Source: governance-index.md referencing glossary maintenance pattern)
2. If superseded, successor document includes explicit sourced statements covering the same conceptual ground. (Source: policy-promotion.md referencing promotion record requirement)
3. No open Incomplete blocks whose resolution would introduce novel normative content. (Source: gap-priority-matrix.md – avoidance of hiding gaps)
4. Triage classification lists file as Historical / Archival candidate. (Source: uncovered-triage.md)

A document MUST NOT be archived if ANY are true:
- It holds the only citation for a glossary entry. (Source: glossary.md referencing single-source risk)
- It contains unresolved Decision rationale still referenced by Working-Spec docs. (Source: policy-promotion.md)
- Coverage metrics show it as the exclusive link target for a high-priority gap. (Source: coverage-metrics.md, gap-priority-matrix.md)

## Process
1. Identify candidate in `uncovered-triage.md`. (Source: uncovered-triage.md)
2. Verify alternative coverage in consolidated extraction or overview doc. (Source: origin-derivative-coverage-map.md)
3. Confirm absence from high-priority gap sources. (Source: gap-priority-matrix.md)
4. Add archival header fields; retain original content body unmodified.
5. Add entry to CHANGELOG with rationale. (Source: CHANGELOG-docs.md)
6. Add backlink note (optional) in successor doc pointing to archived file.

## Reversal
If later evidence shows the archived file contains unique normative content not captured elsewhere:
- Remove `Status: Archival` => revert to `Status: Draft`.
- Create extraction doc referencing its unique sections.
- Update coverage metrics and triage classification.

## Incomplete Blocks
Incomplete: Archival Supersession Verification Automation
Needed:
- Script to verify each archived file has a Superseded-By or Archive-Reason field
- Detection of glossary single-source risk before archival
Candidate Sources: tools/ (future script), glossary.md, coverage-metrics.md

Incomplete: Decision Artifact Interaction
Needed:
- Clarify whether Decision docs can transition to Archival after explicit deprecation record
Candidate Sources: policy-promotion.md

Verbatim scope: governance-index.md, uncovered-triage.md, policy-promotion.md, coverage-metrics.md (referenced patterns only; no additional origin text parsed here).
