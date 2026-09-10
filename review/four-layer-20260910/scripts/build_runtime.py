from pathlib import Path
import shutil
r=Path(__file__).resolve().parents[1];src=Path.cwd()/'dynamics-atlas-harness-luna-runtime-v1/agent_experiments/protocol_comparison_v1';rt=r/'runtime'
for fn in ['agent_run.py','container_tools.py','common_prompt.txt']:shutil.copy2(src/fn,rt/fn)
p=rt/'agent_run.py';t=p.read_text();t=t.replace("choices=['D','P','R']","choices=['D','CARD','FEEDBACK','P','R_old','R_scoped','ORIGINAL','SPLIT']");t=t.replace("if arm=='D': return ''\n    return (case_root/('arm_'+arm)/'GUIDANCE.md').read_text()","p=case_root/('arm_'+arm)/'GUIDANCE.md'\n    return p.read_text() if p.exists() else ''")
t=t.replace("if datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['absolute_deadline']):","if spec.get('absolute_deadline') and datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['absolute_deadline']):").replace("if datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['round_deadline']):","if spec.get('round_deadline') and datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['round_deadline']):")
t=t.replace("    cmd=['docker','run'","    if args.arm=='CARD':\n        import shutil\n        mounted=out/'source';shutil.copytree(source,mounted);shutil.copy2(case_root/'arm_CARD/ADMISSION_CARD.json',mounted/'ADMISSION_CARD.json');source=validate_common(mounted)\n    cmd=['docker','run'",1)
t=t.replace("user=(source/'QUESTION.txt').read_text()","user=(source/'QUESTION.txt').read_text()\n    if args.arm=='SPLIT':user=(case_root/'arm_SPLIT/QUESTION.txt').read_text()")
t=t.replace("result={'message':'One optional revision remains in the same budget. Re-submit unchanged if no revision needed.'}","result={'message':'One optional revision remains in the same budget. Re-submit unchanged if no revision needed.'}\n            if args.arm=='FEEDBACK':\n                from ceiling_check import check_submission\n                result['checks']=check_submission(record,tool_outputs,source)\n                log('ceiling_feedback',result['checks'])")
t=t.replace("'runner_stage':'DPR_guidance_v1'","'runner_stage':'four_layer_v2'")
p.write_text(t)
(rt/'ceiling_check.py').write_text('def check_submission(record, tool_outputs, source):\n    raise RuntimeError("E2 checker not installed in this experiment")\n')
print('Base four-layer runtime prepared; E2 own frozen copy required')
