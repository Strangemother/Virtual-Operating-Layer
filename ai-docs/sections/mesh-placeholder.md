---
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Mesh / Nodes / Registry / Scaling

Summary:
- Membrane Concept: Membrane equated to selective transport layer shaping VOL capabilities; mediates data flow between internal user space and external spaces; may chain multiple membranes for operations (e.g., remote file write). (Source: [mesh.md](../../docs/mesh.md))
- Topological Positioning: Each unit connecting to backbone obtains a mesh position and can host its own subgraph or inject routines into primary walking graph. (Source: [mesh.md](../../docs/mesh.md))
- Membrane Responsibilities: Maintains connectivity, protocol methods, event cleaning, message transport path choice and potential reformatting. (Source: [mesh.md](../../docs/mesh.md))
- Onboarding Flow: External unit announces intent (e.g., via Bluetooth); mesh responds, potentially issues challenge via presentation membrane; negotiation can occur on separate dedicated graph segment. (Source: [mesh.md](../../docs/mesh.md))
- Master Terminology Caveat: “Master” not a formal persistent role; used only for simplicity when one CORE with RUNTIME plus containers exist. (Source: [nodes.md](../../docs/nodes.md))
- Node Definition: RUNTIME instance without container providing computational task (e.g., UART monitoring, backups); can mesh into existing session and send display data for container capture. (Source: [nodes.md](../../docs/nodes.md))
- Cross-Platform Node Capture: CORE (e.g., Linux) integrates capabilities of new platform RUNTIME (e.g., Windows with container) starting relevant translators; session shared across CORE and RUNTIME. (Source: [nodes.md](../../docs/nodes.md))
- Internal DB Registry: Lightweight database of live commands for post-cache or event-triggered execution; explicitly not a traditional OS registry. (Source: [registry.md](../../docs/registry.md))
- Distribution Scaling: VOL designed for multi-platform operation; core image minimal; utilities/apps distributed to other CORE or NODE hardware acting as leaves reporting back. (Source: [Scaling.md](../../docs/Scaling.md))
- Visual Scaling: Framebuffer/container translators adapt from tiny IoT displays (1x1) through 1080p/4K; multiple containers may run per desktop host across displays. (Source: [Scaling.md](../../docs/Scaling.md))
- Hardware Scaling: CORE on custom Linux scales with hardware build targets; RUNTIME may operate independently as app connecting over network. (Source: [Scaling.md](../../docs/Scaling.md))
- Process Distribution Model: Host OS runs many processes each with a loop and one container; single container runs a graph; processes stand waiting—implies multiprocessing spread across thin virtual containers. (Source: [multiprocessing.md](../../docs/multiprocessing.md))

Incomplete: Membrane taxonomy
Needed:
- Enumeration of membrane types (transport, presentation, challenge, device-specific)
- Required interface fields (connectivity state, protocol handlers)
Candidate Sources: [mesh.md](../../docs/mesh.md)

Incomplete: Mesh position addressing
Needed:
- Formal structure for "position" assignment in topology
- Collision or rebalancing strategy on dynamic joins/leaves
Candidate Sources: [mesh.md](../../docs/mesh.md), [nodes.md](../../docs/nodes.md)

Incomplete: Multi-graph injection rules
Needed:
- Constraints for unit injecting routines into primary walking graph
- Isolation boundaries and rollback semantics
Candidate Sources: [mesh.md](../../docs/mesh.md), [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

Incomplete: Onboarding challenge protocol
Needed:
- Message sequence (announce → challenge → response → acceptance)
- Security requirements (auth factors, rate limits)
Candidate Sources: [mesh.md](../../docs/mesh.md)

Incomplete: Registry data model
Needed:
- Command record format (fields, indexing)
- Persistence vs ephemeral lifespan rules
Candidate Sources: [registry.md](../../docs/registry.md)

Incomplete: Translator selection criteria
Needed:
- How capability capture drives translator startup for heterogeneous nodes
- Fallback if translator absent
Candidate Sources: [nodes.md](../../docs/nodes.md), [Scaling.md](../../docs/Scaling.md)

Incomplete: Visual scaling limits
Needed:
- Minimum and maximum supported framebuffer specifications
- Degradation strategy for ultra-small displays
Candidate Sources: [Scaling.md](../../docs/Scaling.md)

Incomplete: Multiprocessing container allocation
Needed:
- Policy for mapping loops/processes to containers and graphs
- Resource contention or scheduling approach between processes
Candidate Sources: [multiprocessing.md](../../docs/multiprocessing.md)

Incomplete: Leaf utility distribution workflow
Needed:
- Procedure for deploying core utilities/apps to remote leaf nodes
- Version synchronization / update triggers
Candidate Sources: [Scaling.md](../../docs/Scaling.md), [nodes.md](../../docs/nodes.md)

Verbatim scope: Extracted strictly from cited files (mesh, nodes, registry, Scaling, multiprocessing).
