# Q16 历史拟合与导出路径核对

历史源码确认了与本地直接回算不同的计算路径；实际 Peter 数据使用哪条路径仍未知。8份小源码共不足30KB已按Git blob身份核对，未安装或执行旧软件，原1.15%–3.75%方法差距保持。

| 步骤 | 固定源码 | 观察与意义 |
|---|---|---|
| 逆解 | [get_Tikhonov_new.m#L20-L31](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/get_Tikhonov_new.m#L20-L31) | 使用离散K和正则化非负解；按时间步三次方根缩放距离轴。不能只由工作簿相邻列推断同一估计量。 |
| 模拟分支 | [fit_Tikhonov_new.m#L42-L50](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/fit_Tikhonov_new.m#L42-L50) | 带宽校正开或时间点超过1024调用deer_sim并传入bandwidth；否则get_td_fit。实际配置未取得。 |
| 小调制路径 | [get_td_fit.m#L8-L29](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/get_td_fit.m#L8-L29) | 先按时间步伸缩距离，再PCHIP到标准网格，离散和归一化到0.01；指数模拟后时间插值。 |
| 距离网格 | [get_std_distr.m#L13-L25](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/get_std_distr.m#L13-L25) | 限制原/目标距离范围，round确定网格端点，PCHIP外延0。重采样可改变形状。 |
| 指数模拟 | [pcf2deer.m#L26-L28](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/pcf2deer.m#L26-L28) | exp(pcf*kernel)，非直接线性K*P。单独指数非线性不能自动解释实际差距，见下文。 |
| 另一分支 | [deer_sim.m#L16-L48](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/deer_sim.m#L16-L48) | 52.04MHz/nm立方、1000方向点；忽略低于最大分布1e-3的点，传入exci时使用高斯带宽权重；输出0.99+0.01归一化信号。 |
| 信号导出 | [save_result.m#L108-L120](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/save_result.m#L108-L120) | 从A_sim取模拟，按相对1的调制幅度缩放；时间、实验、模拟为独立三列。 |
| 分布导出 | [save_result.m#L128-L151](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/save_result.m#L128-L151) | A_distr按(n_spins-1)/sum(distr)归一化，随后low/high列按同尺度写出；不是这里直接把mean_distr写为中心。 |
| 运行配置 | [save_result.m#L208-L250](https://github.com/gjeschke/DeerAnalysis2018/blob/d9aaaa17d8ddf26edb6b3abbfb4003f01859ccfe/save_result.m#L208-L250) | _res.txt记录源文件、方法、时间零点、截断、相位、背景、调制深度及所选带宽；需要实际配对文件。 |

源码不是实验原版本身份证明。当前检查的两个已取得存档目录（Figure5 651项、Figure4 253项）没有匹配 _res.txt / _fit.dat / _distr.dat；它们此前已识别为荧光存档，不能由此声称所有公开来源都没有DEER配置。已取得的工作簿提供数组但不补足软件分支、标准核网格和运行参数。

## 哪些差别已经可以排除为单独解释

已有回算允许自由仿射幅度与偏置，所以分布的全局乘法归一化和导出时的全局线性缩放本身不会导致该仿射回算残差。它们仍需在原执行复现中记录，但不能拿来直接解释1%以上差距。

对纯指数步骤也可给出一个明确条件界限：若使用相同的正归一化分布与cosine-minus-one核，仅比较epsilon=0.01的指数和线性变换，核平均范围长度不超过2。令b<=0.02、g(s)=(exp(bs)-1)/(exp(b)-1)，s在[0,1]。割线插值误差不超过max|g''|/8，取b=0.02给出相对指数曲线范围0.0025250833（0.253%）。最佳仿射拟合不劣于这条割线，因此在这些假设下，单纯这个指数步骤不足以解释现有最小1.15%相对RMS。此界限不涵盖不同网格、截断、带宽、核表或估计量配错；也没有证明历史Pake内核实际身份。

结论保持：路径差异有来源，真实根因 DATA_INSUFFICIENT。下一项能推进作者执行复现的证据是匹配运行配置与原导出身份；不逐个试设置到最像论文。独立声明的真实raw条件可行性分析可以继续，其科学限制由自身模型适用性决定。本批无科学拟合、无Rules补算、无题级完成计数增加。
