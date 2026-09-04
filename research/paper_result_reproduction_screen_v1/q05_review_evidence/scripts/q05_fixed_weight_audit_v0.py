"""Bounded method audit: exact source functions, fixed weights, no optimization.

AST extraction avoids executing imports for unavailable optional dependencies and
the prior local optimizer. This is a function comparison, not a full BME run.
"""
from pathlib import Path
from types import SimpleNamespace
import ast
import csv
import datetime
import json
import shutil
import sys
import numpy as np
import pandas as pd
from scipy.special import logsumexp

ROOT = Path(__file__).resolve().parents[1]
INP = ROOT / 'inputs/q05_author'
OUT = ROOT / 'outputs/q05_fixed_weight_audit_v0'
OUT.mkdir(parents=True, exist_ok=True)
RTOL, ATOL = 1e-10, 1e-12
THETA = 6.0  # Previously fixed comparison parameter; no inference about author config.
checks = []


def compare(name, local, author):
    a, b = np.asarray(local), np.asarray(author)
    passed = a.shape == b.shape and bool(np.allclose(a, b, rtol=RTOL, atol=ATOL))
    checks.append({'name': name, 'passed': passed, 'shape': list(a.shape),
                   'max_abs_difference': float(np.max(np.abs(a - b))) if a.shape == b.shape else None})
    return passed


sources = {
    'local': ROOT / 'scripts/q05_numeric_v0.py',
    'tools': INP / 'bme_source/BME_tools.py',
    'bme': INP / 'bme_source/BME.py',
}
for key, path in sources.items():
    shutil.copyfile(path, OUT / (key + '_source.py'))
trees = {k: ast.parse(p.read_text()) for k, p in sources.items()}
local_nodes = [node for node in trees['local'].body if 19 <= node.lineno and node.end_lineno <= 57]
local_nodes += [node for node in trees['local'].body if isinstance(node, ast.FunctionDef) and node.name == 'metrics']
local = {'np': np, 'INP': INP, 'THETA': THETA, 'logsumexp': logsumexp}
exec(compile(ast.Module(body=local_nodes, type_ignores=[]), str(sources['local']), 'exec'), local)
author_nodes = [node for node in trees['tools'].body if
                (isinstance(node, ast.FunctionDef) and node.name in {'parse', 'calc_chi', 'standardize', 'srel'}) or
                (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in
                 {'exp_types', 'bound_types', 'averaging_types'} for t in node.targets))]
author = {'np': np, 'pd': pd}
exec(compile(ast.Module(body=author_nodes, type_ignores=[]), str(sources['tools']), 'exec'), author)

# A reversible three-column format adapter, not a Rules/operator adapter.
experiments, matrices, parse_logs = [], [], []
groups = [('saxs', 'simulation_SAXS.dat'), ('amide', 'simulation_HN2_NOE.dat'), ('methyl', 'simulation_methyl_NOE.dat')]
for key, filename in groups:
    if key == 'saxs':
        rows = [(f'q={q:.17g}', v, e) for q, v, e in local['obs']]
        header, averaging = '# DATA=SAXS', 'linear'
    else:
        labels, values, errors = local['noes'][key]
        rows = list(zip(labels, values, errors))
        header, averaging = '# DATA=NOE BOUND=UPPER', 'power_3'
    exp_path = OUT / (key + '_experiment_adapter.dat')
    exp_path.write_text(header + '\n' + ''.join(f'{lab} {v:.17e} {e:.17e}\n' for lab, v, e in rows))
    _, exp, calc, log, _ = author['parse'](str(exp_path), str(local['p'] / filename), averaging=averaging)
    experiments.append(exp)
    matrices.append(calc)
    parse_logs.append(log)
exp = np.vstack(experiments)
calc = np.hstack(matrices)
expected_bound = np.r_[np.zeros(90), -np.ones(332)]
compare('transformed_experimental_values', local['b'], exp[:, 0])
compare('propagated_standard_deviations', local['sig'], exp[:, 1])
compare('transformed_prediction_matrix', local['A'], calc)
compare('bound_direction', expected_bound, exp[:, 2])
author_lambda_bounds = [(None, 0.0) if bound == -1 else ((0.0, None) if bound == 1 else (None, None)) for bound in exp[:, 2]]
checks.append({'name': 'dual_lambda_bounds', 'passed': local['bounds'] == author_lambda_bounds})
(OUT / 'author_parse_log.txt').write_text('\n'.join(parse_logs))

n, m = calc.shape
w0 = np.ones(n) / n
w_linear = np.arange(1, n + 1, dtype=float)
w_linear /= w_linear.sum()
np.savetxt(OUT / 'fixed_weights.tsv', np.column_stack([local['ids'], w0, w_linear]), delimiter='\t',
           header='frame_id\tuniform\tlinear_index', comments='')
