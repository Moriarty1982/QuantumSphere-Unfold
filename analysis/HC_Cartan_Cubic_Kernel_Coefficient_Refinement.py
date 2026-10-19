"""Cubic coefficient repair in rational kernel coordinates, then refresh quartic."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cubic_kernel_coefficient_parent", Path(__file__).with_name("HC_Cartan_Quartic_Coefficient_Refinement.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
core, common, control = prior.core, prior.common, prior.control
quartic, stable = prior.quartic, prior.quartic.stable
reprepare = stable.prior
CUBICS = tuple(common.exponents(3))
E_COUNT, FREE_COUNT, L_COUNT = 16*len(common.E5), 35*20, 16*len(common.L4)
COUNT = E_COUNT+FREE_COUNT+L_COUNT


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Quartic_Coefficient_Refinement.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def kernel_basis(certificate):
    readout, pivot_map, _, _ = stable.reconstruct_certificate(certificate)
    basis = [[Fraction(0) for _ in range(20)] for _ in range(24)]
    for j, index in enumerate(certificate["free_columns"]):
        basis[index][j] = Fraction(1)
    for k, index in enumerate(certificate["pivot_columns"]):
        basis[index] = pivot_map[k].copy()
    if any(sum(row[i]*basis[i][j] for i in range(24)) for row in readout for j in range(20)):
        raise ValueError("Exact free-coordinate basis leaves the origin readout kernel")
    return np.array([[float(v) for v in row] for row in basis]), basis


def update_kernel_certificate(certificate, increment):
    increment = np.asarray(increment)
    if increment.shape != (35, 20) or not np.all(np.isfinite(increment)):
        raise ValueError("Finite 35-by-20 free-coordinate increment required")
    _, _, old_free, old_blocks = stable.reconstruct_certificate(certificate)
    new_free = [[str(old_free[i][j]+Fraction.from_float(float(increment[i, j]))) for j in range(20)] for i in range(35)]
    updated = {**certificate, "free_monomial_coefficients": new_free}
    readout, _, _, blocks = stable.reconstruct_certificate(updated)
    delta = [[a-b for a, b in zip(new, old)] for new, old in zip(blocks, old_blocks)]
    if any(v for block in stable.contract_readouts(readout, delta) for v in block):
        raise ValueError("Exact updated monomials do not preserve the origin kernel")
    return updated, blocks, delta


def coefficient_response(jacobian, coordinate_rows, basis):
    if jacobian.shape != (80, 440) or coordinate_rows.shape != (16, 440) or basis.shape != (24, 20):
        raise ValueError("Cubic response requires 80+16 rows and a 24-by-20 spinor kernel basis")
    if not all(np.all(np.isfinite(v)) for v in (jacobian, coordinate_rows, basis)):
        raise ValueError("Finite cubic response inputs required")
    combined, result = np.vstack((jacobian, coordinate_rows)), np.zeros((20, 96, COUNT))
    index = {p: i for i, p in enumerate(CUBICS)}

    def add(powers, axes, columns, offset, components, transform=None):
        response = combined[:, columns]
        if transform is not None:
            response = response @ transform
        for i, p in enumerate(powers):
            q, factor = list(p), 1
            for axis in axes:
                factor *= q[axis]
                q[axis] -= 1
            if factor == 0 or min(q) < 0:
                continue
            result[index[tuple(q)], :, offset+i*components:offset+(i+1)*components] += factor*response

    for i, pair in enumerate(common.lower.PAIRS):
        add(common.E5, pair, slice(80+16*i, 96+16*i), 0, 16)
    for r in range(4):
        columns = np.r_[np.arange(264+12*r, 276+12*r), np.arange(312+12*r, 324+12*r)]
        add(common.L4, (r,), columns, E_COUNT, 20, basis)
        add(common.L4, (r,), slice(376+16*r, 392+16*r), E_COUNT+FREE_COUNT, 16)
    return result.reshape(1920, COUNT)


def apply_cubic_increment(case, increment, certificate):
    increment = np.asarray(increment)
    if increment.shape != (COUNT,) or not np.all(np.isfinite(increment)):
        raise ValueError("Finite cubic free-coordinate increment required")
    updated, blocks, delta = update_kernel_certificate(certificate, increment[E_COUNT:E_COUNT+FREE_COUNT].reshape(35, 20))
    ordinary = case[4].copy()
    ordinary[:E_COUNT] += increment[:E_COUNT]
    ordinary[40*len(common.E5):] += increment[E_COUNT+FREE_COUNT:]
    spinor = np.array([[float(v) for v in row] for row in blocks]).ravel()
    return (*case[:4], ordinary, spinor, case[-1].copy()), updated, delta


def fit(matrix, target, services, operation):
    return services.cached(operation, {"matrix": matrix, "target": target, "backend": services.backend.identity,
        "cutoff_policy": {"absolute": 1e-9, "primary_relative": 1e-10, "alternative_relative": 1e-12}},
        lambda: prior.compact_fit(matrix, target, services.backend))


def fit_summary(solved):
    rank, singular = int(solved["primary_rank"]), solved["singular"]
    return {"rank": rank, "cutoff": float(solved["primary_cutoff"]),
        "retained_condition_estimate": float(singular[0]/singular[rank-1]) if rank else None,
        "linear_residual_norm": float(np.linalg.norm(solved["primary_residual"])),
        "left_compatibility_target_norm": float(np.linalg.norm(solved["primary_left_target"])),
        "increment_norm": float(np.linalg.norm(solved["primary_increment"])),
        "alternative_rank": int(solved["tighter_cutoff_rank"]),
        "alternative_residual_norm": float(np.linalg.norm(solved["tighter_cutoff_residual"])),
        "alternative_increment_change": float(np.linalg.norm(solved["primary_increment"]-solved["tighter_cutoff_increment"])),
        "singular_values": singular.tolist()}


def origin_kernel_controls(case, candidate, certificate, delta):
    cauchy = common.lower.prior.previous.first.prior
    quads, triples = list(cauchy.joint.third.diagnostic.QUADS), list(cauchy.joint.third.TRIPLES)
    readout, _, _, total_blocks = stable.reconstruct_certificate(certificate)
    exact_delta = stable.c3_entries(stable.contract_readouts(readout, stable.exact_fourth_update(delta, quads)), quads, triples)
    exact_total = stable.c3_entries(stable.contract_readouts(readout, stable.exact_fourth_update(total_blocks, quads)), quads, triples)
    prepared, point, _, _, _, lift = prior.prior.general.domain.load_data()
    coordinates, highest = np.asarray(lift["fitted_coordinates"]), np.asarray(lift["fitted_highest"])
    lc = cauchy.joint.third.lc_cubic(prepared, point)
    anchor = cauchy.evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
    raw = []
    for value in (case[5], candidate[5]):
        changed = highest.copy()
        changed[880:] += reprepare.fourth_coordinates(value, quads)
        raw.append(float(np.linalg.norm(cauchy.evaluate_fields(prepared, point, coordinates, changed, lc)["vector"])))
    old_fields, old_higher = control.fields_and_higher(case, np.zeros(4))
    new_fields, new_higher = control.fields_and_higher(candidate, np.zeros(4))
    return {"exact_parametric_C3_increment_zero": all(v == 0 for v in exact_delta),
        "exact_parametric_total_C3_update_zero": all(v == 0 for v in exact_total), "exact_C3_rows_checked": len(exact_delta),
        "origin_lower_field_change": float(np.linalg.norm(common.pack_fields(new_fields)-common.pack_fields(old_fields))),
        "origin_higher_through_used_orders_change": float(np.linalg.norm([np.linalg.norm(new_higher[k]-old_higher[k]) for k in old_higher])),
        "inherited_binary64_anchor_1114_norm": float(np.linalg.norm(anchor)),
        "raw_rounded_before_1114_norm": raw[0], "raw_rounded_after_1114_norm": raw[1],
        "raw_rounded_negative_controls_not_replaced_by_zero": True,
        "not_a_new_high_precision_nonlinear_origin_solve": True}


def evaluate():
    fingerprints = input_fingerprints()
    previous = json.loads(Path(__file__).with_name("HC_Cartan_Quartic_Coefficient_Refinement.json").read_text(encoding="utf-8"))
    if previous["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Quartic coefficient refinement inputs are stale")
    old_case = control.load_case()
    case = (*old_case[:-1], np.asarray(previous["candidate_quartic_field_coefficients"]))
    origin_report = json.loads(Path(__file__).with_name("HC_Cartan_Cubic_Spinor_Reprepare.json").read_text(encoding="utf-8"))
    if origin_report["input_sha256"] != reprepare.input_fingerprints():
        raise ValueError("Origin kernel certificate has stale inputs")
    certificate = origin_report["exact_origin_preservation_certificate"]
    basis, _ = kernel_basis(certificate)
    _, _, _, old_blocks = stable.reconstruct_certificate(certificate)
    if not np.array_equal(case[5], np.array([[float(v) for v in row] for row in old_blocks]).ravel()):
        raise ValueError("Current spinor polynomial does not match the kernel certificate")
    services = common.lower.prior.previous.first.prior.create_container().services()
    prepared, point, jets, background, _, _, _ = case
    origin = prior.prior.general.domain.temporal.fields(prepared, point, jets, background, np.zeros(4))
    expected_readout = [[Fraction(str(v)) for v in row] for row in reprepare.exact_readout_matrix(origin).tolist()]
    if expected_readout != stable.rational_matrix(certificate["readout_matrix"], 4, 24):
        raise ValueError("Kernel certificate does not match the actual frozen origin readout")
    jacobian = services.cached("Cartan.cubic-gate-origin-jacobian/v1", {
        "sources": reprepare.gate.input_fingerprints(), "prepared": prepared,
        "fields": {key: origin[key] for key in common.lower.prior.previous.FIELD_KEYS}},
        lambda: {"matrix": common.field_jacobian(prepared, origin)})["matrix"]
    _, original, _, _, _ = common.lower.source.neighborhood.load_data()
    reduction = common.lower.source.normal.build_reduction(prepared, original)
    coordinates = common.normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)
    matrix = coefficient_response(jacobian, coordinates, basis)
    indices3, indices4 = [core.INDEX[p] for p in CUBICS], [core.INDEX[p] for p in prior.QUARTICS]
    before = np.asarray(previous["reports"][0]["coefficients"])
    target = np.column_stack((before[indices3], np.zeros((20, 16)))).ravel()
    print("Cubic coefficient system prepared; resolving compact cached SVD", flush=True)
    cubic = fit(matrix, target, services, "Cartan.cubic-kernel-coefficient-refinement/v1")
    intermediate, certificate, delta = apply_cubic_increment(case, cubic["primary_increment"], certificate)
    middle, _ = prior.residual_model(intermediate, common.RADIUS)
    matrix4 = prior.coefficient_response(jacobian, coordinates)
    target4 = np.column_stack((middle.coefficients[indices4], np.zeros((35, 16)))).ravel()
    print("Cubic candidate recomputed; refreshing quartic coefficients", flush=True)
    fourth = fit(matrix4, target4, services, "Cartan.quartic-coefficient-refinement/v1")
    candidate = (*intermediate[:-1], intermediate[-1]+fourth["primary_increment"])
    predicted3 = cubic["primary_residual"].reshape(20, 96)[:, :80]
    predicted4 = fourth["primary_residual"].reshape(35, 96)[:, :80]

    def run(report):
        radius, old = report["radius"], np.asarray(report["coefficients"])
        updated, ratios = prior.residual_model(candidate, radius)
        third, last = updated.coefficients[indices3], updated.coefficients[indices4]
        checks = []
        for y in (np.eye(4)[0], np.eye(4)[1], np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            old_fields, _ = control.fields_and_higher(case, radius*y)
            new_fields, _ = control.fields_and_higher(candidate, radius*y)
            actual = common.lower.lower_residual(prepared, new_fields)
            checks.append({"direction": y.tolist(), "before_norm": float(np.linalg.norm(common.lower.lower_residual(prepared, old_fields))),
                "after_norm": float(np.linalg.norm(actual)),
                "Taylor_tail_discrepancy": float(np.linalg.norm(actual-updated.evaluate(y)))})
        lower = np.flatnonzero(core.DEGREES < 3)
        return {"radius": radius, "before_cubic_norm": float(np.linalg.norm(old[indices3])),
            "after_cubic_norm": float(np.linalg.norm(third)), "before_quartic_norm": float(np.linalg.norm(old[indices4])),
            "after_quartic_norm": float(np.linalg.norm(last)),
            "lower_than_cubic_coefficient_change": float(np.linalg.norm(updated.coefficients[lower]-old[lower])),
            "cubic_prediction_error": float(np.linalg.norm(third-(radius/common.RADIUS)**3*predicted3)),
            "quartic_prediction_error": float(np.linalg.norm(last-(radius/common.RADIUS)**4*predicted4)),
            "cubic_norm_by_block": {name: float(np.linalg.norm(third[:, a:b])) for name, a, b in
                (("constraint", 0, 16), ("probe", 16, 40), ("coframe", 40, 56), ("curl", 56, 80))},
            "quartic_norm_by_block": {name: float(np.linalg.norm(last[:, a:b])) for name, a, b in
                (("constraint", 0, 16), ("probe", 16, 40), ("coframe", 40, 56), ("curl", 56, 80))},
            "refreshed_combined_enclosure": prior.full.summary(updated), "coefficients": updated.coefficients.tolist(),
            "sample_controls_not_a_regional_proof": checks, **ratios}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, previous["reports"]))
    controls = origin_kernel_controls(case, candidate, certificate, delta)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Cubic kernel refinement inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "cubic_matrix_shape": list(matrix.shape), "cubic_fit": fit_summary(cubic), "quartic_refresh": fit_summary(fourth),
        "cubic_free_increment": cubic["primary_increment"].tolist(), "quartic_increment": fourth["primary_increment"].tolist(),
        "cubic_coordinate_increment_norm": float(np.linalg.norm(cubic["primary_residual"].reshape(20, 96)[:, 80:])),
        "quartic_coordinate_increment_norm": float(np.linalg.norm(fourth["primary_residual"].reshape(35, 96)[:, 80:])),
        "intermediate_cubic_norm": float(np.linalg.norm(middle.coefficients[indices3])),
        "intermediate_quartic_norm_before_refresh": float(np.linalg.norm(middle.coefficients[indices4])),
        "updated_exact_kernel_certificate": certificate, "origin_controls": controls,
        "candidate_ordinary_coefficients": candidate[4].tolist(), "candidate_rounded_spinor_coefficients": candidate[5].tolist(),
        "candidate_quartic_coefficients": candidate[6].tolist(), "reports": reports,
        "exact_free_pivot_representation_authoritative": True, "all_bounds_and_samples_use_rounded_representative": True,
        "kernel_readout_checked_against_actual_frozen_origin": True,
        "exact_origin_identity_and_rounded_neighborhood_are_not_a_single_certified_solution": True,
        "coordinate_constraints_not_released": True, "quartic_system_refreshed_after_cubic_change": True,
        "no_exact_low_order_closure_regional_solution_or_native_identification": True,
        "parent_polynomials_reports_and_main_TeX_PDF_unchanged": True}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"cubic_fit": {k: v for k, v in result["cubic_fit"].items() if k != "singular_values"},
        "quartic_refresh": {k: v for k, v in result["quartic_refresh"].items() if k != "singular_values"},
        "origin_controls": result["origin_controls"], "reports": [{k: v for k, v in r.items() if k != "coefficients"}
            for r in result["reports"]]}, indent=2))
