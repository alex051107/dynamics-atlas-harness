第19轮开放独立审阅：请继续自由审查整个项目、原20题、科学方法、代码、证据和下一优先级，不限于下列变更，不限制篇幅、工具或发现数量。目标是实质科学回答的正确率和覆盖，不是收集工程PASS。你可以自主读取GitHub、原文、做自己的核验；区分实读/实算与推断。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
固定head 4e0ac1c6d793eb97349b0683b17d12998c589784；上一审查3758f6e8089b127a2bf076c046f619a77d41adc2。实际代码提交a037c2734b175ad8b1b41f7ed8ccf403b7ed9b59，随后只把发布的工作簿目录缩成表头（此前数值字符串被归入text_cells，完整目录仍在本地）。远端head已读回OPEN DRAFT，未合并。本地319测试全部通过；CI33981551473提交时运行中，请读实际日志。前代码提交CI33981509916也可核验。

Pro18全文保存在research/paper_result_reproduction_screen_v1/pro_review_round18。已完成你要求的一批：

1. Q09文件一致性与零动作衔接：
q09_targeted_continuation_v1.history_reports/verify_saved_history 检查最新与历史一致；整个被消费的历史以evidence_result中的history_report_ids绑定，兼容既有单报告证据。连续零动作沿用原证据文件，不制造数值证据。test_q09_targeted_continuation_v1有旧历史局部变异拒绝、两次真实CLI零调用（明确源加载stub、禁止拟合）、最新STOP和off测试。请核验实际文件路径及多轮状态，发现问题照常指出。

2. Q09人工背景派生点进入同一实例：
scripts/consume_q09_background_candidates_v1.py 与q09_background_admission_v1/。对已经保存的3个背景派生点核验原曲线目标、完整梯度、父候选和非背景参数不变，0新拟合/求根/Rules-extra。D01接受条件驻点，D24低点仍STOP；下一请求仅D24低点最新参数。人工来源独立标明，没有虚构full-fit optimizer_success。科学状态数仍未解决，不用旧全33比较替代新方法比较。

3. Q15现在已有实际APBS观测结果：
新模块q15_apbs_comparison_v1.py、runner scripts/run_q15_apbs_comparison_v1.py，以及research/paper_result_reproduction_screen_v1/q15_apbs_comparison_v1/的report、source_manifest、method_source_facts、图和回执。
实际取得175/228的69个APBS、55/175正常对照71个APBS，两对位点各apo/holo3个源标记重复。140文件共364326事件；原始AA+DD+DA≥150，先背景再α/δ/γ/β，0.25<S<0.75，选44451事件。不是DCBS重命名。Source-compatible背景和时长口径由实际匹配的公开ALEX Suite代码支持：
https://github.com/DirkHaehnel/LABViewlib/blob/49dfef079129696e84c4983ecc330d7b5d60e71b/SIMA_NED_Version/py/ALEX-Suite-1.2.0/alex/models.py
144–146定义背景counts/ms，602–605乘Tau*1000；merge_bursts.py的13列dtype及arrival*time_resolution对应导出，模式0/50光子默认匹配。Peter2022精确二进制版本仍未知。该旧软件有负值裁剪（索引也可疑），本次按明确Hellenkamp公式不裁剪，保留180个选中事件负校正计数和715个E区间外值，差异公开记录。请审查这个方法是否合理以及它如何影响结果，不能把它当作原作者精确执行版本已确认。

首次主计算数值（不是Rules-extra）：
175/228 apo三重复平均E .339156，holo .312987，ΔE -.026169；所有交叉重复差[-.076140,+.040806]，下降不是跨所有重复稳健。
55/175 apo .724613，holo .806602，ΔE +.081990；交叉重复差[+.053158,+.128408]。这是描述性范围，不是CI；不把burst数当独立实验或把闭合方向硬编码。
逐文件/重复E–S摘要和E直方图、超范围诊断全部保存；未拟合Gaussian、未用R0换距离、未推断蛋白结构域闭合。

4. Q15一个确定来源缺口：
完整13.11MB发布XLSX已用仅2.626MB尾段补齐，重叠一致，全部50ZIP成员CRC通过。Figure4的AE:AL E/Events列只有前三行标题，完整XML第四行后没有任何值；所以TMR/Cy5双标直方图并非我们漏下载，当前发布工作簿确实缺载荷。另有单染料anisotropy/intensity，但不是双标换染料对照。原Q15入口拒收保持，完整题未回答。已有作者处理后的DEER时间曲线/分布来源可供下一步适当计算，不能改用Cα距离替代探针模型。

请判断现在最值得做的Q15实际规则义务与额外证据：已经冻结首次主计算，尚未把任何人工额外诊断冒充Rules功劳。需要根据实际结果触发可执行义务，并保留条件支持、冲突和不确定性；不能把“含175”一概否定，也不能先设定染料问题就解释一切。请同时看原20题推进是否仍过慢/过度针对单题，以及是否存在更有效的覆盖策略。Q01继续冻结，完整开发内容1/20、人类最终批准0、准确率未测。用户已授权连续同PR修复/提交/审阅循环，不需逐轮许可；本审阅不构成合并或人类最终科学批准。
