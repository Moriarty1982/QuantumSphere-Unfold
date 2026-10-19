"""Joint exterior-derivative enclosure for the unchanged 24 Cartan curl rows."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "joint_curl_parent", Path(__file__).with_name("HC_Cartan_Pair_Antisymmetric_Ricci_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
readout = prior.prior
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract
PAIRS = tuple((r, s) for r in range(4) for s in range(r+1, 4))
EXTERIOR_OPERATOR = np.zeros((6, 4, 4))
for k, (r, s) in enumerate(PAIRS):
    EXTERIOR_OPERATOR[k, r, s], EXTERIOR_OPERATOR[k, s, r] = 1., -1.
EXTERIOR_NORM_UPPER = readout.rational_sqrt_upper(Fraction(2))


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Pair_Antisymmetric_Ricci_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def exterior_model(derivatives):
    """Apply D to separately controlled derivative models, never to a value tail."""
    derivatives = tuple(derivatives)
    if len(derivatives) != 4 or any(d.center.shape != (4, 4, 4) for d in derivatives):
        raise ValueError("Four controlled connection derivative tensors required")
    first = core.stack(derivatives)
    coefficients = np.einsum("krs,nrsab->nkab", EXTERIOR_OPERATOR, first.coefficients)
    return T(coefficients, EXTERIOR_NORM_UPPER*first.tail)


def curl_model(fields, omega, cache):
    psi, dp, de = (fields[k] for k in ("psi", "dp", "de"))
    selector = general.prolong.Q
    remainders = []
    for r, s in PAIRS:
        direct = c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, dp[s], general.prolong.WEIGHTS).imag().scale(2)
        connection = (readout.centered_readout(dp[r], psi, omega.value[s], selector, cache)
            -readout.centered_readout(dp[s], psi, omega.value[r], selector, cache))
        remainders.append(direct+connection-de[r, :, s]+de[s, :, r])
    rest = full.vectorize(remainders)
    exterior = exterior_model(omega.derivatives)
    differentiated = full.reshape(readout.centered_readout(psi, psi, exterior, selector, cache).scale(.5), (24,))
    return rest+differentiated, {
        "joint_exterior_input_tail": exterior.tail,
        "separately_controlled_derivative_tails": [d.tail for d in omega.derivatives],
        "joint_differentiated_readout_tail": differentiated.tail,
        "other_curl_terms_tail": rest.tail,
        "exterior_operator_norm_upper": EXTERIOR_NORM_UPPER}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Pair_Antisymmetric_Ricci_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Pair-antisymmetric Ricci report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), readout.prior.hermitian.load_parent()
    case, cache = control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    psi, dp = origin["psi"].center, origin["dp"].center
    readout.frozen_map(psi, psi, general.prolong.Q, cache)
    for r in range(4):
        readout.frozen_map(dp[r], psi, general.prolong.Q, cache)

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, _, _, ratios = full.connection_models(case[0], fields)
        curls, pieces = curl_model(fields, omega, cache)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, 56:] = curls.coefficients
        tails = [initial["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
        combined = T(coefficients, float(np.linalg.norm([*tails, previous["coframe"]["tail_bound"], curls.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "curl": full.summary(curls), "coframe": previous["coframe"],
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "previous_curl_tail": previous["curl"]["tail_bound"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Joint exterior curl inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "exterior_gram": "2 I_6", "exterior_exact_norm": "sqrt(2)",
        "exterior_norm_upper": EXTERIOR_NORM_UPPER,
        "physical_derivative_models_retained_not_unknown_value_tail_differentiated": True,
        "all_variable_spinor_readout_cross_terms_retained": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_fixed_linear_constants_are_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
