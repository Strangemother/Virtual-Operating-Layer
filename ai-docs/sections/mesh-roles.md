---
Status: Draft
Last-Touched: 2025-09-13
Depends-On: ../index.md
---
# Mesh Role Taxonomy (Extraction Draft)

Purpose: Consolidate explicit role/actor terminology from existing mesh-related documents without introducing new role names.

## Extracted Roles & Entities

1. CORE – Primary system image hosting VOL machinery, session apps, data persistence (Source: [nodes.md](../../docs/nodes.md); [Scaling.md](../../docs/Scaling.md))
2. RUNTIME – Executable environment that can run with or without a CORE; meshes into existing session (Source: [nodes.md](../../docs/nodes.md))
3. CONTAINER – Visual/display execution context rendering outputs; may run on same or different machine from CORE (Source: [nodes.md](../../docs/nodes.md); [Scaling.md](../../docs/Scaling.md))
4. NODE – A RUNTIME instance without a CONTAINER or direct view; performs task-specific computation (Source: [nodes.md](../../docs/nodes.md))
5. SESSION – Shared execution state spanning CORE and RUNTIME(s) (Source: [nodes.md](../../docs/nodes.md))
6. Master (Contextual label) – Informal reference to a single CORE in a simple deployment; explicitly noted as not a formal construct (Source: [nodes.md](../../docs/nodes.md))
7. Internal DB Registry – Database of live commands invoked after cache/event requests (Source: [registry.md](../../docs/registry.md))

## Observed Relationships

* A new NODE (RUNTIME) may advertise capabilities; CORE integrates and starts necessary translators (Source: [nodes.md](../../docs/nodes.md))
* CORE + Windows RUNTIME + CONTAINER combine into mesh sharing a SESSION (Source: [nodes.md](../../docs/nodes.md))
* Distribution dimension: CORE and RUNTIME designed for operation across multiple platforms (Source: [Scaling.md](../../docs/Scaling.md))
* Hardware scaling independent from session runtime (Source: [Scaling.md](../../docs/Scaling.md))

## Incomplete Blocks

Incomplete: Capability Advertisement Protocol
Needed:
- Concrete fields for capability description (e.g., transport, display, IO) – none enumerated
- Authentication / challenge steps during onboarding
Candidate Sources: [nodes.md](../../docs/nodes.md), future mesh protocol docs (TODO: discover)

Incomplete: Translator Selection Criteria
Needed:
- Rules for matching RUNTIME capabilities to translator components
- Lifecycle (init, reload, removal) for translators
Candidate Sources: [nodes.md](../../docs/nodes.md), [Scaling.md](../../docs/Scaling.md)

Incomplete: Registry Command Schema
Needed:
- Format of "live commands" entries
- Trigger sequence after cache and event requests
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Session Sharing Semantics
Needed:
- Ownership rules when multiple CORE or RUNTIME units attach
- Conflict resolution or arbitration model
Candidate Sources: [nodes.md](../../docs/nodes.md), [Scaling.md](../../docs/Scaling.md)

Incomplete: Role Boundary Definitions
Needed:
- Formal distinction (if any) between NODE vs RUNTIME when a display attaches later
- Conditions under which "Master" label should be avoided in docs
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Mesh Topology Representation
Needed:
- Canonical data structure representing mesh layout
- Addressing or naming scheme for units
Candidate Sources: [mesh.md](../../docs/mesh.md), [nodes.md](../../docs/nodes.md)

Verbatim scope: [nodes.md](../../docs/nodes.md), [registry.md](../../docs/registry.md), [Scaling.md](../../docs/Scaling.md) only.
