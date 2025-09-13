See also: [capability-advertisement.md](capability-advertisement.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: registry.md
# Registry Capability Broker (Extraction Stub)

Purpose: Determine whether the internal DB registry mediates capability advertisement or execution context beyond its described function.

## Sourced Statements
1. Registry described as a database of live commands to run after cache and event requests (Source: [registry.md](../../docs/registry.md))

## Observed Concepts (Names Only)
* database of live commands
* cache
* event requests

## Incomplete Blocks

Incomplete: Capability Mediation
Needed:
- Any statement tying registry entries to node/RUNTIME capability advertisement
- Mechanism (if any) for storing capability metadata
Candidate Sources: [registry.md](../../docs/registry.md), [nodes.md](../../docs/nodes.md) (no current linkage observed)

Incomplete: Persistence Model
Needed:
- Whether registry state persists across sessions or reboots
- Data lifecycle and eviction rules
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Event / Command Relationship
Needed:
- Trigger conditions converting an event request into a live command execution
- Ordering or prioritization semantics
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Security / Isolation
Needed:
- Access control or isolation boundaries for live commands
- Validation before execution
Candidate Sources: [registry.md](../../docs/registry.md)

Verbatim scope: [registry.md](../../docs/registry.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md (minimal source; promotion acknowledges sparse definition).
