# Introducing VOL FS

Status: Draft
Last-Touched: 2026-08-23
Depends-On: overview.md

## Verbatim Scope

ai-docs-2/fs/overview.md, docs/fs/readme.md, docs/fs/File System.md,
docs/fs/file-resolution.md, docs/fs/grains.md, docs/fs/grain-iterator.md,
docs/fs/representation.md, docs/fs/Nomenclature.md,
docs/fs/nonimal-vector-names.md, docs/fs/Space and Space Discovery.md,
docs/fs/stock-coms.md, docs/fs/synthetic-markers.md, docs/core/structure.md

## A Different Starting Point for a Filesystem

When we say "file," most of us picture a named object containing a sequence of
bytes. We picture opening it, moving through it, changing some bytes, and
saving it again. The host filesystem usually makes that picture feel simple by
hiding where the bytes physically live.

VOL FS starts from a different question: what if the logical thing a person
wants to open does not have to be one contiguous object in one storage system?
The research notes describe a virtual filesystem that can present content from
local memory, a host filesystem, network services, or object storage. Its
logical content can be represented as metadata plus references to separately
stored byte or binary chunks. (Source: docs/fs/readme.md; docs/fs/Space and Space Discovery.md;
docs/fs/stock-coms.md)

That does not mean the reader should imagine a mysterious cloud of bytes with
no structure. The proposal has a structure. A user-facing "file" is generally
described internally as an **aggregate**. The aggregate is reached through a
header, associated with one or more **grains**, and reconstructed from
**particles**. A particle is a content chunk, and the aggregate preserves the
relationship that lets those chunks be read in order. (Source: docs/fs/File System.md;
docs/fs/grains.md; docs/fs/representation.md)

The simplest way to say it is this:

> VOL FS treats a logical item as a named composition of references to content,
> rather than assuming that the logical item must be one physical file.

This is a conceptual summary, not a finished protocol definition. The source
notes still need to settle the exact relationships among a file, aggregate,
grain, colloid, and phenocryst. (Source: ai-docs-2/fs/overview.md;
docs/fs/File System.md; docs/fs/Nomenclature.md)

## The Reader's Mental Picture

A conventional filesystem encourages us to think in terms of a path leading to
an object. VOL FS encourages us to think in terms of a reference leading to a
resolution process:

```text
caller
  |
  v
logical name or nominal vector
  |
  v
phenocryst: metadata and entry reference
  |
  v
aggregate: the logical readable unit
  |
  v
grain: ordered particle references
  |
  +--> particle --> local or memory space
  +--> particle --> host filesystem space
  +--> particle --> network or object space
                         |
                         v
                 resolved ordered stream
```

The picture is intentionally modest. It does not say that every particle is
remote, that every aggregate is distributed, or that every read executes code.
It says that the logical item may be resolved through references whose backing
spaces can differ. (Source: docs/fs/File System.md;
docs/fs/Space and Space Discovery.md; docs/fs/file-resolution.md)

## First, What Is a Particle?

A particle is the smallest content unit named by the filesystem notes. It is a
chunk of bytes or binary content, and it may be held in memory, on disk, or in
another abstract storage location. The notes allow its width to be determined
by the storage allocation, with additional particles following when the
available width is exhausted. (Source: docs/fs/memory allocation table.md;
docs/fs/File System.md)

The word "smallest" needs a little care here. It means the smallest unit in the
described content model, not necessarily one byte and not necessarily the
smallest unit understood by a physical device. A particle may contain a
substantial run of text, part of an image, or a fragment of another binary
resource. The source notes do not define a universal particle size.
(Source: docs/fs/memory allocation table.md)

A particle has an address that identifies its stored content. The notes
separate this address from a human-facing name: names may be shared, while a
particle address is intended to be unique. That separation matters because a
logical name can gather one particle or several particles without pretending
that the name itself is a physical location. (Source: docs/fs/Nomenclature.md;
docs/fs/nonimal-vector-names.md)

