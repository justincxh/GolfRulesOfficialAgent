# Golf Rules Official Agent

An open-source Codex skill for answering Rules of Golf questions with a
Markdown-first, current-rules workflow.

This repository intentionally does **not** include official Rules of Golf PDFs,
converted Markdown rules text, embeddings, vector databases, or any other
redistributed official rules corpus.

## What This Is

- A Codex skill: `golf-rules-official-agent`
- A workflow for answering golf rules questions from local sources
- A Markdown-first corpus search pattern
- Scripts to prepare and search a local user-owned corpus
- Official source links and safe repository boundaries

## What This Is Not

- Not affiliated with or endorsed by R&A, USGA, or any national golf association
- Not a copy of the Rules of Golf
- Not legal advice
- Not a substitute for a referee, Committee, or official ruling

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R golf-rules-official-agent "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then ask Codex:

```text
Use $golf-rules-official-agent to answer this Rules of Golf question: ...
```

## Prepare A Local Corpus

Download official materials yourself from the R&A, USGA, or your national
association. Put the PDFs in a local directory that is not committed to git.

Install Poppler if needed so `pdftotext` is available:

```bash
brew install poppler
```

Convert local PDFs to Markdown:

```bash
mkdir -p ./source-pdfs ./corpus
python3 golf-rules-official-agent/scripts/prepare_corpus.py \
  --source-dir ./source-pdfs \
  --output-dir ./corpus
```

Set the corpus path:

```bash
export GOLF_RULES_CORPUS_DIR="$PWD/corpus"
```

Search it:

```bash
python3 golf-rules-official-agent/scripts/search_rules.py "$GOLF_RULES_CORPUS_DIR" 'Rule 11|equipment'
```

## Public Repository Safety

Do not commit:

- Official PDFs
- Markdown converted from official PDFs
- Copied official rule pages
- Embeddings or vector databases generated from official rule text
- Private Obsidian notes or local paths

The included `.gitignore` blocks common corpus paths and generated artifacts.

## Official Sources

Start here:

- R&A Rules of Golf: https://www.randa.org/en/rog/the-rules-of-golf
- R&A Clarifications: https://www.randa.org/en/rog/clarifications
- R&A Committee Procedures: https://www.randa.org/en/rog/committee-procedures
- USGA Rules Hub: https://www.usga.org/content/usga/home-page/rules-hub.html

Use current Rules, Definitions, Clarifications, Additional Clarifications,
Committee Procedures, Model Local Rules, and current Official Guide materials
for current rulings. Old Decisions are historical and should only be used for
historical questions or to map old Decision numbers into current materials.

## License

Code and original documentation in this repository are licensed under the MIT
License. This license does not apply to third-party Rules of Golf content, PDFs,
official pages, or any corpus you generate locally.
