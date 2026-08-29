# Historical frozen initial baseline

> **Historical initial baseline:** This document records the 2026-08-25
> control-plane-smoke baseline. It is not the current execution state. Read
> [the repository execution-status snapshot](docs/CURRENT_EXECUTION_STATUS_ZH.md)
> before interpreting the scope or next action.

## Baseline identity

```text
project: Dynamics Atlas Harness
baseline: harness-control-plane-smoke-v0.2
frozen_at: 2026-08-25
primary_branch: main
delivery_visibility: private
```

这个 baseline 固定当前 Master Plan、Harness contracts、provider boundary、Rules workspace adapter、Evaluation Contract、RunPlan、registered-operator specs、tests 和一份脱敏的 milestone evidence summary。

`target architecture` 是设计目标。当前 baseline 的已观察证据只到 control-plane smoke：一个真实旧 selector 被调用、case route 正确停在 blocked、一个独立 Operator canary 成功。它不是完整 Agent Harness、Rules semantic prototype 或真实 Rule-to-Operator case resolution。

## Versioned in this repository

- `docs/MASTER_PLAN_ZH.md` 和三份架构说明；
- `prompts/profile_case_v1.md`；
- `src/dynamics_atlas_harness/`；
- `config/` 中的 method/operator/workspace registries 与 frozen asset manifest；
- `tests/` 中不含 reference answer 泄漏的 fixtures 和 boundary tests；
- `evidence/target_architecture_v0_2/` 中的脱敏结果摘要；
- PR template、CI test workflow 和 contribution policy。

## Intentionally not versioned

- `runs/`：包含本机绝对路径、完整 selector output 和 scientific payload；
- 上游 33-row Rules Registry、v0.3 bindings/index、method scope 和 rich CaseGraph；
- HSP90 frame assignments、route predictions 和其他研究数据；
- Zotero PDF、会议 transcript、Obsidian vault 和 task-control state；
- credentials、tokens、`.env`、cache、build artifacts 和 local logs。

上游 assets 保持原位权威。`config/frozen_assets_v0_1.json` 只保存 workspace-relative locator、role 和 SHA-256，不复制内容。

## Current evidence boundary

允许表述：

- actual v0.3 selector 在一个 exposed X-EISD development case 上被调用；
- 它产生 59 obligations、15 selector unresolved inputs 和 16 total gaps；
- RunPlan 保存 21 nodes、35 execution edges，并合理停在 blocked route；
- 一个 HSP90 existing-analysis canary 独立成功；
- final local test suite 为 18/18 PASS。

禁止表述：

- Rules、semantic correctness 或 scientific conclusion 已验证；
- HSP90 canary 解决了 X-EISD gaps；
- MDAnalysis operator 已可执行；
- transfer、Agent value、external scientific review 或 production readiness 已建立。

## Change policy

这个 initial baseline 可以直接落到新私有仓库的 `main`。完成 baseline push 后：

1. 不再直接向远端 `main` 提交功能或文档修改；
2. 每次修改创建独立 branch；
3. 通过 Pull Request 展示 diff、检查结果、claim boundary 和 remaining risk；
4. PR 合并后更新本文件或 manifest，只在 baseline/authority/claim boundary 真实变化时修改；
5. frozen upstream asset 改变时，必须在 PR 中说明原因并更新对应 SHA-256。