The notes also describe particle phases. A **solid** particle has persistently
stored content. A **fluid** particle is represented but its content is volatile,
likely cached in memory. A **floating** particle has a reference or content that
has not been applied to a graph or owner. These terms describe an appealing
lifecycle vocabulary, but the transitions between phases are not specified.
(Source: docs/fs/File System.md)

## Then, What Is an Aggregate?

An aggregate is the logical unit that a session or application is likely to
want to read. Rather than owning a contiguous byte array, it maintains the
organization needed to resolve a sequence of particle pointers. The filesystem
can then return the particles as discrete blocks or as an ordered stream.
(Source: docs/fs/File System.md)

This is where the natural-material language becomes useful. The notes compare a
user-created aggregate to a clod and a system-created aggregate to a ped. Many
such units may form a mass. Those names give the design a memorable vocabulary,
but they should not yet be mistaken for rules about how data is grouped or
stored. The creation and composition rules for peds, clods, and masses remain
open. (Source: docs/fs/File System.md)

The aggregate is therefore less like a box and more like a maintained answer to
the question: "Which pieces, in what order, make up this readable thing?" That
answer may be stable even if the pieces live in different spaces. This is the
central conceptual shift in VOL FS. (Source: docs/fs/File System.md;
docs/fs/readme.md)

## The Header: A Phenocryst

An aggregate needs an entry point. In the notes, that role is played by a
**phenocryst**, which is a header or independent metadata reference associated
with the aggregate. It may contain a local name, creation information,
permissions, locations, an owner, and a current or immediate hash. (Source: docs/fs/File System.md;
docs/core/structure.md; docs/fs/representation.md)

The phenocryst is what lets a human-friendly reference become a filesystem
operation. If a caller asks for something like `foo.bar.baz`, the filesystem
first needs a way to find the metadata that explains what that reference means.
The notes describe the header as that bridge between the logical name and the
content organization. (Source: docs/fs/File System.md;
docs/fs/shared mem view permissioning.md)

This also explains an important risk. If the content chunks survive but their
header or reference structure is lost, the system may no longer know how to
reconstruct the intended logical item. The notes explicitly identify lost
headers as a possible reason that otherwise stored chunks become unusable.
(Source: docs/core/structure.md; docs/fs/File System.md)

The phenocryst is not yet a complete schema. We do not have a settled list of
fields, a serialization format, or a definitive answer about whether it owns
an aggregate directly or points to another record. Those are not small details;
they determine how the filesystem can recover, authenticate, version, and
share a logical item. (Source: ai-docs-2/fs/overview.md;
docs/fs/File System.md; docs/core/structure.md)

## Where Do the Pieces Live?

VOL FS uses the word **space** for a configured storage location and the
service needed to use it. A space might be local storage, memory, FTP, S3, a
network service, or a proposed IPFS-backed store. The idea is not that all these
services become the same internally. The idea is that the virtual filesystem
can address them through a common resolution layer. (Source: docs/fs/Space and Space Discovery.md;
docs/fs/stock-coms.md)

A space has to do more than identify a place. It also needs the parameters and
translation procedures that allow a virtual particle reference to be stored or
retrieved there. The notes describe space discovery as considering the user
session, permissions, membrane, threads, remote services, and available
locations before selecting a viable writer or reader. (Source: docs/fs/Space and Space Discovery.md)

The **membrane** is the name given to the connective layer between a host volume,
the filesystem, user space, and network space. It is a useful way to talk about
crossing from one service or device into another, but the notes do not yet
define a membrane protocol, packet format, or failure model. (Source: docs/fs/File System.md;
docs/fs/Space and Space Discovery.md)

This gives VOL FS a deliberately broad storage horizon. A logical text item
might have local pieces, host-backed pieces, and remotely resolved pieces. It
might also begin in volatile memory and later become persistent. Those are
capabilities and design directions in the notes, not guarantees that every
implementation must distribute every item. (Source: docs/fs/readme.md;
docs/fs/File System.md)

## How a Read Feels to the User

