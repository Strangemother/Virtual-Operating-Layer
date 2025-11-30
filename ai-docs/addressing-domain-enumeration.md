# Addressing Domain Enumeration (Extraction)
Status: Draft
Last-Touched: 2025-11-30
Depends-On: root-monolith-step-addresses-layers-extraction.md
Verbatim scope: root-monolith-step-addresses-layers-extraction.md

## Purpose
Flat enumeration of all addressing domain labels and identifiers from root-monolith sources. Hierarchy and relationships tracked as gap #16 in gap-priority-matrix.md.

## Enumerated Identifiers
Lower-case sequence (all mapped to "another space of memory (tree structure)"):
- a, b, c, d, e, f (query access location in memory small space), g, h, i, j, k, l (Source: root-monolith-step-addresses-layers-extraction.md; docs/root-monolith/step addresses and layers.md)

Upper / symbolic domain labels:
- F, I, J (jump frame), K, L, Q, T (time frame), X, Y (sequence memory graph), Z (series memory graph) (Source: root-monolith-step-addresses-layers-extraction.md; docs/root-monolith/step addresses and layers.md)

Domain descriptors:
- index space domain
- expanded space domain
- family space domain
- extended family space domain
- related family space domain
- dictionary space domain (Source: root-monolith-step-addresses-layers-extraction.md; docs/root-monolith/step addresses and layers.md)

## Cross-References
- Glossary working-term stubs for all domain labels (See: sections/glossary.md)
- Related gap: Layered Addressing Contract (#16 in gap-priority-matrix.md)

## Incomplete Blocks
```
Incomplete: Domain Relationship Specification
Needed: Cardinality or subset relations among listed domains; transformation or promotion criteria.
Candidate Sources: docs/root-monolith/step addresses and layers.md, docs/core/structure.md, TODO: discover
```
```
Incomplete: Identifier Collision Rules
Needed: Whether lower-case vs upper-case namespaces overlap; uniqueness guarantees.
Candidate Sources: docs/root-monolith/step addresses and layers.md, root-monolith-index.md
```
```
Incomplete: Frame vs Domain Namespace Separation
Needed: Confirmation that frame identifiers (T, J) do not share resolution path with domain labels.
Candidate Sources: docs/root-monolith/Frame Switching.md, docs/root-monolith/step addresses and layers.md
```

## Notes
- Enumeration intentionally flat to avoid implied ordering.
- Pending future normalization once explicit relationships appear.
