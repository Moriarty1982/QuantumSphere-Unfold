"""Degree-four Taylor models with tails for the complete 80-row residual.

Physical coordinate derivatives are modeled independently of unknown tails.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "full_taylor_core", Path(__file__).with_name("HC_Cartan_Constitutive_Taylor_Bound.py"))
core = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(core)
control, common, general = core.control, core.common, core.general
T, c = core.TaylorTensor, core.contract


def input_fingerprints():
    result = core.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


class TaylorJet:
    """Value and four separately controlled physical derivative models."""

    def __init__(self, value, derivatives=None):
        self.value = core.tensor(value)
        self.derivatives = tuple(derivatives) if derivatives is not None else tuple(
            core.tensor(np.zeros_like(self.value.center)) for _ in range(4))
        if len(self.derivatives) != 4 or any(d.center.shape != self.value.center.shape for d in self.derivatives):
            raise ValueError("Four derivative models matching the value shape required")

    def __add__(self, other):
        other = jet(other)
        return TaylorJet(self.value+other.value, [a+b for a, b in zip(self.derivatives, other.derivatives)])

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+-jet(other)

    def scale(self, value):
        return TaylorJet(self.value.scale(value), [d.scale(value) for d in self.derivatives])

    def conjugate(self):
        return TaylorJet(self.value.conjugate(), [d.conjugate() for d in self.derivatives])

    def real(self):
        return TaylorJet(self.value.real(), [d.real() for d in self.derivatives])

    def transpose(self, *axes):
        return TaylorJet(self.value.transpose(*axes), [d.transpose(*axes) for d in self.derivatives])


def jet(value):
    return value if isinstance(value, TaylorJet) else TaylorJet(value)


def jc(expression, *values):
    values = tuple(jet(value) for value in values)
    ordinary = [value.value for value in values]
    derivatives = []
    for r in range(4):
        parts = [c(expression, *(ordinary[:i]+[value.derivatives[r]]+ordinary[i+1:]))
                 for i, value in enumerate(values)]
        total = parts[0]
        for part in parts[1:]:
            total = total+part
        derivatives.append(total)
    return TaylorJet(c(expression, *ordinary), derivatives)


def reshape(value, shape):
    return T(value.coefficients.reshape(len(core.POWERS), *shape), value.tail)


def vectorize(values):
    return T(np.concatenate([v.coefficients.reshape(len(core.POWERS), -1) for v in values], axis=1),
             float(np.linalg.norm([v.tail for v in values])))


def base_derivative(derivatives, radius, order):
    sample = derivatives[order]
    coefficients = np.zeros((len(core.POWERS), *sample.shape), dtype=sample.dtype)
    for p in core.POWERS:
        degree = sum(p)
        if degree+order not in derivatives:
            continue
        indices = tuple(i for i in range(4) for _ in range(p[i]))
        value = derivatives[degree+order][indices] if indices else derivatives[degree+order]
        coefficients[core.INDEX[p]] = value*radius**degree/math.prod(math.factorial(a) for a in p)
    return T(coefficients)


def field_models(case, radius):
    result = core.field_models(case, radius)
    _, point, jets, full, ordinary, _, coefficients = case
    ed = {2: point["coframe_second"], 3: jets["e3"], 4: full["e4"]}
    ld = {1: point["multiplier_first"], 2: jets["l2"], 3: full["l3"]}
    result["dde"] = base_derivative(ed, radius, 2)
    result["dl"] = base_derivative(ld, radius, 1)
    old_e, old_p = 16*len(common.E5), 40*len(common.E5)
    new_e, new_p = 16*len(control.parent.E6), 16*len(control.parent.E6)+24*len(control.parent.P5)
    for powers, values in ((common.E5, ordinary[:old_e].reshape(-1, 4, 4)),
                           (control.parent.E6, coefficients[:new_e].reshape(-1, 4, 4))):
        addition = core.stack([core.stack([core.monomial_terms(powers, values, common.RADIUS**2,
            radius, (r, s)) for s in range(4)]) for r in range(4)])
        result["dde"] = result["dde"]+addition
    for powers, values in ((common.L4, ordinary[old_p:].reshape(-1, 4, 4)),
                           (control.parent.P5, coefficients[new_p:].reshape(-1, 4, 4))):
        result["dl"] = result["dl"]+core.stack([core.monomial_terms(powers, values, common.RADIUS,
            radius, (r,)) for r in range(4)])
    return result


def connection_models(prepared, fields):
    e = TaylorJet(fields["e"], [fields["de"][r] for r in range(4)])
    de = TaylorJet(fields["de"], [fields["dde"][r] for r in range(4)])
    inverse, e_ratio = core.matrix_inverse(e.value)
    if np.linalg.det(e.value.center) <= 0:
        raise ValueError("Positive coframe orientation required")
    volume = core.determinant(e.value)
    dinverse = -c("ma,rav,vb->rmb", inverse, fields["de"], inverse)
    dvolume = c(",ma,ram->r", volume, inverse, fields["de"])
    inv = TaylorJet(inverse, [dinverse[r] for r in range(4)])
    vol = TaylorJet(volume, [dvolume[r] for r in range(4)])
    psi = TaylorJet(fields["psi"], [fields["dp"][r] for r in range(4)])
    lam = TaylorJet(fields["lam"], [fields["dl"][r] for r in range(4)])
    forms, eta = prepared["component_forms"], general.prolong.ETA
    components = jc("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = jc(",ma,pam->p", vol, inv, components)
    response = jc("ui,pamij,uj->amp", psi.conjugate(), forms, jc("uv,vj->uj", general.prolong.Q, psi)).real().scale(-1)
    hessian = jc(",ma,nb,pqmnab->pq", vol, inv, inv, prepared["curvature_hessian"]).scale(.5)
    hinv, h_ratio = core.matrix_inverse(hessian.value)
    inverse_hessian = TaylorJet(hinv, [-c("pa,ab,bq->pq", hinv, dh, hinv) for dh in hessian.derivatives])
    k = jc("pq,q->p", inverse_hessian, -source+jc("amp,am->p", response, lam))
    metric_inverse = jc("ma,ab,nb->mn", inv, eta, inv)
    metric_first = jc("ram,ab,bv->rmv", de, eta, e)+jc("am,ab,rbv->rmv", e, eta, de)
    lower = (metric_first.transpose(1, 0, 2)+metric_first.transpose(1, 2, 0)-metric_first).scale(.5)
    gamma = jc("as,sbc->abc", metric_inverse, lower)
    lc = jc("ab,mbv,vc->mac", eta, jc("ap,pmq->maq", e, gamma)-de, inv)
    omega = lc+jc("p,pmab->mab", k, general.cartan.OMEGA_BASIS)
    spin = jc("mab,aij,bjk->mik", omega, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    weights = jc(",ma,aij->mij", vol, inv, general.prolong.FLAT_WEIGHTS)+jc("am,aij->mij", lam, general.prolong.Q_WEIGHTS)
    return omega, spin, weights, vol, inverse, {"coframe_neumann_ratio": e_ratio, "hessian_neumann_ratio": h_ratio}


def residual_models(prepared, fields):
    omega, spin, weights, volume_jet, inverse, ratios = connection_models(prepared, fields)
    e, de, psi, dp, lam = (fields[k] for k in ("e", "de", "psi", "dp", "lam"))
    volume = volume_jet.value
    eta, selector, frame_weights = general.prolong.ETA, general.prolong.Q, general.prolong.WEIGHTS
    covariant = dp+c("mij,uj->mui", spin.value, psi)
    constraint = c("ui,uv,mvj,aij->am", psi.conjugate(), selector, covariant, frame_weights).imag()-e
    spin_full = reshape(c("uv,mij->muivj", np.eye(3), spin.value), (4, 12, 12))
    divergence = weights.derivatives[0][0]
    for r in range(1, 4):
        divergence = divergence+weights.derivatives[r][r]
    defect = divergence-c("mji,mjk->ik", spin_full.conjugate(), weights.value)-c("mij,mjk->ik", weights.value, spin_full)
    probe = (c("mij,mj->i", weights.value, reshape(covariant, (4, 12))).scale(1j)
             -c(",ij,j->i", volume, general.prior.joint.prior.MASS_WEIGHT, reshape(psi, (12,)))
             +c("ij,j->i", defect, reshape(psi, (12,))).scale(.5j))
    real_probe = T(np.concatenate((probe.coefficients.real, probe.coefficients.imag), axis=1), probe.tail)
    mixed = c("ab,mbc->mac", eta, omega.value)
    commutator = c("mac,ncb->mnab", mixed, mixed)
    curvature = c("mnac,cb->mnab", commutator-commutator.transpose(1, 0, 2, 3), eta)
    first = core.stack(omega.derivatives)
    curvature = curvature+c("ac,mncd,db->mnab", eta, first-first.transpose(1, 0, 2, 3), eta)
    imag = c("ui,muj,aij->am", psi.conjugate(), covariant, frame_weights).imag()
    mass = c("ui,uv,vj,ij->", psi.conjugate(), general.prolong.MASS, psi, general.cartan.BETA).real()
    ld = -c(",->", volume, c("ma,am->", inverse, imag)+mass)
    lg = c(",ma,nb,mnab->", volume, inverse, inverse, curvature).scale(.5)
    gravity = (c(",va->av", ld+lg, inverse)+c(",ma,ab,bv->mv", volume, inverse, imag, inverse).transpose(1, 0)+lam
        -c(",ma,vc,kb,mkcb->av", volume, inverse, inverse, inverse, curvature).scale(.5)
        -c(",mc,ka,vb,mkcb->av", volume, inverse, inverse, inverse, curvature).scale(.5))
    curls = []
    for r in range(4):
        for s in range(r+1, 4):
            difference = (c("ij,uj->ui", spin.derivatives[r][s]-spin.derivatives[s][r], psi)
                +c("uj,ij->ui", dp[r], spin.value[s])-c("uj,ij->ui", dp[s], spin.value[r]))
            cross = (c("ui,uv,vj,aij->a", dp[r].conjugate(), selector, covariant[s], frame_weights)
                -c("ui,uv,vj,aij->a", dp[s].conjugate(), selector, covariant[r], frame_weights)
                +c("ui,uv,vj,aij->a", psi.conjugate(), selector, difference, frame_weights)).imag()
            curls.append(cross-de[r, :, s]+de[s, :, r])
    blocks = {"constraint": constraint, "probe": real_probe, "coframe": gravity, "curls": vectorize(curls)}
    return vectorize(list(blocks.values())), blocks, ratios


def summary(model):
    norms = model.coefficient_norms()
    levels = [float(sum(norms[core.DEGREES == k])) for k in range(5)]
    return {"coefficient_level_bounds": levels, "tail_bound": model.tail,
            "whole_cube_upper_estimate": sum(levels)+model.tail}


def point_models(fields):
    mapping = {"e": "coframe", "de": "coframe_first", "dde": "coframe_second", "psi": "psi",
               "dp": "psi_first", "lam": "multiplier", "dl": "multiplier_first"}
    return {key: core.tensor(fields[name]) for key, name in mapping.items()}


def evaluate():
    fingerprints = input_fingerprints()
    case = control.load_case()

    def run(radius):
        model, blocks, ratios = residual_models(case[0], field_models(case, radius))
        checks = []
        for y in (np.eye(4)[0], np.array([.5, -.5, .5, -.5]), np.array([.2, -.3, .1, .4]),
                  np.ones(4), np.array([-1., 1., -1., 1.])):
            fields, _ = control.fields_and_higher(case, radius*y)
            actual = common.lower.lower_residual(case[0], fields)
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "polynomial_norm": float(np.linalg.norm(model.evaluate(y))),
                "tail_discrepancy": float(np.linalg.norm(actual-model.evaluate(y)))})
        return {"radius": radius, **summary(model), **ratios,
            "blocks": {key: summary(value) for key, value in blocks.items()},
            "coefficients": model.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, (common.RADIUS, common.RADIUS/2)))
    point_checks = []
    for y in (np.zeros(4), np.ones(4)):
        fields, _ = control.fields_and_higher(case, common.RADIUS*y)
        model, _, _ = residual_models(case[0], point_models(fields))
        actual = common.lower.lower_residual(case[0], fields)
        point_checks.append({"direction": y.tolist(), "tail": model.tail,
            "actual_norm": float(np.linalg.norm(actual)), "match_error": float(np.linalg.norm(actual-model.center))})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Full Taylor inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "degree-four Taylor polynomial plus whole-cube tail for all 80 equations",
        "row_count": 80, "retained_degree": 4, "reports": reports, "point_controls": point_checks,
        "physical_derivative_models_built_from_original_polynomial": True,
        "no_coefficients_fitted_or_zeroed": True, "not_outward_rounded_or_interval_certified": True,
        "not_exact_low_order_vanishing_or_regional_solution": True,
        "not_distance_to_solution_or_PDE_convergence": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k != "input_sha256"}, indent=2))
