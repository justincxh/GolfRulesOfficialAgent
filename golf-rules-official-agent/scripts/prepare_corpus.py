#!/usr/bin/env python3
"""Create a local Markdown corpus from user-provided PDFs.

This script does not download or redistribute official rule text. It converts
PDFs that the user already has permission to use locally.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path


def slugify(name: str) -> str:
    chars = []
    previous_dash = False
    for char in name.lower():
        if char.isalnum():
            chars.append(char)
            previous_dash = False
        elif not previous_dash:
            chars.append("-")
            previous_dash = True
    return "".join(chars).strip("-") or "document"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def convert_pdf(pdf: Path, output_dir: Path, overwrite: bool) -> Path:
    output_path = output_dir / f"{slugify(pdf.stem)}.md"
    if output_path.exists() and not overwrite:
        raise FileExistsError(f"{output_path} already exists; pass --overwrite")

    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf), str(output_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"pdftotext failed for {pdf}")
    return output_path


def write_readme(output_dir: Path, rows: list[tuple[Path, Path, str]]) -> None:
    lines = [
        "# Local Golf Rules Corpus",
        "",
        "Generated from user-provided local PDFs.",
        "",
        "Do not publish this directory unless you have permission to redistribute",
        "the underlying source text.",
        "",
        "| Markdown | Source PDF | Source SHA-256 |",
        "|---|---|---|",
    ]
    for markdown, pdf, digest in rows:
        lines.append(f"| `{markdown.name}` | `{pdf.name}` | `{digest}` |")
    lines.append("")
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, help="Directory containing local PDFs.")
    parser.add_argument("--output-dir", required=True, help="Directory for generated Markdown.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Markdown files.")
    parser.add_argument("--no-readme", action="store_true", help="Do not write a corpus README.")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if shutil.which("pdftotext") is None:
        print("pdftotext is required. Install poppler first.", file=sys.stderr)
        return 2
    if not source_dir.is_dir():
        print(f"Source directory not found: {source_dir}", file=sys.stderr)
        return 2

    pdfs = sorted(source_dir.glob("*.pdf")) + sorted(source_dir.glob("*.PDF"))
    if not pdfs:
        print(f"No PDFs found in {source_dir}", file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[Path, Path, str]] = []
    for pdf in pdfs:
        markdown = convert_pdf(pdf, output_dir, args.overwrite)
        rows.append((markdown, pdf, sha256(pdf)))
        print(f"converted {pdf.name} -> {markdown.name}")

    if not args.no_readme:
        write_readme(output_dir, rows)
        print(f"wrote {output_dir / 'README.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
