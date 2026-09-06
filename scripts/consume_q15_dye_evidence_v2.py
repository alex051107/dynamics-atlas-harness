"""Apply previously admitted processed dye observations to the existing Q15 instance."""
import argparse
import json
from pathlib import Path
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q
from dynamics_atlas_harness.q15_dye_evidence_v2 import summarize_dye_evidence


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--task-root', type=Path, required=True)
    p.add_argument('--dye-receipt', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise ValueError('OUTPUT_ALREADY_EXISTS')
    def read(name):
        return json.loads((a.task_root/'outputs'/name).read_text())
    original = dict(main=read('q15_apbs_comparison_v1/report.json'),
        summary=read('q15_pro19_verification_v1/report.json'),
        deer=read('q15_deer_source_audit_v1/report.json'), forward=read('q15_probe_forward_source_facts_v1.json'))
    q.verify_admitted_sources(original)
    receipt = json.loads(a.dye_receipt.read_text())
    dyes = {k: read(v['path']) for k, v in receipt['sources'].items()}
    # A changed source is rejected before relational synthesis and before output.
    for name, value in dyes.items():
        if q.canonical_digest(value) != receipt['sources'][name]['canonical_sha256']:
            raise ValueError('DYE_SOURCE_NOT_PREVIOUSLY_ADMITTED:'+name)
    e = q.synthesize_manual_evidence(*(original[k] for k in ['main', 'summary', 'deer', 'forward']))
    before = q.evaluate(original['main'], e, admitted_sources=original)
    de = summarize_dye_evidence(dyes, e)
    after = q.evaluate(original['main'], e, admitted_sources=original,
        dye_sources=dyes, dye_receipt=receipt, dye_evidence=de)
    off = q.evaluate(original['main'], e, False, admitted_sources=original,
        dye_sources=dyes, dye_receipt=receipt, dye_evidence=de)
    assert before['rule_instance_id'] == after['rule_instance_id'] == off['rule_instance_id']
    a.output.mkdir(parents=True)
    for name, value in {'before':before, 'after':after, 'off':off, 'evidence':de, 'admission':receipt}.items():
        (a.output/(name+'.json')).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    (a.output/'REPORT_ZH.md').write_text('# Q15 规则生成的有边界答复（待独立题级审阅）\n\n'
        +after['question_answer_candidate']['scientific_synthesis']['answer']+'\n\n'
        +'\n'.join(after['question_answer_candidate']['scientific_synthesis']['limitations'])+'\n\n'
        +de['histogram_answer']+'\n\n'+de['probe_answer']+'\n\n'
        +'以下表格按绑定数值比较两对位点的荧光、DEER 与参考探针预测。方向关系本身不构成人口估计或唯一机制证明。\n\n'
        +'| 位点 | 实测 Alexa E 变化 | DEER 中心变化（来源轴单位） | 参考读出关系 |\n|---|---:|---:|---|\n'
        +''.join(f"| {r['pair']} | {r['observed_E_effect']:.8f} | {r['DEER_central_mean_change_source_axis_units']:.8f} | {r['fluorescence_relation']} |\n" for r in e['rows'])
        +'\n'+ '\n'.join('- '+x for x in de['limits'])+'\n\n'
        +'本轮将既有人工数值证据接回同一规则实例，未重跑原 APBS、DEER 或寿命拟合，新增数值补算计数为 0。规则关闭时不产生这份题级综合。完成开发答案数暂不增加，等待独立审阅题级证据是否充分。\n')
    print(json.dumps({'same_instance': True, 'on_evidence_applications': after['evidence_applications'],
        'off_evidence_applications': off['evidence_applications'], 'new_numeric_operators':0,
        'answer': after['partial_answer_status'], 'histogram':de['histogram_answer'], 'probe':de['probe_answer']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
