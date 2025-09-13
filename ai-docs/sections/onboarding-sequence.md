Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: nodes.md, mesh.md, registry.md
# Onboarding Sequence (Extraction Stub)

Purpose: Linearize sourced statements about how a new NODE/RUNTIME joins an existing VOL, without inventing intermediate phases.

## Sourced Statements
1. RUNTIME may mesh into an existing VOL with an existing SESSION (Source: [nodes.md](../../docs/nodes.md))
2. VOL captures new nodes and integrates them to the MESH as a role governed by capabilities of the new RUNTIME (Source: [nodes.md](../../docs/nodes.md))
3. CORE captures capabilities and starts the relevant translator (Source: [nodes.md](../../docs/nodes.md))
4. Newly formed mesh example: Linux CORE + Windows RUNTIME + CONTAINER sharing a SESSION (Source: [nodes.md](../../docs/nodes.md))
5. A unit may announce intent to become part of the system; mesh responds and onboards the unit (Source: [mesh.md](../../docs/mesh.md))
6. All units connected to the backbone gain a position in topology (Source: [mesh.md](../../docs/mesh.md))
7. Registry is a database of live commands executed after cache/event requests (Source: [registry.md](../../docs/registry.md))

## Ordered Narrative (Derived Ordering – Not Normative)
NOTE: Sequence below is a collation; ordering not asserted by sources.
- Intent announcement (Source: [mesh.md](../../docs/mesh.md))
- Capability capture (Source: [nodes.md](../../docs/nodes.md))
- Translator start (Source: [nodes.md](../../docs/nodes.md))
- Role/topology position assignment (Source: [mesh.md](../../docs/mesh.md); [nodes.md](../../docs/nodes.md))
- Session sharing/continuation (Source: [nodes.md](../../docs/nodes.md))
- (Potential) command/event registration (Source: [registry.md](../../docs/registry.md))

## Incomplete Blocks

Incomplete: Formal Ordering Guarantees
Needed:
- Confirm actual mandated order between capability capture, translator start, role assignment, and session binding
- Whether topology position can precede translator start
Candidate Sources: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md)

Incomplete: Handshake Protocol
Needed:
- Message forms for intent announcement
- Acceptance / rejection signaling
Candidate Sources: [mesh.md](../../docs/mesh.md), [nodes.md](../../docs/nodes.md)

Incomplete: Role Assignment Criteria
Needed:
- Explicit factors used to compute role
- Any fallback/default role
Candidate Sources: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md)

Incomplete: Registry Integration
Needed:
- Whether onboarding inserts live commands
- Persistence of those commands relative to session
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Failure / Retry Semantics
Needed:
- Behavior if translator start fails
- Partial onboarding rollback steps
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Security / Authorization
Needed:
- Challenge/response or verification mention
- Membrane-level filtering or gating
Candidate Sources: [mesh.md](../../docs/mesh.md)

Verbatim scope: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md), [registry.md](../../docs/registry.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md (ordering still non-normative; marked as collation).
