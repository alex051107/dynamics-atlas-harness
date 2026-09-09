## 结论摘要

材料支持一个有限而明确的结论：在 T4 溶菌酶（T4L）这一特定体系、特定集成流程和特定 CV/MSM 分析下，AMS 比“只使用生成模型输出的 ensemble”覆盖了更广的构象空间，并且在无显式 metadynamics 偏置的后续 MD 中恢复了四态模型中的闭合态；其主要状态分数与作者采用的 EMD 参考结果大体接近，也能在 smFRET 分布中恢复实验对应的开、闭两类宏观状态。

但材料不支持若干更强的说法：不能据此证明 AMS 普遍优于所有单独生成模型、普遍优于 EMD、得到真实或更准确的平衡分布、在计算效率上已经优于 EMD，或可无条件迁移到其他蛋白体系。尤其是 EMD 的原始轨迹不可用，作者明确说无法进行 AMS–EMD 的精确 population-weighted 直接比较。

## 一、相对于单独生成模型，已有证据支持的结果

### 1. 单独 GenAI ensemble 主要集中在 exposed/open

**作者报告：**除 AF-cluster 外，多数 GenAI 方法主要重现 exposed/open，不能独立采样 T4L 的瞬态闭合态及其相对占比；图 2 说明合并 GenAI ensembles 主要集中于单一状态（论文 md 第 152–156、235–240 行）。

**依据材料作出的判断：**这只支持“在本文测试的模型、样本量和状态定义下，单独生成模型对闭合态覆盖不足”，不支持“生成模型原则上不能生成闭合态”。AF-cluster 是明确例外，作者报告其构象覆盖明显更宽（第 182–183 行）。

### 2. AMS 在本例中覆盖四态，而单独 GenAI ensemble 没有同等覆盖

四态由 Ser44–Ile150 距离 d1（closed/open）和 Phe4 locking coordinate p（buried/exposed）定义。作者报告 AMS 采样到了 exposed/open、exposed/closed、buried/open 和 buried/closed；同时称单独 GenAI ensemble 不能采样 buried/open（第 120–129、184–192 行）。

**我的判断：**这支持“生成模型种子加物理 MD 加 MSM 的整体流程，获得了比生成模型输出本身更完整的四态覆盖”，不能说明 AMS 的每一个组成部分都独立贡献了同样效果。

### 3. AMS 的闭合态发现高度依赖 AF-cluster

作者报告 AF-cluster 覆盖最宽；排除 AF-cluster 后，AMS 未能采样 closed state，但仍比从单一晶体结构开始的 unbiased MD 覆盖更宽（第 193–201、253–278 行）。

**我的判断：**不能简单说“组合多个生成模型就足够”。本文结果显示 AMS 对种子组成敏感，至少闭合态恢复依赖 AF-cluster；更准确的结论是，含有合适的多样化种子时，后续物理模拟可以弥补生成模型 ensemble 的不足。

### 4. 相同名义轨迹时长下，AMS 比单一晶体结构起始的 unbiased MD 覆盖更广

作者比较了 AMS Round 1 的 100×200 ns（20 μs）与从 PDB 5LZM 起始的 20 条 1 μs unbiased MD，并报告后者未采样 closed state，而 AMS 覆盖了更广异质性（第 214–217、219–230 行）。

**我的判断：**这支持多起点、多样化种子在本例中的探索优势，但不是严格的计算效率证明，也不是对每个单独生成模型的公平比较。

## 二、相对于 EMD，已有证据支持的结果

### 1. AMS 与 EMD 都覆盖四态，主要人口大体接近

作者报告的状态人口为：exposed/open，AMS 38.3%、EMD 39.1%；buried/open，58.7%、54.0%；buried/closed，2.3%、2.9%；exposed/closed，0.7%、3.9%（正文第 120–129 行）。

**作者报告：**前三个状态相对人口可比，exposed/closed 在 AMS 中低估，是最难访问的瞬态状态。

