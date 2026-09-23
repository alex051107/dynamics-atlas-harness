# Run prompts (fixed before the first run)

Both groups get the same prompt except for one paragraph. `{PAPER}`, `{URL}`, `{EUROPEPMC}`, `{CODE}`, `{RUN}` and `{GROUP}` are filled per run. Analysis agents run on Sonnet.

## Shared prompt

```text
You are analyzing one scientific paper to write a database entry. Work carefully; accuracy matters more than speed.

Read the task definition, evidence tiers, rules and the 15-field entry format here, and follow them exactly:
<pilot>/task_common.md

{WORKFLOW_PARAGRAPH}

The paper: {PAPER}. Full text: {URL} (Europe PMC alternative: {EUROPEPMC}). Read the full text, figure legends and methods; use the supplementary material if you need it.

Isolation rules. Apart from the file(s) named above, do not open any file on this computer. In particular do not open anything else in the pilot_workflow_ab folder, anything named "_sealed_reference", or any other run's output. Do not use general web search and do not read other papers. You may query BMRB or PDB only for entries this paper cites.

Write your entry to:
<pilot>/runs/{CODE}_{GROUP}_{RUN}.md
(create the folder if needed) and return the same entry as your final message. Output only the entry, at most 900 words.
```

## The one paragraph that differs

Control group:

```text
(no additional guidance)
```

Workflow group:

```text
Use the stage cards in this file as your analysis workflow, and follow them stage by stage before writing the entry:
<pilot>/stage_cards_v1_pilot_frozen.md
Do not mention the cards in your entry.
```

## Blind grader prompt (Opus, one call per paper)

```text
You are grading four database entries written about the same paper, against a reference answer. You do not know how the entries were produced; do not guess. Grade each entry on its content only.

Reference answer (reference entry, must-get-right facts, over-claim list):
{REF_FILE}
Task definition the entries were written to:
.../pilot_workflow_ab/task_common.md
Entries, labeled E1 to E4:
{E1_FILE} ... {E4_FILE}
Open only these files. You may open the paper ({URL}) to settle a disagreement between an entry and the reference; say when you do.

For each entry, score items 1–9 as 0 (wrong or missing), 1 (partly right), 2 (right), or NA (the paper has no such information):
1 apo verdict and the ligand it is relative to; 2 major and alternative states; 3 exchange parameters with sources; 4 residues or regions; 5 identity basis; 6 structural mapping and simulations; 7 functional relevance, with wording matched to the evidence; 8 evidence type and provenance; 9 tier.
Then count: over-claims (statements the paper does not support, including those on the reference's over-claim list) and factual errors (wrong numbers, IDs, conditions). Give one line of justification per nonzero deduction.
Output a table (entry × items, over-claims, factual errors, total of scored items, number of scored items) and short notes. Write to {GRADE_FILE} and return the same content.
```
