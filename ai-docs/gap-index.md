Status: Draft
Last-Touched: 2025-09-13
# Gap Index (Aggregated Incomplete Blocks)

Purpose: Central list of all current Incomplete blocks across extraction stubs for prioritization. No new interpretation added.

## Capability Advertisement
Reference: capability-advertisement.md
- Capability Field List
- Translator Selection Rules
- Session Merge Semantics
- Capability Revocation / Update
- Role Derivation Algorithm
- Registry Involvement (If Any)

## Mesh Role Derivation
Reference: mesh-role-derivation.md
- Role Enumeration
- Derivation Inputs
- Subgraph Injection Rules
- Topology Position Semantics
- Membrane Influence
- Leaf Task Specialization

## Registry Capability Broker
Reference: registry-capability-broker.md
- Capability Mediation
- Persistence Model
- Event / Command Relationship
- Security / Isolation

## Onboarding Sequence
Reference: onboarding-sequence.md
- Formal Ordering Guarantees
- Handshake Protocol
- Role Assignment Criteria
- Registry Integration
- Failure / Retry Semantics
- Security / Authorization

## Pointer 0 / Boot
Reference: pointer-0-payload.md, boot-sequence-diagram.md
- Pointer 0 payload schema
- Ordering of zero-suite services
- Error handling semantics

## SEM Tape Extraction
Reference: sem-tape-extraction.md
- Detailed SEM TAPE field list
- mcom memory layout specifics

## Interface Event Taxonomy
Reference: interface-event-taxonomy.md
- Canonical event type list
- Event normalization rules

## Filesystem Layering
Reference: filesystem-layering-outline.md
- Layer boundaries formal definition
- Inter-layer permission model
- Resolution conflict rules

## Identity & Memory Unification
Reference: identity-memory-unification.md
- Slot vs grain mapping rules
- Identity lifecycle states

## Layered Addressing Domains
Reference: root-monolith-step-addresses-layers-extraction.md
- Domain relationship hierarchy (index/expanded/family/extended family/related family/dictionary)
- Collision / precedence rules
- Transformation / escalation path

## Acquisition Pipeline
Reference: root-monolith-memory-module-extraction.md
- Acquisition unit input/output contract
- Frame orientation ordering
- Block processing semantics
- Non-acquisition unit responsibilities

## Frame Switching
Reference: root-monolith-frame-switching-extraction.md
- Frame taxonomy enumeration
- Quantum→Command transition preconditions
- Timeline linearization criteria
- Persistence vs reinit state set
- Authorization / signaling model

## Command Lifecycle Coupling
Reference: root-monolith-commands-extraction.md
- Command schema (fields)
- Lifecycle phase enumeration
- Graph traversal selection rules
- Frame 0 privilege scope
- Timeout / rollback semantics

## Sequence vs Series Graph Distinction
Reference: root-monolith-step-addresses-layers-extraction.md; root-monolith-graph-walk-extraction.md
- Differentiation criteria (temporal vs structural)
- Traversal algorithm divergence
- Lifecycle / creation triggers

Verbatim scope: Aggregated from existing ai-docs/sections/* extraction files only.

## Consolidation References (No New Gaps)
Reference: frame-model-skeleton.md, root-monolith-index.md, addressing-domain-enumeration.md
- These consolidation docs aggregate existing sourced statements; all gaps remain listed under their originating sections above.

## Input Stream Stepping
Reference: root-monolith-monolith-readme-extraction.md
- Termination key definition
- Multi-line or composite command framing
- Partial command recovery rules

## Walking Register Structure
Reference: root-monolith-monolith-readme-extraction.md
- Field inventory per input-session key
- Persistence / lifetime rules
- Capacity / overflow behavior

## Cold-Store Entropy Policy
Reference: root-monolith-monolith-readme-extraction.md
- Age/access threshold metrics
- Rehydration triggers
- Collision handling upon reintroduction

## Frame Switcher Semantics
Reference: root-monolith-comprehensive-extraction.md
- Transition triggers
- Isolation guarantees
- Rollback / diff strategy

## Code Allocator Mechanism
Reference: root-monolith-comprehensive-extraction.md; root-monolith-byte-function-load-extraction.md
- Allocation unit size
- Free list or mapping strategy
- Integration with graph memory

## Variation Tree Definition
Reference: root-monolith-comprehensive-extraction.md
- Node types
- Relationship to generative grammar
- Execution influence

## Library Auto-Exposure Rules
Reference: root-monolith-comprehensive-extraction.md; root-monolith-libs-extraction.md
- Inclusion criteria
- Override precedence
- Sandbox limitations

## Byte Function Reconstruction
Reference: root-monolith-byte-function-load-extraction.md
- Byte grouping/boundary detection
- Entry point derivation
- Error recovery on mismatch

## Checksum Referencing
Reference: root-monolith-byte-function-load-extraction.md; root-monolith-security-init-extraction.md
- Algorithm identity
- Verification stage (pre/post execution)
- Failure handling semantics

## Execution Safety (Byte-Loaded Functions)
Reference: root-monolith-byte-function-load-extraction.md; root-monolith-comprehensive-extraction.md
- Sandbox / isolation requirements
- Permission gating
- Interaction with code allocator

## Security Initialization Chain Ordering
Reference: root-monolith-security-init-extraction.md; root-monolith-phase-0-extraction.md; root-monolith-phase-sequence-extraction.md
- Initial graph bits → key chain derivation ordering
- CRC randomization placement
- root.lock() validation sequence