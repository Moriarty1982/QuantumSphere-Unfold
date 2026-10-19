"""Identify known normal compatibility rows and the remaining mixed-curl gates.

Conditional subsidiary identities, not a closed coupled propagation theorem.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
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


uniform = local_module("compatibility_split_uniform", "HC_Cartan_Uniform_Normal_Bound.py")
lorentz = local_module("compatibility_split_lorentz", "HC_Cartan_Lorentz_Residual_Identity.py")
general, prior = uniform.general, uniform.prior


def input_fingerprints():
    result = uniform.input_fingerprints()
    result.update(lorentz.input_fingerprints())
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def known_rows(fields):
    spatial = [4*a+mu for a in range(4) for mu in (1, 2, 3)]
    gravity = [40+4*a for a in range(4)]
    selectors = np.eye(68)[spatial+gravity]
    identities = []
    for generator in lorentz.generators():
        row = np.zeros(68)
        row[:16] = (generator.T @ fields["multiplier"]).reshape(-1)
        spin = fields["psi"] @ lorentz.spin_generator(generator).T
        row[16:40] = 2*prior.joint.prior.realify(spin)
        row[40:56] = (generator @ fields["coframe"]).reshape(-1)
        identities.append(row)
    return selectors, np.asarray(identities)


def left_space(matrix):
    left, singular, _ = np.linalg.svd(matrix, full_matrices=True)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    return left[:, rank:], rank


def split_projectors(matrix, fields):
    selectors, identities = known_rows(fields)
    p_spatial = selectors[:12].T @ selectors[:12]
    p_gravity = selectors[12:].T @ selectors[12:]
    p_selected = p_spatial+p_gravity
    residual_identities = (np.eye(68)-p_selected) @ identities.T
    identity_frame, singular, _ = np.linalg.svd(residual_identities, full_matrices=False)
    if np.sum(singular > 1e-9) != 6:
        raise ValueError("The six Lorentz identities are not independent of the selected constraints")
    identity_frame = identity_frame[:, :6]
    p_identity = identity_frame @ identity_frame.T
    known = p_selected+p_identity
    left, rank = left_space(matrix)
    old_left, old_rank = left_space(matrix[:56])
    old_projector = np.zeros((68, 68))
    old_projector[:56, :56] = old_left @ old_left.T
    if rank != 40 or old_rank != 34:
        raise ValueError("This split requires the sampled rank-40/rank-34 branch")
    remaining = (np.eye(68)-known) @ left
    frame, values, _ = np.linalg.svd(remaining, full_matrices=False)
    if np.sum(values > 1e-8) != 6:
        raise ValueError("Six remaining mixed-curl gates required")
    frame = frame[:, :6]
    p_mixed = frame @ frame.T
    return {"spatial": p_spatial, "gravity": p_gravity, "Lorentz_representative": p_identity,
            "mixed": p_mixed, "mixed_frame": frame, "full_left": left @ left.T,
            "old_left": old_projector, "selectors": selectors, "identities": identities,
            "rank": rank, "old_rank": old_rank}


def direct_normal_matrix(prepared, fields):
    spatial = fields["psi_first"].copy()
    spatial[0] = 0
    hessian = general.prolong.fast_cartan_data(prepared, fields["coframe"], fields["psi"])[0]
    values = {"e": fields["coframe"], "inverse": np.linalg.inv(fields["coframe"]),
              "volume": np.asarray(abs(np.linalg.det(fields["coframe"]))),
              "de": fields["coframe_first"], "psi": fields["psi"], "spatial_dp": spatial,
              "lam": fields["multiplier"], "hessian_inverse": np.linalg.inv(hessian)}
    return uniform.coefficient_matrix(prepared, **{k: uniform.ball(v) for k, v in values.items()})[0].center


def projection_state(matrix, target):
    left, singular, right = np.linalg.svd(matrix, full_matrices=False)
    if singular[-1] <= max(1e-10, singular[0]*1e-10):
        raise ValueError("Full-column-rank augmented matrix required")
    inverse = (right.T/singular) @ left.T
    projector = np.eye(matrix.shape[0])-matrix @ inverse
    return {"inverse": inverse, "projector": projector, "solution": inverse @ target,
            "residual": projector @ target, "minimum_singular": float(singular[-1])}


def compatibility_transport(matrix, target, matrix_first, target_first):
    state = projection_state(matrix, target)
    p, inv, solution, residual = (state[k] for k in ("projector", "inverse", "solution", "residual"))
    forcing = p @ (target_first-matrix_first @ solution)
    homogeneous = -inv.T @ matrix_first.T @ residual
    return dict(state, forcing=forcing, homogeneous=homogeneous, derivative=forcing+homogeneous)


def transport_diagnostic(prepared, point, jets, full, coordinate_rows, radius):
    def data(x):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        matrix = direct_normal_matrix(prepared, fields)
        values = general.normal_values(fields)
        actual = general.equations(prepared, fields)["vector"]
        base = actual-matrix @ values
        augmented = np.vstack((matrix, coordinate_rows))
        target = np.r_[-base, coordinate_rows @ values]
        return augmented, target, projection_state(augmented, target)
    x = np.eye(4)[0]*radius
    matrix, target, state = data(x)
    result = []
    for step in (1e-7, 5e-8):
        plus_matrix, plus_target, plus = data(x+step*np.eye(4)[0])
        minus_matrix, minus_target, minus = data(x-step*np.eye(4)[0])
        dmatrix, dtarget = (plus_matrix-minus_matrix)/(2*step), (plus_target-minus_target)/(2*step)
        calculated = compatibility_transport(matrix, target, dmatrix, dtarget)
        direct = (plus["residual"]-minus["residual"])/(2*step)
        result.append({"step": step, "compatibility_norm": float(np.linalg.norm(state["residual"])),
            "forcing_norm": float(np.linalg.norm(calculated["forcing"])),
            "homogeneous_norm": float(np.linalg.norm(calculated["homogeneous"])),
            "direct_derivative_norm": float(np.linalg.norm(direct)),
            "transport_difference_error": float(np.linalg.norm(direct-calculated["derivative"]))})
    return {"coordinate": x.tolist(), "diagnostic_radius_not_uniform_majorant_radius": radius,
            "minimum_augmented_singular": state["minimum_singular"], "differences": result}


def evaluate(*, workers=2):
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    before = json.loads(Path(__file__).with_name("HC_Cartan_General_Normal_Chart.json").read_text(encoding="utf-8"))
    if before["input_sha256"] != general.input_fingerprints():
        raise ValueError("General normal chart has stale inputs")
    radius = before["radius_used_for_samples"]
    coordinate_rows = np.array(before["fixed_coordinate_rows"])
    services = prior.create_container().services()
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4)[0]))

    def sample(direction):
        fields = general.domain.temporal.fields(prepared, point, jets, full, radius*direction)
        matrix = general.normal_system(prepared, fields, services=services)["matrix"]
        result = general.equations(prepared, fields)["vector"]
        split = split_projectors(matrix, fields)
        selected, identities = split["selectors"], split["identities"]
        values = general.normal_values(fields)
        trial = general.equations(prepared, general.with_normal_values(
            fields, values+np.random.default_rng(191028).normal(size=56)*.1))["vector"]
        pieces = [split[k] for k in ("spatial", "gravity", "Lorentz_representative", "mixed")]
        return {"direction": direction.tolist(), "full_rank": split["rank"], "old_rank": split["old_rank"],
            "selector_matrix_error": float(np.linalg.norm(selected @ matrix)),
            "Lorentz_matrix_error": float(np.linalg.norm(identities @ matrix)),
            "Lorentz_actual_identity_norm": float(np.linalg.norm(identities @ result)),
            "Lorentz_unfitted_identity_norm": float(np.linalg.norm(identities @ trial)),
            "known_span_old_left_error": float(np.linalg.norm(sum(pieces[:3])-split["old_left"])),
            "full_left_split_error": float(np.linalg.norm(sum(pieces)-split["full_left"])),
            "block_dimensions": {k: int(round(np.trace(split[k]))) for k in (
                "spatial", "gravity", "Lorentz_representative", "mixed")},
            "spatial_constraint_norm": float(np.linalg.norm(selected[:12] @ result)),
            "gravitational_constraint_norm": float(np.linalg.norm(selected[12:] @ result)),
            "remaining_mixed_gate_norm": float(np.linalg.norm(split["mixed"] @ result)),
            "remaining_normal_variation_error": float(np.linalg.norm(split["mixed"] @ (trial-result))),
            "all_left_compatibility_norm": float(np.linalg.norm(split["full_left"] @ result))}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        samples = list(pool.map(sample, directions))
    diagnostic = transport_diagnostic(prepared, point, jets, full, coordinate_rows, radius)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Compatibility split inputs changed")
    return {"scope": "Known normal compatibility identities, conditional propagation and six remaining mixed gates",
        "input_sha256": fingerprints, "samples": samples, "transport_diagnostic": diagnostic,
        "kinematic_identity": "partial_0 C_ai = J_0i,a + partial_i C_a0",
        "projector_identity": "r_t = P(g_t - T_t T^+ g) - (T^+)^T T_t^T r",
        "six_Lorentz_rows_are_identities_not_independent_initial_constraints": True,
        "constitutive_propagation_requires_temporal_constraint_and_all_mixed_curls": True,
        "remaining_six_gate_propagation_not_closed": True,
        "projector_transport_forcing_not_shown_homogeneous": True,
        "not_full_constraint_propagation_or_regional_existence": True,
        "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    result = evaluate(workers=args.workers)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"origin": result["samples"][0],
        "maximum_mixed_gate": max(s["remaining_mixed_gate_norm"] for s in result["samples"]),
        "transport": result["transport_diagnostic"]}))


if __name__ == "__main__":
    main()
