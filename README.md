# dynamics-atlas-harness

## Current execution status

当前仓库状态、当前授权和下一允许动作以
[仓库执行状态快照](docs/CURRENT_EXECUTION_STATUS_ZH.md) 与
[机器可读快照](governance/current_execution_status.json) 为准。PR #19 的准确交付状态是：

- `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE`
- `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`
- `LIVE_AGENT_DECISION_CLOSURE_NOT_YET_ESTABLISHED`

真实模型和 common-flow suite 是两套并列证据。真实路径只覆盖 HSP90 的 proposal transport 与描述性 action；
direct evaluation、narrow lookup、registered computation 和 explicit stop 六个场景全部是
`NO_AGENT_DETERMINISTIC_SCENARIO`，不构成 live-Agent common-flow coverage。三态 reducer 的 SUPPORT 只来自
明确标记的 synthetic contract fixture。

真实 OpenRouter development campaign 共发出 17 次 HTTP 请求，其中 13 次完成并计入调用上限，累计费用为
USD 0.145264010。其余 4 次在 provider HTTP 400 前失败，未完成、未计费。获准的 key 从
本机 Excel Benchmark secret location 安全注入当前进程环境，没有打印、记录或持久化。Campaign 在取得
第一条完整 HSP90 chain 后自适应停止，没有为了填满上限继续跑到 16 次。

这条真实链使用冻结的 HSP90 MiniMax Profiler proposal 和 StreamLake 提供的 MiniMax M2.5 Planner
proposal。Profiler 为 `CORE_ADMISSION_PASS`，完整 field-annotation envelope 为
`FULL_ANNOTATION_ENVELOPE_FAIL`，错误为 `UNKNOWN_STATUS_CORE_VALUE_MISMATCH`。Planner 面对的决策面是
`ONE_LEGAL_CARD_VERSUS_ABSTAIN`，因此只证明 schema-constrained selection，不证明 nontrivial route selection。
授权后的 EvidenceResult 属于 `DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT`；same-Rule transition count 为 0，
ConclusionPacket 未计算，terminal state 为 `NOT_CALCULATED_BY_CASE_RUNNER / NOT_EVALUATED`。

H1 继续保持 `PENDING_DOMAIN_REVIEW`。Public HSP90 broad Rule closure、runner-generated public-case
ConclusionPacket、ADK dynamics portability 和 held-out evaluation 仍未完成。精确 delivery SHA、merge state
与 GitHub PR merge-ref CI 由 Draft PR metadata 记录，不写入会自我失效的 tracked status。

PR #18 的 recorded-replay evidence execution and inspection path 仍是当前 live-capable 路径的确定性基线。

这些 development artifacts 不构成 full Profiler grounding、nontrivial Planner utility、live-Agent decision
closure、source-science approval、transfer、Agent value 或 production readiness。完整的工程行为、blocker 与复现记录见
[LIVE_AGENT_COMMON_FLOWS_V1.md](docs/LIVE_AGENT_COMMON_FLOWS_V1.md)。旧的
[ENGINEERING_V1_COMPLETION.md](docs/ENGINEERING_V1_COMPLETION.md) 仍保留为 PR #18 工程基线记录。

## Canonical development path

`run-agent-case` 是当前主入口。默认模式仍是 recorded replay，不读凭据、不联网，也不计算 public-case
terminal scientific state：

```bash
dynamics-atlas run-agent-case \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-recorded

dynamics-atlas run-agent-case \
  --case-id ADK_EXPOSED_PORTABILITY_V1 \
  --output-dir /tmp/dynamics-atlas-adk-recorded
```

只有显式指定 `--agent-mode live-openrouter` 才会进入 OpenRouter 路径。单案例命令受所选 campaign config
中的预算、completed-call 上限和独立本地 ledger 共同约束。本轮 exact campaign 已关闭，因此当前配置下的 live 命令会在读取
credential 或联网前返回 `LIVE_AGENT_CAMPAIGN_CLOSED_REQUIRES_NEW_AUTHORIZATION`。下例只说明新一轮经过明确
授权后所使用的接口；它不是重开本轮 campaign 的命令：

```bash
dynamics-atlas run-agent-case \
  --agent-mode live-openrouter \
  --campaign-config /path/to/authorized-campaign.json \
  --model-profile minimax \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-live
```

