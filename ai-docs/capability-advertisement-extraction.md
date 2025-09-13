Status: Draft
Last-Touched: 2025-09-13
Depends-On: mesh-roles-matrix.md

# Capability Advertisement Extraction

Purpose: Aggregate explicit references to capability-driven role assignment and identify absence of a formal advertisement schema. Only sourced statements included.

## Sourced Statements
1. Role integration governed by capabilities of new RUNTIME (capability set) when meshing into existing SESSION. (Source: docs/nodes.md)
2. CORE captures capabilities and starts relevant translator for new NODE/RUNTIME scenario. (Source: docs/nodes.md)
3. Leaf units perform unique tasks communicating back into mesh / master system aggregation. (Source: docs/Scaling.md)
4. Internal DB Registry executes live commands post cache/event requests (operational context; no capability fields given). (Source: docs/registry.md)

## Observed Concepts (Names Only)
- Capability Set (working-term) (Source: docs/nodes.md)
- Translator (initiated based on capabilities) (Source: docs/nodes.md)
- Leaf task specialization (Source: docs/Scaling.md)
- Registry live command execution (Source: docs/registry.md)

## Not Present
- Field list for capability advertisement (no keys such as cpu, memory, display, transport enumerated)
- Negotiation sequence or merge rules
- Versioning or expiry of capability data
- Security/authentication of provided capabilities

## Incomplete Blocks
Incomplete: Capability Field Enumeration
Needed:
- Canonical list of capability attributes
- Mandatory vs optional classification
Candidate Sources: docs/nodes.md, docs/registry.md, docs/Scaling.md

Incomplete: Negotiation / Merge Procedure
Needed:
- Ordering of capture vs translator initiation
- Conflict handling if multiple CORE-like nodes present
Candidate Sources: docs/nodes.md, docs/Scaling.md

Incomplete: Capability Update Semantics
Needed:
- Whether capabilities can be refreshed dynamically
- Trigger conditions for re-evaluating role
Candidate Sources: docs/nodes.md, docs/registry.md

Incomplete: Security & Trust Model
Needed:
- Validation mechanism for advertised capabilities
- Handling of malicious or overstated capability sets
Candidate Sources: docs/nodes.md

Verbatim scope: docs/nodes.md, docs/Scaling.md, docs/registry.md
