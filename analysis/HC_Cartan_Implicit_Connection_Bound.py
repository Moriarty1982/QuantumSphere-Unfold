"""Implicit Cartan derivatives and a joint fixed-basis embedding enclosure."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "implicit_connection_parent", Path(__file__).with_name("HC_Cartan_Isometric_Curvature_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc
readout = prior.readout
BASIS_OPERATOR = general.cartan.OMEGA_BASIS.reshape(24, 64).T
BASIS_NORM_UPPER = readout.rational_sqrt_upper(Fraction(2))


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Isometric_Curvature_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def embed(value):
    if value.center.shape != (24,):
        raise ValueError("Twenty-four Cartan coefficients required")
    coefficients = (value.coefficients @ BASIS_OPERATOR.T).reshape(70, 4, 4, 4)
    return T(coefficients, BASIS_NORM_UPPER*value.tail)


def embed_jet(value):
    return J(embed(value.value), [embed(d) for d in value.derivatives])


def implicit_solve(hessian, rhs):
    """Differentiate H k=f by solving H dk=df-dH k; keep all Taylor tails."""
    if hessian.value.center.ndim != 2 or hessian.value.center.shape[0] != hessian.value.center.shape[1]:
        raise ValueError("Square Hessian model required")
    if rhs.value.center.shape != (hessian.value.center.shape[0],):
        raise ValueError("Vector right side must match Hessian")
    inverse, ratio = core.matrix_inverse(hessian.value)
    value = c("pq,q->p", inverse, rhs.value)
    derivatives = [c("pq,q->p", inverse, df-c("pq,q->p", dh, value))
                   for dh, df in zip(hessian.derivatives, rhs.derivatives)]
    inverse_jet = J(inverse, [-c("pa,ab,bq->pq", inverse, dh, inverse) for dh in hessian.derivatives])
    product_rule_control = jc("pq,q->p", inverse_jet, rhs)
    return J(value, derivatives), product_rule_control, ratio


def geometry_models(fields):
    e = J(fields["e"], [fields["de"][r] for r in range(4)])
    de = J(fields["de"], [fields["dde"][r] for r in range(4)])
    inverse, ratio = core.matrix_inverse(e.value)
    if np.linalg.det(e.value.center) <= 0:
        raise ValueError("Positive coframe orientation required")
    volume = core.determinant(e.value)
    dinverse = -c("ma,rav,vb->rmb", inverse, fields["de"], inverse)
    dvolume = c(",ma,ram->r", volume, inverse, fields["de"])
    inv = J(inverse, [dinverse[r] for r in range(4)])
    vol = J(volume, [dvolume[r] for r in range(4)])
    eta = general.prolong.ETA
    metric_inverse = jc("ma,ab,nb->mn", inv, eta, inv)
    metric_first = jc("ram,ab,bv->rmv", de, eta, e)+jc("am,ab,rbv->rmv", e, eta, de)
    lower = (metric_first.transpose(1, 0, 2)+metric_first.transpose(1, 2, 0)-metric_first).scale(.5)
    gamma = jc("as,sbc->abc", metric_inverse, lower)
    lc = jc("ab,mbv,vc->mac", eta, jc("ap,pmq->maq", e, gamma)-de, inv)
    return lc, vol, inv, ratio


def connection_models(prepared, fields):
    lc, vol, inv, e_ratio = geometry_models(fields)
    psi = J(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = J(fields["lam"], [fields["dl"][r] for r in range(4)])
    forms = prepared["component_forms"]
    components = jc("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = jc(",ma,pam->p", vol, inv, components)
    response = jc("ui,pamij,uj->amp", psi.conjugate(), forms, jc("uv,vj->uj", general.prolong.Q, psi)).real().scale(-1)
    hessian = jc(",ma,nb,pqmnab->pq", vol, inv, inv, prepared["curvature_hessian"]).scale(.5)
    rhs = -source+jc("amp,am->p", response, lam)
    k, old_k, h_ratio = implicit_solve(hessian, rhs)
    old = lc+jc("p,pmab->mab", old_k, general.cartan.OMEGA_BASIS)
    basis_only = lc+embed_jet(old_k)
    omega = lc+embed_jet(k)
    pieces = {"old_connection_value_tail": old.value.tail,
        "old_connection_derivative_tails": [d.tail for d in old.derivatives],
        "basis_only_connection_derivative_tails": [d.tail for d in basis_only.derivatives],
        "new_connection_value_tail": omega.value.tail,
        "new_connection_derivative_tails": [d.tail for d in omega.derivatives],
        "product_rule_cartan_derivative_tails": [d.tail for d in old_k.derivatives],
        "implicit_cartan_derivative_tails": [d.tail for d in k.derivatives],
        "levi_civita_value_tail": lc.value.tail,
        "levi_civita_derivative_tails": [d.tail for d in lc.derivatives],
        "connection_value_coefficient_error": float(np.linalg.norm(omega.value.coefficients-old.value.coefficients)),
        "connection_derivative_coefficient_error": float(np.linalg.norm(np.stack([
            a.coefficients-b.coefficients for a, b in zip(omega.derivatives, old.derivatives)])))}
    return omega, vol, inv.value, {"coframe_neumann_ratio": e_ratio, "hessian_neumann_ratio": h_ratio}, pieces


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Isometric_Curvature_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Isometric curvature report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), readout.prior.hermitian.load_parent()
    case, cache = control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    psi, dp = origin["psi"].center, origin["dp"].center
    for selector in (general.prolong.Q, np.eye(3)):
        readout.frozen_map(psi, psi, selector, cache)
    for r in range(4):
        readout.frozen_map(dp[r], psi, general.prolong.Q, cache)

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, volume, inverse, ratios, pieces = connection_models(case[0], fields)
        coframe, coframe_pieces = prior.coframe_model(fields, omega, volume.value, inverse, cache)
        curls, curl_pieces = prior.prior.curl_model(fields, omega, cache)
        old = np.asarray(previous["coefficients"])
        coefficients = old.copy()
        coefficients[:, 40:56] = coframe.coefficients.reshape(70, 16)
        coefficients[:, 56:] = curls.coefficients
        tails = [initial["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
        combined = T(coefficients, float(np.linalg.norm([*tails, coframe.tail, curls.tail])))
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            connection = general.connection_jets(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "connection_value_tail_discrepancy": float(np.linalg.norm(connection["omega"]-omega.value.evaluate(y))),
                "connection_derivative_tail_discrepancies": [float(np.linalg.norm(v-d.evaluate(y)))
                    for v, d in zip(connection["first"], omega.derivatives)],
                "coframe_tail_discrepancy": float(np.linalg.norm(actual[40:56].reshape(4, 4)-coframe.evaluate(y))),
                "curl_tail_discrepancy": float(np.linalg.norm(actual[56:]-curls.evaluate(y))),
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, "coframe": full.summary(coframe), "curl": full.summary(curls),
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "previous_coframe_tail": previous["coframe"]["tail_bound"], "previous_curl_tail": previous["curl"]["tail_bound"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "connection_diagnostics": pieces, "coframe_diagnostics": coframe_pieces, "curl_diagnostics": curl_pieces,
            **ratios, "coefficients": coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Implicit connection inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "embedding_gram": "2 I_24", "embedding_exact_norm": "sqrt(2)",
        "embedding_norm_upper": BASIS_NORM_UPPER,
        "implicit_derivative_identity": "H dk = df - dH k",
        "no_unknown_value_tail_differentiated": True, "all_inverse_and_product_tails_retained": True,
        "constraint_and_probe_bounds_deliberately_inherited": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_fixed_linear_constants_are_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
