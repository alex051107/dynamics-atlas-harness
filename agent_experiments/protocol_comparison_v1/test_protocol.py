from pathlib import Path
import tempfile,json
from agent_run import guidance,validate_common,campaign_usage
with tempfile.TemporaryDirectory()as t:
 p=Path(t);(p/'common').mkdir();(p/'common/data.txt').write_text('same data')
 for arm,text in [('P','existing seven-rule protocol'),('R','selector-rendered guidance')]:
  (p/('arm_'+arm)).mkdir();(p/('arm_'+arm)/'GUIDANCE.md').write_text(text)
 assert guidance(p,'D')==''
 assert guidance(p,'P')=='existing seven-rule protocol'
 assert guidance(p,'R')=='selector-rendered guidance'
 validate_common(p/'common')
 (p/'common/hidden').mkdir()
 try:validate_common(p/'common');raise AssertionError('hidden directory admitted')
 except RuntimeError:pass
 (p/'runtime').mkdir();(p/'outputs').mkdir();(p/'old/outputs').mkdir(parents=True)
 (p/'outputs/paid_usage.jsonl').write_text(json.dumps({'cost':.05})+'\n');(p/'old/outputs/paid_usage.jsonl').write_text(json.dumps({'cost':.13830195})+'\n')
 (p/'runtime/campaign.json').write_text(json.dumps({'task_roots':['.','old'],'absolute_deadline':'2099-01-01T00:00:00+00:00','round_deadline':'2099-01-01T00:00:00+00:00','model_cost_cap_usd':1.55}))
 assert abs(campaign_usage(p)[0]-.18830195)<1e-12
s=Path(__file__).with_name('agent_run.py').read_text();assert "choices=['D','P','R']"in s and 'harness_checks'not in s and "args.arm=='C'"not in s
print('PASS guidance routing, common-source isolation, carried cost, no C execution')
