# Live-Agent exposed cases v1

This directory is a narrow, two-case exposed-development evaluation slice. It keeps
the evaluated model tool-less and gives it only one task packet at a time.

- `workspaces/` contains model-visible inputs only.
- `sealed_references/` is read only by deterministic comparison code and is never
  included in a model request.
- `recorded/` receives request receipts and model outputs from a bounded local run.

The Profiler proposes a CaseGraph projection. The Planner receives the human
canonical projection and proposes actions only. Neither role selects Rules, changes
claim ceilings, or executes an attestation or Operator. The three reported views —
`parse_and_leakage_view`, `typed_contract_view`, and
`sealed_reference_and_authorization_view` — inspect the same recorded proposal. They
are not independent model arms, samples, or an accuracy benchmark.

Each recorded run can be regenerated with
[`scripts/replay_live_agent_exposed_v1.py`](../../scripts/replay_live_agent_exposed_v1.py).
The replay only reads committed packets, references, responses, and proposals; it
does not start a model transport. Its `evaluation_manifest.json` records which prompt
snapshots are reproducible and which historical prompt hashes are retained without
matching text.

Scope: `EXPOSED_DEVELOPMENT_ACTIVE / EXACT_CASE_BOUND / NOT_GENERAL / NOT_PRODUCTION`.
The artifacts cannot support a scientific conclusion, Agent-value claim, transfer
claim, or held-out claim.
