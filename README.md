# Golf Rules Official Agent

An open-source agent skill for answering Rules of Golf questions with a
Markdown-first, current-rules workflow. It ships the **method** — a fact
checklist, a referee case-adjudication workflow, bilingual routing, and corpus
search scripts — but intentionally ships **no official rules content**.

This repository does **not** include official Rules of Golf PDFs, converted
Markdown rules text, embeddings, vector databases, or any other redistributed
official rules corpus. You bring your own local, user-owned corpus.

## What This Is

- An agent skill (`golf-rules-official-agent`) for Codex and Claude Code.
- A workflow for answering golf rules questions from local sources.
- A referee case-adjudication branch workflow with hard output requirements.
- A Markdown-first corpus search pattern with prepare/search scripts.
- Official source links and safe public-repository boundaries.

## What This Is Not

- Not affiliated with or endorsed by R&A, USGA, or any national golf association.
- Not a copy of the Rules of Golf.
- Not legal advice, and not a substitute for a referee, Committee, or official ruling.

## Install

**Codex** — copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R golf-rules-official-agent "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Claude Code** — the skill uses the standard `SKILL.md` + `references/` format,
so the same folder works as a Claude skill:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R golf-rules-official-agent "$HOME/.claude/skills/"
```

Then ask your agent:

```text
Use golf-rules-official-agent to answer this Rules of Golf question: ...
```

## Prepare A Local Corpus

Download official materials yourself from the R&A, USGA, or your national
association. Put the PDFs in a local directory that is **not** committed to git.

Install Poppler if needed so `pdftotext` is available:

```bash
brew install poppler
```

Convert local PDFs to Markdown and set the corpus path:

```bash
mkdir -p ./source-pdfs ./corpus
python3 golf-rules-official-agent/scripts/prepare_corpus.py \
  --source-dir ./source-pdfs \
  --output-dir ./corpus
export GOLF_RULES_CORPUS_DIR="$PWD/corpus"
```

Search it:

```bash
python3 golf-rules-official-agent/scripts/search_rules.py "$GOLF_RULES_CORPUS_DIR" 'Rule 11|equipment'
```

## Example

> **Q:** In stroke play my ball rolls into a red penalty area, but I found it.
> Can I just play it as it lies?

A good answer from this skill:

1. **Clarify the facts first** — is the ball actually inside the penalty area
   margin, is it safe and legal to play from where it lies, and do you want to
   play it as it lies or take one-stroke relief.
2. **Ruling** — yes, you may play a ball that lies in a penalty area as it lies
   with no penalty, or take relief for one penalty stroke.
3. **Procedure** — if taking relief, identify the relevant options (stroke and
   distance, back-on-the-line, or lateral relief for a red penalty area).
4. **Basis** — Rule 17 (Penalty Areas), Definition of "Penalty Area"; check
   Clarifications only if the case involves the entry point, back-line, or
   lateral relief specifics.
5. **Confidence** — high, based on rule text; note it was checked against the
   local corpus.

The referee case-adjudication workflow (`references/referee-adjudication.md`)
adds a stricter branch process for officials ruling on concrete cases: rule
text first, exception-scan the local Clarifications corpus by rule number, and
only drop into the case layer when the rule text does not settle the facts.

## Public Repository Safety

Do not commit official PDFs, Markdown converted from official PDFs, copied
official rule pages, embeddings or vector databases generated from official
rule text, or private notes and local paths. The included `.gitignore` blocks
common corpus paths and generated artifacts. See
`golf-rules-official-agent/references/corpus-policy.md` for the full boundary.

## Official Sources

- R&A Rules of Golf: https://www.randa.org/en/rog/the-rules-of-golf
- R&A Clarifications: https://www.randa.org/en/rog/clarifications
- R&A Committee Procedures: https://www.randa.org/en/rog/committee-procedures
- USGA Rules Hub: https://www.usga.org/content/usga/home-page/rules-hub.html

Use current Rules, Definitions, Clarifications, Additional Clarifications,
Committee Procedures, Model Local Rules, and current Official Guide materials for
current rulings. Old Decisions are historical and should only be used for
historical questions or to map old Decision numbers into current materials.

## License

Code and original documentation in this repository are licensed under the MIT
License. This license does not apply to third-party Rules of Golf content, PDFs,
official pages, or any corpus you generate locally.
