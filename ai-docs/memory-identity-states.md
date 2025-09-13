Status: Draft
Last-Touched: 2025-09-13
# Memory Identity States (Extraction)

Purpose: Capture conceptual framing of replacing linear data with neural network (NN) tensor artifacts; enumerate gaps for identity/persistence taxonomy.

## Sourced Statements
1. Proposal: A "file" could be a neural net of weights and biases trained to recite original linear data. (Source: memory-as-weights-and-biases.md)
2. Current paradigm: Stored data is procedural linear bits/bytes consumed by LOAD EXECUTE machines. (Source: memory-as-weights-and-biases.md)
3. Data records considered finite with defined beginning and end. (Source: memory-as-weights-and-biases.md)
4. Hypothesis: Train NN on dataset to produce identical linear data upon load/unpack. (Source: memory-as-weights-and-biases.md)
5. Result object is a tensor transported and read by receiver which performs an unpack. (Source: memory-as-weights-and-biases.md)
6. Internal compression may reduce hidden node count via data structure properties. (Source: memory-as-weights-and-biases.md)
7. Example aspiration: Minimal input nodes, single output node emitting bytes sequentially. (Source: memory-as-weights-and-biases.md)
8. Observed experimental note: Unknown internal node reused multiple times per iteration (indicative of internal recurrence). (Source: memory-as-weights-and-biases.md)
9. Security concerns acknowledged; no mitigation described. (Source: memory-as-weights-and-biases.md)

## Implied Artifact Types (Names Only)
- Tensor-as-File (NN representation) (Source: memory-as-weights-and-biases.md)
- Linear File (traditional) (Source: memory-as-weights-and-biases.md)
- Unpack Stage (reconstruction process) (Source: memory-as-weights-and-biases.md)

## Not Defined
- Identity schema for tensor-based file (hashing, version markers)
- Persistence lifecycle states (trained, in-training, deprecated, archived)
- Trust/verification mechanism before unpack
- Performance/cost metrics for unpack vs direct read

## Incomplete Blocks
Incomplete: Tensor Identity Schema
Needed:
- Fields required to assert integrity (hash of weights, training manifest)
- Mapping to legacy filename / aggregate concept
Candidate Sources: memory-as-weights-and-biases.md, docs/fs/File System.md

Incomplete: Lifecycle State Enumeration
Needed:
- Canonical states (e.g., draft model, active model, retired model)
- Transition triggers
Candidate Sources: memory-as-weights-and-biases.md

Incomplete: Security Validation
Needed:
- Malicious payload detection approach inside tensor
- Sandbox or deterministic execution requirement
Candidate Sources: memory-as-weights-and-biases.md

Incomplete: Unpack Protocol
Needed:
- Ordering guarantees for emitted bytes
- Error handling when reconstruction diverges
Candidate Sources: memory-as-weights-and-biases.md

Incomplete: Compression Claim Clarification
Needed:
- Conditions under which internal compression reduces node count
- Boundaries for acceptable loss (if any)
Candidate Sources: memory-as-weights-and-biases.md

Verbatim scope: memory-as-weights-and-biases.md only.
