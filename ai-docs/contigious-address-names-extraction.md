# Contiguous Address Names (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Source Files: docs/core/Contigious address names.md

Purpose: Extract explicit statements regarding graph walking, address allocation, and proposed addressing algorithms. No new semantics introduced.

## Sourced Statements
1. Pointer attains an address and reads memory at that location. (Source: docs/core/Contigious address names.md)
2. Address bound to a small chunk of accessible memory allocated by primary service. (Source: docs/core/Contigious address names.md)
3. Stepper machine accesses an address 'app' to yield list of contiguous addresses for suite of executions. (Source: docs/core/Contigious address names.md)
4. Large memory availability suggests directing subset of work toward mapped allocation. (Source: docs/core/Contigious address names.md)
5. Initial step: virtual addressing providing persistent base for graphs/long-term data plus transient memory (RAM). (Source: docs/core/Contigious address names.md)
6. Primary machine allocated subset of greater memory (example: 50mg of 100mg). (Source: docs/core/Contigious address names.md)
7. Exposing linear address list to digesting service deemed imprudent (risks overflow when walking 1D). (Source: docs/core/Contigious address names.md)
8. Re-addressing memory would lead to inner graph faults. (Source: docs/core/Contigious address names.md)
9. Proposed solution: 'perfect hashmap' mapping linear memory through named reference map OR closed loop algorithm to lock address into bound space. (Source: docs/core/Contigious address names.md)
10. Stepper can deduce range of steps without reading memory (pure computation) enabling page/subset allocation. (Source: docs/core/Contigious address names.md)
11. Example pseudocode shows StepperMachine with key_function=minkowski_plane and iterative next vector generation. (Source: docs/core/Contigious address names.md)
12. Candidate methods listed: Minkowski plane projects; Euclid line on 2D projection; Hemisphere or subflower vector plots; 130x130 Knights Tour; Self-avoiding walk. (Source: docs/core/Contigious address names.md)

## Observed Concept Elements (Names Only)
- Virtual addressing
- Persistent base vs transient memory
- Perfect hashmap (naming unformalized)
- Closed loop algorithm
- Pages / subsets of graphs
- Minkowski plane, Euclid line, hemisphere/subflower plots
- Knights Tour, self-avoiding walk

## Incomplete Blocks
Incomplete: Address Space Normalization
Needed:
- Formal definition of virtual address format
- Mapping rules from named reference map to physical/persistent storage
- Boundaries for closed loop algorithm (collision avoidance criteria)
Candidate Sources: docs/core/Contigious address names.md, graph-overview.md, memory-identity-overview.md

Incomplete: Paging / Subset Allocation Semantics
Needed:
- Criteria to partition graph into pages
- Consistency guarantees when pages mutate
- Interaction with stepper prediction mechanism
Candidate Sources: docs/core/Contigious address names.md, docs/core/graph stepper.md

Incomplete: Algorithm Selection Contract
Needed:
- Selection criteria among listed methods (Minkowski, Euclid, etc.)
- Performance or determinism expectations
- Reproducibility requirement for vector generation
Candidate Sources: docs/core/Contigious address names.md

Incomplete: Hashmap vs Closed Loop Tradeoff
Needed:
- Failure modes (overflow, collision, fragmentation)
- Recovery strategy on address fault
- Memory overhead description
Candidate Sources: docs/core/Contigious address names.md

Incomplete: Stepper Predictive Range Computation
Needed:
- Formal inputs required (current vector, algorithm key function)
- Maximum lookahead window definition
- Handling of dynamic graph changes during precomputed walk
Candidate Sources: docs/core/Contigious address names.md, docs/core/graph stepper.md

Verbatim scope: docs/core/Contigious address names.md only.
