# Uncovered Origin Files Triage
Status: Draft
Last-Touched: 2025-09-13
Depends-On: coverage-metrics.md, origin-derivative-coverage-map.md

Purpose: Classify uncovered origin markdown files into categories: Candidate Extraction, Historical / Archival, Needs Review. No speculative interpretation of content; classification provisional pending file content inspection.

Source Basis: coverage-metrics.md Uncovered Files list (Source: coverage-metrics.md)

## Categories
- Candidate Extraction: Likely to contain normative or structural concepts required for core coherence.
- Historical / Archival: Narrative, deprecated, or exploratory content not immediately needed for working-spec promotion.
- Needs Review: Unopened—content not yet assessed; classification deferred.

## Initial Classification

Candidate Extraction
- docs/core/Contigious address names.md (Now extracted) (Source: contigious-address-names-extraction.md)
- docs/memory/Single Identity.md (Now extracted) (Source: single-identity-extraction.md)
- docs/garbage collector.md (Now extracted) (Source: garbage-collector-extraction.md)

Historical / Archival (Provisional)
- docs/(easter)-bunny.md
- docs/discussion/gnu.md
- docs/discussion/new paradigm.md

Needs Review (Unopened)
- docs/memory/Single Identity.md (removed from this list after extraction)
- docs/root-monolith/phase-0.md
- docs/root-monolith/applying-vol-runtime-libs.md
- docs/root-monolith/security research.md
- docs/root-monolith/phases.md
- docs/root-monolith/readme.md
- docs/root-monolith/byte-function-load.md
- docs/root-monolith/stack-processing.md
- docs/core/Contigious address names.md (moved to Candidate Extraction post extraction) 
- docs/garbage collector.md (moved to Candidate Extraction post extraction)
- docs/core/Contigious address names.md (duplicate marker) 

Incomplete: Root Monolith Content Assessment
Needed:
- Determine if root-monolith directory describes legacy bootstrap path or active design elements
- Identify any unique terminology needing glossary inclusion
Candidate Sources: root-monolith/*

## Processed Root-Monolith Files (Extraction Completed)
- docs/root-monolith/graph-walk.md (Extracted: root-monolith-graph-walk-extraction.md)
- docs/root-monolith/step addresses and layers.md (Extracted: root-monolith-step-addresses-layers-extraction.md)
- docs/root-monolith/memory-module.md (Extracted: root-monolith-memory-module-extraction.md)
- docs/root-monolith/Frame Switching.md (Extracted: root-monolith-frame-switching-extraction.md)
- docs/root-monolith/commands.md (Extracted: root-monolith-commands-extraction.md)

## Incomplete Blocks (New Gaps From Root-Monolith Extraction)
```
Incomplete: Layered addressing contract
Needed: Formal relationship among index / expanded / family / extended family / related family / dictionary domains; collision handling; escalation path.
Candidate Sources: docs/root-monolith/step addresses and layers.md, docs/core/structure.md, TODO: discover
```
```
Incomplete: Acquisition-triggered frame orientation
Needed: Whether frame orientation is prerequisite or side-effect of acquisition; concurrency semantics when multiple acquisition units operate.
Candidate Sources: docs/root-monolith/memory-module.md, docs/core/frame-context.md, TODO: discover
```
```
Incomplete: Frame switching authorization model
Needed: Who/what initiates switch; validation gate; rejection and rollback procedures.
Candidate Sources: docs/root-monolith/Frame Switching.md, docs/core/system core.md, TODO: discover
```
```
Incomplete: Command invocation lifecycle coupling
Needed: Ordering constraints between command execution and graph walk initialization; timeout or deadlock safeguards.
Candidate Sources: docs/root-monolith/commands.md, docs/root-monolith/graph-walk.md, TODO: discover
```
```
Incomplete: Sequence vs series graph traversal distinction
Needed: Distinct traversal algorithms or use-cases; temporal vs structural differentiation.
Candidate Sources: docs/root-monolith/step addresses and layers.md, docs/root-monolith/graph-walk.md, TODO: discover
```

Incomplete: Discussion File Relevance
Needed:
- Confirm if discussion/ files hold decisions that influenced promoted specs
- Decide archival tag format
Candidate Sources: docs/discussion/gnu.md, docs/discussion/new paradigm.md

Incomplete: Archival Tagging Policy
Needed:
- Define status marker or front-matter field for archival classification
- Retention / relocation procedure
Candidate Sources: governance-index.md, policy-promotion.md, policy-archival.md (now provides criteria)

Verbatim scope: coverage-metrics.md only (no internal reading of root-monolith or discussion files yet).
