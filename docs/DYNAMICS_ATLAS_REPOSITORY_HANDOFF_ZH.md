# Dynamics Atlas Harness 现状与交接

这份仓库已经有一条真实模型参与的开发流程。模型负责提交受限 proposal，确定性代码负责 Rule、授权、证据、重评和结论。最新的正向运行把一个 X-EISD source declaration Rule 从 `UNRESOLVED` 改为 `PASS`，配对的 removed-card 运行让同一个模型 abstain，并留下零执行记录。两条运行最后都进入已有的 `ABSTAIN_OR_HUMAN_REVIEW` reducer。

这份证据足以说明开发链已经接通。它还不能回答论文判断是否正确、Agent 是否普遍有价值、HSP90 broad Rule 是否成立、ADK 是否具备 dynamics portability，或者新案例能否迁移。具名 source-science review 仍是当前科学 gate。

本文给第一次进入仓库的人一个入口。它说明现在该从哪里读、哪些命令属于现行路径、几轮模型实验各自证明了什么、哪些目录只是历史证据，以及下一次人类决策需要在什么范围内作出。

## 三十秒状态

| 项目 | 当前事实 |
|---|---|
| GitHub repo | private repository `alex051107/dynamics-atlas-harness` |
| 当前 main | `da584173ee64bfad9854132a3418ed1e871c69f5`，PR #19 merge commit |
| 当前 Draft | [PR #20](https://github.com/alex051107/dynamics-atlas-harness/pull/20)，base 为上述 main；最新 head、CI 和 merge state 以 GitHub metadata 为准 |
| PR #19 | 已合并为 live-model proposal transport 与 no-Agent deterministic common-flow regression 两个 bounded baseline |
| PR #20 | 一条 `RECORDED_PROFILE_LIVE_PLANNER` 的 X-EISD decision-closure 路径，仍待人审查，未合并 |
| 最新真实模型结果 | Luna Planner 选择 exact lookup，目标 Rule `UNRESOLVED -> PASS`；removed-card arm abstain，零执行 |
| 最新终局 | 两臂均为 `ABSTAIN_OR_HUMAN_REVIEW`，没有 real scientific SUPPORT |
| 科学 gate | H1 `PENDING_DOMAIN_REVIEW` |
| Held-out | `NOT_ACCESSED` |

当前机器可读事实在 [`governance/current_execution_status.json`](../governance/current_execution_status.json)，中文状态摘要在 [`CURRENT_EXECUTION_STATUS_ZH.md`](./CURRENT_EXECUTION_STATUS_ZH.md)。GitHub 上会变化的 SHA、CI、Draft 和 merge 状态由 PR metadata 管理，不由 tracked status 追写。

## 这个项目实际在做什么

项目的稳定目标有四层。G1 研究异质动力学数据里哪些量可信。G2 处理跨模态 landscape 的可比性。G3 把已验证的方法、输入、参数、provenance 和审查固化成可复跑 workflow。G4 只检验有限 Agent 能否减少例行整理和决策成本。G4 可以失败，也不能覆盖 G1 和 G2 的科学问题。

仓库里的产品路径可以缩成下面这一行。

```text
scientific question + declared sources + declared data
  -> recorded or live Profile proposal
  -> deterministic admission
  -> RuleInstances and unresolved obligations
  -> legal action cards
  -> recorded or live Planner proposal
  -> deterministic authorization
  -> direct evaluation / exact lookup / registered computation / stop
  -> EvidenceResult
  -> same-Rule reevaluation
  -> bounded ConclusionPacket
  -> human scientific review
```

模型只写 Profile proposal 或 Planner proposal。它不能新建 Rule、修改 threshold、注册 Operator、执行 shell、决定 EvidenceResult、改写 RuleResult 或给出最终科学 verdict。

## 仓库是怎样走到现在的

最早几轮先搭起 Profile、Rules、typed bindings、RunPlan 和 Operator canary。那时 X-EISD 有 59 个 obligations、15 个 unresolved inputs 和 16 个 gaps，但没有可路由 Operator，正确结果是 `RUN_PLAN_BLOCKED`。

随后仓库加入真实 case vertical slice、Stage-2 reducer、可复跑 demo、paper question smoke、answer-blind public packet 和 HSP90/static-ADK capsule。PR #18 把两案例 recorded replay、fresh Rule state、legal cards、授权、EvidenceResult、CaseView 和静态 workbench 接在一起。那一阶段仍没有 live model，也没有 runner-generated scientific conclusion。

PR #19 把 OpenRouter 模型 proposal 接入现有 runtime，并保留多模型失败证据。MiniMax 最终完成一次 HSP90 proposal-to-descriptive-action transport。仓库另用无 Agent 的确定性 fixtures 覆盖 direct、lookup、registered computation、stop 和三个 reducer state。两组证据各自成立，不能合并成“Agent 已覆盖四类 common flows”。

PR #20 补上了最关键的因果缺口。它使用 recorded X-EISD profile 和 live Luna Planner。正向 arm 让模型选择 exact allowlisted lookup，确定性代码完成 evidence attachment、same-Rule reevaluation 和已有 reducer。配对 arm 移除 action card，模型 abstain，系统没有偷偷执行 lookup 或 Operator。完整证据在 [`LIVE_AGENT_DECISION_CLOSURE_V1.md`](./LIVE_AGENT_DECISION_CLOSURE_V1.md)。

| GitHub 阶段 | 交付 | 今天怎样看 |
|---|---|---|
| PR #1 至 #3 | Rules prototype、frozen plan、baseline boundary normalization | 早期治理和结构基础；PR #1 关闭，后续基线吸收有效部分 |
| PR #4 至 #6 | proposal-only Rules、F02/F03 prerequisites、real-case vertical slice | 当前 deterministic evaluation 和 exact route 的来源 |
| PR #7 至 #11 | live-Agent contract failure、Stage-2 reducer、local Qwen diagnostic、OpenRouter screening setup、status reconciliation | 保留 fail-closed 和 reducer 证据；不当作成功 Agent 路径 |
| PR #12 至 #15 | runnable demo、end-to-end smoke、public packet、two-case capsule | recorded development case 和 reproduction 基线 |
| PR #16 至 #18 | source-science console、root instructions、engineering workbench | PR #16、#17 已由 PR #18 吸收并关闭；PR #18 已合并 |
| PR #19 | multi-model proposal transport 与 no-Agent common-flow regression | 已合并的两个 bounded baseline |
| PR #20 | live Planner exact lookup、same-Rule transition、paired stop | 当前 Draft，待人审查 |

## 先读哪些目录

| 路径 | 现在负责什么 | 阅读建议 |
|---|---|---|
| `src/dynamics_atlas_harness/` | runtime、Rules adapter、transport、scenario、CaseView 和 workbench renderer | 先看 `cli.py`，再按下面的 canonical path 进入 |
| `tests/` | 237 项 GitHub full-suite 行为检查的来源，另有 clean-archive integration | 用来判断某个 claim 是否有 behavioral test，不把通过测试写成科学批准 |
| `agent_experiments/` | frozen campaign config、prompt、model profile 和 ledger identity | 只在解释一次具体 campaign 时读 |
| `evidence/` | committed receipts、model attempts、Rule transitions、ConclusionPackets 和 scenario matrices | 证据主库，按 milestone 读取，不要从头浏览 306 个文件 |
| `review/` | 已生成的只读 workbench snapshots | 快速看结果，不作为新的执行证据 |
| `review/source_science_v1/` | H1 advisory packet 与空白 official reviewer form | 人类 source-science 工作区，Agent 不能代签 |
| `governance/` | 当前仓库 execution status 和冻结计划 | 读当前事实；GitHub mutable state 仍以 PR metadata 为准 |
| `registries/`、`schemas/`、`config/` | Rule、Operator、proposal 和 campaign 的冻结合同 | 排查身份、schema、授权和 claim ceiling 时读 |
| `docs/` | 各阶段完成报告、架构说明和这份入口 | 新读者先看本文和两个 live-agent completion docs |
| `methodology/`、旧 completion docs | 项目演化和早期设计语境 | 保留复现价值，不当作现行入口 |

本次文档变更前的 Git tree 有 33 个 tracked source files、44 个 tracked test files、305 个 tracked evidence files，共 542 个 tracked files。工作区里的 `evidence/` 约 11 MB，是最大目录。这里的主要问题是导航，不是需要把冻结 artifacts 全部搬走。

## 现行代码路径

### 1. 两个 exposed public case 的默认路径

入口是 `run-agent-case`，默认 `recorded`，不读 credential，也不联网。

```bash
dynamics-atlas run-agent-case \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-recorded

dynamics-atlas run-agent-case \
  --case-id ADK_EXPOSED_PORTABILITY_V1 \
  --output-dir /tmp/dynamics-atlas-adk-recorded
```

主要实现位于 [`case_runner_v1.py`](../src/dynamics_atlas_harness/case_runner_v1.py)。它负责 registered public packet、recorded proposals、fresh Rules、legal cards、授权、一个 descriptive action 或 abstain、EvidenceResult 和 run manifest。public HSP90/ADK runner 仍保持 `NOT_CALCULATED_BY_CASE_RUNNER`。

### 2. 多模型 proposal transport baseline

`run-agent-case --agent-mode live-openrouter` 和 `run-agent-campaign` 是显式 live transport 接口。已提交的 PR #19 campaign 已关闭，所以当前 config 会在 credential 和网络之前 fail closed。开始新 campaign 需要新的明确授权、config 和 ledger，不能靠换 output directory 解锁旧 campaign。

主要实现位于 [`live_agent_common_flows_v1.py`](../src/dynamics_atlas_harness/live_agent_common_flows_v1.py) 与 [`openrouter_proposal_transport_v1.py`](../src/dynamics_atlas_harness/openrouter_proposal_transport_v1.py)。这两处负责模型 request、strict schema、provider identity、预算、raw response、usage/cost 和 receipt。模型执行科学工具的权限始终为零。

### 3. 当前 active Rule decision closure

PR #20 的入口如下。

```bash
dynamics-atlas run-agent-decision-closure \
  --campaign-config /path/to/new-authorized-decision-closure-campaign.json \
  --output-dir /tmp/dynamics-atlas-live-decision-closure
```

已提交 campaign 同样关闭。代码在 [`live_agent_decision_closure_v1.py`](../src/dynamics_atlas_harness/live_agent_decision_closure_v1.py)。它冻结 X-EISD unresolved base state，为 card-present 和 card-removed 两臂分别生成 Planner-visible input。模型输出经过 admission 后，exact lookup、Rule reevaluation 和 reducer 由 [`real_case_vertical_slice_v1.py`](../src/dynamics_atlas_harness/real_case_vertical_slice_v1.py) 与 [`minimal_stage2_exposed_conclusions_v1.py`](../src/dynamics_atlas_harness/minimal_stage2_exposed_conclusions_v1.py) 完成。

### 4. 无 Agent 的 common-flow 回归

```bash
dynamics-atlas run-scenario-suite \
  --output-dir /tmp/dynamics-atlas-common-flows
```

实现位于 [`common_flow_scenarios_v1.py`](../src/dynamics_atlas_harness/common_flow_scenarios_v1.py)。它证明 deterministic runtime 能表达四类常见 route 和三种 terminal behavior。每一行都明确标成 `NO_AGENT_DETERMINISTIC_SCENARIO`。

### 5. 只读检查面

`build-workbench` 读取 recorded 或 live artifact roots，重验身份与 links，再生成静态页面。

```bash
dynamics-atlas build-workbench \
  --status governance/current_execution_status.json \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_PRESENT \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_REMOVED \
  --output-dir /tmp/dynamics-atlas-decision-closure-workbench
```

[`case_view_v1.py`](../src/dynamics_atlas_harness/case_view_v1.py) 是 fail-closed read model，[`review_console_v0.py`](../src/dynamics_atlas_harness/review_console_v0.py) 负责静态 renderer。页面不执行模型、lookup、Operator 或 state mutation。

## 模型证据不只来自 Luna

仓库保留了几代真实或本地模型诊断。它们回答的是不同问题，不能做成 leaderboard。

| 模型 | 实际观察 | 能支持的判断 |
|---|---|---|
| local `qwen2.5:1.5b` | 两轮 proposal diagnostic 均保持安全边界，但 Profiler 关键事实、required UNKNOWN 和 Planner typed envelope 未通过 | 小模型可以 fail closed；没有 typed capability pass |
| `deepseek/deepseek-v4-flash-0731` | PR #19 中出现 HTTP 400 或 provider `finish_reason=error`，没有形成可 admission 的 JSON proposal | transport/provider negative evidence |
| `openai/gpt-5.6-luna` in PR #19 | HSP90 Profiler core admission 通过，完整 annotation envelope 失败；ADK core 被拒；HSP90 Planner strict request 两次 HTTP 400 | 有 core proposal 能力，尚无 full Profiler envelope 或 PR #19 Planner success |
| `minimax/minimax-m2.5` | HSP90 Profiler core admission 通过但 annotation envelope 失败；live Planner 在一张 legal card 与 abstain 之间选中 card，完成一个 descriptive action | 真实 proposal transport 和 deterministic authorization 已跑通；Rule 没有变化，ConclusionPacket 未计算 |
| `openai/gpt-5.6-terra` | HSP90 Profiler core admission 通过但 annotation envelope 失败；ADK core 被拒 | 额外 diagnostic evidence，没有成功 decision path |
| `openai/gpt-5.6-luna` in PR #20 | paired X-EISD Planner 两臂完成；正向 exact lookup 使同一 Rule `UNRESOLVED -> PASS`，stop arm 零执行 | 一条 active evidence decision closure 在 development contract 内成立 |

PR #19 的多模型 campaign 共 17 个 HTTP attempts、13 个 completed calls，completed-call cost 为 USD 0.145264010。完整矩阵在 [`live_agent_development_matrix.json`](../evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/live_agent_development_matrix.json)，完成 receipt 在 [`live_agent_campaign_manifest.json`](../evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/live_agent_campaign_manifest.json)。

PR #20 共 3 个 HTTP attempts、2 个 completed calls，cost 为 USD 0.00072385。第一次请求在生成前因为 provider strict-schema 不接受 `uniqueItems` 返回 HTTP 400。一次 schema-only repair 后，两臂完成。paired matrix 在 [`paired_arm_matrix.json`](../evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/paired_arm_matrix.json)。

## 四类 common flow 和三个终局

| 场景 | Agent 参与 | 结果 |
|---|---|---|
| Direct evaluation | 无 | existing structured evidence 进入 frozen evaluation contract，终局 `ABSTAIN_OR_HUMAN_REVIEW` |
| Narrow lookup | 无，PR #20 另有 live Planner 版本 | exact X-EISD lookup 使目标 declaration Rule `UNRESOLVED -> PASS` |
| Registered computation | 无 | exact HSP90 control 的 F04R02 `UNRESOLVED -> PASS`，scope 仍为 exact-control-only |
| Explicit stop | 无 | 缺失 source declaration 保持 `UNRESOLVED`，没有未经授权的分析 |
| Reducer SUPPORT | 无 | 只由 `SYNTHETIC_CONTRACT_BEHAVIOR_ONLY` fixture 演示 |
| Reducer CANNOT SUPPORT | 无 | X-EISD explicit relation mismatch 生成 `CANNOT_SUPPORT_REQUESTED_CLAIM` |

完整 scenario matrix 在 [`common_flow_matrix.json`](../evidence/common_flow_scenarios_v1/development_runs/common_flow_scenarios_v1/common_flow_matrix.json)。这张表证明 route 和 reducer behavior，不证明 live Agent 覆盖四类 route。

## 哪些东西现在保留，哪些只留作历史

### 继续作为当前主线

- `run-agent-case` 的 recorded default 与显式 live mode
- `run-agent-decision-closure` 的 paired decision experiment interface
- `run-scenario-suite`
- deterministic admission、Rules、legal cards、authorization、EvidenceResult、same-Rule reevaluation 和现有 reducers
- provider-thin OpenRouter proposal transport、budget 和 receipts
- CaseView 与 read-only workbench
- source-science reviewer workspace
- 冻结的 unique model failures 和 successful run roots
- Python 3.11/3.12 CI 与 clean-archive checks

### 保留，但不再作为 README 主入口

- `run-fixture` 与 `run-prototype`，它们说明早期 control plane 和 blocked routing
- `run-demo` 与 `run-smoke`，它们继续用于历史 reproduction 和 regression
- `run-case`，功能由 recorded `run-agent-case` 覆盖，现阶段仍为 compatibility alias
- `TARGET_ARCHITECTURE_ZH.md`、旧 completion reports、早期 agent experiments 和 milestone evidence trees
- PR #16、#17 的分支历史。它们已被 PR #18 吸收并在 GitHub 上关闭为 superseded

### 现在不要继续增加

- model leaderboard 或新 provider matrix
- provider registry、Agents SDK、多 Agent runtime
- scheduler、DAG engine、database、RAG、MCP、plugin system
- React、FastAPI 或 stateful GUI
- Agent-controlled shell、自动 Rule 生成、自动 Operator 注册、自动科学批准
- 为了得到 PASS 而新增 synthetic Rule 或把 exact control 写成 broad closure

## 现在允许怎样描述项目

允许使用下面这段表述。

> Dynamics Atlas Harness 已有一个可复现、fail-closed 的 development workflow。它可以让 recorded 或真实模型提交受限 proposal，再由确定性代码完成 admission、Rules、legal actions、授权、证据、same-Rule reevaluation、bounded reducer 和只读审查。一次真实 Luna Planner 运行已经使 exact X-EISD declaration Rule 从 `UNRESOLVED` 变为 `PASS`，配对 removed-card 运行留下零执行记录。

下列表述没有证据支持。

- live Profiler 已完整通过 evidence-grounding envelope
- Agent 已参与 direct、lookup、computation、stop 四类 route
- Planner 已证明多路线 decision utility
- Agent value、transfer 或 generalization 已建立
- 模型正确理解论文
- HSP90 broad Rule 已关闭
- public scientific SUPPORT 已成立
- ADK dynamics portability 已建立
- held-out 或 production readiness 已验证

## 目前真正需要人决定什么

第一项决定是 PR #20 是否以当前 bounded claim 合并。代码 checkpoint `a04b2300525bcafb3e47b42a0874c17dba430af5` 的 GitHub Python 3.11/3.12 checks 各通过 237 项并跳过 2 项，clean archive integration 通过 35 项。本文和外部审查 prompt 属于其后的 docs-only delta，新的 exact head 和 CI 由 GitHub PR metadata 记录。

第二项决定是下一科学 milestone。项目控制面只允许两个方向。

1. 由具名 H1 reviewer 检查 primary passages，正式释放一个 broad computable Rule。
2. 由独立 curator 接纳一个新的或 held-out case，冻结 input、source authority、Rule contracts 和 claim ceiling 后再运行。

继续在 HSP90、ADK 和 X-EISD exposed packets 上调 prompt，或再加几个模型，不会回答这两个科学问题。

## 这份交接文稿用了哪些 human-writing skills

本地几种 writing skill 各管一件事。

`storytelling-narrative` 先决定读者顺序。本文的主线是“从多代分散 evidence 走到一条可解释的 canonical path，因为模型 proposal 已经与同一 Rule 和现有 reducer 接通”。它负责取舍和排序，不负责增加事实。

`human-writing` 管事实和说话位置。本文只把 Git history、GitHub PR metadata、代码、tests 和 frozen receipts 能证明的内容写成事实。内部 subagent review、CI、静态页面和模型 proposal 都没有被提升为 scientific approval 或作者个人经历。

`humanizer-zh-plus` 负责最后一遍中文。它清理套话、翻案句、空泛结尾和过度整齐的列表，同时保留技术文档确实需要的表格、英文 identifier、路径和冒号。当前 style profile 还没有用户真实语料，所以采用克制、具体、长短句交错的普通话，没有假装复刻个人口头禅。

`chatgpt-pro-prompt` 单独负责外部审查合同。它要求 ChatGPT Pro 对明确 claims 返回 `VERIFIED`、`WRONG` 或 `DATA_INSUFFICIENT`，并给出可执行的 repo/PR 修改意见。它不会要求模型展示 chain-of-thought，也不会用主观 confidence 分数代替证据。

以后写项目交接、研究复盘或对外说明，可以继续按这个顺序使用。先整理读者路径，再固定事实 ownership 和 claim ceiling，最后做中文冷读与机械扫描。外部审查 prompt 放在 [`CHATGPT_PRO_WHOLE_REPO_REVIEW_PROMPT_ZH.md`](./CHATGPT_PRO_WHOLE_REPO_REVIEW_PROMPT_ZH.md)。

## 接手后的最短阅读路线

1. 看本文的三十秒状态和模型表。
2. 打开 [`review/live_agent_decision_closure_v1/index.html`](../review/live_agent_decision_closure_v1/index.html)，并列看 positive 和 stop arms。
3. 看 [`LIVE_AGENT_DECISION_CLOSURE_V1.md`](./LIVE_AGENT_DECISION_CLOSURE_V1.md) 的 exact evidence route、validation 和 claim ceiling。
4. 看 [`LIVE_AGENT_COMMON_FLOWS_V1.md`](./LIVE_AGENT_COMMON_FLOWS_V1.md) 的多模型 diagnostic 与 no-Agent scenario matrix。
5. 到 GitHub 检查 PR #20 最新 head、files、CI 和 review state。
6. 把下一份 prompt 贴进 ChatGPT Pro，要求它对“是否合并、哪些路径应降级、下一科学 milestone 选哪一个”给出独立审查。
