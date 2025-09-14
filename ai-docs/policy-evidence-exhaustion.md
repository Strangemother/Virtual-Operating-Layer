Status: Draft
Last-Touched: 2025-09-13
Depends-On: gap-closure-roadmap.md, policy-promotion.md
Verbatim scope: gap-closure-roadmap.md, policy-promotion.md

# Policy: Evidence Exhaustion Protocol

Purpose: Define standardized procedure for declaring a gap's current evidence base exhausted without inventing new semantics.

## Scope
Applies to Incomplete blocks in extraction documents under ai-docs/ that have undergone systematic review attempts.

## Definitions
- Systematic Pass: Targeted scan of all origin sources cited in the extraction doc plus sibling thematic docs (same cluster folder) for statements addressing the gap.
- Evidence Exhausted: State where two completed systematic passes yield no additional normative or descriptive statements relevant to the gap.

## Preconditions
All must be true before marking a gap Evidence Exhausted:
1. Extraction doc lists current Incomplete block with clear Needed requirements. (Source: gap-closure-roadmap.md practice)
2. Two Systematic Passes documented with timestamps and source file list. (Source: protocol requirement)
3. No uncited potentially relevant origin file remains in the cluster inventory. (Source: governance need for completeness)
4. Promotion criteria not yet satisfied for term or document (cross-check policy-promotion.md). (Source: policy-promotion.md)

## Procedure
1. Identify gap candidate for second pass completion.
2. Conduct Pass #2 (if Pass #1 already recorded); note any newly discovered files.
3. If no new statements, insert an Evidence Exhausted Note directly ABOVE the Incomplete block:
```
Evidence Exhausted: <gap title>
Passes: 2
Last Pass: YYYY-MM-DD
Sources Reviewed: <comma-separated file list>
Action: Await new origin material or design decision record.
```
4. In `gap-closure-roadmap.md`, move gap under 'Awaiting New Source Material'.
5. Update CHANGELOG-docs.md with entry referencing exhaustion marking.

## Reopening Exhausted Gaps
Trigger conditions:
- New origin document added touching the concept
- Design decision record introduces relevant semantics
Action: Remove Evidence Exhausted note; append Pass Reset log (date + trigger file) below Incomplete block.

## Non-Conformance Handling
If a gap is prematurely marked exhausted (missing pass documentation), revert status and add an Incomplete block:
```
Incomplete: Exhaustion Revalidation
Needed: Re-run systematic passes; supply missing pass evidence.
Candidate Sources: <prior sources + new additions>
```

## Recording Format Examples
Example Evidence Exhausted note:
```
Evidence Exhausted: Frame 0 Security Model
Passes: 2
Last Pass: 2025-09-20
Sources Reviewed: docs/root-monolith/graph-walk.md, docs/root-monolith/commands.md, root-monolith-security-init-extraction.md
Action: Await new origin material or design decision record.
```

## Incomplete Blocks
```
Incomplete: Pass Logging Automation
Needed: Script or checklist template to reduce manual error in pass documentation.
Candidate Sources: governance-index.md (tooling references), tools directory (if extended)
```
```
Incomplete: Cluster Inventory Verification Method
Needed: Standard method to assert no uncited origin files remain before exhaustion claim.
Candidate Sources: uncovered-triage.md, origin-derivative-coverage-map.md
```

Backlinks: Will be referenced by gap-closure-roadmap.md and individual extraction documents upon adoption.

## Standard Pass Planning Block (Template)
To be inserted BEFORE executing a subsequent systematic pass (e.g., Pass #2):
```
Pass Planning: <Pass #>
Scope Expansion: <list added source clusters / file glob patterns>
Primary Objectives: <concise bullet list of what evidence is sought>
Success Criteria: <conditions that would prevent exhaustion marking>
Null Criteria: <conditions that, if met, allow exhaustion after this pass>
Deferral Note: <if pass deferred, reason + prerequisite>
Scheduled: YYYY-MM-DD (planned)
```

## Evidence Exhaustion Decision Block (Template)
Inserted immediately ABOVE the Incomplete block after qualifying passes if gap is declared exhausted:
```
Evidence Exhausted: <gap title>
Passes: <count>
Last Pass: YYYY-MM-DD
Sources Reviewed: <comma-separated file list>
Decision Basis: <reference Pass Planning Block null criteria>
Action: Await new origin material or design decision record.
```

## Adoption & Transitional Use
- Existing extraction docs MAY retroactively add Pass Planning Blocks for already completed Pass #1 (optional; recommended for audit consistency).
- New passes SHOULD include a Pass Planning Block prior to execution per this policy once this file is referenced in an extraction doc or roadmap entry.
- Exhaustion decisions MUST cite the Decision Basis line referencing the null criteria previously declared.

Incomplete: Adoption Confirmation
Needed: Explicit roadmap note acknowledging application start date for standardized Pass Planning Blocks.
Candidate Sources: gap-closure-roadmap.md (pending update)
