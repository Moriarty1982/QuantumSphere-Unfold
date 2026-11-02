"""Exact signed-axis isometries in the unchanged Cartan curvature formula."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "isometric_curvature_parent", Path(__file__).with_name("HC_Cartan_Joint_Exterior_Curl_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
ricci, readout = prior.prior, prior.readout
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Joint_Exterior_Curl_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def signed_axis(value, metric, axis):
    """Apply a fixed diagonal +/-1 metric along one tensor axis, with norm one."""
    metric = np.asarray(metric)
    if metric.shape != (4, 4) or not np.array_equal(metric, np.diag(np.diag(metric))):
        raise ValueError("Fixed four-dimensional diagonal signature matrix required")
    signs = np.diag(metric)
    if not np.all((signs == 1) | (signs == -1)):
        raise ValueError("Metric entries must be exactly plus or minus one")
    ndim = value.center.ndim
    if not -ndim <= axis < ndim:
        raise ValueError("Tensor axis out of range")
    axis %= ndim
    if value.center.shape[axis] != 4:
        raise ValueError("Signature action requires an axis of length four")
    shape = [1]*(ndim+1)
    shape[axis+1] = 4
    return T(value.coefficients*signs.reshape(shape), value.tail)


def curvature_model(omega):
    eta = general.prolong.ETA
    mixed = signed_axis(omega.value, eta, 1)
    product = c("mac,ncb->mnab", mixed, mixed)
    commutator = signed_axis(product-product.transpose(1, 0, 2, 3), eta, 3)
    first = core.stack(omega.derivatives)
    exterior = first-first.transpose(1, 0, 2, 3)
    derivative = signed_axis(signed_axis(exterior, eta, 2), eta, 3)
    return commutator+derivative, {"curvature_derivative_tail": derivative.tail,
        "curvature_commutator_tail": commutator.tail,
        "stacked_physical_derivative_tail": first.tail,
        "connection_value_tail": omega.value.tail,
        "signed_metric_action_operator_norm": 1.}


def coframe_model(fields, omega, volume, inverse, cache):
    psi, dp, lam = (fields[k] for k in ("psi", "dp", "lam"))
    partial = c("ui,muj,aij->am", psi.conjugate(), dp, general.prolong.WEIGHTS).imag()
    connection = readout.centered_readout(psi, psi, omega.value, np.eye(3), cache).transpose(1, 0).scale(.5)
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    curvature, curvature_pieces = curvature_model(omega)
    model, pieces = ricci.factorized_euler(inverse, volume, partial+connection, mass, curvature, lam)
    return model, {**pieces, **curvature_pieces, "curvature_tail": curvature.tail}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Joint_Exterior_Curl_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Joint exterior curl report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), readout.prior.hermitian.load_parent()
    case, cache = control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    readout.frozen_map(origin["psi"].center, origin["psi"].center, np.eye(3), cache)

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, volume, inverse, ratios = full.connection_models(case[0], fields)
        coframe, pieces = coframe_model(fields, omega, volume.value, inverse, cache)
        old_curvature = ricci.trace.curvature_model(omega)
        curvature, _ = curvature_model(omega)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, 40:56] = coframe.coefficients.reshape(70, 16)
        tails = [initial["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
        combined = T(coefficients, float(np.linalg.norm([*tails, coframe.tail, previous["curl"]["tail_bound"]])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "coframe_tail_discrepancy": float(np.linalg.norm(actual[40:56].reshape(4, 4)-coframe.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "coframe": full.summary(coframe), "curl": previous["curl"],
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "previous_coframe_tail": previous["coframe"]["tail_bound"],
            "previous_curvature_tail": old_curvature.tail,
            "curvature_coefficient_identity_error": float(np.linalg.norm(curvature.coefficients-old_curvature.coefficients)),
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Isometric curvature inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "fixed_signature": general.prolong.ETA.tolist(),
        "signed_metric_action_exact_euclidean_operator_norm": 1,
        "not_an_indefinite_lorentz_norm_claim": True,
        "all_connection_value_and_derivative_tails_retained": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_fixed_linear_constants_are_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