From the user's point of view, a read should remain simple. They provide a
logical reference, and the filesystem returns content. Underneath, the notes
suggest a sequence like this:

1. The caller presents a name, vector, or other logical reference.
2. The filesystem locates the associated phenocryst or header.
3. The header identifies the aggregate and its grain or particle references.
4. Each reference is resolved through its assigned space.
5. The resolved particle content is ordered according to the aggregate's
   organization.
6. The caller receives particles or an ordered stream.

This is not intended to expose the storage topology to the reader. A caller
should not need to know whether the next particle came from memory, a local
host file, or an object service. The source notes describe the grain as
quietly stepping through spaces and ordered particles while yielding a stream
to the requesting interface. (Source: docs/fs/File System.md;
docs/fs/grains.md; docs/fs/grain-iterator.md)

The word "quietly" is a useful user-experience goal, but it should not hide
operational truth from a system administrator. Remote resolution can be slow,
permissions can prevent a grain from resolving, and a missing location can
make a particle unavailable. The notes identify these concerns but do not
define retries, timeouts, partial reads, cancellation, or error reporting.
(Source: docs/fs/File System.md; docs/fs/file-resolution.md;
docs/fs/Space and Space Discovery.md)

The broader VOL documentation also describes graph pointers and steppers that
walk keys and execute actions in context. That is adjacent to filesystem
resolution, but it is not automatically the same thing. A particle is content
in the filesystem model; the source notes do not establish that reading every
particle executes it. Keeping data resolution and graph execution distinct is
important until their boundary is deliberately defined. (Source: docs/core/graph pointer.md;
docs/core/graph stepper.md; docs/core/graph functions.md;
docs/fs/File System.md)

## A Friendly Name Is Not Necessarily a Path

The notes explore **nominal vectors** as names made from several words. One
example is `audio.eric.wedding`. In that example, the words can describe
meaningful dimensions of a reference and may also select different nominal
spaces. A longer vector is possible in the same general direction. (Source: docs/fs/Nomenclature.md;
docs/fs/nonimal-vector-names.md)

A friendly local name might expand to a vector. For example, the notes show a
name like `my-morning-speech` associated with a longer reference such as
`audio.eric.wedding:main-morning-speech`. This is a way to make the reference
comfortable for people without making the human-friendly label the physical
particle address. (Source: docs/fs/nonimal-vector-names.md)

There is a lot of design potential here, especially for discovery and
classification. There is also a lot to specify. The notes do not yet define
separator escaping, namespace ownership, collision handling, vector length,
or whether the parts of a vector have fixed meanings. For now, a nominal vector
should be read as a naming proposal rather than a finished address grammar.
(Source: ai-docs-2/fs/overview.md; docs/fs/Nomenclature.md;
docs/fs/nonimal-vector-names.md)

## What Happens When We Save Text?

Let us make this concrete. Suppose a user edits a text item containing:

```text
first line
second line
```

In a conventional application, "save" often feels like one operation: write the
new bytes to the file and close it. In VOL FS, the notes suggest a sequence in
which the logical result is assembled from content units and references. The
exact commands are not defined, so this is a conceptual walkthrough rather
than an API contract. (Source: docs/fs/readme.md;
docs/fs/representation.md)

### 1. Establish Access

The caller first needs a session and an allowed space. The access notes describe
a user authenticating a header or initial key, receiving a reserved address,
and using the returned key for later interaction with the allowed content graph.
Space discovery also considers the session, permissions, membrane, and available
services. (Source: docs/fs/shared mem view permissioning.md;
docs/fs/Space and Space Discovery.md)

In practical terms, the filesystem needs to know two things before it can save:
who is asking, and which storage locations that caller is allowed to use. The
notes identify those concerns, but they do not yet provide a complete capability
schema, credential format, or permission inheritance model. (Source: docs/core/structure.md;
docs/fs/shared mem view permissioning.md)

### 2. Find or Create the Logical Reference

