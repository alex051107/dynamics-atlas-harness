"""Reveal only after sealing; describe all observations without automatic scientific grading."""
from pathlib import Path
from collections import defaultdict
from statistics import median
from decimal import Decimal
import json,csv,hashlib,datetime
r=Path(__file__).resolve().parents[1];b=r/'blind';o=r/'outputs';seal=json.loads((b/'SCORE_SEAL.json').read_text());assert hashlib.sha256((b/'blind_scores.csv').read_bytes()).hexdigest()==seal['sha256'];assert hashlib.sha256((b/'INITIAL_BLIND_SCORES.json').read_bytes()).hexdigest()==seal['initial_scores_sha256'];assert not(o/'UNBLINDING.json').exists(),'No repeated reveal'
key=json.loads((o/'BLIND_KEY_PRIVATE.json').read_text());scores={x['blind_id']:x for x in csv.DictReader((b/'blind_scores.csv').open())};initial={x['blind_id']:x for x in json.loads((b/'INITIAL_BLIND_SCORES.json').read_text())};groups=defaultdict(list);joined=[];flags=[];revisions=[]
metrics=['core_correct','core_errors','overclaim','unnecessary_abstention','defect_detected','defect_downgraded','next_action','inapplicable_adoption','subquestion_coverage']
for k in key:
 s=scores[k['blind_id']];row={**k,**s};row.update({m:int(s[m])for m in metrics});run=r/k['experiment']/'runs'/k['run'];rc=json.loads((run/'receipt.json').read_text());row.update({'cost_usd':rc.get('totals',{}).get('cost',0),'input_tokens':rc.get('totals',{}).get('input',0),'output_tokens':rc.get('totals',{}).get('output',0),'wall_seconds':rc.get('wall_seconds',0),'accepted':(run/'answer.md').exists(),'status':rc['status']});joined.append(row);groups[(k['experiment'],k['case'],k['arm'])].append(row)
 if k['experiment']=='E2':
  ini=initial[k['blind_id']];revisions.append({'blind_id':k['blind_id'],'case':k['case'],'arm':k['arm'],'initial_core_errors':ini['core_errors'],'final_core_errors':row['core_errors'],'initial_overclaim':ini['overclaim'],'final_overclaim':row['overclaim'],'initial_core_correct':ini['units'].count('C'),'final_core_correct':row['core_correct'],'initial_rationale':ini['rationale']})
  draft=json.loads((run/'draft_1.json').read_text())if(run/'draft_1.json').exists()else{}
  for line in(run/'events.jsonl').read_text().splitlines():
   ev=json.loads(line)
   if ev['kind']=='ceiling_feedback':
    for j,flag in enumerate(ev['value']['flags']):
     idx=flag.get('claim_index');claim=draft.get('claims',[])[idx]if isinstance(idx,int)and idx<len(draft.get('claims',[]))else None
     flags.append({'flag_id':f"{k['blind_id']}-F{j+1}",'blind_id':k['blind_id'],'case':k['case'],'check':flag['check'],'flag':flag,'claim':claim,'review_classification':None,'review_rationale':None})
summary=[]
for (exp,case,arm),rows in sorted(groups.items()):
 summary.append({'experiment':exp,'case':case,'arm':arm,'n':len(rows),'accepted':sum(x['accepted']for x in rows),'median':{m:median(x[m]for x in rows)for m in metrics},'sum':{m:sum(x[m]for x in rows)for m in metrics},'cost_usd':float(sum(Decimal(str(x['cost_usd']))for x in rows)),'input_tokens':sum(x['input_tokens']for x in rows),'output_tokens':sum(x['output_tokens']for x in rows),'wall_seconds':sum(x['wall_seconds']for x in rows)})
with(o/'UNBLINDED_SCORES.csv').open('w')as h:w=csv.DictWriter(h,fieldnames=list(joined[0]));w.writeheader();w.writerows(joined)
(o/'GROUP_RESULTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));(o/'E2_REVISION_COMPARISON.json').write_text(json.dumps(revisions,ensure_ascii=False,indent=2));(o/'E2_FLAG_REVIEW.json').write_text(json.dumps(flags,ensure_ascii=False,indent=2));(o/'UNBLINDING.json').write_text(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'score_seal':seal,'n':len(joined),'primary_scores_unchanged':True},indent=2));print('Revealed',len(joined),'outputs;',len(summary),'groups;',len(flags),'flags require independent semantic review')
