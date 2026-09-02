# Dynamics Atlas 仓库执行状态快照

仓库内的机器可读快照是
[current_execution_status.json](../governance/current_execution_status.json)。它供创建分支、编写
PR 和外部审查时快速了解已合并的 repository state；它不是新的科学权威，也不能单独释放下一阶段。
live Status 只记录当前 gate 与已记录的人类决定；只有具名 human/domain review 或具名 project-owner
direction 才能释放科学阶段。

## 当前已验证状态

- 当前 main 是 PR #19 merge commit `da584173ee64bfad9854132a3418ed1e871c69f5`。PR #19 的两个准确
  baseline 是 `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE` 与
  `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`；它没有被追认成 live-Agent common-flow completion。
- 当前 `feature/live-agent-decision-closure-v1` 已达到
  `LIVE_AGENT_DECISION_CLOSURE_V1_COMPLETE` 的 development-only boundary。
- Profile mode 是 `RECORDED_PROFILE_LIVE_PLANNER`。这轮没有 live Profiler call，也没有把 X-EISD recorded
  canonical profile 伪称为完整 evidence-grounded Profiler output。
- 真实 `openai/gpt-5.6-luna` Planner 通过 existing exact OpenAI-provider OpenRouter transport 运行。正向臂
  看到一张 current exact lookup card 并返回 `SELECT_ACTIONS`；card-removed 臂看到零张 card 并返回
  `ABSTAIN_NO_ACTION`。
- 正向臂经 deterministic authorization 执行一次 exact allowlisted X-EISD source lookup，产生一个 active
  EvidenceResult。目标 RuleInstance
  `F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_random_candidate_pool`
  从 `UNRESOLVED` 变为 `PASS`；只有两个冻结合同声明的 downstream dependencies 一起改变，
  `unrelated_rule_changes=[]`。
- 正向臂复用 existing X-EISD route reducer 与 Stage-2 reducer，生成 bounded
  `ABSTAIN_OR_HUMAN_REVIEW` ConclusionPacket。它没有生成 scientific SUPPORT。
- card-removed 臂的 lookup、operator、EvidenceResult 均为 0；全部 RuleResults 不变，目标保持
  `UNRESOLVED`；existing reducer 同样生成 `ABSTAIN_OR_HUMAN_REVIEW`。
- Campaign 共 3 次 HTTP attempt、2 次 completed call；两个 completed calls 的 provider-reported cost 合计
  USD 0.00072385。第一次 request 在 generation 前因 strict schema 的 `uniqueItems` 失败，没有 response ID、
  usage 或 provider-reported cost。唯一一次 schema-only repair 没有修改冻结 prompt 或语义。
- Campaign 已 `CLOSED_FROZEN`。Credential 由获准的本机 Excel Benchmark secret loader 注入 inherited
  environment，没有打印、记录、hash、持久化或提交。
- 两个 paired arms 已接入 read-only
  [workbench](../review/live_agent_decision_closure_v1/index.html)。页面显示 model/provider、usage/cost、Planner
  proposal、authorization、EvidenceResult、same-Rule transition 与 ConclusionPacket，不执行任何 mutation。
- F04R02 的 deterministic engineering traceability 已连接 dossier、manifest、typed Rule contract、receipt、
  EvidenceResult、same-Rule RuleResult 和 ConclusionPacket，并对跨 artifact 混搭 fail closed。旧
  `HSP90-TIME-ANATOMY-CONTRACT-V1` 只保留为 `runtime_authority=NONE` 的 legacy alias，等待 human alias/
  deprecation decision；scientific disposition 仍为 `NOT_EVALUATED`。
- H1 保持 `PENDING_DOMAIN_REVIEW`。Public HSP90 broad Rule closure、ADK dynamics portability、Agent value、
  transfer 与 held-out evaluation 均未建立。

历史 delivery 仍按原边界解释：PR #18 是 recorded-replay engineering workbench；PR #19 是 live-model proposal
transport 加独立 no-Agent common-flow regression。当前 milestone 只增加一条 live Planner X-EISD narrow-lookup
counterfactual，不代表 direct、lookup、registered computation 和 stop 四类 route 都已有 Agent coverage。

完整实现、实际调用、paired result、claim ceiling 与复现命令见
[LIVE_AGENT_DECISION_CLOSURE_V1.md](LIVE_AGENT_DECISION_CLOSURE_V1.md)。精确 delivery head、Draft PR state 和
GitHub merge-ref CI 由 PR metadata 记录，不写入会自我失效的 tracked final SHA。

## 阅读与命名规则

GitHub PR 编号只是 delivery ID；Frozen Plan 的 `PR 8` 指未来的 frozen-held-out semantic
milestone，并不等于 GitHub PR #8。每个 PR 必须同时说明其 Frozen Plan position、当前授权、
实际行为改变、刻意排除的工作、claim ceiling 和下一道 gate，避免把 case-bound development
artifact 写成通用 runtime 或阶段完成。

当前 live campaign 已关闭，不再调整 exposed-case prompts、扩模型矩阵或重开调用。下一个 scientific milestone
必须由人选择：具名 H1 reviewer 释放一个 broad computable Rule，或由独立 curator 接纳一个新／held-out case。
缺少该决定时，不把 static ADK exposure 升级为 dynamics portability，不启动 held-out，不升级 source-science
claim，也不通过新 config 绕过 frozen campaign。
