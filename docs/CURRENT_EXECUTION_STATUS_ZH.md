# Dynamics Atlas 仓库执行状态快照

仓库内的机器可读快照是
[current_execution_status.json](../governance/current_execution_status.json)。它供创建分支、编写
PR 和外部审查时快速了解已合并的 repository state；它不是新的科学权威，也不能单独释放下一阶段。
live Status 只记录当前 gate 与已记录的人类决定；只有具名 human/domain review 或具名 project-owner
direction 才能释放科学阶段。

## 当前已验证状态

- 当前 main 为 PR #18 merge commit `e8d4f7781590c4c0424c83dffb62f62fbe526fcf`。
  PR #16 与 PR #17 的补丁内容已经由 PR #18 吸收；两者已关闭为 superseded，没有再次合并。
- `feature/live-agent-common-flows-v1` 的准确完成状态是
  `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE`、
  `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`、
  `LIVE_AGENT_DECISION_CLOSURE_NOT_YET_ESTABLISHED`。它取得一条真实 HSP90 proposal transport chain：
  冻结的 core-admitted MiniMax Profiler proposal 进入同一 deterministic
  runner，live MiniMax Planner 选择一张合法 card；runner 授权并执行一个描述性 action，产生一个
  EvidenceResult，RuleResults 保持不变，terminal state 为 `NOT_CALCULATED_BY_CASE_RUNNER`。
- 本轮共发出 17 次 HTTP 请求，其中 13 次完成并计入调用上限，累计实际费用为 USD 0.145264010；4 次
  provider HTTP 400 未完成、未计费。Campaign 在第一条 proposal-to-descriptive-action success 后自适应停止并冻结，没有声称
  16 个 frozen cells 全部运行。
- 获准的 credential 来自本机 Excel Benchmark secret location，只注入当前进程继承环境；没有打印、
  记录、hash、持久化或提交 key。
- HSP90 成功链的 Profiler 为 `CORE_ADMISSION_PASS`，完整 annotation envelope 为
  `FULL_ANNOTATION_ENVELOPE_FAIL`，错误是 `UNKNOWN_STATUS_CORE_VALUE_MISMATCH`。Luna Profiler 两次 core PASS，
  但 annotation diagnostic 两次失败；MiniMax bounded repair core PASS；
  Terra diagnostic fallback core PASS；DeepSeek 停在 JSON/schema/provider failure。所有 static ADK model
  proposals 均 core fail。Luna Planner 两次 HTTP 400，均未完成、未计费；MiniMax Planner 成功。
- MiniMax Planner 只面对 `ONE_LEGAL_CARD_VERSUS_ABSTAIN`，因此当前结果为
  `NOT_NONTRIVIAL_ROUTE_SELECTION`。成功链的 evidence 为
  `DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT`，`SAME_RULE_TRANSITION_COUNT_ZERO`，
  `CONCLUSION_PACKET_NOT_CALCULATED`。
- Common-flow suite 已重新运行 direct evaluation、narrow lookup、registered computation 与 explicit stop。
  六行全部是 `NO_AGENT_DETERMINISTIC_SCENARIO`，状态为 `NOT_LIVE_AGENT_COMMON_FLOW_COVERAGE`。三个
  terminal behavior 均出现；`SUPPORT_WITHIN_CEILING` 只属于
  `SYNTHETIC_CONTRACT_BEHAVIOR_ONLY`，real scientific support packet 数量为 0。
- 同一 HSP90 case 的 recorded replay、实际 live full-chain run 与 common-flow matrix 已并列接入 read-only
  [workbench](../review/live_agent_common_flows_v1/index.html)。
- 本分支记录了 internal adversarial subagent review passes；它们是同一 Codex development campaign 的
  内部审查，不是独立 GitHub review、domain approval 或 scientific validation。

- GitHub **PR #6**：exposed-development 的 no-Agent route-integrity baseline 已合并。
- GitHub **PR #8**：两个 exposed development case 的最小 Stage-2 ConclusionPacket 已合并；
  结果是三条 `ABSTAIN_OR_HUMAN_REVIEW` 和一条 relation-scoped
  `CANNOT_SUPPORT_REQUESTED_CLAIM`，没有任何 scientific `SUPPORT`。
