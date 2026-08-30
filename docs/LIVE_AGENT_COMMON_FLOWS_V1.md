# Live Model Proposal Transport 与 Deterministic Common-Flow Regression v1

## Decision

当前交付由三个状态共同描述：

- `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE`
- `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`
- `LIVE_AGENT_DECISION_CLOSURE_NOT_YET_ESTABLISHED`

这轮第一次获得了真实模型参与的 proposal transport 链：冻结的 HSP90 MiniMax Profiler core proposal 进入现有
deterministic admission，fresh Rules 和 legal cards 随后生成；StreamLake 提供的 MiniMax M2.5 Planner
选择一张合法 card，deterministic authorization 放行一个描述性 action，runner 产生一个
EvidenceResult。该 evidence 没有 active Rule effect，因此 same-Rule 检查后所有 RuleResults 保持不变，
终局仍为 `NOT_CALCULATED_BY_CASE_RUNNER / NOT_EVALUATED`。

Profiler 的 core admission 通过，完整 annotation envelope 失败，错误为
`UNKNOWN_STATUS_CORE_VALUE_MISMATCH`。Planner 只面对一张 legal card 和 abstain，因此该路径不构成
nontrivial route selection。四类 common-flow 场景全部由确定性代码运行，没有 Agent 参与。真实模型路径与
common-flow regression 不能合并解释为 live-Agent common-flow completion。

整个自适应 campaign 共发出 17 次 HTTP 请求，其中 13 次完成并计入调用上限，累计实际费用为
USD 0.145264010。其余 4 次停在 provider HTTP 400，未完成、未计费。流程在获得第一条完整成功链后停止，
没有为了填满矩阵继续跑到 16 次。该 exact campaign 已关闭并冻结；持久化预算预留、跨进程累计与 closed-
campaign guard 已接入 canonical code path，不再继续追加同一 campaign 的模型调用。

## Repository identity

- Repository：`alex051107/dynamics-atlas-harness`
- Branch：`feature/live-agent-common-flows-v1`
- Exact base：`e8d4f7781590c4c0424c83dffb62f62fbe526fcf`
- Exact delivery head 由最终 Draft PR metadata 记录；tracked 文档不写入会因自身提交而失效的 final SHA
- PR #16 与 PR #17 已关闭为 superseded，未再次合并；其有效补丁已经由 PR #18 吸收

## 本轮在完整项目中的位置

项目现在同时有两条明确路径：recorded replay 是无网络默认值；显式 live mode 负责产生 Profiler 和 Planner
typed proposal。两者进入同一个 deterministic runner，不存在第二套 live scientific engine。另有一套
`NO_AGENT_DETERMINISTIC_SCENARIO` regression suite，用于复验四类 route 与三态 reducer；它不是 live 路径的
后半段。

模型只能提出 Profile 和 Planner selection。Rules、legal cards、authorization、action execution、
EvidenceResult attachment、Rule reevaluation 和 conclusion boundary 仍由确定性代码控制。

当前保留：

- 两案例 public packet、deterministic admission、fresh Rules、obligations 和 legal cards
- recorded replay 默认路径
- strict、tool-less OpenRouter proposal transport 与 provider/model receipt
- exact source lookup、exact HSP90 control 和现有 Stage-2 reducer
- artifact-only CaseView 与只读 workbench
- H1 advisory、空白 official reviewer form 和 named-review gate

历史 `run-fixture`、`run-prototype`、`run-demo`、`run-smoke`、旧 Ollama experiment 和 Profiler-only sweep
继续保留用于复现，不再是 README 主路径。本轮没有引入 Agents SDK、provider router、DAG engine、scheduler、
MCP、RAG、数据库、Agent shell、自动 Rule/Operator 创建或新 GUI framework。

## Canonical runtime path

