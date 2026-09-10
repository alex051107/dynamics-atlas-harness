import json,csv,os
from pathlib import Path
from render_active_rules import render

registry={'R':{'proposed_project_rule':'Original scientific wording','required_fields':'field','abstain_route':'unknown'}}
items=[{'obligation_id':'o1','rule_id':'R','target':{'source_ids':['x']},'required_check':'check x','reason_from_input':'x reason','claim_scope':'local'}, {'obligation_id':'o2','rule_id':'R','target':{'source_ids':['y']},'required_check':'check y','reason_from_input':'y reason','claim_scope':'local'}]
text,missing,result=render({'obligations':items},registry)
assert text.count('**[R]**')==1 and result['selector_branch']=='OK'
for item in items:
    line=next(line for line in text.splitlines() if item['obligation_id'] in line)
    decoded=json.loads(line[2:]);assert all(decoded[k]==item[k] for k in ('obligation_id','target','required_check','reason_from_input','claim_scope'))
assert render({'obligations':[]},registry)[2]['selector_branch']=='EMPTY'
assert render({'obligations':[dict(items[0],rule_id='missing')]},registry)[2]['selector_branch']=='UNMAPPED'
if os.environ.get('ATLAS_SELECTOR_PROBE'):
    data=json.loads(Path(os.environ['ATLAS_SELECTOR_PROBE']).read_text())
    with Path(os.environ['ATLAS_RULE_REGISTRY']).open(newline='') as f:registry={r['rule_id']:r for r in csv.DictReader(f)}
    text,missing,result=render(data,registry)
    mapped=[o for o in data['obligations'] if o['rule_id'] in registry]
    assert mapped and text.count('**[')==len({o['rule_id'] for o in mapped})
    for o in mapped:
        block=text.split('**['+o['rule_id']+']**',1)[1].split('\n**[',1)[0]
        parsed=[json.loads(line[2:]) for line in block.splitlines() if line.startswith('- ')]
        assert any(all(record[k]==o.get(k) for k in ('obligation_id','target','required_check','reason_from_input','claim_scope')) for record in parsed)
print('Original rule grouping and intact per-target checks, empty/unmapped branches, optional real selector probe: PASS')
