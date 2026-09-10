"""Record reviewer-authored judgments without loading the condition key."""
from pathlib import Path
import json,csv,sys,datetime,hashlib
r=Path(__file__).resolve().parents[1];b=r/'blind';out=b/'reviewer_scores.json';index=json.loads((b/'BLIND_INDEX.json').read_text())['index'];ids={x['blind_id']for x in index}
if sys.argv[1]=='seal':
 rows=json.loads(out.read_text());assert {x['blind_id']for x in rows}==ids,'Every available output requires a score';assert not(b/'SCORE_SEAL.json').exists(),'Scores already sealed'
 initial=b/'INITIAL_BLIND_SCORES.json';assert initial.exists(),'Record E2 initial judgments before reveal';initial_rows=json.loads(initial.read_text());assert {x['blind_id']for x in initial_rows}=={x['blind_id']for x in index if x['experiment']=='E2'}
else:
 assert not(b/'SCORE_SEAL.json').exists(),'No post-seal edits';rows=json.loads(out.read_text())if out.exists()else[];new=json.loads(Path(sys.argv[1]).read_text());existing={x['blind_id']for x in rows}
 for x in new:
  assert x['blind_id']in ids and x['blind_id']not in existing,x['blind_id'];assert len(x['units'])==5 and all(v in ['C','M','E']for v in x['units']);assert x['rationale']
  for k in ['core_errors','overclaim','unnecessary_abstention','defect_detected','defect_downgraded','next_action','inapplicable_adoption','subquestion_coverage']:assert isinstance(x[k],int)and x[k]>=0,k
  existing.add(x['blind_id'])
 rows+=new;rows.sort(key=lambda x:x['blind_id']);out.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
fields=['blind_id','core_correct','core_errors','overclaim','unnecessary_abstention','defect_detected','defect_downgraded','next_action','inapplicable_adoption','subquestion_coverage','units','rationale']
with(b/'blind_scores.csv').open('w')as h:
 w=csv.DictWriter(h,fieldnames=fields);w.writeheader()
 for x in rows:w.writerow({**{k:x[k]for k in fields if k not in ['core_correct','units']},'core_correct':x['units'].count('C'),'units':''.join(x['units'])})
if sys.argv[1]=='seal':
 seal={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'n':len(rows),'sha256':hashlib.sha256((b/'blind_scores.csv').read_bytes()).hexdigest(),'reviewer':'current Codex session, condition labels withheld; case curator overlap disclosed','unblinded':False,'initial_scores_sha256':hashlib.sha256((b/'INITIAL_BLIND_SCORES.json').read_bytes()).hexdigest()};(b/'SCORE_SEAL.json').write_text(json.dumps(seal,indent=2));print('SEALED',len(rows))
else:print('Recorded',len(rows),'of',len(ids),'blind scores')
