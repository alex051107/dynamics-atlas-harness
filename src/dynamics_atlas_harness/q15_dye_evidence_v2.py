"""Bounded Q15 dye evidence; every directional relation follows admitted numbers."""
import math


def histogram_direction(source):
    if not source or source.get('role') != 'PUBLISHED_MEASURED_HISTOGRAM_BARS_NOT_FITTED_CURVES':
        return {'direction': 'SOURCE_INSUFFICIENT', 'sentence': '缺少身份明确的实测柱形，不能判断换染料后的方向。'}
    if source.get('variant') != 'HiSiaP175/228' or source.get('dye_pair') != 'TMR/Cy5':
        raise ValueError('HISTOGRAM_PAIR_IDENTITY')
    rows = {}
    for condition in ['apo', 'holo']:
        bars = source.get('bins', {}).get(condition, [])
        frame = source.get('frames', {}).get(condition, [])
        if not bars or len(frame) != 4:
            return {'direction': 'SOURCE_INSUFFICIENT', 'sentence': '缺少配对面板或柱形，不能判断换染料后的方向。'}
        left, right = frame[:2]
        if not all(map(math.isfinite, frame)) or right <= left:
            raise ValueError('INVALID_PANEL')
        edges, masses = [], []
        for bar in bars:
            a, b, h = [bar[k] for k in ['left_pt', 'right_pt', 'height_pt']]
            if not all(map(math.isfinite, [a, b, h])) or b <= a or h < 0:
                raise ValueError('INVALID_BAR')
            edges.append(((a-left)/(right-left), (b-left)/(right-left)))
            masses.append((b-a)*h)
        total = sum(masses)
        if total <= 0:
            raise ValueError('EMPTY_HISTOGRAM_MASS')
        masses = [v/total for v in masses]
        low = sum(a*m for (a, b), m in zip(edges, masses))
        high = sum(b*m for (a, b), m in zip(edges, masses))
        rows[condition] = dict(bars=len(bars), centroid=(low+high)/2,
            lower=low, upper=high, max_bin_width=max(b-a for a, b in edges))
    a, h = rows['apo'], rows['holo']
    registration = a['max_bin_width']+h['max_bin_width']
    low, high = h['lower']-a['upper']-registration, h['upper']-a['lower']+registration
    direction = 'RIGHT' if low > 0 else 'LEFT' if high < 0 else 'GEOMETRIC_DIRECTION_UNRESOLVED'
    description = {'RIGHT': '加配体后向右移动', 'LEFT': '加配体后向左移动',
        'GEOMETRIC_DIRECTION_UNRESOLVED': '在声明的图形扰动范围内方向未定'}[direction]
    return dict(direction=direction, conditions=rows, centroid_shift=h['centroid']-a['centroid'],
        geometric_bounds=[low, high], sentence='代表性已处理 TMR/Cy5 直方图'+description+'。',
        uncertainty='Within-bar position plus one bin registration per panel; not a confidence interval.')


