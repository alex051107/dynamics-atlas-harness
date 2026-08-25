# Dynamics Atlas 当前执行计划与停止点

`DA-HARNESS-FROZEN-PLAN-v1.0` 已成为本仓库后续工作的控制计划。现在只允许核对开放中的 PR #1 是否满足 PR0 和 PR1 的 Exit Gate，并整理一份 `PASS / PARTIAL / FAIL / DEVIATION` 审查包。PR2 至 PR8 均未获授权。

## 第一屏结论

| 问题 | 当前答案 |
| --- | --- |
| 现在在做什么 | 固化执行计划，并把 PR #1 放回 PR0、PR1 Exit Gate 下审查 |
| 为什么停在这里 | PR #1 在计划采纳前创建，合并了 PR0 边界修正和部分 PR1 Rules Prototype 工作，不能追溯声明为按计划分支执行 |
| 已经固定什么 | 计划原文、PR 顺序、当前授权、停止点、偏差记录和 PR 报告字段 |
| 现有证据支持什么 | 支持“计划已经前瞻生效，下一动作只限 PR0/PR1 审查” |
| 尚未解决什么 | PR0、PR1 的完整 Exit Gate，PR #1 的人工处置，以及 PR1 的科学批准 |

## 当前授权

| 阶段 | 状态 | 当前处理 |
| --- | --- | --- |
| PR0 Baseline Boundary Normalization | 合并在开放 PR #1 中，尚未按 Exit Gate 完整审查 | 只读核对并记录缺口 |
| PR1 Rules Prototype v1 | 部分实现在开放 PR #1 中，尚未按 Exit Gate 完整审查 | 生成统一审查包，交给人工决定 |
| PR2 至 PR8 | `NOT_AUTHORIZED` | 不建分支，不改代码，不运行对应实验 |

允许的下一动作只有以下四项。

1. 对照计划核对 PR #1 的 diff、产物和验证记录。
2. 分别给 PR0、PR1 的 Exit Gate 标记 `PASS`、`PARTIAL`、`FAIL` 或 `DEVIATION`。
3. 列出缺失产物、已知风险和可选人工处置。
4. 提交审查包，停下等待项目负责人决定。

未经新的直接授权，不得自动拆分、关闭、合并、替换或强推 PR #1，也不得开始 PR2。

## 已登记的历史偏差

`DA-DEV-20260825-001` 记录了一项事实。PR #1 早于本计划，分支 `codex/rules-prototype-v1` 同时包含 PR0 生命周期与 baseline 调整，以及部分 PR1 Rules Prototype。该记录保存真实历史，不替代 Exit Gate，也不预先选择接受、补齐、拆分或关闭方案。

## 已知未闭合项

PR0 目前至少需要核对以下三项。

- `config/operators.json` 是否明确标为 `LEGACY_FIXTURE_ONLY`；
- 是否有正式 PR0 Exit Gate 报告；
- 合并分支与计划要求的独立 PR0 分支之间如何处置。

PR1 目前至少需要核对以下七项。

- 计划指定的目录布局；
- coverage gap register；
- 显式 rule-family overlay；
- missing-evidence fixture；
- wrong-target fixture；
- `RULES_PROTOTYPE_V1_REVIEW_PACKET.md`；
- 人工科学审查与批准。

这些条目是待审查清单，不等于最终失败判定。最终状态以审查包中的文件证据和人工处置为准。

## 状态归属与优先级

- 控制计划见 [DA-HARNESS-FROZEN-PLAN-v1.0](DA_HARNESS_FROZEN_EXECUTION_PLAN_V1_0_ZH.md)
- 机器可读计划状态见 [frozen_execution_plan_v1_0.json](../governance/frozen_execution_plan_v1_0.json)
- 机器可读当前执行点见 [current_execution_status.json](../governance/current_execution_status.json)
- 追加式偏差记录见 [deviations.jsonl](../governance/deviations.jsonl)
- 项目唯一 live status 见 [DYNAMICS_ATLAS_STATUS.md](../../autoresearch/DYNAMICS_ATLAS_STATUS.md)

新的直接用户指令、项目永久边界和 live Status 中已登记的人工决定优先于本计划。设计说明和任务笔记只能补充实现细节，不能自行扩大授权。
