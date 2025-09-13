# See: [filesystem-overview.md](filesystem-overview.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: filesystem.md
# Filesystem Layering Outline (Enumeration Only)

Purpose: Enumerate named filesystem/storage related entities without inferring hidden layers.

## Entities (As Named)
1. Aggregate (ag) (Source: [File System.md](../../docs/fs/File%20System.md))
2. Phenocryst (Header) (Source: [File System.md](../../docs/fs/File%20System.md))
3. Grain (Particle Pointer) (Source: [File System.md](../../docs/fs/File%20System.md); [grains.md](../../docs/fs/grains.md))
4. Particle (Segment) (Source: [File System.md](../../docs/fs/File%20System.md))
5. Colloid (Function referencing particles/grains) (Source: [File System.md](../../docs/fs/File%20System.md))
6. Orphan Particle (Source: [File System.md](../../docs/fs/File%20System.md))
7. Solid / Fluid / Floating Particle Phases (Source: [File System.md](../../docs/fs/File%20System.md))
8. Mass (Collection of peds/clods) (Source: [File System.md](../../docs/fs/File%20System.md))
9. Ped (System-generated aggregate) (Source: [File System.md](../../docs/fs/File%20System.md))
10. Clod (User-generated aggregate) (Source: [File System.md](../../docs/fs/File%20System.md))
11. Membrane (Network connective layer; mentioned contextually) (Source: [File System.md](../../docs/fs/File%20System.md))

## Noted Relationships (Descriptive Phrases Only)
* Phenocryst references aggregate and grains (Source: [File System.md](../../docs/fs/File%20System.md))
* Aggregate lists particle pointers (grains) to segments (Source: [File System.md](../../docs/fs/File%20System.md))
* Grain resolves particle content into session space (Source: [File System.md](../../docs/fs/File%20System.md))
* Colloid fetches particles (and possibly grains) (Source: [File System.md](../../docs/fs/File%20System.md))
* Orphan particles may solidify and move to cold-store (Source: [File System.md](../../docs/fs/File%20System.md))

## Incomplete Blocks

Incomplete: Layer Classification
Needed:
- Formal layered grouping (e.g., metadata, aggregation, resolution) – not specified
- Criteria distinguishing function vs data entity
Candidate Sources: [File System.md](../../docs/fs/File%20System.md), [grains.md](../../docs/fs/grains.md)

Incomplete: Permission Header Structure
Needed:
- Fields in permissions header referenced for filename resolution
- Access model / inheritance rules
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Phase Transition Mechanics
Needed:
- Triggers for particle phase changes (solid ↔ fluid ↔ floating)
- Timing or state machine representation
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Orphan Recovery Process
Needed:
- Steps for re-associating an orphan particle
- Hash/pointer usage for reconstruction
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Verbatim scope: [File System.md](../../docs/fs/File%20System.md), [grains.md](../../docs/fs/grains.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 2.
