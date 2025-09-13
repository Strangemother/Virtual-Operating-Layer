# Root Monolith – Phase 0 (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/phase-0.md
Verbatim scope: docs/root-monolith/phase-0.md

## Purpose
Capture explicit statements about graph key #0 (phase-0), protected start behavior, and initial loop persistence.

## Sourced Statements
1. Graph key #0 (phase-0) is protected and owned by the BIOD. (Source: docs/root-monolith/phase-0.md)
2. First stage persists the loop; initial graph likely an empty loop requesting a magic key (boot point). (Source: docs/root-monolith/phase-0.md)
3. Some graph IDs are read-only and reserved for internal operations. (Source: docs/root-monolith/phase-0.md)
4. Beneath the user's loading magic key lies phase-0 performing a phase-0 test (power on features and core library loading). (Source: docs/root-monolith/phase-0.md)
5. Fundamental libraries listed: Schedulers, Steppers, Pointer Executors. (Source: docs/root-monolith/phase-0.md)
6. Required components enumerated: system core monolith, CPUs, the FS, range of root internal membranes, "Cells" connected to membranes. (Source: docs/root-monolith/phase-0.md)

## Observed Concept Elements (Names Only)
- Graph Key 0 / phase-0
- BIOD
- Reserved Graph IDs
- Loop persistence before magic key
- Fundamental libraries (schedulers/steppers/pointer executors)
- Internal membranes / cells

## Cross-References
- Glossary working-term stubs: Graph Key 0, BIOD, Reserved Graph ID (See: sections/glossary.md)
- Related gap: Phase 0 Ordered Requirements (root-monolith-triage.md)

## Incomplete Blocks
```
Incomplete: Phase-0 Protection Mechanism
Needed: Enforcement method for read-only / protected key; BIOD role definition; mutation prevention strategy.
Candidate Sources: docs/root-monolith/phase-0.md, docs/root-monolith/security research.md
```
```
Incomplete: Loop Persistence State
Needed: Structure of persisted empty loop; criteria for requesting magic key; failure escalation.
Candidate Sources: docs/root-monolith/phase-0.md, docs/root-monolith/phases.md
```
```
Incomplete: Fundamental Library Load Ordering
Needed: Whether schedulers precede steppers; dependency prerequisites; fallback if missing.
Candidate Sources: docs/root-monolith/phase-0.md, docs/root-monolith/comprehensive.md
```

## Notes
- No sequencing or enforcement algorithms specified; extraction remains purely enumerative.

Backlink: Referenced by root-monolith-triage.md and root-monolith-index.md
