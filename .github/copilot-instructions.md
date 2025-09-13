## Virtual Operating Layer – Documentation / Thesis Phase Guidance (AI Agents)

Current phase: Treat all code under `v1/`, `v2/`, `graphics/`, `nector/` as exploratory prototypes however using any markdown or `docs/` within is encouraged. The authoritative product is the conceptual documentation in `docs/`. Your job: curate, normalize, cross‑reference, and elevate the documents toward a coherent specification for a future implementation.

### 0. Non‑Speculation Principles (Must Follow)
- Never invent behaviors, data formats, APIs, or terminology. If a detail is not explicitly present in an existing doc, mark it as incomplete instead of inferring.
- Cite source for every normative claim with a parenthetical `(Source: relative/path.md)`; if multiple, list the most specific file first.
- Use an incompletion block when gaps appear:
	```
	Incomplete: <topic>
	Needed: <explicit missing facts / enumerated items>
	Candidate Sources: <files to review or TODO: discover>
	```
- Do not derive specification rules from experimental code in `v1/`, `v2/`, `graphics/`, `nector/`; code may inform questions, not conclusions.
- Prefer asking the user (or leaving a clearly tagged gap) over silent assumption. Phrase clarifying prompts minimally and reference the doc cluster involved.
- For ambiguous or colliding terms add a glossary entry stub: `Naming Collision: <Term A>/<Term B> – TODO: disambiguate (Source: file1.md, file2.md)`.
- If you summarize, include `Verbatim scope:` listing the files you actually read for that summary to prevent overreach.
- Reject external analogy creep: avoid mapping to existing OS kernels, filesystems, or schedulers unless an internal doc explicitly does so.
- Large-scale readership goal (43k devs): prioritize stable anchors—avoid renaming established files without leaving a relocation stub.

### 1. Documentation Domains (Concept Clusters)
- Core Runtime: `docs/core/` (boot, kernel, os-runtime, structure, system core, terminology, zero-suite) – defines lifecycle, abstractions, naming primitives.
- Graph / Procedure Model: `docs/core/Procedure Graph.md`, `graph *.md`, plus top-level `Procedure Graph.md` – execution semantics & addressing.
- Filesystem & Storage: `docs/fs/` (File System, File Names, FS vol top level naming, grain/grain-iterator, memory allocation table, open table, representation, synthetic-markers) – design a layered spec for logical vs physical layout.
- Memory & Identity: `docs/memory/` + `docs/concepts/memory-as-weights-and-biases.md` – unify terminology around slots, identity, allocation, bias/weight metaphors.
- Mesh / Nodes / Registry: `mesh.md`, `nodes.md`, `registry.md`, `Scaling.md`, `multiprocessing.md` – distributed topology & coordination.
- Interface & Display: `display (container).md`, `inputs.md`, `Facade.md`, branding assets – presentation contract & user/device ingress.
- Boot & Genesis: `boot.md`, `Genesis-Origin.md`, `top level.md`, `the loop.md` – startup narrative & steady-state loop.

### 2. Normalization Tasks (High Value)
1. Create a central Glossary (pull from `terminology.md`, scattered doc-specific definitions) – single source of truth, alphabetical, each term: definition + canonical file link.
2. Introduce Status Tags: At top of each doc add `Status: Draft | Working-Spec | Decision` (do not promote without cross-file consistency check).
3. Add Cross-Refs: When a doc references a concept defined elsewhere, insert inline `(See: core/graph pointer.md)` – prefer relative paths.
4. De-duplicate Graph Content: Merge overlapping "graph key names / node compass / pointer / stepper" into a structured hierarchy outline; leave original files but insert a header note: `Superseded by: graph/OVERVIEW.md`.
5. Filesystem Layering: Synthesize a concise `docs/fs/overview.md` summarizing naming, grain model, resolution, allocation, permissioning (draw from existing discrete files).
6. Boot Sequence Diagram Stub: Draft textual sequence listing (Boot loader → Zero-suite init → Kernel frame-context → Graph registration → FS mount bootstrap → Mesh discovery → Presentation attach). Cite source files per step.

### 3. Style Guide (Apply Incrementally)
- Headings: Use at most 3 levels (`#`, `##`, `###`); avoid deeper nesting—promote structure diagrams instead.
- Naming: Preserve original capitalization from source unless a canonical form is declared in glossary; flag inconsistencies via TODO.
- Directives Block: After main title optionally include: `Status:`, `Owner:`, `Last-Touched: YYYY-MM-DD`, `Depends-On:` (list filenames), `Superseded-By:`.
- Decision Records: For irreversible design choices add a `### Decision` section with: Context → Options → Rationale → Consequences.
- Diagrams: Prefer ASCII first; if external images needed, note `[diagram pending]` placeholder; no binary assets unless essential.

### 4. Cross-Referencing Rules
- Never invent a concept name—search first. If ambiguity: append a clarifier `(working-term)` and tag with `TODO: confirm naming`.
- For overlapping terms (e.g., “graph” vs “procedure graph”) add an alias line in glossary: `Aliases: procedure graph, exec graph`.
- Link priority: (a) Specific file → (b) Cluster overview → (c) Glossary anchor.

### 5. Consistency & Drift Control
- Before editing a doc, scan sibling files in same cluster to avoid silent divergence.
- If merging content, leave a short "Relocated" notice in the source file with a link; do not delete historical prose yet.
- Mark speculative / inspirational prose with an italicized prefix `_Speculative:_` so future implementers can filter signal vs ideation.

### 6. Suggested AI Micro‑Tasks
- Glossary extraction pass (aggregate terms + first definition sentence + source path).
- Graph concept consolidation skeleton (`graph-OVERVIEW.md`).
- FS overview synthesis.
- Boot sequence linear narrative.
- Identity & memory unification note (slots vs grains vs allocation table).
- Mesh roles matrix (nodes.md + registry.md + scaling.md) → concise table (textual, no pipes if avoiding markdown tables; bullet matrix acceptable).

### 7. Quality Bar for a “Working-Spec” Promotion
- All referenced terms appear in glossary.
- No unresolved `TODO` blocks inside normative sections (only in Future Work).
- At least one inbound link from another doc (validate discoverability).
- Status header present with date not older than 60 days (else mark `Stale`).

### 8. Non-Goals (For Now)
- Do not refactor experimental code to match docs—code is not authoritative.
- No performance claims or binary protocol commitments until a draft message schema exists.
- Avoid selecting concrete external dependencies (CEF, PyPy, etc.) in spec language—describe capability, not implementation.

### 9. When Unsure
- Prefer consolidating & annotating over rewriting expressive original narrative.
- Open a lightweight `NOTE:` block rather than pruning ambiguous historical context.
- Escalate naming conflicts by adding a `Naming Collision:` list in glossary draft.

---
Deliver doc changes as focused patches (one thematic improvement set per commit) with a short rationale referencing the originating files.

Never edit the origin `docs/` only perform changes within the `ai-docs/`