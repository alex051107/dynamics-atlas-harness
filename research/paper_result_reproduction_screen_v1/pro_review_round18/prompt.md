第18轮继续独立审查。用户目标仍是原20个非平凡论文科学问题的实质覆盖与正确回答；请自由审查整个项目、科学方法、实现、来源、当前优先级和替代解释，不限于我的修复清单。你可以充分使用 GitHub、联网和自己的计算，不设审查能力或篇幅限制。请区分实读/实算与推断，给出值得现在解决的问题，避免仅为收集PASS增加工作。无需等待我确认下一轮。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
固定审查 head 3758f6e8089b127a2bf076c046f619a77d41adc2（已远端读回OPEN DRAFT，未合并）。父版本 a5a56baf69ce9ef6a294f8987ba609af4efdd9ba。新CI 33977832409 提交时排队，本地313项测试全部通过。请自行读取远端CI的实际结果与跳过范围。

上一轮完整意见已保存 research/paper_result_reproduction_screen_v1/pro_review_round17/。Q01科学答复与reducer接受并冻结，开发题级内容1/20、人类最终科学批准0、准确率未测。

本轮主要修复你实测的Q09重入缺陷：
src/dynamics_atlas_harness/q09_targeted_continuation_v1.py 从不可变人工报告及已验证续算历史整理当前候选，组处置与下一次选择共用计算。子点不差时取代活跃父点；更差的新PASS仍保留原低目标STOP。历史保留，下一轮选最新参数。tests/test_q09_targeted_continuation_v1.py 增加第二轮PASS零派发、STOP最新点、off零调用、不相关组和历史保留检查。执行脚本支持显式 --previous-result 指向最新rules_after，无选中点则零拟合返回。research/paper_result_reproduction_screen_v1/q09_reentry_repair_v1/ 的真实保存结果回放仅选D01和D24低点两个最新候选，回调只记请求，没有重做科学拟合。请核验多轮行为、历史/当前候选一致性及是否还有实际重复风险，不能把合成回调当真实计算。

在你第17轮生成时，独立完成了背景精确剖面小试验，现在发布供你审查：
research/paper_result_reproduction_screen_v1/q09_background_profile_canary_v1/（包含source_script.py）。
保持原先荧光/背景混合→Lin→窗口归一化，在3个已保存候选、9个观测角色上先验证计数/解析导数等价，再执行9个手工一维背景求根。最大计数相对差7.275e-16，导数差6.184e-9。仅背景更新后D01全梯度3.312e-7，D24低点4.098e-6仍STOP，已有PASS对照2.561e-8；原模型、原阈值。0完整FRET拟合、0Rules-extra，未替换正式候选，也未宣称Q09科学完成。请判断它对实际科学预测/参数是否有必要价值及如何小范围处理；不要为了标签把它扩成新平台。

Q15已开始来源工作，不等Q09所有数值标签：
research/paper_result_reproduction_screen_v1/q15_calibration_intake_v1/。
Peter SI已下载原PDF并用安装的pdftotext转一次MD；Table3物理21页AF555/647校正参数已视觉核对。Hellenkamp2018第10页公式14/18–21已复用现有MD并回看PDF，公式事实单独保存。原PDF在工作区，不上传原始受版权资料；请按你的访问能力独立核查来源。
精确重清点既有Figure3成员回执：66成功=63DCBS+3背景，0APBS；13失败=6APBS+6apo第三重复DCBS+1背景。已有74,318行是DCBS，不能冒充论文APBS/150光子筛选结果。仍需时长单位、背景积分/占空比、APBS筛选及重复/校准适用性；没有把作者拟合E或距离当输入，也没有新拟合。原Q15入口拒收先前已保存，不能冒充规则漏判。

请继续给出当前科学/实现判断以及原20题整体最值得推进的下一步，尤其Q15如何用最小真实数据与正常位点对照区分探针问题和构象变化。你上一轮指出的PDB图注次序与175位点不能一概否定的边界会保留。审查不构成合并或人类最终科学批准；用户已授权同PR持续修复/提交/审查循环。