**我的判断：**只能说主要状态及一个稀有状态大体接近。四态差异并不均匀，尤其 exposed/closed 的相对误差很大；不宜无条件概括为“AMS reproduces EMD equilibrium populations”。

### 2. AMS 恢复了实验 smFRET 的开、闭宏观状态

Supporting Information Figure S1 报告 AMS 的 MSM-weighted FRET 分布同时显示 open 和 closed，并捕获实验中的稀有 closed-state 概率；正文也作了同样报告（论文第 188–201 行；SI Figure S1）。

**我的判断：**这支持宏观开/闭状态层面的实验一致性，不等于整个 FRET 分布都被精确重现。作者明确承认过渡构象区域与实验有偏离（第 287–318 行）。

### 3. 本文的 AMS MSM 比 EMD MSM 更连通

SI Figure S8 报告 AMS Round 1 的 connected state fraction 和 count fraction 均为 1.00，而 EMD 存在与主网络断开的状态块；正文也报告 EMD MSM 有 disconnected transition matrix（第 158–162、265–278 行）。

**我的判断：**这证明本文两套 MSM 的网络连通性不同，但不自动证明 AMS 的动力学更正确；MSM 连通性受起点、轨迹长度、特征、聚类和 lag time 影响。

### 4. AMS 对若干分析选择表现出稳定性

SI Figures S2–S4、S6 报告不同 lag time、cluster 数以及 RMSD/TICA 特征下，AMS 的自由能面和人口总体稳定，并给出 Bayesian 95% 区间；作者据此称其收敛较稳健（正文第 158–163 行）。

**我的判断：**这支持在所测试的分析设置范围内结果不是完全由单一参数选择造成的，但不能替代独立重复、更多采样或不同力场/水模型验证。

## 三、尚未支持的更强结论

1. **AMS 普遍优于单独生成模型：未证明。**本文只测试一个体系、一组模型和一个 CV/MSM 流程；AF-cluster 是例外且对成功很关键。没有证明 AMS 对每个单独模型加相同 MD 都更好，也没有跨模型版本、随机种子或体系验证。

2. **AMS 普遍优于 EMD：未证明。**本文 EMD 是由 unbiased MD、metadynamics 和后续 seeded MD 组成的特定参考流程，不是一个唯一标准；EMD 原始数据不完整，作者明确说无法进行完全一致的精确 population-weighted 比较（第 308–319 行）。

3. **AMS 给出真实平衡人口：未证明。**人口依赖 MSM；smFRET 主要验证开/闭宏观分布，不能独立验证全部四态。作者也承认过渡区域与实验有偏离，并指出力场、水模型、特征和 CV 的影响。

4. **AMS 整个流程完全无目标导向：表述过强。**MD 阶段没有 metadynamics bias，但 CV、SFA、K-center、种子数量、MSM 特征和 lag time 都包含研究者选择；“无 MD 偏置”不等于“整个流程无选择性”。

5. **AMS 计算效率优于 EMD：未证明。**论文报告 Round 1 在三张 A100 上约 10 天，但没有以相同硬件、总 GPU-hours、准备/分析成本和同等置信度与 EMD 作严格比较。

6. **可普遍迁移至其他蛋白：仍是前景。**论文提出可用于更广泛蛋白，但本文只验证 T4L，尚无跨体系证据。

## 四、未解决部分与最有信息价值的下一步

1. 公开 AMS 和 EMD 全部原始轨迹，在相同特征、聚类、lag time、MSM 和误差模型下重算人口、转移概率和 FRET。
2. 对 AF-cluster、其他 GenAI 方法和随机种子进行多次消融/重复，报告闭合态发现概率。
3. 以 GPU-hours/CPU-hours、准备成本和达到给定置信区间所需轨迹长度比较计算成本。
4. 加入 NMR、突变体平衡数据或多对 smFRET 距离，检验 buried/exposed 状态和四态人口。