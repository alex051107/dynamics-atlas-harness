"""Review-side fixed author weights only. Never imports optimizer or feeds Rules."""
from pathlib import Path
import csv, datetime, json, sys, argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--input-root", type=Path, required=True)
parser.add_argument("--output-dir", type=Path, required=True)
args = parser.parse_args()
INPUT = args.input_root
METHOD = INPUT / "BME_reweight/inputs_and_method"
REFERENCE = INPUT / "BME_reweight/reference_only"
OUT = args.output_dir
RTOL, ATOL = 1e-6, 1e-5

def tokens(path):
    return [x.split() for x in path.read_text().splitlines()
            if x.strip() and not x.lstrip().startswith("#")]

def run():
    OUT.mkdir(exist_ok=False)
    result = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_commit": "85979b1b4123b6b5391b617d16551969eda9f56e",
        "command": [sys.executable, str(Path(__file__).resolve())],
        "scope": "REVIEW_SIDE_AUTHOR_WEIGHT_RECONSTRUCTION_ONLY",
        "optimization_runs": 0, "rules_runs": 0,
        "tolerance": {"rtol": RTOL, "atol": ATOL,
            "basis": "Predeclared diagnostic tolerance for finite deposited predictions and five-decimal post-fit stats; not a scientific acceptance threshold."},
        "coordinate_mapping": "NOT_VERIFIED",
    }
    try:
        weights = np.loadtxt(REFERENCE / "BME_simulation_weights.dat")
        raw = weights[:, 1]
        assert np.all(np.isfinite(weights)) and np.all(raw >= 0) and raw.sum() > 0
        w = raw / raw.sum()
        uniform = np.ones(len(w)) / len(w)
        pos = w > 0
        kl = float(np.sum(w[pos] * np.log(w[pos] / uniform[pos])))
        result["weights"] = {"rows": len(w), "raw_sum": float(raw.sum()),
            "normalization": "divide deposited weights by their sum",
            "relative_entropy": -kl, "entropy_effective_fraction": float(np.exp(-kl)),
            "weight_ess_not_independent_samples": float(1 / np.sum(w*w)),
            "max_weight": float(w.max())}
        inputs = {
            "saxs": "simulation_SAXS.dat",
            "amide": "simulation_HN2_NOE.dat",
            "methyl": "simulation_methyl_NOE.dat",
        }
        sims = {k: np.loadtxt(METHOD / v) for k, v in inputs.items()}
        for k, a in sims.items():
            assert np.array_equal(a[:, 0], weights[:, 0]), (k, "frame IDs mismatch")
            assert np.all(np.isfinite(a)) and np.all(a[:, 1:] > 0)
        assert len(np.unique(weights[:, 0])) == len(w)
        result["matrix_row_identity"] = "All three matrices have same unique ordered IDs as author weights; coordinate mapping separate."
        channels, auditrows = {}, []
        saxsstats = np.loadtxt(REFERENCE / "BME_stats_SAXS.dat")
        experiment = np.loadtxt(INPUT / "SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat", skiprows=1)
        matched = []
        for q in saxsstats[:, 0]:
            ids = np.flatnonzero(np.isclose(experiment[:, 0], q, rtol=0, atol=1e-10))
            assert len(ids) == 1, ("q mapping", q)
            matched.append(int(ids[0]))
        assert len(set(matched)) == len(matched)
        observed = experiment[matched]
        assert len(observed) == sims["saxs"].shape[1]-1
        assert np.all(observed[:, 2] > 0)
        assert np.allclose(observed[:, 1], saxsstats[:, 2], rtol=RTOL, atol=ATOL)
        pred = w @ sims["saxs"][:, 1:]
        delta = pred - saxsstats[:, 1]
        agree = np.isclose(pred, saxsstats[:, 1], rtol=RTOL, atol=ATOL)
        channels["saxs"] = {"observables": len(pred), "postfit_matches": int(agree.sum()),
            "max_abs_postfit_delta": float(abs(delta).max()),
            "uniform_chi2_mean": float(np.mean(((uniform @ sims["saxs"][:,1:]-observed[:,1])/observed[:,2])**2)),
            "author_weight_chi2_mean": float(np.mean(((pred-observed[:,1])/observed[:,2])**2))}
        for i in range(len(pred)):
            auditrows.append(["saxs", str(observed[i,0]), pred[i], saxsstats[i,1], delta[i], bool(agree[i])])
        totals = {key: {"count": 0, "violations": 0, "intensity_sum": 0.0, "distance_sum": 0.0}
                  for key in ("uniform", "author_weight")}
        for name, expfile, statsfile in (
            ("amide","exp_HN2_NOE.dat","BME_stats_HN_NOE.dat"),
            ("methyl","exp_methyl_NOE.dat","BME_stats_methyl_NOE.dat")):
            er = tokens(METHOD / expfile); sr = tokens(REFERENCE / statsfile)
            assert all(len(x)==5 and x[-1]=="UPPER" for x in er)
            labels = ["-".join(x[:2]) for x in er]
            slabels = ["".join(x[:-2]) for x in sr]
            assert labels == slabels, (name, "restraint identity/order mismatch")
            upper = np.array([float(x[2]) for x in er])
            sigma = np.array([float(x[3]) for x in er])
            reported = np.array([float(x[-2]) for x in sr])
            assert np.allclose(upper, [float(x[-1]) for x in sr], rtol=0, atol=1e-10)
            assert len(upper) == sims[name].shape[1]-1
            matrix = sims[name][:,1:]
            intensity = matrix**-3
            y, error = upper**-3, 3*sigma/upper**4
            info = {"observables": len(upper), "restraint_labels_and_bounds": "MATCH"}
            for key, ww in (("uniform",uniform),("author_weight",w)):
                ipred = ww @ intensity
                distance = ipred**(-1/3)
                iz = np.maximum(y-ipred,0)/error
                dz = np.maximum(distance-upper,0)/sigma
                nv = int(np.sum(distance>upper))
                isum, dsum = float(iz@iz), float(dz@dz)
                info[key] = {"upper_violations": nv,
                    "intensity_chi2_all": isum/len(upper),
                    "intensity_chi2_violations_only": isum/nv if nv else None,
                    "distance_chi2_all": dsum/len(upper),
                    "distance_chi2_violations_only": dsum/nv if nv else None}
                totals[key]["count"] += len(upper)
                totals[key]["violations"] += nv
                totals[key]["intensity_sum"] += isum
                totals[key]["distance_sum"] += dsum
                if key == "author_weight":
                    diff = distance-reported
                    agree = np.isclose(distance,reported,rtol=RTOL,atol=ATOL)
                    info.update(postfit_matches=int(agree.sum()), max_abs_postfit_delta=float(abs(diff).max()))
                    for i in range(len(labels)):
                        auditrows.append([name,labels[i],distance[i],reported[i],diff[i],bool(agree[i])])
            channels[name] = info
        for key,v in totals.items():
            v["intensity_chi2_all"] = v["intensity_sum"]/v["count"]
            v["intensity_chi2_violations_only"] = v["intensity_sum"]/v["violations"] if v["violations"] else None
            v["distance_chi2_all"] = v["distance_sum"]/v["count"]
            v["distance_chi2_violations_only"] = v["distance_sum"]/v["violations"] if v["violations"] else None
        result.update(channels=channels,noe_combined=totals)
        result["postfit_comparison"] = {
            "matched": sum(v["postfit_matches"] for v in channels.values()),
            "total": sum(v["observables"] for v in channels.values())}
        result["table2_reference"] = {
            "source": "Bengtsen2020 eLife56518 Table2 p7; existing source-matched Markdown lines304-320",
            "uniform": {"saxs":10.0,"noe":8.2,"relative_entropy":0},
            "joint_fit": {"saxs":1.9,"noe":6.0,"relative_entropy":-1.7},
            "comparison_boundary": "One-decimal reference values; matching a rounded value does not establish original config or exact chi2 definition."}
        result["status"] = "POSTFIT_PREDICTIONS_MATCH" if all(x[-1] for x in auditrows) else "POSTFIT_PREDICTIONS_DIFFER"
        with (OUT/"per_observable.csv").open("w") as f:
            writer=csv.writer(f);writer.writerow(["channel","label","recalculated","author_reported","delta","within_tolerance"]);writer.writerows(auditrows)
    except Exception as e:
        result.update(status="INPUT_OR_AUDIT_FAILURE",error=f"{type(e).__name__}: {e}")
        raise
    finally:
        (OUT/"result.json").write_text(json.dumps(result,indent=2)+"\n")
        (OUT/"audit_source.py").write_text(Path(__file__).read_text())
        print(json.dumps(result,indent=2))
if __name__=="__main__":
    run()

