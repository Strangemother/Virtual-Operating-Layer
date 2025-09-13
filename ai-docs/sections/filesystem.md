---
Status: Draft
Last-Touched: 2025-09-13
Source: restructured-notes-2025.md
---
# Filesystem & Storage Layers

Summary:
- Dual Layer (HOST + VFS): HOST provides conventional storage access; VFS adds custom virtual file system with graph-based history and transaction references; permissions externalized in sibling record. (Source: [structure.md](../../docs/core/structure.md))
- Aggregate Model: A VOL “file” (Aggregate) is an ordered list of segment pointers (grains/particles) resolved to a stream for requesting app via label lookup and header (Phenocryst) meta chain. (Source: [File System.md](../../docs/fs/File%20System.md))
- Phenocryst Header: Independent metadata record referencing aggregate composition (segment/grain list, permissions, dates, location metadata) enabling reconstruction and chaining of transactions. (Source: [File System.md](../../docs/fs/File%20System.md), [structure.md](../../docs/core/structure.md))
- Grain Role: Executes resolution of particles; maintains header with references to many particles; enables ordering and iteration; particles may exist across processes or remote spaces. (Source: [grains.md](../../docs/fs/grains.md), [File System.md](../../docs/fs/File%20System.md))
- Particle (Segment): Immutable byte/binary unit; may have forward/back pointers; phases: solid (unchanging stored), fluid (volatile/RAM cached), floating (unattached); orphan handling and cold-store notion. (Source: [File System.md](../../docs/fs/File%20System.md))
- Colloid: Functional read/aggregation construct assembling particles via grain association; mediates ordered stream assembly and possible partial returns. (Source: [File System.md](../../docs/fs/File%20System.md))
- Grain Iteration: Grain steps sequentially 0→n gathering particle content across spaces; user sees unified ordered stream abstracting distribution. (Source: [grain-iterator.md](../../docs/fs/grain-iterator.md))
- Resolution Style: Pointer/seek-based pattern where each particle pointer behaves like a seek reference; owner aggregates into final digestible form; pointers closed after exhaustion. (Source: [file-resolution.md](../../docs/fs/file-resolution.md))
- Naming & Pedology Analogy: Terms (Aggregate, Phenocryst, Grain, Particle, Colloid) drawn from geological metaphor; large phenocrysts termed megaphenocrysts; bonding/agglomeration/coalescence terminology noted. (Source: [FS vol top level naming.md](../../docs/fs/FS%20vol%20top%20level%20naming.md), [File System.md](../../docs/fs/File%20System.md))
- Distributed Access: Membrane layer implied for resolving remote grains; HOST owns request/transport aggregating distributed particle references into colloid for iteration. (Source: [File System.md](../../docs/fs/File%20System.md))
- Header Chain: Metadata (permissions, dates, locations, transaction IDs) stored separately; loss of header can render segment blocks unusable; chain supports historical reconstruction. (Source: [structure.md](../../docs/core/structure.md))

Incomplete: File Names specification
Needed:
- Definitions for filename pattern, label normalization, namespace or extension rules (current file empty)
- Distinction between user-facing label vs internal pointer addressing
Candidate Sources: [File Names.md](../../docs/fs/File%20Names.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: Permission externalization model
Needed:
- Structure/location of sibling permission records
- Access control integration with Phenocryst retrieval
Candidate Sources: [structure.md](../../docs/core/structure.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: Particle phase transitions
Needed:
- Criteria for moving particle between fluid ↔ solid ↔ floating states
- Cold-store reclamation or consolidation process
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Orphan particle recovery
Needed:
- Re-indexing algorithm using forward/back pointers absent Phenocryst
- Collision handling for multiple potential aggregates
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Colloid partial fetch semantics
Needed:
- Guarantees on ordering with partial or delayed particle resolution
- Timeout or retry policy for remote grains
Candidate Sources: [File System.md](../../docs/fs/File%20System.md), [grain-iterator.md](../../docs/fs/grain-iterator.md)

Incomplete: Membrane FS interaction
Needed:
- Formal API surface for membrane-mediated grain resolution
- Caching / consistency model for remote particle fetch
Candidate Sources: [File System.md](../../docs/fs/File%20System.md)

Incomplete: Header chain integrity / tamper model
Needed:
- Hashing or linkage specification for transaction chain
- Recovery steps if a link/header lost
Candidate Sources: [structure.md](../../docs/core/structure.md), [File System.md](../../docs/fs/File%20System.md)

Incomplete: Aggregate mutation workflow
Needed:
- Procedure for appending/replacing particles while preserving history
- Handling of version lineage vs overwrite
Candidate Sources: [File System.md](../../docs/fs/File%20System.md), [structure.md](../../docs/core/structure.md)

## Cross-References
See also: 
- [Filesystem Overview](filesystem-overview.md) for entity relationships and naming consolidation
- [Filesystem Layering Outline](filesystem-layering-outline.md) for structural hierarchy
- [Memory & Identity Model](memory-identity.md) for NN-as-file integration considerations

Verbatim scope: restructured-notes-2025.md Section 3 only.
