第15轮开放审阅。第14轮完整DIRECTION_PASS已保存并独立核验。本批已推进Q01完整40条真实轨迹，以及Q09的具体方法对照，不只改接口。请自由审查整个项目、科学解释、代码、数据方法、原20题路线和当前优先级；不限篇幅、工具、发现数量或结论，不必仅检查下列内容。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
新head 5e962ea75adbaf2be87ef81661248d7d666fd483，前轮 bfa54f45616988a99d3deafd172640373bf4944f。OPEN DRAFT，未合并。295本地测试0skip通过，远端CI33968607852两环境各295含2既有workspace-only跳过成功，merge ref前缀71def42。请独立核准。

Q01来源边界已查清：SI Table2原PDF页4–5视觉核对，O04/O10有c,f（R46A未观察、明确不用于MD），O15有d,f（R60A未观察、明确不用于MD），O23/O24有e,f（WT未观察、明确不用于MD）。因此19open+5closed是SI自己的MD子集，没有填不存在的阈值。作者Clustering.zsh是backbone及residue40–97/137–220对齐、98–136lid；MDTraj原始源和文档明确backbone为N/CA/C/O、residue为resSeq。新计算显式选四种原子，不再用旧Cα坐标，也未冒称重跑TTClust。

实际40次现有gmx traj，每次同时提取同一XTC的选定原子和盒矩阵；每条1001帧，20–1020ns。甲基三等质量H中心、源PBC最小镜像、单位转换一致。两阈值共享同一距离，每条对照作者存档pseudo-COM评分；全部通过，最大差0.005001660Å，预定容差0.011Å。主链相邻C–N最大.147221nm；所有原子/时间轴验收保存。无新MD、依赖安装或大下载，0重复轨迹读取。原始PDF/ZIP/XTC及提取的原子坐标数组未上传；完整衍生距离/RMSD、映射、命令、路径及回执已提交。

第一项新窄Q01 CASE规则先实际触发同距离双阈值比较：on1/off0，同实例数值重评。我们在看40条分组结果前冻结“自身NMR20模型留一最近lidRMSD最大值+自身接触均值最大值”的construction包络，要求几何和接触都支持同一态。真实失败是40/40起点都在范围之外！原始输出及错误的“路径判决未变”措辞留档，当前明确这是未建立初始范围支持，不能答离开哪个状态。不能把这个全体不分类算合理科学弃权或成功增益。

同一RuleInstance随后从已核准的全体初始范围缺口触发一个不同估计量的跟进（on1/off0），复用40条衍生数据，0新gmx/优化。第二方法在看分组偏好结果前单独冻结：几何margin=d_closed-d_open；接触两通道分别用NMR开/闭参考均值差归一化，再等权投影，避免直接比19接触/5接触的未校准均值；两者同号才判相对参照偏好，否则保留冲突。前一范围外事实不删除，不放宽范围追论文人数。这里明确是exposed development方法修订，不是heldout、状态归属、概率或原作者离散类别。

这个完整时间路径比较得到：
- 主判据20连续采样点（实际采样跨度19ns）：20open-seeded均未持续丢失开放偏好；20closed-seeded中9条出现持续open偏好、1条持续丢失closed偏好但没有相反参照一致支持、10条未持续丢失closed偏好。
- 5点时closed组10相反偏好/1冲突/9保留；50点时8/2/10。
- 两套接触阈值在这三种持续性条件下的全部轨迹类别相同。逐帧偏好有342个差异，20点主类别变化0/40。没有因此宣称Rules准确率增益。
- 每条完整路径、首次相反偏好区间、最长连续段和返回均可审，图在q01_relative_paths_v1/full40_paths.png。
这是有界的方向差异证据；我们暂未把完整题级科学验收从0/20加一，因为相对偏好、状态支持和论文“亚稳性”的解释还需审查。请直接判断目前哪些原Q01子结论已经足够回答、哪些仍缺计算或定义；也请挑战这次reference-normalized projection/持续性设计是否在回答目标，是否又发生方法-问题错配。不要因为它不是平衡轨迹就要求补平衡速率，也无需迎合我们现在的计数。

源码：
src/dynamics_atlas_harness/q01_path_comparison_v1.py
src/dynamics_atlas_harness/q01_relative_paths_v1.py
scripts/run_q01_path_comparison_v1.py（prepare先于run）
scripts/run_q01_relative_paths_v1.py（先冻结修订再运行）
对应两项test文件。
证据research/paper_result_reproduction_screen_v1/q01_path_comparison_v1/、q01_relative_paths_v1/。先看REPORT_ZH、frozen_method/policy、numerical_report、rules_before/after、source_method_review。full_paths/full_preference_paths各40040行，完全可查；每轨迹measurements.npz含24接触距离和两参考RMSD。原20实例0数值义务基线q01_rules_baseline_v1未改；这些新CASE规则不冒充原规则包或跨题泛化。

Q09在你第14轮生成时已完成：
1) 60–119在显式padded_linear_v2下10次新局部拟合全部满足驻点判据。分别D0/DA的有效双指数总D49446.949，共享donor零FRET和4个FRET2起点均D213413.964、f0=1。主共享冲突集中5–20ns，D0自身仍有系统偏差。单独DA是有效曲线形状，不是已确认新donor光物理，更低loss不能直接证明样品/参考错误。保存30个固定时间区段残差。
2) 我们独立算了条件潜在平均发光时间：分别有效模型D0=2.050815ns、DA=2.375665ns；与你提出共同donor必要条件一致，但这是条件拟合的解析矩，不是校准稳健的原始数据反证。未直接比raw均值，未宣称已做common-IRF卷积检验。
3) 13个来源三donor/原二donor组，各两起点共26拟合。13个2→3精确嵌入通过；23PASS，3stop（D01一个更低可行点未完成，D24/70共享两起点未完成）。FRET仍2，参考只计一次；D70原共享三/二阶配置仍UNKNOWN。这不是3蛋白态或恢复论文作者配置。
这两批是手工方法诊断，尚未计Rulesextra；代码中当时临时绑定padded策略的方式在method和execution_source明确标注，未冒称正式all33方法迁移完成。

为去除全局梯度重复计算，新增很窄CachedGroup，正式显式shift_policy=padded_linear_v2，缓存未归一化寿命和(tau,R)核，混合后才IRF/Lin/总计数归一化，128entryLRU。真实D01三donor两标记组全参数扰动和shared3全梯度对照：预测相对差7.11e-16、梯度缩放差3.75e-11、目标差6.94e-18；一次冷/热梯度速度约2.14/2.16倍，仅一组microbenchmark，不宣称全33速度或收敛。0优化。
Q09证据在q09_60_119_response_diagnostic_v1/、q09_donor_order_groups_v2/、q09_cached_group_v2/，源码q09_cached_group_v2.py及对应测试，旧全局/两变体拟合不重跑。

请继续审科学方法、真实Rules因果作用、现在是否值得把这批方法结果接回Q09处置，以及下一项能最快推进原20题完整作答的工作。我们会在你生成期间继续可独立推进的工作，收到完整回复后核验、修改、再提交，不再因为一轮结束停住循环。
