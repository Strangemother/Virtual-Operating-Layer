#!/usr/bin/env python3
"""Term occurrence counter.
Scans specified directories for markdown files and counts whole-word occurrences of terms.
No inference; purely mechanical tally to aid collision-resolution-procedure.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path
from collections import Counter, defaultdict

MD_EXT = {".md"}

WORD_BOUNDARY = r"(?<![A-Za-z0-9_]){term}(?![A-Za-z0-9_])"

def collect_files(paths):
    for base in paths:
        p = Path(base)
        if not p.exists():
            continue
        if p.is_file() and p.suffix in MD_EXT:
            yield p
        else:
            for f in p.rglob("*.md"):
                yield f

def count_terms(files, terms):
    compiled = {t: re.compile(WORD_BOUNDARY.format(term=re.escape(t))) for t in terms}
    per_file = defaultdict(lambda: Counter())
    global_counter = Counter()
    for file in files:
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for term, pattern in compiled.items():
            matches = pattern.findall(text)
            if matches:
                per_file[str(file)][term] += len(matches)
                global_counter[term] += len(matches)
    return global_counter, per_file


def main():
    ap = argparse.ArgumentParser(description="Count occurrences of glossary/collision terms.")
    ap.add_argument("terms", nargs="+", help="Terms to count (exact, case sensitive). Use quotes for spaces.")
    ap.add_argument("--paths", nargs="+", default=["docs", "ai-docs"], help="Directories to scan.")
    ap.add_argument("--files", nargs="*", default=[], help="Optional explicit file list (overrides paths).")
    ap.add_argument("--per-file", action="store_true", help="Show per-file breakdown.")
    args = ap.parse_args()

    files = list({Path(f) for f in args.files if f}) if args.files else list(collect_files(args.paths))
    global_counts, per_file = count_terms(files, args.terms)

    print("# Term Occurrence Summary")
    for term in args.terms:
        print(f"{term}: {global_counts.get(term, 0)}")

    if args.per_file:
        print("\n# Per File Breakdown")
        for file, ctr in sorted(per_file.items()):
            line = ", ".join(f"{t}={ctr[t]}" for t in args.terms if ctr[t])
            if line:
                print(f"{file}: {line}")

if __name__ == "__main__":  # pragma: no cover
    main()
