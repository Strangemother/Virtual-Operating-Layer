Status: Draft
Last-Touched: 2025-09-13
Depends-On: frame-0-privilege-boundary-extraction.md, graph-key-0-enforcement-extraction.md, user-tape-validation-extraction.md, capability-set-schema-extraction.md, promotion-candidate-checklist.md
Verbatim scope: listed extraction docs and promotion-candidate-checklist.md

# Gap Closure Roadmap (Promotion Blockers)

Purpose: Central consolidation of unresolved Incomplete blocks inhibiting promotion of Ready Candidate terms. No new semantics added.

## Prioritization Principles
1. Boot / Early Integrity First (Frame 0, Graph Key 0)
2. Configuration & User Onboarding (User Tape)
3. Mesh Distribution / Scaling (Capability Set)

## Blocker Inventory

### Frame 0 (Privilege Boundary)
Source Doc: frame-0-privilege-boundary-extraction.md
Incomplete Blocks:
- Exclusive Operation Set
- Escalation Criteria
- Security Model
- Namespace/Scope Definition
Status: Evidence Pass #1 completed 2025-09-13 – no new source evidence located (See: frame-0-privilege-boundary-extraction.md Evidence Pass #1 Log).
Next Action: Schedule Evidence Pass #2 expanding scope to core/ graph docs; defer until after Batch B initialization unless promotion urgency escalates.

### Graph Key 0 (Enforcement)
Source Doc: graph-key-0-enforcement-extraction.md
Incomplete Blocks:
- Enforcement Mechanism
- Reserved ID Registry
- BIOD Role Clarification
- Failure Handling
Status: Evidence Pass #1 completed 2025-09-13 – no enforcement mechanism evidence surfaced (See: graph-key-0-enforcement-extraction.md Evidence Pass #1 Log).
Next Action: Plan Evidence Pass #2 including broader security-related origin docs; evaluate early marking criteria after second pass per policy-evidence-exhaustion.md.

### User Tape (Validation)
Source Doc: user-tape-validation-extraction.md
Incomplete Blocks:
- Integrity Verification Procedure
- Source Precedence Rules
- Failure Handling Semantics
- Update / Reload Policy
- Security Coupling
Status: Evidence Pass #1 completed 2025-09-13 – no validation / precedence / failure semantics discovered (See: user-tape-validation-extraction.md Evidence Pass #1 Log).
Next Action: Plan Evidence Pass #2 including CRC service and security research docs; if still null, evaluate evidence exhaustion marking criteria.

### Capability Set (Schema)
Source Doc: capability-set-schema-extraction.md
Incomplete Blocks:
- Field Enumeration
- Matching / Evaluation Algorithm
- Validation & Sanitization
- Security Handling
- Versioning / Evolution
- Translator Selection Coupling
Status: Evidence Pass #1 completed 2025-09-13 – no schema, evaluation, validation, or security semantics discovered (See: capability-set-schema-extraction.md Evidence Pass #1 Log).
Next Action: Schedule Evidence Pass #2 (mesh, scaling, registry, security docs). If still null, evaluate evidence exhaustion marking.

## Cross-Cutting Gaps
- Security Chain Coupling: Frame 0 boundary + Graph Key 0 enforcement + User Tape security ordering (Sources: respective extraction docs)
- Role Assignment Determinism: Capability set matching + translator selection dependency (Sources: capability-set-schema-extraction.md)

## Suggested Resolution Batch Sequence
1. Batch A (Integrity Core): Frame 0 + Graph Key 0 (attempt evidence expansion or mark evidence exhausted)
2. Batch B (User Configuration): User Tape validation semantics
3. Batch C (Mesh Onboarding): Capability set schema placeholders & evaluation algorithm gap structuring

### Upcoming Pass Planning (Queued)
Batch B – Evidence Pass #1 (Planned):
- Scope: user-tape-validation-extraction.md; origin docs referencing tape / load order.
- Objective: Surface any latent integrity verification or precedence semantics.
- Not Started: Pending completion of Batch A Pass #2 decision point.

Batch C – Evidence Pass #1 (Planned):
- Scope: capability-set-schema-extraction.md; origin mentions of capability advertisement / matching.
- Objective: Identify any implicit field enumeration or evaluation sequence hints.
- Not Started: Queued after Batch B.

### Unified Pass #2 Planning (Adopted Templates)
Adoption Date: 2025-09-13 (See: policy-evidence-exhaustion.md 'Adoption & Transitional Use')

Integrity Core Pass #2 (Frame 0 + Graph Key 0):
- Execute prior to User Tape Pass #2; required before considering exhaustion for either Frame 0 or Graph Key 0.
- Use Pass Planning Blocks already inserted in respective extraction docs.

User Tape Pass #2:
- Run after Integrity Core Pass #2 start; may overlap Capability Set Pass #2.
- Follow Pass Planning Block inserted in user-tape-validation-extraction.md.

Capability Set Pass #2:
- Parallel permissible with User Tape Pass #2 once Integrity Core Pass #2 initiated.
- Follow Pass Planning Block in capability-set-schema-extraction.md.

