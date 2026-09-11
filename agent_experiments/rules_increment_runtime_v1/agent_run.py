"""Task-scoped autonomous Luna runner.

Four HSP90 v3.4 A/B sessions completed at commit 430c13e.
The original campaign is closed to automatic expansion; see the round report.
This post-run documentation update does not change executed logic.
"""
import json,subprocess,time,urllib.request,urllib.error,uuid,argparse,fcntl,os
from pathlib import Path
TOOLS=[{'type':'function','function':{'name':'workspace','description':'Read/search public sources, run Python, or view a PDF page/image. PDF pages zero based. Python executes offline in /work; public data /source. Use Python freely for established analysis.','parameters':{'type':'object','properties':{'kind':{'type':'string','enum':['list','read','search','python','image']},'path':{'type':'string'},'query':{'type':'string'},'code':{'type':'string'},'start_line':{'type':'integer'},'lines':{'type':'integer'},'page':{'type':'integer'}},'required':['kind']}}}, {'type':'function','function':{'name':'submit','description':'Submit the readable scientific answer and structured claims. One feedback and revision opportunity within the same budget.','parameters':{'type':'object','properties':{'answer':{'type':'string'},'claims':{'type':'array','items':{'type':'object'}}},'required':['answer','claims']}}}]

def credential():
    key=os.environ.get('OPENROUTER_API_KEY')
    if not key:raise RuntimeError('OPENROUTER_API_KEY must be set in the process environment')
    return key

def balance_precheck(key):
    request=urllib.request.Request('https://openrouter.ai/api/v1/key',headers={'Authorization':'Bearer '+key})
    data=json.load(urllib.request.urlopen(request,timeout=20))['data']
    remaining=data.get('limit_remaining')
    if remaining is None:
        request=urllib.request.Request('https://openrouter.ai/api/v1/credits',headers={'Authorization':'Bearer '+key})
        data=json.load(urllib.request.urlopen(request,timeout=20))['data']
        remaining=data['total_credits']-data['total_usage']
    if remaining<=0:raise RuntimeError('No funded OpenRouter balance')
    return float(remaining)

def validate_common(source):
    forbidden=('ACTIVE_RULES','grading_rubric','reference_values','literature_claims','rule_coverage','metadata_profile')
    source=source.resolve()
    if not source.is_dir():raise RuntimeError('Missing task common directory')
    for path in source.rglob('*'):
        resolved=path.resolve()
        if not resolved.is_relative_to(source):raise RuntimeError('Common source link escapes its task directory')
        if any(part in ('hidden','arm_B') for part in path.relative_to(source).parts) or any(part in ('hidden','arm_B') for part in resolved.relative_to(source).parts):raise RuntimeError('Hidden treatment directory in common sources')
        if path.name.startswith(forbidden) or resolved.name.startswith(forbidden):raise RuntimeError('Hidden evaluation or rule file in common sources')
    return source

def campaign_usage(root):
    import datetime
    spec=json.loads((root/'runtime/campaign.json').read_text())
    if datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['absolute_deadline']):raise RuntimeError('Campaign absolute deadline reached')
    if datetime.datetime.now(datetime.timezone.utc)>datetime.datetime.fromisoformat(spec['round_deadline']):raise RuntimeError('Round absolute deadline reached')
    spent=0.
    for location in spec['task_roots']:
        task=(root/location).resolve()
        if (task/'outputs/UNKNOWN_CHARGE.json').exists():raise RuntimeError('Unreconciled charge in campaign; all runs stopped')
        ledger=task/'outputs/paid_usage.jsonl'
        if ledger.exists():spent+=sum(json.loads(line)['cost'] for line in ledger.read_text().splitlines())
    return spent,float(spec['model_cost_cap_usd'])

def input_bound(messages):
    estimate=len(json.dumps(messages,ensure_ascii=False).encode())+len(json.dumps(TOOLS).encode())+1000
    for m in messages:
        if isinstance(m.get('content'),list):
            for p in m['content']:
                if p.get('type')=='image_url':estimate+=12000-len(p['image_url']['url'].encode())
    return estimate

def submission_error(a):
    """Validate delivery structure only; never rank scientific answer quality."""
    if not isinstance(a,dict) or not isinstance(a.get('answer'),str) or not a['answer'].strip():
        return 'submit requires a nonempty answer string'
    claims=a.get('claims')
    if not isinstance(claims,list) or not claims or any(not isinstance(c,dict) or not isinstance(c.get('text'),str) or not c['text'].strip() for c in claims):
        return 'submit requires at least one claim record with nonempty text; unknown scientific fields may remain empty'
    return None

