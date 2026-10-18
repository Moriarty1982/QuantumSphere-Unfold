"""Uniform tilted-normal estimates for a 28-real-dimensional partial block.

Geometry derivatives are frozen in this block. This is not the coupled symbol.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "joint_normal_neighborhood", Path(__file__).with_name("HC_Cartan_Joint_Neighborhood.py"))
neighborhood = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(neighborhood)
cartan, prolong, prior = neighborhood.cartan, neighborhood.prolong, neighborhood.prior


def schur_block(coframe, psi, multiplier, normal):
    normal = cartan.checks._real(normal, (4,), "normal covector")
    p = np.asarray(psi).reshape(12)
    weight = np.einsum("m,mij->ij", normal, cartan.kinetic_weights(coframe, multiplier))
    eigenvalues = np.linalg.eigvalsh(weight)
    if eigenvalues[0] <= 0:
        raise ValueError("Positive normal probe weight required")
    vectors = np.array([np.linalg.solve(weight, a @ p) for a in prolong.Q_WEIGHTS])
    block = np.array([[-.5*np.vdot(p, a @ v).imag for v in vectors] for a in prolong.Q_WEIGHTS])
    return {"weight": weight, "block": block, "weight_eigenvalues": eigenvalues,
            "singular_values": np.linalg.svd(block, compute_uv=False)}


def partial_matrix(coframe, psi, multiplier, normal):
    """Unknowns: u (24 real) and a_b=n_mu delta(lambda_b^mu) (4 real).

    Output: probe principal residual and X^mu F_a,mu, with n_mu X^mu=1.
    The constitutive rows thus have coefficient L(u), not n0*L(u).
    """
    block = schur_block(coframe, psi, multiplier, normal)
    p = np.asarray(psi).reshape(12)
    probe = np.column_stack([prior.realify(1j*block["weight"] @ prior.complexify(e, (12,)))
                             for e in np.eye(24)])
    divergence = np.column_stack([prior.realify(.5j*a @ p) for a in prolong.Q_WEIGHTS])
    lower = neighborhood.third.spatial.constraint_principal_map(np.asarray(psi))
    return np.block([[probe, divergence], [lower, np.zeros((4, 4))]])


def cone_bound(prepared, point, jets, extras, data, ball):
    radius, d = ball["radius"], ball["coframe_change_bound"]
    spatial_multiplier = (np.linalg.norm(point["multiplier"][:, 1:])
        +np.linalg.norm(point["multiplier_first"][..., 1:])*radius
        +np.linalg.norm(jets["l2"][..., 1:])*radius**2/2
        +np.linalg.norm(extras["l3"][..., 1:])*radius**3/6)
    spatial_weight = np.sqrt(2)*(1+d)**4/(1-d)+spatial_multiplier/np.sqrt(2)
    m, s = ball["probe_eigenvalue_lower_bound"], ball["constraint_singular_value_lower_bound"]
    p = data["spinor_value"]+ball["spinor_change_bound"]
    metric_change = ball["inverse_metric_change_bound"]
    sufficient_h = min(m/2, s*m*m/(p*p+s*m))
    metric_limit = np.sqrt((1-metric_change)/(1+metric_change))
    rho = .5*min(sufficient_h/spatial_weight, metric_limit)
    h = rho*spatial_weight
    lower_m = m-h
    change_t = p*p*h/(2*m*lower_m)
    lower_s = s-change_t
    # Norm bounds on the two off-diagonal blocks are ||L||<=p, ||D||<=p/2.
    inverse_majorant = np.array([[1/lower_m+.5*p*p/(lower_m**2*lower_s), .5*p/(lower_m*lower_s)],
                                [p/(lower_m*lower_s), 1/lower_s]])
    return {"coordinate_radius": radius, "normal_convention": "n=(1,q), |q|_Euclidean<=rho",
            "spatial_multiplier_norm_upper_bound": float(spatial_multiplier),
            "spatial_weight_operator_bound": float(spatial_weight), "spinor_norm_upper_bound": float(p),
            "tilt_radius": float(rho), "extra_weight_change_bound": float(h),
            "probe_eigenvalue_lower_bound": float(lower_m),
            "constraint_change_from_temporal_bound": float(change_t),
            "constraint_singular_value_lower_bound": float(lower_s),
            "normal_metric_quadratic_upper_bound": float(-1+rho*rho+metric_change*(1+rho*rho)),
            "partial_28_inverse_norm_upper_bound": float(np.linalg.norm(inverse_majorant, 2)),
            "inverse_majorant": inverse_majorant.tolist()}


def sample_checks(prepared, point, jets, extras, cone):
    rng = np.random.default_rng(281114)
    directions = np.vstack((np.eye(4), -np.eye(4), rng.normal(size=(8, 4))))
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    qdirections = np.vstack((np.eye(3), -np.eye(3), rng.normal(size=(6, 3))))
    qdirections /= np.linalg.norm(qdirections, axis=1, keepdims=True)
    result = []
    for direction in directions:
        f = neighborhood.fields(prepared, point, jets, extras, cone["coordinate_radius"]*direction)
        inverse_metric = np.linalg.inv(f["bundle"]["metric"])
        for q in qdirections:
            n = np.r_[1., cone["tilt_radius"]*q]
            block = schur_block(f["coframe"], f["psi"], f["multiplier"], n)
            matrix = partial_matrix(f["coframe"], f["psi"], f["multiplier"], n)
            result.append({"probe_minimum_eigenvalue": float(block["weight_eigenvalues"][0]),
                           "constraint_minimum_singular_value": float(block["singular_values"][-1]),
                           "normal_metric_quadratic": float(n @ inverse_metric @ n),
                           "partial_28_inverse_norm": float(np.linalg.norm(np.linalg.inv(matrix), 2))})
    return result


def input_fingerprints():
    result = neighborhood.input_fingerprints()
    data = Path(__file__).read_bytes().replace(b"\r\n", b"\n")
    result[Path(__file__).name] = hashlib.sha256(data).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, extras, _ = neighborhood.load_data()
    data = neighborhood.coefficient_norms(prepared, point, jets, extras)
    ball = neighborhood.select_radius(data)
    cone = cone_bound(prepared, point, jets, extras, data, ball)
    samples = sample_checks(prepared, point, jets, extras, cone)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Tilted-cone inputs changed")
    return {"scope": "Normalized tilted probe/constitutive subblock, with geometric derivatives frozen",
            "input_sha256": fingerprints, "uniform_cone_estimate": cone,
            "sample_checks_not_the_proof": samples,
            "not_full_gravitational_normal_symbol": True, "not_hyperbolicity_or_Cauchy_existence": True,
            "not_interval_certified": True, "no_physical_angle_or_length_calibration": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps(result["uniform_cone_estimate"], indent=2))


if __name__ == "__main__":
    main()
