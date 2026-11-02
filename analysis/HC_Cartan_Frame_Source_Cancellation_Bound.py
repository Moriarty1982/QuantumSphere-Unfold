"""Exact source support cancellation before the curved Cartan solve bounds."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "source_cancellation_parent", Path(__file__).with_name("HC_Cartan_Frame_Factorized_Solve_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Frame_Factorized_Solve_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def source_support_certificate(forms):
    forms = np.asarray(forms)
    if forms.shape != (24, 4, 4, 4, 4) or not np.all(np.isfinite(forms)):
        raise ValueError("Finite Cartan component forms with shape (24,4,4,4,4) required")
    flat = forms[:6, :, 0].copy()
    expected = np.zeros_like(forms)
    for mu in range(4):
        expected[6*mu:6*mu+6, :, mu] = flat
    if not np.array_equal(forms, expected):
        raise ValueError("Exact coordinate-support identity failed")
    return flat, {"coordinate_blocks_checked": 16,
        "identity": "F_(mu,l),a,m = delta_(m,mu) Fflat_l,a",
        "exact_coefficient_equality_not_tolerance": True,
        "coefficient_sha256": hashlib.sha256(np.asarray(forms, dtype=np.complex128).tobytes()).hexdigest()}


def reshape_jet(value, shape):
    return J(full.reshape(value.value, shape), [full.reshape(d, shape) for d in value.derivatives])


def source_solve(coframe, volume, psi, lam, forms, flat_inverse, cache):
    flat, _ = source_support_certificate(forms)
    spinor = jc("ui,laij,uj->la", psi.conjugate(), flat, psi).real()
    weighted = jc("ui,laij,uj->la", psi.conjugate(), flat,
        jc("uv,vj->uj", general.prolong.Q, psi)).real()
    multiplier_frame = jc("am,rm->ar", lam, coframe)
    channel = jc("ar,la->rl", multiplier_frame, weighted)
    reciprocal, ratio = prior.reciprocal_volume(volume)
    effective = spinor.transpose(1, 0)+jc(",rl->rl", reciprocal, channel)
    middle = prior.matrix_vector_jet(J(flat_inverse), reshape_jet(effective, (24,)), cache)
    left = J(prior.lift(coframe.value, True), [prior.lift(d, True) for d in coframe.derivatives])
    return -prior.matrix_vector_jet(left, middle, cache), ratio


def connection_models(prepared, fields, flat_inverse, cache):
    lc, volume, inverse, e_ratio = prior.prior.implicit.geometry_models(fields)
    psi = J(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = J(fields["lam"], [fields["dl"][r] for r in range(4)])
    coframe = J(fields["e"], [fields["de"][r] for r in range(4)])
    k, ratio = source_solve(coframe, volume, psi, lam, prepared["component_forms"], flat_inverse, cache)
    return lc+prior.prior.implicit.embed_jet(k), volume, inverse.value, {
        "coframe_neumann_ratio": e_ratio, "volume_reciprocal_neumann_ratio": ratio}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Frame_Factorized_Solve_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Frame-factorized solve report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case = load_parent(), control.load_case()
    flat_inverse, hessian_certificate = prior.factorization_certificate(case[0]["curvature_hessian"])
    _, certificate = source_support_certificate(case[0]["component_forms"])

    def run(previous):
        radius = previous["radius"]
        fields, maps = full.field_models(case, radius), {}
        omega, volume, inverse, ratios = connection_models(case[0], fields, flat_inverse, {})
        old, _, _, _ = prior.connection_models(case[0], fields, flat_inverse, {})
        constraint, _ = prior.prior.prior.constraint_model(fields, omega, maps)
        probe, _ = prior.prior.prior.prior.prior.probe_model(fields, omega, volume, inverse)
        coframe, _ = prior.prior.implicit.prior.coframe_model(fields, omega, volume.value, inverse, maps)
        curls, _ = prior.prior.prior.prior.curl_model(fields, omega, maps)
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
            "combined": full.summary(combined),
            "previous_combined_upper_estimate": previous["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(combined.coefficients-np.asarray(previous["coefficients"]))),
            "connection_diagnostics": {"old_value_tail": old.value.tail, "new_value_tail": omega.value.tail,
                "old_derivative_tails": [d.tail for d in old.derivatives],
                "new_derivative_tails": [d.tail for d in omega.derivatives],
                "value_coefficient_error": float(np.linalg.norm(omega.value.coefficients-old.value.coefficients)),
                "derivative_coefficient_error": float(np.linalg.norm(np.stack([a.coefficients-b.coefficients
                    for a, b in zip(omega.derivatives, old.derivatives)])))},
            **ratios, "coefficients": combined.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Source cancellation inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "source_support_certificate": certificate, "hessian_certificate": hessian_certificate,
        "identity": "k=-(E^T tensor I6) H0^-1 vec(T^T+v^-1 (lambda E^T)^T U^T)",
        "spinor_source_volume_and_inverse_cancelled_algebraically": True,
        "multiplier_channel_and_all_its_derivatives_retained": True,
        "all_frame_spinor_volume_derivatives_and_tails_retained": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
