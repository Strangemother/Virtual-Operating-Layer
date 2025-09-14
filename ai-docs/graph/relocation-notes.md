# Graph Concept Relocation Notes
Status: Draft
Last-Touched: 2025-09-13
Depends-On: OVERVIEW.md

Verbatim scope: docs/core/graph pointer.md, docs/core/graph stepper.md, docs/core/graph key names.md, docs/core/graph node compass.md, docs/core/graph functions.md, docs/core/Procedure Graph.md

Purpose: Enumerate original source files and declare that high-level orientation is now consolidated in `OVERVIEW.md`. Originals remain authoritative for granular prose and examples.

## Source File Index
- docs/core/Procedure Graph.md – General procedural graph narrative
- docs/core/graph pointer.md – Pointer definition & naming variants
- docs/core/graph stepper.md – Stepper, machine hierarchy, execution sequence
- docs/core/graph key names.md – Key naming patterns, vector bits, TODO for collision-free formula
- docs/core/graph node compass.md – Internal compass path validation via summed vectors
- docs/core/graph functions.md – SES/function execution characteristics & examples

## Superseded Sections (Orientation Layer Only)
The following conceptual headings are superseded at the OVERVIEW layer (originals retained):
- Pointer (overview aspects only)
- Stepper (high-level description only)
- Key Names (summary of naming patterns & vector components)
- Internal Compass (summary definition)
- Functions / SES (role definition and capability list)

## Not Superseded
- Detailed examples, code-like pseudo snippets
- Open TODO comments present in originals
- Any implementation-specific narrative

## Cross-Reference Guidance
When citing:
1. Use original file for detailed behavior quote-level citation.
2. Use `OVERVIEW.md` for orientation or multi-concept linkage.
3. Avoid inferring missing behaviors—log gap in `OVERVIEW.md` incomplete blocks.

## Incomplete Tracking Alignment
All unresolved items collected in `OVERVIEW.md` under dedicated Incomplete blocks. No additional gap list maintained here to avoid drift.

## Change Control
Future structural merges must:
- Add new source file path to Source File Index.
- Update `OVERVIEW.md` Depends-On header.
- Append CHANGELOG entry referencing both this file and the overview.

_No normative content introduced here._