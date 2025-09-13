# Library Exposure Pathways Matrix (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/applying-vol-runtime-libs.md, docs/root-monolith/comprehensive.md
Verbatim scope: Listed files only.

## Purpose
Enumerate observed library/module exposure mechanisms mentioned in sources without adding precedence or selection logic.

## Sourced Pathways
1. Lib/ directory: Store all assets directly. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
2. vol._vpt file: Addresses local paths of folders and zips for library supply. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
3. Root module application: Apply the module within the root. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
4. Auto-exposed library of tools to application code (criteria unspecified). (Source: docs/root-monolith/comprehensive.md)

## Observed Concept Elements (Names Only)
- Lib/ asset store
- vol._vpt path descriptor
- Root module application
- Auto-exposed library set

## Cross-References
- Related gaps: Library Provision Mechanisms; Library Auto-Exposure Rules (gap-index.md)
- See also: root-monolith-libs-extraction.md; root-monolith-comprehensive-extraction.md; graph-memory-loading-contracts-outline.md

## Incomplete Blocks
```
Incomplete: Exposure Precedence
Needed: Resolution order when same module appears via multiple pathways; conflict handling.
Candidate Sources: docs/root-monolith/applying-vol-runtime-libs.md, docs/root-monolith/comprehensive.md
```
```
Incomplete: vol._vpt Schema
Needed: Field structure; path resolution strategy; zip vs directory priority.
Candidate Sources: docs/root-monolith/applying-vol-runtime-libs.md
```
```
Incomplete: Auto-Exposure Inclusion Criteria
Needed: Eligibility rules; version/update policy; security sandbox constraints.
Candidate Sources: docs/root-monolith/comprehensive.md, docs/root-monolith/applying-vol-runtime-libs.md
```

## Notes
- No preference statement present in sources; none added.

Backlink: Will be indexed in governance-index.md
