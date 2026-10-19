"""Quartic homogeneous extension of the cubic-reprepared polynomial field.

Coefficient estimates and independent controls, not regional PDE existence.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location("quartic_stable_kernel", Path(__file__).with_name("HC_Cartan_Kernel_Stable_Evaluation.py"))
stable = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stable)
prior, common, general = stable.prior, stable.common, stable.general
tool = prior.tool
E6, P5 = common.exponents(6), common.E5
COUNT = 16*len(E6)+40*len(P5)
QUARTICS = common.L4
DIRECTIONS = np.asarray(QUARTICS, float)/4


def input_fingerprints():
    result = stable.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def quartic_stencil(function, step):
    """Return the t^4 coefficient, cancelling all lower polynomial terms."""
    return (function(2*step)-4*function(step)+6*function(0.)
            -4*function(-step)+function(-2*step))/(24*step**4)


def quartic_estimates(function):
    cache = {}

    def value(t):
        if t not in cache:
            cache[t] = function(t)
        return cache[t]

    a, b, c = (quartic_stencil(value, h) for h in (1., .5, .25))
    return (4*b-a)/3, (4*c-b)/3


def derivative_blocks(y):
    e2 = np.vstack([common.block_map(E6, y, pair, common.RADIUS**2, 16) for pair in common.lower.PAIRS])
    raw = np.vstack([common.block_map(P5, y, (r,), common.RADIUS, 24) for r in range(4)])
    order = [24*r+12*part+j for part in range(2) for r in range(4) for j in range(12)]
    dl = np.vstack([common.block_map(P5, y, (r,), common.RADIUS, 16) for r in range(4)])
    return e2, raw[order], dl


def leading_response(jacobian, coordinate_rows, y):
    e2, dp, dl = derivative_blocks(y)
    return (np.hstack((jacobian[:, 80:240] @ e2, jacobian[:, 264:360] @ dp, jacobian[:, 376:] @ dl)),
            np.hstack((coordinate_rows[:, 80:240] @ e2, coordinate_rows[:, 264:360] @ dp, coordinate_rows[:, 376:] @ dl)))


def field_correction(x, coefficients):
    y = np.asarray(x)/common.RADIUS
    e_stop, p_stop = 16*len(E6), 16*len(E6)+24*len(P5)
    ec = coefficients[:e_stop].reshape(len(E6), 16)
    pc = coefficients[e_stop:p_stop].reshape(len(P5), 24)
    lc = coefficients[p_stop:].reshape(len(P5), 16)
    weights = common.derivative_weights
    e = weights(E6, y, (), common.RADIUS**2) @ ec
    de = np.array([weights(E6, y, (r,), common.RADIUS**2) @ ec for r in range(4)])
    e2 = np.array([weights(E6, y, pair, common.RADIUS**2) @ ec for pair in common.lower.PAIRS])
    psi = weights(P5, y, (), common.RADIUS) @ pc
    dp = np.array([weights(P5, y, (r,), common.RADIUS) @ pc for r in range(4)])
    dl = np.array([weights(P5, y, (r,), common.RADIUS) @ lc for r in range(4)])
    return np.r_[e, de.ravel(), e2.ravel(), psi, dp[:, :12].ravel(), dp[:, 12:].ravel(),
                 weights(P5, y, (), common.RADIUS) @ lc, dl.ravel()]


def higher_correction(x, coefficients):
    y = np.asarray(x)/common.RADIUS
    e_stop, p_stop = 16*len(E6), 16*len(E6)+24*len(P5)
    ec = coefficients[:e_stop].reshape(len(E6), 16)
    pc = coefficients[e_stop:p_stop].reshape(len(P5), 24)
    lc = coefficients[p_stop:].reshape(len(P5), 16)
    e3 = np.array([common.derivative_weights(E6, y, (r, s, t), common.RADIUS**2) @ ec
                   for r in range(4) for s in range(4) for t in range(4)])
    p2, l2 = [], []
    for r in range(4):
        for s in range(4):
            p2.append(general.prior.joint.prior.complexify(common.derivative_weights(P5, y, (r, s), common.RADIUS) @ pc, (3, 4)))
            l2.append(common.derivative_weights(P5, y, (r, s), common.RADIUS) @ lc)
    return {"e3": e3.reshape(4, 4, 4, 4, 4), "p2": np.array(p2).reshape(4, 4, 3, 4),
            "l2": np.array(l2).reshape(4, 4, 4, 4)}


def load_background():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Cubic_Spinor_Reprepare.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Cubic reprepare inputs changed")
    prepared, point, jets, _, full, _ = general.domain.load_data()
    certificate = report["exact_origin_preservation_certificate"]
    _, _, _, exact_blocks = stable.reconstruct_certificate(certificate)
    spinor = np.array([[float(value) for value in block] for block in exact_blocks]).ravel()
    ordinary = np.asarray(report["ordinary_coefficients"])
    return prepared, point, jets, full, ordinary, spinor


def background_fields(prepared, point, jets, full, ordinary, spinor, x):
    fields = general.domain.temporal.fields(prepared, point, jets, full, x)
    return common.unpack_fields(common.pack_fields(fields)+common.field_map(x) @ ordinary+prior.spinor_fields(x, spinor))


def background_higher(jets, full, ordinary, spinor, x):
    higher = common.lower.prior.previous.translated_higher(jets, full, x)
    delta = common.higher_correction(x, ordinary)
    pc = spinor.reshape(35, 24)
    for r in range(4):
        for s in range(4):
            real = common.derivative_weights(common.L4, np.asarray(x)/common.RADIUS, (r, s), common.RADIUS) @ pc
            delta["p2"][r, s] += general.prior.joint.prior.complexify(real, (3, 4))
    return {key: higher[key]+delta[key] for key in higher}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, full, ordinary, spinor = load_background()
    cauchy = common.lower.prior.previous.first.prior
    services = cauchy.create_container().services()
    origin = general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    jacobian = services.cached("Cartan.cubic-gate-origin-jacobian/v1", {
        "sources": prior.gate.input_fingerprints(), "prepared": prepared,
        "fields": {key: origin[key] for key in common.lower.prior.previous.FIELD_KEYS}},
        lambda: {"matrix": common.field_jacobian(prepared, origin)})["matrix"]
    _, original, _, _, _ = common.lower.source.neighborhood.load_data()
    reduction = common.lower.source.normal.build_reduction(prepared, original)
    rows = common.normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)

    def fields(x, coefficients=None):
        result = background_fields(prepared, point, jets, full, ordinary, spinor, x)
        return result if coefficients is None else common.unpack_fields(common.pack_fields(result)+field_correction(x, coefficients))

    def residual(x, coefficients=None):
        return common.lower.lower_residual(prepared, fields(x, coefficients))

    def baseline(y):
        return quartic_estimates(lambda t: residual(common.RADIUS*t*y))

    with ThreadPoolExecutor(max_workers=2) as pool:
        estimates = list(pool.map(baseline, DIRECTIONS))
    coarse, fine = (np.asarray([entry[i] for entry in estimates]) for i in (0, 1))
    augmented = np.empty((35*96, COUNT))
    for i, y in enumerate(DIRECTIONS):
        matrix, coordinate_matrix = leading_response(jacobian, rows, y)
        augmented[80*i:80*(i+1)] = matrix
        augmented[2800+16*i:2800+16*(i+1)] = coordinate_matrix
    target = np.r_[coarse.ravel(), np.zeros(560)]
    fine_target = np.r_[fine.ravel(), np.zeros(560)]

    def solve():
        # Cache the compact result only, not hundreds of MB of full SVD factors.
        system = tool.eliminate(augmented, services=services.backend)
        fit = tool.fit_sources(system, target, tolerance=1e-10)
        fine_fit = tool.fit_sources(system, fine_target, tolerance=1e-10)
        return {"coefficients": fit["higher_increment"], "singular": system["singular"],
                "rank": np.array(system["rank"]), "cutoff": np.array(system["cutoff"]),
                "residual": fit["residual"], "fine_coefficients": fine_fit["higher_increment"],
                "fine_fit_residual": fine_fit["residual"]}

    solved = services.cached("Cartan.quartic-leading-solve/v1", {
        "sources": fingerprints, "numpy": np.__version__, "matrix": augmented,
        "target": target, "fine_target": fine_target}, solve)
    coefficients = solved["coefficients"]
    residual_by_node = solved["residual"][:2800].reshape(35, 80)
    fine_remainder = fine-coarse+residual_by_node
    checks = []
    for y in (np.eye(4)[0], np.eye(4)[1], np.eye(4)[2], np.array([.3, .2, .1, .4]), np.array([.2, -.3, .1, .4])):
        actual, actual_fine = quartic_estimates(lambda t: residual(common.RADIUS*t*y, coefficients))
        baseline_quartic, _ = baseline(y)
        response, _ = leading_response(jacobian, rows, y)
        cubic_before, _ = prior.gate.cubic_estimates(lambda t: residual(common.RADIUS*t*y))
        cubic_after, _ = prior.gate.cubic_estimates(lambda t: residual(common.RADIUS*t*y, coefficients))
        radii = []
        for fraction in (1., .5, .25):
            x = common.RADIUS*fraction*y
            radii.append({"fraction": fraction, "before": float(np.linalg.norm(residual(x))),
                          "after": float(np.linalg.norm(residual(x, coefficients))),
                          "fine_fit_after": float(np.linalg.norm(residual(x, solved["fine_coefficients"]))),
                          "new_normal_coordinate_drift": float(np.linalg.norm(rows @ field_correction(x, coefficients)))})
        x = common.RADIUS*y
        higher = background_higher(jets, full, ordinary, spinor, x)
        new_higher = higher_correction(x, coefficients)
        before_first = common.lower.prior.previous.first_prolongation(prepared, fields(x), higher)
        after_first = common.lower.prior.previous.first_prolongation(prepared, fields(x, coefficients),
            {key: higher[key]+new_higher[key] for key in higher})
        checks.append({"direction": y.tolist(), "actual_quartic_norm": float(np.linalg.norm(actual)),
            "quartic_step_change": float(np.linalg.norm(actual-actual_fine)),
            "response_prediction_error": float(np.linalg.norm(actual-baseline_quartic-response @ coefficients)),
            "cubic_change_norm": float(np.linalg.norm(cubic_after-cubic_before)),
            "radius_checks": radii, "first_prolongation_before": float(np.linalg.norm(before_first)),
            "first_prolongation_after": float(np.linalg.norm(after_first))})
    vandermonde = np.array([[np.prod(y**np.asarray(power)) for power in QUARTICS] for y in DIRECTIONS])
    rank, singular = int(solved["rank"]), solved["singular"]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Quartic extension inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "quartic homogeneous correction of the shared cubic-reprepared field",
        "unknown_count": COUNT, "quartic_monomials": 35, "shape": list(augmented.shape),
        "rank": rank, "cutoff": float(solved["cutoff"]),
        "retained_minimum_singular": float(singular[rank-1]),
        "first_omitted_singular": float(singular[rank]) if rank < len(singular) else None,
        "retained_condition_estimate": float(singular[0]/singular[rank-1]),
        "coefficient_norm": float(np.linalg.norm(coefficients)),
        "fine_fit_coefficient_change_norm": float(np.linalg.norm(coefficients-solved["fine_coefficients"])),
        "fine_fit_residual_norm": float(np.linalg.norm(solved["fine_fit_residual"])),
        "baseline_quartic_sample_norm": float(np.linalg.norm(coarse)),
        "baseline_estimate_step_change": float(np.linalg.norm(coarse-fine)),
        "predicted_quartic_remainder_norm": float(np.linalg.norm(residual_by_node)),
        "fine_estimate_remainder_norm": float(np.linalg.norm(fine_remainder)),
        "fixed_coordinate_quartic_drift": float(np.linalg.norm(solved["residual"][2800:])),
        "vandermonde_condition": float(np.linalg.cond(vandermonde)),
        "new_polynomial_degrees": {"coframe": 6, "psi": 5, "multiplier": 5},
        "origin_and_cubic_preserved_by_degree": True, "exact_parent_kernel_certificate_remains_authoritative": True,
        "sample_extraction_can_reach_two_times_previous_radius": True,
        "coefficients": coefficients.tolist(), "checks": checks,
        "no_regional_PDE_solution_or_interval_certificate": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in ("input_sha256", "coefficients")}, indent=2))
