Status: Draft
Last-Touched: 2025-09-13
# Backlink Insertion Plan

Purpose: Add non-intrusive backlinks in original source docs pointing to extracted summaries in ai-docs for discoverability. No alteration of substantive content.

## Backlink Format
At top (after existing title/status if present):
```
Backlink: See extracted summary in ../../ai-docs/sections/<file>.md
```
(Adjust relative path depth accordingly.)

## Target Files (Initial Set)
- docs/core/graph pointer.md -> ai-docs/sections/graph-overview.md
- docs/core/graph stepper.md -> ai-docs/sections/graph-overview.md
- docs/core/graph node compass.md -> ai-docs/sections/graph-overview.md
- docs/core/frame-context.md -> ai-docs/sections/runtime-overview.md (assuming frame-context summarized there; verify)

## Incomplete Blocks
Incomplete: Frame Context Summary Mapping
Needed:
- Confirm destination summary filename for frame-context (runtime or graph cluster?)
Candidate Sources: ai-docs/sections/runtime-overview.md, ai-docs/sections/graph-overview.md

Verbatim scope: docs/core/graph pointer.md, docs/core/graph stepper.md, docs/core/graph node compass.md, docs/core/frame-context.md only.
