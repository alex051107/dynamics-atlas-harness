"""First descriptive calculation on source-published measured bars, not Rules extra."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

TASK = Path(__file__).resolve().parents[1]

def main():
    source = json.loads((TASK/'outputs/q15_tmr_histogram_intake_v1/source_geometry.local.json').read_text())
    assert source['role'] == 'PUBLISHED_MEASURED_HISTOGRAM_BARS_NOT_FITTED_CURVES'
    out = TASK/'outputs/q15_tmr_histogram_direction_v1'
    out.mkdir(exist_ok=False)
    rows = {}
    fig, axes = plt.subplots(2, 1, figsize=(7,5), sharex=True)
    for ax, condition in zip(axes, ['apo', 'holo']):
        bars = source['bins'][condition]
        left, right = source['frames'][condition][:2]
        width = right-left
        assert width > 0
        edges = [((v['left_pt']-left)/width, (v['right_pt']-left)/width) for v in bars]
        mass = [v['height_pt']*(v['right_pt']-v['left_pt']) for v in bars]
        total = sum(mass)
        mass = [m/total for m in mass]
        centers = [(a+b)/2 for a,b in edges]
        mean = sum(x*m for x,m in zip(centers,mass))
        low = sum(a*m for (a,b),m in zip(edges,mass))
        high = sum(b*m for (a,b),m in zip(edges,mass))
        cumulative = 0
        for index,m in enumerate(mass):
            cumulative += m
            if cumulative >= .5:
                median = centers[index]
                break
        mode = centers[max(range(len(mass)), key=mass.__getitem__)]
        rows[condition] = dict(bars=len(bars), centroid=mean, weighted_median=median,
            modal_bin_center=mode, within_bar_centroid_bounds=[low, high],
            maximum_bin_width=max(b-a for a,b in edges), probability_mass_sum=sum(mass))
        ax.bar([a for a,b in edges], mass, width=[b-a for a,b in edges], align='edge',
            color='0.65' if condition=='apo' else '#7bb67b', edgecolor='0.3', linewidth=.4)
        ax.set(ylabel='Normalized bar area', title=condition)
    delta = rows['holo']['centroid']-rows['apo']['centroid']
    conservative = rows['holo']['within_bar_centroid_bounds'][0]-rows['apo']['within_bar_centroid_bounds'][1]
    conservative -= rows['holo']['maximum_bin_width']+rows['apo']['maximum_bin_width']
    report = dict(status='ROBUST_RIGHTWARD_PUBLISHED_HISTOGRAM_SHIFT' if conservative>0 else 'GEOMETRIC_DIRECTION_UNRESOLVED',
        conditions=rows, centroid_shift_frame_units=delta,
        lower_shift_after_within_bin_and_one_bin_registration_per_panel=conservative,
        comparison='Opposite direction to original APBS175/228 mean shift; compatible with shorter-distance DEER under stable readout within each dye.',
        role='MANUAL_FIRST_PROCESSED_OBSERVATION_CALCULATION', rules_extra_credit=0,
        exact_E_calibration=False, scientific_full_question_answer=False,
        uncertainty='Bin-location and coarse frame-registration bound, not a statistical confidence interval.',
        limits=['One published representative histogram per condition; repetition-resolved TMR data unavailable.',
                'Processed histogram cannot verify original event selection or calibration.',
                'Different dye absolute efficiencies not compared; no E-to-distance conversion.',
                'No unique photophysical mechanism, binding equilibrium or population inference.'],
        source='Peter2022 originalPDF physical7 Figure4d right: gray measured bars only')
    axes[-1].set(xlabel='Horizontal position relative to published plot frame (not calibrated E)', xlim=(0,1))
    fig.suptitle('HiSiaP175/228 TMR/Cy5: extracted measured histogram bars')
    fig.tight_layout()
    fig.savefig(out/'measured_histograms.png',dpi=150)
    plt.close(fig)
    (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    (out/'REPORT_ZH.md').write_text('# Q15 双标记染料对照\n\n'
        f'TMR/Cy5 公开事件直方图在加配体后向右移动：按图框宽度归一化的柱形重心变化为 {delta:.6f}。'
        f'把每根柱内位置及每个面板一整根柱宽的配准偏差纳入后，下界仍为 {conservative:.6f}。\n\n'
        '与原始 APBS 数据中 Alexa175/228 的下降方向相反；在各自染料读出稳定的条件下，TMR方向与DEER缩短相容。'
        '计算输入是原PDF图4d的68个灰色观测柱形，没有使用印出的拟合均值、平滑拟合曲线或图4e距离。\n\n'
        '这是代表性处理后直方图的描述性比较，几何界限不是统计置信区间。没有逐重复TMR数据，不能核验原事件选择、给出精确E或绝对距离，也不能唯一归因为某一种光物理机制。本轮是首个手工主计算，Rules补算计数为0。\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
