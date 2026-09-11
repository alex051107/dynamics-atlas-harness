"""Frozen four checks: warnings only, no answer editing or scientific adjudication."""
import json,re
NUMBER=re.compile(r'[-+−]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')
CEILING=re.compile(r'占比|population|速率|\brate\b|平衡|收敛|机制',re.I)
CONDITION=re.compile(r'窗口|帧|轨迹|统计单位|n\s*=|\bns\b|\bμs\b|\bus\b|WT|L28R|条件|作者|论文|报告|文献',re.I)
def numbers(text):
 return [float(x.replace('−','-')) for x in NUMBER.findall(text)]
def check(submission,tool_outputs,facts):
 answer=submission['answer']; warnings=[]
 for i,s in enumerate(re.split(r'[。！？!?\n]+',answer),1):
  if CEILING.search(s) and not CONDITION.search(s):warnings.append({'check':'claim_ceiling','location':i,'message':f'第{i}句需要条件或来源'})
 found=numbers(json.dumps(tool_outputs,ensure_ascii=False))
 for i,claim in enumerate(submission.get('claims',[]),1):
  missing=[n for n in numbers(json.dumps(claim,ensure_ascii=False)) if not any(abs(n-v)<=max(abs(n)*.01,1e-9) for v in found)]
  if missing:warnings.append({'check':'numeric_trace','location':i,'message':f'第{i}条数字无工具来源'})
 for field,pattern in [('比较条件',r'WT|L28R|闭合|开放|起始|体系|条件'),('时间窗口',r'\bns\b|μs|微秒|纳秒|frame|帧|窗口'),('统计单位',r'统计单位|每条|轨迹|独立重复|样本|\bn\s*=')]:
  if not re.search(pattern,answer,re.I):warnings.append({'check':'statistical_unit','location':field,'message':f'缺少{field}'})
 for row in facts.get('input_checks',[]):
  if (row.get('max_distance_A',0)>row.get('half_box_lower_bound_A',float('inf'))) or row.get('frames_match') is False or row.get('unit_valid') is False:
   warnings.append({'check':'input_reasonableness','location':row['column'],'message':f"输入第{row['column']}列有物理异常，请检查"})
 return warnings
