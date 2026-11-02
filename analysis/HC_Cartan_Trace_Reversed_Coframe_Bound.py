"""Factorized coframe Euler equation and four-dimensional trace-map bounds."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "trace_coframe_parent", Path(__file__).with_name("HC_Cartan_Hermitian_Curl_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.prior, prior.core, prior.control, prior.common, prior.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Hermitian_Curl_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def trace_map(value, trace_factor, sign):
    """Exact Frobenius norm on trace/traceless subspaces, without symmetry."""
    if value.center.shape != (4, 4):
        raise ValueError("The trace-map bound here is four-dimensional")
    traces = np.trace(value.coefficients, axis1=1, axis2=2)
    coefficients = sign*value.coefficients+trace_factor*traces[:, None, None]*np.eye(4)
    norm = max(abs(sign), abs(sign+4*trace_factor))
    return T(coefficients, norm*value.tail)


def curvature_model(omega):
    eta = general.prolong.ETA
    mixed = c("ab,mbc->mac", eta, omega.value)
    commutator = c("mac,ncb->mnab", mixed, mixed)
    curvature = c("mnac,cb->mnab", commutator-commutator.transpose(1, 0, 2, 3), eta)
    first = core.stack(omega.derivatives)
    return curvature+c("ac,mncd,db->mnab", eta, first-first.transpose(1, 0, 2, 3), eta)


def matrix_product(a, b):
    """Separate fixed centers so their spectral, not Frobenius, norms act on tails."""
    if a.center.ndim != 2 or b.center.ndim != 2 or a.center.shape[1] != b.center.shape[0]:
        raise ValueError("Compatible matrix models required")
    result = c("ij,jk->ik", a, b)
    an, bn = a.coefficient_norms(), b.coefficient_norms()
    discarded = float(np.sum((an[:, None]*bn[None, :])[core.HIGH]))
    result.tail = (discarded+a.tail*(np.linalg.norm(b.center, 2)+sum(bn[1:]))
        +b.tail*(np.linalg.norm(a.center, 2)+sum(an[1:]))+a.tail*b.tail)
    return result


def ricci_pullback(inverse, curvature):
    """Apply the joint constant pullback as one linear map, then retain deviations."""
    if inverse.center.shape != (4, 4) or curvature.center.shape != (4, 4, 4, 4):
        raise ValueError("Four-dimensional inverse and curvature models required")
    center = inverse.center
    basis = np.eye(256).reshape(256, 4, 4, 4, 4)
    operator = np.einsum("ma,kb,tmkcb->tac", center, center, basis).reshape(256, 16).T
    norm = float(np.linalg.norm(operator, 2))
    leading = T((curvature.coefficients.reshape(70, 256) @ operator.T).reshape(70, 4, 4),
                norm*curvature.tail)
    delta = inverse-core.tensor(center)
    result = (leading+c("ma,kb,mkcb->ac", delta, center, curvature)
        +c("ma,kb,mkcb->ac", center, delta, curvature)
        +c("ma,kb,mkcb->ac", delta, delta, curvature))
    return result, norm


def factorized_euler(inverse, volume, imag, mass, curvature, multiplier):
    """Requires the actual curvature antisymmetric in each of its index pairs."""
    y = c("cm,ma->ac", imag, inverse)
    matter = trace_map(y, -1., 1.)-c(",ac->ac", mass, np.eye(4))
    ricci, pullback_norm = ricci_pullback(inverse, curvature)
    einstein = trace_map(ricci, .5, -1.)
    coframe = c(",av->av", volume, matrix_product(matter+einstein, inverse.transpose(1, 0)))+multiplier
    return coframe, {"matter_frame_tail": matter.tail, "ricci_frame_tail": ricci.tail,
        "trace_reversed_gravity_tail": einstein.tail, "frame_sum_tail": matter.tail+einstein.tail,
        "centered_ricci_pullback_operator_norm": pullback_norm,
        "centered_right_inverse_operator_norm": float(np.linalg.norm(inverse.center, 2))}


def coframe_model(fields, omega, volume, inverse):
    psi, dp, lam = (fields[k] for k in ("psi", "dp", "lam"))
    response = c("mbc,abcij->maij", omega.value, prior.RESPONSE)
    partial = c("ui,muj,aij->am", psi.conjugate(), dp, general.prolong.WEIGHTS).imag()
    connection = c("ui,uj,maij->am", psi.conjugate(), psi, response).imag().scale(.5)
    imag = partial+connection
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    curvature = curvature_model(omega)
    model, pieces = factorized_euler(inverse, volume, imag, mass, curvature, lam)
    pieces["curvature_coefficient_pair_antisymmetry_error"] = float(np.linalg.norm(
        curvature.coefficients+curvature.coefficients.swapaxes(3, 4)))
    pieces["unweighted_readout_tail"] = imag.tail
    return model, pieces


def compact_at_point(prepared, fields):
    connection = general.connection_jets(prepared, fields)
    omega = full.TaylorJet(core.tensor(connection["omega"]), [core.tensor(v) for v in connection["first"]])
    model, _ = coframe_model(full.point_models(fields), omega,
        core.tensor(np.asarray(connection["volume"])), core.tensor(connection["inverse"]))
    return model.center


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Hermitian_Curl_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Hermitian curl report has stale inputs")
    return report


def combine_with_parent(parent_report, original, coframe):
    coefficients = np.asarray(parent_report["coefficients"]).copy()
    coefficients[:, 40:56] = coframe.coefficients.reshape(len(core.POWERS), 16)
    tails = [original["blocks"][k]["tail_bound"] for k in ("constraint", "probe")]
    return T(coefficients, float(np.linalg.norm([*tails, coframe.tail, parent_report["curl"]["tail_bound"]])))


def evaluate():
    fingerprints = input_fingerprints()
    parent, original = load_parent(), prior.load_parent()
    case = control.load_case()

    def run(pair):
        current, initial = pair
        radius = current["radius"]
        fields = full.field_models(case, radius)
        omega, _, _, volume, inverse, ratios = full.connection_models(case[0], fields)
        coframe, pieces = coframe_model(fields, omega, volume.value, inverse)
        combined = combine_with_parent(current, initial, coframe)
        previous_coframe = np.asarray(current["coefficients"])[:, 40:56]
        checks = []
        for y in (np.eye(4)[0], np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = general.equations(case[0], actual_fields)["gravity"]
            checks.append({"direction": y.tolist(), "actual_coframe_norm": float(np.linalg.norm(actual)),
                "point_identity_error": float(np.linalg.norm(actual-compact_at_point(case[0], actual_fields))),
                "coframe_tail_discrepancy": float(np.linalg.norm(actual-coframe.evaluate(y)))})
        return {"radius": radius, "coframe": full.summary(coframe), "combined": full.summary(combined),
            "previous_coframe_tail": initial["blocks"]["coframe"]["tail_bound"],
            "previous_combined_upper_estimate": current["combined"]["whole_cube_upper_estimate"],
            "coefficient_identity_error": float(np.linalg.norm(coframe.coefficients.reshape(70, 16)-previous_coframe)),
            "tail_diagnostics": pieces, **ratios, "coefficients": combined.coefficients.tolist(),
            "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, zip(parent["reports"], original["reports"])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Trace-reversed coframe inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "off-shell factorization of 16 coframe Euler rows, other 64 unchanged",
        "reports": reports, "gravity_trace_map_frobenius_operator_norm": 1.,
        "matter_trace_map_frobenius_operator_norm": 3., "ricci_symmetry_not_assumed": True,
        "no_coefficients_fitted_or_zeroed": True, "not_outward_rounded_or_interval_certified": True,
        "not_exact_low_order_closure_or_regional_solution": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k != "input_sha256"}, indent=2))
