"""Source-parameterized normal inverse of actual Cartan comparison equations.

Finite normal form only: six unresolved source coordinates are not new gauge.
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


neighborhood = local_module("normal_source_joint", "HC_Cartan_Joint_Neighborhood.py")
remaining = local_module("normal_source_remaining", "HC_Cartan_Remaining_Multiplier.py")
regular, spatial, prior, cartan = neighborhood.regular, neighborhood.third.spatial, neighborhood.prior, neighborhood.cartan


def orthonormal_columns(matrix):
    matrix = np.asarray(matrix, float)
    if matrix.ndim != 2 or not np.all(np.isfinite(matrix)):
        raise ValueError("Finite column matrix required")
    q, r = np.linalg.qr(matrix, mode="reduced")
    if np.min(np.abs(np.diag(r))) < 1e-10:
        raise ValueError("Independent columns required")
    for j in range(q.shape[1]):
        if q[np.argmax(abs(q[:, j])), j] < 0:
            q[:, j] *= -1
    return q


def build_reduction(prepared, point):
    system = spatial.normal_curl_system(prepared, point)
    matrix = system["matrix"]
    left, singular, right = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular > singular[0]*1e-10))
    if rank != 40:
        raise ValueError("This normal-source chart requires rank 40")
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    gauge = orthonormal_columns(regular.coframe_normal_gauge_basis())
    canonical = remaining.canonical_basis(prepared)["basis"]
    sources = orthonormal_columns(canonical-gauge @ (gauge.T @ canonical))
    projector = right[rank:].T @ right[rank:]
    if (np.linalg.norm(matrix @ np.c_[gauge, sources]) > 1e-8
            or np.linalg.norm(projector-gauge @ gauge.T-sources @ sources.T) > 1e-8):
        raise ValueError("Declared gauge/source columns do not span this normal kernel")
    return {"matrix": matrix, "inverse": inverse, "rank": rank, "singular": singular,
            "left_null": left[:, rank:], "gauge": gauge, "sources": sources,
            "null_projector": projector, "system": system}


def solve(reduction, rhs, gauge_values=None, source_values=None, tolerance=1e-9):
    """Solve to declared compatibility tolerance; zero defaults select a particular solution."""
    rhs = cartan.checks._real(rhs, (68,), "68 normal equation increments")
    g = np.zeros(10) if gauge_values is None else cartan.checks._real(gauge_values, (10,), "ten gauge coordinates")
    q = np.zeros(6) if source_values is None else cartan.checks._real(source_values, (6,), "six unresolved coordinates")
    if not np.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Positive finite compatibility tolerance required")
    compatibility = reduction["left_null"].T @ rhs
    if np.linalg.norm(compatibility) > tolerance*(1+np.linalg.norm(rhs)):
        raise ValueError("Normal right-hand side violates left compatibility; no solution")
    return reduction["inverse"] @ rhs+reduction["gauge"] @ g+reduction["sources"] @ q


def normal_equations(prepared, point):
    lower = spatial.rank_model.point_equations(
        prepared, point["psi_first"], point["coframe_second"], point["multiplier"], point["multiplier_first"])
    return np.r_[lower["vector"], spatial.explicit_curl(prepared, point)[:3].reshape(-1)]


def higher_source_response(prepared, point, jets, reduction):
    base = regular.equations(prepared, point, jets)["vector"]
    response, affinity = [], []
    for direction in reduction["sources"].T:
        image = regular.equations(prepared, remaining.normal_point(point, direction), jets)["vector"]-base
        double = regular.equations(prepared, remaining.normal_point(point, direction, 2.), jets)["vector"]-base
        response.append(image)
        affinity.append(double-2*image)
    return np.array(response).T, np.array(affinity).T


def input_fingerprints():
    result = neighborhood.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Remaining_Multiplier.py", "HC_Cartan_Spatial_Propagation.py",
                 "HC_Cartan_Cauchy_Rank.py", "HC_Cartan_Regular_Gravity.py"):
        result[name] = hashlib.sha256(Path(__file__).with_name(name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, _ = neighborhood.load_data()
    reduction = build_reduction(prepared, point)
    n, inv, g, u, left = [reduction[key] for key in ("matrix", "inverse", "gauge", "sources", "left_null")]
    higher, affinity = higher_source_response(prepared, point, jets, reduction)
    origin = normal_equations(prepared, point)
    rows = []
    pattern = np.array([1., -.5, .3, .2, .4, -.1])
    connection = spatial.connection_first(prepared, point)
    curvature = cartan.curvature_upper(*connection)
    for amplitude in (0., .01, -.01, .02):
        q = amplitude*pattern
        delta = solve(reduction, np.zeros(68), source_values=q)
        changed = remaining.normal_point(point, delta)
        result = regular.equations(prepared, changed, jets)
        base_higher = regular.equations(prepared, point, jets)["vector"]
        new_connection = spatial.connection_first(prepared, changed)
        rows.append({"amplitude": amplitude,
                     "unprojected_all_68_normal_equations_norm": float(np.linalg.norm(normal_equations(prepared, changed))),
                     "incremental_normal_error": float(np.linalg.norm(n @ delta)),
                     "source_coordinate_error": float(np.linalg.norm(u.T @ delta-q)),
                     "gauge_coordinate_error": float(np.linalg.norm(g.T @ delta)),
                     "curvature_change_norm": float(np.linalg.norm(cartan.curvature_upper(*new_connection)-curvature)),
                     "frozen_higher_384_residual_norm": float(np.linalg.norm(result["vector"])),
                     "higher_affine_prediction_error": float(np.linalg.norm(result["vector"]-base_higher-higher @ q))})
    augmented = np.vstack((n, g.T, u.T))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Normal source inputs changed")
    return {"scope": "Actual added neutral Cartan normal equations with six unresolved coordinates",
            "input_sha256": fingerprints, "normal_shape": list(n.shape), "normal_rank": reduction["rank"],
            "normal_singular_values": reduction["singular"].tolist(),
            "normal_inverse_norm": float(np.linalg.norm(inv, 2)),
            "left_compatibility_dimension": left.shape[1], "gauge_dimension": g.shape[1],
            "unresolved_source_dimension": u.shape[1], "gauge_basis": g.tolist(), "source_basis": u.tolist(),
            "null_projector_decomposition_error": float(np.linalg.norm(reduction["null_projector"]-g @ g.T-u @ u.T)),
            "normal_null_error": float(np.linalg.norm(n @ np.c_[g, u])),
            "penrose_reconstruction_error": float(np.linalg.norm(n @ inv @ n-n)),
            "left_compatibility_error": float(np.linalg.norm(left.T @ n)),
            "augmented_shape": list(augmented.shape),
            "augmented_rank": int(np.linalg.matrix_rank(augmented, tol=1e-9)),
            "origin_all_68_residual_norm": float(np.linalg.norm(origin)),
            "origin_left_compatibility_norm": float(np.linalg.norm(left.T @ origin)),
            "latest_jet_higher_source_response_rank": int(np.linalg.matrix_rank(higher, tol=1e-9)),
            "latest_jet_higher_source_response_singular_values": np.linalg.svd(higher, compute_uv=False).tolist(),
            "higher_response_affinity_error": float(np.linalg.norm(affinity)),
            "unresolved_spatial_multiplier_projection_rank": int(np.linalg.matrix_rank(u[40:][remaining.SPATIAL_INDICES], tol=1e-9)),
            "source_controls": rows,
            "six_coordinates_not_proved_gauge_or_physical_modes": True,
            "zero_source_default_is_only_particular_solution_not_closure": True,
            "incompatible_rhs_rejected_above_declared_tolerance": True,
            "source_values_preserved_when_supplied": True,
            "pointwise_reduction_not_regional_evolution_or_wellposedness": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "normal_rank", "left_compatibility_dimension", "augmented_rank",
        "latest_jet_higher_source_response_rank", "source_controls")}))


if __name__ == "__main__":
    main()
