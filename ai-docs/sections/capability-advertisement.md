See also: [mesh-roles-matrix.md](mesh-roles-matrix.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: mesh-roles.md
# Capability Advertisement (Extraction Stub)

Purpose: Summarize onboarding wording for new NODE/RUNTIME capability capture without inventing field schema.

## Sourced Statements
1. New NODE (RUNTIME) may mesh into existing VOL with existing SESSION (Source: [nodes.md](../../docs/nodes.md))
2. CORE will capture the capabilities of the new RUNTIME and start the relevant translator (Source: [nodes.md](../../docs/nodes.md))
3. Session shared across CORE and RUNTIME (Source: [nodes.md](../../docs/nodes.md))
4. VOL captures new nodes and integrates them to the MESH as a role governed by capabilities of the new RUNTIME (Source: [nodes.md](../../docs/nodes.md))
5. Example configuration lists resulting mesh composition (Linux CORE, Windows RUNTIME+CONTAINER) after capability capture and translator start (Source: [nodes.md](../../docs/nodes.md))

## Cross References
Related role assignment context: See: [mesh.md](../../docs/mesh.md) (role integration narrative – if present) – TODO: verify explicit role assignment wording.
Session continuity implications: See: [registry.md](../../docs/registry.md) – TODO: confirm whether registry mediates capability advertisement.

## Glossary Stubs (Do not define beyond sources)
Translator – mechanism started after capability capture (Source: [nodes.md](../../docs/nodes.md))
Capability Set (working-term) – aggregate capabilities governing role integration (Source: [nodes.md](../../docs/nodes.md))
Role (mesh) – placement governed by capability set (Source: [nodes.md](../../docs/nodes.md))

## Observed Entities (Names Only)
* capabilities (unspecified contents)
* translator (relevant)
* SESSION
* CORE / RUNTIME / NODE / CONTAINER

## Incomplete Blocks

Incomplete: Capability Field List
Needed:
- Enumerated capability attributes (e.g., display modes, IO channels) – not present
- Mandatory vs optional indicators
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Translator Selection Rules
Needed:
- Matching logic between capability set and chosen translator
- Re-initialization or hot-swap procedure
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Session Merge Semantics
Needed:
- Conflict resolution if capability overlaps existing node
- Ordering of capability registration events
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Capability Revocation / Update
Needed:
- Mechanism for removing or altering advertised capabilities
- Signaling path to dependent translators
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Role Derivation Algorithm
Needed:
- Explicit mapping rule from capability set to assigned mesh role
- Ordering dependencies (e.g., capability capture before translator start?)
Candidate Sources: [nodes.md](../../docs/nodes.md), [mesh.md](../../docs/mesh.md)

Incomplete: Registry Involvement (If Any)
Needed:
- Whether a registry component records or brokers capability advertisement
- Persistence model for capability metadata across sessions
Candidate Sources: [registry.md](../../docs/registry.md), [nodes.md](../../docs/nodes.md)

Verbatim scope: [nodes.md](../../docs/nodes.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 3.
