---
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Core Runtime & Lifecycle

Summary:
- System Core: Single managing thread orchestrating apps/services, imports, filesystem usage, thread management, driver hoisting, garbage collection via Health Doctor. (Source: [system core.md](../../docs/core/system%20core.md))
- Health Doctor: Mentioned as integral for RAM/import cleanup; operational triggers unspecified. (Source: [system core.md](../../docs/core/system%20core.md))
- Terminology Hierarchy (Chamber, Mantle, Magmatic, Igneous): Defines layered grouping of core libraries and build variants; precise load ordering and exclusivity not enumerated. (Source: [terminology.md](../../docs/core/terminology.md))
- Kernel Naming Caveat: Term “Kernel” provisionally used; implements classical subsystems (process, memory, file, IPC, network, device) adapted for HOST-bound abstraction. (Source: [kernel.md](../../docs/core/kernel.md))
- Event Taxonomy Options: Dotted path vs vector-based triplet naming, unresolved selection. (Source: [kernel.md](../../docs/core/kernel.md))
- Structural Overview ties FS (VFS + HOST) with root configuration, header metadata chain, graph-based historical storage. (Source: [structure.md](../../docs/core/structure.md))
- Runtime Phases: Host config → pre-image → init config → first phase (pre-checks, pre-scene framebuffer, base memory (vram), FS, event trigger DB, environment settings) → second phase (drivers, presystems, init apps). (Source: [os-runtime.md](../../docs/core/os-runtime.md))

Incomplete: Health Doctor operational model
Needed:
- Trigger conditions for GC
- Scope of import cleanup vs memory reclamation
- Relation to permissions or FS header integrity
Candidate Sources: [system core.md](../../docs/core/system%20core.md), [structure.md](../../docs/core/structure.md)

Incomplete: Formal hierarchy & load sequencing of Chamber → Mantle → Magmatic → Igneous
Needed:
- Whether multiple Igneous builds may coexist
- Deployment vs runtime mutable boundaries
Candidate Sources: [terminology.md](../../docs/core/terminology.md)

Incomplete: Kernel vs System Core boundary
Needed:
- Which subsystems are exclusive to System Core vs Kernel
- Planned canonical term (deprecate “Kernel”?)
Candidate Sources: [system core.md](../../docs/core/system%20core.md), [kernel.md](../../docs/core/kernel.md)

Incomplete: Event naming decision criteria
Needed:
- Performance, caching, or semantic reasons for selecting dotted vs vector
- Collision or namespacing policy
Candidate Sources: [kernel.md](../../docs/core/kernel.md)

Verbatim scope: restructured-notes-2025.md Section 1 only.
