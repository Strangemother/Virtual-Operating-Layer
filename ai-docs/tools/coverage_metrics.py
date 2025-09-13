#!/usr/bin/env python3
"""Coverage Metrics Tool
Scans ai-docs/ for references to origin docs/ markdown files and produces a markdown report.
Constraints: Non-invasive, read-only. Does not infer semantics beyond string matching.

Method:
1. Enumerate origin markdown files under docs/ (non-recursive PDF exclusion, include subdirs).
2. Build normalized keys (relative path from repo root).
3. Scan ai-docs/ *.md for occurrences of those filenames.
4. Tally counts per origin file (simple substring match of base filename; if ambiguous, note ambiguity).
5. Produce coverage-metrics.md with:
   - Summary counts (total origin, covered, uncovered)
   - Table-style bullet list per origin: count, ambiguous flag
   - Incomplete blocks for limitations.

Limitations:
- Base filename collisions (e.g., duplicate names in different subdirectories) flagged as ambiguous.
- Does not parse markdown links for path accuracy; pure substring occurrence.
"""
from __future__ import annotations
import os
from collections import defaultdict, Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ORIGIN_DIR = REPO_ROOT / 'docs'
DERIV_DIR = REPO_ROOT / 'ai-docs'
REPORT_PATH = DERIV_DIR / 'coverage-metrics.md'

EXCLUDE_EXT = {'.pdf'}
EXCLUDE_DIRS = {'.git', 'branding', 'hardware', 'research', 'interface'}  # interface maybe later

def enumerate_origin_markdown():
    origin_files = []
    for root, dirs, files in os.walk(ORIGIN_DIR):
        # Skip excluded dirs by mutating dirs in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() not in {'.md'}:
                continue
            if p.suffix.lower() in EXCLUDE_EXT:
                continue
            rel = p.relative_to(REPO_ROOT)
            origin_files.append(rel)
    return origin_files

def scan_derivative_for_references(origin_files):
    # Map base name -> list of full origin rel paths
    basename_map = defaultdict(list)
    for rel in origin_files:
        basename_map[rel.name].append(rel)

    counts = {rel: 0 for rel in origin_files}
    ambiguous = set()

    # Pre-classify ambiguous basenames
    for base, rels in basename_map.items():
        if len(rels) > 1:
            for r in rels:
                ambiguous.add(r)

    # Collect derivative markdown files
    deriv_files = []
    for root, _, files in os.walk(DERIV_DIR):
        for f in files:
            if f.endswith('.md'):
                deriv_files.append(Path(root) / f)

    # Simple substring scan
    for dfile in deriv_files:
        try:
            text = dfile.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        for base, rels in basename_map.items():
            if base in text:
                for rel in rels:
                    counts[rel] += 1

    return counts, ambiguous

def generate_report(counts, ambiguous):
    total = len(counts)
    covered = sum(1 for c in counts.values() if c > 0)
    uncovered = total - covered

    lines = []
    lines.append("Status: Draft")
    lines.append("Last-Touched: 2025-09-13")
    lines.append("# Coverage Metrics Report")
    lines.append("")
    lines.append("Purpose: Quantify reference coverage of origin markdown sources within ai-docs derivative set. Purely mechanical string scan; no semantic validation.")
    lines.append("")
    lines.append(f"Summary: Total origin files: {total}; Covered (≥1 ref): {covered}; Uncovered: {uncovered}")
    lines.append("")
    lines.append("## Per-File Reference Counts")
    lines.append("Format: count – relative/path (AMBIGUOUS if base name collision)")
    lines.append("")

    # Sort by uncovered first then descending count
    sorted_items = sorted(counts.items(), key=lambda kv: (kv[1] == 0, -kv[1], str(kv[0])))
    for rel, cnt in sorted_items:
        marker = " AMBIGUOUS" if rel in ambiguous else ""
        lines.append(f"- {cnt:3d} – {rel}{marker}")

    lines.append("")
    lines.append("## Uncovered Files")
    for rel, cnt in counts.items():
        if cnt == 0:
            lines.append(f"- {rel}")

    lines.append("")
    lines.append("Incomplete: Methodological limitations")
    lines.append("Needed:")
    lines.append("- Path-aware link parsing (current method may overcount plain-text mentions)")
    lines.append("- Distinguish glossary-only citations vs deep extraction")
    lines.append("- Weight references by document type (overview vs section)")
    lines.append("Candidate Sources: coverage-metrics.md (this), origin-derivative-coverage-map.md, governance-index.md")

    lines.append("")
    lines.append("Verbatim scope: File system listings only; derivative scans limited to substring presence.")

    return "\n".join(lines) + "\n"


def main():
    origin = enumerate_origin_markdown()
    counts, ambiguous = scan_derivative_for_references(origin)
    report = generate_report(counts, ambiguous)
    REPORT_PATH.write_text(report, encoding='utf-8')
    print(f"Wrote {REPORT_PATH}")

if __name__ == '__main__':
    main()
