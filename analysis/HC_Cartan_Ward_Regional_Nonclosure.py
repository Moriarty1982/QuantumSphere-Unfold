"""Smooth necessary-Ward-system controls, NOT lifts to parent field solutions.

The temporal multiplier gate is reused; the full multiplier background is not.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def local_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


second = local_module("regional_second_closure", "HC_Cartan_Constitutive_Second_Closure.py")
coordinate = local_module("regional_coordinate_ward", "HC_Cartan_Diffeomorphism_Residual_Identity.py")
lorentz = local_module("regional_lorentz_ward", "HC_Cartan_Lorentz_Residual_Identity.py")
RADIUS = .01
SEED_VECTOR = np.array([1., 0., 0., 0.])
SPATIAL_VECTOR = np.array([1., .3, -.2])


def input_fingerprints():
    result = second.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Diffeomorphism_Residual_Identity.py",
                 "HC_Cartan_Lorentz_Residual_Identity.py"):
        result[name] = hashlib.sha256(Path(__file__).with_name(name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def load_gate():
    _, point, _, _, _ = second.neighborhood.load_data()
    return second.multiplier_gate(point)


def profile(t, kind):
    if not np.isfinite(t):
        raise ValueError("Finite time required")
    if kind == "linear":
        return np.array([t, 1., 0.])
    if kind != "flat":
        raise ValueError("Profile must be linear or flat")
    # exp(-tau^2/t^2) and both derivatives underflow below this threshold.
    tau = .25
    if t <= tau/30:
        return np.zeros(3)
    z = t/tau
    b = np.exp(-1/z**2)
    return np.array([b, 2*b/(tau*z**3), b*(4/z**6-6/z**4)/tau**2])


def projected_vector(matrix, x):
    """v=P_ell q and its exact first/second spatial derivatives."""
    x = np.asarray(x, float)
    if x.shape != (3,) or not np.all(np.isfinite(x)):
        raise ValueError("Three finite spatial coordinates required")
    ell = matrix[0]+x @ matrix[1:]
    gradient = matrix[1:]
    s, n = ell @ ell, ell @ SEED_VECTOR
    if s <= 1e-20:
        raise ValueError("Nonzero temporal multiplier required")
    sj = 2*gradient @ ell
    nj = gradient @ SEED_VECTOR
    sjk = 2*gradient @ gradient.T
    alpha = n/s
    aj = nj/s-n*sj/s**2
    ajk = (-(np.outer(nj, sj)+np.outer(sj, nj)+n*sjk)/s**2
           +2*n*np.outer(sj, sj)/s**3)
    v = SEED_VECTOR-ell*alpha
    dv = -gradient*alpha-np.outer(aj, ell)
    ddv = np.empty((3, 3, 4))
    for j, k in np.ndindex(3, 3):
        ddv[j, k] = -gradient[j]*aj[k]-gradient[k]*aj[j]-ell*ajk[j, k]
    return ell, v, dv, ddv


def fields(matrix, t, x, kind="flat"):
    """Formal residual fields. F is NOT evaluated from any spinor or coframe."""
    ell, v, dv, ddv = projected_vector(matrix, x)
    b, bt, btt = profile(t, kind)
    f, df, ddf = np.zeros((4, 4)), np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))
    f[:, 1:] = b*np.outer(v, SPATIAL_VECTOR)
    df[0, :, 1:] = bt*np.outer(v, SPATIAL_VECTOR)
    ddf[0, 0, :, 1:] = btt*np.outer(v, SPATIAL_VECTOR)
    for j in range(3):
        df[j+1, :, 1:] = b*np.outer(dv[j], SPATIAL_VECTOR)
        ddf[0, j+1, :, 1:] = ddf[j+1, 0, :, 1:] = bt*np.outer(dv[j], SPATIAL_VECTOR)
        for k in range(3):
            ddf[j+1, k+1, :, 1:] = b*np.outer(ddv[j, k], SPATIAL_VECTOR)
    lam, dl = np.zeros((4, 4)), np.zeros((4, 4, 4))
    lam[:, 0] = ell
    dl[1:, :, 0] = matrix[1:]
    return {"multiplier": lam, "multiplier_first": dl,
            "constraint": f, "constraint_first": df, "constraint_second": ddf,
            "coframe": np.eye(4), "coframe_first": np.zeros((4, 4, 4)),
            "Euler": np.zeros((4, 4)), "Euler_first": np.zeros((4, 4, 4)),
            "probe": np.zeros((3, 4), complex), "psi_first": np.zeros((4, 3, 4), complex)}


def differentiated_coordinate_terms(data):
    """Only two groups survive for these formal residual fields."""
    lam, dl, df, ddf = [data[k] for k in (
        "multiplier", "multiplier_first", "constraint_first", "constraint_second")]
    first, second_term = np.zeros((4, 4)), np.zeros((4, 4))
    for r, nu in np.ndindex(4, 4):
        first[r, nu] = sum(dl[r, a, mu]*(df[mu, a, nu]-df[nu, a, mu])
                           for a, mu in np.ndindex(4, 4))
        second_term[r, nu] = sum(lam[a, mu]*(ddf[r, mu, a, nu]-ddf[r, nu, a, mu])
                                 for a, mu in np.ndindex(4, 4))
    return first, second_term


def actual_point_lorentz_gate():
    """Separate mixed Lorentz2 gate, not the altered Ward-only background."""
    _, point, _, _, _ = second.neighborhood.load_data()
    rows = []
    for generator in lorentz.generators():
        for j in range(1, 4):
            rows.append((generator.T @ point["multiplier_first"][j])[:, 1:].T.reshape(-1))
    return np.array(rows)


def evaluate():
    fingerprints = input_fingerprints()
    matrix = load_gate()
    singular = np.linalg.svd(matrix, compute_uv=False)
    ell_lower = np.linalg.norm(matrix[0])-np.linalg.norm(matrix[1:], 2)*RADIUS
    if ell_lower <= 0:
        raise ValueError("Chosen spatial ball does not retain ell nonzero")
    points = [np.zeros(3), np.array([.003, -.002, .001]), np.array([-.002, .004, .001])]
    rows = []
    for kind in ("linear", "flat"):
        for t in (0., .125, .25):
            for x in points:
                data = fields(matrix, t, x, kind)
                a, b = differentiated_coordinate_terms(data)
                algebraic = np.array([np.sum(data["constraint"]*(g.T @ data["multiplier"]))
                                      for g in lorentz.generators()])
                rows.append({"profile": kind, "time": t, "spatial_point": x.tolist(),
                             "constraint_norm": float(np.linalg.norm(data["constraint"])),
                             "constraint_first_norm": float(np.linalg.norm(data["constraint_first"])),
                             "constraint_second_norm": float(np.linalg.norm(data["constraint_second"])),
                             "coordinate_Ward_norm": float(np.linalg.norm(coordinate.ward(data))),
                             "Lorentz_Ward_norm": float(np.linalg.norm(algebraic)),
                             "differentiated_coordinate_Ward_norm": float(np.linalg.norm(a+b)),
                             "omitted_second_constitutive_source_norm": float(np.linalg.norm(a))})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Regional Ward control inputs changed")
    gate = actual_point_lorentz_gate()
    return {"scope": "Formal necessary Ward residual system ONLY, not parent-realizable fields",
            "input_sha256": fingerprints, "gate_matrix": matrix.tolist(),
            "spatial_radius": RADIUS, "temporal_multiplier_lower_norm": float(ell_lower),
            "uniform_gate_singular_lower_bound": float(singular[-1]/(1+RADIUS)),
            "uniform_invertibility_derivation": "M(x)=T(x)M(0), T=I+e0*(0,x), ||T^-1||<=1+|x|",
            "reuses_only_temporal_multiplier_value_and_spatial_temporal_column_gradient": True,
            "spatial_multiplier_columns_identically_zero_not_saved_parent_jets": True,
            "formal_zero_Euler_and_probe_residuals_not_evaluated_parent_equations": True,
            "zero_initial_data_with_smooth_nonzero_later_formal_residual": True,
            "not_a_parent_solution_or_parent_nonuniqueness_counterexample": True,
            "control_fields": rows, "actual_point_mixed_Lorentz2_gate_shape": list(gate.shape),
            "actual_point_mixed_Lorentz2_gate_singular_values": np.linalg.svd(gate, compute_uv=False).tolist(),
            "actual_point_mixed_Lorentz2_gate_rank": second.first.matrix_rank(gate)[0],
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "uniform_gate_singular_lower_bound", "actual_point_mixed_Lorentz2_gate_rank")}))


if __name__ == "__main__":
    main()