For an existing text item, the caller resolves its logical name and opens it.
The open-table notes describe a graph-header area that keeps active references,
open handles, counters, and readers. For a new item, the representation notes
show an entry point where content can be agglomerated against a reference.
(Source: docs/fs/open table.md; docs/fs/representation.md)

The important point is that opening the logical item does not necessarily mean
opening one host file. It means establishing the active context from which the
filesystem can read or update the item's metadata and content references.
Whether the first persistent object for a new item is a phenocryst, aggregate,
grain, or colloid is still unresolved. (Source: ai-docs-2/fs/overview.md;
docs/fs/readme.md; docs/fs/representation.md)

### 3. Turn the Text into Particles

The text is bytes. The filesystem divides those bytes into particles according
to the selected allocation and storage constraints. If one particle reaches its
available width, the content continues into another particle. The particle
boundaries do not have to be visible to the person reading the text.
(Source: docs/fs/memory allocation table.md; docs/fs/File System.md)

For a small example, the result might be conceptually represented like this:

```text
logical text:  first line\nsecond line\n
particles:     [P1, P2, ...]
P1 content:    first line\n
P2 content:    second line\n
```

`P1` and `P2` are explanatory labels, not a prescribed identifier format. The
source notes do not say where particle boundaries must fall, whether chunks
should be content-addressed, or whether a particle may be rewritten in place.
(Source: docs/fs/memory allocation table.md; docs/fs/Nomenclature.md)

### 4. Store or Stage the Particles

Each particle is sent to a selected space. A local space might use the host
filesystem; another space might use memory or a remote object service. The
notes describe a particle address being returned after the content is
persistently confirmed, while also allowing fluid, volatile content during
runtime. (Source: docs/fs/stock-coms.md; docs/fs/File System.md;
docs/fs/Nomenclature.md)

This creates a question that any real implementation must answer: when is the
new text visible? It could be after every particle is persistent, after the
reference structure is committed, or according to some other rule. The notes
do not choose among these possibilities. They mention an open hash and a
hash written to metadata on close, but not atomic publication semantics.
(Source: docs/fs/readme.md; docs/fs/File System.md)

### 5. Bind the Particles in Order

The aggregate or grain records which particle references make up the text and
in what order. The chunks can remain in their selected spaces; the logical
relationship is maintained by the reference structure. This is how the system
can present one readable text stream even when the content is physically
separated. (Source: docs/fs/File System.md; docs/fs/grains.md)

The distinction between content and arrangement is the heart of the model. A
particle stores a piece of content. The grain or aggregate explains how that
piece participates in the larger readable item. The phenocryst gives the caller
an entry point into that organization. (Source: docs/fs/File System.md;
docs/fs/representation.md)

### 6. Update the Header and Hash

The notes describe a file-like structure maintaining a hash as writes occur,
with an open hash being written to metadata when the file is closed. The header
or phenocryst is the natural location named for persistent information such as
the local reference and current hash. (Source: docs/fs/readme.md;
docs/fs/File System.md; docs/fs/representation.md)

That hash could eventually help the system recognize a version, verify content,
or identify a completed state. Those uses are not yet specified. The algorithm,
canonical input, treatment of metadata, and behavior when verification fails all
remain open. (Source: ai-docs-2/fs/overview.md;
docs/fs/readme.md)

### 7. Close or Finalize

The existing notes use `close` as the point where the open hash is written to
file metadata. It is therefore reasonable to discuss close as a finalization
step in the current model. It is not yet safe to equate close with a complete
transaction commit, because the notes do not define abort behavior, visibility
rules, or recovery after a partial write. (Source: docs/fs/readme.md;
docs/core/structure.md)

A subsequent read would resolve the same logical reference, follow the ordered
particle references, and yield the text as a stream. That is the user-facing
promise of the model even while the storage and transaction machinery is still
being designed. (Source: docs/fs/File System.md; docs/fs/grain-iterator.md)

## Editing Without Rewriting Everything

