See also: [mesh-roles-matrix.md](mesh-roles-matrix.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: mesh.md, nodes.md
# Mesh Role Derivation (Extraction Stub)

Purpose: Capture explicit wording (if any) around how roles or positions within the mesh are established. Avoid introducing algorithms not present in sources.

## Sourced Statements
1. All units connected to the backbone assign a mesh and gain a position within the topology (Source: [mesh.md](../../docs/mesh.md))
2. Units may contain their own subgraph or inject a routine into the walking primary (Source: [mesh.md](../../docs/mesh.md))
3. VOL captures new nodes and integrates them to the MESH as a role governed by capabilities of the new RUNTIME (Source: [nodes.md](../../docs/nodes.md))
4. A unit may announce intent to become part of the system; mesh responds and onboards the unit (Source: [mesh.md](../../docs/mesh.md))
5. Core utilities and applications are distributed to other CORE or NODE machinery, each leaf performing a unique task (Source: [Scaling.md](../../docs/Scaling.md))
6. Distributed environment setup: RUNTIME can run as an app connecting to a CORE (Source: [Scaling.md](../../docs/Scaling.md))

## Observed Concepts (Names Only)
* position within the topology
* subgraph
* inject a routine
* role (governed by capabilities)
* onboarding
* membrane

## Incomplete Blocks

Incomplete: Role Enumeration
Needed:
- List of possible mesh roles (none enumerated in sources)
- Distinction (if any) between role and position
Candidate Sources: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md)

Incomplete: Derivation Inputs
Needed:
- Inputs (capabilities, topology state, session data) used to select role
- Whether onboarding handshake yields provisional vs final role
Candidate Sources: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md)

Incomplete: Subgraph Injection Rules
Needed:
- Conditions permitting a unit to inject a routine into the walking primary
- Isolation or safety constraints
Candidate Sources: [mesh.md](../../docs/mesh.md)

Incomplete: Topology Position Semantics
Needed:
- Stability guarantees of position assignment
- Reassignment triggers (network changes, capability update)
Candidate Sources: [mesh.md](../../docs/mesh.md), [nodes.md](../../docs/nodes.md)
 
Incomplete: Leaf Task Specialization
Needed:
- Formal definition of "leaf" vs other unit types
- Whether specialization influences role naming or topology weighting
Candidate Sources: [Scaling.md](../../docs/Scaling.md), [mesh.md](../../docs/mesh.md)

Incomplete: Membrane Influence
Needed:
- Whether membrane type constrains or informs role derivation
- Cross-membrane onboarding sequence ordering
Candidate Sources: [mesh.md](../../docs/mesh.md)

Verbatim scope: [mesh.md](../../docs/mesh.md), [nodes.md](../../docs/nodes.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md (extended set). All incomplete blocks remain outstanding; no ordering or algorithms added.
