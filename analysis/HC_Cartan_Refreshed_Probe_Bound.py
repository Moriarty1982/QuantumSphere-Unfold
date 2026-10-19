"""Refresh the unchanged first 40 equations with the improved connection model."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "refreshed_probe_parent", Path(__file__).with_name("HC_Cartan_Implicit_Connection_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Implicit_Connection_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def realify_probe(probe):
    if probe.center.shape != (12,):
        raise ValueError("Twelve complex probe components required")
    return T(np.concatenate((probe.coefficients.real, probe.coefficients.imag), axis=1), probe.tail)


def primary_models(fields, omega, volume, inverse):
    """Same contractions and derivative identities as the full Taylor evaluator."""
    e, psi, dp, lam = (fields[k] for k in ("e", "psi", "dp", "lam"))
    dinverse = -c("ma,rav,vb->rmb", inverse, fields["de"], inverse)
    inv = J(inverse, [dinverse[r] for r in range(4)])
    multiplier = J(lam, [fields["dl"][r] for r in range(4)])
    weights = (jc(",ma,aij->mij", volume, inv, general.prolong.FLAT_WEIGHTS)
        +jc("am,aij->mij", multiplier, general.prolong.Q_WEIGHTS))
    spin = c("mab,aij,bjk->mik", omega.value, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    covariant = dp+c("mij,uj->mui", spin, psi)
    constraint = c("ui,uv,mvj,aij->am", psi.conjugate(), general.prolong.Q, covariant, general.prolong.WEIGHTS).imag()-e
    spin_full = full.reshape(c("uv,mij->muivj", np.eye(3), spin), (4, 12, 12))
    divergence = weights.derivatives[0][0]
    for r in range(1, 4):
        divergence = divergence+weights.derivatives[r][r]
    defect = divergence-c("mji,mjk->ik", spin_full.conjugate(), weights.value)-c("mij,mjk->ik", weights.value, spin_full)
    kinetic = c("mij,mj->i", weights.value, full.reshape(covariant, (4, 12))).scale(1j)
    mass = c(",ij,j->i", volume.value, general.prior.joint.prior.MASS_WEIGHT, full.reshape(psi, (12,)))
    balance = c("ij,j->i", defect, full.reshape(psi, (12,))).scale(.5j)
    probe = realify_probe(kinetic-mass+balance)
    return constraint, probe, {"spin_value_tail": spin.tail,
        "weights_value_tail": weights.value.tail, "weights_derivative_tails": [d.tail for d in weights.derivatives],
        "covariant_spinor_jet_tail": covariant.tail, "weight_divergence_tail": divergence.tail,
        "probe_defect_matrix_tail": defect.tail, "kinetic_probe_tail": kinetic.tail,
        "mass_probe_tail": mass.tail, "balance_probe_tail": balance.tail}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Implicit_Connection_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Implicit connection report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), prior.readout.prior.hermitian.load_parent()
    case = control.load_case()

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, volume, inverse, ratios, _ = prior.connection_models(case[0], fields)
        constraint, probe, pieces = primary_models(fields, omega, volume, inverse)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, :16] = constraint.coefficients.reshape(70, 16)
        coefficients[:, 16:40] = probe.coefficients
        combined = T(coefficients, float(np.linalg.norm([constraint.tail, probe.tail,
            previous["coframe"]["tail_bound"], previous["curl"]["tail_bound"]])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "constraint_tail_discrepancy": float(np.linalg.norm(actual[:16].reshape(4, 4)-constraint.evaluate(y))),
                "probe_tail_discrepancy": float(np.linalg.norm(actual[16:40]-probe.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "constraint": full.summary(constraint), "probe": full.summary(probe),
            "coframe": previous["coframe"], "curl": previous["curl"], "combined": full.summary(combined),
            "previous_constraint_tail": initial["blocks"]["constraint"]["tail_bound"],
            "previous_probe_tail": initial["blocks"]["probe"]["tail_bound"],
            "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Refreshed probe inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "primary_equation_contractions_unchanged": True,
        "coframe_and_curl_enclosures_unchanged": True,
        "no_connection_derivative_needed_by_primary_equations": True,
        "physical_weights_derivative_models_retained": True,
        "complex_to_real_probe_packing_is_isometric": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
