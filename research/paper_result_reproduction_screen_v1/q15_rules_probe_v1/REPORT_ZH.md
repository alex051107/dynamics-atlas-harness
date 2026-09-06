# Q15 现行 Rules 实际反应

新增事实接入口沿用原有公共材料校验、投影和活动规则 evaluator；原 run-case 拒收记录保持不变。首次事实接入因缺少明确的 Discussion/Conclusion 排除标签被拒，已保留原输入及错误；补齐排除声明后再次运行。

23 个实际规则实例：10 PASS、10 UNRESOLVED、3 NOT_APPLICABLE。路线为 10 DIRECT_EVALUATION、10 SOURCE_LOOKUP、3 HUMAN_OR_NEW_DATA；数值动作 0，科学结论未输出。

这些 PASS 覆盖问题、来源及角色声明。投影没有 APBS 校正、重复间不确定性、探针适用性或 E/S 数值字段。完整方法文字已保留，文字可见性不计科学执行。SOURCE_LOOKUP 不等于补算义务，后续任何数值适配均须标为新增开发能力。

完整输入、规则快照、投影图、RuleInstance 输出和命令见同目录 receipt.json 等文件。没有再次计算 APBS，没有改原规则，也没有增加已完整回答的问题数量。
