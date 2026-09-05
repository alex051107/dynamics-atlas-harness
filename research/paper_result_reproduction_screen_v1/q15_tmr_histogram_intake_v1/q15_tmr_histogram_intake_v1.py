"""Extract measured gray bar rectangles only, from the original PDF Figure4d.

Run pdftocairo -f 7 -l 7 -svg ORIGINAL.pdf /tmp/q15_figure4.svg first.
Smooth curves, printed fitted values and all other figure panels are excluded.
"""
from pathlib import Path
import json, re, shutil, xml.etree.ElementTree as ET

TASK = Path(__file__).resolve().parents[1]
GRAY = 'rgb(66.665649%, 66.665649%, 66.665649%)'

def main():
    out = TASK/'outputs/q15_tmr_histogram_intake_v1'
    out.mkdir(exist_ok=False)
    root = ET.parse('/tmp/q15_figure4.svg').getroot()
    parents = {child: parent for parent in root.iter() for child in parent}
    bins = {'apo': [], 'holo': []}
    # Frame corners read from closed stroked SVG paths, independently of bars/fits.
    frames = {'apo': [435.507836713295, 535.5117189965033, 293.22657487404496, 348.2265623731084],
              'holo': [435.43361721658005, 535.4335937830069, 348.42970001365995, 403.429687467778]}
    for index, path in enumerate(root.iter('{http://www.w3.org/2000/svg}path')):
        d = path.get('d', '')
        if path.get('fill') != GRAY or re.findall('[A-Za-z]', d) != ['M', 'L', 'L', 'L', 'Z', 'M']:
            continue
        numbers = list(map(float, re.findall(r'-?\d+(?:\.\d+)?', d)))
        x0, base, x1, base2, x2, top, x3, top2 = numbers[:8]
        if not (436 < x0 < 535 and 290 < top < base < 405):
            continue
        assert base == base2 and top == top2 and x0 == x3 and x1 == x2
        assert path.get('transform') is None
        ancestor = parents.get(path)
        while ancestor is not None:
            assert ancestor.get('transform') is None, 'Unresolved ancestor transform'
            ancestor = parents.get(ancestor)
        condition = 'apo' if base < 350 else 'holo'
        assert 2.03 < x1-x0 < 2.05
        bins[condition].append(dict(svg_path_index=index, left_pt=x0, right_pt=x1,
            top_pt=top, baseline_pt=base, height_pt=base-top))
    for condition, values in bins.items():
        values.sort(key=lambda row: row['left_pt'])
        assert all(b['left_pt'] >= a['right_pt']-.005 for a,b in zip(values,values[1:]))
        assert all(v['height_pt'] > 0 for v in values)
    assert len(bins['apo']) == 35 and len(bins['holo']) == 33
    source = dict(role='PUBLISHED_MEASURED_HISTOGRAM_BARS_NOT_FITTED_CURVES',
        source_pdf='Peter_2022_NatureCommunications_DEER_smFRET_crossvalidation.pdf',
        physical_page=7, figure='4d right column', variant='HiSiaP175/228', dye_pair='TMR/Cy5',
        converter='installed pdftocairo -f7 -l7 -svg', frames=frames, bins=bins,
        calibration='Same displayed E scale in stacked panels; exact bin edges not printed. Frame-normalized displacement only until quantitative axis mapping admitted.',
        exclusions=['Smooth Gaussian paths', 'Printed fitted mean/sigma', 'Figure4e distance bars', 'Single-label traces'],
        repetition_status='Representative published histograms; no individual repetition identity or event count available',
        scientific_calculation=False)
    (out/'source_geometry.local.json').write_text(json.dumps(source,indent=2)+'\n')
    shutil.copyfile('/tmp/q15_figure4.svg', out/'source_figure4.local.svg')
    report = {key:value for key,value in source.items() if key != 'bins'}
    report['bar_counts'] = {k:len(v) for k,v in bins.items()}
    report['status'] = 'PROCESSED_OBSERVATION_GEOMETRY_ADMITTED_FOR_DIRECTION_ONLY'
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
