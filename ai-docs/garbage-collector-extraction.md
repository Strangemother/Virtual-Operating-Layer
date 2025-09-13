# Quiet Time Cleaner / Garbage Collector (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Source Files: docs/garbage collector.md

Purpose: Extract explicit behavior statements about garbage collection scheduling and resource reclamation triggers. No inferred mechanisms added.

## Sourced Statements
1. Quiet Time Cleaner deletes old imports, RAM cache, general live data imports. (Source: docs/garbage collector.md)
2. As application operates it populates filesystem graphs and import caches. (Source: docs/garbage collector.md)
3. GC runs when no other app is currently using CPU time (scheduled through core thread). (Source: docs/garbage collector.md)
4. If a softheader is reached within sleep time, a light cleaner is applied minimizing cost. (Source: docs/garbage collector.md)
5. If RAM, FS, Imports reach hard peak, the subset is frozen for a hard clean (standard GC cleanup). (Source: docs/garbage collector.md)
6. Aim: utilize power more efficiently via conditional cleaning strategy. (Source: docs/garbage collector.md)

## Observed Concept Elements (Names Only)
- Quiet Time Cleaner
- Old imports
- RAM cache
- Filesystem graphs
- Import caches
- Core thread scheduling
- Softheader (threshold) vs hard peak
- Light cleaner vs hard clean
- Freeze subset

## Incomplete Blocks
Incomplete: Threshold Definitions
Needed:
- Quantitative criteria for softheader
- Metrics defining hard peak (memory %, object count?)
- Scope of "subset" freeze (per app, global, per graph)
Candidate Sources: docs/garbage collector.md, system core.md

Incomplete: Light vs Hard Clean Operations
Needed:
- Actions performed in light cleaner (which resources skipped)
- Hard clean sequence ordering
- Impact on running graph execution
Candidate Sources: docs/garbage collector.md

Incomplete: Scheduling Semantics
Needed:
- Idle detection algorithm for "no other app using CPU time"
- Interaction with pointer/stepper execution cycles
- Preemption or deferral rules if workload resumes mid-clean
Candidate Sources: docs/garbage collector.md, docs/core/system core.md

Incomplete: Freeze Mechanism Behavior
Needed:
- What "freeze" entails (suspend writes? lock pages?)
- Duration and release conditions
- Error handling if access attempted during freeze
Candidate Sources: docs/garbage collector.md

Incomplete: Resource Classification
Needed:
- Formal list of reclaimable resource categories
- Relationship to particle / aggregate model (if any)
- Identity or permission checks required before deletion
Candidate Sources: docs/garbage collector.md, File System.md

Verbatim scope: docs/garbage collector.md only.
