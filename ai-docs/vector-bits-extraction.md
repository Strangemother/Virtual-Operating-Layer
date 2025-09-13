Status: Draft
Last-Touched: 2025-09-13
Depends-On: graph-overview.md

# Vector Bits Extraction (Graph Addressing) 

Purpose: Enumerate explicit mentions of vector / bit components (layer, graph, position, ownership/sysbit) used in pointer key naming and identify unspecified semantics. Only verbatim concepts captured.

## Sourced Occurrences
1. Position vector values correspond to "layer" and "ownership" (sysbit) (Source: docs/core/graph key names.md)
2. Example assignment: `Layer = 0` (representing 'root') (Source: docs/core/graph key names.md)
3. Example assignment: `Sysbit = 1` (user permission?—question mark indicates uncertainty in source) (Source: docs/core/graph key names.md)
4. Position index example: `position = 7` and increment to `position + 1` (Source: docs/core/graph key names.md)
5. Vector elements enumerated: #1 Layer bit, #2 Graph bit (identity), #3 Position bit (contiguous layer of SES). (Source: docs/core/graph key names.md)
6. SES may be locked to its layer or graph; moving SES to another vector may break expectations. (Source: docs/core/graph key names.md)
7. Friendly name concept to mask unreadable computed names (Source: docs/core/graph key names.md)
8. Security concern: keys visible; potential encryption of key names at runtime (Source: docs/core/graph key names.md)
9. TODO in source: Find formula to compute next key without collisions within space (Source: docs/core/graph key names.md)

## Structural Summary (Descriptive)
- Vector triple pattern: [layer, graph, position] with optional additional ownership/sysbit dimension referenced textually. (Source: docs/core/graph key names.md)
- Collision avoidance acknowledged but no algorithm provided. (Source: docs/core/graph key names.md)

## Not Specified
- Formal domain/range for layer, graph, position integers.
- Distinction (if any) between ownership/sysbit and permission model.
- Maximum position value or wrap behavior.
- Collision resolution strategy beyond modulo caution in compass context. (Source cross-reference: docs/core/graph node compass.md referencing modulo collision risk)

## Incomplete Blocks
Incomplete: Bit Field Definitions
Needed:
- Enumeration of bit field names and order
- Whether ownership/sysbit is separate from layer/graph triple
Candidate Sources: docs/core/graph key names.md, graph-overview.md

Incomplete: Collision Avoidance Algorithm
Needed:
- Deterministic function for computing next key
- Handling of exhausted position space
Candidate Sources: docs/core/graph key names.md

Incomplete: Permission / Ownership Semantics
Needed:
- Mapping from sysbit value(s) to permission categories
- Whether permission influences traversal
Candidate Sources: docs/core/graph key names.md

Incomplete: Encryption Handling
Needed:
- Scope of encrypted keys (full name vs segment)
- Decryption timing (pre-stepper vs inline)
Candidate Sources: docs/core/graph key names.md

Verbatim scope: docs/core/graph key names.md, docs/core/graph node compass.md
