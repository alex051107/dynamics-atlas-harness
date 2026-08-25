# Dynamics Atlas 当前执行计划与停止点

`DA-HARNESS-FROZEN-PLAN-v1.0` 继续控制本仓库的后续工作。原合并 PR #1 已收到 `CHANGES_REQUESTED`，改名为 proposal 并在未合并的情况下关闭，branch 与 commit 保留。独立 PR0 已提交为 GitHub [PR #3](https://github.com/alex051107/dynamics-atlas-harness/pull/3)，当前为 OPEN/CLEAN，远端 unit CI 通过。

## 第一屏结论

| 问题 | 当前答案 |
| --- | --- |
| 现在在做什么 | 等待人工审查独立 PR0 的 baseline 与 Operator lifecycle 修正 |
| 为什么停在这里 | Frozen Plan 要求 PR0 先独立审查和合并，修订 PR1 不能提前创建 |
| 已经固定什么 | CHANGES_REQUESTED、原 PR 的 superseded 状态、PR0 diff、测试结果和 PR1 修复清单 |
| 现有证据支持什么 | 支持 control-plane smoke 命名、canary 隔离和 ROSTER-only routing gate |
| 尚未解决什么 | PR0 人工 merge decision，以及 PR1 的 source、scope、schema、policy、Human Gate、behavioral fixtures 和科学批准 |

GitHub PR #3 是平台自动编号，不代表 Frozen Plan 阶段 PR3。Frozen Plan PR2 至 PR8 仍为 `NOT_AUTHORIZED`。

## 当前授权

| 阶段 | 状态 | 当前处理 |
| --- | --- | --- |
| PR0 Baseline Boundary Normalization | 独立 PR #3 已开放，本地 focused tests 和远端 CI 通过 | 只读审查并作出人工 merge decision |
| PR1 Rules Prototype v1 | `CHANGES_REQUESTED`，原合并 PR 已关闭且未合并 | 只保留修复清单，不创建 replacement branch |
| PR2 至 PR8 | `NOT_AUTHORIZED` | 不建分支，不改代码，不运行对应实验 |

允许的下一动作只有以下三项。

1. 阅读 PR #3 的 diff、PR0 Exit Gate 报告和 CI。
2. 对 PR0 提出修改，或由人工决定是否合并。
3. 在 PR0 合并后更新 `main`，再决定是否创建修订 PR1。

当前自动代码修改权限已经停止。不得提前创建修订 PR1，也不得合并治理 PR #2 或 PR0 #3，除非项目负责人直接作出 merge decision。

## PR0 当前证据

独立 PR0 从 `main@ba318e5` 创建，head 为 `253a7b4`。它不含 `rules_prototype/v1` 文件，改动只覆盖 baseline、Operator registries、RunPlan admission、CLI canary 默认值、直接相关文档和 `test_target_architecture.py`。

本地一个 focused invocation 运行 6 项 tests，结果为 6/6 PASS。workspace assets 可用，因此实际 selector、MDAnalysis blocked probe 和 HSP90 canary tests 均未 skip。X-EISD 保持 59 obligations、15 unresolved inputs、16 blocked gaps 和 0 个 case-routed Operators。GitHub Actions run `32867680634` 的 unit job 也已通过。

这些结果只证明 PR0 的 structural 和 execution boundary。HSP90 仍为 `CANARY_PASS / routable=false`，MDAnalysis projection 仍为 `REGISTERED_BLOCKED / routable=false`。

## 原 PR #1 的处置

`DA-DEV-20260825-001-DISPOSITION-001` 记录了人工结论。原 PR #1 在计划采纳前混合 PR0 与部分 PR1，现已改名为 `Propose review-led Rules Prototype v1`，状态为 CLOSED，`mergedAt=null`，branch `codex/rules-prototype-v1@2f9422a` 保留。

这一处置保存了历史，也恢复了 Frozen Plan 的阶段隔离。它不表示旧 PR 已满足 PR1 Exit Gate。

## 修订 PR1 必须解决什么

- proposal 命名和机器状态
- plan-defined 目录、coverage gap register 和 family overlay
- source-grounding evidence packet 与 atomic paper statement
- SP02、SP04、SP06、SP08 的 multi-target sub-bindings 和 contracts
- binding grammar、JSON Schema 和 current/vNext CaseGraph path mapping
- Resolution Policy 字段类型与 action vocabulary
- scientific claim-ceiling contract 与独立 `HumanDecisionGate`
- SP03 method-profile boundary 和 SP04 两类 failure mode
- positive、one-field negative、missing-evidence 和 wrong-target behavioral runner
- remote CI 与 local workspace integration 的分开报告
- `RULES_PROTOTYPE_V1_REVIEW_PACKET.md` 和人工 approve、revise、reject 字段

修订 PR1 仍需 human scientific review。source passage 可以进入 review evidence packet 或通过 locator 解析，但不能复制进 runtime overlay 形成第二套 scientific authority。

## 状态归属与优先级

- 控制计划见 [DA-HARNESS-FROZEN-PLAN-v1.0](DA_HARNESS_FROZEN_EXECUTION_PLAN_V1_0_ZH.md)
- 机器可读计划状态见 [frozen_execution_plan_v1_0.json](../governance/frozen_execution_plan_v1_0.json)
- 机器可读当前执行点见 [current_execution_status.json](../governance/current_execution_status.json)
- 追加式偏差与处置记录见 [deviations.jsonl](../governance/deviations.jsonl)
- PR0 Exit Gate 报告将在独立 PR0 中维护
- 项目唯一 live status 见 [DYNAMICS_ATLAS_STATUS.md](../../autoresearch/DYNAMICS_ATLAS_STATUS.md)

新的直接用户指令、项目永久边界和 live Status 中已登记的人工决定优先于本计划。设计说明和任务笔记只能补充实现细节，不能自行扩大授权。
