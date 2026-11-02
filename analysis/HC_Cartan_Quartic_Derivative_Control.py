"""Derivative-order controls and refreshed normal-chart majorants.

Sampled derivative agreement and float bounds, not regional PDE existence.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "quartic_derivative_parent", Path(__file__).with_name("HC_Cartan_Quartic_Residual_Extension.py"))
parent = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(parent)
common, general = parent.common, parent.general
prolongation = common.lower.prior.previous
uniform = prolongation.split.uniform


def input_fingerprints():
    result = parent.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Quartic_Residual_Extension.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def load_case():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Quartic_Residual_Extension.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != parent.input_fingerprints():
        raise ValueError("Quartic extension report has stale inputs")
    return (*parent.load_background(), np.asarray(report["coefficients"]))


def fields_and_higher(case, x, corrected=True):
    prepared, point, jets, full, ordinary, spinor, coefficients = case
    fields = parent.background_fields(prepared, point, jets, full, ordinary, spinor, x)
    higher = parent.background_higher(jets, full, ordinary, spinor, x)
    if corrected:
        fields = common.unpack_fields(common.pack_fields(fields)+parent.field_correction(x, coefficients))
        delta = parent.higher_correction(x, coefficients)
        higher = {key: higher[key]+delta[key] for key in higher}
    return fields, higher


def coordinate_derivative(function, x, step):
    """Five-point derivative of the actual shared-coordinate field residual."""
    rows = []
    for direction in np.eye(4):
        values = [function(x+k*step*direction) for k in (-2, -1, 1, 2)]
        rows.append((values[0]-8*values[1]+8*values[2]-values[3])/(12*step))
    return np.asarray(rows)


def sample_direction(case, y):
    prepared = case[0]

    def primary(x):
        fields, _ = fields_and_higher(case, x)
        return general.equations(prepared, fields)["vector"]

    samples = []
    for fraction in (1., .5, .25):
        x = common.RADIUS*fraction*np.asarray(y)
        fields, higher = fields_and_higher(case, x)
        first = prolongation.first_prolongation(prepared, fields, higher).reshape(4, 68)
        half = prolongation.first_prolongation(prepared, fields, higher, step=5e-5).reshape(4, 68)
        step = common.RADIUS*fraction/8
        direct = coordinate_derivative(primary, x, step)
        direct_half = coordinate_derivative(primary, x, step/2)
        extrapolated = (16*direct_half-direct)/15
        residual = general.equations(prepared, fields)["vector"]
        before_fields, before_higher = fields_and_higher(case, x, corrected=False)
        before = prolongation.first_prolongation(prepared, before_fields, before_higher).reshape(4, 68)
        before_residual = general.equations(prepared, before_fields)["vector"]
        samples.append({"fraction": fraction, "first_norm": float(np.linalg.norm(first)),
            "before_first_norm": float(np.linalg.norm(before)),
            "jet_step_change": float(np.linalg.norm(first-half)),
            "coordinate_step_change": float(np.linalg.norm(direct-direct_half)),
            "coordinate_derivative_discrepancy": float(np.linalg.norm(first-extrapolated)),
            "primary_norm": float(np.linalg.norm(residual)),
            "euler_fifth_remainder": float(np.linalg.norm(x @ first-5*residual)),
            "euler_fourth_before_remainder": float(np.linalg.norm(x @ before-4*before_residual)),
            "euler_fourth_after_remainder": float(np.linalg.norm(x @ first-4*residual))})
    return {"direction": np.asarray(y).tolist(), "samples": samples}


def polynomial_bound(powers, coefficients, amplitude, radius, order=0):
    """Triangle majorant on |x_i| <= radius, hence on the Euclidean ball.

    Ordered derivative tuples retain multiplicities of the full tensor norm.
    Complex realification has the same Frobenius norm as the complex block.
    """
    if not np.isfinite(radius) or radius < 0 or not isinstance(order, int) or order < 0:
        raise ValueError("Finite nonnegative radius and integer derivative order required")
    coefficients = np.asarray(coefficients)
    if coefficients.ndim != 2 or len(coefficients) != len(powers) or not np.all(np.isfinite(coefficients)):
        raise ValueError("Finite coefficient blocks must match powers")
    norms = np.linalg.norm(coefficients, axis=1)
    y = np.full(4, radius/common.RADIUS)
    values = [common.derivative_weights(powers, y, indices, amplitude) @ norms
              for indices in itertools.product(range(4), repeat=order)]
    return float(np.linalg.norm(values))


def correction_bounds(case, radius):
    ordinary, spinor, coefficients = case[4:]
    old_e, old_p = 16*len(common.E5), 40*len(common.E5)
    new_e, new_p = 16*len(parent.E6), 16*len(parent.E6)+24*len(parent.P5)
    terms = {"e": [(common.E5, ordinary[:old_e].reshape(-1, 16), common.RADIUS**2),
                    (parent.E6, coefficients[:new_e].reshape(-1, 16), common.RADIUS**2)],
             "psi": [(common.E5, ordinary[old_e:old_p].reshape(-1, 24), common.RADIUS),
                      (common.L4, spinor.reshape(-1, 24), common.RADIUS),
                      (parent.P5, coefficients[new_e:new_p].reshape(-1, 24), common.RADIUS)],
             "lam": [(common.L4, ordinary[old_p:].reshape(-1, 16), common.RADIUS),
                      (parent.P5, coefficients[new_p:].reshape(-1, 16), common.RADIUS)]}
    result = {}
    for name, order in (("e", 0), ("e", 1), ("psi", 0), ("psi", 1), ("lam", 0)):
        result[f"{name}{order}"] = sum(polynomial_bound(p, c, a, radius, order) for p, c, a in terms[name])
    return result


def refreshed_balls(case, radius):
    prepared, point, jets, full = case[:4]
    norms = uniform.coefficient_norms(prepared, point, jets, full)
    balls = uniform.field_balls(prepared, point, norms, radius)
    extra = correction_bounds(case, radius)
    for key, increment in (("e", extra["e0"]), ("de", extra["e1"]),
                           ("psi", extra["psi0"]), ("spatial_dp", extra["psi1"]), ("lam", extra["lam0"])):
        balls[key] = uniform.TensorBall(balls[key].center, balls[key].radius+increment)
    d = balls["e"].radius
    if d >= 1:
        raise ValueError("Changed coframe inverse majorant is unresolved")
    volume_change = 4*d+6*d*d+4*d**3+d**4
    volume_lower = (1-d)**4
    inverse_hessian_change = np.linalg.norm(prepared["inverse_hessian"])*(
        (2*d+d*d)/volume_lower+volume_change/volume_lower)
    balls["inverse"] = uniform.TensorBall(np.eye(4), d/(1-d))
    balls["volume"] = uniform.TensorBall(np.array(1.), volume_change)
    balls["hessian_inverse"] = uniform.TensorBall(prepared["inverse_hessian"], float(inverse_hessian_change))
    return balls, extra


def regularity_control(case):
    prepared = case[0]
    report = json.loads(Path(__file__).with_name("HC_Cartan_General_Normal_Chart.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != general.input_fingerprints():
        raise ValueError("General normal chart has stale inputs")
    rows = np.asarray(report["fixed_coordinate_rows"])
    center, _ = uniform.coefficient_matrix(prepared, **refreshed_balls(case, 0.)[0])
    sigma = float(np.linalg.svd(np.vstack((center.center, rows)), compute_uv=False)[-1])
    normal_sigma = float(np.linalg.svd(center.center, compute_uv=False)[39])
    trials = []
    radius = common.RADIUS
    for _ in range(70):
        balls, extra = refreshed_balls(case, radius)
        matrix, blocks = uniform.coefficient_matrix(prepared, **balls)
        trials.append({"radius": radius, "matrix_change_majorant": matrix.radius})
        if matrix.radius < min(sigma, normal_sigma)/2:
            break
        radius /= 2
    else:
        raise ValueError("Changed augmented-chart bound unresolved")
    checks = []
    for direction in (np.eye(4)[0], np.eye(4)[2], np.array([.5, -.5, .5, -.5])):
        fields, _ = fields_and_higher(case, radius*direction)
        actual = prolongation.split.direct_normal_matrix(prepared, fields)
        checks.append({"direction": direction.tolist(),
            "matrix_change": float(np.linalg.norm(actual-center.center, 2)),
            "augmented_minimum_singular": float(np.linalg.svd(np.vstack((actual, rows)), compute_uv=False)[-1])})
    return {"radius": radius, "center_augmented_minimum_singular": sigma,
        "matrix_change_majorant": matrix.radius, "block_majorants": blocks,
        "augmented_singular_lower_bound": sigma-matrix.radius,
        "inverse_norm_upper_bound": 1/(sigma-matrix.radius),
        "normal_singular_40_lower_bound": normal_sigma-matrix.radius,
        "correction_bounds_at_selected_radius": extra,
        "correction_bounds_at_residual_sampling_radius": correction_bounds(case, common.RADIUS),
        "selection_trials": trials, "sample_checks_not_the_proof": checks,
        "not_uniform_exact_normal_rank_or_compatibility_propagation": True,
        "not_outward_rounded_or_interval_certified": True}


def evaluate():
    fingerprints = input_fingerprints()
    case = load_case()
    directions = [np.eye(4)[0], np.eye(4)[1], np.eye(4)[2], np.array([.3, .2, .1, .4]), np.array([.2, -.3, .1, .4])]
    with ThreadPoolExecutor(max_workers=2) as pool:
        checks = list(pool.map(lambda y: sample_direction(case, y), directions))
    bounds = regularity_control(case)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Derivative control inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "quartic-corrected shared polynomial derivative and normal-chart controls",
        "checks": checks, "refreshed_normal_chart": bounds,
        "two_bounded_local_workers": True, "no_new_coefficients_fitted": True,
        "exact_parent_kernel_certificate_remains_authoritative": True,
        "not_regional_PDE_solution_or_all_order_convergence": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
