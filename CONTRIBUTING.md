# Contribution and Pull Request policy

## Controlling execution plan

后续工作受 [DA-HARNESS-FROZEN-PLAN-v1.0](docs/DA_HARNESS_FROZEN_EXECUTION_PLAN_V1_0_ZH.md) 控制。创建分支前，先读取 [current_execution_status.json](governance/current_execution_status.json)，确认当前阶段、下一允许动作和停止点。

只有上一阶段的 Exit Gate 已有文件证据，并获得计划要求的人工批准，才能进入下一阶段。缺少批准时保留 blocked receipt，不用更小的旁支任务绕开 gate。计划偏差追加到 [deviations.jsonl](governance/deviations.jsonl)，不得改写成追溯合规。

## Branch policy

Initial baseline push完成后，所有修改都通过 Pull Request：

```text
main
  └── codex/<bounded-change>
      or feature/<bounded-change>
      or fix/<bounded-change>
```

不要直接向远端 `main` push 后续修改。紧急修复也使用 `fix/<scope>` 分支和 PR。

## PR 必须写清楚

每个 PR 使用固定的报告结构：

1. `Observed gap`
2. `Change made`
3. `Contracts affected`
4. `Assets kept frozen`
5. `Validation actually run`
6. `Validation intentionally skipped`
7. `Allowed claim`
8. `Forbidden upgrade`
9. `Remaining risk`
10. `Next authorized action`

同时说明是否修改 `config/frozen_assets_v0_1.json`。如果当前动作没有写在机器可读状态的 allowlist 中，先停下并请求人工决定。

## Validation

默认 PR check：

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Workspace-dependent tests 在独立 GitHub runner 上会明确 skip；它们只能在具有 Dynamics Atlas upstream assets 的受控 workspace 中运行。不能把 skip 写成 actual-selector integration pass。

完整 build、lint、E2E 和 hash 只在对应风险出现时运行。相同 code state 不重复检查。

## Data and authority boundary

- 不提交 `runs/`、raw/derived scientific payload、absolute local paths、credentials 或 personal data；
- 不复制上游 Rules Registry 形成第二套 authority；
- frozen assets 只通过 manifest 与 SHA-256 引用；
- operator output 不能直接写 scientific support；
- semantic correctness、claim upgrade 和 final scientific judgment 保留 human review。

## Merge boundary

PR tests通过仍只证明声明的 structural/execution boundary。涉及 Rules、method profile、operator claim ceiling、threshold 或 scientific interpretation 的修改，需要完成对应 Exit Gate 和明确 human review 才能合并。合并一个阶段不会自动授权下一阶段。
