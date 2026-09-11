"""Narrow deterministic submission checks; flags are audit prompts, not verdicts."""
import json,re
from pathlib import Path

def numbers(text):
 return [float(x)for x in re.findall(r'(?<![A-Za-z_])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',text)]

def check_submission(record,tool_outputs,source):
 flags=[];unverified=[];answer=record['answer'];seen=numbers(json.dumps(tool_outputs,ensure_ascii=False));facts=[]
 p=Path(source)/'PUBLIC_FACTS.json'
 if p.exists():
  f=json.loads(p.read_text());facts=f if isinstance(f,list)else[]
 for i,c in enumerate(record['claims']):
  text=c.get('text','');negative=c.get('polarity')=='negative'or bool(re.search(r'不能|不足|不支持|无法|未证明|not |cannot|unresolved',text,re.I));bound=bool(re.search(r'有限|帧|轨迹|窗口|作者|条件|估计|模型|observ|trajectory|frame|window|author|model|conditional|estimate',text,re.I))
  if not negative and not bound and re.search(r'平衡(?:占比|分布)|转换速率|唯一机制|equilibrium population|transition rate|unique mechanism',text,re.I):flags.append({'check':'claim_ceiling','claim_index':i,'message':'该强结论未带可见适用条件；请核对证据允许的层级。'})
  if c.get('origin')=='current_calculation':
   nums=numbers(str(c.get('quantity','')))
   if nums and any(not any(abs(n-v)<=max(.02,abs(n)*.0001)for v in seen)for n in nums):flags.append({'check':'numeric_trace','claim_index':i,'message':'所声明数值未全部匹配本次可见工具输出；请核对计算或转述。此检查不判定数字真伪。'})
   if not nums:unverified.append({'check':'numeric_trace','claim_index':i,'reason':'No parseable structured quantity; semantic provenance not determined'})
  role=str(c.get('evidence_role',''))
  if not negative and re.search(r'independent.validation|独立验证',role,re.I):
   matched=[f for f in facts if all(c.get(k)and c.get(k)==f.get(k)for k in ['result_id','observation_subset','analysis_id'])]
   if any(f.get('relation')=='used_in_fitting'for f in matched):flags.append({'check':'evidence_role','claim_index':i,'message':'该具名结果/观测/分析组合在公开来源中属于拟合重用，请核对独立验证措辞。'})
   elif not matched:unverified.append({'check':'evidence_role','claim_index':i,'reason':'No exact public relation match; not automatically independent'})
 if any(c.get('origin')=='current_calculation'for c in record['claims']):
  context=answer+' '+json.dumps([c.get('observation_subset','')for c in record['claims']],ensure_ascii=False)
  if not re.search(r'帧|轨迹|窗口|frame|trajectory|window|ns|μs|微秒|样本|construct',context,re.I):flags.append({'check':'unit_window','message':'计算答案未明确统计单位或观察窗口，请核对。'})
 return {'flags':flags,'unverified':unverified,'scope':'Only trace/explicit-language checks; no scientific answer supplied, no correction imposed','message':'请自行核对这些提示；可保留原答案并解释误报。仅一次预算内修订。'}
