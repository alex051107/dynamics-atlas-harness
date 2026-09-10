## 结论

当前最稳妥的判断是：**纳米盘的椭圆形、含脂质构象 ensemble 与 SAXS 和 NOE 总体相容，但不是无条件一致，也不能据此确定唯一静态构象。** SAXS 主要约束含蛋白和脂质的全局尺寸/形状及距离分布；NOE 约束蛋白 belt 上的局部原子距离，二者是互补观测（/source/paper.txt:376–384）。

- 模拟前三个聚类约占 95%，均呈椭圆形、但长轴方向不同（/source/paper.txt:250–253）。这与 SAXS/SANS 对椭圆形的提示相容，但不代表只有一个椭圆构象。
- SAXS 方面，论文报告模拟能再现约 0.07 Å⁻¹ 极小值深度，但不能准确再现 0.15–0.20 Å⁻¹ 的肩部（/source/paper.txt:298–303），因此全局形状描述大体正确，仍有模型或 ensemble 残差。
- NOE 方面，论文报告甲基和酰胺 NOE 总体吻合，但有少数距离超过实验上限；酰胺 NOE 的良好表现主要说明局部螺旋/二级结构得到保持（/source/paper.txt:312–318）。
- 原 NMR/EPR 结构呈圆形而 SAXS/SANS 更提示椭圆形，但原结构缺少脂质，不能直接作公平 SAXS 比较；补加 DMPC 后也只能再现部分特征（/source/paper.txt:304–310）。

## 实际数据核对

我读取给定的重加权统计文件和实验文件，进行了两项直接比较。

### 1. SAXS 逐 q 误差标准化比较

使用 `/source/BME_reweight/reference_only/BME_stats_SAXS.dat` 与 `/source/SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat`，按相同 q 配对 90 个点，计算

\[
\chi^2_{mean}=N^{-1}\sum_q[(I_{sim}-I_{exp})/\sigma_q]^2.
\]

结果：q 范围 0.00281393–0.24080569 Å⁻¹，配对最大 q 差为 0；总标准化平方残差 172.37，平均 χ² **1.915**。q≤0.10 Å⁻¹ 的平均 χ²为 **1.52**，q≤0.15 Å⁻¹为 **1.55**，q≤0.20 Å⁻¹为 **1.99**。这支持“重加权 ensemble 与 SAXS 在总体误差尺度上相容”，但不支持“逐点完美吻合”。该新计算标识为 `calc_reweighted_saxs_chi2_v1`。

### 2. NOE 上限逐项检查

用 `/source/BME_reweight/reference_only/BME_stats_HN_NOE.dat`、`BME_stats_methyl_NOE.dat` 中的重加权距离，与实验文件中的 upper bound 比较：

- HN NOE：292 项中 47 项超过上限，约 **16.1%**；最大超出 4.91 Å。
- 甲基 NOE：40 项中 8 项超过上限，约 **20.0%**；最大超出 2.75 Å。

因此，“NOE 总体相容”必须明确限定为**大多数约束相容、但仍有少量局部违背**，不能说所有 NOE 都被满足。该新计算标识为 `calc_reweighted_noe_upperbounds_v1`。

论文表 2 也显示互补性：未重加权 MD 的 SAXS/NOE χ²为 10.0/8.2；仅用 SAXS 或 NOE 重加权后，相应指标分别改善至 1.5 或 4.2，但另一类数据仍为 7.9 或 8.9；联合重加权为 1.9/6.0（/source/paper.txt:326–338）。这说明单一观测不能完全替代另一观测，联合约束可以同时达到合理但非完美的拟合。

## 限制与未解决部分

1. 我的 SAXS 平均 χ²和 NOE 违背比例是按给定文件重新定义/计算的统计量，不应与论文表 2 的 χ²直接等同。
2. NOE 是 ensemble 平均且为上限约束；平均距离超限不等于每一帧都错误，也可能受峰归属、交换、误差模型或模型近似影响。
3. SAXS 的形状、脂质数目、柔性、标度和多分散性可能互相补偿；论文也指出脂质数目多分散性可能影响标准溶液 SAXS 的解释（/source/paper.txt:225–231）。
4. 现有资料不能证明唯一椭圆率、唯一构象或残差必然源于真实构象异质性。

最有信息价值的下一步是保留逐帧 BME 权重，进行统一误差模型下的 posterior-predictive 检查：特别追踪 0.15–0.20 Å⁻¹ SAXS 肩部和最大 NOE 违背是否由同一构象子群产生，并用留出的 SAXS q 区间、NOE 子集或未用于拟合的 SANS/PRE/EPR 做独立验证。论文报告 PRE/EPR 总体上与精炼 ensemble 相容、且重加权通常改善 EPR（/source/paper.txt:396–401），但这部分不能仅凭当前 SAXS/NOE 文件独立复现。