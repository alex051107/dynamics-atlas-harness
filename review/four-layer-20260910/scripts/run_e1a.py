from pathlib import Path
import json,hashlib,datetime
from admission_check import check
r=Path(__file__).resolve().parents[1];b=r/'E1a';assert not(b/'E1a_RESULTS.json').exists(),'No outcome-driven reruns'
f={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest()for p in b.rglob('*')if p.is_file()},'checker_sha256':hashlib.sha256(Path(__file__).with_name('admission_check.py').read_bytes()).hexdigest()};(b/'FREEZE.json').write_text(json.dumps(f,indent=2));plan=json.loads((b/'E1_PLANTED_DEFECTS.json').read_text());out=[]
for name in plan['clean']+[p['packet']for p in plan['defects']]:
 p=b/'packets'/name;system=json.loads((p/'DECLARED_METADATA.json').read_text())['system'];res=check(p,b/'reference'/system);res['packet']=name;res['is_planted_defect']=name not in plan['clean'];out.append(res)
clean_fp=sum(x['status']=='FAIL'for x in out if not x['is_planted_defect']);caught=sum(x['status']=='FAIL'for x in out if x['is_planted_defect']);real=next(x['status']=='FAIL'for x in out if x['packet']=='defect_1');status='MET'if caught>=5 and clean_fp==0 and real else'NOT_MET';data={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':out,'clean_falsepositives':clean_fp,'caught':caught,'defects':6,'real_defect_caught':real,'code_criterion':status,'agent_behavior_not_tested':True};(b/'E1a_RESULTS.json').write_text(json.dumps(data,indent=2));print(json.dumps({k:v for k,v in data.items()if k!='results'}))