```text
public scientific question and declared sources/data
  -> recorded or explicit live OpenRouter Profiler proposal
  -> deterministic proposal admission
  -> fresh RuleResults and unresolved obligations
  -> fresh same-case legal action cards
  -> recorded or explicit live OpenRouter Planner proposal
  -> deterministic authorization or abstention
  -> direct / exact lookup / registered computation / explicit stop
  -> EvidenceResult
  -> same-RuleInstance reevaluation
  -> existing bounded reducer where the scenario owns one
  -> CaseView
  -> static read-only workbench
  -> human scientific review
```

## Credential、调用与费用

获准的 key 来自本机 Excel Benchmark 的 secret location，并只注入当前进程继承环境。key 的值没有被打印、
记录、hash、写入 artifact 或提交；没有扫描 shell history、keychain、home directory 或无关 repository。

| Item | Observed result |
|---|---|
| Credential source | authorized local Excel Benchmark secret location → inherited environment |
| Key printed, logged, hashed, persisted or committed | No |
| HTTP attempts | 17 |
| Completed API calls | 13 |
| Provider HTTP 400 before completion | 4；未完成、未计费 |
| Campaign maximum | 16 completed calls；未跑满 |
| Actual cumulative cost | USD 0.145264010 |
| Campaign stop | adaptive stop after first proposal-to-descriptive-action success |
| Held-out access | No |
| Campaign state | closed and frozen |

最终预算 readback 为 USD 5 cap、USD 4.854735990 remaining。HTTP 400 的 Luna Planner 请求没有完成、没有计入
13 次 completed calls，也没有产生费用；另有两次初始 DeepSeek HTTP 400，故总 HTTP attempts 为 17。

本轮聚合 receipt 与逐调用 matrix 位于：

```text
evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/
  live_agent_campaign_manifest.json
  live_agent_development_matrix.json
```

## Profiler results

| Case | Model/provider | Core result | Diagnostic/result boundary |
|---|---|---|---|
| HSP90 | Luna / OpenAI，trial 1–2 | core admission PASS 两次 | annotation target diagnostic 两次失败；core proposal 未因此升级为 scientific result |
| HSP90 | MiniMax M2.5 / StreamLake | `CORE_ADMISSION_PASS` | `FULL_ANNOTATION_ENVELOPE_FAIL`；`UNKNOWN_STATUS_CORE_VALUE_MISMATCH`；冻结 core 被后续成功链复用 |
| HSP90 | Terra / OpenAI diagnostic fallback | core admission PASS | compatibility diagnostic 失败；未作为 named reviewer 或 scientific authority |
| HSP90 | DeepSeek / Sail Research | 未得到可用 core proposal | JSON/schema/provider response failures，fail closed |
| static ADK | Luna、MiniMax、Terra、DeepSeek | 全部 core fail | edge identity、core contract 或 transport/schema/provider failure；没有 ADK live route |

Profiler 的成功只表示 proposal core 可以进入 deterministic admission。当前没有 full Profiler success；
`FULL_ANNOTATION_ENVELOPE_FAIL` 被单独保留，没有倒写为 scientific authority，也没有把 UNKNOWN 补成已知事实。

## Planner results 与实际 proposal transport path

Luna Planner 两次请求都以 HTTP 400 停在 strict schema request，未形成 completed/charged call。MiniMax M2.5
经 StreamLake 返回 strict typed Planner proposal，并通过当前 legal-card schema 和 deterministic authorization。
它面对的输入是 `ONE_LEGAL_CARD_VERSUS_ABSTAIN`，所以结果为 `NOT_NONTRIVIAL_ROUTE_SELECTION`。

成功链的 canonical artifact root：

```text
evidence/live_agent_common_flows_v1/development_runs/
authorized_planner_from_frozen_hsp90_minimax_repair1_20260830/trial-1
```

该链的观察结果：

