---
Status: Draft
Last-Touched: 2025-09-13
Depends-On: boot-loop.md
---
# Boot Sequence Table (Extraction Draft)

Purpose: Present a linearized textual sequence of explicitly documented boot phases without inventing missing details.

## Ordered Phases (Sourced)

1. Process Foreign Boot – Console process initiates mandatory loadout (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
2. Load Boot SEM – Pre-compiled ZIM-SEM stores step values via SEM TAPE to mcom; prepares virtual environment (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
3. BIOS Completion Signal – Continuing statements load until BIOS emits complete (Source: [boot.md](../../docs/boot.md))
4. MBR Analogy Stage – SEM accepts BIOS config; prepares hardware/drivers/software platform; selects kernel (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
5. Driver Selection & Initialization – Build list and map platform-specific drivers (e.g., VDU, peripherals) (Source: [boot.md](../../docs/boot.md))
6. Zero Suite Handoff – First services: code libs, VM, pointer class, memory allocations, executor placements (Source: [zero-suite.md](../../docs/core/zero-suite.md))
7. Pointer 0 Payload Load – Executable payload unpacked to primary memory enabling pointer to step into position 0 (Source: [zero-suite.md](../../docs/core/zero-suite.md))
8. Establish Pointer Void State – No graph/stepper/os yet; pointer exists with minimal state (Source: [zero-suite.md](../../docs/core/zero-suite.md))
9. Top-Level Root Types & Imports Setup – ROOT/HOST import phase sets fundamental types & modules (Source: [top level.md](../../docs/top%20level.md))
10. OS Runtime First Phase – Pre-checks, framebuffer interface, base memory (vram), VOL FS, internal DB cache, system settings (Source: [os-runtime.md](../../docs/os-runtime.md))
11. OS Runtime Second Phase – Load drivers (graphics, network, audio, inputs, mesh), install presystems, load init apps (Source: [os-runtime.md](../../docs/os-runtime.md))
12. Loop Initialization – Key pointer executes BIOD tape establishing empty space for next magic key (Source: [the loop.md](../../docs/the%20loop.md))
13. Progressive Key Walking – Stepper/pointer advances through path; graph may mutate externally (Source: [the loop.md](../../docs/the%20loop.md))

## Phase Grouping (Derived Ordering Only)

Boot Core: 1–5
Foundation Services: 6–8
Runtime Construction: 9–11
Execution Loop: 12–13

## Incomplete Blocks

Incomplete: SEM TAPE Format
Needed:
- Field enumeration (GUID, init settings already mentioned but not structured)
- Encoding / delimiter rules
Candidate Sources: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md)

Incomplete: BIOS Completion Criteria
Needed:
- Explicit success condition for BIOS emit complete
- Error/failure pathway handling
Candidate Sources: [boot.md](../../docs/boot.md)

Incomplete: Driver Mapping Policy
Needed:
- Selection algorithm for multi-platform driver sets
- Fallback ordering or priority metrics
Candidate Sources: [boot.md](../../docs/boot.md), [os-runtime.md](../../docs/os-runtime.md)

Incomplete: Pointer 0 Payload Schema
Needed:
- Asset list structure inside pointer 0 executable
- Memory layout or relocation steps
Candidate Sources: [zero-suite.md](../../docs/core/zero-suite.md)

Incomplete: Root Types Load Ordering
Needed:
- Canonical order constraints (if any) among root type groups
- Dependency mapping between categories (simple, complex, abstracted)
Candidate Sources: [top level.md](../../docs/top%20level.md)

Incomplete: Loop Step Frequency
Needed:
- Target rate or scheduling policy for key stepper
- Concurrency governance with multiple pointers
Candidate Sources: [the loop.md](../../docs/the%20loop.md)

Incomplete: Multi-Phase Timing Targets
Needed:
- Allocation of < 5s (<2s preferred) budget across phases
- Metrics collection points
Candidate Sources: [os-runtime.md](../../docs/os-runtime.md)

Verbatim scope: [boot.md](../../docs/boot.md), [core/boot.md](../../docs/core/boot.md), [zero-suite.md](../../docs/core/zero-suite.md), [top level.md](../../docs/top%20level.md), [os-runtime.md](../../docs/os-runtime.md), [the loop.md](../../docs/the%20loop.md) only.
