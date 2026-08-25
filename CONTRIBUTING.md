# Contribution and Pull Request policy

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

- 改了什么；
- 解决哪个 observed gap 或风险；
- 哪些 frozen/public contracts 改变；
- 实际运行了哪些 checks；
- 哪些 checks 有意跳过以及原因；
- allowed claim、forbidden upgrade 和 remaining risk；
- 是否修改 `config/frozen_assets_v0_1.json`。

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

PR tests通过仍只证明声明的 structural/execution boundary。涉及 Rules、method profile、operator claim ceiling、threshold 或 scientific interpretation 的修改，需要明确 human review 才能合并。