- Profiler：冻结的 core-admitted HSP90 MiniMax proposal
- Planner：live MiniMax M2.5 / StreamLake proposal
- Selection：`SELECT_ACTIONS`
- Authorized card：`HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1`
- Action count：1
- EvidenceResult：1 个 `DESCRIPTIVE_ANALYSIS_ONLY`
- Active Rule effect：`DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT`
- Rule reevaluation：`SAME_RULE_TRANSITION_COUNT_ZERO`；before 与 after 完全相同，`reevaluated_rule_instance_ids=[]`
- Terminal scientific state：`NOT_CALCULATED_BY_CASE_RUNNER`
- Scientific disposition：`NOT_EVALUATED`
- ConclusionPacket：`CONCLUSION_PACKET_NOT_CALCULATED`

这条路径证明真实 model proposal 已进入现有 deterministic workflow 并执行合法描述性 action。它没有证明
full Profiler grounding、Planner decision utility、active Rule closure 或 live-path ConclusionPacket。

## Common-flow scenario matrix

| Scenario | Agent mode | Route | Same-Rule effect | Terminal behavior | Boundary |
|---|---|---|---|---|---|
| A X-EISD A1 | `NO_AGENT_DETERMINISTIC_SCENARIO` | direct evaluation | existing RuleResults | `ABSTAIN_OR_HUMAN_REVIEW` | real repository review status retained |
| B X-EISD composition | `NO_AGENT_DETERMINISTIC_SCENARIO` | exact source lookup | target Rule `UNRESOLVED -> PASS` | `ABSTAIN_OR_HUMAN_REVIEW` | downstream dependency diffs recorded |
| C HSP90 control | `NO_AGENT_DETERMINISTIC_SCENARIO` | registered computation | exact control Rule `UNRESOLVED -> PASS` | `ABSTAIN_OR_HUMAN_REVIEW` | exact-control-only, no broad closure |
| D missing composition | `NO_AGENT_DETERMINISTIC_SCENARIO` | explicit stop | target Rule remains `UNRESOLVED` | `ABSTAIN_OR_HUMAN_REVIEW` | zero unauthorized analysis |
| T1 synthetic gate | `NO_AGENT_DETERMINISTIC_SCENARIO` | direct reducer fixture | engineering contract only | `SUPPORT_WITHIN_CEILING` | `SYNTHETIC_CONTRACT_BEHAVIOR_ONLY` |
| T2 explicit mismatch | `NO_AGENT_DETERMINISTIC_SCENARIO` | relation-blocked reducer | mismatch Rule `FAIL` | `CANNOT_SUPPORT_REQUESTED_CLAIM` | no source-local invalidation |

六个场景覆盖四种常见 route 和三种 engineering terminal state，但状态为
`NOT_LIVE_AGENT_COMMON_FLOW_COVERAGE`。T1 只证明 reducer contract；real scientific support packet 数量仍为 0。
完整 matrix 位于：

```text
evidence/common_flow_scenarios_v1/development_runs/
common_flow_scenarios_v1/common_flow_matrix.json
```

## Canonical commands

Recorded replay 是默认路径，不读取 credential 或联网：

```bash
dynamics-atlas run-agent-case \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-recorded
```

显式 live 单案例开发接口如下。本轮配置已冻结关闭，当前会在 credential 读取和网络请求前 fail closed；只有
新的明确授权、独立 campaign 配置与独立预算账本才能使用该接口开始新一轮：

```bash
dynamics-atlas run-agent-case \
  --agent-mode live-openrouter \
  --campaign-config /path/to/authorized-campaign.json \
  --model-profile minimax \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-live
```

显式 frozen-panel campaign 接口如下。上面记录的历史 exact campaign 已关闭；新的空输出目录不会绕过
closed guard，只有新的授权、独立 campaign 配置与独立预算账本才能启动另一轮：

```bash
dynamics-atlas run-agent-campaign \
  --campaign-config /path/to/authorized-campaign.json \
  --output-dir /tmp/dynamics-atlas-live-campaign
```

Deterministic common flows：

```bash
dynamics-atlas run-scenario-suite \
  --output-dir /tmp/dynamics-atlas-common-flows
```

把同一 HSP90 case 的 recorded replay、实际 live proposal-to-descriptive-action path 和独立 scenario matrix
投影到同一个只读 workbench：

