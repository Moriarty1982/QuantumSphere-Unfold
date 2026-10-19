"""Leading cubic residual gate with the existing origin jet frozen.

Richardson coefficient estimates, numerical ranks and negative controls only.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location("cubic_gate_common", Path(__file__).with_name("HC_Cartan_Common_Polynomial_Germ.py"))
common = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(common)
general, lower, tool = common.general, common.lower, common.tool
CUBICS = common.exponents(3)
DIRECTIONS = np.asarray(CUBICS, float)/3
ACTIVE = np.r_[np.arange(16*len(common.E5)), np.arange(40*len(common.E5), common.COUNT)]


def input_fingerprints():
    result = common.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def cubic_field_map(y):
    """Only E2 and lambda1 changes contribute to homogeneous residual degree 3."""
    result = np.zeros((440, len(ACTIVE)))
    e_stop = 16*len(common.E5)
    result[80:240, :e_stop] = np.vstack([
        common.block_map(common.E5, y, pair, common.RADIUS**2, 16) for pair in lower.PAIRS])
    result[376:, e_stop:] = np.vstack([
        common.block_map(common.L4, y, (r,), common.RADIUS, 16) for r in range(4)])
    return result


def cubic_stencil(function, step):
    """Extract a t^3 coefficient; constants, linear and quadratic terms cancel."""
    return (function(2*step)-2*function(step)+2*function(-step)-function(-2*step))/(12*step**3)


def cubic_estimates(function):
    cache = {}

    def value(t):
        if t not in cache:
            cache[t] = function(t)
        return cache[t]

    a, b, c = (cubic_stencil(value, h) for h in (.5, .25, .125))
    return (4*b-a)/3, (4*c-b)/3


def expand_coefficients(values):
    result = np.zeros(common.COUNT)
    result[ACTIVE] = values
    return result


def fit_report(system, target, coefficient_count):
    fitted = tool.fit_sources(system, target, tolerance=1e-10)
    singular, rank = system["singular"], system["rank"]
    return fitted["higher_increment"], {
        "shape": list(system["matrix"].shape), "rank": rank, "cutoff": system["cutoff"],
        "retained_minimum_singular": float(singular[rank-1]) if rank else None,
        "first_omitted_singular": float(singular[rank]) if rank < len(singular) else None,
        "full_linear_residual_norm": fitted["residual_norm"],
        "coefficient_norm": float(np.linalg.norm(fitted["higher_increment"])),
        "residual_by_block": {name: float(np.linalg.norm(fitted["residual"][:coefficient_count].reshape(20, 80)[:, begin:end]))
            for name, begin, end in (("constraint", 0, 16), ("probe", 16, 40), ("gravity", 40, 56),
                                     ("mixed_curl", 56, 68), ("spatial_curl", 68, 80))}}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    services = lower.prior.previous.first.prior.create_container().services()
    origin = general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    jacobian = services.cached("Cartan.cubic-gate-origin-jacobian/v1", {
        "sources": fingerprints, "prepared": prepared, "fields": {key: origin[key] for key in lower.prior.previous.FIELD_KEYS}},
        lambda: {"matrix": common.field_jacobian(prepared, origin)})["matrix"]
    _, original, _, _, _ = lower.source.neighborhood.load_data()
    reduction = lower.source.normal.build_reduction(prepared, original)
    coordinate_rows = common.normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)

    def residual(x, coefficients=None):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        if coefficients is not None:
            fields = common.unpack_fields(common.pack_fields(fields)+common.field_map(x) @ coefficients)
        return lower.lower_residual(prepared, fields)

    def baseline(direction):
        return cubic_estimates(lambda t: residual(common.RADIUS*t*direction))

    with ThreadPoolExecutor(max_workers=2) as pool:
        estimates = list(pool.map(baseline, DIRECTIONS))
    coarse = np.asarray([entry[0] for entry in estimates])
    fine = np.asarray([entry[1] for entry in estimates])
    vandermonde = np.array([[np.prod(y**np.asarray(power)) for power in CUBICS] for y in DIRECTIONS])
    coarse_coefficients = np.linalg.solve(vandermonde, coarse)
    fine_coefficients = np.linalg.solve(vandermonde, fine)
    maps = [cubic_field_map(y) for y in DIRECTIONS]
    matrix = np.vstack([jacobian @ item for item in maps])
    coordinate_matrix = np.vstack([coordinate_rows @ item for item in maps])
    target = coarse.ravel()
    fixed_system = tool.eliminate(np.vstack((matrix, coordinate_matrix)), services=services)
    fixed, fixed_report = fit_report(fixed_system, np.r_[target, np.zeros(320)], len(target))
    del fixed_system
    free_system = tool.eliminate(matrix, services=services)
    free, free_report = fit_report(free_system, target, len(target))
    del free_system

    def controls(name, values, report):
        coefficients = expand_coefficients(values)
        predicted = coarse+(matrix @ values).reshape(20, 80)
        report.update(predicted_cubic_norm=float(np.linalg.norm(predicted)),
                      fine_estimate_remainder_norm=float(np.linalg.norm(fine+(matrix @ values).reshape(20, 80))),
                      coordinate_cubic_drift=float(np.linalg.norm(coordinate_matrix @ values)))
        checks = []
        for y in (np.eye(4)[0], np.eye(4)[1], np.array([.3, .2, .1, .4])):
            actual, actual_fine = cubic_estimates(lambda t: residual(common.RADIUS*t*y, coefficients))
            base, _ = baseline(y)
            expected = base+jacobian @ cubic_field_map(y) @ values
            checks.append({"direction": y.tolist(), "actual_cubic_norm": float(np.linalg.norm(actual)),
                "response_prediction_error": float(np.linalg.norm(actual-expected)),
                "estimate_step_change": float(np.linalg.norm(actual-actual_fine)),
                "full_lower_at_radius": float(np.linalg.norm(residual(common.RADIUS*y, coefficients))),
                "full_lower_at_half_radius": float(np.linalg.norm(residual(common.RADIUS*y/2, coefficients)))})
        return dict(report, case=name, coefficients=coefficients.tolist(), checks=checks)

    cases = [controls("fixed_normal_coordinate_cubic", fixed, fixed_report), controls("free_coordinate_control", free, free_report)]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Cubic residual inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "cubic residual correction with original spinor fourth jet frozen",
        "cubic_monomials": 20, "active_coefficients": len(ACTIVE), "spinor_correction_zero": True,
        "vandermonde_condition": float(np.linalg.cond(vandermonde)),
        "baseline_cubic_sample_norm": float(np.linalg.norm(coarse)),
        "baseline_estimate_step_change": float(np.linalg.norm(coarse-fine)),
        "baseline_cubic_coefficient_norm": float(np.linalg.norm(coarse_coefficients)),
        "coefficient_estimate_step_change": float(np.linalg.norm(coarse_coefficients-fine_coefficients)),
        "cases": cases, "no_exact_or_regional_nonexistence_claim": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in ("input_sha256", "cases")}, indent=2))
    print(json.dumps([{key: value for key, value in case.items() if key != "coefficients"} for case in result["cases"]], indent=2))
