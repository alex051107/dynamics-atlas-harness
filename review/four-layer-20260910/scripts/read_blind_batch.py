"""Display only requested blind documents and their source-based keys."""
from pathlib import Path
import json,sys
r=Path(__file__).resolve().parents[1];b=r/'blind'
assert(b/'BLIND_INDEX.json').exists()
index={x['blind_id']:x for x in json.loads((b/'BLIND_INDEX.json').read_text())['index']}
for bid in sys.argv[1:]:
 x=index[bid];print('\n'+bid+' | '+x['experiment']+' | '+x['case']+' | '+x['status'])
 rubric=json.loads((b/f'{bid}.rubric.json').read_text());print('CORE:',json.dumps(rubric['core_units'],ensure_ascii=False));print('SUBQUESTIONS:',rubric.get('subquestions',[]))
 print((b/f'{bid}.md').read_text())
