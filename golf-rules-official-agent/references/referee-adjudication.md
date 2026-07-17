# Referee Case Adjudication

Use this workflow when the user acts as a referee or official and gives a
concrete case that needs a ruling, rather than a general "how do I proceed"
question. This is a branch process, not a pipeline: **most cases should close at
step 2.** Only continue down the steps when the plain rule text cannot cover the
facts of the case.

## Workflow

1. **Extract the key facts.** Competition format (stroke play / match play /
   four-ball / foursomes), area of the course, ball status, the time order of
   actions, who caused what, and whether a stroke / drop / substitution has
   already happened. If a fact that would change the ruling is missing, ask
   before ruling.

2. **Rule-first; if it is clear, close the case.** Locate the controlling
   provision in the rule text of your local corpus. If the rule text directly
   and unambiguously covers the facts, cite the rule number and give the
   conclusion — you do **not** need to dig into the case layer. The one exception
   scan: before closing, run a single rule-number query against the local
   Clarifications corpus (seconds) to confirm there is no exception entry under
   that rule that would change the conclusion. If nothing relevant appears,
   conclude.

   ```bash
   # Exception scan by rule number over the local Clarifications corpus
   rg -n '### 9\.4|### 11\.1' "$GOLF_RULES_CORPUS_DIR"
   ```

3. **If the rule text is unclear, ambiguous, or the case has special
   elements, go to the case layer.** Search the local Clarifications corpus (the
   current replacement layer for the old Decisions Book). Narrow by rule number
   first, then match by the fact elements of the case.

4. **If there is still no clear basis**, check Additional Clarifications and
   Committee Procedures / Model Local Rules (online), and explicitly state that
   the local corpus has no directly corresponding entry.

5. **If the user gives an old Decision number**, map it to the current number
   first, then rule per the current text. Old Decisions are not a basis for a
   current ruling on their own.

## Output Requirements (hard)

- The conclusion must land on an explicit basis: `Rule X.Xx`,
  `Clarification X.Xx/N`, `Committee Procedures Section N`, or `MLR X-N`. State
  whether the basis is the rule text or the case layer.
- Give: the ruling, the number of penalty strokes (state stroke play and match
  play separately if they differ), and the correct follow-up procedure (where to
  play from, how to drop).
- If neither the rule text nor the case layer has a match, say plainly that the
  current framework has no directly corresponding entry, give the closest
  provision and your reasoning, mark it low confidence, and recommend referring
  it to the Committee (Rule 20.2).
- Confidence: high (rule text covers directly) / medium (case-layer analogy) /
  low (no direct basis).

## Rule Routing Table

Use this to jump straight to the likely controlling rule. Rule numbers
themselves are not copyrighted text; do not paste the rule wording into the
repository.

| User question | Look up first |
|---|---|
| Ball moved, ball at rest questions | Rule 9, Definitions, Clarifications |
| Ball in motion hits self / equipment / flagstick / person | Rule 11, Rule 13 |
| Dropping, re-dropping, placing, substituting a ball | Rule 14 |
| Loose impediments / movable obstructions | Rule 15 |
| Immovable obstruction, abnormal course conditions, embedded ball | Rule 16 |
| Red / yellow stakes, penalty areas | Rule 17 |
| Lost ball, out of bounds, provisional ball | Rule 18 |
| Unplayable ball | Rule 19 |
| Unsure how to proceed on course, second ball, dispute mid-round | Rule 20 |
| Case / Decision / Official Guide / Interpretation lookup | Clarifications, Committee Procedures |
| Match play specific handling | Rule 3, Rule 20, relevant match-play Clarifications |
| Local Rules, temporary water, ground under repair, course markings | Committee Procedures, Model Local Rules |
| Self-standing putters, DMD, damaged club, ball conformance | Equipment Rules, Rule 4, Model Local Rules G-1/G-3/G-5 |
| Prize money, teaching fees, professional / amateur status | Rules of Amateur Status |
| Card return, handicap, acceptable scores, unfinished holes | Rules of Handicapping / WHS |