- GitHub **PR #9**：两例 Agent contract diagnostic 已合并为安全但 capability-rejected 的
  baseline；它不证明 Agent value，也不是 Frozen Plan 的 Agent 阶段完成。
- GitHub **PR #10**：默认不可调用的 OpenRouter Profiler screening setup 已合并；默认配置
  不读取 key、不发请求、不花费 credits，也没有 model result。
- GitHub **PR #15**：two-case exposed development causal capsule 已合并为
  `03ae77ef`。它证明 fresh Draft Rule state 可以物化受限的 Planner 输入，合法 card selection
  或 abstention 才会触发选中的描述性 action；HSP90 的 exact F04R02 control 仍单独显示，不能
  当作 broad public case 的 closure。该 PR 仍是 recorded proposal replay，不是独立 live Agent
  result，也没有 source-science approval。
- engineering workbench v1 以 bounded engineering integration baseline v1 记录；它整合并修复了
  PR #16/#17，提供两案例 recorded-replay
  runner、proposal provenance、artifact-only CaseView、九项 H1 advisory package、
  [source-science review workspace](../review/source_science_v1/README.md) 和四视图
  [static Review Console](../review_console/index.html)。它只执行受限描述性 action、投影已有 artifact，
  不调用 live model、读取凭据或写回 scientific state。F04R02 仍是 `DATA_INSUFFICIENT`，broad
  same-Rule closure 仍是 `BLOCKED_BROAD_CLOSURE`。

`03ae77efdfaabeaebbf2cf8cae5a490c15241be1` 是 bounded engineering integration 的冻结
development/runtime baseline commit，不是对当前 literal `main`、delivery head、merge state 或 CI
结果的实时断言。精确 delivery SHA 与 GitHub PR merge-ref CI 结果由 GitHub PR metadata 记录；tracked
status 使用 `GITHUB_PR_METADATA_AUTHORITATIVE_FOR_DELIVERY_STATE`，因此不会因后续 merge 立即失真。

当前工程面已经包含一条真实 OpenRouter proposal-to-descriptive-action transport chain，以及一套独立的
no-Agent common-flow regression。H1 保持
`PENDING_DOMAIN_REVIEW`，broad active-Rule closure 未完成，
public-case runner 仍不生成 terminal ConclusionPacket，ADK dynamics portability 保持 `NOT_EVALUATED`，
held-out evaluation 未授权，Agent value 未建立。

PR #18 的历史工程范围仍准确命名为 recorded-replay evidence execution and inspection path。这个名称保留
它在当前 live-capable 分支中的基线角色，不把后续 live integration 写回成 PR #18 的能力。

本次 exact campaign 已关闭并冻结，不再补跑至 16 calls。Closed guard 现在由 config 中的 campaign ID、
completion receipt path/hash、closed state 和 receipt 记录的调用/费用总计驱动；新授权 campaign 可通过新
config 与独立 ledger 建立，不需要修改产品源码。PR #19 合并后的下一工程 milestone 是
`LIVE_AGENT_DECISION_CLOSURE_V1`；H1 的具名 human/domain source-science review 仍是独立科学 gate。

## 阅读与命名规则

GitHub PR 编号只是 delivery ID；Frozen Plan 的 `PR 8` 指未来的 frozen-held-out semantic
milestone，并不等于 GitHub PR #8。每个 PR 必须同时说明其 Frozen Plan position、当前授权、
实际行为改变、刻意排除的工作、claim ceiling 和下一道 gate，避免把 case-bound development
artifact 写成通用 runtime 或阶段完成。

创建任何新分支前，先读 JSON 快照和当前 live Status。缺少具名 source-review disposition 时，
不要把 static ADK exposure 升级为 dynamics portability，不要启动 held-out、source-science claim
upgrade，也不要在没有新授权、独立 campaign 配置与独立预算账本的情况下重开已冻结的 live campaign。
