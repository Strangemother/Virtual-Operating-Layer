# Root Monolith Remaining Files Triage
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/phase-0.md, docs/root-monolith/applying-vol-runtime-libs.md, docs/root-monolith/security research.md, docs/root-monolith/phases.md, docs/root-monolith/readme.md, docs/root-monolith/comprehensive.md, docs/root-monolith/byte-function-load.md, docs/root-monolith/stack-processing.md
Verbatim scope: Listed files only.

## Purpose
Classify remaining root-monolith origin files for (a) Extraction Needed, (b) Archival Candidate, (c) Already Covered. No speculative semantics added.

## File Assessments

### phase-0.md
Key Points (Verbatim Concepts):
- Graph key #0 as protected start point (phase-0 test; owned by BIOD). (Source: docs/root-monolith/phase-0.md)
- First stage persists the loop; empty loop requests magic key (boot point). (Source: docs/root-monolith/phase-0.md)
- Some graph IDs are read-only / reserved. (Source: docs/root-monolith/phase-0.md)
- Fundamental libraries listed: Schedulers, Steppers, Pointer Executors. (Source: docs/root-monolith/phase-0.md)
- Required components list (system core monolith, CPUs, FS, membranes, "Cells"). (Source: docs/root-monolith/phase-0.md)
Classification: Extraction Needed (boot-start alignment & reserved ID concept not elsewhere consolidated).

### applying-vol-runtime-libs.md
Key Points:
- Three methods of supplying libraries: store assets in Lib/, create vol._vpt addressing local paths, apply module within root. (Source: docs/root-monolith/applying-vol-runtime-libs.md)
Classification: Extraction Needed (introduces library supply pathways not captured elsewhere).

### security research.md
Key Points:
- Initial random graph bits to encrypt within; sequence of graph keys + steps forming chain. (Source: docs/root-monolith/security research.md)
- Nodes as mathematical calculations; returns system key decrypted via two-part secure process. (Source: docs/root-monolith/security research.md)
- CRC start key using boot file; one-way BIOS key bits. (Source: docs/root-monolith/security research.md)
- root.lock() finalizes BIOS state and verifies record; refuses start on failure. (Source: docs/root-monolith/security research.md)
- CRC may denote boot key sequence bridging execution string; requires randomization to prevent tampering. (Source: docs/root-monolith/security research.md)
Classification: Extraction Needed (security initialization primitives not represented elsewhere).

### phases.md
Key Points:
- Phase 0 description for monolith initialization into base OS mode. (Source: docs/root-monolith/phases.md)
- Sequence: wake/magic number → power/register tests → run root binary → create root language/core methods → load virtual-ram functions → enforce code → load baseline functions → register house events → perform last call changes → load first user tape. (Source: docs/root-monolith/phases.md)
- User tape sources (flash, network, baked, host file, register). (Source: docs/root-monolith/phases.md)
- Subsequent load: Event Stack, Filesystem, Graph memory, multiprocessing, REPL, then GUI. (Source: docs/root-monolith/phases.md)
Classification: Extraction Needed (ordered list of initialization artifacts not yet collated).

### readme.md
Key Points:
- Monolith provides base language and bedrock tools (multiprocessing, async, REPL). (Source: docs/root-monolith/readme.md)
- Root core module list (printing, UART, exceptions, preprocessor, REPL receiver, websockets, multi-processor allocation, runtime module loadouts, early config management, graph methods, clock & scheduler). (Source: docs/root-monolith/readme.md)
- Input stream model (continuous, char-stepped graph progression, termination yields command). (Source: docs/root-monolith/readme.md)
- Graph key 0 start description (duplicate concept from phase docs). (Source: docs/root-monolith/readme.md)
- Output stream headless container description; container debug surface elements list. (Source: docs/root-monolith/readme.md)
Classification: Extraction Needed (consolidated functional inventory + input stepping model).

### comprehensive.md
Key Points:
- Checklist-style module list: Runtime, VRAM, echo printer, Memory Modules, Register, Graph Memory, Event Stack, Resource Reader, Interpreter, Filesystem, REPL. (Source: docs/root-monolith/comprehensive.md)
- VRAM paging size suggestion (65K per slice) and closed allocation space. (Source: docs/root-monolith/comprehensive.md)
Classification: Extraction Needed (structured module dependency hints & sizing reference).

