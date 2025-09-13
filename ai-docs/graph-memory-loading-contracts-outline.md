# Graph Memory Loading Contracts Outline (Extraction Skeleton)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/byte-function-load.md, docs/root-monolith/comprehensive.md
Verbatim scope: Listed source files only.

## Purpose
Collect explicit mentions relating to executable/code loading and allocation without introducing new mechanism details.

## Sourced Statements
- Code allocator stores chunk under predictable function name; chunk may be precompiled file or macro-generated. (Source: docs/root-monolith/byte-function-load.md)
- Memory module can access HOST vol file; load memory byte arrays as compiled executable; OS accesses loaded executable at address. (Source: docs/root-monolith/byte-function-load.md)
- VRAM slice (65K suggestion) and closed allocation space referenced. (Source: docs/root-monolith/comprehensive.md)
- Library of tools auto-exposed to application code (no criteria defined). (Source: docs/root-monolith/comprehensive.md)

## Observed Concept Elements
- Predictable function naming on load
- Precompiled vs macro-generated source parity
- Executable address exposure
- VRAM slice sizing suggestion
- Closed allocation space (implied boundary)

## Cross-Refs
- root-monolith-byte-function-load-extraction.md (granular function reconstruction gaps)
- root-monolith-comprehensive-extraction.md (allocator & VRAM slice gaps)

## Incomplete Blocks
```
Incomplete: Allocation Boundary Definition
Needed: Delineation between VRAM slice, closed allocation space, and general graph memory; alignment constraints.
Candidate Sources: docs/root-monolith/comprehensive.md, docs/root-monolith/byte-function-load.md
```
```
Incomplete: Predictable Naming Collision Policy
Needed: Handling strategy when function name already present; overwrite vs versioning vs reject.
Candidate Sources: docs/root-monolith/byte-function-load.md
```
```
Incomplete: Executable Exposure Contract
Needed: Conditions under which loaded executable becomes addressable; permission checks; invalidation triggers.
Candidate Sources: docs/root-monolith/byte-function-load.md, docs/root-monolith/comprehensive.md
```
```
Incomplete: Source Equivalence Rules
Needed: Whether macro-generated and precompiled binaries must attest equivalence; checksum validation tie-in.
Candidate Sources: docs/root-monolith/byte-function-load.md, root-monolith-security-init-extraction.md
```
```
Incomplete: Library Auto-Exposure Inclusion Criteria
Needed: Rule set for which tools become auto-exposed; precedence with manually loaded functions.
Candidate Sources: docs/root-monolith/comprehensive.md, root-monolith-libs-extraction.md
```

## Notes
- Outline only; refrains from proposing structural schema.
