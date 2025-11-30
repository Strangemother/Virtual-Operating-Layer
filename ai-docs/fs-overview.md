Status: Draft
Last-Touched: 2025-11-30
Depends-On: sections/glossary.md

# Filesystem Overview (Layering Extraction Skeleton)

Purpose: Synthesize discrete filesystem terminology into layered conceptual structure. Only explicit source statements cited; absent definitions captured as incomplete blocks.

## Layered Entities

### Particle
Descriptor: Unchanging byte/binary content unit; subset of aggregate. (Source: docs/fs/File System.md)
Phases: solid, fluid, floating (states). (Source: docs/fs/File System.md)
- Solid: Particle with persistent stored content. (Source: docs/fs/File System.md)
- Fluid: Volatile content resides in RAM cache. (Source: docs/fs/File System.md)
- Floating: Reference/content not applied to a graph. (Source: docs/fs/File System.md)
Orphan Particle: Lacking header and neighbor references; moves to cold-store after delay. (Source: docs/fs/File System.md)

### Grain
Descriptor: Address-like pointer plus iteration context grouping particles for an aggregate. (Source: docs/fs/grains.md; docs/fs/File System.md)
Iterator: Grain iterator concept present. (Source: docs/fs/grain-iterator.md)

### Aggregate (ag)
Descriptor: Readable unit: ordered list of particle pointers (PP) resolved to data stream. (Source: docs/fs/File System.md)
Ped: System-generated aggregate. (Source: docs/fs/File System.md)
Clod: User-generated aggregate. (Source: docs/fs/File System.md)
Mass: Collection of peds and clods forming larger structure. (Source: docs/fs/File System.md)

### Phenocryst (Header)
Descriptor: Independent metadata reference pointing to aggregate and grains. (Source: docs/fs/File System.md)
Role: Connects metadata to particle organization. (Source: docs/fs/File System.md)

### Colloid
Descriptor: Functional read/fetch construct aggregating particles (may return grains/particles). (Source: docs/fs/File System.md)

## Resolution & Access
- File resolution and naming files present (File Names, file-resolution). (Source: docs/fs/file-resolution.md; docs/fs/File Names.md)
- Top level volume naming: FS vol top level naming. (Source: docs/fs/FS vol top level naming.md)

## Lifecycle & State
- Orphan handling (cold-store after delay). (Source: docs/fs/File System.md)
- Particle phase transitions implied but not enumerated mechanistically. (Source: docs/fs/File System.md)

## Incomplete Blocks
Incomplete: Sector Definition
Needed:
- Formal "sector" term definition if distinct from particle/grain
- Physical vs logical boundary description
Candidate Sources: docs/fs/File System.md, docs/fs/build-assets.md

Incomplete: Permission / Access Model
Needed:
- Read/write/execute or alternative capability taxonomy
- Scope (aggregate vs particle) and inheritance rules
Candidate Sources: docs/fs/File System.md, docs/fs/file-resolution.md

Incomplete: Allocation / Mapping Tables
Needed:
- Existence and naming of allocation table structure
- Relationship to phenocryst metadata
Candidate Sources: docs/fs/File System.md, docs/fs/grains.md

Incomplete: Grain Iterator Semantics
Needed:
- Ordering guarantees
- Mutation during iteration constraints
Candidate Sources: docs/fs/grain-iterator.md

Incomplete: Mass Composition Rules
Needed:
- Criteria for grouping peds and clods into a mass
- Lifecycle or dissolution conditions
Candidate Sources: docs/fs/File System.md

Verbatim scope: docs/fs/File System.md, docs/fs/grains.md, docs/fs/grain-iterator.md, docs/fs/file-resolution.md, docs/fs/File Names.md, docs/fs/FS vol top level naming.md, docs/fs/build-assets.md
