#!/usr/bin/env python3
"""
cluster_validation.py

Purpose: Validate completeness and uniqueness mapping of untracked Incomplete block titles into cluster membership.

Inputs (implicit):
 - ai-docs/incomplete-block-audit-report.md (source of authoritative untracked list)
 - ai-docs/gap-cluster-membership.md (cluster enumerations)
 - ai-docs/active-gaps-index.md (Normalization Queue mirror list) [optional cross-check]

Outputs:
 - Prints summary counts
 - Emits detailed report to stdout (redirect by caller) including:
   * Total untracked titles (from audit)
   * Count enumerated in clusters
   * Missing titles
   * Duplicate titles (appearing in >1 cluster)
   * Cluster → count mapping

Method:
 1. Parse audit report: collect lines under '## Untracked Blocks' until blank line before '## All Discovered Blocks'. Extract title text before first '(' trimming whitespace.
 2. Parse cluster membership file: identify cluster headers starting with '## ' or '### ' that match 'Cluster:' or domain headings preceding bullet lists; for simplicity treat any bullet line beginning with ' - ' (dash-space) under a top-level cluster section as potential title.
 3. Normalize titles by stripping trailing spaces and periods for comparison; keep original for reporting.
 4. Compute set differences and duplicates.
 5. Optional: cross-check that every enumerated title appears at least once in membership (should by definition) and optionally appears in active-gaps-index Normalization Queue (skipped if file missing or mismatch not critical).

Assumptions:
 - Files encoded UTF-8.
 - Bullet prefix pattern consistent ('- ' at line start after optional single space).

Limitations:
 - Will not attempt to disambiguate intentionally duplicated items (e.g., "Glossary completeness") beyond flagging duplicates.

Exit codes:
 0 success (even if missing titles exist; report communicates issues)
 1 unexpected exception

"""
from __future__ import annotations
import re
from pathlib import Path
import sys
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'incomplete-block-audit-report.md'
MEMBERSHIP = ROOT / 'gap-cluster-membership.md'

TITLE_LINE_RE = re.compile(r'^- (.+?) \(File:')


def parse_audit_untracked(path: Path):
    text = path.read_text(encoding='utf-8').splitlines()
    untracked_section = False
    titles = []
    for line in text:
        if line.startswith('## Untracked Blocks'):
            untracked_section = True
            continue
        if untracked_section:
            if line.startswith('## All Discovered Blocks'):
                break
            m = TITLE_LINE_RE.match(line.strip())
            if m:
                raw = m.group(1).strip()
                titles.append(raw)
    return titles

CLUSTER_HEADER_RE = re.compile(r'^## ')
BULLET_RE = re.compile(r'^- (.+)')


MEMBERSHIP_LINE_RE = re.compile(r'^- (.+?) \(File:')


def parse_cluster_membership(path: Path):
    titles = []
    for line in path.read_text(encoding='utf-8').splitlines():
        m = MEMBERSHIP_LINE_RE.match(line.strip())
        if m:
            titles.append(m.group(1).strip())
    return titles


def normalize(title: str) -> str:
    return title.rstrip('.').strip().lower()


def main():
    if not AUDIT.exists() or not MEMBERSHIP.exists():
        print('Required files missing', file=sys.stderr)
        return 1

    audit_titles = parse_audit_untracked(AUDIT)
    membership_titles = parse_cluster_membership(MEMBERSHIP)

    norm_audit = {normalize(t): t for t in audit_titles}
    # membership may have duplicates of same normalized form
    membership_norm_map = defaultdict(list)
    for t in membership_titles:
        membership_norm_map[normalize(t)].append(t)

    missing = []
    for norm_key, original in norm_audit.items():
        if norm_key not in membership_norm_map:
            missing.append(original)

    duplicates = {orig_norm: versions for orig_norm, versions in membership_norm_map.items() if len(versions) > 1}

    coverage = 1 - (len(missing) / len(audit_titles) if audit_titles else 0)

    summary = {
        'audit_untracked_total': len(audit_titles),
        'membership_enumerated': len(membership_titles),
        'missing_from_membership': len(missing),
        'duplicate_normalized_titles': len(duplicates),
        'coverage_ratio': f"{coverage:.3f}",
    }

    print('# Cluster Validation Report')
    print()
    print('Summary:')
    for k, v in summary.items():
        print(f'- {k}: {v}')
    print()
    if missing:
        print('## Missing Titles')
        for t in missing:
            print(f'- {t}')
        print()
    else:
        print('## Missing Titles')
        print('- None')
        print()
    if duplicates:
        print('## Duplicate Normalized Titles')
        for norm_key, versions in duplicates.items():
            display = ', '.join(sorted(set(versions)))
            print(f'- {norm_key}: {display}')
        print()
    else:
        print('## Duplicate Normalized Titles')
        print('- None')
        print()
    print('## Notes')
    print('- Duplicates may be intentional (e.g., repeated "Glossary completeness" in distinct source contexts).')
    print('- Missing titles indicate cluster enumeration coverage gap.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        raise SystemExit(1)
