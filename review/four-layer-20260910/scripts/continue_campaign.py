from pathlib import Path
import json,time,subprocess,sys,datetime
r=Path(__file__).resolve().parents[1];e=r/'E1b'
# Existing E1b owns its per-round lock. Never dispatch another copy.
while json.loads((e/'runtime/readiness.json').read_text()).get('approved_for_development'):
 time.sleep(5)
if list(r.glob('*/outputs/UNKNOWN_CHARGE.json')):
 print('GLOBAL STOP unknown charge',flush=True);sys.exit(1)
for name in ['ADK_plain','E2','E3','E4']:
 if (r/'USER_STOP.json').exists():break
 if list(r.glob('*/outputs/UNKNOWN_CHARGE.json')):print('GLOBAL STOP unknown charge',flush=True);break
 spent=sum(json.loads(l)['cost']for p in r.glob('*/outputs/paid_usage.jsonl')for l in p.read_text().splitlines())
 if spent>=1.85:print('GLOBAL COST STOP',spent,flush=True);break
 if (r/name/'outputs/private_run_manifest.json').exists():raise RuntimeError('Do not duplicate an already started experiment')
 print('START',name,datetime.datetime.now(datetime.timezone.utc).isoformat(),flush=True)
 p=subprocess.run([sys.executable,str(r/'scripts/run_experiment.py'),name])
 if list(r.glob('*/outputs/UNKNOWN_CHARGE.json')):print('GLOBAL STOP unknown charge',flush=True);break
 # A known per-experiment budget stop ends that experiment only; other independent budgets stay bounded.
 stop=r/name/'outputs/STOP.json'
 if stop.exists()and json.loads(stop.read_text()).get('reason')!='COST_LIMIT':print('GLOBAL STOP execution failure',name,flush=True);break
print('CAMPAIGN_RUNNER_EXIT',flush=True)
