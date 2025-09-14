 Walking Register (Working-Term)
 Definition: Register that accumulates results of continuous input stream character steps until termination. (Source: docs/root-monolith/readme.md)
 Status: Stub

 Input-Session Key (Working-Term)
 Definition: Key stepped with each input character in continuous REPL stream; termination yields execution. (Source: docs/root-monolith/readme.md)
 Status: Stub

 Variation Tree (Working-Term)
 Definition: Structure associated with generative grammar; node/edge semantics not defined. (Source: docs/root-monolith/comprehensive.md)
 Status: Stub

 Generative Grammar (Working-Term)
 Definition: Grammar used with variation tree for structural spec generation; formal rules absent. (Source: docs/root-monolith/comprehensive.md)
 Status: Stub
---
Status: Working-Spec
Last-Touched: 2025-09-13
Source: restructured-notes-2025.md
---
# Glossary Seed

Core Runtime Terms
+ Chamber – Directory of magmatic core libraries (Source: [terminology.md](../../docs/core/terminology.md))
+ Mantle – Collection of modules/packages forming installable library store (Source: [terminology.md](../../docs/core/terminology.md))
+ Magmatic (Magma) – Grouping of mantle and core components (Source: [terminology.md](../../docs/core/terminology.md))
+ Igneous – Root monolith build relying on stable mantle (Source: [terminology.md](../../docs/core/terminology.md))
+ System Core – Managing thread for apps/services and housekeeping (Source: [system core.md](../../docs/core/system%20core.md))
+ Health Doctor – Garbage collection / cleanup component (Source: [system core.md](../../docs/core/system%20core.md))
+ Procedure Graph – Ordered function chain representing application execution (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
+ Pointer – Header element executing SES and graph mutations (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
+ Stepper – Walker resolving next pointer and executing sequentially (Source: [graph stepper.md](../../docs/core/graph%20stepper.md))
+ SES (Self Executing Source) – Function/code unit executed via pointer (Source: [graph functions.md](../../docs/core/graph%20functions.md))
+ Context Frame – Current view with memory, graph, temp data, APIs (Source: [frame-context.md](../../docs/core/frame-context.md))
+ Zero Suite – First service set post-handoff (Source: [zero-suite.md](../../docs/core/zero-suite.md))
+ Node Compass – Internal vector path resolution map (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
Stepper Machine – Manager for stepper frequency/allowances; injects post-step routines; coexists with peers via membranes (Source: [graph stepper.md](../../docs/core/graph%20stepper.md))
Machine Parent – Builder/owner of stepper machines; provides facades & subset graph; monitors lifecycle (Source: [graph stepper.md](../../docs/core/graph%20stepper.md))
 + SEM TAPE – Mechanism used by boot zim sem to store loading step values into mcom as a TAPE string (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
 + mcom – Anonymous memory reference/file descriptor receiving SEM TAPE data (config, kernel address, loading steps) (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
 Vector (Graph Position Vector) – Position identifier used in pointer/function examples (Source: [graph functions.md](../../docs/core/graph%20functions.md))
 Modulo Collision (Compass) – Risk where modulo of looped pointer path collides with valid compass direction (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
 Boot zim sem – Pre-compiled boot SEM maintaining GUID and init settings (Source: [boot.md](../../docs/boot.md); [core/boot.md](../../docs/core/boot.md))
 Tape (Pointer Tape) – Sequence of keys describing execution path (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
	Aliases: Pointer Tape (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))

Filesystem & Storage Terms
+ Aggregate (ag) – Readable unit: ordered list of particle pointers (PP) resolved to data stream (Source: [File System.md](../../docs/fs/File%20System.md))
+ Phenocryst (Header) – Independent metadata reference pointing to aggregate and grains (Source: [File System.md](../../docs/fs/File%20System.md))
+ Grain – Address-like pointer plus iteration context grouping particles for an aggregate (Source: [grains.md](../../docs/fs/grains.md); [File System.md](../../docs/fs/File%20System.md))
+ Particle (Segment) – Unchanging byte/binary content unit; subset of aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Colloid – Functional read/fetch construct aggregating particles (may return grains/particles) (Source: [File System.md](../../docs/fs/File%20System.md))
+ Orphan Particle – Particle lacking header and neighbor references; moves to cold-store after delay (Source: [File System.md](../../docs/fs/File%20System.md))
+ Solid Particle – Particle with persistent stored content (Source: [File System.md](../../docs/fs/File%20System.md))
+ Fluid Particle – Particle whose volatile content resides in RAM cache (Source: [File System.md](../../docs/fs/File%20System.md))
+ Floating Particle – Particle reference/content not applied to a graph (Source: [File System.md](../../docs/fs/File%20System.md))
+ Mass – Collection of peds and clods forming larger structure (Source: [File System.md](../../docs/fs/File%20System.md))
+ Ped – System-generated aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Clod – User-generated aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Particle Phase – State of particle: solid, fluid, floating (Source: [File System.md](../../docs/fs/File%20System.md))

Mesh / Distribution Terms
+ Membrane – Connectivity/transport layer bridging internal and external spaces (Source: [mesh.md](../../docs/mesh.md))
+ Mesh – Topology of connected units (Source: [mesh.md](../../docs/mesh.md))
+ CORE – Primary system image hosting VOL machinery, session apps, persistence (Source: [nodes.md](../../docs/nodes.md))
+ RUNTIME – Executable environment that can mesh into existing session with/without CORE (Source: [nodes.md](../../docs/nodes.md))
+ CONTAINER – Visual/display execution context for rendering outputs (Source: [nodes.md](../../docs/nodes.md); [display (container).md](../../docs/display%20(container).md))
+ NODE – RUNTIME instance without a CONTAINER performing specific task (Source: [nodes.md](../../docs/nodes.md))
+ SESSION – Shared execution state across CORE and RUNTIME(s) (Source: [nodes.md](../../docs/nodes.md))
+ Master (contextual) – Informal label for single CORE deployment; not formal role (Source: [nodes.md](../../docs/nodes.md))
+ Internal DB Registry – Database of live commands executed post cache/event requests (Source: [registry.md](../../docs/registry.md))
	Aliases: Live Command Database (Source: [registry.md](../../docs/registry.md))
 + Role (mesh) – Position within topology assigned when unit connects (Source: [mesh.md](../../docs/mesh.md))
 + Capability Set (working-term) – Aggregate capabilities of new RUNTIME governing its role integration (Source: [nodes.md](../../docs/nodes.md))
 + Leaf (distribution) – Unit performing a unique task communicating back into the mesh (Source: [Scaling.md](../../docs/Scaling.md))

Interface & Presentation Terms
+ Display Container – Rendering container orchestrating visual output (Source: [display (container).md](../../docs/display%20(container).md))
+ Facade – Abstraction exposing simplified interface (Source: [Facade.md](../../docs/Facade.md))
+ Translator – Component translating input/output data formats between RUNTIME and CONTAINER (Source: [inputs.md](../../docs/inputs.md))
+ Portal (Container Portal) – Interface surface through which inputs/outputs flow (Source: [inputs.md](../../docs/inputs.md))
+ Layer Assignment – ID-assigned draw/display layer binding (Source: [display (container).md](../../docs/display%20(container).md))

Boot & Loop Terms
+ Pointer 0 – Initial pointer invoked post zero-suite (Source: [boot.md](../../docs/boot.md); [zero-suite.md](../../docs/core/zero-suite.md))
 + SEM (Boot SEM) – Boot sequence self executing module reference (Source: [boot.md](../../docs/boot.md))
 + Magic Value (Pointer 0) – Value that sends pointer from position 0 to first position (Source: [zero-suite.md](../../docs/core/zero-suite.md))
 Micro Ticks Slot – Slot #1 tracking micro ticks (Source: [first.md](../../docs/memory/first.md))
 Master Ticks Slot – Slot #2 tracking master ticks per micro overflow (Source: [first.md](../../docs/memory/first.md))

Memory & Identity Terms
+ (Identity Model) – Neural network file concept (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
+ Data-as-NN Hypothesis – Replacement of linear dataset with trained tensor (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
+ Tensor Unpack – Loading model then emitting original linear data (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

Root & Foundational Apps Terms
+ Root Fundamental Apps – Core baseline applications (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
+ Container Manifest – Describes containerized components (Source: [container-manifest.md](../../docs/container-manifest.md))
+ First Apps – Initial demonstration/baseline apps (Source: [first-apps.md](../../docs/first-apps.md))

Aliases
+ Procedure Graph: exec graph, application graph (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))

Incomplete: Glossary completeness
Needed:
- Sector (if distinct) definition
- Capability advertisement fields (mesh onboarding)
- Canonical input event category names
- Tensor persistence state taxonomy
- Capability Advertisement (schema pending – only capture operation observed) (Source: [nodes.md](../../docs/nodes.md))
Candidate Sources: Files in: ../../docs/fs/, ../../docs/concepts/, ../../docs/mesh.md, ../../docs/nodes.md, ../../docs/registry.md, ../../docs/display (container).md

---
### New Term Candidate Stubs (Pending Validation)

Softheader (working-term) – Threshold preceding a hard peak triggering a light cleaner pass. (Source: [garbage collector.md](../../docs/garbage%20collector.md))
Hard Peak (working-term) – Resource usage level causing freeze and hard clean. (Source: [garbage collector.md](../../docs/garbage%20collector.md))
Quiet Time Cleaner – Garbage collection process executed when no other app uses CPU. (Source: [garbage collector.md](../../docs/garbage%20collector.md))
Perfect Hashmap (working-term) – Proposed mapping enabling linear memory allocation through named references. (Source: [Contigious address names.md](../../docs/core/Contigious%20address%20names.md))
Closed Loop Algorithm (working-term) – Alternative addressing method locking memory within bounded space. (Source: [Contigious address names.md](../../docs/core/Contigious%20address%20names.md))
Paging (address pages) – Partitioning approach allocating subsets of graph steps to a walking machine. (Source: [Contigious address names.md](../../docs/core/Contigious%20address%20names.md))

Acquisition Unit (working-term) – Unit performing frame orientation, block processing, and block mapping during memory acquisition pipeline. (Source: [memory-module.md](../../docs/root-monolith/memory-module.md))
Non-Acquisition Unit (working-term) – Unit that consumes or references mapped memory without performing acquisition steps. (Source: [memory-module.md](../../docs/root-monolith/memory-module.md))
Frame Orientation (working-term) – Initial operation aligning a frame prior to processing a memory block. (Source: [memory-module.md](../../docs/root-monolith/memory-module.md))
Block Mapping (working-term) – Step applying a processed memory block into broader structure/graph. (Source: [memory-module.md](../../docs/root-monolith/memory-module.md))
Quantum Frame (working-term) – Referenced frame state preceding command frame; semantics unspecified. (Source: [Frame Switching.md](../../docs/root-monolith/Frame%20Switching.md))
Command Frame (working-term) – Frame state following quantum frame; execution semantics unspecified. (Source: [Frame Switching.md](../../docs/root-monolith/Frame%20Switching.md))
Time Frame (working-term) – Identifier `T` mapped to time frame in layered addressing list. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Jump Frame (working-term) – Identifier `J` mapped to jump frame in layered addressing list. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Sequence Memory Graph (working-term) – Listed graph type `Y` without defined distinction criteria. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Series Memory Graph (working-term) – Listed graph type `Z` without defined distinction criteria. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Frame 0 (working-term) – Initial frame referenced for early command handling. (Source: [graph-walk.md](../../docs/root-monolith/graph-walk.md); [commands.md](../../docs/root-monolith/commands.md))
Command Lifecycle (working-term) – Concept implying staged processing of commands; phases not enumerated. (Source: [commands.md](../../docs/root-monolith/commands.md))
Index Space Domain (working-term) – Domain label in layered addressing enumeration; relationship to other domains undefined. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Expanded Space Domain (working-term) – Domain label enumerated alongside index space domain. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Family Space Domain (working-term) – Domain label enumerated; transformation rules absent. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Extended Family Space Domain (working-term) – Domain label enumerated; hierarchy unspecified. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Related Family Space Domain (working-term) – Domain label enumerated; linkage semantics absent. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Dictionary Space Domain (working-term) – Domain label enumerated; precedence unresolved. (Source: [step addresses and layers.md](../../docs/root-monolith/step%20addresses%20and%20layers.md))
Graph Key 0 (working-term) – Protected start point initiating root monolith config/module installation. (Source: [phase-0.md](../../docs/root-monolith/phase-0.md); [readme.md](../../docs/root-monolith/readme.md))
Reserved Graph ID (working-term) – Read-only graph identifiers reserved for internal operations. (Source: [phase-0.md](../../docs/root-monolith/phase-0.md))
BIOD (working-term) – Entity owning phase-0 test and protected graph key #0 (role unspecified). (Source: [phase-0.md](../../docs/root-monolith/phase-0.md))
vol._vpt (working-term) – File referencing local library paths (folders/zips) for module supply. (Source: [applying-vol-runtime-libs.md](../../docs/root-monolith/applying-vol-runtime-libs.md))
Initial Graph Bits (working-term) – Random graph bits used to seed encryption and key chains. (Source: [security research.md](../../docs/root-monolith/security%20research.md))
CRC Start Key (working-term) – Boot file CRC used as boot key sequence identifier. (Source: [security research.md](../../docs/root-monolith/security%20research.md))
root.lock() (working-term) – Operation finalizing BIOS state and verifying record before start. (Source: [security research.md](../../docs/root-monolith/security%20research.md))
User Tape (working-term) – Initial user startup/config tape loaded post phase steps. (Source: [phases.md](../../docs/root-monolith/phases.md))
Enforced Code (working-term) – First-load AOP / extension code baked and optionally updated via protected changes. (Source: [phases.md](../../docs/root-monolith/phases.md))
Virtual RAM Slice (working-term) – Suggested 65K page unit for VRAM allocation. (Source: [comprehensive.md](../../docs/root-monolith/comprehensive.md))
Code Allocator (working-term) – Component storing loaded executable chunks under predictable function names. (Source: [byte-function-load.md](../../docs/root-monolith/byte-function-load.md))

Naming Collision: Walking Register/Register
Observed Usage: "Walking register" (stream accumulation) vs generic "register" (system/registers functions). (Source: docs/root-monolith/readme.md; phases.md)
Action: Add glossary disambiguation entry

Naming Collision: Virtual RAM Slice/VRAM slice
Observed Usage: "Virtual RAM Slice" (suggested 65K page) vs "virtual-ram functions" (phase loading functions). (Source: comprehensive.md; phases.md)
Action: Add glossary disambiguation entry

Backlink: Term promotion status tracking in term-promotion-readiness-matrix.md

### Disambiguation Stubs (Pending)
Walking Register vs Register
Definition Boundary: Walking Register = continuous input accumulation construct; Register = general system/registers functions space and configuration memory references. (Source: docs/root-monolith/readme.md; phases.md)
Incomplete: Need explicit structural field list for Walking Register.

Virtual RAM Slice vs Virtual-RAM Functions
Definition Boundary: Virtual RAM Slice = proposed allocation sizing unit (65K suggestion); virtual-ram functions = phase load stage providing memory write functions. (Source: comprehensive.md; phases.md)
Incomplete: Need explicit inclusion criteria for virtual-ram function set and formal slice boundary metrics.

Incomplete: Candidate Term Formalization
Needed:
- Determine permanence of each working-term vs migration to formal definition
- Define disambiguation if alternative terms exist elsewhere (e.g., paging vs pages)
- Establish if Quiet Time Cleaner distinct from Health Doctor
Candidate Sources: docs/garbage collector.md, docs/core/Contigious address names.md, system core.md

Verbatim scope: restructured-notes-2025.md Section 10 plus additions from mesh-roles, interface-input-events, identity-persistence.

---
---
Archived Seed (Historical Duplicate Retained)
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Glossary Seed

+ Chamber – Directory of magmatic core libraries (Source: [terminology.md](../../docs/core/terminology.md))
+ Mantle – Collection of modules/packages forming installable library store (Source: [terminology.md](../../docs/core/terminology.md))
+ Magmatic (Magma) – Grouping of mantle and core components (Source: [terminology.md](../../docs/core/terminology.md))
+ Igneous – Root monolith build relying on stable mantle (Source: [terminology.md](../../docs/core/terminology.md))
+ System Core – Managing thread for apps/services and housekeeping (Source: [system core.md](../../docs/core/system%20core.md))
+ Health Doctor – Garbage collection / cleanup component (Source: [system core.md](../../docs/core/system%20core.md))
+ Procedure Graph – Ordered function chain representing application execution (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))
+ Pointer – Header element executing SES and graph mutations (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))
+ Stepper – Walker resolving next pointer and executing sequentially (Source: [graph stepper.md](../../docs/core/graph%20stepper.md))
+ SES (Self Executing Source) – Function/code unit executed via pointer (Source: [graph functions.md](../../docs/core/graph%20functions.md))
+ Context Frame – Current view with memory, graph, temp data, APIs (Source: [frame-context.md](../../docs/core/frame-context.md))
+ Zero Suite – First service set post-handoff (Source: [zero-suite.md](../../docs/core/zero-suite.md))
+ Node Compass – Internal vector path resolution map (Source: [graph node compass.md](../../docs/core/graph%20node%20compass.md))
+ Tape (Pointer Tape) – Sequence of keys describing execution path (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))

 Tape (Pointer Tape) – Sequence of keys describing execution path (Source: [graph pointer.md](../../docs/core/graph%20pointer.md))

Filesystem & Storage Terms
+ Aggregate (ag) – Readable unit: ordered list of particle pointers (PP) resolved to data stream (Source: [File System.md](../../docs/fs/File%20System.md))
+ Phenocryst (Header) – Independent metadata reference pointing to aggregate and grains (Source: [File System.md](../../docs/fs/File%20System.md))
+ Grain – Address-like pointer plus iteration context grouping particles for an aggregate (Source: [grains.md](../../docs/fs/grains.md); [File System.md](../../docs/fs/File%20System.md))
+ Particle (Segment) – Unchanging byte/binary content unit; subset of aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Colloid – Functional read/fetch construct aggregating particles (may return grains/particles) (Source: [File System.md](../../docs/fs/File%20System.md))
+ Orphan Particle – Particle lacking header and neighbor references; moves to cold-store after delay (Source: [File System.md](../../docs/fs/File%20System.md))
+ Solid Particle – Particle with persistent stored content (Source: [File System.md](../../docs/fs/File%20System.md))
+ Fluid Particle – Particle whose volatile content resides in RAM cache (Source: [File System.md](../../docs/fs/File%20System.md))
+ Floating Particle – Particle reference/content not applied to a graph; potentially incomplete (Source: [File System.md](../../docs/fs/File%20System.md))
+ Mass – Collection of peds and clods (aggregates) forming larger structure (Source: [File System.md](../../docs/fs/File%20System.md))
+ Ped – System-generated aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Clod – User-generated aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
+ Particle Phase – State of particle: solid, fluid, floating (Source: [File System.md](../../docs/fs/File%20System.md))

Mesh / Distribution Terms
+ Membrane – Connectivity/transport layer bridging internal and external spaces; maintains protocol & topology shape (Source: [mesh.md](../../docs/mesh.md))
+ Mesh – Topology of connected units assigning positions and enabling subgraph injection (Source: [mesh.md](../../docs/mesh.md))
 + Role (mesh) – Position within topology assigned when unit connects (Source: [mesh.md](../../docs/mesh.md))
 + Capability Set (working-term) – Aggregate capabilities of new RUNTIME governing its role integration (Source: [nodes.md](../../docs/nodes.md))

Memory & Identity Terms
+ (Identity Model) – Neural network file concept referencing weights/bias persistence (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

Interface & Presentation Terms
+ Display Container – Rendering container orchestrating visual output (Source: [display (container).md](../../docs/display%20(container).md))
+ Facade – Abstraction exposing simplified interface (Source: [Facade.md](../../docs/Facade.md))

Boot & Loop Terms
+ Pointer 0 – Initial pointer invoked post zero-suite (Source: [boot.md](../../docs/boot.md); [zero-suite.md](../../docs/core/zero-suite.md))
+ SEM (Boot SEM) – Referenced in boot sequence context (Source: [boot.md](../../docs/boot.md))

Root & Foundational Apps Terms
+ Root Fundamental Apps – Core baseline applications (Source: [Root Fundamental apps.md](../../docs/core/Root%20Fundamental%20apps.md))
+ Container Manifest – Manifest describing containerized components (Source: [container-manifest.md](../../docs/container-manifest.md))
+ First Apps – Initial demonstration or baseline apps (Source: [first-apps.md](../../docs/first-apps.md))

Aliases
+ Procedure Graph: exec graph, application graph (Source: [Procedure Graph.md](../../docs/core/Procedure%20Graph.md))

Incomplete: Glossary completeness
Needed:
- Coverage of filesystem (grains, header, sector), memory identity, mesh roles, interface layer
Candidate Sources: Files in: ../../docs/fs/, ../../docs/concepts/, ../../docs/mesh.md, ../../docs/nodes.md, ../../docs/registry.md, ../../docs/display (container).md

Incomplete: Mesh role taxonomy terms
Needed:
 - Explicit role names (node types, registry semantics)
Candidate Sources: [nodes.md](../../docs/nodes.md), [registry.md](../../docs/registry.md), [Scaling.md](../../docs/Scaling.md)

Incomplete: Memory identity detailed enumeration
Needed:
 - Formal identity persistence states
 - Mapping between identity and filesystem aggregates
Candidate Sources: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md), files in ../../docs/fs/

Incomplete: Interface input event taxonomy
Needed:
 - Canonical list of input event types
 - Mapping to display container handlers
Candidate Sources: [inputs.md](../../docs/inputs.md), [display (container).md](../../docs/display%20(container).md), [Facade.md](../../docs/Facade.md)

Incomplete: Boot sequence nomenclature normalization
Needed:
 - Definitive definitions for SEM, Zero Suite handoff markers, pointer 0 payload schema
Candidate Sources: [boot.md](../../docs/boot.md), [zero-suite.md](../../docs/core/zero-suite.md), [top level.md](../../docs/top%20level.md)

 Verbatim scope: restructured-notes-2025.md Section 10 only.

---
Promotion Record:
Promoted: 2025-09-13
Basis: Criteria met per policy-promotion.md (alias normalization, duplicates collapsed)
Sources: glossary historical seed, graph pointer.md, graph node compass.md, boot.md, registry.md
