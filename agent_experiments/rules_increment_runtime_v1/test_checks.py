import copy
from harness_checks import check
s={'answer':'WT条件下，每条轨迹窗口11–1000ns，不将其当独立重复。','claims':[{'text':'均值4.62 Å'}]};before=copy.deepcopy(s)
assert check(s,[{'stdout':'mean4.62'}],{'input_checks':[]})==[]
assert check(s,[],{'input_checks':[]})[0]['check']=='numeric_trace'
assert any(x['check']=='claim_ceiling' for x in check({'answer':'已经证明机制。','claims':[]},[],{}))
assert any(x['check']=='input_reasonableness' for x in check(s,[],{'input_checks':[{'column':'a','max_distance_A':90,'half_box_lower_bound_A':30}]}))
assert s==before
# Warnings never mutate answer, and valid values at the exact bound do not flag.
assert not any(x['check']=='input_reasonableness' for x in check(s,[],{'input_checks':[{'column':'a','max_distance_A':30,'half_box_lower_bound_A':30}]}))
print('Four check categories + no-mutation boundary PASS')
