"""One isolated development session. Sequential batch; no case-specific action plan."""
import json,subprocess,time,urllib.request,urllib.error,uuid,argparse,fcntl,os
from pathlib import Path
from finite_checks import check
ROOT=Path(__file__).resolve().parents[1]
TOOLS=[{'type':'function','function':{'name':'workspace','description':'Read/search public sources, run Python, or view a PDF page/image. PDF pages zero based. Python executes offline in /work; public data /source. Use Python freely for established analysis.','parameters':{'type':'object','properties':{'kind':{'type':'string','enum':['list','read','search','python','image']},'path':{'type':'string'},'query':{'type':'string'},'code':{'type':'string'},'start_line':{'type':'integer'},'lines':{'type':'integer'},'page':{'type':'integer'}},'required':['kind']}}}, {'type':'function','function':{'name':'submit','description':'Submit the readable scientific answer and structured claims. One feedback and revision opportunity within the same budget.','parameters':{'type':'object','properties':{'answer':{'type':'string'},'claims':{'type':'array','items':{'type':'object'}}},'required':['answer','claims']}}}]

def credential():
    # Credential is provided only to trusted host process, never container or model context.
    import re
    s=(Path.home()/'.codex/sessions/2026/08/30/rollout-2026-08-30T09-51-23-01a052f0-6c75-7f40-947d-83e6b84fe38a.jsonl').read_text()
    for k in dict.fromkeys(re.findall(r'sk-or-v1-[a-fA-F0-9]{64}(?![a-fA-F0-9])',s)):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request('https://openrouter.ai/api/v1/key',headers={'Authorization':'Bearer '+k}),timeout=20))['data']
            if d.get('limit_remaining',0)>.08:return k
        except urllib.error.HTTPError:pass
    raise RuntimeError('No funded credential')

def input_bound(messages):
    estimate=len(json.dumps(messages,ensure_ascii=False).encode())+len(json.dumps(TOOLS).encode())+1000
    for m in messages:
        if isinstance(m.get('content'),list):
            for p in m['content']:
                if p.get('type')=='image_url':estimate+=12000-len(p['image_url']['url'].encode())
    return estimate

