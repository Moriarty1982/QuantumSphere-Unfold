"""Uniform algebraic Cartan regularity on the saved joint1114 Taylor fields.

Finite floating point evaluation of analytic inequalities, not interval certification
or a full PDE existence result. Independent of the joint-neighborhood sidecar.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import types

import numpy as np


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "joint_cartan_completion", ROOT / "HC_Cartan_Next_Joint_Completion.py")
joint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(joint)
cartan, prior, prolong = joint.cartan, joint.prior, joint.prolong


def input_fingerprints():
    """Fingerprint local dependency modules and saved reports with LF normalization."""
    paths = {Path(__file__).resolve(), ROOT / "HC_Cartan_Next_Joint_Completion.json",
             ROOT / "HC_Cartan_Joint_Neighborhood.json"}
    seen = set()
    def visit(module):
        path = Path(getattr(module, "__file__", "")).resolve()
        if path.parent != ROOT or path in seen:
            return
        seen.add(path)
        paths.add(path)
        if path.with_suffix(".json").exists():
            paths.add(path.with_suffix(".json"))
        for value in vars(module).values():
            if isinstance(value, types.ModuleType):
                visit(value)
    visit(joint)
    return {p.name: hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
            for p in sorted(paths)}


def expand_symmetric(values, order):
    values = np.asarray(values)
    indices = tuple(itertools.combinations_with_replacement(range(4), order))
    if values.shape[0] != len(indices) or not np.all(np.isfinite(values)):
        raise ValueError("Finite unique symmetric derivative coordinates required")
    full = np.zeros((4,)*order+values.shape[1:], dtype=values.dtype)
    for index, value in zip(indices, values):
        for permutation in set(itertools.permutations(index)):
            full[permutation] = value
    return full


def load_data():
    prepared, point, saved, fingerprint = joint.third.diagnostic.load_data()
    report = json.loads((ROOT / "HC_Cartan_Next_Joint_Completion.json").read_text(encoding="utf-8"))
    jets = joint.regular.unpack(np.asarray(report["jet_coordinates"]))
    if report["input_sha256"] != joint.input_fingerprints():
        raise ValueError("Saved joint completion has stale inputs")
    if report["input_scalar_completion_sha256"] != fingerprint:
        raise ValueError("Saved joint completion has another lower-point source")
    if not np.array_equal(jets["p2"], saved["p2"]):
        raise ValueError("Retained spinor Hessian changed")
    coordinates = cartan.checks._real(report["connection_coordinates"], (880,), "joint E4/lambda3")
    p4 = cartan.checks._real(report["fourth_spinor_real"], (35, 24), "joint psi4")
    extras = {"e4": coordinates[:560].reshape(35, 4, 4),
              "l3": coordinates[560:].reshape(20, 4, 4),
              "p4": np.array([prior.complexify(v, (3, 4)) for v in p4])}
    return prepared, point, jets, extras, report


def fields(prepared, point, jets, extras, x):
    """Evaluate the full new quartic fields and eliminate the exact Cartan block."""
    x = cartan.checks._real(x, (4,), "coordinate displacement")
    base = joint.regular.taylor_fields(prepared, point, jets, x)
    hjet = joint.third.diagnostic.homogeneous_jet
    e = base["coframe"]+hjet(extras["e4"], 4, x)
    de = base["coframe_first"]+np.array([hjet(extras["e4"], 4, x, (r,)) for r in range(4)])
    dde = base["coframe_second"]+np.array([
        [hjet(extras["e4"], 4, x, (r, s)) for s in range(4)] for r in range(4)])
    psi = base["psi"]+hjet(extras["p4"], 4, x)
    dp = base["psi_first"]+np.array([hjet(extras["p4"], 4, x, (r,)) for r in range(4)])
    lam = base["multiplier"]+hjet(extras["l3"], 3, x)
    bundle = prolong.dirac.bundle(e, de, dde)
    hessian, response, source = prolong.fast_cartan_data(prepared, e, psi)
    k = np.linalg.solve(hessian, -source+response.T @ lam.reshape(-1))
    omega = bundle["omega"]+cartan.unpack(k)
    return {"coframe": e, "psi": psi, "psi_first": dp, "multiplier": lam,
            "omega": omega, "hessian": hessian,
            "Cartan": hessian @ k+source-response.T @ lam.reshape(-1)}


def exact_hessian(prepared, e):
    _, inverse, volume = cartan.frame_data(e)
    return volume*np.einsum("ma,nb,pqmnab->pq", inverse, inverse,
                            prepared["curvature_hessian"])/2


def congruence_hessian(prepared, e):
    transform = np.kron(np.linalg.inv(e).T, np.eye(6))
    return abs(np.linalg.det(e))*transform.T @ prepared["hessian"] @ transform


def coefficient_norms(prepared, point, jets, extras):
    singular = np.linalg.svd(prepared["hessian"], compute_uv=False)
    return {"coframe_second": float(np.linalg.norm(point["coframe_second"])),
            "coframe_third": float(np.linalg.norm(jets["e3"])),
            "coframe_fourth": float(np.linalg.norm(expand_symmetric(extras["e4"], 4))),
            "coframe_fourth_unique_unweighted": float(np.linalg.norm(extras["e4"])),
            "minimum_base_hessian_singular_value": float(singular[-1]),
            "base_hessian_operator_norm": float(singular[0])}


def uniform_bound(data, d):
    d = cartan.checks._scalar(d, "coframe operator distance")
    if not 0 <= d < 1:
        raise ValueError("Coframe distance must satisfy 0 <= d < 1")
    sigma = data["minimum_base_hessian_singular_value"]
    norm = data["base_hessian_operator_norm"]
    if not (np.isfinite(sigma) and np.isfinite(norm) and 0 < sigma <= norm):
        raise ValueError("Positive finite base Hessian singular margin required")
    t = d/(1-d)
    volume_change = 4*d+6*d*d+4*d**3+d**4
    change = norm*(volume_change/(1-d)**2+2*t+t*t)
    lower = sigma*(1-d)**4/(1+d)**2
    return {"coframe_change_bound": d, "hessian_change_bound": change,
            "perturbation_singular_value_lower_bound": sigma-change,
            "hessian_singular_value_lower_bound": lower,
            "hessian_inverse_norm_upper_bound": 1/lower, "resolved": True}


def bound(data, radius):
    radius = cartan.checks._scalar(radius, "nonnegative coordinate radius")
    if radius < 0:
        raise ValueError("Nonnegative radius required")
    norms = [data[k] for k in ("coframe_second", "coframe_third", "coframe_fourth")]
    if not np.all(np.isfinite(norms)) or min(norms) < 0:
        raise ValueError("Finite nonnegative full tensor norms required")
    d = norms[0]*radius**2/2+norms[1]*radius**3/6+norms[2]*radius**4/24
    if not np.isfinite(d) or d >= 1:
        return {"radius": radius, "coframe_change_bound": d, "resolved": False,
                "reason": "coframe ball must have distance less than one"}
    return dict(uniform_bound(data, d), radius=radius)


def select_radius(data):
    radius = 1.
    for _ in range(80):
        estimate = bound(data, radius)
        if (estimate["resolved"] and estimate["perturbation_singular_value_lower_bound"]
                >= data["minimum_base_hessian_singular_value"]/2):
            return estimate
        radius /= 2
    raise ValueError("No positive Cartan perturbation margin resolved")


def samples(prepared, point, jets, extras, radius):
    rng = np.random.default_rng(11142026)
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4), rng.normal(size=(8, 4))))
    directions[1:] /= np.linalg.norm(directions[1:], axis=1, keepdims=True)
    result = []
    for direction in directions:
        f = fields(prepared, point, jets, extras, radius*direction)
        e, h = f["coframe"], f["hessian"]
        original = cartan.contorsion_hessian(e)
        result.append({"coframe_change": float(np.linalg.norm(e-np.eye(4), 2)),
                       "hessian_change": float(np.linalg.norm(h-prepared["hessian"], 2)),
                       "hessian_minimum_singular_value": float(np.linalg.svd(h, compute_uv=False)[-1]),
                       "hessian_inverse_norm": float(np.linalg.norm(np.linalg.inv(h), 2)),
                       "polarized_hessian_error": float(np.linalg.norm(h-original, 2)),
                       "congruence_error": float(np.linalg.norm(h-congruence_hessian(prepared, e), 2)),
                       "Cartan_residual_norm": float(np.linalg.norm(f["Cartan"]))})
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, extras, _ = load_data()
    data = coefficient_norms(prepared, point, jets, extras)
    estimate = select_radius(data)
    controls = []
    for factor in (1., 16., 4096.):
        changed = dict(data, coframe_fourth=data["coframe_fourth"]*factor)
        controls.append({"fourth_tensor_norm_factor": factor,
                         "same_radius_bound": bound(changed, estimate["radius"]),
                         "reselected_bound": select_radius(changed)})
    checks = samples(prepared, point, jets, extras, estimate["radius"])
    parent_report = json.loads((ROOT / "HC_Cartan_Joint_Neighborhood.json").read_text(encoding="utf-8"))
    parent_radius = parent_report["regular_neighborhood"]["radius"]
    parent_estimate = bound(data, parent_radius)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Inputs changed during Cartan regularity evaluation")
    return {"scope": "Uniform algebraic Cartan invertibility on saved joint1114 quartic Taylor fields",
            "input_sha256_LF_normalized": fingerprints,
            "fixed_couplings": "Q, M unchanged; Einstein coefficient 1; vacuum 0",
            "coefficient_norms": data, "regular_neighborhood": estimate,
            "at_joint_temporal_neighborhood_radius": parent_estimate,
            "sample_checks_not_the_proof": checks, "norm_scaling_countercontrols": controls,
            "finite_float_not_interval_certified": True, "not_full_PDE_existence": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
