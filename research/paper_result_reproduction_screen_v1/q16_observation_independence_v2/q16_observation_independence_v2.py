"""Actual 14-block Pro21 check, preserving the original coupled extraction."""
import json
from pathlib import Path
from q16_condition_inventory_v1 import BLOCKS, colnum, col
from dynamics_atlas_harness.q16_source_extract_v2 import extract_processed_roles
from dynamics_atlas_harness.q16_common_window_v1 import POLICY, validate_input

TASK = Path(__file__).resolve().parents[1]
REPO = TASK.parents[2]/'dynamics-atlas-harness-rules-prototype-acceptance-v1'

def main():
    out = TASK/'outputs/q16_observation_independence_v2'
    out.mkdir(exist_ok=False)
    old = json.loads((TASK/'outputs/q16_condition_inventory_v1/source_curves.local.json').read_text())
    new = json.loads(json.dumps(old))
    sheets = {sheet:{cell['cell']:cell for cell in json.loads((TASK/'outputs/q15_complete_workbook_v1'/f'{sheet}.source_cells.json').read_text())} for sheet,_,_ in BLOCKS}
    audits = []
    for sheet,condition,start in BLOCKS:
        key = sheet+':'+condition
        column = colnum(start)+4
        result = extract_processed_roles(sheets[sheet],*[col(column+i) for i in range(3)])
        new[key]['processed'] = result['processed']
        new[key]['fit_audit'] = result['fit_audit']
        unchanged = result['processed'] == [row[:2] for row in old[key]['processed']]
        audits.append(dict(key=key, observation_values_unchanged=unchanged, **result['selection_audit']))
    pairs = {}
    for pair,conditions in [('29',['eg50_1mM','eg50_10mM','eg0_1mM','eg25_1mM','gly25_1mM']),('36',['eg50_1mM','eg50_10mM','eg0_1mM'])]:
        pairs[pair] = {}
        for condition in conditions:
            sheet = 'SI Figure9' if condition=='eg50_10mM' else 'SI Figure10'
            key = sheet+':'+pair+'_'+condition
            record = new[key]
            pairs[pair][condition] = dict(source_block=key,role='AUTHOR_DEPOSITED_OBSERVED_DEER_TRACES',raw=record['raw'],processed=record['processed'])
    payload = dict(doi='10.1038/s41467-022-31945-6',policy=POLICY,pairs=pairs)
    prior = json.loads((REPO/'research/paper_result_reproduction_screen_v1/q16_common_window_v1/source_admission.json').read_text())
    identity = validate_input(payload)
    report = dict(status='OBSERVATIONS_IDENTICAL_NO_SCIENCE_RERUN' if all(a['observation_values_unchanged'] for a in audits) and identity==prior['input_id'] else 'CHANGED_SOURCE_REQUIRES_EXPLICIT_READMISSION',
        blocks=audits, prior_input_id=prior['input_id'], new_observed_input_id=identity,
        operator_calls=0, source='Original full XLSX parsed cells, Figure5/SI Figure9/SI Figure10',
        source_roles='processed is time+observed only; fit_audit is separate time+fit, never selects observed rows')
    (out/'source_curves.local.json').write_text(json.dumps(new)+'\n')
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    (out/'REPORT_ZH.md').write_text('# Q16 观测点提取核对\n\n'+report['status']+'。真实14个块中，时间加观测有效的行集合与旧版额外要求fit有效的集合逐一核对，完整差集见report.json。\n\n'
        '新版将作者拟合曲线独立为方法审计角色，不能决定观测点是否进入计算。旧提取和原结果保留；若既有输入身份相同，不重复运行科学比较。\n')
    print(json.dumps({'status':report['status'],'blocks':len(audits),'differences':{a['key']:a['previously_excluded_observed_rows'] for a in audits},'input_id':identity,'operator_calls':0},indent=2))

if __name__ == '__main__':
    main()
