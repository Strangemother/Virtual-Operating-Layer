---
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Root & Foundational Apps / Containerization

Summary:
- Root Fundamentals Set: Graph machine (system-wide graph representation), Address resolver (incoming graph key to app path resolution), Virtual memory (contiguous allocation with addressing). (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- Pointer Class Dependencies: Requires persistent + virtual memory foundations. (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- Stepper Class Dependencies: Needs graph machine subsets + address resolver to advance pointer. (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- Stepper Machine Role: Uses graph machine plus context generation for cells (subsets) enabling multi-context operation. (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- BIOD vs Monolith Analogy: Root runtime (BIOD) hosts monolith that can generate subsets and dispatch kernels to other BIODs by recompiling with added graph features prior to SES actuation. (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- Core Apps (Libraries): Import lib (synthetic modeling importer), Eval lib (live source execution / graph pointer collection), Stepping lib (graph key stepping for stepper machine). (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
- Container Manifest Purpose: Central configuration file in container `home/`, accessible to HOST/SYSTEM/VOL/Container; acts like master boot/init settings; default-initialized then overridden; runtime access is read-only. (Source: [container-manifest.md](../../docs/container-manifest.md))
- Manifest Name Key: Provides friendly name ID for applications. (Source: [container-manifest.md](../../docs/container-manifest.md))
- First Demo Apps Set: Audio Machine, Textpad (graph-linked note system), Timer (scheduler), REPL (in-VOL terminal), FS file reader, Permission system, Calculator (container HTML), WebGL/Vulkan 3D demo. (Source: [first-apps.md](../../docs/first-apps.md))

Incomplete: Graph machine interface
Needed:
- Public methods for acquiring & mutating graph representation
- Versioning or snapshot semantics when subsets created
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Address resolver specification
Needed:
- Input key format vs output path schema
- Error handling for unresolved keys
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Virtual memory model details
Needed:
- Allocation granularity and fragmentation policy
- Distinction persistent vs volatile regions
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Kernel dispatch process
Needed:
- Steps for compiling and sending new kernel to remote BIOD
- Authentication/authorization for kernel deployment
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Import lib synthetic modeling
Needed:
- Definition of "synthetic" modeling in import context
- Caching or dependency resolution rules
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Eval lib safety constraints
Needed:
- Sandboxing or permission gating for live code execution
- Rollback or transaction isolation for runtime mutations
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Stepping lib API boundaries
Needed:
- Minimal operations (next, jump, branch?)
- Interaction with address resolver under dynamic graph edits
Candidate Sources: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md)

Incomplete: Manifest key inventory
Needed:
- Complete list of supported keys beyond Name
- Override precedence and validation rules
Candidate Sources: [container-manifest.md](../../docs/container-manifest.md)

Incomplete: Demo app boot ordering
Needed:
- Which first apps are auto-start vs user-triggered
- Dependency prerequisites among demo apps
Candidate Sources: [first-apps.md](../../docs/first-apps.md)

Incomplete: Permission system demo scope
Needed:
- Operations covered (read/write/execute?)
- Integration with filesystem header/permissions chain
Candidate Sources: [first-apps.md](../../docs/first-apps.md), [File System.md](../../docs/fs/File%20System.md)

Verbatim scope: Extracted strictly from cited root/manifest/first apps documents.