def summarize_dye_evidence(sources, cross_evidence):
    histogram = histogram_direction(sources.get('histogram'))
    pair = next(r for r in cross_evidence['rows'] if r['pair'] == '175_228')
    effect = pair['observed_E_effect']
    if not math.isfinite(effect):
        raise ValueError('NONFINITE_ALEXA_EFFECT')
    hs = {'RIGHT': 1, 'LEFT': -1}.get(histogram['direction'], 0)
    alexa = (1 if effect > 0 else -1 if effect < 0 else 0)
    if not pair['descriptive_direction_retained_in_manual_checks']:
        alexa = 0
    relation = 'UNRESOLVED' if not hs or not alexa else 'OPPOSITE' if hs != alexa else 'SAME'
    deer = pair['DEER_central_mean_change_source_axis_units']
    if not math.isfinite(deer):
        raise ValueError('NONFINITE_DEER_EFFECT')
    expected = -1 if deer > 0 else 1 if deer < 0 else 0
    deer_relation = 'UNRESOLVED' if not hs or not expected else 'COMPATIBLE' if hs == expected else 'TENSION'
    relation_text = {'UNRESOLVED': '与 Alexa 方向的关系未定。', 'OPPOSITE': '与绑定的 Alexa 观测方向相反。', 'SAME': '与绑定的 Alexa 观测方向相同。'}[relation]
    deer_text = {'UNRESOLVED': '与 DEER 的方向关系未定。', 'COMPATIBLE': '在各自读出稳定且采用共同正距离尺度时，与 DEER 方向相容。', 'TENSION': '在各自读出稳定且采用共同正距离尺度时，与 DEER 方向存在张力。'}[deer_relation]
    report = sources['dye_summary']
    if report['status'] != 'SOURCE_LABELLED_DYE_POSITION_OBSERVATIONS':
        raise ValueError('DYE_OBSERVATION_ROLE')
    rows = {}
    for name in ['175_AF555', '58_AF555', '175_TMR']:
        value = report['results'][name]
        conditions = {}
        for condition in ['apo', 'holo']:
            windows = value[condition]['windows']
            if windows['early']['delay_ns'] != [2., 4.] or windows['late']['delay_ns'] != [6., 8.]:
                raise ValueError('DYE_WINDOW_CHANGED')
            early = windows['early']['mean_peak_normalized_intensity']
            late = windows['late']['mean_peak_normalized_intensity']
            aniso = windows['late']['intensity_weighted_anisotropy']
            if not all(map(math.isfinite, [early, late, aniso])) or early <= 0 or late <= 0:
                raise ValueError('INVALID_DYE_SUMMARY')
            conditions[condition] = dict(late_early=late/early, anisotropy=aniso)
        a, h = conditions['apo'], conditions['holo']
        rows[name] = dict(conditions=conditions, decay_shape_ratio=h['late_early']/a['late_early'],
            anisotropy_change=h['anisotropy']-a['anisotropy'])
    af, control, tmr = [rows[k] for k in ['175_AF555', '58_AF555', '175_TMR']]
    contrast = abs(math.log(af['decay_shape_ratio'])) > abs(math.log(control['decay_shape_ratio']))
    replacement = abs(math.log(tmr['decay_shape_ratio'])) < abs(math.log(af['decay_shape_ratio']))
    lower_anisotropy = all(tmr['conditions'][c]['anisotropy'] < af['conditions'][c]['anisotropy'] for c in ['apo', 'holo'])
    probe = ('所选时间窗内，175 位点 Alexa 供体的衰减形状变化大于 58 位点对照；' if contrast else '所选时间窗未显示 175 位点 Alexa 供体比 58 位点对照具有更大的衰减形状变化；')
    probe += ('TMR 供体的衰减形状变化较小。' if replacement else 'TMR 供体没有显示更小的衰减形状变化。')
    probe += ('TMR 在两个条件的晚窗各向异性均较低。' if lower_anisotropy else 'TMR 并非在两个条件的晚窗各向异性均较低。')
    concordance = sources['concordance']
    if concordance['status'] != 'NUMERIC_WORKBOOK_CSV_MATCH_WITH_PDF_CY5_VISUAL_DISCREPANCY':
        raise ValueError('UNREVIEWED_CY5_CONCORDANCE_STATE')
    return dict(histogram=histogram, Alexa_relation=relation, DEER_relation=deer_relation,
        histogram_answer=histogram['sentence']+relation_text+deer_text, dye_numbers=rows,
        probe_answer=probe, probe_readout_condition_dependence=contrast,
        replacement_donor_reduces_observed_concern=replacement and lower_anisotropy,
        Cy5_mechanistic_use='EXCLUDED_PENDING_PDF_SOURCE_CONCORDANCE',
        limits=['Representative processed histogram, not replicate-level uncertainty or original burst-selection validation.',
            'Geometric bounds cover stated graphical perturbations only, not selection/calibration systematics.',
            'Window ratios are not fitted lifetimes, quantum yields, gamma or R0 calibrations.',
            'Lower anisotropy and similar decay shape do not establish complete probe applicability.',
            'Cy5 deposited curves disagree visually with paper panel; no Cy5 mechanism or calibration certification.',
            'Distinct temperatures/probes and directional agreement do not identify a unique protein ensemble or microscopic dye mechanism.'],
        provenance='RULE_APPLICATION_OF_PREVIOUS_MANUAL_NUMERICAL_EVIDENCE', new_numerical_operator_calls=0)
