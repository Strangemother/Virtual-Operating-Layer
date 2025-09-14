Status: Draft
Last-Touched: 2025-09-13
Depends-On: capability-advertisement-extraction.md, mesh-roles-matrix.md, sections/glossary.md
Verbatim scope: capability-advertisement-extraction.md, mesh-roles-matrix.md, sections/glossary.md

# Capability Set Schema (Extraction)

Purpose: Aggregate sourced statements referencing capability set usage in mesh onboarding and translator/role integration. Surface absent schema fields & evaluation rules. No new semantics introduced.

## Sourced Statements
1. Role integration governed by capabilities of new RUNTIME (capability set) when meshing into existing SESSION. (Source: capability-advertisement-extraction.md)
2. Capability Set governs role integration when new RUNTIME connects. (Source: mesh-roles-matrix.md)
3. Capability Set (glossary) defined as aggregate capabilities of new RUNTIME governing its role integration. (Source: sections/glossary.md)
4. Matching logic between capability set and chosen translator not specified. (Source: sections/capability-advertisement.md)
5. Explicit mapping rule from capability set to assigned mesh role absent. (Source: sections/capability-advertisement.md)
6. Handling of malicious or overstated capability sets identified as gap. (Source: capability-advertisement-extraction.md)

## Observed Themes (Descriptive)
- Central Selection Input: Capability set influences translator choice and mesh role assignment.
- Security Concern: Overstatement or malicious declaration considered but not defined.
- Absent Formal Schema: No enumerated fields, required vs optional segregation, or validation ordering.

