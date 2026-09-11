"""Narrow checks of explicit public relations, never free-text keyword judging."""
def check(claims, facts):
    conflicts=[]
    for i,c in enumerate(claims):
        if c.get('type')!='conclusion' or c.get('polarity')!='affirmative':
            continue
        # Provenance (author/new) is distinct from validation role.
        if c.get('evidence_role')=='independent_validation':
            for f in facts:
                if (f.get('relation')=='used_in_fitting'
                    and all(c.get(k) and c.get(k)==f.get(k) for k in ('result_id','observation_subset','analysis_id'))):
                    conflicts.append(dict(claim_index=i,check='fitting_overlap',evidence=f['locator'],message='The listed observations participated in fitting this same result. Please reconcile the independent-validation claim.'))
        if c.get('origin')=='current_calculation' and c.get('quantity')=='transition_rate':
            for f in facts:
                if (f.get('relation')=='exclusive_analysis_basis' and f.get('basis')=='unordered_static_only'
                    and f.get('extra_dynamics_model') is False and f.get('time_calibration') is False
                    and f.get('rate_observation') is False
                    and all(c.get(k) and c.get(k)==f.get(k) for k in ('result_id','analysis_id'))):
                    conflicts.append(dict(claim_index=i,check='static_rate',evidence=f['locator'],message='The recorded basis contains only unordered static conformations. Check whether additional dynamical evidence supports this new rate estimate.'))
    return conflicts

if __name__=='__main__':
    c=dict(type='conclusion',polarity='affirmative',origin='current_calculation',quantity='transition_rate',result_id='r',observation_subset='o',analysis_id='a',evidence_role='independent_validation')
    f=dict(relation='used_in_fitting',result_id='r',observation_subset='o',analysis_id='a',locator='public:1')
    assert len(check([c],[f]))==1
    assert not check([dict(c,observation_subset='other')],[f])
    assert not check([dict(c,type='limitation')],[f])
    assert not check([c],[])
    g=dict(relation='exclusive_analysis_basis',basis='unordered_static_only',extra_dynamics_model=False,time_calibration=False,rate_observation=False,result_id='r',analysis_id='a',locator='public:2')
    assert len(check([c],[g]))==1
    assert not check([dict(c,origin='author_report')],[g])
    assert not check([c],[dict(g,extra_dynamics_model=True)])
    assert not check([c],[dict(g,time_calibration=None)])
    assert len(check([c,dict(c,type='limitation')],[f,g]))==2
    print('Finite check explicit conflict / allowed / unknown / per-claim preservation: PASS')
