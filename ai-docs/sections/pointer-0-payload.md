# See: [graph-overview.md](graph-overview.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: boot-sequence-table.md
# Pointer 0 Payload Extraction

Purpose: Collate explicit statements regarding pointer 0 and its payload without defining absent schema details.

## Sourced Statements
1. Pointer 0 is an executable (.bin or .elf like structure) to initiate core code (Source: [zero-suite.md](../../docs/core/zero-suite.md))
2. Payload is unpacked and loaded into primary allowed memory (Source: [zero-suite.md](../../docs/core/zero-suite.md))
3. Payload contains all assets for an effective VM (Source: [zero-suite.md](../../docs/core/zero-suite.md))
4. Pointer steps into position 0 (default) then a magic value sends pointer to first position (Source: [zero-suite.md](../../docs/core/zero-suite.md))
5. During zero state there is no graph, pointer stepper, or OS (Source: [zero-suite.md](../../docs/core/zero-suite.md))

## Observed Entities (Names Only)
* pointer 0 executable
* primary allowed memory
* assets for VM
* magic value
* position 0 (default)

## Incomplete Blocks

Incomplete: Pointer 0 Asset List
Needed:
- Enumerated asset types (currently only "all assets for an effective VM" phrase)
- Distinction between code libs, allocator, executor specifics
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Magic Value Specification
Needed:
- Format or origin of magic value
- Validation / misuse handling
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Memory Layout
Needed:
- Segment ordering (code, data, metadata) for pointer 0 payload
- Relocation or alignment rules
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Execution Handoff Semantics
Needed:
- Conditions determining first post-position after magic value
- Failure/error fallback path
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Absence Components Confirmation
Needed:
- Explicit confirmation that stepper instantiation follows pointer 0 rather than embedded
- Criteria to instantiate initial graph
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Verbatim scope: [zero-suite.md](../../docs/core/zero-suite.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 2.
