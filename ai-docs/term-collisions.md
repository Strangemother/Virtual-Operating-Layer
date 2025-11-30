Status: Draft
Last-Touched: 2025-11-30
# Term Collisions Catalog

Purpose: Enumerate observed naming collisions or near-collisions to support glossary disambiguation. No new terms are created here.

## Format
Collision: <Term A>/<Term B>
Observed Usage: <short note> (Source: <files>)
Action: Add glossary disambiguation entry

## Collisions

Collision: Tape/Pointer Tape
Observed Usage: Both forms describe ordered key/path structure for graph traversal (Source: glossary.md, docs/core/graph pointer.md)
Action: RESOLVED – Canonical set to "Tape (Pointer Tape)" with alias per glossary (Status: Working-Spec glossary.md)

Collision: SEM/Boot SEM
Observed Usage: SEM used alone and with Boot qualifier referencing boot self executing module (Source: glossary.md, docs/boot.md)
Action: RESOLVED – Canonical SEM with alias Boot SEM in glossary

Collision: Internal DB Registry/Live Command Database
Observed Usage: Phrasings for database of live commands executed after cache/event requests (Source: glossary.md, docs/registry.md)
Action: RESOLVED – Internal DB Registry primary; Live Command Database alias

Collision: Tape (Pointer Tape)/Pointer Tape (ordering variant)
Observed Usage: Ordering variation only; same semantic scope (Source: glossary.md)
Action: RESOLVED – Variant removed; canonical ordering retained

Collision: Walking Register/Register
Observed Usage: "Walking register" used for continuous input accumulation vs generic "register" referencing system/registers functions and config memory. (Source: docs/root-monolith/readme.md; docs/root-monolith/phases.md; sections/glossary.md)
Action: PENDING – Disambiguation entry required in glossary (stream accumulator vs general register set)

Collision: Virtual RAM Slice/virtual-ram functions
Observed Usage: "Virtual RAM Slice" a sizing suggestion (65K) vs "virtual-ram functions" used in phase sequence for loading functions; potential confusion between memory page unit and functional loader set. (Source: docs/root-monolith/comprehensive.md; docs/root-monolith/phases.md; sections/glossary.md)
Action: PENDING – Disambiguation entry required in glossary (allocation unit vs function category)

## Incomplete Blocks

Incomplete: Collision Resolution Procedure
Needed:
- Validate applicability of drafted steps to future multi-term collisions
- Determine occurrence counting method (manual vs automated)
Candidate Sources: glossary.md, collision-resolution-procedure.md

Incomplete: Additional Collision Discovery
Needed:
- Systematic scan of graph-related variants (pointer, stepper, compass)
- Clarify whether "graph key names" vs "graph pointer" requires alias or structural separation
Candidate Sources: docs/core/graph key names.md, docs/core/graph pointer.md, docs/core/graph node compass.md, docs/core/graph stepper.md, ai-docs/sections/graph-overview.md

Note: Remaining open discovery focuses on multi-file graph concept boundaries (pointer vs key names vs compass vs stepper) – see graph-boundary-outline.md for sourced role consolidation.

Verbatim scope: glossary.md, docs/core/graph pointer.md, docs/boot.md, docs/registry.md only.
