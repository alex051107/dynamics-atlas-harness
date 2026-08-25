# Rules Table 与 typed bindings

## Rules Table 放在哪里

Rules 的 authoring truth 继续留在原位置：

`autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/ruleset/v0_1/rule_registry.tsv`

文献 evidence、source locator 和历史 Rule ID 不移动。Harness 只通过 `config/workspace_assets.json` 引用现有 registry、v0.3 bindings、compiled index 和 selector。这样可以避免产生两套科学权威。

## 为什么需要 typed binding

Rule Registry 的一行面向人类，通常包含 paper finding、required fields、gate、integration hint、validation route、abstain route 和 transfer scope。它告诉我们“科学上要检查什么”，但不能直接回答以下运行问题：

- 这条 Rule 作用于 CASE、SOURCE 还是 EDGE？
- 哪类 method/evidence role/bridge status 会触发？
- CaseGraph 的哪些字段必须存在？
- 缺字段时产生什么 gap？
- 这项 check 的最高 claim scope 是什么？

Typed binding 是这层翻译：

```text
Rule row
  ├─ source + scientific boundary
  └─ required scientific check
          │ compile
          ▼
TypedBinding
  ├─ scope
  ├─ exact predicates
  ├─ required_fields
  ├─ gap_checks
  ├─ claim_scope
  └─ evidence_evaluation_required
```

它不是为了增加 schema 数量，而是防止 selector 用自由文本或 LLM 临时猜测 Rule 的适用范围。

## 三类对象的所有权

| 对象 | 负责什么 | 不负责什么 |
|---|---|---|
| Rule row | 文献来源、科学 check、claim/abstain 边界 | runtime predicate 的具体字段路径 |
| TypedBinding | 把 Rule 映射到 CaseGraph 的 scope、predicate 和 required fields | 创造新的科学规则 |
| OperatorSpec | 一个具体分析怎样运行、输出什么 | 决定 Rule 是否适用 |

Registry 中旧的 `integration_operator` 适合作为 action hint，不应直接当可执行 `operator_id`。真正的 `operator_id` 只能来自 registered operator registry，并经过 runtime probe 和 canary。

## 当前 v0.3 的实际作用

2026-08-25 prototype 使用同一个 rich X-EISD CaseGraph：

- 旧 v0.1 snapshot 曾产生 51 obligations / 17 unresolved；
- 当前 v0.3 compiled index 实际产生 59 obligations / 15 unresolved。

这个差异说明 typed bindings 会改变可执行 selection。测试必须绑定明确的 package version，不能继续重放旧 output 再说 selector 已接通。

这些数字只表示 development review-plan behavior，不表示 59 项都必要，也不证明 Rules 完整或 semantic correctness。

## Workable 的 Rules Table 形态

短期保留三层即可：

1. `rule_registry.tsv`：人读、文献可追溯、稳定 ID；
2. `registry_bound_typed_bindings_v0_3.json`：机器适用条件；
3. `compiled_registry_rule_index_v0_3.json`：selector 运行输入与 compile receipt。

未来 vNext 可以把重复的 paper-specific rows 合并成 generic family，并把 method-specific 差异下放到 method/operator profile；在人工冻结前，不改当前运行包。

当前 `rules_prototype/v1/` 已把这个方向固定成八类 proposal。它同时保留 14-family 方法学地图、33-rule audit lineage、seed bindings、Resolution Policies 与 Evaluation Contracts。RF02 和 RF07 没有因为进入地图就自动升级为 active rule，RF12 也没有进入 scientific registry。该 package 通过人工审查以前，不编译进 v0.3 runtime。
