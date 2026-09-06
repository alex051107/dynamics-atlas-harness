"""Read raw support/noise proxies before choosing a conditional likelihood."""
import json
from pathlib import Path
import numpy as np

TASK = Path(__file__).resolve().parents[1]

def statistics(values):
    x, y = values[:, 1], values[:, 3]
    differences = np.diff(y)
    return dict(n=len(y), imaginary_mean=float(np.mean(y)), imaginary_std=float(np.std(y,ddof=1)),
        imaginary_difference_MAD_scale=float(np.median(np.abs(differences-np.median(differences)))/(.6744897501960817*np.sqrt(2))),
        imaginary_lag1=float(np.corrcoef(y[:-1],y[1:])[0,1]),
        real_imaginary_correlation=float(np.corrcoef(x,y)[0,1]))

def main():
    source = json.loads((TASK/'outputs/q16_observation_independence_v2/source_curves.local.json').read_text())
    out = TASK/'outputs/q16_raw_applicability_v1'
    out.mkdir(exist_ok=False)
    rows = []
    for pair in ['29','36']:
        for condition in ['eg50_1mM','eg0_1mM']:
            key = f'SI Figure10:{pair}_{condition}'
            raw = np.asarray(source[key]['raw'],float)
            processed = np.asarray(source[key]['processed'],float)
            assert raw.shape[1]==4 and processed.shape[1]==2
            assert np.isfinite(raw).all() and np.all(np.diff(raw[:,0])>0)
            positive = raw[raw[:,0]>=0]
            midpoint = len(positive)//2
            b = positive[:,2]
            rows.append(dict(key=key, raw_all_n=len(raw), raw_nonnegative_n=len(positive),
                raw_time_range_us=[float(raw[0,0]),float(raw[-1,0])],
                processed_time_range_us=[float(processed[0,0]),float(processed[-1,0])],
                raw_points_beyond_processed_end=int(sum(positive[:,0]>processed[-1,0]+1e-9)),
                proxies={'full':statistics(positive),'first_half':statistics(positive[:midpoint]),'second_half':statistics(positive[midpoint:])},
                deposited_background_audit_only=dict(start=float(b[0]),end=float(b[-1]),
                    increasing_steps=int(sum(np.diff(b)>0)),decreasing_steps=int(sum(np.diff(b)<0)),
                    positive=bool(np.all(b>0))),
                inference='Imaginary channel is a proxy; phase/orientation/coherence and temporal correlation require interpretation.'))
    report = dict(status='RAW_SUPPORT_AND_NOISE_PROXIES_ONLY',rows=rows,
        main_author_fit_or_distribution_used=False, accepted_likelihood=False,
        optimizations=0,rules_extra_credit=0,scientific_full_answer=False,
        implications=['Both no-EG raw records extend to4.896us, beyond their3.488/3.008us processed windows.',
                      'Cropping long raw records to the actual short acquisition support is different from cropping to the author analysis window.',
                      'Background arrays are audited as source processing, not treated as independent calibration.',
                      'No confidence limits derived from imaginary-channel proxy statistics.'])
    (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    (out/'REPORT_ZH.md').write_text('# Q16 原始记录与噪声代理\n\n'
        '两个无保护剂原始记录均延伸至4.896微秒；作者处理后只到3.488和3.008微秒。截短原始记录与复用作者处理窗口是不同问题。\n\n'
        '报告按原始复数观测的虚部分别计算全段/前半/后半尺度、自相关与实虚相关，仅用于选择后续条件噪声模型，未当成已核准似然或统计置信区间。存档背景单独审计，不作为短窗重新分析的独立校准。\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
