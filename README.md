# dynamics-atlas-harness

## Current execution status

当前仓库状态、当前授权和下一允许动作以
[仓库执行状态快照](docs/CURRENT_EXECUTION_STATUS_ZH.md) 与
[机器可读快照](governance/current_execution_status.json) 为准。

PR #19 已作为两个 bounded baseline 合并到 main（merge commit
`da584173ee64bfad9854132a3418ed1e871c69f5`）：

- `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE`
- `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`

当前 development branch 又完成了一个更窄但因果闭合的 milestone：
`LIVE_AGENT_DECISION_CLOSURE_V1_COMPLETE`。它使用
`RECORDED_PROFILE_LIVE_PLANNER`，没有把 recorded X-EISD profile 伪称为 live Profiler success。真实
`openai/gpt-5.6-luna` Planner 在 card-present 臂选择唯一的 exact allowlisted lookup；确定性代码随后执行
lookup、验证 EvidenceResult，并使目标 RuleInstance
`F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_random_candidate_pool`
从 `UNRESOLVED` 变为 `PASS`。现有 Stage-2 reducer 生成
`ABSTAIN_OR_HUMAN_REVIEW` ConclusionPacket。相同冻结状态的 card-removed 臂由 Luna 返回
`ABSTAIN_NO_ACTION`，lookup、operator 和 evidence action 均为 0，目标 Rule 保持 `UNRESOLVED`，reducer 同样
生成 `ABSTAIN_OR_HUMAN_REVIEW`。

本轮共发生 3 次 HTTP attempt：第一次在生成前因 OpenAI strict-schema 不接受 `uniqueItems` 返回 HTTP 400，
没有 response ID、usage 或 provider-reported cost；一次 schema-only compatibility repair 没有修改冻结 prompt
及其语义。之后两个 paired arms 均完成，completed-call provider-reported cost 合计 USD 0.00072385。
Campaign 已关闭并冻结，不会继续调用模型。获准的 key 由本机 Excel Benchmark secret loader 只注入进程环境，
没有打印、记录、hash、持久化或提交。

这个结果证明一条 real-model Planner decision 已与 exact evidence、same-Rule transition 和现有 reducer 接成同一条
development-only 因果链。它不证明 full live Profiler、四类 common flows 都有 Agent 参与、Agent value、source-
science approval、scientific SUPPORT、transfer 或 held-out behavior。H1 继续保持
`PENDING_DOMAIN_REVIEW`。完整记录见
[LIVE_AGENT_DECISION_CLOSURE_V1.md](docs/LIVE_AGENT_DECISION_CLOSURE_V1.md)；PR #19 的 bounded baseline 记录仍见
[LIVE_AGENT_COMMON_FLOWS_V1.md](docs/LIVE_AGENT_COMMON_FLOWS_V1.md)，PR #18 记录见
[ENGINEERING_V1_COMPLETION.md](docs/ENGINEERING_V1_COMPLETION.md)。

## Canonical development path

`run-agent-case` 仍是 HSP90/static-ADK public-case 主入口。默认模式是 recorded replay，不读凭据、不联网，也不计算
public-case terminal scientific state：

```bash
dynamics-atlas run-agent-case \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-recorded

dynamics-atlas run-agent-case \
  --case-id ADK_EXPOSED_PORTABILITY_V1 \
  --output-dir /tmp/dynamics-atlas-adk-recorded
```

只有显式指定 `--agent-mode live-openrouter` 才会进入 OpenRouter 路径。PR #19 的 exact campaign 已关闭，
因此提交配置会在读取 credential 或联网前拒绝。下面只展示新一轮获得明确授权后使用的接口：

```bash
dynamics-atlas run-agent-case \
  --agent-mode live-openrouter \
  --campaign-config /path/to/authorized-campaign.json \
  --model-profile minimax \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-live
```

PR #19 campaign 的关闭状态由 config 中的 campaign ID、completion receipt path/hash、closed state 与 receipt
中的实际调用/费用总计绑定。新的空输出目录不会解锁它：

```bash
dynamics-atlas run-agent-campaign \
  --campaign-config /path/to/authorized-campaign.json \
  --output-dir /tmp/dynamics-atlas-live-campaign
```

四类 common flow 与三态 reducer 使用现有 X-EISD、exact HSP90 control 和 Stage-2 assets；该命令不调用
Agent：

```bash
dynamics-atlas run-scenario-suite \
  --output-dir /tmp/dynamics-atlas-common-flows
```

本轮 decision-closure 的 canonical interface 是 `run-agent-decision-closure`。它运行 paired card-present /
card-removed arms，模型只提交 Planner proposal；exact lookup、authorization、Rule reevaluation 和 reducer 均由
确定性代码执行。提交的 campaign 已关闭，所以当前配置会在读取 credential 和联网前 fail closed。只有新的明确
授权、独立 config 与 ledger 才能重新调用：

```bash
dynamics-atlas run-agent-decision-closure \
  --campaign-config /path/to/new-authorized-decision-closure-campaign.json \
  --output-dir /tmp/dynamics-atlas-live-decision-closure
```

