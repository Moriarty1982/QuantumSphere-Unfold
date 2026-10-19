"""Certified fixed-center matrix actions in the implicit Cartan connection."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "centered_inverse_parent", Path(__file__).with_name("HC_Cartan_Hermitian_Constraint_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
implicit = prior.prior.connection_core
readout = implicit.readout
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Hermitian_Constraint_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def upper_float(value):
    value = Fraction(value)
    if value < 0:
        raise ValueError("Nonnegative upper bound required")
    try:
        result = float(value)
    except OverflowError as error:
        raise ValueError("Finite dyadic upper bound required") from error
    if Fraction.from_float(result) < value:
        result = float(np.nextafter(result, np.inf))
    if not np.isfinite(result) or Fraction.from_float(result) < value:
        raise ValueError("Finite dyadic upper bound required")
    return result


def fixed_matrix_bound(center, cache):
    array = np.asarray(center)
    if array.ndim != 2 or min(array.shape) == 0 or np.any(array.imag) or not np.all(np.isfinite(array)):
        raise ValueError("Finite real matrix center required")
    array = np.asarray(array.real, dtype=np.float64)
    key = (array.shape, array.tobytes())
    if key not in cache:
        exact = sp.Matrix([[sp.Rational(float(v)) for v in row] for row in array])
        reference = exact.applyfunc(lambda v: sp.Rational(round(2*v), 2))
        gram = reference.T*reference
        polynomial = gram*gram-sp.Rational(5, 4)*gram+sp.eye(gram.rows)/4
        reference_proved = polynomial == sp.zeros(gram.rows)
        error_squared = sum(v*v for v in exact-reference)
        if reference_proved:
            error_upper = readout.rational_sqrt_upper(Fraction(error_squared))
            upper = upper_float(Fraction(1)+Fraction.from_float(error_upper))
            certificate = "reference Gram spectrum contained in {1/4,1}; triangle with full center error"
        else:
            actual_gram = exact.T*exact
            row_bound = max(sum(abs(actual_gram[i, j]) for j in range(actual_gram.cols)) for i in range(actual_gram.rows))
            upper = readout.rational_sqrt_upper(Fraction(row_bound))
            certificate = "exact Gram absolute-row-sum fallback"
        cache[key] = {"upper": upper, "certificate": certificate,
            "reference_gram_polynomial_verified": reference_proved,
            "reference_error_squared": str(error_squared),
            "exact_center": [[str(v) for v in row] for row in exact.tolist()],
            "reference": [[str(v) for v in row] for row in reference.tolist()]}
    return cache[key]


def matrix_vector(matrix, vector, cache):
    if matrix.center.ndim != 2 or vector.center.shape != (matrix.center.shape[1],):
        raise ValueError("Compatible matrix/vector models required")
    constant = fixed_matrix_bound(matrix.center, cache)
    leading = T(vector.coefficients @ matrix.center.T, constant["upper"]*vector.tail)
    return leading+c("pq,q->p", matrix-core.tensor(matrix.center), vector)


def implicit_solve(hessian, rhs, cache):
    inverse, ratio = core.matrix_inverse(hessian.value)
    value = matrix_vector(inverse, rhs.value, cache)
    derivatives = [matrix_vector(inverse, df-c("pq,q->p", dh, value), cache)
                   for dh, df in zip(hessian.derivatives, rhs.derivatives)]
    return J(value, derivatives), ratio


def connection_models(prepared, fields, cache):
    lc, vol, inv, e_ratio = implicit.geometry_models(fields)
    psi = J(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = J(fields["lam"], [fields["dl"][r] for r in range(4)])
    forms = prepared["component_forms"]
    components = jc("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = jc(",ma,pam->p", vol, inv, components)
    response = jc("ui,pamij,uj->amp", psi.conjugate(), forms, jc("uv,vj->uj", general.prolong.Q, psi)).real().scale(-1)
    hessian = jc(",ma,nb,pqmnab->pq", vol, inv, inv, prepared["curvature_hessian"]).scale(.5)
    rhs = -source+jc("amp,am->p", response, lam)
    k, ratio = implicit_solve(hessian, rhs, cache)
    old_k, _, _ = implicit.implicit_solve(hessian, rhs)
    omega, old = lc+implicit.embed_jet(k), lc+implicit.embed_jet(old_k)
    diagnostics = {"old_connection_value_tail": old.value.tail, "new_connection_value_tail": omega.value.tail,
        "old_connection_derivative_tails": [d.tail for d in old.derivatives],
        "new_connection_derivative_tails": [d.tail for d in omega.derivatives],
        "connection_coefficient_identity_error": float(np.linalg.norm(omega.value.coefficients-old.value.coefficients)),
        "derivative_coefficient_identity_error": float(np.linalg.norm(np.stack([
            a.coefficients-b.coefficients for a, b in zip(omega.derivatives, old.derivatives)])))}
    return omega, vol, inv.value, {"coframe_neumann_ratio": e_ratio, "hessian_neumann_ratio": ratio}, diagnostics


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Hermitian_Constraint_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Hermitian constraint report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case = load_parent(), control.load_case()

    def run(previous):
        radius = previous["radius"]
        fields, cache, maps = full.field_models(case, radius), {}, {}
        omega, volume, inverse, ratios, diagnostics = connection_models(case[0], fields, cache)
        constraint, _ = prior.constraint_model(fields, omega, maps)
        probe, _ = prior.prior.prior.probe_model(fields, omega, volume, inverse)
        coframe, _ = implicit.prior.coframe_model(fields, omega, volume.value, inverse, maps)
        curls, _ = prior.prior.curl_model(fields, omega, maps)
        combined = full.vectorize([constraint, probe, coframe, curls])
        old = np.asarray(previous["coefficients"])
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            connection = general.connection_jets(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "connection_value_discrepancy": float(np.linalg.norm(connection["omega"]-omega.value.evaluate(y))),
                "connection_derivative_discrepancies": [float(np.linalg.norm(v-d.evaluate(y)))
                    for v, d in zip(connection["first"], omega.derivatives)],
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, **{name: full.summary(value) for name, value in
            zip(("constraint", "probe", "coframe", "curl"), (constraint, probe, coframe, curls))},
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(combined.coefficients-old)),
            "connection_diagnostics": diagnostics, "fixed_matrix_certificates": list(cache.values()),
            **ratios, "coefficients": combined.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Centered inverse-action inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "actual_center_matrix_not_rounded_or_replaced": True,
        "all_variable_matrix_cross_terms_retained": True, "reference_bound_checked_not_assumed": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_fixed_matrix_constants_are_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k not in ("coefficients", "fixed_matrix_certificates")}
        for r in result["reports"]]}, indent=2))
