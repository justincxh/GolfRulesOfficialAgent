#!/usr/bin/env python3
"""Search a local Markdown Rules of Golf corpus."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def iter_markdown(corpus_dir: Path):
    for path in sorted(corpus_dir.rglob("*.md")):
        if path.is_file():
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus_dir", help="Directory containing generated Markdown files.")
    parser.add_argument("pattern", help="Regular expression to search for.")
    parser.add_argument("--context", type=int, default=1, help="Context lines before and after a match.")
    parser.add_argument("--ignore-case", action="store_true", help="Case-insensitive search.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum matching lines to print.")
    args = parser.parse_args()

    corpus_dir = Path(args.corpus_dir).expanduser().resolve()
    if not corpus_dir.is_dir():
        raise SystemExit(f"Corpus directory not found: {corpus_dir}")

    flags = re.IGNORECASE if args.ignore_case else 0
    regex = re.compile(args.pattern, flags)
    printed = 0

    for path in iter_markdown(corpus_dir):
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for idx, line in enumerate(lines):
            if not regex.search(line):
                continue
            start = max(0, idx - args.context)
            end = min(len(lines), idx + args.context + 1)
            for number in range(start, end):
                prefix = ":" if number == idx else "-"
                print(f"{path}:{number + 1}{prefix}{lines[number]}")
            printed += 1
            if printed >= args.limit:
                return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
