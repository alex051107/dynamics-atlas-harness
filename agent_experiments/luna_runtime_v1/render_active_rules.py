"""Render original registry wording and intact target/check obligation pairs."""
import argparse,csv,json
from pathlib import Path

def render(data,registry,method_families=None):
    obligations=data.get('obligations')
    if not isinstance(obligations,list):raise ValueError('obligations must be a list')
    if method_families is None:
        method_families=json.loads(Path(__file__).with_name('paper_method_family.json').read_text())
    case_methods=set(data.get('method_families', []))
    groups={};unmapped=[]
    for o in obligations:
        if not isinstance(o,dict) or not all(k in o for k in ('obligation_id','rule_id','target','required_check')):
            raise ValueError('Malformed obligation')
        if o['rule_id'] not in registry:
            unmapped.append(o);continue
        record={k:o.get(k) for k in ('obligation_id','target','required_check','reason_from_input','claim_scope')}
        line=json.dumps(record,ensure_ascii=False,sort_keys=True)
        group=groups.setdefault(o['rule_id'],[])
        if line not in group:group.append(line)
    text=['以下为分析提醒，可质疑；与资料冲突时以资料为准并说明。']
    for rid,lines in groups.items():
        r=registry[rid]
        paper=r.get('paper_id','UNKNOWN')
        families=method_families.get(paper,{}).get('method_families',[])
        applicable=bool(case_methods.intersection(families)) or r.get('rule_class') in {'claim_ceiling','estimand_non_equivalence','evidence_role_separation'}
        text.extend(['',f"**[{rid}]** 项目归纳的本题检查（不是来源论文的普适条款）"])
        text.extend('- '+line for line in lines)
        text.extend([f"原条款（来源 {paper}；方法家族 {', '.join(families) or 'UNKNOWN'}；transfer_scope：{r.get('transfer_scope','UNKNOWN')}）",r['proposed_project_rule']])
        if applicable:
            text.append(f"必填：{r['required_fields']}　弃权路线：{r['abstain_route']}")
        else:
            text.append(f"原文条件：{r['required_fields']}；原文弃权路线：{r['abstain_route']}")
            text.append('本题适用性未确认：以上条件不作为必填或弃权理由。')
    branch='EMPTY' if not obligations else ('OK' if groups else 'UNMAPPED')
    return '\n'.join(text)+'\n',unmapped,{'selector_branch':branch,'obligations':len(obligations),'mapped_rules':len(groups),'unmapped_obligations':len(unmapped)}

def main():
    p=argparse.ArgumentParser()
    for n in ('obligations','registry','output','unmapped','receipt'):p.add_argument('--'+n,type=Path,required=True)
    a=p.parse_args()
    try:
        with a.registry.open(newline='') as f:registry={r['rule_id']:r for r in csv.DictReader(f)}
        text,unmapped,result=render(json.loads(a.obligations.read_text()),registry)
        a.output.write_text(text);a.unmapped.write_text(json.dumps(unmapped,ensure_ascii=False,indent=2)+'\n')
    except Exception as e:
        result={'selector_branch':'FAILED','error':type(e).__name__,'message':str(e)}
    a.receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':main()
