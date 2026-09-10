## 结论（以给定 DH5-DMPC 纳米盘资料为限）

当前证据支持的是**条件性的跨观测一致性**，而不是“所有观测都被同一个构象集合很好解释”：

1. **SAXS 与 BME 重加权结果基本相容，但不是无条件的精确吻合。** 逐点比较给定的 BME SAXS 预测和实验文件（90 个相同 q 点）得到 reduced χ²≈1.913，53.3% 的点落在实验给定的 1σ 误差内；平均绝对相对差约 2.83%。因此，在采用该 BME 的散射预测、误差列和重加权方案的前提下，SAXS 是可接受的支持证据，但仍有系统偏差/误差模型问题的可能。
2. **HN-NOE 与 methyl-NOE 的数值吻合明显较弱。** 对作者提供的重加权统计文件直接计算，HN-NOE（292 项）的 MAE=0.763、RMSE=1.088，只有 31.2% 的预测与实验相差不超过 0.5；methyl-NOE（40 项）的 MAE=1.994、RMSE=2.231，只有 10.0% 差值不超过 0.5。尤其 methyl-NOE 不能被描述为与实验逐项高度一致。因此，不能仅凭“联合 BME”标签断言 SAXS、HN-NOE 和 methyl-NOE 共同验证了同一套构象权重。
3. 这更适合表述为：**给定模型和重加权设置下，SAXS 层面有中等/可接受的一致性，而 NOE 层面存在未解决的观测—模型差异；跨观测整体一致性尚未充分建立。** 这并不证明构象模型必然错误，也可能反映 NOE 的回算/观测误差、实验条件差异、标度或权重正则化等问题。

## 实际核对与分析

我使用的是给定的逐点文件，而非把 reference-only 数值当作新的发表结果：

- 读取 `/source/BME_reweight/reference_only/BME_stats_SAXS.dat` 的 simulation、experiment 两列，并与 `/source/SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat` 按 q 配对；计算
  `RMSE = sqrt(mean((I_sim-I_exp)^2))`、平均绝对相对差、以及 `sum((I_sim-I_exp)/I_err)^2 / 90`。
- 结果为 RMSE=0.00133546、MAE=0.000620667、平均绝对相对差=0.0283223、reduced χ²=1.91284、1σ 覆盖率=0.5333。举例，最低几个 q 点中，q=0.00336388 Å⁻¹ 的预测/实验为 0.03459/0.04260，残差为 −0.00801，已超过该点误差 0.005016；所以“总体可接受”不能被误读为“逐点完美”。
- 对 `/source/BME_reweight/reference_only/BME_stats_HN_NOE.dat` 和 `BME_stats_methyl_NOE.dat` 的 simulation、experiment 两列分别计算 MAE、RMSE 和 |残差|≤0.5 的比例，得到上列 NOE 数值。

这些比较直接影响结论：如果只看 SAXS，会得到较乐观的支持；加入逐项 NOE 核对后，结论必须降级为“部分一致、尚有冲突/不确定性”。

## 方法与模型检查的适用边界

给定论文说明其整合框架是 MD 加 NMR、SAXS/SANS 的 Bayesian/maximum-entropy（BME）整合；论文摘要称所得集合与各方法一致，但本次对随数据提供的逐项数值进行了独立复核（`/source/method_sources/Bengtsen_2020.txt`，第23–31、83–90行；`/source/BME_reweight/inputs_and_method/README.md`，第6–25行）。

对方法卡 [rule id redacted] 所要求的检查，资料足以确认有 simulation-derived observables、BME 权重和超参数扫描；但不能完整重建一个独立的 shared-weights forward-model 审计：未在本次分析中重新优化权重，也没有足够资料把每个观测的 likelihood、系统误差项、MD 先验扰动和熵惩罚逐项拆开。权重文件本身的权重和约为 1，按给定权重计算的有效样本数约 84.6（这是本次由权重计算的诊断），说明权重并非只集中在一个帧；但这不等于证明权重是热力学态人口，也不等于证明状态发现或动力学。

此外，`hyperparameter_theta.dat` 显示 θ=2 时列出的 χ²最低（2.970803），而 θ 增大到 40 时相对熵降至 0.029822、χ²升至 7.765671；这说明拟合—扰动之间存在明显正则化选择，而不能把一个权重集合当作先验无关的唯一答案。文件把统计值列作给定 BME 结果；上述差值、χ²、覆盖率和有效样本数是本次计算。

## 未解决部分

- NOE 文件的实验不确定度/允许偏差、回算算子（例如是否为非线性平均）及单位/标度没有在给定 README 中充分展开；因此不能把 MAE=1.994 直接转换成严格的统计拒绝概率。
- SAXS 的 1σ 误差可能没有覆盖全部相关系统误差，且实验文件是 30°C、无 tag 的静态 SAXS；不能自动把它与所有论文中 10°C、His-tag 或 SEC-SAXS/SANS 条件混为同一实验。论文明确区分了这些条件（`paper.txt` 第168–180行）。
- 没有执行独立的 Bayesian forward-model、先验敏感性分析或 shared-weight 的重新拟合，所以不能判断差异究竟来自构象缺失、实验条件、观测算子还是误差模型。

## 信息价值最高的下一步

在保持相同实验条件和原始误差模型的前提下，分别进行：(i) SAXS-only、HN-NOE-only、methyl-NOE-only 及三者联合的 BME/MaxEnt 重加权；(ii) 对 θ、NOE 回算算子和 SAXS nuisance/systematic-error 模型做预先规定的敏感性分析；(iii) 报告各数据集的 posterior predictive residual、权重边界行为和先验扰动。若不同数据集需要互不相容的权重，才可更有力地区分“构象集合不足”与“观测/误差模型不适配”。

证据位置：`/source/BME_reweight/reference_only/BME_stats_SAXS.dat`、`BME_stats_HN_NOE.dat`、`BME_stats_methyl_NOE.dat`、`BME_simulation_weights.dat`、`/source/BME_reweight/inputs_and_method/hyperparameter_theta.dat`、`/source/SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat`、`/source/BME_reweight/inputs_and_method/README.md`、`/source/method_sources/Bengtsen_2020.txt` 与 `/source/paper.txt`。