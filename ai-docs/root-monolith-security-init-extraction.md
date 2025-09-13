# Root Monolith – Security Initialization (Extraction)
Status: Draft
Last-Touched: 2025-09-13
Depends-On: docs/root-monolith/security research.md
Verbatim scope: docs/root-monolith/security research.md

## Purpose
Capture explicit security-related primitives and initialization references.

## Sourced Statements
1. Initial random graph bits used to encrypt within. (Source: docs/root-monolith/security research.md)
2. A range of initial keys after #0 act as security bits; chain sequence uncovered through keypair decryption yields decrypt signature from graph keys. (Source: docs/root-monolith/security research.md)
3. Chain example: 5 graph keys and 10 steps; each node is a mathematical calculation. (Source: docs/root-monolith/security research.md)
4. Process returns the system key decrypted based on secure two parts. (Source: docs/root-monolith/security research.md)
5. CRC start key uses the boot file; one-way BIOS key bits mentioned. (Source: docs/root-monolith/security research.md)
6. `root.lock()` finalizes BIOS state and tests record; refuses to start if verification fails. (Source: docs/root-monolith/security research.md)
7. Kernel input stream may be verified via string testing; CRC of file denotes a key graph path. (Source: docs/root-monolith/security research.md)
8. CRC may act as boot key sequence bridging execution string, starting with CRC identifier. (Source: docs/root-monolith/security research.md)
9. Randomization of CRC via graph pre-bits suggested to prevent tampering. (Source: docs/root-monolith/security research.md)

## Observed Concept Elements (Names Only)
- Initial graph bits
- Security bit chain (graph keys + steps)
- Mathematical node calculations
- System key (decryption output)
- CRC start key / boot key sequence
- One-way BIOS key bits
- root.lock() verification
- Graph pre-bits randomization

## Cross-References
- Glossary stubs: Initial Graph Bits, CRC Start Key, root.lock() (See: sections/glossary.md)
- Related gap: Security Initialization Chain (root-monolith-triage.md)

## Incomplete Blocks
```
Incomplete: Security Bit Chain Formalization
Needed: Exact relationship between number of graph keys and steps; validation algorithm; failure handling.
Candidate Sources: docs/root-monolith/security research.md
```
```
Incomplete: CRC Randomization Mechanism
Needed: Randomization method; entropy source; prevention of replay/tampering.
Candidate Sources: docs/root-monolith/security research.md
```
```
Incomplete: root.lock() Operation Contract
Needed: Input parameters; success/failure return model; persistence of verification data.
Candidate Sources: docs/root-monolith/security research.md
```

## Notes
- No cryptographic primitives specified; none inferred.

Backlink: Referenced by root-monolith-triage.md and root-monolith-index.md
