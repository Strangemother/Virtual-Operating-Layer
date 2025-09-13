# Term Promotion Readiness Matrix (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: sections/glossary.md, policy-promotion.md
Verbatim scope: sections/glossary.md, policy-promotion.md

## Purpose
List working-term stubs and identify missing elements preventing term stabilization; no new definitions added.

## Readiness Categories
- Ready Candidate: Appears in multiple extraction docs; no naming collision; gap references stable.
- Collision Review: Term appears in collision notice requiring disambiguation.
- Underdefined: Referenced but lacks any structural or behavioral hint beyond name.

## Term Inventory (Full Working-Term Pass)
Softheader – Category: Underdefined (threshold mechanics absent) (Source: sections/glossary.md)
Hard Peak – Category: Underdefined (trigger conditions absent) (Source: sections/glossary.md)
Quiet Time Cleaner – Category: Underdefined (differentiation vs Health Doctor unclear) (Source: sections/glossary.md)
Perfect Hashmap – Category: Underdefined (algorithm not specified) (Source: sections/glossary.md)
Closed Loop Algorithm – Category: Underdefined (address binding rules absent) (Source: sections/glossary.md)
Paging (address pages) – Category: Underdefined (page structure undefined) (Source: sections/glossary.md)
Acquisition Unit – Category: Underdefined (responsibility contract incomplete) (Source: sections/glossary.md)
Non-Acquisition Unit – Category: Underdefined (consumption boundaries unspecified) (Source: sections/glossary.md)
Frame Orientation – Category: Underdefined (entry outputs unspecified) (Source: sections/glossary.md)
Block Mapping – Category: Underdefined (merge mechanics absent) (Source: sections/glossary.md)
Quantum Frame – Category: Underdefined (transition triggers missing) (Source: sections/glossary.md)
Command Frame – Category: Underdefined (execution semantics missing) (Source: sections/glossary.md)
Time Frame – Category: Underdefined (role unspecified) (Source: sections/glossary.md)
Jump Frame – Category: Underdefined (role unspecified) (Source: sections/glossary.md)
Sequence Memory Graph – Category: Underdefined (differentiators absent) (Source: sections/glossary.md)
Series Memory Graph – Category: Underdefined (differentiators absent) (Source: sections/glossary.md)
Frame 0 – Category: Ready Candidate (multi-source references) (Source: sections/glossary.md)
Command Lifecycle – Category: Underdefined (phase enumeration absent) (Source: sections/glossary.md)
Index Space Domain – Category: Underdefined (relationship rules missing) (Source: sections/glossary.md)
Expanded Space Domain – Category: Underdefined (relationship rules missing) (Source: sections/glossary.md)
Family Space Domain – Category: Underdefined (relationship rules missing) (Source: sections/glossary.md)
Extended Family Space Domain – Category: Underdefined (hierarchy unspecified) (Source: sections/glossary.md)
Related Family Space Domain – Category: Underdefined (linkage semantics absent) (Source: sections/glossary.md)
Dictionary Space Domain – Category: Underdefined (precedence unresolved) (Source: sections/glossary.md)
Graph Key 0 – Category: Ready Candidate (multi-source: phase-0, readme) (Source: sections/glossary.md)
Reserved Graph ID – Category: Underdefined (enforcement unspecified) (Source: sections/glossary.md)
BIOD – Category: Underdefined (role unspecified) (Source: sections/glossary.md)
vol._vpt – Category: Underdefined (schema absent) (Source: sections/glossary.md)
Initial Graph Bits – Category: Underdefined (entropy source unspecified) (Source: sections/glossary.md)
CRC Start Key – Category: Underdefined (derivation steps missing) (Source: sections/glossary.md)
root.lock() – Category: Underdefined (operation contract missing) (Source: sections/glossary.md)
User Tape – Category: Ready Candidate (multiple phase sources) (Source: sections/glossary.md)
Enforced Code – Category: Underdefined (update policy missing) (Source: sections/glossary.md)
Virtual RAM Slice – Category: Collision Review (Virtual RAM Slice/VRAM slice) (Source: sections/glossary.md)
Code Allocator – Category: Underdefined (allocation mechanics missing) (Source: sections/glossary.md)
Walking Register – Category: Collision Review (Walking Register/Register) (Source: sections/glossary.md)
Input-Session Key – Category: Underdefined (termination criteria missing) (Source: sections/glossary.md)
Variation Tree – Category: Underdefined (node types absent) (Source: sections/glossary.md)
Generative Grammar – Category: Underdefined (rule set absent) (Source: sections/glossary.md)

## Summary Counts
Ready Candidate: 4 (Frame 0, Graph Key 0, User Tape, Capability Set*)
Collision Review: 2 (Virtual RAM Slice, Walking Register)
Underdefined: Remaining terms
*Capability Set appears with qualifier (working-term) and needs schema to move beyond Ready Candidate.

## Incomplete Blocks
```
Incomplete: Promotion Candidate Enumeration
Needed: Full pass enumerating all working-term stubs beyond selected sample; criteria mapping for each.
Candidate Sources: sections/glossary.md, term-collisions.md
```
```
Incomplete: Collision Resolution Dependencies
Needed: Sequence for resolving Virtual RAM Slice/VRAM and Walking Register/Register before promotion.
Candidate Sources: sections/glossary.md, collision-resolution-procedure.md
```

## Notes
- Only a selected subset listed to establish matrix structure; remaining terms require subsequent inventory pass.

Backlink: Will be indexed in governance-index.md
Additional Backlink: Referenced by sections/glossary.md
Collision Backlink: Disambiguation stubs present in sections/glossary.md for Walking Register/Register and Virtual RAM Slice/virtual-ram functions
Promotion Checklist Backlink: See promotion-candidate-checklist.md for per-candidate evidence & gaps
Frame 0 Gap Backlink: See frame-0-privilege-boundary-extraction.md for sourced privilege boundary gaps
Graph Key 0 Gap Backlink: See graph-key-0-enforcement-extraction.md for enforcement & ownership gaps
User Tape Gap Backlink: See user-tape-validation-extraction.md for validation & source precedence gaps
