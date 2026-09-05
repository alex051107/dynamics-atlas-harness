请继续作为独立科学与工程审阅者，帮助我们让 Rules、连接的 Operator 和必要额外计算，真正以高正确率回答原20个论文科学问题。你可以审查整个仓库、任意原题、全部相关论文/数据/方法，自由使用所有可用工具、运行反例和科学计算；不限制问题数量或审查范围，也可以推翻我的优先级和完成条件。请区分实读、实算、未验证并引用来源。本轮不需修改GitHub，建议由我独立核验实施。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
固定head：2ced6352fd1c7ea0a8013fa093b241ed840bf218
你上一轮审阅16f81d8并给DIRECTION_PASS，本轮已经完整保存pro_review_round21/reply.ax.txt和reply.md。PR仍OPEN DRAFT未合并。原20题仍1完整开发(Q01)、4部分(Q05/Q09/Q15/Q16)、15未科学运行；最终人类批准0，整体准确率未测。on/off只验证控制关系，不是正确率增益。Q15旧验收修复冻结，Q09不再追D24，Q01保持冻结。

优先入口：research/paper_result_reproduction_screen_v1/CURRENT_STATUS_ZH.md、README.md、questions_20.json。以下相对路径均在该research目录下。

1. 你的Q16 fit列选择问题已实际核对并修复。
q16_observation_independence_v2/report.json记录原完整XLSX的14块time+observed与旧time+observed+fit全部行集合和差集：全部相同，实际观测值相同，新payload与既有source_admission的input_id相同。因此0科学重跑，原比值保留。
生产模块src/dynamics_atlas_harness/q16_source_extract_v2.py将processed(time,observed)与fit_audit(time,fit)独立提取。3个定向测试覆盖fit尾部/内部缺失、观测缺失及fit数值变异。旧v1提取记录保留，不用于随后观察数据入口。
338项本地回归在既有py311科学环境PASS；第一次误用了系统py314，因缺pymbar产生8import错误，切回已有环境后通过，未安装依赖。CI请按当前head读回。任务审计脚本快照保留本地任务目录布局依赖，源码供审查；生产模块和tests可在仓库运行，未上传原始工作簿/曲线数组。

2. 有新的真实Q15换染料观测，不是作者最终拟合均值。
此前查不到原始TMR双标APBS；现在从原论文PDF physical7 Figure4d右栏提取独立灰色实测事件直方图柱形：apo35、holo33，共68柱。图中平滑Gaussian曲线、印出的mean/sigma和4e距离均排除。pdftocairo的SVG原页只本地保存，筛选精确灰色矩形路径/页坐标/面板位置；祖先transform全部核对为空，完整原图和柱形重建图视觉核验。
q15_tmr_histogram_intake_v1/report.json和脚本记录角色、轴框、限制；q15_tmr_histogram_direction_v1/report.json、REPORT_ZH.md、measured_histograms.png和脚本给实际计算。
按柱面积归一化，以各自图框宽度作坐标：apo重心0.340522、holo0.477327，差+0.136805。柱内位置界限再扣除每面板一整柱宽的配准偏差，差下界仍+0.075481。加配体后右移，与既有Alexa175/228 APBS组均值下降方向相反，且在各自稳定读出条件下与DEER缩短方向相容。
没有把这些数当精确E、采样CI、三个独立重复或绝对距离；这是作者公开的代表性处理后观测，不能核验原事件选择/完整校准。本轮是手工首次处理观测，0Rules-extra，尚未把它冒充规则收益或完整Q15结项。
请审查这种处理后观测是否足以完成原题哪一部分、是否需要补何种真正会改变判断的校准/各向异性/寿命证据，以及如何接回已有规则的剩余义务而不增建框架。原图4c有实测各向异性/寿命，相关小数值文件也在本地，但部分来源175/165及配体标签冲突保留。不要为了唯一微观机制才允许结束，也不要降低真实观测的适用性要求。

3. Q16原定反演前向核对出现差距，保留失败，尚未做长短记录反演。
q16_forward_method_audit_v1/report.json、REPORT_ZH.md、脚本：用10条唯一条件的作者存档中心P(r)重建对应作者fit列，只作METHOD_AUDIT_TARGET，绝不把fit或P(r)作为科学主计算目标/已知蛋白状态。Fig5 physical8明确Å，而workbook写nm；预先固定source_r/10到nm，没有调轴追fit。
使用标准4pulse isotropic two-spin Fresnel kernel，物理常数326.983345946672 rad/us nm^3；1024点独立方向积分最大差7.9e-15。中心P(r)梯形归一化，唯一拟合是10次解析两参数offset/amplitude，0迭代优化。
预先选择相对fit幅度范围0.5% RMS作为“是否可直接接上原方法”的审计容差，不是实验噪声阈值/科学显著性。10曲线相对RMS1.15%-3.75%均不达此容差。完整失败已保存。作者存档中心分布和fit是否来自同一估计、validation平均/导出/原DeerAnalysis2018具体配置尚未确认。不能由此断言论文或软件错误。
ETH官方页面提供2019作为2018 bugfix继任；只尝试小范围请求源代码，公开ZIP链接404，首个请求即停止；没有下载128MB整包/安装软件。
请独立判断差距最可能来自哪一项可核对方法/源角色，而不是盲目降低容差。也请判断我是否过度要求与作者fit一致才允许做一个明确条件的本地可辨识性分析。你的Pro21建议是先在真实raw记录层截短，然后重新处理背景/调制深度等，报告长距离贡献的条件允许范围，再讨论结构归属。我接受这条方向；目前新方法审核失败应如何影响这个下一步，需要科学依据。不可把缺holo spin参照误当所有信号计算都不能做，也不能跳过模型失配。

Q16已有同窗排序仍只称观测层面，不称人口效应/构象因果。你指出dshape^2=2(1-rho)和噪声反例已接受。请继续关注真正的科学证据、模型适用性、原20题覆盖/正确率，以及怎样最快形成可信完整答案；不必局限上述三组文件或我提出的解释。
