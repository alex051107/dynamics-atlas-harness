"""Source-compatible APBS fluorescence comparison; no protein-state inference."""
import numpy as np
import zlib


def validate_member_bytes(data, member):
    """Consume the already-admitted ZIP member identity, before any parsing."""
    if len(data) != member['expanded_bytes']:
        raise ValueError('SOURCE_MEMBER_EXPANDED_LENGTH_MISMATCH')
    if f'{zlib.crc32(data) & 0xffffffff:08x}' != member['crc32'].lower():
        raise ValueError('SOURCE_MEMBER_CRC_MISMATCH')

POLICY = {'version':'q15-apbs-reported-method/v1','selection':'APBS source exports; raw total AA+DD+DA at least150',
          'minimum_raw_photons':150,'stoichiometry_open_interval':[.25,.75],
          'background_kHz_DD_DA_AA':[1.33,.83,.77],'alpha':.084,'delta':.065,'gamma':2.17,'beta':.82,
          'Tau_unit':'seconds under matching ALEX Suite export convention','background_exposure':'whole burst Tau*1000 ms; source-compatible, exact paper executable unknown',
          'negative_values_clipped':False,'source':'Peter2022 SI Table3 and Hellenkamp2018 eq14,18-21',
          'unit':'source-labelled repetition; files within repetition are technical segments',
          'calibration_applicability':'CONDITIONAL_SHARED_SYSTEM_LEVEL_VALUES',
          'protein_state_or_distance_claim':False}


def correct(counts, duration_s, policy=POLICY):
    counts=np.asarray(counts,dtype=float);duration=np.asarray(duration_s,dtype=float)
    if counts.ndim!=2 or counts.shape[1]!=3 or duration.shape!=(len(counts),):raise ValueError('COUNT_SHAPE')
    if not np.isfinite(counts).all() or np.any(counts<0) or np.any(counts!=np.floor(counts)) or not np.isfinite(duration).all() or np.any(duration<=0):raise ValueError('RAW_COUNTS_OR_DURATION_INVALID')
    dd,da,aa=(counts-duration[:,None]*1000*np.asarray(policy['background_kHz_DD_DA_AA'])).T
    f=da-policy['alpha']*dd-policy['delta']*aa
    donor_total=policy['gamma']*dd+f;total=donor_total+aa/policy['beta']
    with np.errstate(divide='ignore',invalid='ignore'):
        e=f/donor_total;s=donor_total/total
    length=counts.sum(axis=1);positive=(donor_total>0)&(total>0);finite=np.isfinite(e)&np.isfinite(s)
    eligible=length>=policy['minimum_raw_photons'];lo,hi=policy['stoichiometry_open_interval'];selected=eligible&positive&finite&(s>lo)&(s<hi)
    return {'E':e,'S':s,'selected':selected,'eligible':eligible,'corrected_counts_DD_DA_AA':np.column_stack([dd,da,aa]),
            'positive_totals':positive,'finite_ratios':finite,'raw_length':length}


def summarize(values):
    v=np.asarray(values,dtype=float)
    if len(v)==0:return {'n':0,'mean':None,'std':None,'median':None,'q25':None,'q75':None,'outside_zero_one':0}
    return {'n':len(v),'mean':float(np.mean(v)),'std':float(np.std(v,ddof=1))if len(v)>1 else None,
            'median':float(np.median(v)),'q25':float(np.quantile(v,.25)),'q75':float(np.quantile(v,.75)),
            'minimum':float(np.min(v)),'maximum':float(np.max(v)), 'outside_zero_one':int(np.sum((v<0)|(v>1)))}


def group_difference(repetitions):
    result={}
    for pair in sorted({r['pair']for r in repetitions}):
        groups={cond:[r for r in repetitions if r['pair']==pair and r['condition']==cond]for cond in ['apo','holo']}
        if any(len(v)!=3 or len({r['repetition']for r in v})!=3 for v in groups.values()):raise ValueError('THREE_SOURCE_REPETITIONS_REQUIRED')
        if any(r['E']['mean']is None for v in groups.values()for r in v):raise ValueError('EMPTY_REPETITION')
        means={cond:np.array([r['E']['mean']for r in rows])for cond,rows in groups.items()}
        delta=float(means['holo'].mean()-means['apo'].mean())
        result[pair]={'apo_repetition_means':means['apo'].tolist(),'holo_repetition_means':means['holo'].tolist(),
                      'apo_mean':float(means['apo'].mean()),'holo_mean':float(means['holo'].mean()),
                      'apo_between_repetition_sd':float(means['apo'].std(ddof=1)),
                      'holo_between_repetition_sd':float(means['holo'].std(ddof=1)),
                      'holo_minus_apo_E':delta,'observed_direction':'INCREASE'if delta>0 else'DECREASE'if delta<0 else'NO_CHANGE',
                      'all_cross_repetition_difference_range':[float(means['holo'].min()-means['apo'].max()),float(means['holo'].max()-means['apo'].min())],
                      'uncertainty':'between source-labelled repetitions only; shared calibration and executable uncertainty not divided by burst count',
                      'protein_closure_inferred':False}
    return result
