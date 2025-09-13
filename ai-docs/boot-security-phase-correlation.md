# Boot / Security / Phase Correlation Extraction
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/boot.md, docs/core/boot.md, docs/root-monolith/phase-0.md, docs/root-monolith/phases.md, docs/root-monolith/security research.md
Verbatim scope: Listed source files only.

## Purpose
Aggregate ordering claims across boot, phase 0 initialization, and security chain references. No inferred sequencing beyond explicit textual orderings.

## Sourced Ordering Mentions
1. Phase 0 test references Graph key #0 as protected start point; loop persistence established early. (Source: docs/root-monolith/phase-0.md)
2. Phase sequence: wake/magic number → power/register tests → run root binary → create root language/core methods → load virtual-ram functions → enforce code → load baseline functions → register house events → perform last call changes → load first user tape. (Source: docs/root-monolith/phases.md)
3. Subsequent loading after user tape: Event Stack → Filesystem → Graph Memory → multiprocessing → REPL → GUI. (Source: docs/root-monolith/phases.md)
4. Security research chain: initial random graph bits → chain of graph keys + steps → CRC start key using boot file + one-way BIOS key bits → root.lock() finalizes BIOS state & verifies record; refusal on failure. (Source: docs/root-monolith/security research.md)
5. CRC may denote boot key sequence bridging execution string; randomization required to prevent tampering. (Source: docs/root-monolith/security research.md)
6. Boot file involvement implied in CRC start key derivation. (Source: docs/root-monolith/security research.md)

## Cross-Referenced Extraction Docs
- root-monolith-phase-0-extraction.md (Graph key 0, reserved IDs)
- root-monolith-phase-sequence-extraction.md (Explicit ordered list)
- root-monolith-security-init-extraction.md (Security chain primitives)

## Observed Concept Elements
- Protected graph start key (#0)
- Random initial graph bits (encryption context)
- CRC start key (boot file linkage)
- root.lock() BIOS state validation
- Enforced code stage (from phase sequence)
- User tape load point

## Incomplete Blocks
```
Incomplete: Integrated Boot-Security Ordering Contract
Needed: Explicit relative position of security random graph bits generation vs phase 0 test; placement of CRC randomization relative to enforce code and baseline function load; dependency (if any) between user tape load and root.lock() finalization.
Candidate Sources: docs/root-monolith/security research.md, docs/root-monolith/phase-0.md, docs/root-monolith/phases.md, docs/boot.md
```
```
Incomplete: Failure Handling Semantics
Needed: Retry or halt behavior on root.lock() verification failure; logging/audit obligations; recovery pathway.
Candidate Sources: docs/root-monolith/security research.md
```

## Notes
- No attempt made to interleave security sequence with phase sequence beyond listed raw order fragments.
