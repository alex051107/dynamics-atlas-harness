from pathlib import Path
import json,random,hashlib,datetime,sys,shutil,subprocess
r=Path(__file__).resolve().parents[1];name=sys.argv[1];e=r/name;spec=json.loads((e/'DESIGN.json').read_text());assert not(e/'FREEZE.json').exists();(e/'runtime').mkdir(exist_ok=True);(e/'outputs').mkdir(exist_ok=True);(e/'runs').mkdir(exist_ok=True)
for p in (r/'runtime').iterdir():
 if p.is_file() and not(e/'runtime'/p.name).exists():shutil.copy2(p,e/'runtime'/p.name)
order=[{'case':c,'arm':a,'replicate':i}for c in spec['cases']for a in spec['arms']for i in range(1,spec['replicates']+1)];random.Random(spec['seed']).shuffle(order)
(e/'runtime/campaign.json').write_text(json.dumps({'task_roots':['../E1b','../E2','../E3','../E4','../ADK_plain'],'round_cost_roots':['.'],'absolute_deadline':None,'round_deadline':None,'model_cost_cap_usd':1.85},indent=2))
image='sha256:d99fa29fcffbf7de8dce05abf1c71a7002c39acf8e19276328582a5556c84e29'
sys.path.insert(0,str(e/'runtime'));from agent_run import validate_common
for c in (e/'cases').iterdir():validate_common(c/'common');assert(c/'hidden/rubric.json').exists()
freeze={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'run_order':order,'image':image,'cap_usd':spec['cap_usd'],'sha256':{str(p.relative_to(e)):hashlib.sha256(p.read_bytes()).hexdigest()for top in ['cases','runtime']for p in(e/top).rglob('*')if p.is_file() and p.suffix in ['.py','.txt','.md','.json','.tsv','.csv','.pdf']},'design':spec,'design_sha256':hashlib.sha256((e/'DESIGN.json').read_bytes()).hexdigest()};(e/'FREEZE.json').write_text(json.dumps(freeze,indent=2));(e/'runtime/readiness.json').write_text(json.dumps({'approved_for_development':True,'authorization':'user15–18'}));print(name,'FROZEN',len(order))
