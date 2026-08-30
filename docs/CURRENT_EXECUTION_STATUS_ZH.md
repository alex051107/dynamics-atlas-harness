# Dynamics Atlas 仓库执行状态快照

仓库内的机器可读快照是
[current_execution_status.json](../governance/current_execution_status.json)。它供创建分支、编写
PR 和外部审查时快速了解已合并的 repository state；它不是新的科学权威，也不能单独释放下一阶段。
live Status 只记录当前 gate 与已记录的人类决定；只有具名 human/domain review 或具名 project-owner
direction 才能释放科学阶段。

## 当前已验证状态

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

当前工程面只覆盖 recorded-replay evidence execution and inspection path。它不执行 live Agent，不完成
broad active-Rule closure，也不由 `run-case` 生成 terminal ConclusionPacket。H1 保持
`PENDING_DOMAIN_REVIEW`，ADK dynamics portability 保持 `NOT_EVALUATED`，held-out evaluation 未授权。
internal adversarial subagent review passes 是内部工程审查，不是 external 或 independent approval。

当前真实的科学下一步仍是 F01/F02/F03/F04/F06 的具名 human/domain
source-science review，而不是已完成的 PR #7 merge review。

## 阅读与命名规则

GitHub PR 编号只是 delivery ID；Frozen Plan 的 `PR 8` 指未来的 frozen-held-out semantic
milestone，并不等于 GitHub PR #8。每个 PR 必须同时说明其 Frozen Plan position、当前授权、
实际行为改变、刻意排除的工作、claim ceiling 和下一道 gate，避免把 case-bound development
artifact 写成通用 runtime 或阶段完成。

创建任何新分支前，先读 JSON 快照和当前 live Status。缺少具名 source-review disposition 时，
不要把 static ADK exposure 升级为 dynamics portability，不要启动 held-out、source-science claim
upgrade、OpenRouter execution 或新的 scientific Agent work。
