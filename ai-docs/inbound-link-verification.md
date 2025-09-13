Status: Draft
Last-Touched: 2025-09-13
# Inbound Link Verification Checklist

Purpose: Provide procedure to satisfy promotion criterion requiring at least one inbound link for a document.

## Definitions
Inbound Link – Any reference from another ai-docs file or updated source doc (Backlink line) pointing to the target document. (Source: promotion practice, backlink-plan.md)

## Acceptable Link Forms
1. Inline cross-reference: "See: <relative path>" (Source: existing section cross refs)
2. Backlink line in original source: "Backlink: See extracted summaries ..." (Source: source doc backlink insertions)
3. Index or overview list item referencing filename (Source: status-readiness.md pattern)

## Verification Steps
1. Identify target document path.
2. Grep for filename (case-sensitive) across ai-docs and relevant source dirs.
3. Confirm at least one occurrence not inside the target file itself.
4. Record verification date inside Promotion Record (optional enhancement). (Source: policy-promotion.md incomplete inbound method)
 5. Optional: Run tooling script `tools/inbound_link_check.py` to list files lacking inbound references (Source: tools/inbound_link_check.py)

## Manual Grep Template
```
# Example (conceptual, not executed here):
grep -R "procedure-graph.md" ai-docs/sections docs/core
```
(Source: generic search approach—no automation committed.)

## Failure Handling
If no inbound link found:
- Add reference from nearest cluster overview or glossary if term-heavy.
- Re-run verification.

## Incomplete Blocks
Incomplete: Link Classification Enhancement
Needed:
- Differentiate link types (index vs source relocation vs peer reference)
- Threshold rules (is single index mention sufficient?)
Candidate Sources: policy-promotion.md, backlink-plan.md

Verbatim scope: backlink-plan.md, policy-promotion.md, status-readiness.md, tools/inbound_link_check.py.
