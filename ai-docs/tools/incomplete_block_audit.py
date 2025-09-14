#!/usr/bin/env python3
"""Incomplete Block Audit

Scans ai-docs/ for lines beginning with 'Incomplete:' (or 'Pending:' for roadmap style) and
compares findings against the tracked sets in:
 - active-gaps-index.md
 - exhausted-gaps-index.md

Outputs a markdown report to stdout. Intended to be idempotent and free of external deps.

Non-goal: Interpreting or modifying source files.
"""
from __future__ import annotations
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]  # /workspaces/Virtual-Operating-Layer
AIDOCS = ROOT / "ai-docs"

INCOMPLETE_PATTERN = re.compile(r"^(Incomplete|Pending):\s*(.+)")

INDEX_FILES = {
    "active": AIDOCS / "active-gaps-index.md",
    "exhausted": AIDOCS / "exhausted-gaps-index.md",
}

def collect_incomplete_blocks():
    results = []
    for path in AIDOCS.rglob("*.md"):
        # Skip archived seed duplicates if any future naming emerges; keep all currently
        rel = path.relative_to(AIDOCS)
        with path.open("r", encoding="utf-8", errors="ignore") as fh:
            for lineno, line in enumerate(fh, 1):
                m = INCOMPLETE_PATTERN.match(line.strip())
                if m:
                    kind, title = m.groups()
                    results.append({
                        "file": str(rel),
                        "line": lineno,
                        "kind": kind,
                        "title": title.strip(),
                    })
    return results

def parse_index_titles(path: Path):
    titles = set()
    if not path.exists():
        return titles
    with path.open("r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            # Exhausted list lines typically have '- <Title>' or headings '### Title'
            line_strip = line.strip()
            if line_strip.startswith("- ") and "Await new origin material" in line_strip:
                t = line_strip[2:].split("(Passes:")[0].strip()
                titles.add(t)
            elif line_strip.startswith("### "):
                # headings might represent gap groups; ignore here
                continue
            elif line_strip.startswith("- ") and line_strip.lower().startswith("- field enumeration"):
                # already captured by pattern above; fallthrough
                pass
    return titles

def main():
    discovered = collect_incomplete_blocks()
    active_body = INDEX_FILES["active"].read_text(encoding="utf-8") if INDEX_FILES["active"].exists() else ""
    exhausted_body = INDEX_FILES["exhausted"].read_text(encoding="utf-8") if INDEX_FILES["exhausted"].exists() else ""

    # Extract titles from index bodies by simple heading match after '###'
    def extract_index_titles(body: str):
        titles = set()
        for line in body.splitlines():
            if line.startswith("### "):
                t = line[4:].strip()
                titles.add(t)
        return titles

    active_titles = extract_index_titles(active_body)
    # Exhausted gaps stored as list lines with hyphen start after group headings; capture simpler token before '– Await'
    exhausted_titles = set()
    for line in exhausted_body.splitlines():
        ls = line.strip()
        if ls.startswith("- ") and "Await new origin material" in ls:
            exhausted_titles.add(ls[2:].split("– Await")[0].strip())

    # Build canonical discovered set
    discovered_titles = {(d["title"], d["file"]) for d in discovered}

    # Titles appearing in discovered but not in either index (for tracking by name only)
    tracked_name_set = active_titles | exhausted_titles
    untracked = [d for d in discovered if d["title"] not in tracked_name_set]

    # Report
    now = datetime.utcnow().isoformat(timespec='seconds') + 'Z'
    print(f"# Incomplete Block Audit Report\nGenerated: {now}\n")
    print("## Summary")
    print(f"Discovered blocks: {len(discovered)}")
    print(f"Active index titles: {len(active_titles)}  | Exhausted titles: {len(exhausted_titles)}")
    print(f"Untracked (by title): {len(untracked)}\n")

    if untracked:
        print("## Untracked Blocks")
        for item in untracked:
            print(f"- {item['title']} (File: {item['file']} line {item['line']})")
        print()
    else:
        print("## Untracked Blocks\nNone\n")

    print("## All Discovered Blocks")
    for d in sorted(discovered, key=lambda x: (x['file'], x['line'])):
        status = "EXHAUSTED" if d['title'] in exhausted_titles else ("ACTIVE" if d['title'] in active_titles else "UNTRACKED")
        print(f"- {d['title']} [{d['kind']}] — {status} (Source: {d['file']}:{d['line']})")

if __name__ == "__main__":
    main()
