import tempfile,json,sys,subprocess,io
from pathlib import Path
from unittest.mock import patch
import agent_run as a

def tc(i,name,args):return {'id':i,'type':'function','function':{'name':name,'arguments':json.dumps(args)}}
def response(msg,i):return {'id':'mock'+str(i),'choices':[{'message':{'role':'assistant',**msg}}],'usage':{'prompt_tokens':100,'completion_tokens':20,'cost':.0001}}
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp);(root/'runtime').mkdir();(root/'outputs').mkdir();s=root/'cases/test/common';s.mkdir(parents=True)
 (root/'runtime/readiness.json').write_text('{"approved_for_development":true}')
 (s/'QUESTION.txt').write_text('test');(root/'runtime/campaign.json').write_text(json.dumps({'task_roots':['.'],'absolute_deadline':'2999-01-01T00:00:00+00:00','round_deadline':'2999-01-01T00:00:00+00:00','model_cost_cap_usd':0.60}))
 rs=[response({'content':None,'tool_calls':[tc('i','workspace',{'kind':'image'}),tc('r','workspace',{'kind':'read'})]},0),response({'content':None,'tool_calls':[tc('s','submit',{'answer':'draft','claims':[{'text':'fixture claim'}]}),tc('d','submit',{'answer':'duplicate','claims':[{'text':'fixture claim'}]})]},1),response({'content':None,'tool_calls':[tc('f','submit',{'answer':'final','claims':[{'text':'fixture claim'}]})]},2)]
 requests=[]
 def network(req,**kw):
  requests.append(json.loads(req.data));return io.BytesIO(json.dumps(rs.pop(0)).encode())
 def run(cmd,**kw):
  if cmd[:2]==['docker','exec']:
   arg=json.loads(kw['input']);data={'image_base64':'AAAA','mime':'image/png'} if arg['kind']=='image' else {'text':'ok'}
   return subprocess.CompletedProcess(cmd,0,json.dumps(data),'')
  return subprocess.CompletedProcess(cmd,0,'container','')
 with patch.object(a,'balance_precheck',return_value=4),patch.object(a,'credential',return_value='dummy'),patch.object(sys,'argv',['agent_run','test','A','--image','mock','--task-root',str(root),'--budget-usd','0.15']),patch.object(a.urllib.request,'urlopen',side_effect=network),patch.object(a.subprocess,'run',side_effect=run):a.main()
 roles=[m['role'] for m in requests[1]['messages']];assert roles[-4:]==['assistant','tool','tool','user'],roles
 receipts=list((root/'runs').glob('*/receipt.json'));r=json.loads(receipts[0].read_text());assert r['submissions']==2 and r['status']=='COMPLETE'
 assert (receipts[0].parent/'answer.md').read_text()=='final'
 assert json.loads((receipts[0].parent/'draft_1.json').read_text())['answer']=='draft'
 assert not (root/'outputs/UNKNOWN_CHARGE.json').exists()
 print('Offline actual runner: image ordering, feedback round, duplicate submit, draft retention, ledger PASS')
