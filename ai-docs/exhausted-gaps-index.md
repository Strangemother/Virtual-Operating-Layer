Status: Draft
Last-Touched: 2025-09-13
Depends-On: gap-closure-roadmap.md, policy-evidence-exhaustion.md
Verbatim scope: gap-closure-roadmap.md, policy-evidence-exhaustion.md, frame-0-privilege-boundary-extraction.md, graph-key-0-enforcement-extraction.md, user-tape-validation-extraction.md, capability-set-schema-extraction.md

# Exhausted Gaps Index

Purpose: Central listing of gaps marked Evidence Exhausted. No new semantics introduced; mirrors per‑document Evidence Exhausted notes.

## Reopen Criteria (Policy Reference)
Triggers requiring gap reactivation (Source: policy-evidence-exhaustion.md):
- New origin document containing potential normative statements
- Design decision record introducing relevant semantics
- Correction of previously uncited origin file uncovered by coverage audit

Procedure on Reopen (Source: policy-evidence-exhaustion.md):
- Remove Evidence Exhausted note in extraction doc
- Insert Pass Reset log (date + trigger file)
- Schedule new systematic pass with planning block

## Exhausted Gaps (2025-09-13)

### Frame 0 (Source: frame-0-privilege-boundary-extraction.md)
- Exclusive Operation Set (Passes: 2) – Await new origin material
- Escalation Criteria (Passes: 2) – Await new origin material
- Security Model (Passes: 2) – Await new origin material
- Namespace/Scope Definition (Passes: 2) – Await new origin material

### Graph Key 0 (Source: graph-key-0-enforcement-extraction.md)
- Enforcement Mechanism (Passes: 2) – Await new origin material
- Reserved ID Registry (Passes: 2) – Await new origin material
- BIOD Role Clarification (Passes: 2) – Await new origin material
- Failure Handling (Passes: 2) – Await new origin material

### User Tape (Source: user-tape-validation-extraction.md)
- Integrity Verification Procedure (Passes: 2) – Await new origin material
- Source Precedence Rules (Passes: 2) – Await new origin material
- Failure Handling Semantics (Passes: 2) – Await new origin material
- Update / Reload Policy (Passes: 2) – Await new origin material
- Security Coupling (Passes: 2) – Await new origin material

### Capability Set (Source: capability-set-schema-extraction.md)
- Field Enumeration (Passes: 2) – Await new origin material
- Matching / Evaluation Algorithm (Passes: 2) – Await new origin material
- Validation & Sanitization (Passes: 2) – Await new origin material
- Security Handling (Passes: 2) – Await new origin material
- Versioning / Evolution (Passes: 2) – Await new origin material
- Translator Selection Coupling (Passes: 2) – Await new origin material

## Cross-List Consistency
All exhausted gaps appear in gap-closure-roadmap.md under 'Awaiting New Source Material' (Source: gap-closure-roadmap.md)

## Incomplete Blocks
```
Incomplete: Exhausted Gap Monitoring Automation
Needed: Script to diff origin tree changes and alert when filenames or content areas associated with exhausted gaps change.
Candidate Sources: coverage-metrics.md, origin-derivative-coverage-map.md
```
```
Incomplete: Reopen Logging Template
Needed: Standard Pass Reset log template referencing original Evidence Exhausted decision.
Candidate Sources: policy-evidence-exhaustion.md
```

Backlinks: Will be added to governance-index.md and gap-closure-roadmap.md
