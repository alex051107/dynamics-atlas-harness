# Receipt检查范围字段勘误

冻结运行器的receipt.check_scope沿用了旧D/P/R文本“no deterministic scientific checks in any condition”。这项常量对E2的FEEDBACK条件不成立。实际调用路径在agent_run.py accept()中：第一次合法submit且arm=FEEDBACK时调用ceiling_check.check_submission，并写入ceiling_feedback事件，再把checks反馈给Agent。

保持已冻结代码、原receipt及原答不变。最终证据表必须用实际ceiling_feedback事件与反馈轮次核对检查是否发生，不能用这个过期字段推断“未检查”或“已检查”。其他条件没有该反馈调用。发现时E2已运行，因此修订只作为旁注，不修改冻结实验或重跑。
