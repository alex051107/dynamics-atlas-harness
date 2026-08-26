# Live-Agent exposed cases v1

This directory is a narrow, two-case exposed-development evaluation slice. It keeps
the evaluated model tool-less and gives it only one task packet at a time.

- `workspaces/` contains model-visible inputs only.
- `sealed_references/` is read only by deterministic comparison code and is never
  included in a model request.
- `recorded/` receives request receipts and model outputs from a bounded local run.

The Profiler proposes a CaseGraph projection. The Planner receives the human
canonical projection and proposes actions only. Neither role selects Rules, changes
claim ceilings, or executes an attestation or Operator. The three reported views
(`free_form`, `vocabulary_assisted`, and `bounded_harness`) inspect the same recorded
proposal; they are not independent model samples or an accuracy benchmark.

Scope: `EXPOSED_DEVELOPMENT_ACTIVE / EXACT_CASE_BOUND / NOT_GENERAL / NOT_PRODUCTION`.
The artifacts cannot support a scientific conclusion, Agent-value claim, transfer
claim, or held-out claim.
