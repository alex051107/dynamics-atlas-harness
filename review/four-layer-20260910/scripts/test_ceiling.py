from pathlib import Path
import sys,tempfile,json
r=Path(__file__).resolve().parents[1];sys.path.insert(0,str(r/'runtime'));from ceiling_check import check_submission
with tempfile.TemporaryDirectory()as d:
 p=Path(d);(p/'PUBLIC_FACTS.json').write_text(json.dumps([{'relation':'used_in_fitting','result_id':'r','observation_subset':'s','analysis_id':'a'}]))
 clean={'answer':'在本轨迹0–10ns窗口内均值4.62Å；不能得到平衡占比。','claims':[{'text':'本轨迹均值4.62Å','origin':'current_calculation','quantity':4.62,'observation_subset':'trajectory0–10ns'},{'text':'不能得到平衡占比','polarity':'negative'}]};assert not check_submission(clean,[{'mean':4.62}],p)['flags']
 bad={'answer':'均值92','claims':[{'text':'equilibrium population is 0.9','polarity':'affirmative'},{'text':'numeric result','origin':'current_calculation','quantity':92},{'text':'independent validation','evidence_role':'independent_validation','result_id':'r','observation_subset':'s','analysis_id':'a'}]};f=check_submission(bad,[{'mean':4.62}],p)['flags'];assert {x['check']for x in f}=={'claim_ceiling','numeric_trace','evidence_role','unit_window'}
 assert check_submission({'answer':'作者报告4.3ms','claims':[{'text':'作者报告4.3ms','origin':'author_report'}]},[],p)['flags']==[]
print('PASS fixed narrow checker controls; not empirical layer effectiveness')
