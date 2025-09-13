See also: [capability-advertisement.md](capability-advertisement.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: nodes.md, registry.md, Scaling.md, display (container).md
# Mesh Roles Matrix (Extraction)

Purpose: Enumerate roles and related capabilities explicitly mentioned. No inferred attributes added.

## Sourced Role/Entity Statements
1. RUNTIME may mesh into existing VOL with existing SESSION and its own RUNTIME (Source: [nodes.md](../../docs/nodes.md))
2. Node may send display information for a CONTAINER to capture (Source: [nodes.md](../../docs/nodes.md))
3. New NODE (RUNTIME) example: Windows machine with active CONTAINER (Source: [nodes.md](../../docs/nodes.md))
4. CORE captures capabilities of new RUNTIME and starts relevant translator (Source: [nodes.md](../../docs/nodes.md))
5. SESSION shared across CORE and RUNTIME; CORE maintains working core (session apps, data persistence) (Source: [nodes.md](../../docs/nodes.md))
6. Internal DB Registry is database of live commands (Source: [registry.md](../../docs/registry.md))
7. Scaling: VOL manifests as CORE machine; runtime with REPL and a VDU (Source: [Scaling.md](../../docs/Scaling.md))
8. RUNTIME may run as an app (exe) network connecting to CORE (Source: [Scaling.md](../../docs/Scaling.md))
9. Containers can utilize GPU in a client (Source: [Scaling.md](../../docs/Scaling.md))
10. Framebuffer and container output translators manage standard displays (Source: [Scaling.md](../../docs/Scaling.md))
11. Display container renders visual output (Source: [display (container).md](../../docs/display%20(container).md))

## Roles (Names Only)
* CORE
* RUNTIME
* NODE
* CONTAINER
* SESSION
* Translator (output / capability relevant)
* Registry (Internal DB Registry)

## Capability / Responsibility Bullets (Restated)
CORE:
- Captures capabilities of new RUNTIME (Source: [nodes.md](../../docs/nodes.md))
- Maintains session apps and data persistence (Source: [nodes.md](../../docs/nodes.md))

RUNTIME / NODE:
- May mesh into existing SESSION (Source: [nodes.md](../../docs/nodes.md))
- Sends display information for CONTAINER capture (Source: [nodes.md](../../docs/nodes.md))
- May run as app connecting to CORE (Source: [Scaling.md](../../docs/Scaling.md))

CONTAINER:
- Renders visual output (Source: [display (container).md](../../docs/display%20(container).md))
- Can utilize GPU in a client (Source: [Scaling.md](../../docs/Scaling.md))

SESSION:
- Shared execution state across CORE and RUNTIME(s) (Source: [nodes.md](../../docs/nodes.md))

Translator:
- Started based on captured capabilities of new RUNTIME (Source: [nodes.md](../../docs/nodes.md))
- Manages framebuffer / container output (Source: [Scaling.md](../../docs/Scaling.md))

Registry:
- Database of live commands (Source: [registry.md](../../docs/registry.md))

## Incomplete Blocks

Incomplete: Capability Schema Definition
Needed:
- Enumerated fields CORE captures from RUNTIME
- Update / revocation process
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: Translator Selection Mechanics
Needed:
- Matching logic from capability to translator choice
- Hot-swap or multi-translator criteria
Candidate Sources: [nodes.md](../../docs/nodes.md), [Scaling.md](../../docs/Scaling.md)

Incomplete: Registry Command Entry Format
Needed:
- Structure of a "live command"
- Lifecycle (insertion, expiration)
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Session Arbitration Rules
Needed:
- Conflict handling when multiple CORE candidates exist
- Authority resolution for persistence updates
Candidate Sources: [nodes.md](../../docs/nodes.md)

Incomplete: GPU Utilization Boundaries
Needed:
- Resource sharing constraints among multiple CONTAINERs
- Fallback path without GPU
Candidate Sources: [Scaling.md](../../docs/Scaling.md), [display (container).md](../../docs/display%20(container).md)

Verbatim scope: [nodes.md](../../docs/nodes.md), [registry.md](../../docs/registry.md), [Scaling.md](../../docs/Scaling.md), [display (container).md](../../docs/display%20(container).md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 1.
