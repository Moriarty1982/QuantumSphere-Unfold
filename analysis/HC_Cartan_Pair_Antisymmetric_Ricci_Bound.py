"""Ricci tail bound on actual double-pair-antisymmetric Cartan curvature."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "pair_ricci_parent", Path(__file__).with_name("HC_Cartan_Background_Readout_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
trace = prior.prior.prior
T, c = core.TaylorTensor, core.contract
IDENTITY_CENTER_NORM_UPPER = prior.rational_sqrt_upper(Fraction(3, 2))


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Background_Readout_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def pair_projection(value):
    """Orthogonal projection in the Euclidean Frobenius norm, last four axes."""
    value = np.asarray(value)
    if value.shape[-4:] != (4, 4, 4, 4):
        raise ValueError("Four curvature axes of length four required")
    return (value-value.swapaxes(-4, -3)-value.swapaxes(-2, -1)
            +value.swapaxes(-4, -3).swapaxes(-2, -1))*.25


def centered_operator(center):
    if np.asarray(center).shape != (4, 4):
        raise ValueError("Four-dimensional inverse center required")
    basis = pair_projection(np.eye(256).reshape(256, 4, 4, 4, 4))
    return np.einsum("ma,kb,tmkcb->tac", center, center, basis).reshape(256, 16).T


def ricci_pullback(inverse, curvature, *, actual_pair_antisymmetry):
    """An enclosure of an actual pair-antisymmetric field, not arbitrary data."""
    if actual_pair_antisymmetry is not True:
        raise ValueError("Actual curvature pair antisymmetry must be justified")
    if inverse.center.shape != (4, 4) or curvature.center.shape != (4, 4, 4, 4):
        raise ValueError("Four-dimensional inverse and curvature required")
    # R=P R implies ||R-P polynomial|| <= ||R-polynomial||. No PDE is used.
    projected = T(pair_projection(curvature.coefficients), curvature.tail)
    projection_error = float(np.linalg.norm(projected.coefficients-curvature.coefficients))
    if not np.array_equal(inverse.center, np.eye(4)):
        result, norm = trace.ricci_pullback(inverse, projected)
        return result, {"centered_ricci_pullback_operator_norm_upper": norm,
            "exact_identity_center_constant_used": False,
            "curvature_coefficient_projection_error": projection_error}
    operator = centered_operator(inverse.center)
    leading = T((curvature.coefficients.reshape(70, 256) @ operator.T).reshape(70, 4, 4),
                IDENTITY_CENTER_NORM_UPPER*curvature.tail)
    delta = inverse-core.tensor(inverse.center)
    result = (leading+c("ma,kb,mkcb->ac", delta, inverse.center, projected)
        +c("ma,kb,mkcb->ac", inverse.center, delta, projected)
        +c("ma,kb,mkcb->ac", delta, delta, projected))
    return result, {"centered_ricci_pullback_operator_norm_upper": IDENTITY_CENTER_NORM_UPPER,
        "exact_identity_center_constant_used": True,
        "curvature_coefficient_projection_error": projection_error}


def factorized_euler(inverse, volume, imag, mass, curvature, multiplier):
    y = c("cm,ma->ac", imag, inverse)
    matter = trace.trace_map(y, -1., 1.)-c(",ac->ac", mass, np.eye(4))
    ricci, diagnostics = ricci_pullback(inverse, curvature, actual_pair_antisymmetry=True)
    einstein = trace.trace_map(ricci, .5, -1.)
    result = c(",av->av", volume, trace.matrix_product(matter+einstein, inverse.transpose(1, 0)))+multiplier
    return result, {**diagnostics, "matter_frame_tail": matter.tail, "ricci_frame_tail": ricci.tail,
        "trace_reversed_gravity_tail": einstein.tail,
        "frame_sum_tail": matter.tail+einstein.tail}


def coframe_model(fields, omega, volume, inverse, cache):
    psi, dp, lam = (fields[k] for k in ("psi", "dp", "lam"))
    partial = c("ui,muj,aij->am", psi.conjugate(), dp, general.prolong.WEIGHTS).imag()
    connection = prior.centered_readout(psi, psi, omega.value, np.eye(3), cache).transpose(1, 0).scale(.5)
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    return factorized_euler(inverse, volume, partial+connection, mass, trace.curvature_model(omega), lam)


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Background_Readout_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Background readout report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), prior.prior.hermitian.load_parent()
    case, cache = control.load_case(), {}
    origin = full.field_models(case, common.RADIUS)
    prior.frozen_map(origin["psi"].center, origin["psi"].center, np.eye(3), cache)

    def run(pair):
        previous, initial = pair
        radius = previous["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, volume, inverse, ratios = full.connection_models(case[0], fields)
        coframe, pieces = coframe_model(fields, omega, volume.value, inverse, cache)
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
            "previous_ricci_frame_tail": previous["tail_diagnostics"]["ricci_frame_tail"],
            "coefficient_identity_error": float(np.linalg.norm(coefficients-old)),
            "tail_diagnostics": pieces, **ratios, "coefficients": coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Pair-antisymmetric Ricci inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "identity_center_gram_eigenvalues": {"3/2": 1, "1/2": 15},
        "identity_center_norm_upper": IDENTITY_CENTER_NORM_UPPER,
        "actual_curvature_pair_antisymmetry_required": True,
        "ricci_symmetry_pair_exchange_and_bianchi_not_assumed": True,
        "all_variable_inverse_cross_terms_retained": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_identity_center_operator_constant_is_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True,
        "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k != "coefficients"} for r in result["reports"]]}, indent=2))
