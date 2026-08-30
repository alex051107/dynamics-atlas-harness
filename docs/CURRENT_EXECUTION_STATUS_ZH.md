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
- 当前 Delivery A 分支提供 [source-science review workspace](../review/source_science_v1/README.md)
  和 [static Review Console](../review_console/index.html)。它们只展示现有 sources、RuleResults、
  EvidenceResults、exact control 与空白审查字段；不调用模型、Operator、API 或数据库，也不写回
  scientific state。

`03ae77efdfaabeaebbf2cf8cae5a490c15241be1` 是当前 merged PR #15 后的
development/runtime baseline commit；仓库内 Delivery A 文件在新的 Draft PR 合并前仍是审查表面，
不是 literal current `main` HEAD 的声明。
当前真实的科学下一步仍是 F01/F02/F03/F04/F06 的具名 human/domain
source-science review，而不是已完成的 PR #7 merge review。

## 阅读与命名规则

GitHub PR 编号只是 delivery ID；Frozen Plan 的 `PR 8` 指未来的 frozen-held-out semantic
milestone，并不等于 GitHub PR #8。每个 PR 必须同时说明其 Frozen Plan position、当前授权、
实际行为改变、刻意排除的工作、claim ceiling 和下一道 gate，避免把 case-bound development
artifact 写成通用 runtime 或阶段完成。

创建任何新分支前，先读 JSON 快照和当前 live Status。缺少具名 source-review disposition 时，
不要启动 ADK、held-out、source-science claim upgrade、OpenRouter execution 或新的 scientific
Agent work。
