---
Status: Draft
Last-Touched: 2025-09-13
Source: restructured-notes-2025.md
---
# Boot & Loop Sequence

Summary:
- Foreign Process Start: Console process triggers mandatory loadout; parameters likely implicit via init file; represents the 'power on' equivalence. (Source: [boot.md](../../docs/core/boot.md))
- Boot SEM Load: Pre-compiled ZIM-SEM holds GUID + init settings; first statement stores TAPE of loading step values into anonymous mcom reference; environment parameters preload then BIOS process self-terminates handing control forward. (Source: [boot.md](../../docs/core/boot.md))
- BIOS Completion Signal: Continuing statements run until BIOS emits completion back to boot manager signaling readiness for next stage. (Source: [boot.md](../../docs/core/boot.md))
- MBR Analogy (Virtual): Non-physical MBR SEM accepts BIOS config, reads values, mediates control pass to chosen kernel; prepares initial libraries, IO, driver selection, VDU baseline. (Source: [boot.md](../../docs/core/boot.md))
- Driver Abstraction Layer: Target-device variability (i-device, Pi, Windows/Linux, container) normalized by driver selection compiled or mapped at MBR stage; IO may be transparent in container with sibling threads monitoring peripherals. (Source: [boot.md](../../docs/core/boot.md))
- Zero Suite Handoff: After MBR, first services establish VM (source machine), pointer class, memory allocations, executor placements; occurs before any graph or stepper exists (pointer alone in void). (Source: [zero-suite.md](../../docs/core/zero-suite.md))
- Pointer 0 Role: Executable payload (.bin / .elf like) unpacks VM assets into primary memory then sends magic value to transition to first post-zero position. (Source: [zero-suite.md](../../docs/core/zero-suite.md))
- Absence of Graph Pre-Zero: No graph/stepper/machine present; emphasizes staged construction where pointer fundamentals precede scheduling/execution fabric. (Source: [zero-suite.md](../../docs/core/zero-suite.md))
- OS-Runtime Phase (Pre-Graph) Alignment: Host config → pre-image → internal init config precede first phase tasks (pre-checks, framebuffer pre-scene, base memory + VOL FS, internal db cache, environment configuration). (Source: [os-runtime.md](../../docs/core/os-runtime.md))
- OS-Runtime Second Phase: Driver loading (graphics, network, audio, inputs, mesh membranes) → presystems install (using db cache + settings) → init apps load (user file entry point). (Source: [os-runtime.md](../../docs/core/os-runtime.md))
- Performance Target: Boot to working environment aspirational < 5s (preferred < 2s) across phases. (Source: [os-runtime.md](../../docs/core/os-runtime.md))
- Loop Definition Clarified: Loop is a key stepper advancing at predictable rate; end of tree may recycle to pointer location or close traversal; walker metaphor emphasizes path-built-next execution. (Source: [the loop.md](../../docs/the%20loop.md))
- Runtime Pointer Establishment: Upon runtime establishment pointer moves to runtime position (#0) executing BIOD tape statement to build empty space for incoming magic key; initial key yields next pointer; linear baked procedures may omit explicit returns. (Source: [the loop.md](../../docs/the%20loop.md))
- Graph Mutability During Loop: Graph may alter live, redirecting pointer; multiple pointers may concurrently operate on one graph; multiple graphs can exist across membranes/meshes. (Source: [the loop.md](../../docs/the%20loop.md))

Incomplete: Phase mapping table
Needed:
- Explicit alignment rows (Foreign Start / Boot SEM / BIOS Complete / MBR / Zero Suite / Pointer 0 / First Phase steps / Second Phase steps)
- Error handling & retry semantics per row
Candidate Sources: [boot.md](../../docs/core/boot.md), [os-runtime.md](../../docs/core/os-runtime.md), [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Pointer 0 payload specification
Needed:
- Structural fields (header, relocation info, embedded assets list)
- Validation / signature or hash mechanism before execution
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Boot SEM TAPE format
Needed:
- Field ordering for loading step values
- Encoding for GUID + init settings
Candidate Sources: [boot.md](../../docs/core/boot.md)

Incomplete: BIOS completion signaling
Needed:
- Mechanism (event, flag, return code) for BIOS 'complete' emission
- Timeout or watchdog behavior
Candidate Sources: [boot.md](../../docs/core/boot.md), [os-runtime.md](../../docs/core/os-runtime.md)

Incomplete: Driver selection mapping
Needed:
- Criteria for selecting device-specific vs generic driver
- Fallback strategy when asset absent
Candidate Sources: [boot.md](../../docs/core/boot.md)

Incomplete: Loop step frequency governance
Needed:
- How predictable rate is enforced (timer, tick source)
- Behavior under overrun or pointer stall
Candidate Sources: [the loop.md](../../docs/the%20loop.md)

Incomplete: Multi-pointer concurrency rules
Needed:
- Contention policy when multiple pointers mutate same graph segment
- Isolation or snapshot strategy
Candidate Sources: [the loop.md](../../docs/the%20loop.md), [Procedure Graph.md](../../docs/core/Procedure%20Graph.md)

## Cross-References
See also:
- [Boot Sequence Table](boot-sequence-table.md) for linearized phase list and format gaps
- [Boot Sequence Diagram](boot-sequence-diagram.md) for textual stage ordering
- [SEM TAPE Extraction](sem-tape-extraction.md) for TAPE format details
- [Pointer 0 Payload](pointer-0-payload.md) for executable payload structure

Verbatim scope: restructured-notes-2025.md Section 6 only.