### byte-function-load.md
Key Points:
- Memory module can access HOST vol file; load memory byte arrays as compiled executable; OS accesses loaded executable at address. (Source: docs/root-monolith/byte-function-load.md)
- Code allocator stores chunk under predictable function name; code chunk may be precompiled file or macro-generated. (Source: docs/root-monolith/byte-function-load.md)
Classification: Extraction Needed (bytecode loading pathway distinct from earlier acquisition notes).

### stack-processing.md
Key Points:
- Displays traced frames/events for simple Python function calls (call/line/return events, co_stacksize). (Source: docs/root-monolith/stack-processing.md)
Classification: Archival Candidate (illustrative trace; no VOL-specific normative claims).

## Summary Table
- Extraction Needed: phase-0.md, applying-vol-runtime-libs.md, security research.md, phases.md, readme.md, comprehensive.md, byte-function-load.md
- Archival Candidate: stack-processing.md
- Already Covered: (none newly eliminated)

## Extraction Documents Created
- root-monolith-phase-0-extraction.md
- root-monolith-libs-extraction.md
- root-monolith-security-init-extraction.md
- root-monolith-phase-sequence-extraction.md
- root-monolith-monolith-readme-extraction.md
- root-monolith-comprehensive-extraction.md
- root-monolith-byte-function-load-extraction.md

## New Term Candidates (Working-Term Stubs Needed)
- Graph Key 0 (if not already canonicalized) (Source: docs/root-monolith/phase-0.md; readme.md)
- Reserved Graph ID (Source: docs/root-monolith/phase-0.md)
- BIOD (appears owning phase-0 test) (Source: docs/root-monolith/phase-0.md)
- vol._vpt (Source: docs/root-monolith/applying-vol-runtime-libs.md)
- Initial Graph Bits (security) (Source: docs/root-monolith/security research.md)
- CRC Start Key (Source: docs/root-monolith/security research.md)
- root.lock() (boot integrity operation) (Source: docs/root-monolith/security research.md)
- User Tape (Source: docs/root-monolith/phases.md)
- Enforced Code (first-load AOP extensions) (Source: docs/root-monolith/phases.md)
- Virtual RAM (VRAM) Slice (65K suggestion) (Source: docs/root-monolith/comprehensive.md)
- Code Allocator (Source: docs/root-monolith/byte-function-load.md)

## Incomplete Blocks (To Add or Merge)
```
Incomplete: Security Initialization Chain
Needed: Ordering of initial graph bits → key chain derivation → CRC randomization → root.lock() validation.
Candidate Sources: docs/root-monolith/security research.md, docs/root-monolith/phase-0.md
```
```
Incomplete: Library Provision Mechanisms
Needed: vol._vpt file structure; resolution precedence vs Lib/ directory; module application constraints.
Candidate Sources: docs/root-monolith/applying-vol-runtime-libs.md, docs/core/system core.md
```
```
Incomplete: Phase 0 Ordered Requirements
Needed: Mandatory vs optional steps; error handling; idempotency when re-entered.
Candidate Sources: docs/root-monolith/phases.md, docs/root-monolith/phase-0.md
```
```
Incomplete: Module Dependency Graph
Needed: Formal dependency edges among Runtime, VRAM, Memory Module, Register, Graph Memory, Event Stack, Resource Reader, Interpreter, Filesystem, REPL.
Candidate Sources: docs/root-monolith/comprehensive.md, docs/root-monolith/readme.md
```
```
Incomplete: Byte Function Load Contract
Needed: File format requirements; executable memory safety; naming/pointer collision policy.
Candidate Sources: docs/root-monolith/byte-function-load.md, docs/root-monolith/memory-module.md
```
```
Incomplete: Input Stream Stepping Semantics
Needed: Termination key definition; concurrency model for multiple streams; error on partial command.
Candidate Sources: docs/root-monolith/readme.md, docs/root-monolith/commands.md
```

## Outstanding Gaps (Unresolved Status Snapshot)
- Input termination criteria (still open after readme extraction)
- Walking register structure
- Cold-store entropy policy
- Frame Switcher semantics
- Code allocator mechanism
- Variation tree definition
- Library auto-exposure rules
- Byte function reconstruction ordering
- Checksum referencing algorithm & failure handling
- Execution safety for byte-loaded functions

## Notes
- Security and phase boot content overlaps with previously extracted boot-sequence materials but introduces distinct integrity primitives; kept separate pending correlation evidence.
- Stack processing trace treated as illustrative; excluded from extraction.