Exhaustion Decision Gate:
- Only evaluated after each domain's Pass #2 null criteria met and cluster inventory verification complete.

Pending: Insert Adoption Confirmation (policy-evidence-exhaustion.md Incomplete: Adoption Confirmation) once first Pass #2 begins.
Adoption Confirmation: Pass #2 execution initiated 2025-09-13 (Integrity Core – Frame 0, Graph Key 0). (Source: frame-0-privilege-boundary-extraction.md; graph-key-0-enforcement-extraction.md)

### Integrity Core Inventory Verification (2025-09-13)
Status: Completed for Frame 0 and Graph Key 0 (Sources: frame-0-privilege-boundary-extraction.md Inventory Verification; graph-key-0-enforcement-extraction.md Inventory Verification)
Findings: Null – no additional normative statements surfaced beyond previously extracted minimal characterizations (Sources: same – absence noted)
Readiness: Both components meet null criteria; deferred exhaustion decision until User Tape & Capability Set Pass #2 results incorporated (Source: policy-evidence-exhaustion.md)
Next Action: Execute User Tape & Capability Set Pass #2, then perform unified exhaustion evaluation gate.

### User Configuration & Mesh Onboarding Pass #2 (2025-09-13)
Status: Completed Pass #2 for User Tape (null) and Capability Set (null) (Sources: user-tape-validation-extraction.md Evidence Pass #2 Log; capability-set-schema-extraction.md Evidence Pass #2 Log)
Findings: No integrity verification, precedence, failure handling, schema field enumeration, evaluation ordering, or security mitigation statements located (Sources: same – absence noted)
Readiness: All four blockers have completed two passes (Frame 0, Graph Key 0, User Tape, Capability Set). Inventory verification pending only for User Tape & Capability Set (to be executed prior to exhaustion decision if required; scope likely enumerated implicitly by Pass #2 query sets) (Source: policy-evidence-exhaustion.md)
Next Action: Evaluate exhaustion preconditions across all four; prepare unified Evidence Exhaustion Decision entries if criteria satisfied.

## Evidence Exhaustion Protocol (Proposed)
Trigger: After two systematic passes yield no new normative statements.
Record: Insert note "Evidence Exhausted: <gap>" inside extraction doc above Incomplete block.
Action: Move gap to 'Awaiting New Source Material' section here.

Incomplete: Evidence Exhaustion Procedure Confirmation
Needed: Formal approval to adopt proposed protocol for unresolved gaps.
Candidate Sources: policy-promotion.md (extension), governance-index.md

Policy Reference: See policy-evidence-exhaustion.md for formal procedure once adopted.

Backlinks: Will be added to individual extraction docs and promotion-candidate-checklist.md

## Awaiting New Source Material (Evidence Exhausted) – 2025-09-13
Frame 0 (Privilege Boundary):
- Exclusive Operation Set (Evidence Exhausted; Passes: 2) (Source: frame-0-privilege-boundary-extraction.md)
- Escalation Criteria (Evidence Exhausted; Passes: 2) (Source: frame-0-privilege-boundary-extraction.md)
- Security Model (Evidence Exhausted; Passes: 2) (Source: frame-0-privilege-boundary-extraction.md)
- Namespace/Scope Definition (Evidence Exhausted; Passes: 2) (Source: frame-0-privilege-boundary-extraction.md)

Graph Key 0 (Enforcement):
- Enforcement Mechanism (Evidence Exhausted; Passes: 2) (Source: graph-key-0-enforcement-extraction.md)
- Reserved ID Registry (Evidence Exhausted; Passes: 2) (Source: graph-key-0-enforcement-extraction.md)
- BIOD Role Clarification (Evidence Exhausted; Passes: 2) (Source: graph-key-0-enforcement-extraction.md)
- Failure Handling (Evidence Exhausted; Passes: 2) (Source: graph-key-0-enforcement-extraction.md)

User Tape (Validation):
- Integrity Verification Procedure (Evidence Exhausted; Passes: 2) (Source: user-tape-validation-extraction.md)
- Source Precedence Rules (Evidence Exhausted; Passes: 2) (Source: user-tape-validation-extraction.md)
- Failure Handling Semantics (Evidence Exhausted; Passes: 2) (Source: user-tape-validation-extraction.md)
- Update / Reload Policy (Evidence Exhausted; Passes: 2) (Source: user-tape-validation-extraction.md)
- Security Coupling (Evidence Exhausted; Passes: 2) (Source: user-tape-validation-extraction.md)

Capability Set (Schema):
- Field Enumeration (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)
- Matching / Evaluation Algorithm (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)
- Validation & Sanitization (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)
- Security Handling (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)
- Versioning / Evolution (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)
- Translator Selection Coupling (Evidence Exhausted; Passes: 2) (Source: capability-set-schema-extraction.md)

Reopen Criteria: Addition of new origin doc or decision record addressing any exhausted gap (See: policy-evidence-exhaustion.md)
