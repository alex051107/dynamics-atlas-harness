# Live Agent 与常见流程覆盖 v1

## Decision

Decision 为 `ACTUAL_LIVE_FULL_CHAIN_OBSERVED_CAMPAIGN_CLOSED_FROZEN`。

这轮第一次获得了真实模型参与的完整开发链：冻结的 HSP90 MiniMax Profiler core proposal 进入现有
deterministic admission，fresh Rules 和 legal cards 随后生成；StreamLake 提供的 MiniMax M2.5 Planner
选择一张合法 card，deterministic authorization 放行一个描述性 action，runner 产生一个
EvidenceResult。该 evidence 没有 active Rule effect，因此 same-Rule 检查后所有 RuleResults 保持不变，
终局仍为 `NOT_CALCULATED_BY_CASE_RUNNER / NOT_EVALUATED`。

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
typed proposal。两者进入同一个 deterministic runner，不存在第二套 live scientific engine。

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
| Campaign stop | adaptive stop after first full-chain success |
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
| HSP90 | MiniMax M2.5 / StreamLake | bounded repair 后 core admission PASS | annotation sidecar 仍有 diagnostic mismatch；冻结的 core proposal 被后续成功链复用 |
| HSP90 | Terra / OpenAI diagnostic fallback | core admission PASS | compatibility diagnostic 失败；未作为 named reviewer 或 scientific authority |
| HSP90 | DeepSeek / Sail Research | 未得到可用 core proposal | JSON/schema/provider response failures，fail closed |
| static ADK | Luna、MiniMax、Terra、DeepSeek | 全部 core fail | edge identity、core contract 或 transport/schema/provider failure；没有 ADK live route |

Profiler 的成功只表示 proposal core 可以进入 deterministic admission。annotation sidecar 的失败被单独保留，
没有倒写为 core scientific authority，也没有把 UNKNOWN 补成已知事实。

## Planner results 与实际 full chain

Luna Planner 两次请求都以 HTTP 400 停在 strict schema request，未形成 completed/charged call。MiniMax M2.5
经 StreamLake 返回 strict typed Planner proposal，并通过当前 legal-card schema 和 deterministic authorization。

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
- Active Rule effect：0
- Rule reevaluation：before 与 after 完全相同，`reevaluated_rule_instance_ids=[]`
- Terminal scientific state：`NOT_CALCULATED_BY_CASE_RUNNER`
- Scientific disposition：`NOT_EVALUATED`

这条路径证明真实 model proposal 已进入现有 deterministic workflow 并执行合法 action。它没有证明模型理解
论文、没有关闭 broad Rule，也没有生成 public-case scientific ConclusionPacket。

## Common-flow scenario matrix

| Scenario | Route | Same-Rule effect | Terminal behavior | Boundary |
|---|---|---|---|---|
| A X-EISD A1 | direct evaluation | existing RuleResults | `ABSTAIN_OR_HUMAN_REVIEW` | real repository review status retained |
| B X-EISD composition | exact source lookup | target Rule `UNRESOLVED -> PASS` | `ABSTAIN_OR_HUMAN_REVIEW` | downstream dependency diffs recorded |
| C HSP90 control | registered computation | exact control Rule `UNRESOLVED -> PASS` | `ABSTAIN_OR_HUMAN_REVIEW` | exact-control-only, no broad closure |
| D missing composition | explicit stop | target Rule remains `UNRESOLVED` | `ABSTAIN_OR_HUMAN_REVIEW` | zero unauthorized analysis |
| T1 synthetic gate | direct reducer fixture | engineering contract only | `SUPPORT_WITHIN_CEILING` | `SYNTHETIC_CONTRACT_BEHAVIOR_ONLY` |
| T2 explicit mismatch | relation-blocked reducer | mismatch Rule `FAIL` | `CANNOT_SUPPORT_REQUESTED_CLAIM` | no source-local invalidation |

六个场景覆盖四种常见 route 和三种 engineering terminal state。T1 只证明 reducer contract；real scientific
support packet 数量仍为 0。完整 matrix 位于：

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
  --model-profile minimax \
  --budget-usd 5.00 \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-live
```

显式 frozen-panel campaign 接口如下。上面记录的 13-call exact campaign 已关闭；新的空输出目录不会绕过
closed guard，只有新的授权、独立 campaign 配置与独立预算账本才能启动另一轮：

```bash
dynamics-atlas run-agent-campaign \
  --output-dir /tmp/dynamics-atlas-live-campaign
```

Deterministic common flows：

```bash
dynamics-atlas run-scenario-suite \
  --output-dir /tmp/dynamics-atlas-common-flows
```

把同一 HSP90 case 的 recorded replay、实际 live full chain 和 scenario matrix 投影到同一个只读 workbench：

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

## Validation status

本轮 completion artifacts 包含 provider/model receipts、usage、cost、latency、request/raw-response hashes、
deterministic admission、authorization、execution、EvidenceResult 和 CaseView-readable run manifest。最终本地
full suite 在 Python 3.11 环境发现并通过 220 tests。验证过程中先修复 2 个旧治理文案契约回归，再根据最终内部
方法审查把 closed-campaign guard 下沉到 3 个公开 runtime 入口，并把 recorded/live 对照接入同一 workbench；
相关 focused tests 通过后，最终 220-test full suite 全部通过。实际 live artifact 也已通过 CaseView 语义绑定。

Focused evidence 包括：8 个 common-flow tests、10 个 persistent-budget/transport tests、20 个 CaseView tests，
以及 25 个 live runtime/CLI/workbench 集成检查。Final clean-archive result 和 Python 3.11/3.12
GitHub merge-ref CI 由提交后的 PR metadata 记录，避免 tracked 文档自我声称尚未产生的 final head 状态。

## Scientific authority and claim ceiling

H1 保持 `PENDING_DOMAIN_REVIEW`。Public HSP90 与 static ADK runner 仍保持
`NOT_CALCULATED_BY_CASE_RUNNER`。Exact HSP90 computation 只覆盖 exact control Rule，scenario T1 的 SUPPORT
只属于 synthetic engineering contract。

本批次允许的 claim：仓库已经用真实 OpenRouter model proposal 跑通一次 HSP90 development-only
Profiler → deterministic workflow → live Planner → authorized descriptive action → EvidenceResult → unchanged
same-Rule state 的完整链；同时完成四类常见 route、三态 reducer、provenance/cost receipt 和只读 workbench。

本批次禁止升级为：Agent value 已建立、模型正确理解论文、HSP90 broad Rule 已关闭、public scientific
SUPPORT、ADK dynamics portability、general case coverage、transfer、held-out 或 production readiness。

## Remaining work

1. 人工审查并决定是否合并当前 Draft PR；本次 13-call campaign 保持关闭，不补跑到 16。
2. 具名 H1 reviewer 检查 primary passages，填写 official dispositions。
3. 解决 F04R02 typed mapping 后，再决定是否释放一个 broad computable Rule。
4. ADK dynamics、held-out 与 source-science claim upgrade 继续等待单独的人类授权。
