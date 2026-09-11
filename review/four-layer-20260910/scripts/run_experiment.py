from pathlib import Path
import json,sys,subprocess,hashlib,datetime
r=Path(__file__).resolve().parents[1];e=r/sys.argv[1];f=json.loads((e/'FREEZE.json').read_text());records=[];mf=e/'outputs/private_run_manifest.json'
if mf.exists():records=json.loads(mf.read_text())
for name,h in f['sha256'].items():assert hashlib.sha256((e/name).read_bytes()).hexdigest()==h,name
for i,spec in enumerate(f['run_order'],1):
 if i<=len(records):continue
 if list(r.glob('*/outputs/UNKNOWN_CHARGE.json')):print('STOP UNKNOWN_CHARGE');break
 if not json.loads((e/'runtime/readiness.json').read_text())['approved_for_development']:break
 before=set((e/'runs').iterdir());cmd=[sys.executable,str(e/'runtime/agent_run.py'),spec['case'],spec['arm'],'--image',f['image'],'--task-root',str(e),'--budget-usd',str(f['cap_usd'])];p=subprocess.run(cmd,capture_output=True,text=True);created=set((e/'runs').iterdir())-before
 if len(created)!=1:(e/'outputs/STOP.json').write_text(json.dumps({'reason':'setup_failure','stderr':p.stderr[-1000:]}));break
 run=created.pop();receipt=json.loads((run/'receipt.json').read_text())if(run/'receipt.json').exists()else{'status':'EXECUTION_ERROR'};records.append({'index':i,**spec,'run':run.name,'receipt':receipt});mf.write_text(json.dumps(records,indent=2));ledger=e/'outputs/paid_usage.jsonl';cost=sum(json.loads(x)['cost']for x in ledger.read_text().splitlines())if ledger.exists()else 0
 line=f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} | {e.name} {i}/{len(f['run_order'])} | {receipt['status']} | ${cost:.8f}";print(line,flush=True)
 with(r.parent/'outputs/ONE_SHOT_PROGRESS.md').open('a')as h:h.write('\n'+line)
 if receipt.get('unknown_charge')or receipt['status']in ['COST_LIMIT','EXECUTION_ERROR']:(e/'outputs/STOP.json').write_text(json.dumps({'reason':receipt['status'],'index':i,'cost':cost}));break
(e/'runtime/readiness.json').write_text(json.dumps({'approved_for_development':False,'ended':True}));print('EXIT',e.name,len(records),flush=True)
