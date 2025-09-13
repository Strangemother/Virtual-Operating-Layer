See also: [identity-memory-unification.md](identity-memory-unification.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: File System.md, File Names.md, grains.md, grain-iterator.md, file-resolution.md, FS vol top level naming.md
# Filesystem Overview (Extraction Synthesis)

Purpose: Collate explicit filesystem/storage naming and behavior statements. No inferred layering or schema introduced beyond phrasing present in sources.

## Core Entities (Sourced Statements)
1. Aggregate (ag) is a readable unit: ordered list of particle pointers (PP) resolved to data stream (Source: [File System.md](../../docs/fs/File%20System.md))
2. Phenocryst (Header) is independent metadata reference pointing to aggregate and grains (Source: [File System.md](../../docs/fs/File%20System.md))
3. Grain acts as address-like pointer plus iteration context grouping particles for an aggregate (Source: [grains.md](../../docs/fs/grains.md); [File System.md](../../docs/fs/File%20System.md))
4. Particle (Segment) is unchanging byte/binary content unit; subset of aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
5. Colloid is a functional read/fetch construct aggregating particles and may return grains/particles (Source: [File System.md](../../docs/fs/File%20System.md))
6. Orphan particle lacking header and neighbor references moves to cold-store after delay (Source: [File System.md](../../docs/fs/File%20System.md))
7. Particle phases: solid (persistent stored content), fluid (volatile content resides in RAM cache), floating (reference/content not applied to a graph) (Source: [File System.md](../../docs/fs/File%20System.md))
8. Mass is collection of peds and clods forming larger structure (Source: [File System.md](../../docs/fs/File%20System.md))
9. Ped is system-generated aggregate; Clod is user-generated aggregate (Source: [File System.md](../../docs/fs/File%20System.md))
10. Phenocryst references aggregate and grains (Source: [File System.md](../../docs/fs/File%20System.md))
11. Aggregate lists particle pointers to segments (Source: [File System.md](../../docs/fs/File%20System.md))
12. Grain resolves particle content into session space (Source: [File System.md](../../docs/fs/File%20System.md))
13. Colloid fetches particles (and possibly grains) (Source: [File System.md](../../docs/fs/File%20System.md))

## Naming & Resolution (Sourced Statements)
14. File naming references a permission resolving mechanism (Source: [File Names.md](../../docs/fs/File%20Names.md))
15. File resolution process (details not enumerated here) mentioned (Source: [file-resolution.md](../../docs/fs/file-resolution.md))
16. Grain iteration described (Source: [grain-iterator.md](../../docs/fs/grain-iterator.md))
17. Volume top level naming considerations stated (Source: [FS vol top level naming.md](../../docs/fs/FS%20vol%20top%20level%20naming.md))

## Observed Entities (Names Only)
* Aggregate (ag)
* Phenocryst (Header)
* Grain
* Particle (Segment)
* Colloid
* Orphan Particle
* Solid / Fluid / Floating Particle (phases)
* Mass
* Ped / Clod
* Permission resolving (term context)
* Grain iterator
* File resolution
* Volume top level naming

## Relationships (Restated From Phrases)
* Phenocryst -> (Aggregate, Grains)
* Aggregate -> Particle pointers -> Segments
* Grain -> resolves particle content
* Colloid -> fetches particles / grains
* Ped/Clod -> are aggregates (system/user generated) composing Mass

## Incomplete Blocks

Incomplete: Permission Header Structure
Needed:
- Field names in permission resolving mechanism
- Link between permissions and filename canonical form
Candidate Sources: [File Names.md](../../docs/fs/File%20Names.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: File Resolution Procedure
Needed:
- Stepwise algorithm for resolution
- Error handling (missing header, orphan references)
Candidate Sources: [file-resolution.md](../../docs/fs/file-resolution.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: Grain Iterator Semantics
Needed:
- Iteration order guarantees
- Partial fetch / pagination behavior
Candidate Sources: [grain-iterator.md](../../docs/fs/grain-iterator.md), [grains.md](../../docs/fs/grains.md)

Incomplete: Volume Top Level Naming Rules
Needed:
- Reserved names / constraints
- Mapping to underlying aggregates
Candidate Sources: [FS vol top level naming.md](../../docs/fs/FS%20vol%20top%20level%20naming.md)

Incomplete: Phase Transition Triggers
Needed:
- Criteria to move particle between solid, fluid, floating
- Timing / state transition controls
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Orphan Recovery Workflow
Needed:
- Re-association procedure
- Cold-store retention policy specifics
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Verbatim scope: [File System.md](../../docs/fs/File%20System.md), [File Names.md](../../docs/fs/File%20Names.md), [grains.md](../../docs/fs/grains.md), [grain-iterator.md](../../docs/fs/grain-iterator.md), [file-resolution.md](../../docs/fs/file-resolution.md), [FS vol top level naming.md](../../docs/fs/FS%20vol%20top%20level%20naming.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 1.
