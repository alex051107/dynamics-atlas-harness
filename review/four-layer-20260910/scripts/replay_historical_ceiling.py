from pathlib import Path
import csv,json,sys,datetime
from collections import deque
r=Path(__file__).resolve().parents[1];sys.path.insert(0,str(r/'E2/runtime'));from ceiling_check import check_submission
rows=list(csv.DictReader((r/'outputs/E0_RETROSPECTIVE_AUDIT.csv').open()));paths={str(Path(x['observed_in']).parent)for x in rows};paths.add('autoresearch/tasks/dynamics_atlas_hsp90_first_round_v3_20260910/runs/HSP90_Q01_A_8bb1da99');out=[]
for name in sorted(paths):
 p=Path(name);answer=(p/'answer.md').read_text();drafts=list(p.glob('draft_*.json'));matched=[(q,json.loads(q.read_text()))for q in drafts if json.loads(q.read_text())['answer']==answer];assert len(matched)>=1;draft,record=sorted(matched,key=lambda v:int(v[0].stem.split('_')[-1]))[-1]
 task=p.parents[1];case=json.loads((p/'receipt.json').read_text())['case'];source=task/'cases'/case/'common'
 if not source.exists():source=task/'cases'/case # earlier development packages used a flat source directory
 assert(source/'SOURCE_INVENTORY.json').exists(),source
 outputs=[];pending=deque();located=False
 for line in(p/'events.jsonl').read_text().splitlines():
  event=json.loads(line);v=event['value']
  if event['kind']=='response':
   pending=deque(x['function']['name']for x in v['choices'][0]['message'].get('tool_calls',[]))
  elif event['kind']=='tool_output':
   fn=pending.popleft()if pending else None
   if fn=='workspace':outputs.append(v)
  elif event['kind']=='submission'and v==record:located=True;break
 assert located,p
 result=check_submission(record,outputs,source)
 out.append({'run':p.name,'source':str(source),'submission':str(draft),'workspace_outputs_before_submission':len(outputs),'public_facts_present':(source/'PUBLIC_FACTS.json').exists(),'claims':record['claims'],'result':result,'scope':'offline replay with existing original claim representation; not a new agent response or causal prevention test'})
(r/'outputs/E0_CEILING_REPLAY.json').write_text(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':'E2/runtime/ceiling_check.py, frozen current implementation','runs':out},ensure_ascii=False,indent=2));print(json.dumps([{'run':x['run'],'flags':x['result']['flags'],'unverified':x['result']['unverified']}for x in out],ensure_ascii=False,indent=2))
