# dynamics-atlas-harness

## Current execution status

当前仓库状态、当前授权和下一允许动作以
[仓库执行状态快照](docs/CURRENT_EXECUTION_STATUS_ZH.md) 与
[机器可读快照](governance/current_execution_status.json) 为准。它们记录的当前状态是：两个
exposed development case 的 case-bound no-Agent routes 和最小 Stage-2 packets 已合并；Agent
diagnostic 仍是 capability-rejected baseline；当前下一步是具名 F01/F02/F03/F04/F06
source-science review。

这些 development artifacts 不构成 source-science approval、通用 runtime、transfer、Agent value 或
production readiness。下面的 initial control-plane smoke 是历史基线，不是当前执行状态。

## Historical initial control-plane smoke v0.2

该历史基线真实调用已有 v0.3 selector，在 exposed X-EISD development case 上产生 59 个
obligations、15 个 selector unresolved inputs 和 16 个 gaps。case RunPlan 没有匹配到可路由
Operator，因此正确停在 `RUN_PLAN_BLOCKED`。独立 HSP90 canary 可以显式运行，但不属于该 case
route。

这份历史证据只支持早期控制面接线和停止行为；它不覆盖后续已合并的 case-bound route、Stage-2
packets 或当前 source-science gate。

## TARGET ARCHITECTURE

目标架构把 rich CaseGraph、Rules Table selector、Evaluation Contract、持久 RunPlan 和 registered Operator 接成一条可审计的数据流。目标路径如下：

```text
Question + Papers + Data
  → Profile Agent proposal
  → deterministic CaseGraph admission
  → existing v0.3 Rules selector
  → Evaluation Contract
  → direct bounded result OR persistent RunPlan
  → registered operator
  → EvidenceResult
  → human review / abstain
```

模型只提出 CaseGraph。它不能选择 Rule、授权 Operator、读取 reference answer 或给出最终科学 verdict。当前 smoke 尚未完成这条目标路径中的真实 case resolution。

## 当前实跑结果

本地 `runs/target_architecture_v0_2_20260825/` 保存完整 trace，但该目录包含本机路径和 scientific payload，不进入 Git。仓库只保留脱敏后的 `evidence/target_architecture_v0_2/`：

- rich X-EISD CaseGraph 通过 `PROFILE_READY`；
- 现有 v0.3 compiled rule index 与 selector 被真实调用，产生 59 个 obligations 和 15 个 unresolved inputs；
- 当前 bundle 缺少 59 个 obligation 的显式 EvaluationResults，因此 Evaluation Contract 走 `RUN_PLAN_REQUIRED`；
- RunPlan 持久化了 16 个 gap，但没有与 X-EISD gaps 匹配的 registered operator，所以 case route 为 `RUN_PLAN_BLOCKED`；
- `hsp90.directional_time_anatomy.v0` 作为独立 registry canary 成功执行。它证明 operator adapter 可运行，不代表它解决了 X-EISD gaps；
- semantic correctness、cross-paper transfer、Agent value 和 production readiness 均为 `NOT_EVALUATED`。

这个 blocked route 是有效结果：它把下一步定位为 gap classification、source lookup、rule-specific EvaluationResults 和合法 capability routing，而不是让模型临时发明分析步骤。

## Profile Agent

Profile Prompt 位于 `prompts/profile_case_v1.md`。当前 `RecordedCaseGraphProvider` 用已有 rich CaseGraph 重放同一个接口；未来廉价模型只需实现 `ProfileProvider.propose_profile()`。

Profile proposal 使用既有 `protein-dynamics-metadata/v0.3-development` contract。deterministic admission 会执行 JSON Schema、answer isolation、source ID 和 EvidenceEdge endpoint 检查。通过后，proposal 才能进入 selector。

## Rules Table 接入

Rules 的 authoring truth 仍在上游原路径。仓库中的 `config/workspace_assets.json` 只保存 read-only references：

- 33-row frozen Rule Registry；
- 17 个 baseline bindings 加 2 个 modality-repair injections；
- v0.3 compiled rule index；
- existing typed selector；
- protein-dynamics method scope；
- rich development CaseGraph。

Harness 不复制、不改写这些资产。`workspace.py` 以固定参数调用现有 selector，并保存 native receipt 和 adapter receipt。

Typed binding 的作用不是再建一张规则表。它把人类可读 Rule row 编译成可执行的 `scope + predicate + required fields + claim scope + gap checks`。Rule row 保存科学来源和边界；binding 保存机器何时实例化它。详见 `docs/RULES_TABLE_AND_TYPED_BINDINGS_ZH.md`。

## Registered operators

目标 registry 位于 `config/registered_operators.json`。每个 OperatorSpec 至少冻结：

- `skill_ref` 或已有分析来源；
- implementation 与 backend/runtime；
- fixed inputs 和 parameters；
- input/output contract；
- route match；
- claim ceiling 与 forbidden claims；
- runtime probe 和 canary receipt。

当前有两个明确状态：

| operator | 状态 | 说明 |
|---|---|---|
| `hsp90.directional_time_anatomy.v0` | `CANARY_PASS / NOT_ROUTABLE` | 复用现有标准库脚本、冻结输入和 `[5,20,50]` persistence grid；完整 output schema 和 case/input binding 未完成 |
| `trajectory.structural_state_projection.v1` | `REGISTERED_BLOCKED` | spec 来自 installed `molecular-dynamics` skill 与 AdK 旧分析；当前 runtime 无 MDAnalysis，且新 case 的 input/mapping/method profile 未冻结 |

Skill 是程序性知识和 OperatorSpec 的来源，不等于 backend 已安装。Operator runtime 必须单独 probe。完整注册规则见 `docs/OPERATOR_REGISTRATION_ZH.md`。

## 本地运行

从 repo 根目录运行现有 workspace integration：

```bash
PYTHONPATH=src python3 -m dynamics_atlas_harness run-prototype \
  --workspace-root "/path/to/Soojung-Dynamic data" \
  --output-dir /tmp/dynamics-atlas-target-run \
  --run-id example-target-run
```

上面的默认命令不会运行独立 canary。只有显式添加以下参数才会执行 HSP90 canary：

```text
--canary-operator-id hsp90.directional_time_anatomy.v0
```

显式 canary 仍不会成为 case RunPlan node，也不会关闭 X-EISD gaps。

运行测试：

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

旧的 `run-fixture` 命令和 v0.1 fixture registry 保留为 Milestone 0 回归，不再代表目标架构。

## 暂不实现

- DataFlow-Harness 风格的 Request–Validate–Commit transaction；
- SQLite、LangGraph、FastAPI、WebUI、RAG 或通用 tool knowledge graph；
- 模型自动注册 operator 或修改 Rules；
- 任意 shell/Python 执行；
- semantic-correctness benchmark、最终科学 verdict、held-out/transfer 或 Agent-value claim。

这些功能只有在当前 trace 暴露重复需求后才进入设计。目标架构和当前边界见 `docs/TARGET_ARCHITECTURE_ZH.md`。

## Frozen baseline 与 PR 约定

- 当前 baseline 的范围、非版本化资产和 claim boundary 见 `BASELINE.md`；
- 上游 Rules、selector、CaseGraph 和 HSP90 inputs 的冻结身份见 `config/frozen_assets_v0_1.json`；
- 初始 baseline 进入 `main` 后，后续修改一律从新分支提交 Pull Request；
- PR 的最小检查和科学边界见 `CONTRIBUTING.md`。
