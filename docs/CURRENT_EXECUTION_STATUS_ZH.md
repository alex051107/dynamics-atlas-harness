# Dynamics Atlas 仓库当前执行状态

仓库内唯一机器可读的 current execution status 是
[current_execution_status.json](../governance/current_execution_status.json)。它记录当前 main、下一允许动作和
claim ceiling。人工授权与计划偏差只追加到
[deviations.jsonl](../governance/deviations.jsonl)；冻结计划仍保留在
[frozen_execution_plan_v1_0.json](../governance/frozen_execution_plan_v1_0.json)，不被重写为 live status。

当前事实：No-Agent Milestone A 已在 `main@dd189362` 通过并合并。受限的
`feature/live-agent-exposed-cases-v1` 已完成两例 exposed development case 的 answer-blind Profiler 与
proposal-only Planner 比较；离线 replay 显示安全边界通过，但低成本模型没有通过 typed capability gates，结果停在 human review。Stage 2、ADK、held-out、Rules/Operator 扩展和 scientific claim upgrade 均未授权。

创建任何分支前先读上述 JSON；需要理解为什么授权发生变化时再读 deviations 记录。
