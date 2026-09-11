import contextlib,io,json,subprocess,sys,tempfile
from pathlib import Path
from unittest.mock import patch
import agent_run as runner

def exercise(arm,budget=0.15):
    with tempfile.TemporaryDirectory() as directory:
        root=Path(directory);common=root/'cases/test/common';common.mkdir(parents=True)
        (root/'runtime').mkdir();(root/'outputs').mkdir()
        (root/'runtime/readiness.json').write_text('{"approved_for_development":true}')
        (root/'runtime/campaign.json').write_text(json.dumps({'task_roots':['.'],'absolute_deadline':'2999-01-01T00:00:00+00:00','round_deadline':'2999-01-01T00:00:00+00:00','model_cost_cap_usd':0.60}))
        question='科学问题，仅用本轮资料。';rules='可质疑的规则提示。'
        (common/'QUESTION.txt').write_text(question)
        private=root/'cases/test/arm_B';private.mkdir();(private/'ACTIVE_RULES.md').write_text(rules)
        (root/'cases/test/hidden').mkdir()
        requests=[];commands=[]
        def call(request,**kwargs):
            requests.append(json.loads(request.data))
            msg={'role':'assistant','content':None,'tool_calls':[{'id':'s','type':'function','function':{'name':'submit','arguments':json.dumps({'answer':'retained answer','claims':[{'text':'an unresolved interpretation'}]})}}]}
            return io.BytesIO(json.dumps({'id':'fixture','choices':[{'message':msg}],'usage':{'prompt_tokens':100,'completion_tokens':20,'cost':0}}).encode())
        def command(args,**kwargs):
            commands.append(args);return subprocess.CompletedProcess(args,0,'mock','')
        assert 'finite_checks' not in sys.modules
        with patch.object(runner,'credential',return_value='dummy'),patch.object(runner,'balance_precheck',return_value=4),patch.object(runner.urllib.request,'urlopen',side_effect=call),patch.object(runner.subprocess,'run',side_effect=command),patch.object(sys,'argv',['agent_run','test',arm,'--task-root',str(root),'--image','mock','--budget-usd',str(budget)]),contextlib.redirect_stdout(io.StringIO()):runner.main()
        assert 'finite_checks' not in sys.modules
        cmd=next(c for c in commands if c[:2]==['docker','run'])
        mounts=[cmd[i+1] for i,x in enumerate(cmd) if x=='-v']
        assert len(mounts)==3
        assert [m for m in mounts if m.endswith(':/source:ro')]==[str(common.resolve())+':/source:ro']
        assert len([m for m in mounts if m.endswith(':/work:rw')])==1
        assert len([m for m in mounts if m.endswith(':/tool.py:ro')])==1
        assert not any('/hidden' in m or '/arm_B' in m for m in mounts)
        receipt_path=next((root/'runs').glob('*/receipt.json'));receipt=json.loads(receipt_path.read_text())
        if budget<0.00001:
            assert not requests and receipt['status']=='COST_LIMIT'
            return None
        assert (root/'outputs/paid_usage.jsonl').exists()
        assert (receipt_path.parent/'answer.md').read_text()=='retained answer'
        message=requests[0]['messages']
        assert message[1]['content']==question+('\n\n'+rules if arm=='B' else '')
        return message[0]['content']

assert exercise('A')==exercise('B')
exercise('A',budget=0.00000001)
with tempfile.TemporaryDirectory() as directory:
    common=Path(directory)/'common';common.mkdir();outside=Path(directory)/'private';outside.mkdir()
    (common/'outside').symlink_to(outside,target_is_directory=True)
    try:runner.validate_common(common);raise AssertionError('escape admitted')
    except RuntimeError:pass
    (common/'outside').unlink();(common/'nested').mkdir();(common/'nested/hidden').mkdir()
    try:runner.validate_common(common);raise AssertionError('hidden admitted')
    except RuntimeError:pass
print('Actual A/B messages, task-specific mounts, no public-facts dependency, output paths, budget stop and descendant isolation: PASS')
