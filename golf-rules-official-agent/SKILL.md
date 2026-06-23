---
name: golf-rules-official-agent
description: Answer Rules of Golf questions with a Markdown-first, current-rules workflow. Use when a user asks about Rules of Golf rulings, penalties, relief procedures, match play or stroke play differences, Local Rules, Clarifications, Official Guide materials, Decisions mapping, bilingual Chinese/English golf rules lookup, or how to build/search a local Rules of Golf corpus without redistributing official rule text.
---

# Golf Rules Official Agent

## Overview

Use this skill to answer golf rules questions from a local user-provided corpus
and current official source links. Do not rely on model memory alone, do not use
old rulebooks or old Decisions as current authority, and do not redistribute
official rules text.

## Core Rules

- Use current Rules of Golf materials only for current rulings: Rules,
  Definitions, Clarifications, Additional Clarifications, Committee Procedures,
  Model Local Rules, and current Official Guide materials.
- Treat old `Decisions on the Rules of Golf` as historical only. Use old
  Decisions or modernization mapping only to route an old Decision number to
  current Rules / Interpretations / Committee Procedures.
- Search local Markdown first. Use PDFs only if the user explicitly asks for
  PDF verification or the Markdown extraction is visibly unclear.
- Never include, create, paste, or commit official rules corpus content into a
  public repository unless the user confirms they have distribution permission.
- Quote only short excerpts when needed; prefer paraphrase plus rule numbers.

## Workflow

1. Identify missing facts that could change the ruling:
   - format: stroke play, match play, four-ball, foursomes, casual play
   - area of the course: teeing area, general area, bunker, penalty area,
     putting green, out of bounds
   - ball status: in motion, at rest, lost, moved, lifted, replaced, dropped
   - actor or cause: player, caddie, opponent, partner, outside influence,
     natural forces
   - Local Rules or Committee conditions that may apply
2. Search the local Markdown corpus with both natural-language terms and likely
   rule numbers.
3. Cross-check current official links when the answer is high stakes,
   contested, or likely to depend on a recent clarification.
4. Answer with a concise ruling, action steps, penalty, rule basis, caveats, and
   confidence.

## Local Corpus

Expect the user to provide their own local corpus. Common environment variable:

```bash
export GOLF_RULES_CORPUS_DIR="$HOME/golf-rules-corpus"
```

Search it directly:

```bash
rg -n 'Rule 11|ball in motion|equipment|stroke play' "$GOLF_RULES_CORPUS_DIR"
rg -n '规则 11|运动中球|装备|比杆赛' "$GOLF_RULES_CORPUS_DIR"
```

If the user has PDFs they are permitted to use locally, run:

```bash
python3 scripts/prepare_corpus.py --source-dir ./source-pdfs --output-dir "$GOLF_RULES_CORPUS_DIR"
```

To search without loading large files into context:

```bash
python3 scripts/search_rules.py "$GOLF_RULES_CORPUS_DIR" 'Rule 11|equipment'
```

## References

Load only what is needed:

- `references/official-sources.md`: official source links and source hierarchy.
- `references/answer-format.md`: response format, fact checklist, and examples.
- `references/bilingual-routing.md`: Chinese/English lookup strategy.
- `references/corpus-policy.md`: copyright and repository safety boundaries.

## Answer Format

1. State the ruling in one or two sentences.
2. Give the required procedure: where to play, whether to drop/place/replace,
   and whether the stroke must be replayed.
3. State the penalty, if any.
4. Cite rule number(s), definitions, Clarifications, or Model Local Rules.
5. Note any facts that would change the answer.
6. State confidence and whether the answer used local corpus or online sources.
