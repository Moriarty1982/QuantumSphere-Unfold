"""Constrained quartic correction using Taylor coefficients, not stencils."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "quartic_coefficient_audit", Path(__file__).with_name("HC_Cartan_Low_Order_Exterior_Compatibility.py"))
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
prior = audit.prior
full, core, common, control = prior.full, prior.core, prior.common, prior.control
quartic = control.parent
QUARTICS = tuple(common.exponents(4))


def input_fingerprints():
    result = audit.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Low_Order_Exterior_Compatibility.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def coefficient_response(jacobian, coordinate_rows):
    if jacobian.shape != (80, 440) or coordinate_rows.shape != (16, 440):
        raise ValueError("Expected 80 field-equation rows and 16 fixed coordinate rows")
    if not np.all(np.isfinite(jacobian)) or not np.all(np.isfinite(coordinate_rows)):
        raise ValueError("Finite response rows required")
    combined = np.vstack((jacobian, coordinate_rows))
    result = np.zeros((35, 96, quartic.COUNT))
    index = {p: i for i, p in enumerate(QUARTICS)}

    def add(powers, axes, input_columns, offset, components):
        for i, p in enumerate(powers):
            q, factor = list(p), 1
            for axis in axes:
                factor *= q[axis]
                q[axis] -= 1
            if factor == 0 or min(q) < 0:
                continue
            result[index[tuple(q)], :, offset+i*components:offset+(i+1)*components] += factor*combined[:, input_columns]

    for pair_index, pair in enumerate(common.lower.PAIRS):
        add(quartic.E6, pair, slice(80+16*pair_index, 96+16*pair_index), 0, 16)
    e_stop = 16*len(quartic.E6)
    p_stop = e_stop+24*len(quartic.P5)
    for r in range(4):
        real = np.r_[np.arange(264+12*r, 276+12*r), np.arange(312+12*r, 324+12*r)]
        add(quartic.P5, (r,), real, e_stop, 24)
        add(quartic.P5, (r,), slice(376+16*r, 392+16*r), p_stop, 16)
    return result.reshape(3360, quartic.COUNT)


def compact_fit(matrix, target, backend):
    left, singular, right = backend.svd(matrix, full_matrices=False)
    results = {"singular": singular}
    for label, relative in (("primary", 1e-10), ("tighter_cutoff", 1e-12)):
        cutoff = max(1e-9, relative*singular[0])
        rank = int(np.sum(singular > cutoff))
        increment = -right[:rank].T @ ((left[:, :rank].T @ target)/singular[:rank])
        results.update({label+"_increment": increment, label+"_rank": np.asarray(rank),
            label+"_cutoff": np.asarray(cutoff), label+"_residual": target+matrix @ increment,
            label+"_left_target": left[:, rank:].T @ target})
    return results


def residual_model(case, radius):
    fields, maps = full.field_models(case, radius), {}
    inverse, _ = prior.frame.factorization_certificate(case[0]["curvature_hessian"])
    omega, volume, coframe_inverse, ratios = prior.connection_models(case[0], fields, inverse, {})
    constitutive, _ = prior.constraint_core.constraint_model(fields, omega, maps)
    probe, _ = prior.probe_core.probe_model(fields, omega, volume, coframe_inverse)
    coframe, _ = prior.implicit.prior.coframe_model(fields, omega, volume.value, coframe_inverse, maps)
    curl, _ = prior.projector.curl_model(fields, omega, maps)
    return full.vectorize([constitutive, probe, coframe, curl]), ratios


def constraint_source_audit(before, after):
    derivative = audit.derivative_matrix(4, 1).astype(float)
    left, singular, right = np.linalg.svd(derivative, full_matrices=False)
    rank = int(np.sum(singular > 1e-12))
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    old = audit.homogeneous(before, 4, slice(0, 16))
    new = audit.homogeneous(after, 4, slice(0, 16))
    source = derivative @ old
    necessary = inverse @ source
    return {"coefficient_differential_shape": list(derivative.shape),
        "numerical_rank_per_constitutive_component": rank,
        "unchanged_d_C4_source_norm": float(np.linalg.norm(source)),
        "d_C4_change_norm": float(np.linalg.norm(derivative @ (new-old))),
        "frozen_source_minimum_constitutive_norm_estimate": float(np.linalg.norm(necessary)),
        "actual_remaining_constitutive_norm": float(np.linalg.norm(new)),
        "remaining_constitutive_minus_known_source_norm": float(np.linalg.norm(new-necessary)),
        "only_known_constitutive_identity_attributed_not_entire_left_kernel": True,
        "conditional_float_source_floor_not_exact_physical_obstruction": True}


def evaluate():
    fingerprints = input_fingerprints()
    previous = json.loads(Path(__file__).with_name("HC_Cartan_Centered_Spinor_Source_Bound.json").read_text(encoding="utf-8"))
    if previous["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Centered source coefficients have stale inputs")
    exterior = json.loads(Path(__file__).with_name("HC_Cartan_Low_Order_Exterior_Compatibility.json").read_text(encoding="utf-8"))
    if exterior["input_sha256"] != audit.input_fingerprints():
        raise ValueError("Exterior compatibility report has stale inputs")
    case = control.load_case()
    services = common.lower.prior.previous.first.prior.create_container().services()
    prepared, point, jets, background, _, _, _ = case
    origin = prior.general.domain.temporal.fields(prepared, point, jets, background, np.zeros(4))
    jacobian = services.cached("Cartan.cubic-gate-origin-jacobian/v1", {
        "sources": quartic.prior.gate.input_fingerprints(), "prepared": prepared,
        "fields": {key: origin[key] for key in common.lower.prior.previous.FIELD_KEYS}},
        lambda: {"matrix": common.field_jacobian(prepared, origin)})["matrix"]
    _, original, _, _, _ = common.lower.source.neighborhood.load_data()
    reduction = common.lower.source.normal.build_reduction(prepared, original)
    coordinates = common.normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)
    matrix = coefficient_response(jacobian, coordinates)
    before = np.asarray(previous["reports"][0]["coefficients"])
    indices = [core.INDEX[p] for p in QUARTICS]
    target = np.column_stack((before[indices], np.zeros((35, 16)))).ravel()
    map_checks = []
    for y in (np.eye(4)[0], np.array([.2, -.3, .1, .4])):
        weights = np.asarray([np.prod(y**np.asarray(p)) for p in QUARTICS])
        coefficient_map = np.einsum("m,mij->ij", weights, matrix.reshape(35, 96, -1))
        field, coordinate = quartic.leading_response(jacobian, coordinates, y)
        map_checks.append({"direction": y.tolist(),
            "independent_node_map_discrepancy": float(np.linalg.norm(coefficient_map-np.vstack((field, coordinate))))})
    print("Quartic coefficient response prepared; starting compact cached SVD", flush=True)
    solved = services.cached("Cartan.quartic-coefficient-refinement/v1", {
        "matrix": matrix, "target": target, "backend": services.backend.identity,
        "cutoff_policy": {"absolute": 1e-9, "primary_relative": 1e-10, "alternative_relative": 1e-12}},
        lambda: compact_fit(matrix, target, services.backend))
    increment = solved["primary_increment"]
    candidate = (*case[:-1], case[-1]+increment)
    predicted = solved["primary_residual"].reshape(35, 96)

    def run(report):
        radius = report["radius"]
        updated, ratios = residual_model(candidate, radius)
        old_coefficients = np.asarray(report["coefficients"])
        scale = (radius/common.RADIUS)**4
        actual_quartic = updated.coefficients[indices]
        lower = np.flatnonzero(core.DEGREES < 4)
        samples = []
        for y in (np.eye(4)[0], np.eye(4)[1], np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            old_fields, _ = control.fields_and_higher(case, radius*y)
            new_fields, _ = control.fields_and_higher(candidate, radius*y)
            actual = common.lower.lower_residual(prepared, new_fields)
            samples.append({"direction": y.tolist(),
                "before_norm": float(np.linalg.norm(common.lower.lower_residual(prepared, old_fields))),
                "after_norm": float(np.linalg.norm(actual)),
                "Taylor_tail_discrepancy": float(np.linalg.norm(actual-updated.evaluate(y))),
                "new_coordinate_drift": float(np.linalg.norm(coordinates @ quartic.field_correction(radius*y, increment)))})
        return {"radius": radius, "before_quartic_norm": float(np.linalg.norm(old_coefficients[indices])),
            "after_quartic_norm": float(np.linalg.norm(actual_quartic)),
            "coefficient_response_prediction_error": float(np.linalg.norm(actual_quartic-scale*predicted[:, :80])),
            "lower_order_coefficient_change": float(np.linalg.norm(updated.coefficients[lower]-old_coefficients[lower])),
            "known_constitutive_source_attribution": constraint_source_audit(old_coefficients, updated.coefficients),
            "quartic_norm_by_block": {name: float(np.linalg.norm(actual_quartic[:, a:b])) for name, a, b in
                (("constraint", 0, 16), ("probe", 16, 40), ("coframe", 40, 56), ("curl", 56, 80))},
            "refreshed_combined_enclosure": full.summary(updated),
            "previous_combined_enclosure": report["combined"], "sample_controls_not_a_regional_proof": samples,
            "coefficients": updated.coefficients.tolist(), **ratios}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, previous["reports"]))
    old_origin, old_higher = control.fields_and_higher(case, np.zeros(4))
    new_origin, new_higher = control.fields_and_higher(candidate, np.zeros(4))
    origin_change = float(np.linalg.norm(common.pack_fields(old_origin)-common.pack_fields(new_origin)))
    higher_change = float(np.linalg.norm([np.linalg.norm(old_higher[k]-new_higher[k]) for k in old_higher]))
    rank, singular = int(solved["primary_rank"]), solved["singular"]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Quartic refinement inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "matrix_shape": list(matrix.shape), "rank": rank, "cutoff": float(solved["primary_cutoff"]),
        "singular_values": singular.tolist(), "retained_condition_estimate": float(singular[0]/singular[rank-1]),
        "baseline_quartic_target_norm": float(np.linalg.norm(target)),
        "linear_fit_residual_norm": float(np.linalg.norm(solved["primary_residual"])),
        "left_compatibility_target_norm": float(np.linalg.norm(solved["primary_left_target"])),
        "coordinate_increment_norm": float(np.linalg.norm(predicted[:, 80:])),
        "increment_norm": float(np.linalg.norm(increment)), "previous_quartic_field_coefficient_norm": float(np.linalg.norm(case[-1])),
        "increment": increment.tolist(), "candidate_quartic_field_coefficients": candidate[-1].tolist(),
        "alternative_cutoff_rank": int(solved["tighter_cutoff_rank"]),
        "alternative_cutoff_residual_norm": float(np.linalg.norm(solved["tighter_cutoff_residual"])),
        "alternative_cutoff_increment_change": float(np.linalg.norm(increment-solved["tighter_cutoff_increment"])),
        "origin_field_change": origin_change, "origin_higher_change": higher_change,
        "coefficient_to_node_response_controls": map_checks, "reports": reports,
        "target_from_Taylor_coefficients_not_finite_difference_extraction": True,
        "frozen_origin_highest_derivative_jacobian_is_still_binary64": True,
        "coordinate_increment_fixed_to_zero_not_released": True,
        "no_previous_regional_bound_reused_for_changed_polynomial": True,
        "candidate_does_not_replace_authoritative_parent_polynomial": True,
        "no_exact_zero_low_order_closure_or_regional_existence_claim": True,
        "inherited_rounded_origin_failure_not_repaired_or_hidden": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_sha256", "singular_values", "increment",
        "candidate_quartic_field_coefficients", "reports")}, indent=2))
    print(json.dumps([{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]], indent=2))