The notes introduce **synthetic markers** as a way to represent an insertion or
replacement at an iteration point. Imagine a large remote text dataset where a
new passage must be inserted near the beginning. A conventional approach may
require moving a large amount of later data. The marker idea is to retain the
existing content and record where another particle should enter the logical
sequence. (Source: docs/fs/synthetic-markers.md)

The same notes connect markers with fragmented particle stepping, multiple
pointers, encrypted blocks, and transient pointer replacement. This suggests a
filesystem interested in changing the logical presentation of content without
always rewriting every underlying byte. It does not yet tell us whether a marker
belongs in the grain, aggregate, particle, or phenocryst, or how markers affect
hashes and history. (Source: docs/fs/synthetic-markers.md)

That distinction is worth keeping visible: a marker is currently a promising
editing idea, not a settled record type.

## Why Build It This Way?

The proposal is motivated by several connected ideas.

First, a logical item can span multiple spaces. A local cache, host storage,
network service, or object store can participate in one content organization.
The caller can still ask for the logical item rather than manually assembling
its pieces. (Source: docs/fs/Space and Space Discovery.md;
docs/fs/stock-coms.md)

Second, the reader can consume content progressively. The source notes describe
particles being resolved and yielded in order, so a large aggregate need not be
presented as one monolithic in-memory value. The exact buffering behavior is
still open, but the intended interaction is stream-oriented. (Source: docs/fs/File System.md;
docs/fs/grain-iterator.md; docs/fs/stock-coms.md)

Third, arrangement can change without necessarily moving every particle. The
aggregate's references can describe a logical sequence independently from the
physical location of the chunks. Synthetic markers extend this idea to
insertion and replacement scenarios. (Source: docs/fs/readme.md;
docs/fs/synthetic-markers.md)

Fourth, metadata can be managed separately from raw content. Identity,
permissions, location, dates, and hash information are described as header
concerns rather than properties that must be embedded in each content chunk.
(Source: docs/core/structure.md; docs/fs/File System.md)

These are design motivations, not measured performance claims. The notes do
not yet provide benchmarks, a consistency model, or a comparison workload.

## The Costs Come Along With the Freedom

A system that separates logical organization from physical storage gains
flexibility, but it also creates more relationships to maintain.

A read depends on a correct chain from logical name to header, from header to
aggregate or grain, and from those references to resolvable particles. A missing
header, stale location, unavailable remote service, or permission failure can
interrupt reconstruction. (Source: docs/core/structure.md;
docs/fs/File System.md; docs/fs/Space and Space Discovery.md)

Ordering is also a correctness property. If the particle sequence is wrong, the
system may successfully retrieve every chunk and still return incorrect text.
The notes describe stepping from position 0 through position n, but do not
specify how order is represented, how it is validated, or what happens when the
sequence changes during a read. (Source: docs/fs/grain-iterator.md;
docs/fs/File System.md)

History introduces another layer of responsibility. The broader structure notes
describe automatic history and transaction references, while the filesystem
model describes edits as graph leaves and ordered records. These ideas could
support versioned content, but the version-selection and garbage-collection
rules are not defined. (Source: docs/core/structure.md)

Security cannot be an afterthought in this model. The notes propose encryption,
automatic hashing, header authentication, and keys that provide access to
allowed content. They do not yet specify key scope, rotation, revocation,
permission inheritance, or the canonical data that a hash authenticates.
(Source: docs/fs/readme.md; docs/fs/shared mem view permissioning.md;
docs/core/structure.md)

## Is This a Filesystem or a Graph?

The honest answer is that the proposal deliberately sits near both ideas. It
uses graph-oriented references to organize content, and the wider VOL design
uses graphs for pointers, stepping, and executable source. The filesystem notes
also describe a graph-backed virtual layer that can bridge a host filesystem.
(Source: docs/core/structure.md; docs/fs/File System.md;
docs/core/graph pointer.md)

But those two uses should not be collapsed too quickly. A graph can describe
relationships without making each related item executable. A particle can be
resolved as bytes without becoming a program. The source material leaves this
boundary open, so a reader should treat "graph-oriented storage" as the current
filesystem description and "self-executing graph" as a related VOL research
area, not as an automatic property of every saved text item. (Source: docs/fs/File System.md;
docs/core/graph stepper.md; docs/core/graph functions.md)