## Incomplete Blocks
Evidence Exhausted: Field Enumeration
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, docs/Scaling.md, docs/registry.md, capability-advertisement-extraction.md, mesh-roles-matrix.md, sections/glossary.md, docs/root-monolith/security research.md
Decision Basis: Null criteria met (no field list or grouping surfaced) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Field Enumeration
Needed: Canonical list of capability set fields; minimal mandatory subset; grouping (e.g., compute, memory, IO, mesh-relay).
Candidate Sources: docs/nodes.md, capability-advertisement-extraction.md
```
Evidence Exhausted: Matching / Evaluation Algorithm
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, docs/Scaling.md, docs/registry.md, capability-advertisement-extraction.md, mesh-roles-matrix.md
Decision Basis: Null criteria met (no deterministic process statements discovered) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Matching / Evaluation Algorithm
Needed: Deterministic process for mapping capability set to translator and mesh role.
Candidate Sources: capability-advertisement-extraction.md, mesh-roles-matrix.md
```
Evidence Exhausted: Validation & Sanitization
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, capability-advertisement-extraction.md, docs/root-monolith/security research.md
Decision Basis: Null criteria met (no rejection or normalization rules) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Validation & Sanitization
Needed: Rules for rejecting malformed/overstated capability sets; normalization steps.
Candidate Sources: capability-advertisement-extraction.md
```
Evidence Exhausted: Security Handling
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, docs/root-monolith/security research.md, capability-advertisement-extraction.md
Decision Basis: Null criteria met (no mitigation or detection strategy statements) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Security Handling
Needed: Detection & response strategy for malicious capability overstatement or spoofed declarations.
Candidate Sources: capability-advertisement-extraction.md
```
Evidence Exhausted: Versioning / Evolution
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, docs/Scaling.md, docs/registry.md, capability-advertisement-extraction.md
Decision Basis: Null criteria met (no evolution mechanism references) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Versioning / Evolution
Needed: Mechanism (if any) for extending capability set fields while preserving backward compatibility.
Candidate Sources: capability-advertisement-extraction.md
```
Evidence Exhausted: Translator Selection Coupling
Passes: 2
Last Pass: 2025-09-13
Sources Reviewed: docs/mesh.md, docs/nodes.md, capability-advertisement-extraction.md, mesh-roles-matrix.md
Decision Basis: Null criteria met (no dependency ordering statements) per Pass #2 planning block.
Action: Await new origin material or design decision record.
```
Incomplete: Translator Selection Coupling
Needed: Explicit dependency ordering between capability evaluation and translator assignment.
Candidate Sources: sections/capability-advertisement.md
```

## Gap Relationship
Primary blocker preventing Capability Set term promotion (See: promotion-candidate-checklist.md; term-promotion-readiness-matrix.md)

Backlinks: Will be registered in governance-index.md and promotion-candidate-checklist.md
Roadmap Backlink: See gap-closure-roadmap.md for aggregated blocker prioritization
Evidence Exhaustion Policy: See policy-evidence-exhaustion.md for marking protocol

## Evidence Pass #1 Log (2025-09-13)
Scope: Origin docs and relocated notes scanned for explicit capability set schema, evaluation, validation, or security semantics.

Search Queries Executed:
- "capability set" (no direct origin matches) (Source: search results summary – absence noted)
- "capability-set" (no matches) (Source: search results summary – absence noted)
- "capabilities" (Sources: docs/nodes.md; docs/discussion/gnu.md; docs/display (container).md)
- "capability" (Source: docs/nodes.md; docs/registry.md relocation note only)

Findings:
1. nodes.md references capturing capabilities of new RUNTIME to integrate into MESH; no field granularity. (Source: docs/nodes.md)
2. registry.md relocation line provides link context only; no schema clauses. (Source: docs/registry.md)
3. discussion/gnu.md uses term capabilities in general context without structured schema meaning. (Source: docs/discussion/gnu.md)
4. display (container).md mentions drawing capabilities unrelated to mesh onboarding capability set schema. (Source: docs/display (container).md)
5. No enumeration, validation, or translator selection ordering statements discovered in origin docs.

Result Assessment:
- All Incomplete blocks remain fully unresolved post Pass #1.
- Absence of any direct schema hints suggests low likelihood of uncovering specifics without new origin authoring.

Next Action Recommendation:
- Schedule Evidence Pass #2 with expanded scope including any mesh, scaling, registry, and potential security documents for indirect constraints; if still null, consider evidence exhaustion marking per policy.

Pass Status: Completed (No schema/evaluation evidence). Draft retained.

### Pass Planning: Pass #2 (Mesh & Security Expansion)
Scope Expansion: docs/mesh.md, docs/registry.md (context), docs/Scaling.md, docs/security research.md (if mesh security interlocks), docs/nodes.md (re-scan), docs/registry.md (re-scan)
Primary Objectives:
- Detect indirect translator selection ordering cues.
- Surface any mention of validation / normalization or rejection of overstated capabilities.
- Identify any role assignment determinism hints (e.g., scaling or registry constraints).
Success Criteria (Blocker Relief):
- Discovery of any explicit field grouping or enumeration OR
- Statement defining evaluation or selection ordering OR
- Security handling description for malicious declarations.
Null Criteria:
- No new statements covering enumeration, evaluation ordering, or security mitigation.
Deferral Note: May run parallel with User Tape Pass #2; schedule after Integrity Core Pass #2 initiation.
Scheduled: 2025-09-13 (planned)

## Evidence Pass #2 Log (2025-09-13)
Scope: Expanded mesh, scaling, registry, nodes, security research, and capability related origin docs per planning block.

Search Queries Executed:
- "capability set" (no matches) (Source: search results summary – absence noted)
- "Capability Set" (no matches) (Source: search results summary – absence noted)
- "capability" / "capabilities" (Sources: docs/nodes.md; docs/mesh.md; docs/Scaling.md; docs/registry.md; docs/display (container).md)
- "translator" (no ordering references tied to capability evaluation) (Source: search results summary – absence noted)
- "role" combined with capability context scan (Sources: docs/nodes.md; docs/mesh.md)
- "validation" / "sanitize" / "normalization" (no capability set schema context found) (Source: search results summary – absence noted)
- "malicious" (no matches) (Source: search results summary – absence noted)
- "overstated" (no matches) (Source: search results summary – absence noted)
- "version" / "versioning" (no capability set evolution semantics) (Source: search results summary – absence noted)

Findings:
1. Mesh & nodes docs reiterate that capabilities influence integration but provide no field enumeration or algorithmic evaluation detail. (Sources: docs/nodes.md; docs/mesh.md)
2. Scaling and registry docs contain no explicit capability schema or translator selection ordering semantics. (Sources: docs/Scaling.md; docs/registry.md)
3. No validation, sanitization, or security mitigation mechanisms (e.g., rejection, normalization) surfaced. (Sources: all scanned – absence noted)
4. No versioning or evolution pathway references for capability set fields encountered. (Sources: all scanned – absence noted)

Assessment:
- Success Criteria NOT met (no enumeration, ordering, or security handling discovered).
- Null Criteria MET (no new statements across scope).

Next Step Recommendation:
- Proceed to exhaustion precondition evaluation after integrating User Tape Pass #2 null result; prepare inventory verification (capability set already covered broad mesh cluster; dedicated inventory section may simply cite full cluster scan and absence).

Pass Status: Completed (Null) – Maintain Incomplete blocks pending exhaustion decision gate.

## Inventory Verification (Capability Set) – 2025-09-13
Scope Enumeration:
- Mesh & Nodes: docs/mesh.md; docs/nodes.md; docs/Scaling.md; docs/registry.md
- Capability Advertisement & Roles: capability-advertisement-extraction.md; mesh-roles-matrix.md; sections/glossary.md
- Security / Supporting: docs/root-monolith/security research.md (scan for malicious declaration mitigation – absence noted)

Consolidated Query Set (Pass #1 + Pass #2):
- "capability set"; "Capability Set"; "capability"; "capabilities"; "translator"; "validation"; "sanitize"; "normalization"; "malicious"; "overstated"; "version"; "versioning"; "role"

Coverage Assessment:
1. All mesh onboarding & scaling origin sources enumerated and scanned; no additional uncited origin file in cluster referencing schema structure (Sources: file list above – absence noted)
2. No field enumeration, ordering, validation, sanitization, security handling, or versioning semantics discovered (Sources: docs/mesh.md; docs/nodes.md; docs/Scaling.md – absence noted)
3. Extracted advertisement & roles matrices contain only gap identification, no normative schema (Sources: capability-advertisement-extraction.md; mesh-roles-matrix.md)

Conclusion:
- Null expansion confirmed; criteria satisfied for exhaustion evaluation post roadmap update aligning with other blockers (Source: policy-evidence-exhaustion.md)

Action Recommendation:
- Insert Evidence Exhaustion Decision blocks (all four) and relocate gaps to roadmap 'Awaiting New Source Material' if unified decision adopted.
