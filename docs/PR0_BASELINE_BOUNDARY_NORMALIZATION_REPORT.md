# Harness baseline 与 Operator lifecycle 修正报告

本次工作把 baseline 和 Operator lifecycle 从原合并 PR 中单独取出。它修正会误导 routing 的命名与状态，不改变 Rules runtime、科学结果或 case obligations。focused test 已通过，X-EISD 仍为 59 obligations、15 unresolved inputs 和 16 blocked gaps。

| 读者需要先知道什么 | 当前答案 |
| --- | --- |
| 本次检查什么 | 当前 baseline 是否准确命名，哪些 Operator 可以进入 case routing |
| 为什么先做 | 原 PR 把安全修正和未批准的 Rules proposal 放在一起，无法独立审查 |
| 做了什么 | 隔离 PR0，统一 Operator lifecycle，标记旧 fixture registry，改为 canary opt-in，补 focused tests |
| 结果支持什么 | 支持 control-plane smoke 的命名和 `ROSTER_PASS + routable=true` routing gate |
| 还没有解决什么 | Rules Prototype、真实 Rule 到 Operator 路径、semantic correctness 和科学批准 |

## PR0 改动

- baseline 名称改为 `harness-control-plane-smoke-v0.2`
- README 第一屏分开 `CURRENT OBSERVED` 和 `TARGET ARCHITECTURE`
- HSP90 状态改为 `CANARY_PASS / routable=false`
- MDAnalysis projection 保持 `REGISTERED_BLOCKED / routable=false`
- case routing 只接受 `ROSTER_PASS / routable=true`
- `config/operators.json` 标记为 `LEGACY_FIXTURE_ONLY`，只供旧 `run-fixture` 路径使用
- `run-prototype` 默认不运行独立 canary
- Operator 注册文档与当前 smoke 边界同步

## Exit Gate

| 要求 | 结果 | 证据 |
| --- | --- | --- |
| Operator lifecycle 统一 | `PASS` | `config/registered_operators.json` |
| HSP90 canary 不可路由 | `PASS` | status 和 routable 双 gate 加 behavioral test |
| blocked Operator 不可路由 | `PASS` | behavioral subtests |
| 只有 `ROSTER_PASS / routable=true` 可路由 | `PASS` | positive routing subtest |
| legacy fixture registry 与目标 registry 分开 | `PASS` | `registry_role=LEGACY_FIXTURE_ONLY` |
| canary 仍可显式运行 | `PASS` | workspace integration test 显式传入 canary ID |
| canary 默认不运行 | `PASS` | CLI parser test |
| X-EISD baseline 不变 | `PASS` | 59 obligations、15 unresolved inputs、16 blocked gaps、0 routed case Operators |

本批次运行一个 focused unittest invocation，共 6 项，结果为 6/6 PASS。workspace-dependent selector、MDAnalysis runtime probe 和 HSP90 canary tests 在本机资产可用，因此没有 skip。

## 保持不变的资产

- `rules_prototype/v1` 未进入本分支
- 上游 33 条 Rule Registry、17 条 baseline bindings、2 条 modality-repair injections 和 v0.3 compiled index 未改
- X-EISD CaseGraph、selector、historical runs 和脱敏 evidence 未改
- HSP90 inputs、分析脚本、参数、output contract 和科学结论未改
- MDAnalysis 没有安装或执行

## Claim boundary

本次结果允许表述为 baseline 与 Operator routing boundary 已在一个本地 development workspace 中通过 focused checks。它不支持 Operator roster 已完成、HSP90 解决了 X-EISD gaps、Rules Prototype 已冻结、scientific correctness 已建立，或 Frozen Plan 的后续阶段已经获批。

## 下一人工 gate

PR0 需要独立审查和 merge decision。PR1 现在不适合开始。原 Rules proposal 的 source、scope、schema、policy、Human Gate、behavioral fixture 和 review packet 问题已经保存在任务修复清单中；只有 PR0 获批并合并后，才能从最新 `main` 创建修订 PR1。

