from pathlib import Path
import json,csv,shutil
p=Path('autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904');o=p/'outputs/q01_absolute_paths_v1';r=json.loads((o/'numerical_report.json').read_text());receipt=json.loads((o/'receipt.json').read_text());rows=r['rows'];cand=[x for x in rows if x['seed_group']=='closed' and x['methods']['deposited_uniform']['unchanged_relative_path']['category']=='SUSTAINED_OPPOSITE_REFERENCE_PREFERENCE']
with(o/'trajectory_answer_table.csv').open('w',newline='')as f:
 wr=csv.writer(f,lineterminator='\n');wr.writerow(['trajectory','seed','relative_label_20samples','terminal_initial_lid_displacement_A','delta_open_NMR_A','delta_closed_NMR_A','terminal_nearest_open_MD_A','uniform_primary_events','uniform_internal_disagreement_frames_in_events','SI_primary_events','SI_internal_disagreement_frames_in_events'])
 for x in rows:
  m=x['absolute_metrics'];m0=x['methods']['deposited_uniform'];m1=x['methods']['SI_per_contact'];wr.writerow([x['trajectory'],x['seed_group'],m0['unchanged_relative_path']['category'],m['lid_displacement_from_20ns_A']['first20_to_last20']['after_median'],m['open_reference_lid_rmsd_A']['first20_to_last20']['delta'],m['closed_reference_lid_rmsd_A']['first20_to_last20']['delta'],m['nearest_open_MD_lid_rmsd_A']['first20_to_last20']['after_median'],len(m0['events_by_persistence']['20']),sum(e['event_contact_internal_disagreement_frames']for e in m0['events_by_persistence']['20']),len(m1['events_by_persistence']['20']),sum(e['event_contact_internal_disagreement_frames']for e in m1['events_by_persistence']['20'])])
