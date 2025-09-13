# Root Monolith – Library Provision (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/applying-vol-runtime-libs.md
Verbatim scope: docs/root-monolith/applying-vol-runtime-libs.md

## Purpose
Capture explicit methods for supplying libraries to the VOL environment.

## Sourced Statements
1. Method 1: Store all assets within the `Lib/` directory. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
2. Method 2: Create a `vol._vpt` file addressing local paths of folders and zips. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
3. Method 3: Apply the module within the root. (Source: docs/root-monolith/applying-vol-runtime-libs.md)

## Observed Concept Elements (Names Only)
- Lib/ directory asset storage
- vol._vpt file
- Root module application

## Cross-References
- Glossary stubs: vol._vpt (working-term) (See: sections/glossary.md)
- Related gap: Library Provision Mechanisms (root-monolith-triage.md)

## Incomplete Blocks
```
Incomplete: vol._vpt File Structure
Needed: Field definitions; path resolution order; support for archive layering.
Candidate Sources: docs/root-monolith/applying-vol-runtime-libs.md
```
```
Incomplete: Module Application Constraints
Needed: Validation rules before applying module; conflict detection; idempotent reapplication behavior.
Candidate Sources: docs/root-monolith/applying-vol-runtime-libs.md, docs/core/system core.md
```

## Notes
- No preference or precedence order specified among methods; none inferred.

Backlink: Referenced by root-monolith-triage.md and root-monolith-index.md
Additional Backlink: Referenced by library-exposure-pathways-matrix.md
