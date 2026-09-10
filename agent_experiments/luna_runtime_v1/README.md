# Task-scoped Luna runtime v1

Migrated from the closed September 9 development maintenance candidate. The original development logs remain frozen outside this repository.

The runner executes autonomous source reading, Python analysis and explicit answer submission. This campaign compares A (common sources) with B (the same sources plus selector-rendered rules). No C arm is run.

Supply the task directory explicitly with `--task-root`; it contains `cases/HSP90_Q01/common`, `cases/HSP90_Q01/arm_B`, `cases/HSP90_Q01/hidden`, `runtime` and `outputs`. Only common material is mounted at `/source`, the current run output at `/work`, and the tool at `/tool.py`. Hidden scoring files and the treatment directory are never mounted. B rules are appended to B's input message.

Read the API key only from `OPENROUTER_API_KEY` in the developer process environment. The analysis container receives no credential and has no network. Use the frozen image and task readiness, campaign deadlines and ledger supplied with the task.

```sh
python3 run_batch.py --freeze "$TASK_ROOT/outputs/frozen_hsp90_q01_v3.json" --task-root "$TASK_ROOT" --budget-usd 0.15
```

The freeze records the randomized A/B order, image, model and input identities. Every request reserves its cost before execution. Unknown charge stops the campaign. The runner does not automatically repeat a completed batch or failed scientific answer.

Case data, hidden keys, raw run logs, credentials and financial ledgers are excluded from this code repository. The runtime alone is not a self-contained scientific case packet. Execute the assertion scripts `test_*.py` directly; they are not all unittest-discover tests. Repository CI uses the declared `exposed-capsule-v1` dependencies.
