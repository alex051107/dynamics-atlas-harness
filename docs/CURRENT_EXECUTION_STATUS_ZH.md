# Dynamics Atlas 仓库执行状态快照

仓库内的机器可读快照是
[current_execution_status.json](../governance/current_execution_status.json)。它供创建分支、编写
PR 和外部审查时快速了解已合并的 repository state；它不是新的科学权威，也不能单独释放下一阶段。
当前 live gate 由项目控制面中的 live Status 和具名人类决定控制。

## 当前已验证状态

- GitHub **PR #6**：exposed-development 的 no-Agent route-integrity baseline 已合并。
- GitHub **PR #8**：两个 exposed development case 的最小 Stage-2 ConclusionPacket 已合并；
  结果是三条 `ABSTAIN_OR_HUMAN_REVIEW` 和一条 relation-scoped
  `CANNOT_SUPPORT_REQUESTED_CLAIM`，没有任何 scientific `SUPPORT`。
- GitHub **PR #9**：两例 Agent contract diagnostic 已合并为安全但 capability-rejected 的
  baseline；它不证明 Agent value，也不是 Frozen Plan 的 Agent 阶段完成。
- GitHub **PR #10**：默认不可调用的 OpenRouter Profiler screening setup 已合并；默认配置
  不读取 key、不发请求、不花费 credits，也没有 model result。

当前 `main` 是 `00faf6f0d2f8916878dd37b57c2018dbfbd45020`。当前真实下一步是
F01/F02/F03/F04/F06 的具名 human/domain source-science review，而不是已完成的 PR #7
merge review。

## 阅读与命名规则

GitHub PR 编号只是 delivery ID；Frozen Plan 的 `PR 8` 指未来的 frozen-held-out semantic
milestone，并不等于 GitHub PR #8。每个 PR 必须同时说明其 Frozen Plan position、当前授权、
实际行为改变、刻意排除的工作、claim ceiling 和下一道 gate，避免把 case-bound development
artifact 写成通用 runtime 或阶段完成。

创建任何新分支前，先读 JSON 快照和当前 live Status。缺少具名 source-review disposition 时，
不要启动 ADK、held-out、source-science claim upgrade、OpenRouter execution 或新的 scientific
Agent work。
