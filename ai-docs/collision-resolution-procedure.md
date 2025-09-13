Status: Draft
Last-Touched: 2025-09-13
# Collision Resolution Procedure

Purpose: Provide a minimal repeatable method to finalize canonical term selection without inventing new terminology.

## Inputs
- Candidate terms set (from term-collisions.md)
- Current glossary entry/entries
- Source file occurrence counts (manual tally)

## Steps
1. Verify Collision: Confirm both (or more) terms appear in glossary or source docs referencing same concept. (Source: term-collisions.md)
2. Source Specificity Check: Prefer term whose definition is cited by the most specific file describing behavior (e.g., graph pointer.md for pointer tape). (Source: glossary.md, graph pointer.md)
3. Frequency Tally: If specificity ties, count occurrences across source docs; higher count wins. (Source: glossary usage pattern – no rule previously, formalized here referencing existing need in term-collisions.md)
4. Canonical Selection: Choose winning term; alternate forms become aliases placed immediately after canonical per alias policy. (Source: policy-alias-format.md)
5. Glossary Update: Collapse duplicates, insert Aliases line citing same primary source unless alias uniquely sourced. (Source: glossary.md current structure)
6. Collisions Catalog Update: Mark collision RESOLVED with canonical term and status. (Source: term-collisions.md pattern)
7. Changelog Entry: Record resolution under Normalization section. (Source: CHANGELOG-docs.md practice)

## Decision Tie Breakers
Order of precedence if ambiguity remains after Steps 2–3:
1. Earlier introduction date (implied by older source file Last-Touched if present) (Source: relocation/promotion record pattern referencing chronology)
2. Shorter, clearer term (brevity preference implied by consolidation practice in glossary normalization)
3. Retain historical variant as alias (Source: alias normalization approach)

## Incomplete Blocks
Incomplete: Automated Occurrence Counting
Needed:
- Scripted method or documented manual template for counting term appearances
- Threshold for ignoring minor variants (case, punctuation)
Candidate Sources: glossary.md, term-collisions.md

Verbatim scope: glossary.md, term-collisions.md, policy-alias-format.md, CHANGELOG-docs.md, graph pointer.md only.