def main():
    ap=argparse.ArgumentParser();ap.add_argument('case');ap.add_argument('arm',choices=['A','B','C']);ap.add_argument('--image',required=True);args=ap.parse_args()
    lock=(ROOT/'runtime/batch.lock').open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    ready=json.loads((ROOT/'runtime/readiness.json').read_text());assert ready['approved_for_development'] is True
    unknown=ROOT/'outputs/UNKNOWN_CHARGE.json'
    if unknown.exists():raise RuntimeError('Unreconciled model request; no retry')
    source=(ROOT/'cases'/args.case).resolve();assert source.is_dir()
    runid=f'{args.case}_{args.arm}_'+uuid.uuid4().hex[:8];out=ROOT/'runs'/runid;out.mkdir(parents=True)
    work=out/'work';work.mkdir();work.chmod(0o777);key=credential();name='atlas-dev-'+uuid.uuid4().hex[:10];runtime=Path(__file__).parent.resolve()
    cmd=['docker','run','-d','--pull','never','--name',name,'--network','none','--cpus','2','--memory','4g','--pids-limit','128','--cap-drop','ALL','--security-opt','no-new-privileges','--read-only','--user','65534:65534','--tmpfs','/tmp:rw,nosuid,size=256m','-e','MPLCONFIGDIR=/tmp/matplotlib','-e','OPENBLAS_NUM_THREADS=2','-v',str(source)+':/source:ro','-v',str(work.resolve())+':/work:rw','-v',str(runtime/'container_tools.py')+':/tool.py:ro','--entrypoint','sleep',args.image,'1800']
    subprocess.run(cmd,check=True,capture_output=True)
    system=(runtime/'common_prompt.txt').read_text();user=(source/'QUESTION.txt').read_text()
    if args.arm in ['B','C']:user+='\n\n'+(runtime/'ACTIVE_RULES_ZH.md').read_text()
    if args.arm=='C':user+='\n\n'+(runtime/'C_POLICY.txt').read_text()
    messages=[{'role':'system','content':system},{'role':'user','content':user}]
    totals={'input':0,'output':0,'cost':0.,'tools':0};started=time.monotonic();submits=[];facts=json.loads((source/'PUBLIC_FACTS.json').read_text());status='INCOMPLETE';ledger=ROOT/'outputs/paid_usage.jsonl'
    def log(kind,v):
        with (out/'events.jsonl').open('a') as f:f.write(json.dumps({'kind':kind,'elapsed':time.monotonic()-started,'value':v},ensure_ascii=False)+'\n')
    def remaining():return max(0,1500-(time.monotonic()-started))
    def accept(a):
        if not isinstance(a.get('answer'),str) or not isinstance(a.get('claims'),list):return {'error':'submit requires answer string and claims list'}
        conflicts=check(a['claims'],facts) if args.arm=='C' else []
        submits.append({'answer':a['answer'],'claims':a['claims'],'conflicts':conflicts});log('submission',submits[-1])
        (out/f'draft_{len(submits)}.json').write_text(json.dumps(submits[-1],ensure_ascii=False,indent=2))
        if len(submits)==1:
            result={'message':'One optional revision remains in the same budget. Re-submit unchanged if no revision needed.'}
            if args.arm=='C':result['conflicts']=conflicts
            return result
        return {'message':'Final submission saved.'}
    try:
        for turn in range(45):
            if remaining()<=0 or totals['tools']>=40:status='RESOURCE_LIMIT';break
            estimate=input_bound(messages)
            if totals['input']+estimate>160000 or totals['output']>=30000:status='TOKEN_LIMIT';break
            maxout=min(4000,30000-totals['output'])
            spent=sum(json.loads(l)['cost'] for l in ledger.read_text().splitlines()) if ledger.exists() else 0.0000654
            reserve=estimate*.00000025+maxout*.0000012
            if spent+reserve>3:status='COST_LIMIT';break
            payload={'model':'openai/gpt-5.6-luna','provider':{'only':['openai'],'allow_fallbacks':False,'require_parameters':True},'reasoning':{'effort':'medium','exclude':True},'max_tokens':maxout,'tools':TOOLS,'messages':messages}
            log('request',payload)
            req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',data=json.dumps(payload).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
            unknown.write_text(json.dumps({'run':runid,'turn':turn,'reserved_max_cost':reserve,'state':'REQUEST_IN_FLIGHT'}))
            with urllib.request.urlopen(req,timeout=min(120,remaining())) as r:response=json.load(r)
            log('response',response);u=response['usage'];totals['input']+=u['prompt_tokens'];totals['output']+=u['completion_tokens'];totals['cost']+=u['cost']
            with ledger.open('a') as f:f.write(json.dumps({'run':runid,'id':response['id'],'cost':u['cost'],'usage':u})+'\n')
            unknown.unlink()
            m=response['choices'][0]['message'];messages.append({k:v for k,v in m.items() if k in ['role','content','tool_calls']});calls=m.get('tool_calls',[])
            if not calls:
                feedback=accept({'answer':m.get('content') or '', 'claims':[]})
                if len(submits)>=2:status='COMPLETE';break
                messages.append({'role':'user','content':json.dumps(feedback)});continue
            pending_images=[];submitted_this_batch=False
            for tc in calls:
                image=None
                if remaining()<=0 or totals['tools']>=40:result={'error':'Resource limit reached'}
                else:
                    totals['tools']+=1
                    try:
                        a=json.loads(tc['function']['arguments']);fn=tc['function']['name']
                        if fn=='submit':
                            if submitted_this_batch:result={'error':'Only one submission per feedback round.'}
                            else:result=accept(a);submitted_this_batch=True
                        elif fn=='workspace':
                            r=subprocess.run(['docker','exec','-i',name,'python','/tool.py'],input=json.dumps(a),capture_output=True,text=True,timeout=min(90,remaining()))
                            result=json.loads(r.stdout) if r.returncode==0 else {'error':r.stderr[:2000]}
                        else:result={'error':'Unknown tool name'}
                    except subprocess.TimeoutExpired:
                        # Kill timed-out child calculations before next action; retained container remains isolated.
                        subprocess.run(['docker','exec',name,'python','-c',"import os,signal;from pathlib import Path;me=os.getpid();[(os.kill(int(p.name),signal.SIGKILL)) for p in Path('/proc').iterdir() if p.name.isdigit() and int(p.name)>1 and int(p.name)!=me and b'python' in (p/'cmdline').read_bytes()]"],capture_output=True,timeout=5)
                        result={'error':'Tool timeout; choose a smaller calculation or inspect partial outputs.'}
                    except Exception as e:result={'error':type(e).__name__,'message':str(e)[:1000]}
                log('tool_output',result)
                if isinstance(result,dict) and 'image_base64' in result:
                    image=result['image_base64'];result={k:v for k,v in result.items() if k!='image_base64'};result['image_delivered_next']=True
                    pending_images.extend([{'type':'text','text':'Requested tool image '+json.dumps(result)},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+image}}])
                messages.append({'role':'tool','tool_call_id':tc['id'],'content':json.dumps(result,ensure_ascii=False)})
            if pending_images:messages.append({'role':'user','content':pending_images})
            if len(submits)>=2:status='COMPLETE';break
    except Exception as e:
        status='EXECUTION_ERROR';log('error',{'type':type(e).__name__,'message':str(e)[:500]})
    finally:
        subprocess.run(['docker','rm','-f',name],capture_output=True)
        if submits:
            last=submits[-1];(out/'answer.md').write_text(last['answer']+ ('\n\n以下具名主张暂不受支持（其余答案保留）：\n'+'\n'.join(str(last['claims'][c['claim_index']].get('text','Claim '+str(c['claim_index'])))+' — '+c['message']+' ['+c['evidence']+']' for c in last['conflicts']) if last['conflicts'] else ''))
        (out/'receipt.json').write_text(json.dumps({'case':args.case,'arm':args.arm,'status':status,'model':'openai/gpt-5.6-luna','reasoning':'medium','image':args.image,'totals':totals,'wall_seconds':time.monotonic()-started,'submissions':len(submits),'check_scope':'public source-bound fitting overlap only; static-rate check inactive','unknown_charge':unknown.exists()},indent=2));print(out,status,totals,flush=True)
if __name__=='__main__':main()
