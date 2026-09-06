"""Audit deposited inverse P(r) -> deposited fit; never a state-population solver.

Kernel reference: https://jeschkelab.github.io/DeerLab/theory.html
Source roles and tolerance frozen in task_spec iteration68 before execution.
"""
import json
from pathlib import Path
import numpy as np
from scipy import constants, special

TASK = Path(__file__).resolve().parents[1]
D = constants.mu_0 / (4*np.pi) * (constants.physical_constants['Bohr magneton'][0]
    * abs(constants.physical_constants['electron g factor'][0]))**2 / constants.hbar * 1e21
TOL = .005

def kernel(t, r):
    phi = D * np.abs(np.asarray(t))[:, None] / np.asarray(r)[None, :]**3
    xi = np.sqrt(6*phi/np.pi)
    s, c = special.fresnel(xi)
    result = np.ones_like(phi)
    np.divide(c*np.cos(phi) + s*np.sin(phi), xi, out=result, where=xi != 0)
    return result

def main():
    source = json.loads((TASK/'outputs/q16_condition_inventory_v1/source_curves.local.json').read_text())
    unique = {}
    for key, curves in source.items():
        condition = key.split(':')[1]
        if condition in unique:
            assert curves == unique[condition][1], ('nonidentical duplicate', key)
        else:
            unique[condition] = (key, curves)
    assert len(unique) == 10
    # Independent orientation integral at the endpoints and interior phases of source domain.
    tcheck = np.array([0., .032, .32, 1., 3., 7.008])
    rcheck = np.array([1.986303, 3., 5., 9.071432])
    u, w = np.polynomial.legendre.leggauss(1024)
    u, w = (u+1)/2, w/2
    phase = D*tcheck[:, None]/rcheck[None, :]**3
    numerical = np.cos(phase[:, :, None]*(1-3*u*u)) @ w
    error = float(np.max(np.abs(kernel(tcheck, rcheck)-numerical)))
    assert error < 1e-10, error
    assert np.array_equal(kernel([0], rcheck), np.ones((1, len(rcheck))))
    out = TASK/'outputs/q16_forward_method_audit_v1'
    out.mkdir(exist_ok=False)
    rows, predictions = [], {}
    for condition, (key, curves) in unique.items():
        distribution = np.asarray(curves['distribution'], float)
        processed = np.asarray(curves['processed'], float)
        r, density = distribution[:, 0]/10, distribution[:, 1]
        t, target = processed[:, 0], processed[:, 2]
        assert np.isfinite(distribution).all() and np.isfinite(processed).all()
        assert (r > 0).all() and (np.diff(r) > 0).all() and (density >= 0).all()
        widths = np.empty_like(r)
        widths[0], widths[-1] = (r[1]-r[0])/2, (r[-1]-r[-2])/2
        widths[1:-1] = (r[2:]-r[:-2])/2
        mass = density*widths
        mass /= mass.sum()
        formfactor = kernel(t, r) @ mass
        design = np.column_stack([np.ones_like(t), formfactor])
        coeff, _, rank, _ = np.linalg.lstsq(design, target, rcond=None)
        assert rank == 2 and np.ptp(target) > 0
        prediction = design @ coeff
        residual = prediction-target
        relative_rms = float(np.sqrt(np.mean(residual**2))/np.ptp(target))
        rows.append(dict(condition=condition, source_key=key, n_time=len(t), n_distance=len(r),
            t_max_us=float(t[-1]), distance_scale_source_to_nm=.1,
            affine_offset=float(coeff[0]), affine_modulation=float(coeff[1]),
            t_zero_prediction=float(coeff.sum()), relative_rms=relative_rms,
            max_abs_residual=float(np.max(np.abs(residual))),
            compatibility='WITHIN_FROZEN_TOLERANCE' if relative_rms <= TOL else 'METHOD_GAP'))
        predictions[key] = dict(t_us=t.tolist(), reconstructed=prediction.tolist(),
            author_fitted_METHOD_AUDIT_TARGET=target.tolist(), residual=residual.tolist())
    report = dict(status='FORWARD_METHOD_COMPATIBLE' if all(r['relative_rms'] <= TOL for r in rows)
        else 'METHOD_GAP_STOP_INVERSE_ADMISSION', rows=rows, unique_curves=len(rows),
        dipolar_constant_rad_us_nm3=float(D), quadrature_max_abs_error=error,
        frozen_relative_rms_tolerance=TOL, integration='trapezoidal normalized central P(r)',
        source='Peter2022 SourceData Figure5/SI Figure9/SI Figure10',
        source_units='Workbook nm header conflicts with visually verified Figure5 physical8 Angstrom axis; fixed divide10, not fitted.',
        role='AUTHOR_INVERSE_DISTRIBUTION_TO_AUTHOR_FIT_METHOD_AUDIT_ONLY',
        scientific_answer=False, rules_extra_credit=0, iterative_optimizations=0,
        closed_form_affine_fits=10,
        limits=['Not an independent reconstruction of protein states.',
                'Does not establish identical DeerAnalysis2018 discretization or original configuration.',
                'No inverse regularization, truncation recovery, noise model or state population tested.'])
    (out/'report.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    (out/'predictions.local.json').write_text(json.dumps(predictions, allow_nan=False)+'\n')
    text = '# Q16 正向方法核对\n\n'+report['status']+'。本轮以作者存档的距离分布重建作者拟合曲线，只核对计算方法。\n\n'
    text += '| 条件 | 相对 RMS | 判据 |\n|---|---:|---|\n'
    for row in rows:
        text += f"| {row['condition']} | {row['relative_rms']:.8g} | {row['compatibility']} |\n"
    text += '\n预先固定容差为拟合曲线幅度范围的 0.5%。只拟合偏移与调制幅度，距离轴按论文图示 Å 除以 10 转为 nm。独立 1024 点方向积分与解析核最大差为 '+str(error)+'。\n\n'
    text += '此结果不计 Rules 补算成功或科学问题完成；作者逆解及拟合曲线仅用于方法核对，不能作为随后科学主计算的目标答案。原软件配置、离散化及截短后的可辨识性仍需区分。\n'
    (out/'REPORT_ZH.md').write_text(text)
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
