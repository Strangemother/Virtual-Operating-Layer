# Single Identity (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Source Files: docs/memory/Single Identity.md

Purpose: Capture explicit statement about identity module isolation and permission gating. No extrapolated semantics.

## Sourced Statements
1. An "Identity" module should live in its own memory. (Source: docs/memory/Single Identity.md)
2. Accessible by its root method to identify who or what has current permissions state. (Source: docs/memory/Single Identity.md)
3. This isolation allows open/close of the protected area. (Source: docs/memory/Single Identity.md)

## Observed Concept Elements (Names Only)
- Identity module
- Dedicated memory region
- Root method
- Permissions state
- Protected area open/close

## Incomplete Blocks
Incomplete: Identity Memory Isolation Semantics
Needed:
- Definition of "own memory" (separate address space? reserved pages?)
- Access control model for root method invocation
- Persistence behavior across sessions
Candidate Sources: docs/memory/Single Identity.md, memory-identity-overview.md

Incomplete: Permissions State Representation
Needed:
- Data structure or fields of permissions state
- Mutation / revocation lifecycle
- Relationship to capability set (if any)
Candidate Sources: docs/memory/Single Identity.md, nodes.md, capability-advertisement-extraction.md

Incomplete: Protected Area Lifecycle
Needed:
- Criteria for open vs closed transitions
- Event hooks or triggers
- Failure handling on unauthorized access
Candidate Sources: docs/memory/Single Identity.md

Verbatim scope: docs/memory/Single Identity.md only.
