from pathlib import Path
import json,datetime
r=Path(__file__).resolve().parents[1];out=[]
for name in ['E1b','ADK_plain','E2','E3','E4']:
 e=r/name;f=json.loads((e/'FREEZE.json').read_text());p=e/'outputs/private_run_manifest.json';a=json.loads(p.read_text())if p.exists()else[];ledger=e/'outputs/paid_usage.jsonl';usage=[json.loads(l)for l in ledger.read_text().splitlines()]if ledger.exists()else[]
 out.append({'experiment':name,'planned':len(f['run_order']),'completed_attempts':len(a),'accepted_answers':sum(bool(x.get('receipt',{}).get('answer_sha256'))for x in a),'settled_cost_usd':round(sum(x['cost']for x in usage),8),'cap_usd':f['cap_usd'],'requests':len(usage),'closed':not json.loads((e/'runtime/readiness.json').read_text()).get('approved_for_development'),'stop':json.loads((e/'outputs/STOP.json').read_text())if(e/'outputs/STOP.json').exists()else None,'request_marker_present':(e/'outputs/UNKNOWN_CHARGE.json').exists()})
s={'as_of':datetime.datetime.now(datetime.timezone.utc).isoformat(),'experiments':out,'total_settled_new_cost_usd':round(sum(x['settled_cost_usd']for x in out),8),'new_cap_usd':1.85,'historical_four_batches_usd':.28550861,'note':'A marker can be a live request; reconcile against live process before declaring unknown charge. No answer quality has been inferred from receipt status.'}
(r/'outputs/CAMPAIGN_PROGRESS.json').write_text(json.dumps(s,indent=2));print(json.dumps(s,indent=2))