## The Vocabulary Is Part of the Design Work

The terminology is imaginative, but terminology is not decoration in a
filesystem. It tells implementers which things can be persisted, which things
are operations, and which things are only ways of looking at data.

At present, several words overlap:

- **File and aggregate:** "file" is the familiar user-facing word, while
  aggregate is the described logical readable unit.
- **Phenocryst and header:** both describe metadata and entry references, but
  their ownership boundary is not fully settled.
- **Grain and pointer:** a grain groups or resolves particle references, while
  other notes use grain as an executable unit.
- **Colloid and fetch result:** colloid is described as a fetch operation and as
  a collection or result of resolved content.
- **Particle, segment, block, and sector:** these may be aliases or different
  logical and physical layers, but the notes do not yet decide which.

These are not merely editorial inconsistencies. They are places where the
future model could accidentally acquire two incompatible meanings. The current
working overview records them as naming collisions for deliberate resolution.
(Source: ai-docs-2/fs/overview.md; docs/fs/File System.md;
docs/fs/concepts.md; docs/fs/representation.md)

## What VOL FS Is, and What It Is Not Yet

At this stage, VOL FS is best understood as a research concept for a virtual,
graph-oriented storage layer. It proposes that a logical item can be addressed
through metadata, composed from ordered content chunks, and resolved across
configurable storage spaces. Its notable interests are streaming, distributed
backing locations, history, hashes, encryption, and edits that can change
references without always rewriting all content. (Source: docs/fs/readme.md;
docs/fs/File System.md; docs/fs/Space and Space Discovery.md;
docs/fs/synthetic-markers.md)

It is not yet a complete filesystem specification. The notes do not provide a
canonical on-disk format, command grammar, particle sizing rule, permission
model, transaction protocol, recovery procedure, or resolver error contract.
Those omissions are not failures to hide; they are the next research questions.
(Source: ai-docs-2/fs/overview.md)

That distinction lets us talk about the idea enthusiastically without
pretending that the difficult engineering has already been solved. The
interesting promise is in the separation between what a reader asks for and
where the bytes happen to be. The engineering challenge is making that
separation understandable, recoverable, secure, and correct.

## Questions for the Next Design Pass

A useful next pass should answer a small set of structural questions before
adding more commands or implementation detail:

1. What is the canonical object hierarchy: phenocryst, aggregate, grain,
   colloid, and particle?
2. Which of those objects are persistent records, and which are runtime views
   or operations?
3. What exactly identifies a particle, and how does that identity relate to a
   human-facing name, nominal vector, version, and physical location?
4. What makes a text save visible, and what does failure leave behind?
5. How is particle order represented and validated during a read?
6. Which permissions apply to metadata, structure, and content, and how are
   they inherited?
7. How do hashes, encryption, history, markers, and garbage collection interact?
8. Where is the boundary between resolving data and executing graph behavior?

The source notes already point toward these questions, but they do not answer
them. A disciplined specification should preserve each question until the
project has explicit evidence or a recorded design decision. (Source: ai-docs-2/fs/overview.md;
docs/fs/readme.md; docs/core/structure.md)

## Closing Perspective

VOL FS asks us to stop treating a file's physical placement as the definition
of the file itself. A person can still open a named text item and read a
continuous stream. Underneath, that stream may be assembled from particles,
organized by grains and aggregates, introduced through a phenocryst, and
resolved across several spaces. (Source: docs/fs/File System.md;
docs/fs/grains.md; docs/fs/Space and Space Discovery.md)

The proposal is compelling because it makes storage relationships visible and
flexible. It is demanding because every relationship now needs a clear identity,
ordering rule, security boundary, and recovery story. That is exactly where the
research should go next: not toward guessing a finished implementation, but
toward defining the smallest set of records and transitions that would let the
idea be tested honestly.
