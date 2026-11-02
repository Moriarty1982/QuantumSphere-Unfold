"""Exact scaled-projector Gram identities for the fixed curl readout maps."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "projector_readout_parent", Path(__file__).with_name("HC_Cartan_Joint_Probe_Response_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
connection_core = prior.prior.prior
readout = connection_core.readout
exterior_core = connection_core.prior.prior
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Joint_Probe_Response_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def certified_gram_norm(exact):
    if exact.rows != 4 or any(v.is_Rational is not True for v in exact):
        raise ValueError("Rational four-output exact matrix required")
    gram = exact*exact.T
    scale = sp.trace(gram)/3
    row_bound = max(sum(abs(gram[i, j]) for j in range(4)) for i in range(4))
    identity = gram*gram == scale*gram
    bound = scale if identity else row_bound
    upper = readout.rational_sqrt_upper(Fraction(int(bound.p), int(bound.q)))
    return {"upper": upper, "projector_identity_verified": identity,
        "exact_scale": str(scale), "exact_gram_row_bound": str(row_bound),
        "exact_squared_norm_or_upper": str(bound)}


def frozen_map(left, right, selector, cache):
    key = readout.map_key(left, right, selector)
    if key not in cache:
        old = readout.frozen_map(left, right, selector, {})
        exact = sp.Matrix([[sp.Rational(v) for v in row] for row in old["exact_coefficients"]])
        cache[key] = {**old, **certified_gram_norm(exact), "previous_upper": old["upper"]}
    return cache[key]


def centered_readout(left, right, omega, selector, cache):
    if np.any(omega.coefficients.imag) or omega.center.shape[-2:] != (4, 4):
        raise ValueError("Real four-dimensional lower connection model required")
    frozen = frozen_map(left.center, right.center, selector, cache)
    leading = omega.center.shape[:-2]
    coefficients = omega.coefficients.reshape(70, -1, 16) @ frozen["matrix"].T
    fixed = T(coefficients.reshape(70, *leading, 4), frozen["upper"]*omega.tail)
    dl, dr = left-core.tensor(left.center), right-core.tensor(right.center)
    response = readout.prior.response_model(omega)
    batched = full.reshape(response, (-1, 4, 4, 4))
    cross = (c("ui,uv,vj,naij->na", dl.conjugate(), selector, right.center, batched)
        +c("ui,uv,vj,naij->na", left.center.conj(), selector, dr, batched)
        +c("ui,uv,vj,naij->na", dl.conjugate(), selector, dr, batched)).imag()
    return fixed+full.reshape(cross, (*leading, 4))


def curl_model(fields, omega, cache):
    psi, dp, de = (fields[k] for k in ("psi", "dp", "de"))
    selector = general.prolong.Q
    parts = []
    for r, s in exterior_core.PAIRS:
        direct = c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, dp[s], general.prolong.WEIGHTS).imag().scale(2)
        connection = (centered_readout(dp[r], psi, omega.value[s], selector, cache)
            -centered_readout(dp[s], psi, omega.value[r], selector, cache))
        parts.append(direct+connection-de[r, :, s]+de[s, :, r])
    rest = full.vectorize(parts)
    exterior = exterior_core.exterior_model(omega.derivatives)
    derivative = full.reshape(centered_readout(psi, psi, exterior, selector, cache).scale(.5), (24,))
    return rest+derivative, {"joint_differentiated_readout_tail": derivative.tail,
        "other_curl_terms_tail": rest.tail, "joint_exterior_input_tail": exterior.tail}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Joint_Probe_Response_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Joint probe response report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case, cache = load_parent(), control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    psi, dp = origin["psi"].center, origin["dp"].center
    frozen_map(psi, psi, general.prolong.Q, cache)
    for r in range(4):
        frozen_map(dp[r], psi, general.prolong.Q, cache)

    def run(previous):
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, ratios, _ = connection_core.connection_models(case[0], fields)
        curls, pieces = curl_model(fields, omega, cache)
        coefficients = np.asarray(previous["coefficients"]).copy()
        old = coefficients.copy()
        coefficients[:, 56:] = curls.coefficients
        tails = [previous[k]["tail_bound"] for k in ("constraint", "probe", "coframe")]
        combined = T(coefficients, float(np.linalg.norm([*tails, curls.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, **{k: previous[k] for k in ("constraint", "probe", "coframe")},
            "curl": full.summary(curls), "combined": full.summary(combined),
            "previous_curl_tail": previous["curl"]["tail_bound"],
            "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Projector readout inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "frozen_maps": [{k: v for k, v in entry.items() if k not in ("matrix", "input_key")}
            for entry in cache.values()],
        "exact_gram_identity_checked_not_assumed": True, "nonprojector_maps_use_row_bound_fallback": True,
        "all_variable_spinor_cross_terms_retained": True, "other_56_components_and_enclosures_unchanged": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True, "projector_rank_not_a_source_gate_identification": True,
        "only_fixed_map_constants_are_exactly_certified": True, "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
