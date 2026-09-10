from pathlib import Path
import json,random,hashlib,re,datetime,shutil
r=Path(__file__).resolve().parents[1];b=r/'blind';assert not(b/'BLIND_INDEX.json').exists(),'No repeated assignment';b.mkdir(exist_ok=True);rows=[];completeness={}
for exp in ['E1b','ADK_plain','E2','E3','E4']:
 e=r/exp;mf=e/'outputs/private_run_manifest.json';records=json.loads(mf.read_text())if mf.exists()else[];target=len(json.loads((e/'FREEZE.json').read_text())['run_order']);completeness[exp]={'completed_attempts':len(records),'planned':target,'complete':len(records)==target}
 if json.loads((e/'runtime/readiness.json').read_text()).get('approved_for_development'):raise RuntimeError('Wait until experiment closes')
 for x in records:rows.append({'experiment':exp,**x})
random.Random(2026091050).shuffle(rows);key=[];index=[]
for i,x in enumerate(rows,1):
 bid=f'V{i:03d}';run=r/x['experiment']/'runs'/x['run'];answer=run/'answer.md';text=answer.read_text()if answer.exists()else'[NO SUBMITTED ANSWER]';rc=x['receipt']
 if answer.exists():assert hashlib.sha256(answer.read_bytes()).hexdigest()==rc['answer_sha256']
 def redact(t):
  t=t.replace(x['run'],'[run redacted]');t=re.sub(r'\b(?:Arm|组别)\s*[:：]?\s*(?:R_scoped|R_old|FEEDBACK|ORIGINAL|SPLIT|CARD|D|P)\b','[condition redacted]',t);return re.sub(r'\[?C\d{3}-RULE-\d{3}\]?','[rule id redacted]',t)
 (b/f'{bid}.md').write_text(redact(text));first=run/'draft_1.json'
 if first.exists():(b/f'{bid}_initial.md').write_text(redact(json.loads(first.read_text())['answer']))
 rubric=r/x['experiment']/'cases'/x['case']/'hidden/rubric.json';shutil.copy2(rubric,b/f'{bid}.rubric.json')
 trace=[]
 for line in(run/'events.jsonl').read_text().splitlines():
  event=json.loads(line)
  if event['kind']=='tool_output':
   v=event['value']
   if isinstance(v,dict):v={k:q for k,q in v.items()if k not in ['image_base64','checks']}
   trace.append(v)
 (b/f'{bid}_tool_outputs.json').write_text(redact(json.dumps(trace,ensure_ascii=False,indent=2)))
 index.append({'blind_id':bid,'experiment':x['experiment'],'case':x['case'],'status':rc['status'],'submitted':answer.exists()});key.append({'blind_id':bid,'experiment':x['experiment'],'case':x['case'],'arm':x['arm'],'replicate':x['replicate'],'run':x['run'],'answer_sha256':rc.get('answer_sha256')})
(b/'BLIND_INDEX.json').write_text(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'completeness':completeness,'index':index},indent=2));(r/'outputs/BLIND_KEY_PRIVATE.json').write_text(json.dumps(key,indent=2));print('Blinded',len(index),'outputs; no condition key printed')
