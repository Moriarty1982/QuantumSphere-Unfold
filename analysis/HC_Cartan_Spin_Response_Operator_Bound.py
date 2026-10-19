"""Exact fixed-spin-response operator norm in curl/coframe Taylor tail bounds."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "spin_operator_parent", Path(__file__).with_name("HC_Cartan_Trace_Reversed_Coframe_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
hermitian, full, core = prior.prior, prior.full, prior.core
control, common, general = prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract
RESPONSE_OPERATOR = hermitian.RESPONSE.transpose(0, 3, 4, 1, 2).reshape(64, 16)
OPERATOR_NORM = 2.


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Trace_Reversed_Coframe_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def response_model(omega):
    """A fixed linear map acts independently on every leading tensor block."""
    if omega.center.shape[-2:] != (4, 4):
        raise ValueError("Last two axes must be the four-dimensional lower connection indices")
    leading = omega.center.shape[:-2]
    coefficients = omega.coefficients.reshape(len(core.POWERS), -1, 16) @ RESPONSE_OPERATOR.T
    return T(coefficients.reshape(len(core.POWERS), *leading, 4, 4, 4), OPERATOR_NORM*omega.tail)


def curl_model(fields, omega):
    psi, dp, de = (fields[k] for k in ("psi", "dp", "de"))
    selector = general.prolong.Q
    connection_response = response_model(omega.value)
    curls = []
    for r in range(4):
        for s in range(r+1, 4):
            differentiated = response_model(omega.derivatives[r][s]-omega.derivatives[s][r])
            direct = c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, dp[s], general.prolong.WEIGHTS).imag().scale(2)
            connection = (c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, psi, connection_response[s])
                -c("ui,uv,vj,aij->a", dp[s].conjugate(), selector, psi, connection_response[r])).imag()
            derivative = c("ui,uv,vj,aij->a", psi.conjugate(), selector, psi, differentiated).imag().scale(.5)
            curls.append(direct+connection+derivative-de[r, :, s]+de[s, :, r])
    return full.vectorize(curls)


def coframe_model(fields, omega, volume, inverse):
    psi, dp, lam = (fields[k] for k in ("psi", "dp", "lam"))
    response = response_model(omega.value)
    partial = c("ui,muj,aij->am", psi.conjugate(), dp, general.prolong.WEIGHTS).imag()
    connection = c("ui,uj,maij->am", psi.conjugate(), psi, response).imag().scale(.5)
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    return prior.factorized_euler(inverse, volume, partial+connection, mass, prior.curvature_model(omega), lam)


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Trace_Reversed_Coframe_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Trace-reversed coframe report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, initial, curl_parent = load_parent(), hermitian.load_parent(), prior.load_parent()
    case = control.load_case()

    def run(pair):
        original, base, previous_curl = pair
        radius = original["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, volume, inverse, ratios = full.connection_models(case[0], fields)
        curls = curl_model(fields, omega)
        coframe, pieces = coframe_model(fields, omega, volume.value, inverse)
        coefficients = np.asarray(original["coefficients"]).copy()
        old_coefficients = coefficients.copy()
        coefficients[:, 40:56] = coframe.coefficients.reshape(70, 16)
        coefficients[:, 56:] = curls.coefficients
        unchanged_tails = [base["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
        combined = T(coefficients, float(np.linalg.norm([*unchanged_tails, coframe.tail, curls.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "coframe_tail_discrepancy": float(np.linalg.norm(actual[40:56].reshape(4, 4)-coframe.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "curl": full.summary(curls), "coframe": full.summary(coframe),
            "combined": full.summary(combined), "previous_combined_upper_estimate": original["combined"]["whole_cube_upper_estimate"],
            "previous_coframe_tail": original["coframe"]["tail_bound"],
            "previous_curl_tail": previous_curl["curl"]["tail_bound"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old_coefficients)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], initial["reports"], curl_parent["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Spin-response bound inputs changed during evaluation")
    swap = np.eye(16).reshape(4, 4, 4, 4).swapaxes(0, 1).reshape(16, 16)
    return {"input_sha256": fingerprints, "scope": "fixed spin-response operator norm in the unchanged 80-row Taylor enclosure",
        "response_operator_norm": OPERATOR_NORM, "response_tensor_frobenius_norm": float(np.linalg.norm(RESPONSE_OPERATOR)),
        "gram_projector_error": float(np.linalg.norm(RESPONSE_OPERATOR.conj().T @ RESPONSE_OPERATOR-2*(np.eye(16)-swap))),
        "reports": reports, "no_coefficients_fitted_or_zeroed": True,
        "not_a_source_gate_identification": True, "not_outward_rounded_or_interval_certified": True,
        "not_exact_low_order_closure_or_regional_solution": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k != "input_sha256"}, indent=2))
