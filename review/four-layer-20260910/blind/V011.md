## 结论及条件

在本数据包定义的可复核观测下，**闭合起始轨迹比开放起始轨迹更容易离开原有构象，并出现指向开放的变化**；但这不是“所有闭合轨迹都完成了闭合→开放转变”，也不能仅凭字段名 `departure`/`return` 作此解释。

比较条件是：20 条 `closed_seeded` 对 20 条 `open_seeded`，每条轨迹的交付分析窗口为 **20–1020 ns（1001 个逐帧点，1 ns 间隔；按轨迹为统计单位）**。原论文的模拟描述为 40 条、各 1 μs；交付表明确采用上述 20–1020 ns 窗口。`trajectory_time_anatomy.tsv` 的 5/20/50 saved-frame persistence 是同一轨迹的三种阈值摘要，不是 120 条独立轨迹。

最稳妥的结论分层如下：

1. **起始依赖的方向变化：支持闭合起始更易偏离。** 逐帧方向判据是 `geometry_delta_A > 0` 且 `contact_margin_A > 0` 才标为 `OPEN_CONSENSUS`；两者均 <0 才是 `CLOSED_CONSENSUS`；否则是 `READOUT_CONFLICT`，零也归冲突。按此判据，闭合起始组有 6764/20020（33.8%）开放共识帧、8341/20020（41.7%）闭合共识帧和 4915/20020（24.6%）冲突帧；开放起始组为 20020/20020（100%）开放共识帧。按轨迹计，闭合组 10/20 轨迹出现过开放共识帧，开放组 20/20 出现；闭合组 18/20 出现过闭合共识帧，而开放组 0/20 出现过。

2. **持续方向摘要也支持该不对称性，但不等同于状态跃迁。** 首个至少 5 个连续保存点的非冲突 run：闭合起始为 15/20 CLOSED、5/20 OPEN；开放起始为 20/20 OPEN。阈值提高到 20 点（端点相隔约 19 ns，表中历史 `persistence_ns` 沿用 saved-frame convention）时，闭合起始为 13 CLOSED、5 OPEN、2 无持久共识；开放起始为 20 OPEN。提高到 50 点（约 49 ns）时，闭合起始为 11 CLOSED、7 OPEN、2 无持久共识；开放起始为 20 OPEN。50 ns 分箱则给出闭合组 143 个 OPEN、169 个 CLOSED、108 个冲突箱，开放组 420 个 OPEN、0 个 CLOSED、0 个冲突箱；这些箱是箱内中位数分类，不能代替逐帧连续 run。

3. **“闭合→开放转变”作为严格、论文式状态转变，当前派生表并未充分证明。** `state_core` 是另一个锚定相对结构支持判据，不是动力学状态：按 JSON 中的阈值，C 需 `delta≤−15.964 Å` 且 `d_closed≤3.300 Å`，O 需 `delta≥17.022 Å` 且 `d_open≤1.790 Å`，否则 U。逐帧计数显示闭合起始仅 1/20 轨迹出现过 C、0/20 出现过 O；开放起始 0/20 出现 C、2/20 出现 O。这个结果说明 `state_core` 很严格且与方向共识不是同一个量，不能用它直接宣称转变频率。

## 与原论文定义的关系

原论文把 open/closed 作为 ATP-lid 的结构构象：open 状态类似未结合配体的已知构象；closed 状态覆盖 ATP/药物结合位点，并涉及闭合态特有的结构重排（文章约第 206–214、296–302 行）。论文对 MD 的解释是：开放起始模拟在 1 μs 内保持稳定；闭合起始模拟有稳定、趋向开放以及进入既非明确 open 也非明确 closed 区域的三类行为。论文报告闭合起始集合的平均 pairwise Cα-RMSD 约 9.3 Å，而开放起始约 4.0 Å（约第 300–330 行），并称约 9 条闭合起始轨迹趋向与开放态 NOE 兼容的构象、约 20% 进入中间/非明确区域（约第 332–350 行）。因此，本包的“方向共识”结果与论文的总体不对称叙述相容，但**方向共识的正负号判据本身不是原论文的 open/closed 结构定义，也不是 NOE 充分验证**。

## 实际分析与判据核查

- 我直接读取了 `FIELD_DEFINITIONS.md`、`state_core_definition.json`、`frame_state_assignments.tsv`、`trajectory_time_anatomy.tsv`、`trajectory_time_bins_50ns.tsv`、`directional_runs.tsv` 和论文文本抽取。
- `geometry_delta_A` 是闭合 medoid 距离减开放 medoid 距离；`contact_margin_A` 是沉积的 closed-contact violation readout 减 open-contact violation readout。二者的同号规则是交付表的操作性方向判据，而不是“离开原构象”或“发生构象跃迁”的独立实验判据。
- `first_persistent_direction` 的参考方向是“第一段持久方向”，**可能不同于 seed_lineage**。`opposite_direction_departure_candidate` 只表示之后有相反方向的持久 run，`return_candidate` 表示随后又回到最初持久方向；所以这些字段不能不加核查地解释为离开起始态、转变和返回起始态。当前摘要中，5/20/50 点阈值下闭合组的 opposite candidate 分别为 5、4、1（开放组均为 0），return 均为 0；这支持有少数较持久的相反方向片段，但不是闭合→开放的完成转变计数。
- `state_core` 的“C/O/U”与方向共识应视为互补读数：前者是严格的 anchor-relative structural support core，后者是两个派生量的符号共识。二者不一致或 U 并不自动代表论文所说的第三类中间构象。

## 仍与哪些解释相容 / 未解决部分

这些数据仍相容于：

1. 闭合起始态在微秒尺度更分散、更易进入开放参考附近；
2. 闭合起始轨迹只是在 `geometry_delta/contact_margin` 投影上偏向开放，并可能是局部 lid 重排、接触读数改变或非二态中间区，而非完整 open basin；
3. 开放起始组的全程 OPEN_CONSENSUS 反映该投影下的稳定性，但不能排除未被这些派生量捕捉的其它构象变化；
4. 论文所述“趋向开放”的 NOE 兼容性，与本包的方向共识并非同一判据，因此不能把 10/20、7/20 等数字直接报告成论文定义的转变概率。

尤其重要的是，`SOURCE_INVENTORY.json` 明确说明原始坐标数组和完整 source-native NOE restraint calculation inputs 不在派生表包内。虽然每轨迹有 native NOE violation 文件和字段判据，但没有在本次关闭阶段完成独立 NOE 复核，因此不能把方向共识当作原生 NOE 验证。

## 有信息价值的下一步

最有价值的是预先固定一个与论文结构定义对应的、逐轨迹的联合判据：在 20–1020 ns 内要求连续窗口同时满足（i）开放/闭合结构参考距离，和（ii）独立的开放/闭合特异 NOE 违例阈值；分别报告首次进入、持续时间、是否回返，并以轨迹为统计单位。随后用 bootstrap 或置换检验比较 20 条闭合起始与 20 条开放起始，且同时报告不依赖阈值的原始距离/接触分布。这样才能区分“离开闭合参考”“进入开放兼容区”和“完成论文意义的 open state transition”。