```bash
dynamics-atlas build-workbench \
  --status governance/current_execution_status.json \
  --artifact-root evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_live_20260830/recorded_replay/hsp90 \
  --artifact-root evidence/live_agent_common_flows_v1/development_runs/authorized_planner_from_frozen_hsp90_minimax_repair1_20260830/trial-1 \
  --scenario-matrix evidence/common_flow_scenarios_v1/development_runs/common_flow_scenarios_v1/common_flow_matrix.json \
  --output-dir /tmp/dynamics-atlas-workbench
```

Committed snapshot 位于 `review/live_agent_common_flows_v1/index.html`。页面并列显示 recorded/live mode、
provider、usage/cost、authorization、EvidenceResult 与 unchanged same-Rule state；它只读，不执行 model、
Operator 或 scientific-state mutation。

## Artifact deduplication audit

Content-hash inventory found one complete redundant tree: the 26 files under
`authorized_campaign_20260830/recorded_replay` were byte-identical to the retained canonical tree under
`authorized_campaign_live_20260830/recorded_replay`, and no repository artifact referenced the older copy. The older
tree was removed. Its campaign-level missing-credential manifest, comparison matrix, and config snapshot remain because
they carry unique fail-closed evidence.

Byte-identical provider error bodies were retained when they belonged to distinct HTTP attempts. The frozen Profiler
copy inside the canonical successful run was also retained because the run's fail-closed CaseView binds its complete
request, response, receipt, and proposal tree. No unique model failure response was deleted.

## Validation status

本轮 completion artifacts 包含 provider/model receipts、usage、cost、latency、request/raw-response hashes、
deterministic admission、authorization、execution、EvidenceResult 和 CaseView-readable run manifest。PR #19
repair 后的本地 targeted check 已验证 closed guard 在 credential 前拒绝、completion receipt 的
config/hash/totals 绑定，以及 workbench 的准确边界显示，共 3 项通过。静态 Python/JSON parse 也通过。

当前主机的系统 Python 缺少仓库已声明的 `pymbar` dependency；本轮没有擅自安装依赖，因此依赖完整科学栈的
本地 focused/full run 未被伪报为完成。Exact-head Python 3.11/3.12 full suite、common-flow regression 与 clean-
checkout install 由提交后的 GitHub PR metadata 记录。旧 head 的通过结果不能替代 repair head 的 CI。

## Scientific authority and claim ceiling

H1 保持 `PENDING_DOMAIN_REVIEW`。Public HSP90 与 static ADK runner 仍保持
`NOT_CALCULATED_BY_CASE_RUNNER`。Exact HSP90 computation 只覆盖 exact control Rule，scenario T1 的 SUPPORT
只属于 synthetic engineering contract。

本批次允许的 claim：真实 OpenRouter model proposal 已安全进入一次 HSP90 development runtime 并触发一个
合法描述性 action；仓库另有四类 deterministic route 与三态 reducer regression suite，并记录完整
provenance/cost receipt 和只读 workbench。

本批次禁止升级为：live Agent 已覆盖四类 common flows、完整 Profiler evidence-grounding contract 已通过、
Planner 展示了有意义的多路线决策、真实 Agent 路径关闭了 Rule 或生成 ConclusionPacket、Agent value 已建立、
模型正确理解论文、HSP90 broad Rule 已关闭、public scientific SUPPORT、ADK dynamics portability、general
case coverage、transfer、held-out 或 production readiness。

## Remaining work

1. 当前 13-call campaign 保持关闭，不新增 API call。
2. 下一工程 milestone 为 `LIVE_AGENT_DECISION_CLOSURE_V1`：一条真实 Planner evidence action 使同一
   RuleInstance `UNRESOLVED -> PASS`，existing reducer 生成 bounded ConclusionPacket；配对 stop arm 必须零执行。
3. 具名 H1 reviewer 检查 primary passages，填写 official dispositions。
4. F04R02 只解决可由标识符确定的 engineering traceability；科学解释继续由具名 reviewer 决定。
