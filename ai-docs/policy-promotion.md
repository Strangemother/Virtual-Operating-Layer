Status: Draft
Last-Touched: 2025-09-13
# Documentation Promotion Policy

Purpose: Define criteria and process for moving a document extraction from Draft to Working-Spec without inventing new behaviors.

## Status Definitions
- Draft: Initial extraction; glossary terms may be incomplete; contains Incomplete blocks. (Source: ai-docs/sections/* initial states)
- Working-Spec: All referenced terms present in glossary; no unresolved TODO inside normative sections; at least one inbound link; Status header present and dated within 60 days. (Source: copilot-instructions.md quality bar)

## Promotion Criteria Checklist
A document is eligible when ALL are true:
1. Status header present with Last-Touched date <= 60 days (Source: copilot-instructions.md)
2. Every normative term appears in glossary.md (Source: glossary.md reference practice)
3. All missing information isolated into explicit Incomplete blocks (Source: extraction methodology across ai-docs/sections)
4. No speculative language unmarked by _Speculative:_ prefix (Source: non-speculation principle)
5. At least one cross-reference inbound from index or another section (Source: status-readiness.md pattern)
6. Original source file retains a relocation/backlink note (Source: existing 'Relocated:' pattern e.g., graph pointer.md)

## Promotion Record Template
Append to end of file:
```
---
Promotion Record:
Promoted: YYYY-MM-DD
Basis: Criteria 1-6 satisfied (see policy-promotion.md)
Sources: <file list used in extraction>
```
(Source: existing promotion records in ai-docs/sections/*.md)

## Process
1. Run criteria checklist.
2. Insert Promotion Record block if absent.
3. Update Status: Working-Spec.
4. Update status-readiness.md table entry. (Source: status-readiness.md maintenance practice)
5. Log action in CHANGELOG-docs.md (Source: CHANGELOG-docs.md pattern)

## Deprecation / Drift
If >60 days without touch OR glossary drift detected:
- Mark Status: Stale (Source: copilot-instructions.md freshness rule)
- Insert Incomplete block noting required re-validation scope.

## Incomplete Blocks

Incomplete: Formal Inbound Link Verification Method
Needed:
- Automated or documented manual procedure to confirm at least one inbound link
- Definition of acceptable link forms (index vs peer doc)
Candidate Sources: status-readiness.md, index or navigation doc (TODO: discover)

Verbatim scope: copilot-instructions.md, ai-docs/sections examples (promotion records), status-readiness.md, CHANGELOG-docs.md, glossary.md.