本轮历史配置最多 16 个 completed calls，并在第 13 次 completed call 后取得第一条 proposal-to-descriptive-
action success，随后关闭并冻结。关闭状态由 config 中的 campaign ID、completion receipt path/hash、closed
state 与 receipt 中的实际调用/费用总计绑定；不再由产品源码中的某个调用数或费用常量决定。新的空输出目录
本身不会解锁它；下面的命令只有在新授权、独立 campaign 配置与独立预算账本同时存在时才能启动另一轮：

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

`build_case_view(case_or_run_root)` 可以读取 recorded 或 live `run-agent-case` root，也可以读取 committed
capsule case root。它会重验 model-visible input、strict schema、provider-only routing、request、raw response、
usage/cost receipt、proposal envelope、authorization、EvidenceResult 和 same-Rule links；required artifact
缺失、malformed、cross-case、stale 或跨调用拼接会 fail closed。

本轮聚合 completion receipt 与逐调用 development matrix 位于：

```text
evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/
  live_agent_campaign_manifest.json
  live_agent_development_matrix.json
```

把同一 HSP90 case 的 recorded replay、实际 live proposal-to-descriptive-action path 和独立 scenario matrix
接入同一个静态 workbench：

```bash
dynamics-atlas build-workbench \
  --status governance/current_execution_status.json \
  --artifact-root evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_live_20260830/recorded_replay/hsp90 \
  --artifact-root evidence/live_agent_common_flows_v1/development_runs/authorized_planner_from_frozen_hsp90_minimax_repair1_20260830/trial-1 \
  --scenario-matrix evidence/common_flow_scenarios_v1/development_runs/common_flow_scenarios_v1/common_flow_matrix.json \
  --output-dir /tmp/dynamics-atlas-workbench
```

Committed snapshot 位于
[review/live_agent_common_flows_v1/index.html](review/live_agent_common_flows_v1/index.html)。
页面并列显示 `RECORDED_PROPOSAL_REPLAY` 与 `LIVE_OPENROUTER_PROPOSAL`，同时显示 provider、usage/cost、
authorization、EvidenceResult、same-Rule transition 和 synthetic-only T1 边界。它只读，不执行模型、
Operator 或 scientific-state mutation。

## Source-science review workspace

Delivery A 把现有窄范围 F01/F02/F03/F04/F06 evidence packet、当前 binding／contract／policy
和 HSP90／ADK application 放入一个只读审查工作台。审查者可从
[`review/source_science_v1/README.md`](review/source_science_v1/README.md) 开始，检查 primary
passage 或 case-bound artifact，再在空白表单中记录具名、日期和 disposition。F04R02 的
case-bound traceability mapping 仍待人工核对。

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
分开显示；F04 仍是 `DATA_INSUFFICIENT`。

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

## Rules Prototype scenario acceptance v1

下面的命令重建八个 fixture-driven development scenarios 的 acceptance artifacts：四个 synthetic
contract fixtures（T1–T4）和四个 exposed development scenarios（T5–T8）。它复用既有受限路径，
比较实际输出与预先声明的 expected results；任何不匹配都会使命令返回非零状态，并在 matrix 中标记
对应 task 为 `FAIL`。

```bash
dynamics-atlas run-prototype-acceptance
```

T5 的 exact lookup 和 T7 的 registered Operator 只会回填各自选定的 RuleInstance。T8 是
`DESCRIPTIVE_NO_ACTIVE_RULE_CONTROL`：它保存静态描述性 evidence，但不会伪造 Rule closure。该 suite
不从任意 CaseGraph 自动选择 family、obligation 或 route，也不构成 scientific validation、coverage、
held-out transfer 或 Agent-value evidence。

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


## Pro17 后续进展（2026-09-05）

Q01科学答复与题级输出通过Pro17并冻结。Q09已修复第二轮选回旧候选的问题：真实保存结果现在只选择两个最新未完成点，0重新拟合；313本地回归通过。下一项新增题目推进Q15，已核对SI校正参数与公式，现有66文件为63DCBS+3背景、0APBS。开发题级内容完成1/20、最终人类批准0、准确率未测。


## Pro18之后的实际科学进展（2026-09-05）

Q15两个位点的140个APBS文件完成首次主计算：55/175平均效率增加0.08199、175/228减少0.02617，后者重复间差异跨零。详见research/paper_result_reproduction_screen_v1/q15_apbs_comparison_v1/。这是条件荧光分析，原Q15的换染料和正交证据仍待完成，0Rules-extra。Q09修复完整历史绑定及连续零动作文件衔接，三个已有人工背景派生点经零拟合验收，D01数值分支结束、D24较低点保留。319本地测试通过，下一轮同PR开放Pro审阅。Q01冻结，开发完整内容1/20、准确率未测。
