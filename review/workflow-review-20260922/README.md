# Review packet, 22 September 2026: stage cards, per-turn context and a first pilot

This folder is for outside review of the Dynamics Atlas plan as it stood on 22 September 2026. The earlier packet, `review/workflow-review-20260920`, stays as it was; it holds the v1.0 plan, the meeting transcript and the meeting notes.

## What the project is building

Dynamics Atlas is a database of alternative apo states: conformations a protein visits on its own when a given ligand is not bound. Most of the evidence comes from NMR, either two resolved peaks in slow exchange or a minor state fitted from relaxation dispersion (CPMG, CEST, R1ρ). Each entry records the protein and conditions, the ligand relative to which the protein counts as apo, the two states, the exchange parameters, the residues involved, why the minor state is thought to resemble a known state, the functional evidence, what the evidence cannot support, and a tier (strong, weak, candidate, not included).

A strong model writes each entry by following eight stage cards. A program around it decides what the model sees each turn, checks every action before it runs, records every result with its provenance, and moves the analysis from stage to stage. People own the definitions, the tiers and the final acceptance of an entry.

## Where to start

Read `HARNESS_EXPLAINER_FOR_PRO_ZH.md` first. It is written in Chinese for a reader who has never seen the project, and it opens with the review request for ChatGPT Pro. It covers three questions in detail:

1. How the scientists' workflow was turned into stage cards: paper-by-paper traces, an evidence table counted by protein, a saturation rule, expert review, then a versioned freeze.
2. How the harness builds the model's context each turn. The program keeps the run state and rebuilds a bounded view every turn instead of resending the chat history. The view has a fixed prefix (system rules, definitions, tool contracts) and a rolling part (the current card, what changed since the last turn, stuck status, recent observations, the evidence index, budget).
3. How tools and registered operators are defined, admitted, executed and recorded.

## Contents

| Path | What it holds |
|---|---|
| `HARNESS_EXPLAINER_FOR_PRO_ZH.md` | The full explanation and the review request |
| `plan/PLAN_V2_1_ZH.md` | Execution plan v2.1 (Chinese) |
| `workflow/STAGE_CARDS_V1_DRAFT.md` | Stage cards, draft v1, built from nine papers |
| `workflow/EVIDENCE_TABLE_V1.md` | 105 moves with paper locations; support counted by distinct protein |
| `workflow/SUBAGENT_DIVISION_ZH.md` | Which parts of the work go to separate subagents, and why |
| `workflow/paper_traces/` | One trace per paper (the two RfaH papers share a file) |
| `workflow/DATA_AVAILABILITY_PROBE.md` | What the BMRB, PDB and author deposits actually contain |
| `research/` | Notes on FutureHouse's public agent code and on LangGraph, with file-level locators |
| `pilot/` | The prompt-level pilot: preregistration, prompts, 16 entries, 4 checked references, 4 blind grades, results |

## The pilot in one paragraph

Sixteen Sonnet runs wrote entries for four papers that were not used to build the cards, half with the stage cards in the prompt and half without. An Opus grader scored each paper's four entries blind against a reference that a separate Sonnet run had checked against the paper. Under the rule fixed before the runs, the cards did not show a benefit: the card group scored higher on two papers, tied on one and scored lower on one, and the rule needed three. The card group made fewer over-claims (8 against 11; five of its eight entries had none, against one of eight in the control group) and more factual errors (3 against 1). The item-level comparisons in `pilot/RESULTS.md` were made after grading and are labelled that way.

## What is not here, and why

- The Compass runtime code lives on a local branch that we have not pushed.
- We left out paper PDFs and supplements. Every trace and entry cites the paper's DOI and a page, figure or table.
- We left out the subagent transcripts. `pilot/PREREGISTRATION.md` records what a script found when it read them: which files each run opened, and that no run opened a reference, another run's output or a general web search.
- We replaced local absolute paths in the prompts with `<pilot>`. The local folders `runs/` and `_sealed_reference/` appear here as `pilot/entries/` and `pilot/references/`.

## Claim limits

Traces, cards, references and grades were written by models and have not been checked by the domain experts yet. The pilot measures one prompt-level contrast on four papers with two runs per group; it says nothing yet about the stage-by-stage harness, which is not built. Numbers from the Compass tests come from scripted stand-ins, not from a model.
