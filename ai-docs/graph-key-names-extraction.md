Status: Draft
Last-Touched: 2025-09-13
# Graph Key Names (Extraction)

Purpose: Summarize naming schemes and unresolved questions for pointer key naming without inventing new rules.

## Sourced Statements
1. Pointer address predictable: previous unit + current unit resolves next pointer (A + B == C). (Source: docs/core/graph key names.md)
2. Position vector values correspond to layer and ownership; definitions for 'layer' and 'ownership' undefined. (Source: docs/core/graph key names.md)
3. Vector name format x,y,z with bits: layer bit, graph bit (identity), position bit (contiguous SES position). (Source: docs/core/graph key names.md)
4. SES may be locked to layer or graph; moving SES could run wrong graph within same layer. (Source: docs/core/graph key names.md)
5. Pointer may return an address making forward address embedded in name invalid. (Source: docs/core/graph key names.md)
6. Tape can override key addressing using ordered sequence of keys. (Source: docs/core/graph key names.md)
7. Key name defines position and forward resolution; runtime parsing can infer processing without inspecting pointer content. (Source: docs/core/graph key names.md)
8. Names may embed multiple semantic segments: from|current|to pattern. (Source: docs/core/graph key names.md)
9. Vector + attributes composite examples include flags like |async and |returns. (Source: docs/core/graph key names.md)
10. Key names may be encrypted for security; decrypted by stepper. (Source: docs/core/graph key names.md)
11. Key names can change dynamically updating graph addressing. (Source: docs/core/graph key names.md)
12. Friendly names should map to changing underlying computed names. (Source: docs/core/graph key names.md)
13. Naming goals: direct next and previous; support unpredictable stepping; potential use of current|next schema. (Source: docs/core/graph key names.md)
14. Dependency reflection: Graph pointer data can reflect function dependency in name. (Source: docs/core/graph key names.md)

## Observed Naming Forms
- Semantic chain: from|current|to
- Vector chain: [0,1]#[0,0,0]#[0,2]
- Vector with flags: [0,2]#[0,0,1]#[0,3] |async
- Vector with returns: [0,3]#[0,0,2]#null |returns
- Hybrid with dependency parentheses: [0,2]#[0,0,1]#[0,3] ([0,2,2])|async

## Distinct Concepts Mentioned (Undeclared Definitions)
- Layer bit (undefined scope) (Source: docs/core/graph key names.md)
- Graph bit (graph identity semantics not formalized) (Source: docs/core/graph key names.md)
- Ownership (vector component) (Source: docs/core/graph key names.md)
- Friendly name mapping layer (Source: docs/core/graph key names.md)
- Encryption of key names (no method specified) (Source: docs/core/graph key names.md)

## Interactions with Other Components
- Stepper decrypts and parses names (implied; explicit decryption process unspecified). (Source: docs/core/graph key names.md)
- Tape override indicates alternate addressing path vs computed vector naming. (Source: docs/core/graph key names.md)
- Pointer return complicates forward embedding. (Source: docs/core/graph key names.md)

## Incomplete Blocks
Incomplete: Vector Component Definitions
Needed:
- Formal definitions for layer, graph, ownership bits
- Constraints or range for each bit
Candidate Sources: docs/core/graph key names.md, docs/core/graph pointer.md

Incomplete: Dynamic Renaming Semantics
Needed:
- Trigger conditions for name mutation
- Consistency guarantees for friendly name mapping
Candidate Sources: docs/core/graph key names.md, docs/core/graph pointer.md

Incomplete: Encrypted Key Handling
Needed:
- Encryption scope (entire name vs segments)
- At-what-stage decryption (before or during stepper parse)
Candidate Sources: docs/core/graph key names.md

Incomplete: Tape vs Vector Precedence
Needed:
- Explicit precedence rule when both tape and computed vector available
- Whether tape can partially override segments
Candidate Sources: docs/core/graph key names.md, docs/core/graph pointer.md

Incomplete: Dependency Annotation Format
Needed:
- Canonical syntax for dependency parentheses
- Rules for multiple dependencies
Candidate Sources: docs/core/graph key names.md

Verbatim scope: docs/core/graph key names.md only.
