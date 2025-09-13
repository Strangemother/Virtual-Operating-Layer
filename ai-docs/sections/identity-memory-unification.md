# See: [filesystem-overview.md](filesystem-overview.md)
See also: [filesystem-overview.md](filesystem-overview.md)
Status: Working-Spec
Last-Touched: 2025-09-13
Depends-On: grains.md, File System.md, init-slots.md, first.md, memory-as-weights-and-biases.md
# Identity & Memory Unification (Extraction Note)

Purpose: Collate explicit statements referencing memory slots, grain/particle addressing, and neural network identity model. No inferred linkage beyond cited phrases.

## Sourced Statements
1. Grain acts as address-like pointer plus iteration context grouping particles for an aggregate (Source: [grains.md](../../docs/fs/grains.md); [File System.md](../../docs/fs/File%20System.md))
2. Grain resolves particle content into session space (Source: [File System.md](../../docs/fs/File%20System.md))
3. Particles are unchanging byte/binary content units (Source: [File System.md](../../docs/fs/File%20System.md))
4. Memory 'slots' provide static facades within the memory module assigned to unique names; underlying addresses hidden (Source: [init-slots.md](../../docs/memory/init-slots.md))
5. Some memory slots are assigned for the CPU only; they factor in the first root bits (Source: [first.md](../../docs/memory/first.md))
6. Two slots: #1 for micro ticks, #2 for master ticks for every micro overflow (Source: [first.md](../../docs/memory/first.md))
7. Identity model concept: neural network file (weights/biases) representing linear data (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))
8. Tensor unpack loads model then emits original linear data (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

## Observed Entities (Names Only)
* Grain
* Particle
* Aggregate
* Memory slot
* CPU-only slot
* Micro ticks / master ticks slots (#1, #2)
* Identity model (neural network file)
* Tensor unpack

## Descriptive Restatements (No New Claims)
* Grains provide addressing/iteration bridging particles to aggregates while memory slots provide named access facades (Sources: [grains.md](../../docs/fs/grains.md); [init-slots.md](../../docs/memory/init-slots.md))
* Identity model proposes replacing linear stored bytes with tensor representation then reconstructing via unpack (Source: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md))

## Incomplete Blocks

Incomplete: Grain to Slot Mapping
Needed:
- Whether grains can be mounted as memory slots
- Rules for exposing grain iteration via slot facade
Candidate Sources: [grains.md](../../docs/fs/grains.md), [init-slots.md](../../docs/memory/init-slots.md)

Incomplete: Identity Tensor Storage Placement
Needed:
- Location (aggregate vs slot vs separate structure) for neural network file
- Lifecycle events (creation, update, retirement)
Candidate Sources: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: Tensor Unpack to Particles Process
Needed:
- Whether unpack emits particles, grains, or direct byte stream
- Error handling for partial unpack
Candidate Sources: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md)

Incomplete: Slot Permission Model
Needed:
- Definition of write protections for CPU-only slots
- Escalation path for modifying protected slots
Candidate Sources: [first.md](../../docs/memory/first.md), [init-slots.md](../../docs/memory/init-slots.md)

Incomplete: Tick Slot Semantics
Needed:
- Formal meaning of micro vs master tick values
- Increment / overflow behavior
Candidate Sources: [first.md](../../docs/memory/first.md)

Incomplete: Identity Versioning
Needed:
- Scheme for tracking tensor revisions
- Relation to aggregate mutation or slot updates
Candidate Sources: [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md)

Verbatim scope: [grains.md](../../docs/fs/grains.md), [File System.md](../../docs/fs/File%20System.md), [init-slots.md](../../docs/memory/init-slots.md), [first.md](../../docs/memory/first.md), [memory-as-weights-and-biases.md](../../docs/concepts/memory-as-weights-and-biases.md) only.

---
### Promotion Record
Promoted to Working-Spec on 2025-09-13 referencing promotion-plan.md Batch 2.