table='\n'.join('|'+x['trajectory'].split('_')[1]+'|'+ '|'.join(f"{x['absolute_metrics'][k]['first20_to_last20'][s]:.2f}"for k,s in [('open_reference_lid_rmsd_A','delta'),('closed_reference_lid_rmsd_A','delta'),('lid_displacement_from_20ns_A','after_median'),('nearest_open_MD_lid_rmsd_A','after_median')])+'|' for x in cand)
text='''# Q01 科学答复：闭合种子在有限时间内发生更大的结构移动，并出现开放方向重排

**在这批apo HSP90α NTD的20条开放种子和20条闭合种子轨迹中，闭合种子组在20–1020 ns窗口内发生更大的lid结构位移；其中9条出现持续的相对开放偏好，并伴随绝对几何上的开放方向重排。不同路径的局部接触重排程度不同，不能把9条都解释为完整进入同一个开放构象。** 这些结果支持论文所讨论的有限时间稳定性不对称和闭合构象亚稳性解释；不估计平衡占比、速率或功能活性。

这是按原题“保持、偏离、向另一构象移动以及偏离两参照”形成的题级答复草案，待下一轮科学审查。完整科学验收数尚未增加；当前已不是只有相对评分或接口报告。

## 两组真正移动了多少

对全40条使用同一core对齐与N/CA/C/O backbone定义，相对每条20 ns分析起点计算lid位移。终段取最后20个已保存采样点（1001–1020 ns），避免只依赖单帧。

| 轨迹组 | 终段lid位移中位数 | 轨迹间四分位范围 |
|---|---:|---:|
| 开放种子20条 | 3.77 Å | 3.51–4.98 Å |
| 闭合种子20条 | 9.71 Å | 5.66–14.64 Å |

闭合减开放的中位数差为5.94 Å。以整条轨迹为单位、固定随机种子的2000次重采样，条件性95%百分位范围为2.07–10.51 Å。该范围描述本批种子集合重采样的变化，假定轨迹可在组内交换；不覆盖共享模型、力场或生物实验的不确定性。40,040帧没有作为独立重复。20条开放种子未观察到某事件，也不表示总体事件概率为0。

开放组20条保持预定的持续开放偏好，但仍有数Å运动，因此“保持偏好”没有被写成“结构不动”。闭合组10条未持续丢失闭合偏好，也包含明显运动，例如ES01终段位移9.66 Å；它们不能全部叫作稳定闭合。ES06持续失去原偏好但没有相反参照一致支持，保留冲突。

## 9条候选的绝对方向

下面统一比较前20点（20–39 ns）与后20点，而非用作者人数作目标。开放参照距离下降、闭合参照距离上升，在9条上同时出现。

| 轨迹 | 开放NMR距离变化 Å | 闭合NMR距离变化 Å | 终段相对起点位移 Å | 终段最近开放MD距离 Å |
|---|---:|---:|---:|---:|
'''+table+'''

完整事件、返回、末端偏好和连续段见numerical_report.json及80,080行full_absolute_paths.tsv（每帧两种阈值）。相同路径在5/20/50点下分别有10/9/8条闭合种子出现持续相反偏好，两阈值的轨迹类别均相同。20点仅说明连续已保存样本跨19 ns，不证明采样间隔内未发生返回。

ES07、ES09、ES10在首尾窗口中到两个NMR参照的距离都增加，这种“同时远离两者”的方向保留在结果中。这里也没有将它们自动判为第三态或完全脱离两类构象；ES10的位移很小，需结合绝对尺度。所有40条都完成相同核查。

## 开放MD参照提供了怎样的结构尺度

从20条开放种子轨迹各固定选20、120、…、1020 ns共11帧，得到220个开发期MD参照。开放组自查时排除整条查询轨迹，共209个其他轨迹参照；闭合轨迹比较全部220帧。保持相同core对齐，计算最近lid结构距离，没有逐帧训练/验证拆分或重新聚类。

开放组留整轨迹后的最近结构距离，中位数2.40 Å、95%分位3.60 Å。9条候选的终段距离为2.01–7.29 Å：ES03、04、15、20的终段中位数位于该95%几何尺度内；ES14、16、19略大，ES05、17仍与已抽样开放MD结构有更明显差异。**3.60 Å只是开发期几何参照尺度，不是新设的开放状态边界。** 各轨迹参与了本地参照构建，这不是外部独立验证；开放查询与闭合查询使用的参照数量也不同。连续值和完整分布均保留。

原NMR构造包络40/40起点不覆盖的失败仍保留，没有扩包络使候选通过。完全返回NMR包络、全部局部结构重折叠不是原论文有限时方向问题的新增门槛。

## 接触通道揭示不完整的局部重排

两种阈值各自保留开放特异/闭合特异接触原始超限量及归一化方向；原平均投影和9条标签不改。ES17第一事件605–646 ns的42点，uniform中41点、SI中42点存在内部方向分歧；开放接触的正方向可以盖过闭合接触的负方向，使平均值仍为正。ES05、ES19的部分事件也存在内部补偿。几何与平均接触同号，不能解释为所有结构指标同时支持完整开放态。

同一Rules实例这次实际要求绝对路径和接触分解，关闭规则时执行0次、开启时1次。证据返回后，每条轨迹的解释受实际通道分歧限制，原相对标签保留。它加强了具体解释约束，没有证明跨20题的准确率提升，也没有宣称Rules自主发明了方法。

## 可复查范围

- 40条连续距离/时间轴/轨迹与原子角色现已绑定；从保存的GROMACS坐标文本、盒矩阵及原始NMR CIF重新构建，全部测量差为0。旧历史记录未改；新验收不能倒推历史文件从未改变。
- 原相对结果零提取重放后保持相同。冻结政策被篡改为37点或改归一化参数会拒绝；部分起点未覆盖会明确列出未处理对象。
- 本次绝对路径实际用时约'''+f"{receipt['elapsed_seconds']:.1f}"+'''秒，0新GROMACS、0优化、0新MD、0依赖安装。MD参照和轨迹bootstrap均是开发期比较。
- 论文及来源：Henot et al., 2022, https://doi.org/10.1038/s41467-022-35399-8；源方法、SI2脚注、NMR参照和40条映射见../q01_path_comparison_v1/source_method_review.md。未以作者轨迹标签、人口数或最终拟合值作为判据输入。

![全40条绝对路径与接触分解](absolute_paths_summary.png)
'''
(o/'REPORT_ZH.md').write_text(text)
(p/'scripts/q01_absolute_report_v1.py').write_text(Path('/tmp/q01_report42.py').read_text())
print('report_written',len(rows),'trajectories',len(cand),'directional_candidates')