weight_results = {}
for name, w in [('uniform', w0), ('linear_index', w_linear)]:
    lp = w @ local['A']
    ap = np.sum(calc * w[:, None], axis=0)
    ld, ad = lp - local['b'], ap - exp[:, 0]
    lm = (expected_bound == 0) | ((expected_bound < 0) & (ld < 0))
    am = (exp[:, 2] == 0) | ((exp[:, 2] < 0) & (ad < 0)) | ((exp[:, 2] > 0) & (ad > 0))
    lr, ar = np.where(lm, ld / local['sig'], 0), np.where(am, ad / exp[:, 1], 0)
    compare(name + ':predictions', lp, ap)
    compare(name + ':raw_residuals', ld, ad)
    compare(name + ':active_bound_masks', lm.astype(int), am.astype(int))
    compare(name + ':normalized_one_sided_residuals', lr, ar)
    ldata = 0.5 * float(np.sum(lr ** 2))
    adata = 0.5 * m * float(author['calc_chi'](exp, calc, w))
    lkl = float(np.sum(w * np.log(w / w0)))
    akl = float(author['srel'](w0, w))
    compare(name + ':half_sum_data_term', ldata, adata)
    compare(name + ':relative_entropy', lkl, akl)
    compare(name + ':half_sum_plus_theta_KL', ldata + THETA * lkl, adata + THETA * akl)
    with (OUT / (name + '_per_observable.tsv')).open('w') as handle:
        writer = csv.writer(handle, delimiter='\t')
        writer.writerow(['label', 'local_target', 'author_target', 'local_sigma', 'author_sigma', 'local_bound', 'author_bound',
                         'local_prediction', 'author_prediction', 'local_raw_residual', 'author_raw_residual',
                         'local_active', 'author_active', 'local_normalized_residual', 'author_normalized_residual'])
        writer.writerows(zip(local['labels'], local['b'], exp[:, 0], local['sig'], exp[:, 1], expected_bound, exp[:, 2],
                             lp, ap, ld, ad, lm, am, lr, ar))
    contributions = {}
    for key, start, end in [('saxs', 0, 90), ('amide', 90, 382), ('methyl', 382, 422)]:
        contributions[key] = {'count': end - start, 'half_sum': float(np.sum(lr[start:end] ** 2) / 2),
                              'mean_squared_residual': float(np.mean(lr[start:end] ** 2))}
    weight_results[name] = {'local_half_sum_data': ldata, 'author_half_sum_data': adata,
                            'theta_KL': THETA * lkl, 'joint_primal_diagnostic': ldata + THETA * lkl,
                            'dataset_contributions': contributions, 'local_distance_domain_display_metrics': local['metrics'](w)}

std_exp, std_calc = exp.copy(), calc.copy()
_, center, scale = author['standardize'](std_exp, std_calc, w0)
for name, a, b in [('center', local['center'], center), ('scale', local['scale'], scale),
                   ('standardized_target', local['y'], std_exp[:, 0]), ('standardized_sigma', local['s'], std_exp[:, 1]),
                   ('standardized_predictions', local['X'], std_calc)]:
    compare(name, a, b)
maxent_node = next(node for node in ast.walk(trees['bme']) if isinstance(node, ast.FunctionDef) and node.name == 'maxent')
tmax = np.log(sys.float_info.max / 5)
dual = {'np': np, 'logsumexp': logsumexp, 'self': SimpleNamespace(calculated=std_calc, experiment=std_exp, w0=w0),
        'tmax': tmax, 'theta': THETA, 'theta_sigma2': THETA * std_exp[:, 1] ** 2}
exec(compile(ast.Module(body=[maxent_node], type_ignores=[]), str(sources['bme']), 'exec'), dual)
probe = 1e-4 * np.sin(np.arange(1, m + 1))
probe[90:] = -np.abs(probe[90:])
dual_results = {}
for name, lam in [('zero', np.zeros(m)), ('fixed_small', probe)]:
    lf, lg = local['fun'](lam)
    af, ag = dual['maxent'](lam)
    compare(name + ':dual_objective_after_constant_offset', lf, af + tmax / THETA)
    compare(name + ':dual_gradient', lg, ag)
    dual_results[name] = {'local_objective': float(lf), 'author_raw_objective': float(af),
                          'author_objective_plus_tmax_over_theta': float(af + tmax / THETA)}
np.savetxt(OUT / 'fixed_lambda_probe.tsv', np.column_stack([np.arange(m), np.zeros(m), probe]), delimiter='\t',
           header='observable_index\tzero\tfixed_small', comments='')
result = {'status': 'METHOD_FUNCTIONS_MATCH' if all(c['passed'] for c in checks) else 'METHOD_GAP_OBSERVED',
          'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'rtol': RTOL, 'atol': ATOL,
          'data_commit': '85979b1b4123b6b5391b617d16551969eda9f56e', 'BME_commit': '314d3b5bb8cd400c1a9eee984acdb903a03c3da4',
          'harness_commit': '738160824a83054d3011695ba1865b12351294ac',
          'runtime': {'executable': sys.executable, 'numpy': np.__version__, 'pandas': pd.__version__},
          'extraction': {k: [{'node': getattr(node, 'name', type(node).__name__), 'start': node.lineno, 'end': node.end_lineno}
                             for node in nodes] for k, nodes in [('local', local_nodes), ('tools', author_nodes), ('bme', [maxent_node])]},
          'checks': checks, 'fixed_weights': weight_results, 'fixed_dual_probes': dual_results,
          'configuration': {'theta': THETA, 'dataset_weights': 'all ones', 'NOE_power': 3,
                            'normalization': 'half sum over 422 observations; calc_chi mean multiplied by 422/2',
                            'dual_constant_removed': float(tmax / THETA), 'original_paper_configuration': 'DATA_INSUFFICIENT'},
          'claim_ceiling': 'Agreement of extracted pinned functions under specified configuration only; no optimizer/full-package run, original-paper reproduction or Rules success.',
          'metric_distinction': 'Local reporting metrics use distance-domain upper-bound residuals; the fitted dual uses propagated r^-3 intensity errors. These diagnostic values are not interchangeable.',
          'optimization_runs': 0}
(OUT / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'checks': len(checks), 'failed': [c for c in checks if not c['passed']],
                  'fixed_weights': weight_results, 'fixed_dual_probes': dual_results}, indent=2))
