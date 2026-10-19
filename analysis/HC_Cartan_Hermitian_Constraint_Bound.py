"""Hermitian regrouping of the existing constitutive/constraint readout."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "hermitian_constraint_parent", Path(__file__).with_name("HC_Cartan_Projector_Readout_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Projector_Readout_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def constraint_model(fields, omega, cache):
    selector, weights = general.prolong.Q, general.prolong.WEIGHTS
    if (not np.array_equal(selector, selector.conj().T)
            or not np.array_equal(weights, weights.conj().swapaxes(-1, -2))):
        raise ValueError("Hermitian fixed channel and frame weights required")
    psi, dp, e = (fields[k] for k in ("psi", "dp", "e"))
    direct = c("ui,uv,mvj,aij->am", psi.conjugate(), selector, dp, weights).imag()
    connection = prior.centered_readout(psi, psi, omega.value, selector, cache).transpose(1, 0).scale(.5)
    return direct+connection-e, {"partial_spinor_readout_tail": direct.tail,
        "joint_connection_readout_tail": connection.tail, "coframe_value_tail": e.tail}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Projector_Readout_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Projector readout report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case, cache = load_parent(), control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    prior.frozen_map(origin["psi"].center, origin["psi"].center, general.prolong.Q, cache)

    def run(previous):
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, ratios, _ = prior.connection_core.connection_models(case[0], fields)
        constraint, pieces = constraint_model(fields, omega, cache)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, :16] = constraint.coefficients.reshape(70, 16)
        tails = [previous[k]["tail_bound"] for k in ("probe", "coframe", "curl")]
        combined = T(coefficients, float(np.linalg.norm([constraint.tail, *tails])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "constraint_tail_discrepancy": float(np.linalg.norm(actual[:16].reshape(4, 4)-constraint.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "constraint": full.summary(constraint),
            **{k: previous[k] for k in ("probe", "coframe", "curl")}, "combined": full.summary(combined),
            "previous_constraint_tail": previous["constraint"]["tail_bound"],
            "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)), "tail_diagnostics": pieces,
            **ratios, "coefficients": coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Hermitian constraint inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "identity_is_off_shell": True, "hermitian_fixed_weights_required": True,
        "all_variable_spinor_cross_terms_and_coframe_tail_retained": True,
        "other_64_components_and_enclosures_unchanged": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_previously_certified_fixed_readout_constant_used": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
