"""Centered spinor readouts with exact-rational fixed-map norm upper bounds."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "background_readout_parent", Path(__file__).with_name("HC_Cartan_Spin_Response_Operator_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Spin_Response_Operator_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def rational_sqrt_upper(value):
    """Small upward dyadic sqrt bound via integer arithmetic, not float sqrt."""
    value = Fraction(value)
    if value < 0:
        raise ValueError("Nonnegative rational required")
    if not value:
        return 0.
    exponent = (value.numerator.bit_length()-value.denominator.bit_length())//2
    unit_exponent = exponent-52
    unit_squared = Fraction(2)**(2*unit_exponent)
    scaled = value/unit_squared
    integer = math.isqrt(scaled.numerator//scaled.denominator)
    if integer*integer*scaled.denominator < scaled.numerator:
        integer += 1
    try:
        result = math.ldexp(float(integer), unit_exponent)
    except OverflowError as error:
        raise ValueError("Square-root bound is outside binary64 range") from error
    if not np.isfinite(result) or result <= 0 or Fraction.from_float(result)**2 < value:
        raise ValueError("No certified finite binary64 square-root upper bound")
    return result


def exact_matrix(array):
    return sp.Matrix([[sp.Rational(float(z.real))+sp.I*sp.Rational(float(z.imag)) for z in row]
                      for row in np.asarray(array, complex)])


def map_key(left, right, selector):
    values = [np.asarray(v, dtype=np.complex128) for v in (left, right, selector)]
    if [v.shape for v in values] != [(3, 4), (3, 4), (3, 3)] or not all(np.all(np.isfinite(v)) for v in values):
        raise ValueError("Finite three-channel spinor centers and selector required")
    if not np.allclose(values[2], values[2].conj().T, atol=1e-14, rtol=0):
        raise ValueError("Hermitian selector required")
    return tuple(v.tobytes() for v in values)


def frozen_map(left, right, selector, cache):
    key = map_key(left, right, selector)
    if key not in cache:
        bilinear = exact_matrix(left).H*exact_matrix(selector)*exact_matrix(right)
        response = prior.hermitian.RESPONSE
        rows = []
        for a in range(4):
            row = []
            for b in range(4):
                for d in range(4):
                    matrix = exact_matrix(response[a, b, d])
                    value = sp.expand(sum(bilinear[i, j]*matrix[i, j] for i in range(4) for j in range(4)))
                    row.append(sp.im(value))
            rows.append(row)
        exact = sp.Matrix(rows)
        gram = exact*exact.T
        row_bound = max(sum(abs(gram[i, j]) for j in range(4)) for i in range(4))
        upper = rational_sqrt_upper(Fraction(int(row_bound.p), int(row_bound.q)))
        cache[key] = {"matrix": np.array(exact.tolist(), float), "upper": upper,
            "exact_coefficients": [[str(v) for v in row] for row in exact.tolist()],
            "exact_gram_row_bound": str(row_bound), "input_key": key}
    return cache[key]


def centered_readout(left, right, omega, selector, cache):
    """Im(left^dagger Q response(omega) right), keeping every deviation term."""
    if np.any(np.imag(omega.coefficients)):
        raise ValueError("The expectation map here requires a real connection model")
    frozen = frozen_map(left.center, right.center, selector, cache)
    leading = omega.center.shape[:-2]
    if omega.center.shape[-2:] != (4, 4):
        raise ValueError("Last two connection axes must be four-dimensional")
    coefficients = omega.coefficients.reshape(70, -1, 16) @ frozen["matrix"].T
    fixed = T(coefficients.reshape(70, *leading, 4), frozen["upper"]*omega.tail)
    dl, dr = left-core.tensor(left.center), right-core.tensor(right.center)
    response = prior.response_model(omega)
    batched = full.reshape(response, (-1, 4, 4, 4))
    cross = (c("ui,uv,vj,naij->na", dl.conjugate(), selector, right.center, batched)
        +c("ui,uv,vj,naij->na", left.center.conj(), selector, dr, batched)
        +c("ui,uv,vj,naij->na", dl.conjugate(), selector, dr, batched)).imag()
    return fixed+full.reshape(cross, (*leading, 4))


def curl_model(fields, omega, cache):
    psi, dp, de = (fields[k] for k in ("psi", "dp", "de"))
    selector = general.prolong.Q
    curls = []
    for r in range(4):
        for s in range(r+1, 4):
            direct = c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, dp[s], general.prolong.WEIGHTS).imag().scale(2)
            connection = centered_readout(dp[r], psi, omega.value[s], selector, cache)-centered_readout(dp[s], psi, omega.value[r], selector, cache)
            derivative = centered_readout(psi, psi, omega.derivatives[r][s]-omega.derivatives[s][r], selector, cache).scale(.5)
            curls.append(direct+connection+derivative-de[r, :, s]+de[s, :, r])
    return full.vectorize(curls)


def coframe_model(fields, omega, volume, inverse, cache):
    psi, dp, lam = (fields[k] for k in ("psi", "dp", "lam"))
    partial = c("ui,muj,aij->am", psi.conjugate(), dp, general.prolong.WEIGHTS).imag()
    connection = centered_readout(psi, psi, omega.value, np.eye(3), cache).transpose(1, 0).scale(.5)
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    return prior.prior.factorized_euler(inverse, volume, partial+connection, mass,
        prior.prior.curvature_model(omega), lam)


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Spin_Response_Operator_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Spin-response report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), prior.hermitian.load_parent()
    case = control.load_case()
    cache = {}
    origin = full.field_models(case, common.RADIUS)
    psi, dp = origin["psi"].center, origin["dp"].center
    frozen_map(psi, psi, general.prolong.Q, cache)
    frozen_map(psi, psi, np.eye(3), cache)
    for r in range(4):
        frozen_map(dp[r], psi, general.prolong.Q, cache)

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, volume, inverse, ratios = full.connection_models(case[0], fields)
        curls = curl_model(fields, omega, cache)
        coframe, pieces = coframe_model(fields, omega, volume.value, inverse, cache)
        coefficients = np.asarray(previous["coefficients"]).copy()
        old = coefficients.copy()
        coefficients[:, 40:56] = coframe.coefficients.reshape(70, 16)
        coefficients[:, 56:] = curls.coefficients
        tails = [initial["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
        combined = T(coefficients, float(np.linalg.norm([*tails, coframe.tail, curls.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "coframe_tail_discrepancy": float(np.linalg.norm(actual[40:56].reshape(4, 4)-coframe.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "curl": full.summary(curls), "coframe": full.summary(coframe),
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "previous_curl_tail": previous["curl"]["tail_bound"], "previous_coframe_tail": previous["coframe"]["tail_bound"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)), "tail_diagnostics": pieces,
            **ratios, "coefficients": coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Background readout inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "fixed-spinor readout plus all variable deviations in unchanged curl/coframe equations",
        "reports": reports, "frozen_maps": [{k: v for k, v in entry.items() if k not in ("matrix", "input_key")} for entry in cache.values()],
        "no_coefficients_fitted_or_zeroed": True, "not_a_frozen_spinor_approximation": True,
        "only_fixed_map_norm_bounds_use_exact_rational_certificates": True,
        "not_a_full_outward_rounded_certificate": True, "not_exact_closure_or_regional_solution": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k not in ("input_sha256", "frozen_maps")}, indent=2))
