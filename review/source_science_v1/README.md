# Dynamics Atlas source-science review workspace

This directory prepares the narrow F01/F02/F03/F04/F06 human/domain review required
after the merged exposed development capsule. It is an evidence map and blank review
form, not a new Rules authority and not a scientific decision.

## What a reviewer should inspect

For every row in `source_passage_index.json` and `case_application_matrix.json`:

1. Open the recorded locator and check the primary passage or case-bound artifact.
2. Decide whether the stated atomic claim supports only the stated reusable use.
3. Check whether the listed HSP90 or ADK application stays inside its claim ceiling.
4. Enter a named, dated disposition in `reviewer_form.json` without changing Rule or
   runtime files.

`F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL` intentionally begins with a pending
traceability mapping. Its case dossier and manifest identify a bounded control record,
but this workspace does not invent a primary-paper passage for it.

## Allowed dispositions

- `APPROVE_AS_WRITTEN`
- `APPROVE_WITH_BOUNDED_REVISION`
- `DEFER_INSUFFICIENT_SOURCE_GROUNDING`
- `REJECT_NOT_REUSABLE`
- `NOT_APPLICABLE_TO_CURRENT_CASE`

A positive disposition does not automatically activate a Rule, Resolution Policy,
Evaluation Contract, Operator, or scientific claim. A later human/project decision must
explicitly select any allowed next action.

## Regeneration

Run from the repository root:

```bash
PYTHONPATH=src python scripts/build_source_science_review_workspace_v1.py \
  --output-dir review/source_science_v1
```

To render the companion read-only trace:

```bash
PYTHONPATH=src python scripts/render_review_console_v0.py \
  --status governance/current_execution_status.json \
  --capsule-root evidence/paper_blind_exposed_v1/development_runs/exposed_paper_blind_scientific_decision_capsule_v1 \
  --review-workspace review/source_science_v1 \
  --output-dir review_console
```

The resulting `review_console/index.html` is local and static. It contains no mutation
endpoint, credential handling, model call, operator execution, or database.
