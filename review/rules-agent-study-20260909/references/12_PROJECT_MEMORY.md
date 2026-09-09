# Dynamics Atlas：稳定项目记忆

> **所有 Dynamics Atlas 工作先读本文件。**  
> 它回答“我们为什么做这件事、什么不能被遗忘”。它不保存实时任务状态、实验数字、图或 slide 版本；这些由 Status 和任务 artifact 保存。

**记忆版本：** MP-3 · 2026-07-31  
**实时状态入口：** autoresearch/DYNAMICS_ATLAS_STATUS.md  
**原则：**“当前 gate”是执行约束，不能改写项目的科学使命。

## 1. 项目要解决的事情

会议中确认的项目有四条相连、但不能互相冒充的工作线：

1. **G1｜可靠性科学。** 对异质蛋白动力学数据，在明确 representation、condition、time semantics 和统计单位后，说明哪些 ensemble quantity 可信、哪些不可信，以及证据为何足够或不足。
2. **G2｜跨模态 landscape。** 公平比较不同来源的 conformational landscape，识别 shared、unique 与 unresolved regions；不能让大量 MD frames 淹没小的 NMR ensemble，也不能把不同 state definition 硬合并。
3. **G3｜可复用 workflow / harness。** 将已验证的既有方法、输入、参数、provenance、prompt、执行和审核固化，使别人能够在相似新数据上复跑、审查和扩展。
4. **G4｜有限 Agent 自动化。** 在 G1–G3 已有冻结的科学与确定性基线后，检验 Agent 是否能减少例行整理／配置／审核成本，而不增加不安全 claim。初期最终科学判断仍由人做。

G1 和 G2 是科学产出；G3 是把可迁移的科学路径固化；G4 是可独立失败的后续假设。不得把 G4 写成整个项目的父目标。

## 2. 永久边界

- 初期只采用有可信文献依据的 established methods；新方法、state definition、threshold 或比较语义需人类冻结。
- 人拥有 molecule/condition/comparability、未注册 adapter、claim upgrade 和最终科学判断的权威。
- Agent 可以提出 locator-grounded EvidenceProposal；deterministic compiler、registered executor、validator 和 human review 才能 canonicalize、执行、否决或批准。
- ABSTAIN／NOT_COMPARABLE 是合法科学结果，不是失败。
- 同一开发 packet、暴露来源或 fixture 永远不能被重命名为 strict held-out。
- HSP90 是重要的 development scientific capsule，不是跨资源泛化或 Agent value 的证明。

## 3. 问什么，就用哪一类权威来源

| 要回答的问题 | 权威来源 |
|---|---|
| 我们为什么做、导师期待什么？ | 2026-07-28 两份原始会议转写：会议纪要/28号会议纪要/2026-07-28_Soojung_会议材料/01_原始转写_前半段_音频1173668587.txt 和 02_原始转写_后半段_Zoom重连.txt |
| 某个科学／技术结论是真的吗？ | 对应 task 中的输入、hash、validation、review、claim ledger 与 replay artifact |
| 现在允许做什么、谁需决定？ | autoresearch/DYNAMICS_ATLAS_STATUS.md、冻结的 phase register，以及 append-only decision log 中的人类决定 |
| 该怎样对外讲？ | 已标为 candidate 或 released 的 deck／网站；它们从不覆盖前三类权威 |

不要用一个全局的“文件优先级”替代这张表：原始会议转写决定意图，不能被后来的科学修正覆盖；反过来，原始会议转写也不能替代当前数据的科学事实。

## 4. 每次重入项目的读法

1. 读本文件，复述 G1–G4 和永久边界。
2. 读实时 Status 的 NOW／当前 gate／reconciliation 项。
3. 只读 Status snapshot 之后的 Decision Log 条目。
4. 若要开始实质工作，先为该 task 写 context receipt：它必须说明所属 G1/G2/G3/G4/治理工作线、唯一可改变的决定、证据单位、claim ceiling 和停止条件。

如果任务不能推动当前 gate，也不产生明确的可迁移产物，标为 EXPLORE；它不能消耗主线注意力或被汇报为项目推进。

## 5. 文档所有权

| 文档 | 只负责什么 | 何时更新 |
|---|---|---|
| PROJECT_MEMORY.md | 稳定使命、权威边界、永久 claim boundary | 只有使命／权威／永久边界改变时 |
| autoresearch/DYNAMICS_ATLAS_STATUS.md | 现在的 evidence ladder、gate、blocker、release/reconciliation 状态 | live fact 或当前允许动作改变时 |
| task state/context_receipt.md | 一项任务为何允许启动、可能改变什么、何时停止 | 新建或实质恢复任务时；完成时追加 exit |
| DYNAMICS_ATLAS_DECISION_LOG.jsonl | 人类确认的优先级、gate、manual decision 历史 | 只追加，不回写历史 |

方法、图、日志、代码、论文笔记和任务细节只留在 task artifact。不要把它们搬回这里。

## 6. 变更记录

| 日期 | 变化 | 后果 |
|---|---|---|
| 2026-07-31 | MP-3：按原始会议转写与跨任务审计重写；恢复 G1–G4，取消 Agent-first 叙事。 | memory 保持稳定；实时工作只由 Status 管理。 |
