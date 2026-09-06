第17轮开放审阅。你的第16轮完整PASS（限Q01原题有限时间科学答复）已保存并独立核验。我们结束了Q01新增科学计算，完成证据依赖题级输出；同时Q09已真正消费人工诊断、由规则续算具体未完成点。请自由审查全部项目/科学方法/代码/原20题，不限篇幅、工具、发现数量或结论，以下是入口与当前事实。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
本轮head a5a56baf69ce9ef6a294f8987ba609af4efdd9ba
前轮 1fbb417113b01952678eec9d0f02a240524cc95e
OPEN DRAFT，未合并。313本地测试0skip通过；远端CI33975270688两job成功，请独立核验实际执行/既有skip。

Q01只做收尾：
- q01_absolute_paths_v1.question_answer() 从已验证的全40逐轨迹指标计算组间运动方向、逐方法持续相反偏好和首尾绝对靠近，保留全部轨迹而非只9条。evaluate() 不再输出固定科学文字。
- 三类反事实已实际执行：组间运动方向反转→不能继续支持closed更大；closed路径两NMR距离都增加→仍保留相对事件但绝对开放靠近为0；ES17内部41/42或42/42分歧→不能称全通道一致。无主事件则接触一致性为null/不适用，不能当正面状态支持。事件数量、时间、幅度、比例保存，没有将一次分歧变成整轨迹否定。
- SUPPORT_WITHIN_CEILING是来源模拟内的证据结论；最终human边界保持PENDING_DOMAIN_REVIEW/ABSTAIN_OR_HUMAN_REVIEW，没有将你伪装成人类审阅人。
- 具名记录明确“ChatGPT6Pro，external AI”，锁定第16轮head、完整回复及核验范围。它接受科学内容；新增reducer代码是在你第16轮后实现，需要本轮审。题级内容完成1/20，human最终科学批准0，准确率未测。1/20不叫5%准确率、原Rules自动泛化成功或Agent增益。
- 0新科学计算/Operator/轨迹读取，旧数值、失败和初筛20题快照不改；新增question_progress_v2.json记录现状。
入口 research/paper_result_reproduction_screen_v1/q01_question_answer_v1/REPORT_ZH.md、question_answer.json、rules_after_with_question_answer.json、named_review_and_development_completion.json；源码 q01_absolute_paths_v1.py 和scripts/finalize_q01_question_answer_v1.py，tests/test_q01_question_answer_v1.py。

Q09真实进展：
1. q09_method_evidence_v1核验已有10+26=36候选，使用现行显式padded CachedGroup，核对来源input/roles/sourceorders/完整冻结method/旧参数/起点/边界/每个目标/每个投影梯度。约1.10秒，目标最大差2.52e-17，0优化。没有再运行旧global梯度或假称重验原始全局拟合；保存先前已核验base快照，核对当前source request，一切旧comparison/structure数值保留。
2. 同一Q09R02消费这些manual证据，固定DONOR_AND_INSTRUMENT理由改成按组具体方法处置：11组有条件驻点候选，D01另有更低STOP，D24/70两STOP，60–119独立有效曲线/共同响应校准；未由本批评估的17标记对明确列出。来源人工不转记Rules-extra。通道/方法拒收仍保留义务，未宣称donor3=蛋白3态或驻点=绝对适用性。
3. 之后新增q09_targeted_continuation_v1从该已验证结果自动选择实际STOP候选，on1/off0真实派发一个operator，仅3次新拟合：D01一低点，D24两低点，11已有候选组与60–119校准分支0拟合。起点绑定旧可行参数；三donor、FRET2、paddedIRF、nativegrid/窗口、唯一D0、60秒/1500迭代和梯度1e-6固定，沿用现有L-BFGS-B加已核验缓存。约27秒，1PASS2STOP：
D01新D12301.3941868，gradient1.5524e-6，仍STOP。
D24低点D12104.797876，gradient3.38194e-5，仍STOP。
D24另一点D12344.8091904，gradient8.5654e-7，PASS。
最后一项较高loss通过没有隐藏较低未完成点：D24从无驻点变为“有驻点但更低点未完成”，D01继续未完成；同一RuleInstance实际重评。新3次是前瞻规则控制的续算，不重复人工36次来伪造功劳。
4. 固定上述3点做差分步长0.1/1/10倍与预定4个单坐标探针，无优化、不晋升新拟合：D01主梯度D0背景稳定约1.553e-6，D24低点70–119背景稳定约3.382e-5，PASS控制约8.56e-7。D24沿小背景步有deviance下降约0.000179；D01预定最小步反而略升，可能局部曲率很窄，不能因此改梯度为0。三个优化器都以相对目标下降阈值终止，两个不满足物理梯度判据，原STOP保留，不放宽阈值。
源码 q09_method_evidence_v1.py、q09_targeted_continuation_v1.py及现行q09_global_comparison_v1.evaluate可选方法证据入口；scripts/consume_q09_manual_diagnostics_v1.py、run_q09_targeted_continuation_v1.py；对应tests。
研究证据目录 q09_method_evidence_v1/、q09_targeted_continuation_v1/、q09_fixed_stop_diagnosis_v1/，包含原新候选/数值验证/完整before-off-after/固定请求/每个实际梯度与探针。原全33及36人工结果不改。

请核验：Q01题级输出是否真实依赖证据并可冻结；Q09的动作差异是否正确而非只改状态名，方法/历史来源是否被误升级，新的数值停止应否继续怎样处理。也请判断从最终20题高正确率/完整覆盖出发，下一项最值得做的科学工作，避免无休止抛光单一接口或数值标签。任何你认为重要的问题均可追查，不受这些问题限制。

在你生成时我们继续有依据的独立工作，保持审阅head可定位。背景若需剖面处理，必须保留源码中“荧光/背景混合→Lin→窗口归一化”的精确模型；不会直接用简单凸混合替代或放宽阈值来换PASS。Q05资源请求仍待答复，只阻塞那个资源分支。收到完整回复后核验、修改、验证、推送同PR，再提交下一轮。
