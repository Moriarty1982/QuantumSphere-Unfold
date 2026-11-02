"""Reprepare the fourth spinor jet in the retained origin-constraint kernel.

Leading cubic cancellation and direct origin checks, not regional existence.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location("cubic_spinor_gate", Path(__file__).with_name("HC_Cartan_Cubic_Residual_Gate.py"))
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)
common, general, tool = gate.common, gate.general, gate.tool


def input_fingerprints():
    result = gate.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def spinor_map(y):
    result = np.zeros((440, 840))
    raw = np.vstack([common.block_map(common.L4, y, (r,), common.RADIUS, 24) for r in range(4)])
    order = [24*r+12*part+j for part in range(2) for r in range(4) for j in range(12)]
    result[264:360] = raw[order]
    return result


def spinor_fields(x, coefficients):
    """Actual degree-four spinor value/first derivative, in the 440 packing."""
    result = spinor_map(np.asarray(x)/common.RADIUS) @ coefficients
    result[240:264] = common.block_map(common.L4, np.asarray(x)/common.RADIUS, (), common.RADIUS, 24) @ coefficients
    return result


def fourth_coordinates(coefficients, quads):
    blocks = coefficients.reshape(35, 24)
    return np.concatenate([common.derivative_weights(common.L4, np.zeros(4), quad, common.RADIUS) @ blocks for quad in quads])


def from_fourth_coordinates(values, quads):
    result = np.zeros((35, 24))
    for quad, block in zip(quads, np.asarray(values).reshape(35, 24)):
        power = tuple(quad.count(i) for i in range(4))
        factorial = math.prod(math.factorial(n) for n in power)
        result[common.L4.index(power)] = block*common.RADIUS**3/factorial
    return result.ravel()


def exact_readout_matrix(origin):
    def exact(value):
        value = complex(value)
        return sp.Rational(*value.real.as_integer_ratio())+sp.I*sp.Rational(*value.imag.as_integer_ratio())

    psi = sp.Matrix([[exact(value) for value in row] for row in origin["psi"]])
    selector = sp.Matrix([[exact(value) for value in row] for row in general.prolong.Q])
    weights = general.prior.joint.third.scalar.odd.readouts.dirac.WEIGHTS
    rows = []
    for weight in weights:
        matrix = sp.Matrix([[exact(value) for value in row] for row in weight])
        value = list(selector.T @ psi.conjugate() @ matrix)
        rows.append([sp.im(entry) for entry in value]+[sp.re(entry) for entry in value])
    return sp.Matrix(rows)


def exact_kernel_representative(origin, coefficients):
    """Use rational free coordinates and dependent pivots as the authority.

    Converting dependent pivots back to binary64 loses exact preservation; the
    rounded vector is used only for the regional numerical diagnostics.
    """
    matrix = exact_readout_matrix(origin)
    numerical = np.array(matrix.tolist(), dtype=float)
    remainder = numerical.copy()
    pivots = []
    for _ in range(4):
        index = int(np.argmax(np.linalg.norm(remainder, axis=0)))
        direction = remainder[:, index]/np.linalg.norm(remainder[:, index])
        remainder -= np.outer(direction, direction @ remainder)
        pivots.append(index)
    free = [i for i in range(24) if i not in pivots]
    pivot_map = -matrix[:, pivots].inv() @ matrix[:, free]
    rounded, free_values = [], []
    exact_zero = True
    for block in coefficients.reshape(35, 24):
        values = [sp.Rational(*float(block[i]).as_integer_ratio()) for i in free]
        dependent = pivot_map @ sp.Matrix(values)
        vector = [sp.S.Zero]*24
        for i, value in zip(free, values):
            vector[i] = value
        for i, value in zip(pivots, dependent):
            vector[i] = value
        exact_zero = exact_zero and matrix @ sp.Matrix(vector) == sp.zeros(4, 1)
        rounded.append([float(value) for value in vector])
        free_values.append([str(value) for value in values])
    certificate = {"readout_rank": int(matrix.rank()), "pivot_columns": pivots, "free_columns": free,
        "readout_matrix": [[str(value) for value in matrix.row(r)] for r in range(4)],
        "pivot_map": [[str(value) for value in pivot_map.row(r)] for r in range(4)],
        "free_monomial_coefficients": free_values,
        "all_35_readout_updates_exactly_zero": bool(exact_zero),
        "arithmetic_scope": "rational interpretation of the frozen binary64 psi, selector and weights"}
    return np.asarray(rounded).ravel(), certificate


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, lift_report = general.domain.load_data()
    cauchy = common.lower.prior.previous.first.prior
    services = cauchy.create_container().services()
    origin = general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    jacobian = services.cached("Cartan.cubic-gate-origin-jacobian/v1", {
        "sources": gate.input_fingerprints(), "prepared": prepared,
        "fields": {key: origin[key] for key in common.lower.prior.previous.FIELD_KEYS}},
        lambda: {"matrix": common.field_jacobian(prepared, origin)})["matrix"]
    _, original, _, _, _ = common.lower.source.neighborhood.load_data()
    reduction = common.lower.source.normal.build_reduction(prepared, original)
    coordinate_rows = common.normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)

    def baseline(y):
        def residual(t):
            fields = general.domain.temporal.fields(prepared, point, jets, full, common.RADIUS*t*y)
            return common.lower.lower_residual(prepared, fields)
        return gate.cubic_estimates(residual)

    with ThreadPoolExecutor(max_workers=2) as pool:
        estimates = list(pool.map(baseline, gate.DIRECTIONS))
    coarse, fine = (np.asarray([entry[i] for entry in estimates]) for i in (0, 1))
    spin_maps = [spinor_map(y) for y in gate.DIRECTIONS]
    response = np.vstack([jacobian @ item for item in spin_maps])
    preserve = response.reshape(20, 80, 840)[:, :16].reshape(320, 840)
    _, singular, right = services.svd(preserve, full_matrices=True)
    preserve_rank = int(np.sum(singular > max(1e-9, singular[0]*1e-10)))
    basis = right[preserve_rank:].T
    ordinary_maps = [gate.cubic_field_map(y) for y in gate.DIRECTIONS]
    ordinary = np.vstack([jacobian @ item for item in ordinary_maps])
    coordinate_ordinary = np.vstack([coordinate_rows @ item for item in ordinary_maps])
    coordinate_spinor = np.vstack([coordinate_rows @ item for item in spin_maps])
    coordinates = np.hstack((coordinate_ordinary, coordinate_spinor @ basis))
    matrix = np.hstack((ordinary, response @ basis))
    target = np.r_[coarse.ravel(), np.zeros(320)]
    system = tool.eliminate(np.vstack((matrix, coordinates)), services=services)
    fit = tool.fit_sources(system, target, tolerance=1e-10)
    ordinary_values = fit["higher_increment"][:len(gate.ACTIVE)]
    spinor = basis @ fit["higher_increment"][len(gate.ACTIVE):]
    ordinary_coefficients = gate.expand_coefficients(ordinary_values)

    # Refine preservation in the original unscaled 1114-row evaluator, not just
    # the tiny radius-scaled cubic symbol where roundoff can conceal a change.
    quads = list(cauchy.joint.third.diagnostic.QUADS)
    c = np.asarray(lift_report["fitted_coordinates"])
    old_highest = np.asarray(lift_report["fitted_highest"])
    lc = cauchy.joint.third.lc_cubic(prepared, point)
    old_vector = cauchy.evaluate_fields(prepared, point, c, old_highest, lc)["vector"]
    highest = cauchy.highest_matrix(prepared, services=services)
    raw_map = highest[-320:, 880:]
    raw_system = tool.eliminate(raw_map, services=services)
    origin_errors = []
    for _ in range(2):
        changed_highest = old_highest.copy()
        changed_highest[880:] += fourth_coordinates(spinor, quads)
        actual = cauchy.evaluate_fields(prepared, point, c, changed_highest, lc)["vector"]
        difference = actual[-320:]-old_vector[-320:]
        origin_errors.append(float(np.linalg.norm(difference)))
        spinor += from_fourth_coordinates(-raw_system["inverse"] @ difference, quads)
    changed_highest = old_highest.copy()
    changed_highest[880:] += fourth_coordinates(spinor, quads)
    new_vector = cauchy.evaluate_fields(prepared, point, c, changed_highest, lc)["vector"]
    float_refinement_norm = float(np.linalg.norm(new_vector))
    spinor, certificate = exact_kernel_representative(origin, spinor)
    changed_highest = old_highest.copy()
    changed_highest[880:] += fourth_coordinates(spinor, quads)
    new_vector = cauchy.evaluate_fields(prepared, point, c, changed_highest, lc)["vector"]
    symbol = np.zeros_like(raw_map)
    readout = np.array(exact_readout_matrix(origin).tolist(), dtype=float)
    for t, triple in enumerate(cauchy.joint.third.TRIPLES):
        for mu in range(4):
            q = quads.index(tuple(sorted((*triple, mu))))
            for a in range(4):
                symbol[16*t+4*a+mu, 24*q:24*q+24] = readout[a]
    predicted = coarse+(ordinary @ ordinary_values+response @ spinor).reshape(20, 80)

    def residual(x, corrected):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        if corrected:
            change = common.field_map(x) @ ordinary_coefficients+spinor_fields(x, spinor)
            fields = common.unpack_fields(common.pack_fields(fields)+change)
        return common.lower.lower_residual(prepared, fields)

    checks = []
    for y in (np.eye(4)[0], np.eye(4)[1], np.array([.3, .2, .1, .4]), np.array([.2, -.3, .1, .4])):
        actual, half = gate.cubic_estimates(lambda t: residual(common.RADIUS*t*y, True))
        base, _ = baseline(y)
        expected = base+jacobian @ gate.cubic_field_map(y) @ ordinary_values+jacobian @ spinor_map(y) @ spinor
        radii = [{"fraction": fraction,
                  "baseline": float(np.linalg.norm(residual(common.RADIUS*fraction*y, False))),
                  "corrected": float(np.linalg.norm(residual(common.RADIUS*fraction*y, True)))} for fraction in (1., .5, .25)]
        checks.append({"direction": y.tolist(), "actual_cubic_norm": float(np.linalg.norm(actual)),
                       "cubic_prediction_error": float(np.linalg.norm(actual-expected)),
                       "cubic_step_change": float(np.linalg.norm(actual-half)), "radius_checks": radii})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Cubic spinor inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "cubic-order reprepare with directly checked retained origin equations",
        "numerical_libraries": {"numpy": np.__version__, "sympy": sp.__version__},
        "spinor_preservation_rank": preserve_rank, "spinor_kernel_dimension": basis.shape[1],
        "coupled_rank": system["rank"], "linear_residual_norm": fit["residual_norm"],
        "predicted_cubic_norm_after_origin_refinement": float(np.linalg.norm(predicted)),
        "fine_cubic_remainder_norm": float(np.linalg.norm(fine+(ordinary @ ordinary_values+response @ spinor).reshape(20, 80))),
        "baseline_estimate_step_change": float(np.linalg.norm(coarse-fine)),
        "normal_coordinate_cubic_drift": float(np.linalg.norm(coordinate_ordinary @ ordinary_values+coordinate_spinor @ spinor)),
        "old_origin_1114_norm": float(np.linalg.norm(old_vector)),
        "new_origin_1114_norm": float(np.linalg.norm(new_vector)),
        "origin_1114_change_norm": float(np.linalg.norm(new_vector-old_vector)),
        "origin_C3_refinement_errors": origin_errors,
        "origin_after_float_refinement_norm": float_refinement_norm,
        "highest_nonC3_spinor_response_norm": float(np.linalg.norm(highest[:-320, 880:])),
        "origin_C3_symbol_match_error": float(np.linalg.norm(raw_map-symbol)),
        "exact_origin_preservation_certificate": certificate,
        "rounded_origin_passes_1e_minus_8": bool(np.linalg.norm(new_vector) < 1e-8),
        "spinor_fourth_jet_change_norm": float(np.linalg.norm(changed_highest[880:]-old_highest[880:])),
        "ordinary_coefficients": ordinary_coefficients.tolist(), "spinor_degree_four_coefficients": spinor.tolist(),
        "checks": checks, "no_regional_PDE_solution_or_all_order_extension": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in
        ("input_sha256", "ordinary_coefficients", "spinor_degree_four_coefficients", "exact_origin_preservation_certificate")}, indent=2))
