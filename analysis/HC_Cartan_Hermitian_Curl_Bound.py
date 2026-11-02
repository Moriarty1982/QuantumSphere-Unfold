"""Off-shell Hermitian regrouping of curl equations before Taylor tail norms."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "hermitian_curl_parent", Path(__file__).with_name("HC_Cartan_Full_Taylor_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
core, control, common, general = prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Full_Taylor_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def hermitian_response(weights, gamma):
    """Frozen linear map omega_bc -> W_a S - S^dagger W_a."""
    weights, gamma = np.asarray(weights), np.asarray(gamma)
    if weights.shape != (4, 4, 4) or gamma.shape != (4, 4, 4):
        raise ValueError("Four frame weights and four gamma matrices required")
    if not np.allclose(weights, weights.conj().swapaxes(-1, -2), atol=1e-14, rtol=0):
        raise ValueError("Hermitian frame weights required")
    generators = -.25*np.einsum("bij,cjk->bcik", gamma, gamma)
    return (np.einsum("aij,bcjk->abcik", weights, generators)
            -np.einsum("bcji,ajk->abcik", generators.conj(), weights))


RESPONSE = hermitian_response(general.prolong.WEIGHTS, general.cartan.GAMMA)


def curl_model(fields, omega, response=RESPONSE, selector=None):
    selector = general.prolong.Q if selector is None else np.asarray(selector)
    if selector.shape != (3, 3) or not np.allclose(selector, selector.conj().T, atol=1e-14, rtol=0):
        raise ValueError("Hermitian three-channel selector required")
    psi, dp, de = (fields[k] for k in ("psi", "dp", "de"))
    connection_response = c("mbc,abcij->maij", omega.value, response)
    curls = []
    for r in range(4):
        for s in range(r+1, 4):
            differentiated = c("bc,abcij->aij", omega.derivatives[r][s]-omega.derivatives[s][r], response)
            direct = c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, dp[s], general.prolong.WEIGHTS).imag().scale(2)
            connection = (c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, psi, connection_response[s])
                -c("ui,uv,vj,aij->a", dp[s].conjugate(), selector, psi, connection_response[r])).imag()
            derivative = c("ui,uv,vj,aij->a", psi.conjugate(), selector, psi, differentiated).imag().scale(.5)
            curls.append(direct+connection+derivative-de[r, :, s]+de[s, :, r])
    return prior.vectorize(curls)


def compact_at_point(prepared, fields):
    connection = general.connection_jets(prepared, fields)
    omega = prior.TaylorJet(core.tensor(connection["omega"]), [core.tensor(v) for v in connection["first"]])
    return curl_model(prior.point_models(fields), omega).center


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Full_Taylor_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Full Taylor report has stale inputs")
    return report


def combine_with_parent(parent_report, curls):
    coefficients = np.concatenate((np.asarray(parent_report["coefficients"])[:, :56], curls.coefficients), axis=1)
    tails = [parent_report["blocks"][key]["tail_bound"] for key in ("constraint", "probe", "coframe")]
    return T(coefficients, float(np.linalg.norm([*tails, curls.tail])))


def evaluate():
    fingerprints = input_fingerprints()
    parent = load_parent()
    case = control.load_case()

    def run(original):
        radius = original["radius"]
        fields = prior.field_models(case, radius)
        omega, _, _, _, _, ratios = prior.connection_models(case[0], fields)
        curls = curl_model(fields, omega)
        full = combine_with_parent(original, curls)
        old_coefficients = np.asarray(original["coefficients"])[:, 56:]
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            compact = compact_at_point(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "curl_actual_norm": float(np.linalg.norm(actual[56:])),
                "point_identity_error": float(np.linalg.norm(compact-actual[56:])),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "full_actual_norm": float(np.linalg.norm(actual))})
        return {"radius": radius, "curl": prior.summary(curls), "combined": prior.summary(full), **ratios,
            "previous_curl_tail": original["blocks"]["curls"]["tail_bound"],
            "previous_combined_upper_estimate": original["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(curls.coefficients-old_coefficients)),
            "coefficients": full.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Hermitian curl inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "off-shell Hermitian regrouping of all 24 curl rows with unchanged first 56 rows",
        "reports": reports, "response_frobenius_norm": float(np.linalg.norm(RESPONSE)),
        "response_antihermitian_error": float(np.linalg.norm(RESPONSE+RESPONSE.conj().swapaxes(-1, -2))),
        "response_antisymmetric_connection_index_error": float(np.linalg.norm(RESPONSE+RESPONSE.swapaxes(1, 2))),
        "no_coefficients_fitted_or_zeroed": True, "identity_does_not_require_field_equations": True,
        "not_outward_rounded_or_interval_certified": True,
        "not_exact_low_order_closure_or_regional_solution": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k != "input_sha256"}, indent=2))
