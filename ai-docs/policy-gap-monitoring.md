Status: Draft
Last-Touched: 2025-09-13
Depends-On: policy-evidence-exhaustion.md, exhausted-gaps-index.md, gap-closure-roadmap.md
Verbatim scope: policy-evidence-exhaustion.md, exhausted-gaps-index.md, gap-closure-roadmap.md

# Policy: Gap Monitoring & Reopen Triggers

Purpose: Define monitoring triggers for transitioning Evidence Exhausted gaps back into active investigation. No new semantics; references existing exhaustion protocol.

## Triggers (Source: policy-evidence-exhaustion.md)
- New origin file added in docs/ clusters containing keywords associated with exhausted gap titles
- Modification to an origin file previously cited with only descriptive context (potential new normative addition)
- Addition of a design decision record referencing an exhausted gap concept
- Discovery (via coverage audit) of uncited origin file relevant to exhausted concept

## Monitoring Inputs (Source: exhausted-gaps-index.md; gap-closure-roadmap.md)
- Exhausted gap list (primary index)
- Roadmap 'Awaiting New Source Material' section alignment
- Coverage metrics deltas (coverage-metrics.md) identifying new or changed origin files

## Reopen Procedure (Source: policy-evidence-exhaustion.md)
1. Remove 'Evidence Exhausted' note in extraction doc.
2. Insert Pass Reset log:
```
Pass Reset: <gap title>
Trigger: <file or decision record>
Date: YYYY-MM-DD
Action: Schedule new systematic pass.
```
3. Add new Pass Planning Block enumerating expanded or changed scope.
4. Update exhausted-gaps-index.md moving gap to 'Reopened' subsection (to be created upon first reopen event).
5. Log change in CHANGELOG-docs.md.

## Incomplete Blocks
```
Incomplete: Automated Trigger Detection
Needed: Script spec to watch git diff for origin doc additions/changes touching exhausted gap keyword set.
Candidate Sources: coverage-metrics.md, origin-derivative-coverage-map.md
```
```
Incomplete: Reopened Gap Index Section
Needed: Structural layout for tracking reopened history (timestamp, trigger, new pass outcomes).
Candidate Sources: exhausted-gaps-index.md
```

Backlinks: Will be added to governance-index.md
