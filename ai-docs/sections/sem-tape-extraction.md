# See: [boot-sequence-diagram.md](boot-sequence-diagram.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: boot-sequence-table.md
# SEM TAPE Extraction (Boot Layer References)

Purpose: Collate explicit references to SEM TAPE without inferring structure or format.

## Sourced Statements
1. Boot zim sem executes a store using SEM TAPE into a new memory reference (mcom) (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
2. mcom file descriptor is anonymous containing loading step values as a TAPE string (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
3. Config and kernel address written to an mcom TAPE location by the boot sem (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))

## Observed Entities (Names Only)
* SEM TAPE
* mcom (anonymous memory reference / file descriptor)
* loading step values (as TAPE string)
* config and kernel address

## Incomplete Blocks

Incomplete: SEM TAPE Field Enumeration
Needed:
- List of explicit fields (GUID, init settings implied elsewhere but not enumerated)
- Ordering or delimiter rules
Candidate Sources: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md)

Incomplete: mcom Descriptor Specification
Needed:
- Data type / size constraints
- Lifetime and ownership semantics
Candidate Sources: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md)

Incomplete: Step Value Encoding
Needed:
- Encoding (text/binary) for "loading step values"
- Error handling on malformed TAPE string
Candidate Sources: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md)

Incomplete: Security / Integrity of SEM TAPE
Needed:
- Validation of config & kernel address before handoff
- Tamper detection strategy
Candidate Sources: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md)

Verbatim scope: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 2.
