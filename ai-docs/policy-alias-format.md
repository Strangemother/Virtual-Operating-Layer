Status: Draft
Last-Touched: 2025-09-13
# Alias Formatting Policy (Documentation)

Purpose: Define canonical formatting for term aliases within the glossary without introducing new terminology beyond existing entries.

## Canonical Format
Primary Line: <Term> – <Definition> (Source: <file path>)
Alias Line (immediately following primary): Aliases: <alias1>, <alias2> (Source: <same or most specific source>)

## Rules (All Backed by Existing Practice)
1. Alias lines must follow directly after the primary term they reference (Source: glossary.md current structure).
2. Canonical naming uses the most frequently occurring source phrase (Source: glossary.md; term-collisions.md).
3. Parenthetical clarifiers retained only if present in source (e.g., "SEM (Boot SEM)") (Source: glossary.md).
4. Duplicated standalone repeats of identical primary lines must be collapsed into one with an alias line (Source: term-collisions.md).
5. If an alias differs only by word order (e.g., "Pointer Tape" vs "Tape (Pointer Tape)") select the form explicitly appearing in formal source explanation (Source: [graph pointer.md](../docs/core/graph%20pointer.md)).
6. Multiple alias entries for the same term are comma separated; no trailing period (Source: glossary.md existing list style).
7. Aliases section does not introduce explanatory text beyond names already present (Source: non-speculation principle in copilot-instructions.md).

## Examples
Tape (Pointer Tape) – Sequence of keys describing execution path (Source: [graph pointer.md](../docs/core/graph%20pointer.md))
Aliases: Pointer Tape (Source: [graph pointer.md](../docs/core/graph%20pointer.md))

Internal DB Registry – Database of live commands executed post cache/event requests (Source: [registry.md](../docs/registry.md))
Aliases: Live Command Database (Source: [registry.md](../docs/registry.md))

SEM (Boot SEM) – Boot sequence self executing module reference (Source: [boot.md](../docs/boot.md))
Aliases: Boot SEM (Source: [boot.md](../docs/boot.md))

## Incomplete Blocks

Incomplete: Alias Conflict Resolution Procedure
Needed:
- Tie-break rule when multiple equally frequent variants exist
- Process for retiring deprecated aliases
Candidate Sources: glossary.md, term-collisions.md

Verbatim scope: glossary.md, term-collisions.md, graph pointer.md, registry.md, boot.md only.
