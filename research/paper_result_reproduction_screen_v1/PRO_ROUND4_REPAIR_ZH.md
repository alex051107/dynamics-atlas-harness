# Pro 第四轮修复与数值审计

第四轮完整回复已归档在本地任务，审阅对象为 e04f260c8418f502473ee07b754166f7b0e4493e。GitHub 工作流 33941686359 的三处失败已独立确认并修复。

- 来源未验证现在进入已有 SOURCE_FACT_MISSING 粗分类，测试保留精确理由 SOURCE_PROPOSED_LINEAGE_REQUIRES_VERIFICATION，后续动作包括具名来源核验。不是声称论文不存在。
- 当前 source-science 视图同步当前合同；历史运行数据不重写，reviewer_form.json 完全未变。
- 历史覆盖测试校验原 manifest 对应的七份冻结 Rules 文件，来源为其 baseline_commit；原 manifest 哈希不改。当前行为另由运行测试覆盖。
- 平台 authority 可携带非空 validation_claim 和可选 validation_lineage_status；缺少请求则不触发，缺少来源则 UNKNOWN。Agent 提案不拥有这些字段。完整入口分别测试声明独立、同一数据、未知独立性、缺少来源，结果为 PASS（仅标签）、FAIL、UNRESOLVED、UNRESOLVED。
- 联合拟合对照把其他可比性前提全部设为满足：QUALITATIVE_TRIANGULATION 可获声明 PASS，仅改为 JOINT_ENSEMBLE_FIT 后保持 UNRESOLVED。

本地完整测试 238 项通过。新增诊断只涉及声明/适用性与测试版本，尚未产生 Rules 驱动的数值义务。二十题完整科学回答仍为 0/20；其他十九题尚未运行。

## 科学证据与下一步

[固定作者权重审计](q05_author_weight_audit_v1/REPORT_ZH.md)恢复 422/422 个已发布预测值。NOE 汇总 6.50542 与论文 6.0 的差异仍在。对原始输入独立清点：292 条酰胺记录仅 237 个唯一完整记录，55 组各出现两次，预测矩阵相应列完全相同；甲基 40 条均唯一。未删除或降权；需核对重复是否表达作者的对称/多聚体或权重设计。逐项预测已匹配，先查汇总定义及重复处理，不能直接认定为优化器根因。

下一实质实现是让现有 Rules 触发一个共同系综 SAXS/NOE 数值检查；Operator 先返回残差、目标分项、权重集中度与来源身份，科学判据须有明确依据。未知配置保留在结果中，不用作者权重替代本地求解，不设任意阈值追逐论文数字。规则开关对照及同一 RuleInstance 重评仍待执行。

## 验证记录

本轮：1 次 preflight；1 次组合冻结文件导出/视图生成/重复记录清点；1 次完整 unittest（238 项）；1 次发布材料检查。七份旧文件按原 manifest 在导入时校验；没有重复科学回算、优化、R0 改写或人工审核表重置。Pro 下一轮可自行审查所有相关代码、原文与设计，不限制发现数量和范围。
