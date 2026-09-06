"""Audit original distribution cells; retain source labels and unknown units."""
import json
import math
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
OUT = TASK / 'outputs/q15_deer_source_audit_v1'


def main():
    cells = json.loads((TASK / 'outputs/q15_complete_workbook_v1/Figure 3.source_cells.json').read_text())
    indexed = {c['cell']: c for c in cells}
    curves = []
    for pair, condition, columns in [
        ('55/175', 'apo', ['AJ', 'AK', 'AL', 'AM']),
        ('55/175', 'holo', ['AX', 'AY', 'AZ', 'BA']),
        ('175/228', 'apo', ['BL', 'BM', 'BN', 'BO']),
        ('175/228', 'holo', ['BZ', 'CA', 'CB', 'CC']),
    ]:
        rows = sorted(int(c['cell'][len(columns[0]):]) for c in cells
                      if c['cell'].rstrip('0123456789') == columns[0]
                      and int(c['cell'][len(columns[0]):]) >= 5)
        data = [[float(indexed[f'{col}{row}']['value']) for col in columns] for row in rows]
        assert all(math.isfinite(v) for row in data for v in row)
        assert all(b[0] > a[0] for a, b in zip(data, data[1:]))
        assert all(row[1] >= 0 for row in data)
        area = sum((b[0]-a[0])*(a[1]+b[1])/2 for a,b in zip(data,data[1:]))
        moment = sum((b[0]-a[0])*(a[0]*a[1]+b[0]*b[1])/2 for a,b in zip(data,data[1:]))
        assert area > 0
        curves.append(dict(pair=pair,condition=condition,columns=columns,
            headers=[indexed[f'{col}4']['value'] for col in columns],
            source_rows=[min(rows),max(rows)],n=len(data),grid_range=[data[0][0],data[-1][0]],
            area_source_units=area,mean_source_axis_units=moment/area,
            mode_source_axis_units=max(data,key=lambda r:r[1])[0],
            original_upper_less_than_lower_rows=sum(r[2]<r[3] for r in data),
            original_upper_greater_than_lower_rows=sum(r[2]>r[3] for r in data),
            central_outside_unordered_envelope_rows=sum(not min(r[2],r[3])-1e-7<=r[1]<=max(r[2],r[3])+1e-7 for r in data),
            central_negative_rows=sum(r[1]<0 for r in data)))
    differences=[]
    for pair in ['55/175','175/228']:
        apo,holo=[next(c for c in curves if c['pair']==pair and c['condition']==s) for s in ['apo','holo']]
        differences.append(dict(pair=pair,mean_change_source_axis_units=holo['mean_source_axis_units']-apo['mean_source_axis_units'],mode_change_source_axis_units=holo['mode_source_axis_units']-apo['mode_source_axis_units'],claim='Central author-processed curve direction only, conditional on common positive axis scale; no uncertainty or structural verdict'))
    report=dict(status='SOURCE_LABEL_CONFLICT_RETAINED',source='Complete publisher workbook Figure 3',
        source_role='AUTHOR_PROCESSED_DEER_DISTRIBUTION_NOT_RAW_TRACE_REINVERSION',
        pdf_locator='Peter 2022 DOI10.1038/s41467-022-31945-6 physical page5 Figure3c',
        visually_verified_pdf_axis='0 to 100 Angstrom',
        original_workbook_axis='r (nm)',unit_resolution='NOT_SILENTLY_RESOLVED_NO_ABSOLUTE_DISTANCE_ADMISSION',
        envelope_policy='Original upper/lower labels preserved; no swap, confidence interval, posterior or independent replicate assumption',
        curves=curves,differences=differences,optimizer_calls=0,rules_extra_credit=0,
        raw_trace_reanalyses=0,scientific_question_answer='INCOMPLETE')
    OUT.mkdir(exist_ok=True)
    (OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
