"""One source-receipt audit and manual verification of Pro19 summary checks."""
import datetime
import json
from pathlib import Path

from dynamics_atlas_harness.q15_apbs_comparison_v1 import validate_member_bytes

TASK = Path(__file__).resolve().parents[1]
OUT = TASK / 'outputs/q15_pro19_verification_v1'


def main():
    OUT.mkdir(exist_ok=False)
    checked=[]
    for source in ['q15_apbs_intake_v1','q15_normal_control_intake_v1']:
        intake=json.loads((TASK/'outputs'/source/'member_intake_receipt.json').read_text())
        for item in intake['results']:
            name=item['member']['name']
            if not name.endswith('_apbs_alex.csv'):continue
            if item['status']!='LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH':raise ValueError('SOURCE_NOT_ADMITTED')
            data=(TASK/'outputs'/source/'source_members'/name).read_bytes()
            validate_member_bytes(data,item['member'])
            checked.append({'member':name,'status':'EXPANDED_LENGTH_AND_CRC_MATCH'})
    assert len(checked)==140
    report=json.loads((TASK/'outputs/q15_apbs_comparison_v1/report.json').read_text())
    diagnostics={}
    for pair in ['175_228','55_175']:
        groups={s:[r for r in report['repetitions'] if r['pair']==pair and r['condition']==s] for s in ['apo','holo']}
        assert all(len(v)==3 for v in groups.values())
        means={s:[r['E']['mean'] for r in rows] for s,rows in groups.items()}
        median_effect=sum(r['E']['median'] for r in groups['holo'])/3-sum(r['E']['median'] for r in groups['apo'])/3
        leave=[(sum(means['holo'])-means['holo'][h])/2-(sum(means['apo'])-means['apo'][a])/2 for h in range(3) for a in range(3)]
        shifts={}
        for s,rows in groups.items():
            lower=sum(r['E_above_one']*min(0,1-r['E']['maximum'])/r['E']['n'] for r in rows)/3
            upper=sum(r['E_below_zero']*max(0,-r['E']['minimum'])/r['E']['n'] for r in rows)/3
            shifts[s]=[lower,upper]
        effect=report['condition_comparisons'][pair]['holo_minus_apo_E']
        diagnostics[pair]={'equal_repetition_mean_effect':effect,'equal_repetition_median_effect':median_effect,
                           'leave_one_per_condition_effects':leave,'leave_one_per_condition_range':[min(leave),max(leave)],
                           'fixed_selected_E_clipping_effect_bound':[effect+shifts['holo'][0]-shifts['apo'][1],effect+shifts['holo'][1]-shifts['apo'][0]],
                           'interpretation':'Descriptive group-effect sensitivity; no added experiments, paired design or confidence interval'}
    result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_crc_length_audit':checked,
            'input_id':report['input_id'],'source_audit_status':'ALL140_MATCH_ORIGINAL_RECEIPTS',
            'main_science_recomputed':False,'original_main_report_preserved':True,'diagnostics':diagnostics,
            'provenance':'MANUAL_VERIFICATION_OF_ALREADY_PRODUCED_PRO19_DIAGNOSTICS',
            'rules_extra_credit':0,'scientific_question_answer':False}
    (OUT/'report.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'files':len(checked),'diagnostics':diagnostics},indent=2))


if __name__=='__main__':main()
