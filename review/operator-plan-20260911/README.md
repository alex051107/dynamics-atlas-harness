# Dynamics Atlas：算子计划 Pro 审查包（2026-09-11）

这是一个供 ChatGPT Pro 做外部设计审查的 review-only capsule。它由本地任务
`dynamics_atlas_operator_plan_20260911` 的已完成交付导出，放在独立分支
`feature/operator-plan-review-20260911`；不修改 `main`，不代表科学结论已获领域批准。

## 推荐阅读顺序

1. [原始审查计划](inputs/PLAN_FOR_PRO_REVIEW_20260911_ZH.md)：规定 10 个判断点、输出格式和禁止升级。
2. [跟进审查包](inputs/PRO_REVIEW_FOLLOWUP_PACKET_20260911_ZH.md)：把上一批 Pro 背景与本次真实执行结果合并成一个自包含问题包。
3. [本地执行报告](outputs/OPERATOR_PLAN_REPORT_ZH.md)：六算子、D1、runtime、F/D/O、盲评和未完成项的总览。
4. [偏差与限制](outputs/DEVIATIONS.md)：运行器修复、跨 revision、D-arm 完整性、第二评分人和外部交付边界。
5. [证据账本](outputs/WORK_EVIDENCE_LEDGER.json) 与 [D1 表](outputs/D1_TABLE_HSP90.md)：查看每一项结果允许支持什么、不能支持什么。
6. [算子定义](outputs/operators/)、[固定结果](outputs/fixed_operator_results/)、[独立复算](outputs/INDEPENDENT_RECOMPUTE_MODEL.json)：核对具体实现与数值绑定。
7. [primary score 汇总](outputs/blind/group_scores.json)、[封存记录](outputs/blind/SCORE_SEAL.json) 和 [第二评分状态](outputs/blind/SECOND_SCORER_STATUS.json)：评分只能作为本次受限评测证据。

## 当前结果的硬边界

- 16 次 D/O 正式运行和 2 次 F 运行完成；新增费用为 `$0.18989771`，无 `UNKNOWN_CHARGE`。
- HSP90 D1 表和固定算子结果已生成；独立复算检查的是数值一致性，不是独立科学验证。
- primary blind score 已封存、揭盲并汇总；第二评分人不可用，因此 agreement 未测。
- 本分支只是把审查材料放到 GitHub，方便 Pro 读取；没有创建或合并科学代码 PR，也没有开始新实验。
- 结果不能升级为平衡 population、交换速率、机制、新状态、普适性、生产能力或 source-science approval。

## 上一批 Pro 材料

上一批 2026-09-10 的 ChatGPT 文件已复制到
[`inputs/prior_chatgpt_packet_20260910/`](inputs/prior_chatgpt_packet_20260910/)。其中的两个原始论文 PDF
没有再次公开发布；论文仍作为本地附件包中的 source-of-record。上一批 Markdown 背景文件按原文件名保留，供本次跟进审查追溯。

## 给审查者的输出要求

请按计划第 5 节逐条回答 1–10：每条只给一个“成立／不成立／证据不足”标签和 1–3 句理由；至少指出一处必须修改的设计并给出可直接执行的替代方案；可核对的数字或引用标“核对过”，不能核对标“未核对”；总长不超过 1500 个汉字。不要建议扩充规则、换更强模型、重跑同题，也不要把 n=4 中位数比较当显著性检验。
