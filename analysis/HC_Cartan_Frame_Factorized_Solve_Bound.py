"""Polynomially checked Cartan Hessian frame factorization and curved solve."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "frame_solve_parent", Path(__file__).with_name("HC_Cartan_Centered_Inverse_Action_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc
LIFT_NORM_UPPER = prior.readout.rational_sqrt_upper(Fraction(6))


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Centered_Inverse_Action_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def factorization_certificate(curvature_hessian):
    raw = np.asarray(curvature_hessian)
    if (raw.shape != (24, 24, 4, 4, 4, 4) or not np.all(np.isfinite(raw))
            or np.any(raw.imag) or not np.array_equal(raw.real, np.rint(raw.real))):
        raise ValueError("Integral real Cartan curvature Hessian coefficients required")
    maximum = max(abs(int(v)) for v in raw.real.flat)
    intermediate_bound = maximum*4*256*24**2
    if intermediate_bound >= 2**63:
        raise ValueError("Integer certificate intermediate overflow bound unresolved")
    tensor = raw.real.astype(np.int64)
    units = np.eye(16, dtype=np.int64).reshape(16, 4, 4)
    identity, channel = np.eye(4, dtype=np.int64), np.eye(6, dtype=np.int64)
    flat_twice = np.einsum("ma,nb,pqmnab->pq", identity, identity, tensor)

    def quadratic(a):
        return np.einsum("ma,nb,pqmnab->pq", a, a, tensor)

    lifts = [np.kron(a.T, channel) for a in units]
    for index, a in enumerate(units):
        if not np.array_equal(quadratic(a), lifts[index].T @ flat_twice @ lifts[index]):
            raise ValueError("Diagonal frame coefficient identity failed")
        for j in range(index):
            cross = quadratic(a+units[j])-quadratic(a)-quadratic(units[j])
            target = lifts[index].T @ flat_twice @ lifts[j]+lifts[j].T @ flat_twice @ lifts[index]
            if not np.array_equal(cross, target):
                raise ValueError("Mixed frame coefficient identity failed")
    flat_exact = sp.Matrix(flat_twice.tolist())/2
    try:
        inverse_exact = flat_exact.inv()
    except sp.matrices.exceptions.NonInvertibleMatrixError as error:
        raise ValueError("Flat Cartan Hessian must be invertible") from error
    if flat_exact*inverse_exact != sp.eye(24):
        raise ValueError("Flat inverse identity failed")
    inverse = np.array(inverse_exact.tolist(), float)
    if sp.Matrix([[sp.Rational(float(v)) for v in row] for row in inverse]) != inverse_exact:
        raise ValueError("Flat inverse does not have an exact binary64 representation")
    return inverse, {"diagonal_coefficient_checks": 16, "mixed_coefficient_checks": 120,
        "integer_intermediate_bound": intermediate_bound,
        "twice_flat_hessian": flat_twice.tolist(),
        "exact_flat_inverse": [[str(v) for v in row] for row in inverse_exact.tolist()],
        "coefficient_sha256": hashlib.sha256(tensor.tobytes()).hexdigest()}


def lift(value, transpose=False):
    if value.center.shape != (4, 4):
        raise ValueError("Four-dimensional frame matrix required")
    coefficients = np.array([np.kron(a.T if transpose else a, np.eye(6)) for a in value.coefficients])
    return T(coefficients, LIFT_NORM_UPPER*value.tail)


def matrix_vector_jet(matrix, vector, cache):
    value = prior.matrix_vector(matrix.value, vector.value, cache)
    derivatives = [prior.matrix_vector(matrix.value, db, cache)+c("pq,q->p", da, vector.value)
        for da, db in zip(matrix.derivatives, vector.derivatives)]
    return J(value, derivatives)


def reciprocal_volume(volume):
    if volume.value.center.shape != () or np.any(volume.value.coefficients.imag) or volume.value.center <= 0:
        raise ValueError("Positive real scalar volume center required")
    matrix, ratio = core.matrix_inverse(full.reshape(volume.value, (1, 1)))
    value = full.reshape(matrix, ())
    return J(value, [-c(",,->", value, d, value) for d in volume.derivatives]), ratio


def frame_solve(coframe, volume, rhs, flat_inverse, cache):
    left = J(lift(coframe.value, True), [lift(d, True) for d in coframe.derivatives])
    right = J(lift(coframe.value), [lift(d) for d in coframe.derivatives])
    middle = matrix_vector_jet(J(flat_inverse), matrix_vector_jet(right, rhs, cache), cache)
    curved = matrix_vector_jet(left, middle, cache)
    reciprocal, ratio = reciprocal_volume(volume)
    return jc(",p->p", reciprocal, curved), ratio


def connection_models(prepared, fields, flat_inverse, cache):
    lc, vol, inv, e_ratio = prior.implicit.geometry_models(fields)
    psi = J(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = J(fields["lam"], [fields["dl"][r] for r in range(4)])
    e = J(fields["e"], [fields["de"][r] for r in range(4)])
    forms = prepared["component_forms"]
    components = jc("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = jc(",ma,pam->p", vol, inv, components)
    response = jc("ui,pamij,uj->amp", psi.conjugate(), forms, jc("uv,vj->uj", general.prolong.Q, psi)).real().scale(-1)
    rhs = -source+jc("amp,am->p", response, lam)
    k, volume_ratio = frame_solve(e, vol, rhs, flat_inverse, cache)
    omega = lc+prior.implicit.embed_jet(k)
    return omega, vol, inv.value, {"coframe_neumann_ratio": e_ratio, "volume_reciprocal_neumann_ratio": volume_ratio}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Centered_Inverse_Action_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Centered inverse action report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case = load_parent(), control.load_case()
    flat_inverse, certificate = factorization_certificate(case[0]["curvature_hessian"])

    def run(previous):
        radius = previous["radius"]
        fields, cache, maps = full.field_models(case, radius), {}, {}
        omega, volume, inverse, ratios = connection_models(case[0], fields, flat_inverse, cache)
        old_omega, _, _, _, _ = prior.connection_models(case[0], fields, {})
        constraint, _ = prior.prior.constraint_model(fields, omega, maps)
        probe, _ = prior.prior.prior.prior.probe_model(fields, omega, volume, inverse)
        coframe, _ = prior.implicit.prior.coframe_model(fields, omega, volume.value, inverse, maps)
        curls, _ = prior.prior.prior.curl_model(fields, omega, maps)
        combined = full.vectorize([constraint, probe, coframe, curls])
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], actual_fields)
            original = general.connection_jets(case[0], actual_fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "connection_value_discrepancy": float(np.linalg.norm(original["omega"]-omega.value.evaluate(y))),
                "connection_derivative_discrepancies": [float(np.linalg.norm(v-d.evaluate(y)))
                    for v, d in zip(original["first"], omega.derivatives)],
                "combined_tail_discrepancy": float(np.linalg.norm(actual-combined.evaluate(y)))})
        return {"radius": radius, **{name: full.summary(value) for name, value in zip(
            ("constraint", "probe", "coframe", "curl"), (constraint, probe, coframe, curls))},
            "combined": full.summary(combined), "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(combined.coefficients-np.asarray(previous["coefficients"]))),
            "connection_diagnostics": {"old_value_tail": old_omega.value.tail, "new_value_tail": omega.value.tail,
                "old_derivative_tails": [d.tail for d in old_omega.derivatives],
                "new_derivative_tails": [d.tail for d in omega.derivatives],
                "value_coefficient_error": float(np.linalg.norm(omega.value.coefficients-old_omega.value.coefficients)),
                "derivative_coefficient_error": float(np.linalg.norm(np.stack([a.coefficients-b.coefficients
                    for a, b in zip(omega.derivatives, old_omega.derivatives)])))},
            **ratios, "coefficients": combined.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Frame-factorized solve inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "factorization_certificate": certificate,
        "identity": "H(A,v)=v (A^T tensor I6)^T H0 (A^T tensor I6)",
        "inverse_identity": "H^-1=v^-1 (E^T tensor I6) H0^-1 (E tensor I6), A=E^-1",
        "all_quadratic_coefficients_checked_not_sampled": True, "flat_inverse_exactly_verified": True,
        "curved_hessian_not_frozen": True, "all_frame_volume_rhs_derivatives_and_tails_retained": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
