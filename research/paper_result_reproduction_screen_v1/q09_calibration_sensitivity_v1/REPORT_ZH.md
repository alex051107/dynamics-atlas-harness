# Q09：IRF校准敏感性已由真实规则派发

同一22–127原始DA/D0数据下，IRF处理改变了推导的短距离组分和donor-only系数。规则从已验证的仪器背景缺口产生可执行补查，完成后返回同一实例。完整Q09蛋白状态数和结构一致性仍未回答；原20题完整答案仍0。

## 本轮观察

| 条件 | 联合deviance | 两距离均值 Å | donor-only系数 f0 | 数值状态 |
|---|---:|---:|---:|---|
| 保留原始IRF中位数0处理 | 13880.048 | 41.570 / 19.727 | 0.4373 | VERIFIED |
| compact_3_7ns | 13624.016 | 42.314 / 22.683 | 0.5027 | PASS |
| adaptive_full_axis | 13570.385 | 42.195 / 22.340 | 0.4975 | PASS |

两个校准假设的均值拟合均通过预定局部梯度检查。每假设另做4个固定种子校准Poisson实现，固定真实DA/D0计数；8次中7次通过，compact/91003梯度3.96e-5高于1e-6，保留为NUMERICAL_STOP，未混入接受的参数范围。全部12次优化包括2个额外固定f0=.8分支起点；两者局部通过并仍得到约28508.119的同一较差合并距离解。这只增加已找到的局部存在点，不证明f0=.8被全局排除。

局部义务状态为PARTIAL_SENSITIVITY_WITH_NUMERICAL_STOPS，不把一次未收敛拟合藏在平均数里。两种均值条件和有限校准实现已足以显示对IRF的依赖；这一批有界诊断结束，下一步可以带着这些限制进入跨变体条件模型比较。

## 校准方法和边界

校准模型为独立Poisson(h+b)，每个IRF各自使用原先固定首/尾256bin估计常数背景，D0=.33203125、DA=.34765625计数/bin。两假设分别限定响应3–7ns、允许全轴响应。分组仅由原始IRF生成：目标256光子、最长128bin、3/7ns切断，之后所有实现固定分组。组内非负Poisson均值估计h=max(组均值−b,0)。这种截断估计可能保留有限样本的正尾部偏差，不能叫无偏净IRF。原始IRF、原数据、既有拟合均保留。

固定种子91001–91004；每个角色每实现抽样一次。每次重新估计同一背景和分组响应；均值拟合及复制条件均保持donor3/FRET2、原物理范围、1500iter/120s、梯度1e-6、sigma6Å、scatter0、非周期卷积。这是校准敏感性，不是样本与校准联合CI；没有按DA拟合改善或论文目标选择校准假设，也没有确定真正的背景或尾部。作者实际原配置仍未知。

## 快速成分与散射

当前基线的潜在积分份额为[0.8943005902334056, 0.09427735257340002, 0.011422057193194399]；卷积并限制到实际计数窗口后的荧光份额为[0.8942965916845245, 0.09428075647792206, 0.01142265183755349]。短距离成分约占1.14%的可见荧光，按当前模型对应约317814光子，属于模型分解而不是独立识别的光子标签。

快速成分与瞬时散射归一化形状的余弦相似度0.9005，总变差0.3176。用实际DA模型概率加权，再投影到IRF移位、背景、f0的局部导数空间，剩余对比范数为原来的0.217。这是有真实IRF/计数约束的条件局部几何；没有独立散射幅度约束，不能据此声称不可分辨或已识别状态。

## Rules与证据复核

前一轮真实17项基线与当前同一Q09R01实例均保留。此次触发来自已复算IRF边缘非零均值但背景中位数为0，以及当前快速分量的时间尺度提示；后者两bin尺度仅为需要补查的路由启发，绝非分辨率判据。规则off实际0派发；on实际1个新增calibration Operator、12个优化调用；完整参数、初值、失败和数值输出均保存。

轮廓证据现在检查必要字段、形状、物理范围、固定坐标、原初值、目标值及约束后的梯度。缺失、数值stop、拒收分别记录，保持已验证joint证据；还验证joint初值和在已验证候选中的最低目标选择。旧11次拟合零优化重评全部通过，未重跑。replay需要明确数值复核成功，NOT_APPLICABLE无法冒充RECOMPUTED。

校准Evidence绑定原始输入、完整base evidence、方法与种子。复核从源IRF重建每个实现与分组响应，检查对应的参数范围、目标、梯度、分段残差和几何。局部校准状态与全局蛋白态数分开；无证据或无效证据仍产生可执行补查，数值stop保留为部分结果。

## 文件与重跑

- `evidence.json`：原始实际12次结果，执行时几何只含潜在积分份额。
- `evidence_geometry_v2.json`：正式重评输入；补充实际窗口卷积份额，拟合和校准实现未变。
- `geometry_derivative_receipt.json`：该零优化补充的差异说明。
- `rule_before.json` / `rule_off.json` / `reassessment_final.json`：同一实例的路由和最终重评。
- `receipt.json` / `replay_receipt.json`：实际执行与零优化重评。
- `profile_reassessment.json`：旧11次拟合的加强核验，3个profile全部VERIFIED。
- src下数值模块与scripts下runner为当前代码；本目录source快照保留首次执行版本。

输入仍使用Zenodo原始archive（MD5 177132ce5bb9fefde871bafe8c92cbfd），不重新发布原始ZIP/PDF。沿用q09_method_admission_v1与q09_decay_admission_v1的来源清单及unpacked路径。NumPy版本记录用于固定种子实现重现；版本不同则明确拒收，而不是默默替换实现。

```bash
PYTHONPATH=src python scripts/replay_q09_calibration_sensitivity_v1.py \
 --input-root /path/to/q09_author \
 --base-evidence-dir research/paper_result_reproduction_screen_v1/q09_forward_adequacy_v1 \
 --evidence research/paper_result_reproduction_screen_v1/q09_calibration_sensitivity_v1/evidence_geometry_v2.json \
 --output-dir /path/to/new_replay
```

验证预算：1预检、针对性测试及实际失败修复、1旧证据零优化重评、1新增科学runner最多12优化、1最终回归/产物核对、1CI和1开放Pro审阅。新增卷积窗口份额的解释风险用1次零优化derivative与replay解决，不重跑拟合。没有下载、安装、额外优化、合并或新增框架；合成期望曲线仅测试验证器，不计实验成功。
