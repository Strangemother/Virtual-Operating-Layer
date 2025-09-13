#!/usr/bin/env python3
"""Inbound Link Checker

Scans ai-docs/ for markdown files and reports those lacking an inbound reference
(from any other file) by filename. Exclusions: tools/ directory, this script,
policy / governance docs (heuristic: filenames starting with 'policy-' or listed
in EXCLUDE_EXACT).

No new semantics are created; this is a utility to support promotion criterion
requiring at least one inbound link. (Source: policy-promotion.md, inbound-link-verification.md)
"""
from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT  # ai-docs/

EXCLUDE_DIRS = {"tools"}
EXCLUDE_EXACT = {
    "CHANGELOG-docs.md",
    "governance-index.md",
    "gap-priority-matrix.md",
    "policy-promotion.md",
    "policy-alias-format.md",
    "collision-resolution-procedure.md",
    "inbound-link-verification.md",
    "backlink-plan.md",
    "term-collisions.md",
}

MD_PATTERN = re.compile(r"^[A-Za-z0-9_.\-]+\.md$")


def collect_markdown() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(DOC_ROOT):
        rel_dir = Path(dirpath).relative_to(DOC_ROOT)
        # Skip excluded dirs
        if any(part in EXCLUDE_DIRS for part in rel_dir.parts):
            continue
        for fn in filenames:
            if not MD_PATTERN.match(fn):
                continue
            if fn in EXCLUDE_EXACT:
                continue
            files.append(Path(dirpath) / fn)
    return files


def index_contents(files: list[Path]):
    contents = {}
    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:  # pragma: no cover
            text = f"<error reading: {e}>"
        contents[p] = text
    return contents


def compute_inbound(files: list[Path], contents):
    # Map file -> inbound count
    name_to_path = {p.name: p for p in files}
    inbound = {p: 0 for p in files}
    for src, text in contents.items():
        for target_name in name_to_path:
            if src.name == target_name:
                continue
            # simple substring match; could refine to markdown link pattern
            if target_name in text:
                inbound[name_to_path[target_name]] += 1
    return inbound


def main():
    files = collect_markdown()
    contents = index_contents(files)
    inbound = compute_inbound(files, contents)
    lacking = [p for p, count in inbound.items() if count == 0]

    print("Inbound Link Report")
    print("Root:", DOC_ROOT)
    print()
    print("Total considered files:", len(files))
    print("Files lacking inbound links (excluding self):", len(lacking))
    print()
    for p in sorted(lacking):
        print("-", p.relative_to(DOC_ROOT))

    print()
    print("Note: Exclusions and heuristic defined in script header.")
    print("Source references: policy-promotion.md, inbound-link-verification.md")


if __name__ == "__main__":  # pragma: no cover
    main()