`build_case_view(case_or_run_root)` 可以读取 recorded 或 live `run-agent-case` root，也可以读取 committed
capsule case root。它会重验 model-visible input、strict schema、provider-only routing、request、raw response、
usage/cost receipt、proposal envelope、authorization、EvidenceResult 和 same-Rule links；required artifact
缺失、malformed、cross-case、stale 或跨调用拼接会 fail closed。

本轮 frozen completion receipt 与 paired matrix 位于：

```text
evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/
  live_agent_decision_closure_manifest_v1.json
  paired_arm_matrix.json
```

把正向执行臂和 paired stop 臂接入同一个静态 workbench：

```bash
dynamics-atlas build-workbench \
  --status governance/current_execution_status.json \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_PRESENT \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_REMOVED \
  --output-dir /tmp/dynamics-atlas-decision-closure-workbench
```

Committed snapshot 位于
[review/live_agent_decision_closure_v1/index.html](review/live_agent_decision_closure_v1/index.html)。页面并列显示
两臂的 live model/provider、usage/cost、Planner proposal、authorization、EvidenceResult、same-Rule transition 和
ConclusionPacket。它只读，不执行模型、lookup、Operator 或 scientific-state mutation。

## Source-science review workspace

Delivery A 把现有窄范围 F01/F02/F03/F04/F06 evidence packet、当前 binding／contract／policy
和 HSP90／ADK application 放入一个只读审查工作台。审查者可从
[`review/source_science_v1/README.md`](review/source_science_v1/README.md) 开始，检查 primary
passage 或 case-bound artifact，再在空白表单中记录具名、日期和 disposition。F04R02 的 deterministic
engineering identity mapping 已接通 dossier、manifest、overlay、binding、contract、policy、receipt、
EvidenceResult、RuleResult 和 ConclusionPacket；official disposition 仍待具名 reviewer。旧
`HSP90-TIME-ANATOMY-CONTRACT-V1` 只作为 `runtime_authority=NONE` 的待决 legacy alias 保留。

下面的命令会从提交的 repository artifacts 重建 source-science workspace，并把上面两个 fresh
run root 接入同一个静态页面：

```bash
PYTHONPATH=src python scripts/build_source_science_review_workspace_v1.py \
  --output-dir review/source_science_v1

PYTHONPATH=src python scripts/render_review_console_v0.py \
  --status governance/current_execution_status.json \
  --case-root /tmp/dynamics-atlas-hsp90-engineering-v1 \
  --case-root /tmp/dynamics-atlas-adk-engineering-v1 \
  --review-workspace review/source_science_v1 \
  --output-dir review_console

python3 -m http.server 8000 --directory review_console
```

`--case-root` 可以重复传入任何 CaseView-compatible committed capsule case 或 fresh `run-case`
root；不传时仍可通过 `--capsule-root` 使用原有的 capsule directory discovery。

随后打开 `http://127.0.0.1:8000/`。页面包含 Case Overview、Source → Rule → Evidence Trace、
Conclusion and Provenance、Human Review 四个主视图；不调用模型、Operator、API 或数据库，也不会
写回 Rule、threshold 或 source-science disposition。H1 advisory 与空白 official review template
分开显示；F04 official source-science disposition 仍是 `DATA_INSUFFICIENT`。

## Runnable reference demo

在新的或空的输出目录中，下面的命令会从仓库冻结输入重新运行 X-EISD A1/A2/A3、HSP90 B1，随后
生成四份 development Stage-2 ConclusionPacket、manifest、summary 和简短报告：

```bash
python -m dynamics_atlas_harness run-demo --output-dir /tmp/dynamics-atlas-demo
```

安装为 editable package 后，同一命令也可以写成：

```bash
dynamics-atlas run-demo --output-dir /tmp/dynamics-atlas-demo
```

输出只写入指定目录，不访问网络、不调用模型、不读取凭据，也不会修改 tracked repository files。
它复现的是两个 exposed development cases 的受限工程行为；F01/F02/F03/F04/F06 的具名
source-science review 仍然是当前科学 gate。

## Paper question → human review smoke test

下面的命令把现有 Lincoff X-EISD paper-derived development question 接到一条可复现的受限流程：
recorded answer-blind Planner card selection → deterministic admission → exact review-derivative attestation /
direct evaluation → Stage-2 packet → human decision packet。它同时重跑既有 HSP90 case-bound Operator
route，验证 Operator receipt、EvidenceResult 和同一 RuleInstance 的重评能出现在同一输出树中：

```bash
dynamics-atlas run-smoke --output-dir /tmp/dynamics-atlas-smoke
```

输出中的 `human_decision_packet.json` 会保留原始 paper question、已选 route、fresh evidence receipts、
claim ceiling 和具名 source-science review 所需的问题。当前两个 case 都正确停在
`ABSTAIN_OR_HUMAN_REVIEW`；它们不产生 scientific support。该 smoke 使用提交的历史 Planner selection，
不调用 live model、不解析 paper 全文，也不把 local review derivative 当成 source-science approval。
它只执行已验证绑定的 X-EISD A1 和 HSP90 B1；runnable reference demo 中的 X-EISD A2/A3
场景不会作为这个 smoke 的隐式副作用运行。

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
