"""Descriptive fluorescence observables from source-labelled worksheet curves."""
import json, math
from pathlib import Path

TASK=Path(__file__).resolve().parents[1]
BLOCKS=[('175_AF555','A','B','C','D','E'),('58_AF555','F','G','H','I','J'),
        ('175_AF647','K','L','M','N','O'),('58_AF647','P','Q','R','S','T'),
        ('175_TMR','U','V','W','X','Y'),('175_Cy5','Z','AA','AB','AC','AD')]

def main():
    cells={x['cell']:x for x in json.loads((TASK/'outputs/q15_complete_workbook_v1/Figure 4.source_cells.json').read_text())}
    out=TASK/'outputs/q15_dye_response_v1';out.mkdir(exist_ok=False)
    results={};curves={};source=[]
    for name,tcol,ar,ai,hr,hi in BLOCKS:
        results[name]={}
        source.append(dict(name=name,source_label=cells[tcol+'1']['value'],columns=[tcol,ar,ai,hr,hi],
            headers=[cells[c+'3']['value'] for c in [tcol,ar,ai,hr,hi]],
            conditions=[cells[ar+'2']['value'],cells[hr+'2']['value']]))
        for condition,rcol,icol in [('apo',ar,ai),('holo',hr,hi)]:
            rows=[]
            for row in range(4,20000):
                v=[cells.get(c+str(row))for c in [tcol,rcol,icol]]
                if all(x and x['type']=='n' for x in v):
                    values=[float(x['value'])for x in v]
                    assert all(map(math.isfinite,values))
                    rows.append(values)
            assert len(rows)==3125 and all(b[0]>a[0]for a,b in zip(rows,rows[1:]))
            peak=max(rows,key=lambda x:x[2]);assert peak[2]>0
            aligned=[[t-peak[0],aniso,intensity/peak[2]]for t,aniso,intensity in rows]
            windows={}
            for label,lo,hi in [('early',2.,4.),('late',6.,8.)]:
                chosen=[(t,r,I)for t,r,I in aligned if lo-1e-9<=t<=hi+1e-9]
                assert len(chosen)==126 and all(x[2]>=0 for x in chosen)
                intensity=sum(x[2]for x in chosen)
                windows[label]=dict(delay_ns=[lo,hi],n=len(chosen),mean_peak_normalized_intensity=intensity/len(chosen),
                    intensity_weighted_anisotropy=sum(x[1]*x[2]for x in chosen)/intensity)
            results[name][condition]=dict(source_rows=len(rows),peak_time_ns=peak[0],source_peak_intensity=peak[2],
                windows=windows,late_to_early_intensity_ratio=windows['late']['mean_peak_normalized_intensity']/windows['early']['mean_peak_normalized_intensity'])
            curves[name+'_'+condition]=aligned
        apo,holo=results[name]['apo'],results[name]['holo']
        results[name]['comparison']=dict(holo_over_apo_late_early_ratio=holo['late_to_early_intensity_ratio']/apo['late_to_early_intensity_ratio'],
            late_anisotropy_holo_minus_apo=holo['windows']['late']['intensity_weighted_anisotropy']-apo['windows']['late']['intensity_weighted_anisotropy'])
    report=dict(status='SOURCE_LABELLED_DYE_POSITION_OBSERVATIONS',results=results,source_blocks=source,
        source='Peter2022 SourceData Figure4 A:AD; source PDFphysical7Figure4a-c',
        roles='Measured anisotropy and intensity only; no author fitted lifetime/distances',
        registration='time minus own observed intensity peak; peak-normalized intensity; fixedpostpeak2-4and6-8ns',
        archive_identity='Separate165/rawarchive label ambiguity not resolved; these publisherworksheet175labels agree withmainfigure175.',
        uncertainty='One source-labelled curve percondition; time bins are not independent experimental repetitions',
        rules_extra_credit=0,optimizers=0,scientific_full_question_answer=False,
        limits=['No fitted lifetime or IRF deconvolution','No brightness/quantum-yield equivalence inferred after peak normalization',
                'No kappa-squared/R0/absolute-distance conversion','Descriptive dye/position dependence does not uniquely identify microscopic interactions'])
    (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    (out/'curves.local.json').write_text(json.dumps(curves,allow_nan=False)+'\n')
    text='# Q15 染料与位点的观测变化\n\n直接使用出版社工作簿明确标为175/58的各向异性与强度曲线，12条各3125点。每条按自身强度峰对齐，固定比较峰后2–4和6–8ns，不拟合寿命。\n\n'
    text+='| 位点/染料 | apo晚窗各向异性 | holo晚窗各向异性 | holo/apo衰减形状比 |\n|---|---:|---:|---:|\n'
    for name,v in results.items():
        text+=f"| {name} | {v['apo']['windows']['late']['intensity_weighted_anisotropy']:.5f} | {v['holo']['windows']['late']['intensity_weighted_anisotropy']:.5f} | {v['comparison']['holo_over_apo_late_early_ratio']:.5f} |\n"
    text+='\n衰减形状比是各自晚/早窗的峰归一化强度比再作holo/apo比较，较小表示该固定时间范围内衰减相对加快，不等同于拟合寿命或量子产率。各向异性按同窗强度加权。没有用时间点数构造置信区间。原始archive的165/175命名冲突仍保留，本计算来源是明确标签与主图一致的独立出版社工作簿。\n'
    (out/'REPORT_ZH.md').write_text(text)
    for name,v in results.items():print(name,v['comparison'],'late_aniso',*[v[c]['windows']['late']['intensity_weighted_anisotropy']for c in ['apo','holo']])

if __name__=='__main__':main()
