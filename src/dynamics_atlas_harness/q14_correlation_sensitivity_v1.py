"""A bounded missing-correlation obligation; no inferred experimental covariance."""
import hashlib
import json
import math
RULE_ID='Q14R01_UNKNOWN_CORRELATION_SENSITIVITY'
OPERATOR_ID='linearized_unknown_correlation_bounds_v1'

def digest(value):
 return hashlib.sha256(json.dumps(value,sort_keys=True,allow_nan=False).encode()).hexdigest()

def sd_bounds(gradient,sd):
 """Sharp bounds over PSD correlations: Gram vectors obey polygon inequalities.

 Each weighted unit Gram vector has length abs(g_i)*sd_i. Their sum norm
 is at most the length sum and at least the largest length minus the rest.
 Collinear vectors attain the upper bound; a closed polygon attains zero
 when possible, otherwise collinear opposition attains the positive minimum.
 """
 if len(gradient)!=len(sd) or not gradient:raise ValueError('MARGINAL_COVERAGE')
 if not all(math.isfinite(x) for x in [*gradient,*sd]) or any(x<0 for x in sd):raise ValueError('INVALID_MARGINALS')
 lengths=[abs(g)*s for g,s in zip(gradient,sd)];high=sum(lengths);low=max(0.,2*max(lengths)-high)
 return dict(delta_sd_bounds=[low,high],delta_variance_bounds=[low*low,high*high],weighted_marginal_lengths=lengths,
  interpretation='Sensitivity over arbitrary PSD correlations with fixed marginal dispersions, not estimated covariance or a confidence interval.')

def source_values(source):
 if source.get('role')!='AUTHOR_SUMMARIZED_INTENSITY_BASED_MEASUREMENTS':raise ValueError('SOURCE_ROLE')
 vals=[];sd=[]
 for pair in ['1','2']:
  for level in ['lo','mid']:
   r=source['samples'][pair+'-'+level];vals.append(r['R_apparent_A']);sd.append(r['R_sd_A'])
 if not all(math.isfinite(x) and x>0 for x in vals) or not all(math.isfinite(x) and x>=0 for x in sd):raise ValueError('INVALID_SOURCE_NUMBERS')
 a,b,c,d=vals
 return vals,sd,[1/b,-a/b**2,-1/d,c/d**2],a/b-c/d

def admitted(source,main,receipt):
 if digest(source)!=receipt['source_digest'] or digest(main)!=receipt['main_digest']:raise ValueError('SOURCE_OR_MAIN_NOT_PREVIOUSLY_ADMITTED')
 vals,sd,g,delta=source_values(source)
 if main['main_inputs']!={'means_A':vals,'published_sd_A':sd} or main['difference_jacobian']!=g or main['cross_pair_difference']!=delta:raise ValueError('MAIN_SOURCE_NUMERICAL_BINDING')
 return sd,g,delta

def operator(source,main,receipt):
 sd,g,delta=admitted(source,main,receipt)
 return dict(operator_id=OPERATOR_ID,input_id=digest(dict(source=source,main=main)),difference=delta,**sd_bounds(g,sd))

def evaluate(source,main,receipt,evidence=None,enabled=True):
 sd,g,delta=admitted(source,main,receipt);identity=digest(dict(source=source,main=main))
 trigger=main['covariance_status']=='UNAVAILABLE_NOT_ASSUMED_ZERO_FOR_CONCLUSION' and sum(g_i*s_i != 0 for g_i,s_i in zip(g,sd)) > 1
 result=dict(rule_id=RULE_ID,rule_instance_id=RULE_ID+'::'+identity,triggered=bool(trigger),
  status='UNRESOLVED',evidence_applications=0,full_question_answer=False,development_adapter=True,
  remaining_obligations=['CORRELATION_SENSITIVITY'] if trigger else [])
 if not enabled or not trigger or evidence is None:return result
 expected=dict(operator_id=OPERATOR_ID,input_id=identity,difference=delta,**sd_bounds(g,sd))
 if evidence!=expected:raise ValueError('EVIDENCE_DIFFERS_FROM_BOUND_SOURCE_CALCULATION')
 result.update(evidence_applications=1,evidence=evidence,partial_claim='UNKNOWN_CORRELATION_CHANGES_PROPAGATED_DISPERSION',
  remaining_obligations=['PAIRED_LAB_DATA_AND_CALIBRATION_COVARIANCE','SAMPLE_SPECIFIC_DYE_AVERAGING_AND_MODEL_APPLICABILITY'],
  answer='The zero-covariance baseline does not establish cross-dye compatibility. The actual published marginals permit the reported range of first-order dispersions; pairing/calibration and dye-model evidence remain necessary.',
  limits=['SD is published measurement dispersion, not uncertainty of a mean or CI.','R0 cancellation requires identical within-pair calibration; sample-specific effects remain.','A broad sensitivity range is not measured disagreement or proof of a common geometry.'])
 return result

def run(source,main,receipt,enabled=True):
 before=evaluate(source,main,receipt,enabled=enabled)
 if not enabled or not before['triggered']:return dict(before=before,after=before,operator_calls=0,evidence=None)
 evidence=operator(source,main,receipt)
 return dict(before=before,after=evaluate(source,main,receipt,evidence),operator_calls=1,evidence=evidence)
