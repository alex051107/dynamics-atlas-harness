# Luna开发结果与下一项科学比较

先读[下一阶段行动计划](NEXT_SCIENTIFIC_STEP_ZH.md)，再读[修订报告](DEVELOPMENT_REPORT_ZH.md)。需要转交Pro时可复制[完整审查提示](PRO_NEXT_STEP_PROMPT_ZH.md)。[领域核对简报](DOMAIN_REVIEW_BRIEF_ZH.md)列出专家需要确认的具体科学边界。

本次采纳[Pro返回审查](PRO_DEVELOPMENT_REVIEW_ZH.md)的归因纠正，完成一次[离线答案保存修复](post_development_review/README.md)。没有新增模型会话、科学拟合、规则或正式题。

十二次历史运行的初稿、终稿、回执和执行记录均保留。第二批T4L B/C初稿和终稿分别展示，离线回放不会替代真实终稿计分。

[运行费用](development_results.json) · [科学核对](SCIENTIFIC_AUDIT_ZH.md) · [原低成本计划](LOW_COST_EXECUTION_PLAN_ZH.md)

原DEVELOPMENT_REVIEW_PACKET.zip保留最初开发交付，未包含本次报告修订。阅读当前计划和结论请使用本目录最新Markdown。执行记录省略重复request，保留模型响应、工具结果和错误。完整原始请求保留本地，来源见父目录references；此包未包括全部矩阵，不是完整离线复现环境。

## 2026-09-09 晚：三体系操作计划（替代 NEXT_SCIENTIFIC_STEP_ZH.md 的下一阶段方案）

- [THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md](THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md)：建 Rules 回路系统 → HSP90 四站 → 结果包交 Pro → ADK/DHFR 只读盘点按规则选一个 → 第二、第三体系。每步含输入、动作、输出、完成标准、停止条件。暂不等领域专家，Pro 审结果包；结论保持"开发暴露、未领域确认"。
- [PRO_CONFIRM_THREE_SYSTEMS_PROMPT_ZH.md](PRO_CONFIRM_THREE_SYSTEMS_PROMPT_ZH.md)：请 Pro 审查该计划的提示。
- `NEXT_SCIENTIFIC_STEP_ZH.md` 中的"四来源 × 3 组 × 2 次 = 24 份"比较停放，未启动。

## 2026-09-09 深夜：Pro 审查 v1 → HSP90 首轮有界计划 v2（供 Codex 执行）

- [PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md](PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md)：Pro 对 v1 的完整审查（CHANGES_REQUESTED_BOUNDED）。两处事实纠错已本地复核为真。
- [HSP90_FIRST_ROUND_PLAN_V2_ZH.md](HSP90_FIRST_ROUND_PLAN_V2_ZH.md)：v2。一个问题（Q01）、同一 Agent、A/B 各两次共四份、C 停、7 个工作日、≤ $0.20；评分依据独立于规则选择；`common/ arm_B/ hidden/` 三分隔离；三列核对；两层报告；四结果表由 PM 决定下一步。§11 逐条处置 Pro 意见。
- [REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md](REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md)：给审阅者的提示（十问，强调执行者是 Codex）。
- `THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md`（v1）已标 superseded，保留为记录。

## 2026-09-09 深夜（二）：Pro 审查 v2 → v3 交付版（供 Codex 执行）

- [PRO_REVIEW_OF_PLAN_V2_ZH.md](PRO_REVIEW_OF_PLAN_V2_ZH.md)：Pro 对 v2 的完整审查（CHANGES_REQUESTED_BOUNDED，"改几处后执行，不再重做路线设计"）。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3 交付版。范围、规模、费用上限、七天到期与 v2 相同。改动：运行器显式 `--task-root`、A/B 去掉公开事实依赖、共同提示改指实际文件、挂载断言按实际可读范围、`FIELD_DEFINITIONS.md` 七条字段含义（每轨迹三行、departure 相对第一个持续方向、帧数式时间约定）、B0 分"论文声明 / 本轮输入已核对"、元数据角色改为"开发者整理未经领域确认"、核对看全文、§8 加"混合/负面/不稳定"行、选择器失败与运行器修改两个分支、B4 跳过。§11.1 逐条处置 Pro 意见；§11.2 列本机核实 v2 引用后新增的修正（注册表实为逗号分隔、选择器状态门槛、旧 readiness 为 false、Docker 镜像无构建记录、无 MDAnalysis、AMBER99SB 出自 Zenodo 描述、主张矩阵是指针文件、收敛题输入的真实位置等）。
- [REVIEW_PROMPT_HSP90_FIRST_ROUND_V3_ZH.md](REVIEW_PROMPT_HSP90_FIRST_ROUND_V3_ZH.md)：给审阅者的核对提示（六问，只核对处置是否到位，不再审路线）。
- `HSP90_FIRST_ROUND_PLAN_V2_ZH.md` 已标 superseded，保留为记录。

## 2026-09-10：Pro 审查 v3 → v3.1（交付版，直接交 Codex）

- [PRO_REVIEW_OF_PLAN_V3_ZH.md](PRO_REVIEW_OF_PLAN_V3_ZH.md)：Pro 对 v3 的审查（CHANGES_REQUESTED_BOUNDED，主要处置已到位，五处局部文字修正后执行）。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：已就地更新为 v3.1，§11.3 逐条处置：A1 先于 A0、规则渲染保留对象与检查配对、B0 来源差异分别保留、字段定义移出汇总结果与答题提示、A-only 分支贯穿 §5–§7。这是交 Codex 执行的版本。

## 2026-09-10：v3.2 一次授权、条件推进（明天开工版）

- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3.2 = v3.1 + §1 授权 1–9 + §8A 自动判定规则 + §14 第二、第三体系的条件推进（顺序、不并行；只读盘点后按写死规则选 ADK 或 DHFR；总停止线 21 个工作日 / $0.60 / 4 GB）。PM 贴一句"授权 1–9，按 v3.2 执行"即可开工。
