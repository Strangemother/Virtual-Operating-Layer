Status: Draft
Last-Touched: 2025-11-30
Depends-On: sections/glossary.md

# Mesh Roles Matrix (Extraction)

Purpose: Aggregate explicit statements about CORE, RUNTIME, NODE roles, capability-driven role assignment, and leaf tasks; capture gaps around capability advertisement schema.

## Sourced Role Concepts
1. CORE – Primary system image hosting VOL machinery, session apps, persistence. (Source: docs/nodes.md)
2. RUNTIME – Executable environment that can mesh into existing session with/without CORE. (Source: docs/nodes.md)
3. NODE – RUNTIME instance without a CONTAINER performing specific task. (Source: docs/nodes.md)
4. SESSION – Shared execution state across CORE and RUNTIME(s). (Source: docs/nodes.md)
5. Capability Set governs role integration when new RUNTIME connects. (Source: docs/nodes.md)
6. Internal DB Registry – Database of live commands executed post cache/event requests (not a Windows-style registry). (Source: docs/registry.md)
7. Leaf – Unit performing a unique task communicating back into the mesh. (Source: docs/Scaling.md)
8. Mesh – Topology of connected units. (Source: docs/mesh.md)

## Observed Role Interactions (Descriptive Only)
- New RUNTIME meshes into existing SESSION; CORE captures capabilities then starts relevant translator (implied capability negotiation). (Source: docs/nodes.md)
- Leaf units contribute specialized tasks communicating back into mesh (aggregation point implied at CORE/master context). (Source: docs/Scaling.md)
- Internal DB Registry executes live commands post cache/event requests (interaction locus for dynamic actions). (Source: docs/registry.md)

## Role Concept Table (Textual)
- CORE: Host of machinery + persistence (Source: docs/nodes.md)
- RUNTIME: Executable environment, may attach to CORE (Source: docs/nodes.md)
- NODE: Headless RUNTIME (Source: docs/nodes.md)
- CONTAINER: Visual/display execution context (Source: docs/nodes.md)
- SESSION: Shared execution state (Source: docs/nodes.md)
- Leaf: Specialized task unit (Source: docs/Scaling.md)
- Internal DB Registry: Live command execution database (Source: docs/registry.md)

## Incomplete Blocks
Incomplete: Capability Advertisement Schema
Needed:
- Fields enumerated for capability set
- Negotiation or merge procedure ordering
Candidate Sources: docs/nodes.md, docs/registry.md

Incomplete: Role Transition Triggers
Needed:
- Conditions elevating NODE to CORE (if allowed)
- Downgrade / detachment semantics
Candidate Sources: docs/nodes.md, docs/Scaling.md

Incomplete: Registry Lifecycle Ordering
Needed:
- When registry initializes relative to SESSION creation
- Failure/restart handling semantics
Candidate Sources: docs/registry.md, docs/nodes.md

Verbatim scope: docs/nodes.md, docs/Scaling.md, docs/registry.md, docs/mesh.md.
