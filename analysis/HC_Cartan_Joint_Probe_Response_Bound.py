"""Off-shell joint probe response with variable frame/channel weights retained."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "joint_probe_parent", Path(__file__).with_name("HC_Cartan_Refreshed_Probe_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc
response_core = prior.prior.readout.prior


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Refreshed_Probe_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def check_weight_structure():
    weights, selector = general.prolong.WEIGHTS, general.prolong.Q
    if (not np.array_equal(general.prolong.FLAT_WEIGHTS, np.array([np.kron(np.eye(3), w) for w in weights]))
            or not np.array_equal(general.prolong.Q_WEIGHTS, np.array([np.kron(selector, w) for w in weights]))
            or not np.array_equal(selector, selector.conj().T)):
        raise ValueError("Existing Hermitian channel/frame weight factorization required")


def response_action(psi, omega, volume, inverse, multiplier):
    check_weight_structure()
    for value in (omega, volume, inverse, multiplier):
        if np.any(value.coefficients.imag):
            raise ValueError("Real connection, volume, inverse and multiplier models required")
    response = response_core.response_model(omega)
    flat = c(",ui->ui", volume, c("ma,maij,uj->ui", inverse, response, psi))
    channel = c("am,uv,maij,vj->ui", multiplier, general.prolong.Q, response, psi)
    return full.reshape(flat+channel, (12,))


def probe_model(fields, omega, volume, inverse):
    psi, dp, multiplier = (fields[k] for k in ("psi", "dp", "lam"))
    dinverse = -c("ma,rav,vb->rmb", inverse, fields["de"], inverse)
    inv = J(inverse, [dinverse[r] for r in range(4)])
    lam = J(multiplier, [fields["dl"][r] for r in range(4)])
    weights = (jc(",ma,aij->mij", volume, inv, general.prolong.FLAT_WEIGHTS)
        +jc("am,aij->mij", lam, general.prolong.Q_WEIGHTS))
    divergence = weights.derivatives[0][0]
    for r in range(1, 4):
        divergence = divergence+weights.derivatives[r][r]
    transport = c("mij,mj->i", weights.value, full.reshape(dp, (4, 12))).scale(1j)
    mass = c(",ij,j->i", volume.value, general.prior.joint.prior.MASS_WEIGHT, full.reshape(psi, (12,)))
    weight_derivative = c("ij,j->i", divergence, full.reshape(psi, (12,))).scale(.5j)
    connection = response_action(psi, omega.value, volume.value, inverse, multiplier).scale(.5j)
    result = prior.realify_probe(transport-mass+weight_derivative+connection)
    # Keep the generic 12x12 regrouping as a distinct control of the factorization.
    spin = c("mab,aij,bjk->mik", omega.value, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    spin_full = full.reshape(c("uv,mij->muivj", np.eye(3), spin), (4, 12, 12))
    generic_response = c("mij,mjk->ik", weights.value, spin_full)-c("mji,mjk->ik", spin_full.conjugate(), weights.value)
    generic_connection = c("ij,j->i", generic_response, full.reshape(psi, (12,))).scale(.5j)
    control_probe = prior.realify_probe(transport-mass+weight_derivative+generic_connection)
    return result, {"transport_tail": transport.tail, "mass_tail": mass.tail,
        "weight_derivative_tail": weight_derivative.tail, "joint_connection_action_tail": connection.tail,
        "generic_regrouped_probe_tail": control_probe.tail,
        "factorized_vs_generic_coefficients_error": float(np.linalg.norm(result.coefficients-control_probe.coefficients)),
        "weights_value_tail": weights.value.tail, "weight_divergence_tail": divergence.tail}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Refreshed_Probe_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Refreshed probe report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case = load_parent(), control.load_case()

    def run(previous):
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, volume, inverse, ratios, _ = prior.prior.connection_models(case[0], fields)
        probe, pieces = probe_model(fields, omega, volume, inverse)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, 16:40] = probe.coefficients
        tails = [previous[k]["tail_bound"] for k in ("constraint", "coframe", "curl")]
        combined = T(coefficients, float(np.linalg.norm([*tails, probe.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "probe_tail_discrepancy": float(np.linalg.norm(actual[16:40]-probe.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "constraint": previous["constraint"], "probe": full.summary(probe),
            "coframe": previous["coframe"], "curl": previous["curl"], "combined": full.summary(combined),
            "previous_probe_tail": previous["probe"]["tail_bound"],
            "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Joint probe response inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "identity": "i W S psi + (i/2)(-S^dagger W-W S)psi = (i/2)(W S-S^dagger W)psi",
        "identity_is_off_shell": True, "variable_volume_inverse_and_multiplier_retained": True,
        "weight_derivatives_not_dropped": True, "other_56_equations_and_enclosures_unchanged": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_previously_certified_fixed_response_constant_used": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
