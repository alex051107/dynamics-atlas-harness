# Rules Table 列说明

33 条候选规则、11 个 paper_id。文件后缀是 `.tsv`，实际为逗号分隔 CSV；读取时用 CSV 引号规则（如 Python csv.DictReader 默认设置），不要按制表符拆列。原始字节保留。条款状态不是科学通过记录；required_fields 和 integration_operator 也不等于本轮 Agent 实际读取或执行。

| 列 | 含义 |
|---|---|
| `rule_id` | 规则唯一标识 |
| `paper_id` | 来源论文唯一标识（共11个） |
| `paper_title` | 历史短标题，完整书目见文献清单 |
| `source_locator` | 原文页／图／节定位 |
| `rule_class` | 规则类别 |
| `source_classification` | 原文证据分类 |
| `gate_path_semantics` | 进入检查路径的语义 |
| `gate_primary` | 主要检查路径 |
| `gate_path` | 完整检查路径 |
| `paper_finding` | 原文发现 |
| `proposed_project_rule` | 项目提出的候选条款 |
| `required_fields` | 条款需要的信息 |
| `integration_operator` | 对应分析／整合操作 |
| `requires_numeric_threshold` | 是否需要数值阈值 |
| `acceptance_rule_status` | 接受判据的成熟状态 |
| `model_or_support_validation_required` | 是否另需模型／支持度验证 |
| `validation_route` | 满足前提后的验证路线 |
| `abstain_route` | 资料不足时的弃权路线 |
| `transfer_scope` | 允许迁移的范围 |
| `project_status` | 项目内状态 |