def fitting_check_scope(claims,facts):
    """Report only structured matching coverage, never whole-answer acceptance."""
    targets=[c for c in claims if c.get('type')=='conclusion' and c.get('polarity')=='affirmative' and c.get('evidence_role')=='independent_validation']
    matched=sum(any(f.get('relation')=='used_in_fitting' and all(c.get(k) and c.get(k)==f.get(k) for k in ('result_id','observation_subset','analysis_id')) for f in facts) for c in targets)
    return {'scope':'source-indexed fitting overlap only','structured_targets':len(targets),'matched_fitting_relations':matched,'unverified_targets':len(targets)-matched,'status':'matched_fitting_conflict' if matched else ('no_matching_public_relation' if targets else 'no_applicable_structured_claim'),'whole_answer_scientifically_validated':False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('case');ap.add_argument('arm',choices=['A','B','C']);ap.add_argument('--image',required=True);ap.add_argument('--task-root',type=Path,required=True);ap.add_argument('--budget-usd',type=float,required=True);args=ap.parse_args()
    ROOT=args.task_root.resolve()
    if not 0<args.budget_usd<=0.80:raise RuntimeError('Round budget must be positive and at most 0.80 USD')
    campaign_usage(ROOT)
    lock=(ROOT/'runtime/batch.lock').open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    ready=json.loads((ROOT/'runtime/readiness.json').read_text());assert ready['approved_for_development'] is True
    unknown=ROOT/'outputs/UNKNOWN_CHARGE.json'
    if unknown.exists():raise RuntimeError('Unreconciled model request; no retry')
    case_root=(ROOT/'cases'/args.case).resolve();assert case_root.is_relative_to((ROOT/'cases').resolve())
    source=validate_common(case_root/'common')
    runid=f'{args.case}_{args.arm}_'+uuid.uuid4().hex[:8];out=ROOT/'runs'/runid;out.mkdir(parents=True)
    work=out/'work';work.mkdir();work.chmod(0o777);key=credential();available_balance=balance_precheck(key);name='atlas-dev-'+uuid.uuid4().hex[:10];runtime=Path(__file__).parent.resolve()
    cmd=['docker','run','-d','--pull','never','--name',name,'--network','none','--cpus','2','--memory','4g','--pids-limit','128','--cap-drop','ALL','--security-opt','no-new-privileges','--read-only','--user','65534:65534','--tmpfs','/tmp:rw,nosuid,size=256m','-e','MPLCONFIGDIR=/tmp/matplotlib','-e','OPENBLAS_NUM_THREADS=2','-v',str(source)+':/source:ro','-v',str(work.resolve())+':/work:rw','-v',str(runtime/'container_tools.py')+':/tool.py:ro','--entrypoint','sleep',args.image,'1800']
    subprocess.run(cmd,check=True,capture_output=True)
    system=(runtime/'common_prompt.txt').read_text();user=(source/'QUESTION.txt').read_text()
    if args.arm in ['B','C']:user+='\n\n'+(case_root/'arm_B/ACTIVE_RULES.md').read_text()
    if args.arm=='C':user+='\n\n'+(runtime/'C_POLICY.txt').read_text()
    messages=[{'role':'system','content':system},{'role':'user','content':user}]
    totals={'input':0,'output':0,'cost':0.,'tools':0};started=time.monotonic();submits=[];facts={};tool_outputs=[];status='INCOMPLETE';ledger=ROOT/'outputs/paid_usage.jsonl';previous_prompt_tokens=None;previous_message_count=0
    if args.arm=='C':
        from harness_checks import check
        facts=json.loads((source/'INPUT_CHECK_FACTS.json').read_text())
    def log(kind,v):
        with (out/'events.jsonl').open('a') as f:f.write(json.dumps({'kind':kind,'elapsed':time.monotonic()-started,'value':v},ensure_ascii=False)+'\n')
    def remaining():return max(0,1500-(time.monotonic()-started))
    def accept(a):
        error=submission_error(a)
        if error:
            rejected={'error':error,'previous_submission_preserved':bool(submits),'check_status':'not_checked_invalid_submission'}
            log('submission_rejected',rejected)
            return rejected
        conflicts=check(a,tool_outputs,facts) if args.arm=='C' and not submits else []
        record={'answer':a['answer'],'claims':a['claims'],'conflicts':conflicts}
        if args.arm=='C':record['check_scope']={'scope':'four frozen warning checks; not scientific grading','whole_answer_scientifically_validated':False}
        submits.append(record);log('submission',submits[-1])
        (out/f'draft_{len(submits)}.json').write_text(json.dumps(submits[-1],ensure_ascii=False,indent=2))
        if len(submits)==1:
            result={'message':'One optional revision remains in the same budget. Re-submit unchanged if no revision needed.'}
            if args.arm=='C':result.update(conflicts=conflicts,check_scope=record['check_scope'])
            return result
        return {'message':'Final submission saved.'}
    try:
        for turn in range(45):
            if remaining()<=0 or totals['tools']>=40:status='RESOURCE_LIMIT';break
            estimate=input_bound(messages) if previous_prompt_tokens is None else previous_prompt_tokens+input_bound(messages[previous_message_count:])
            closing=(160000-totals['input'] < 2*estimate+10000 or 30000-totals['output']<9000 or totals['tools']>=34 or remaining()<180)
            if closing:
                messages.append({'role':'user','content':'Runtime budget notice: please submit your current evidence-based answer now, preserving unresolved parts. No further source or computation calls remain in this closing phase. Your one revision opportunity remains within the same total budget.'})
                estimate += 1000
            if totals['input']+estimate>160000 or totals['output']>=30000:status='TOKEN_LIMIT';break
            maxout=min(4000,30000-totals['output'])
            spent=sum(json.loads(l)['cost'] for l in ledger.read_text().splitlines()) if ledger.exists() else 0.
            reserve=estimate*.00000025+maxout*.0000012
            global_spent,global_cap=campaign_usage(ROOT)
            if spent+reserve>args.budget_usd or global_spent+reserve>global_cap or totals['cost']+reserve>available_balance:status='COST_LIMIT';break
            payload={'model':'openai/gpt-5.6-luna','provider':{'only':['openai'],'allow_fallbacks':False,'require_parameters':True},'reasoning':{'effort':'medium','exclude':True},'max_tokens':maxout,'tools':TOOLS,'messages':messages}
            if closing:payload['tool_choice']={'type':'function','function':{'name':'submit'}}
            log('budget',{'input_used':totals['input'],'next_input_upper_estimate':estimate,'closing':closing})
            log('request',payload)
            req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',data=json.dumps(payload).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
            unknown.write_text(json.dumps({'run':runid,'turn':turn,'reserved_max_cost':reserve,'state':'REQUEST_IN_FLIGHT'}))
            with urllib.request.urlopen(req,timeout=min(120,remaining())) as r:response=json.load(r)
            log('response',response);u=response['usage'];totals['input']+=u['prompt_tokens'];totals['output']+=u['completion_tokens'];totals['cost']+=u['cost']
            with ledger.open('a') as f:f.write(json.dumps({'run':runid,'id':response['id'],'cost':u['cost'],'usage':u})+'\n')
            unknown.unlink()
            previous_prompt_tokens=u['prompt_tokens'];previous_message_count=len(messages)
            m=response['choices'][0]['message'];messages.append({k:v for k,v in m.items() if k in ['role','content','tool_calls']});calls=m.get('tool_calls',[])
            if not calls:
                log('unsubmitted_message',{'content':m.get('content') or '', 'previous_submission_preserved':bool(submits)})
                if submits:status='SUBMITTED_NO_EXPLICIT_REVISION';break
                messages.append({'role':'user','content':'No answer has been submitted. Use the submit tool with a nonempty answer and claim records; ordinary conversation text is not a submission.'});continue
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
                        elif fn=='workspace' and closing:
                            result={'error':'Closing phase; submit available findings without more computation.'}
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
                if fn=='workspace':tool_outputs.append(result)
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
            last=submits[-1];(out/'answer.md').write_text(last['answer'])
        (out/'receipt.json').write_text(json.dumps({'answer_sha256':__import__('hashlib').sha256((out/'answer.md').read_bytes()).hexdigest() if (out/'answer.md').exists() else None,'started_at_utc':__import__('datetime').datetime.fromtimestamp(__import__('time').time()-(time.monotonic()-started),__import__('datetime').timezone.utc).isoformat(),'case':args.case,'arm':args.arm,'development_revision':None,'runner_stage':'one_shot_four_warning_checks_v1','status':status,'model':'openai/gpt-5.6-luna','reasoning':'medium','image':args.image,'totals':totals,'wall_seconds':time.monotonic()-started,'submissions':len(submits),'check_scope':('four warnings only; no answer modification' if args.arm=='C' else 'no deterministic scientific checks'),'unknown_charge':unknown.exists()},indent=2));print(out,status,totals,flush=True)
if __name__=='__main__':main()
