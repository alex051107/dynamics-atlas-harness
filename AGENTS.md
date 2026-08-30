# Repository instructions

## Project path

```text
scientific question
  → deterministic admission
  → Rules and obligations
  → constrained proposal
  → deterministic authorization
  → direct / lookup / registered action / abstain
  → EvidenceResult
  → same-Rule reevaluation
  → bounded ConclusionPacket
  → human review
```

## Authority

- Agent proposes only.
- Rules determine obligations.
- Authorization is deterministic.
- Operator results are evidence.
- Evaluators apply frozen contracts.
- Human/domain reviewer retains scientific authority.
- CI proves engineering behavior only.

## Required preflight

Before implementing:

- inspect the exact `main`;
- inspect open PRs;
- read the current execution status;
- distinguish `Observed` / `Inference` / `Proposal`;
- verify the current gate.

## Development discipline

- one branch, one demonstrated failure layer;
- reuse existing narrow boundaries;
- write behavioral tests;
- no case-specific verdict;
- no hidden held-out access;
- no automatic next milestone.

## Default no-build list

Do not build by default:

- generic scheduler;
- DAG engine;
- database;
- RAG;
- MCP;
- provider framework;
- plugin framework;
- multi-agent runtime;
- arbitrary shell execution controlled by a scientific Agent;
- automatic scientific approval.

## Required completion report

Report:

1. Decision
2. Observed failure
3. Behavior changed
4. Tests run
5. What tests do not prove
6. Allowed claim
7. Forbidden upgrade
8. Remaining risk
9. Exact base/head
10. Next authorized action
