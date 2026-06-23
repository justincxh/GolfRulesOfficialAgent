# Corpus Policy

This skill is designed to be open source without redistributing official Rules
of Golf text.

## Do Not Commit

- Official Rules of Golf PDFs.
- Markdown files generated from official PDFs.
- Full-text copies of R&A, USGA, or national association rules pages.
- Embeddings, vector databases, SQLite databases, or search indexes generated
  from official full text.
- Personal Obsidian vault paths, private notes, or private corpus files.

## Safe To Commit

- The skill instructions.
- Scripts that let users prepare their own local corpus.
- Source links.
- Search workflow instructions.
- Short, original examples.
- Tests that use tiny synthetic sample text, not official rule text.

## Public Repository Pattern

Keep the repository corpus-free. Users should:

1. Download official materials themselves from R&A, USGA, or their national
   association.
2. Store them locally in a directory that is not committed.
3. Run `scripts/prepare_corpus.py`.
4. Set `GOLF_RULES_CORPUS_DIR`.
5. Ask their agent Rules of Golf questions against that local corpus.

This is not legal advice. If a user wants to redistribute official rule text,
they should obtain written permission from the relevant rightsholders.
