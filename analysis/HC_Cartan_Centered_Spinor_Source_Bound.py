"""Centered Hermitian spinor sources, retaining quadratic deviations."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "centered_source_parent", Path(__file__).with_name("HC_Cartan_Frame_Source_Cancellation_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
full, core, control, common, general = prior.full, prior.core, prior.control, prior.common, prior.general
T, c, J, jc = core.TaylorTensor, core.contract, full.TaylorJet, full.jc
frame = prior.prior
implicit = frame.prior.implicit
readout = frame.prior.readout
constraint_core = frame.prior.prior
projector = constraint_core.prior
probe_core = projector.prior


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Frame_Source_Cancellation_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def frozen_source(center, forms, selector, cache):
    center, forms, selector = [np.asarray(v, dtype=np.complex128) for v in (center, forms, selector)]
    if ([v.shape for v in (center, forms, selector)] != [(3, 4), (6, 4, 4, 4), (3, 3)]
            or not all(np.all(np.isfinite(v)) for v in (center, forms, selector))):
        raise ValueError("Finite spinor, flat forms and channel selector required")
    if not np.array_equal(selector, selector.conj().T):
        raise ValueError("Exactly Hermitian selector required")
    key = tuple(v.tobytes() for v in (center, forms, selector))
    if key not in cache:
        z = readout.exact_matrix(center.reshape(12, 1))
        q = readout.exact_matrix(selector)
        rows, constants = [], []
        for l in range(6):
            for a in range(4):
                f = readout.exact_matrix(forms[l, a])
                h = (f+f.H)/2
                operator = sp.kronecker_product(q, h)
                row = z.H*operator
                rows.append([2*sp.re(sp.expand(v)) for v in row]
                    +[-2*sp.im(sp.expand(v)) for v in row])
                constants.append(sp.re(sp.expand((row*z)[0])))
        exact = sp.Matrix(rows)
        gram = exact*exact.T
        bound = max(sum(abs(gram[i, j]) for j in range(24)) for i in range(24))
        upper = readout.rational_sqrt_upper(Fraction(int(bound.p), int(bound.q)))
        cache[key] = {"matrix": np.array(exact.tolist(), float),
            "constant": np.array(constants, float).reshape(6, 4), "upper": upper,
            "exact_coefficients": [[str(v) for v in row] for row in exact.tolist()],
            "exact_gram_row_bound": str(bound),
            "forms": (forms+forms.conj().swapaxes(-1, -2))*.5}
    return cache[key]


def realify(value):
    if value.center.shape != (3, 4):
        raise ValueError("Three four-component spinor channels required")
    coefficients = value.coefficients.reshape(70, 12)
    return T(np.concatenate((coefficients.real, coefficients.imag), axis=1), value.tail)


def centered_source(psi, forms, selector, cache):
    fixed = frozen_source(psi.value.center, forms, selector, cache)
    delta = psi-J(psi.value.center)
    def linear(value):
        real = realify(value)
        return T((real.coefficients @ fixed["matrix"].T).reshape(70, 6, 4), fixed["upper"]*real.tail)
    tangent = J(linear(delta.value), [linear(d) for d in delta.derivatives])
    quadratic = jc("ui,uv,laij,vj->la", delta.conjugate(), selector, fixed["forms"], delta).real()
    return J(fixed["constant"])+tangent+quadratic


def connection_models(prepared, fields, flat_inverse, cache):
    lc, volume, inverse, e_ratio = implicit.geometry_models(fields)
    psi = J(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = J(fields["lam"], [fields["dl"][r] for r in range(4)])
    coframe = J(fields["e"], [fields["de"][r] for r in range(4)])
    forms, _ = prior.source_support_certificate(prepared["component_forms"])
    spinor = centered_source(psi, forms, np.eye(3), cache)
    weighted = centered_source(psi, forms, general.prolong.Q, cache)
    channel = jc("ar,la->rl", jc("am,rm->ar", lam, coframe), weighted)
    reciprocal, ratio = frame.reciprocal_volume(volume)
    effective = spinor.transpose(1, 0)+jc(",rl->rl", reciprocal, channel)
    middle = frame.matrix_vector_jet(J(flat_inverse), prior.reshape_jet(effective, (24,)), {})
    left = J(frame.lift(coframe.value, True), [frame.lift(d, True) for d in coframe.derivatives])
    k = -frame.matrix_vector_jet(left, middle, {})
    candidate = lc+implicit.embed_jet(k)
    previous, _, _, _ = prior.connection_models(prepared, fields, flat_inverse, {})
    # Keep each derivative's entire controlled model, not just its smaller tail.
    omega = J(candidate.value, previous.derivatives)
    return omega, volume, inverse.value, {
        "coframe_neumann_ratio": e_ratio, "volume_reciprocal_neumann_ratio": ratio,
        "centered_candidate_derivative_tails": [d.tail for d in candidate.derivatives]}


def load_parent():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Frame_Source_Cancellation_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Source cancellation report has stale inputs")
    return report


def evaluate():
    fingerprints = input_fingerprints()
    parent, case = load_parent(), control.load_case()
    flat_inverse, _ = frame.factorization_certificate(case[0]["curvature_hessian"])

    def run(previous):
        radius = previous["radius"]
        fields, maps, cache = full.field_models(case, radius), {}, {}
        omega, volume, inverse, ratios = connection_models(case[0], fields, flat_inverse, cache)
        old, _, _, _ = prior.connection_models(case[0], fields, flat_inverse, {})
        constraint, _ = constraint_core.constraint_model(fields, omega, maps)
        probe, _ = probe_core.probe_model(fields, omega, volume, inverse)
        coframe, _ = implicit.prior.coframe_model(fields, omega, volume.value, inverse, maps)
        curls, _ = projector.curl_model(fields, omega, maps)
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
            "frozen_sources": [{k: v for k, v in entry.items() if k not in ("matrix", "constant", "forms")}
                for entry in cache.values()],
            **ratios, "coefficients": combined.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, parent["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Centered spinor source inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "identity": "B(z0+dz)=B(z0)+2 Re(z0^dagger K dz)+B(dz)",
        "quadratic_deviations_and_all_physical_derivatives_retained": True,
        "complete_parent_derivative_models_retained_not_tail_swapped": True,
        "hermitian_selector_checked_not_assumed": True, "realification_tail_isometry_used": True,
        "no_coefficients_fitted_or_low_order_defects_zeroed": True,
        "only_fixed_map_norm_constants_exactly_certified": True,
        "not_a_full_outward_rounded_certificate": True,
        "not_exact_closure_regional_solution_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"reports": [{k: v for k, v in r.items() if k not in ("coefficients", "frozen_sources")}
        for r in result["reports"]]}, indent=2))
