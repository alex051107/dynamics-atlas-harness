# Dynamics Atlas source-science review workspace

This directory prepares the narrow F01/F02/F03/F04/F06 human/domain review required
after the merged exposed development capsule. It is an evidence map and blank review
form, not a new Rules authority and not a scientific decision.

## What a reviewer should inspect

For every row in `source_passage_index.json` and `case_application_matrix.json`:

1. Open the recorded locator and check the primary passage or case-bound artifact.
2. Decide whether the stated atomic claim supports only the stated reusable use.
3. Check whether the listed HSP90 or ADK application stays inside its claim ceiling.
4. Copy `reviewer_form.json` to a local working file. Keep `review_status` as `DRAFT`
   while any item or case record is incomplete.
5. Record dispositions separately for the reusable Rule question and for each exact
   `case_id` + reviewed target/RuleInstance record. Set `COMPLETED` only after all
   records have a named reviewer, role, ISO date, checked passage, allowed scope,
   claim ceiling, and supporting note.

`F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL` has
`PENDING_SOURCE_TRACEABILITY_MAPPING`. The overlay-required packet labels do not map
to repository records keyed by those labels. A positive F04 disposition is invalid
until a human resolves that mapping; the existing record remains an exact-control
regression with `NO_ACTIVE_RULE_EFFECT` on the public HSP90 case.

## Allowed dispositions

- `APPROVE_AS_WRITTEN`
- `APPROVE_WITH_BOUNDED_REVISION`
- `DEFER_INSUFFICIENT_SOURCE_GROUNDING`
- `REJECT_NOT_REUSABLE`
- `NOT_APPLICABLE_TO_CURRENT_CASE`

A positive disposition requires nonempty reviewer identity, role, ISO review date,
checked passage, allowed scope, claim ceiling, and supporting note. It does not
activate a Rule, Resolution Policy, Evaluation Contract, Operator, or scientific claim.
A later human/project decision must explicitly select any allowed next action.

## Local review-template export

The committed `reviewer_form.json` is a blank local template. Copy it to an untracked
working file before editing. The static console links to the template but has no form,
save endpoint, or scientific-state mutation path. Validate any completed record against
`reviewer_form.schema.json` and the exact case-application matrix before treating it as
a review record.

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

View the generated workbench with the standard-library static file server:

```bash
python3 -m http.server 8000 --directory review_console
```

Then open `http://127.0.0.1:8000/`. The server exposes files only; it does not add an
execution, review-save, or scientific-state mutation endpoint.
