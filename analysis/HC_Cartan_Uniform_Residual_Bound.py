"""Whole-ball residual majorants for the saved quartic-corrected germ.

Real-arithmetic enclosures evaluated in floats, not a fifth-order certificate.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "uniform_residual_derivative", Path(__file__).with_name("HC_Cartan_Quartic_Derivative_Control.py"))
previous = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(previous)
common, general, uniform = previous.common, previous.general, previous.uniform
B, c = uniform.TensorBall, uniform.contract


def input_fingerprints():
    result = previous.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Quartic_Derivative_Control.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


class FirstJet:
    """A value ball and its four coordinate derivative balls."""

    def __init__(self, value, derivatives=None):
        self.value = uniform.ball(value)
        self.derivatives = tuple(derivatives) if derivatives is not None else tuple(
            B(np.zeros_like(self.value.center)) for _ in range(4))
        if len(self.derivatives) != 4 or any(d.center.shape != self.value.center.shape for d in self.derivatives):
            raise ValueError("Four derivative balls with the value shape required")

    def __add__(self, other):
        other = jet(other)
        return FirstJet(self.value+other.value, [a+b for a, b in zip(self.derivatives, other.derivatives)])

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+-jet(other)

    def scale(self, value):
        return FirstJet(self.value.scale(value), [d.scale(value) for d in self.derivatives])

    def conjugate(self):
        return FirstJet(self.value.conjugate(), [d.conjugate() for d in self.derivatives])

    def real(self):
        return FirstJet(self.value.real(), [d.real() for d in self.derivatives])

    def transpose(self, *axes):
        return FirstJet(self.value.transpose(*axes), [d.transpose(*axes) for d in self.derivatives])


def jet(value):
    return value if isinstance(value, FirstJet) else FirstJet(value)


def jc(expression, *values):
    """Product-rule lift of the existing multilinear ball contraction."""
    values = tuple(jet(value) for value in values)
    centers = [value.value for value in values]
    derivatives = []
    for r in range(4):
        parts = [c(expression, *(centers[:i]+[value.derivatives[r]]+centers[i+1:]))
                 for i, value in enumerate(values)]
        total = parts[0]
        for part in parts[1:]:
            total = total+part
        derivatives.append(total)
    return FirstJet(c(expression, *centers), derivatives)


def stack(values):
    return B(np.stack([v.center for v in values]), float(np.linalg.norm([v.radius for v in values])))


def vectorize(values):
    return B(np.concatenate([v.center.ravel() for v in values]), float(np.linalg.norm([v.radius for v in values])))


def field_balls(case, radius):
    prepared, point, jets, full, ordinary, spinor, coefficients = case
    balls, _ = previous.refreshed_balls(case, radius)
    old_e, old_p = 16*len(common.E5), 40*len(common.E5)
    new_e, new_p = 16*len(previous.parent.E6), 16*len(previous.parent.E6)+24*len(previous.parent.P5)
    pbound = previous.polynomial_bound
    dp_extra = previous.correction_bounds(case, radius)["psi1"]
    dp_radius = (np.linalg.norm(jets["p2"])*radius+np.linalg.norm(jets["p3"])*radius**2/2
                 +np.linalg.norm(full["p4"])*radius**3/6+dp_extra)
    dde_radius = (np.linalg.norm(jets["e3"])*radius+np.linalg.norm(full["e4"])*radius**2/2
        +pbound(common.E5, ordinary[:old_e].reshape(-1, 16), common.RADIUS**2, radius, 2)
        +pbound(previous.parent.E6, coefficients[:new_e].reshape(-1, 16), common.RADIUS**2, radius, 2))
    dl_radius = (np.linalg.norm(jets["l2"])*radius+np.linalg.norm(full["l3"])*radius**2/2
        +pbound(common.L4, ordinary[old_p:].reshape(-1, 16), common.RADIUS, radius, 1)
        +pbound(previous.parent.P5, coefficients[new_p:].reshape(-1, 16), common.RADIUS, radius, 1))
    balls.update({"dde": B(point["coframe_second"], float(dde_radius)),
                  "dp": B(point["psi_first"], float(dp_radius)),
                  "dl": B(point["multiplier_first"], float(dl_radius))})
    return balls


def point_balls(prepared, fields):
    """Zero-radius controls from an independently evaluated coframe inverse."""
    connection = general.connection_jets(prepared, fields)
    mapping = {"e": "coframe", "de": "coframe_first", "dde": "coframe_second", "psi": "psi",
               "dp": "psi_first", "lam": "multiplier", "dl": "multiplier_first"}
    balls = {key: B(fields[name]) for key, name in mapping.items()}
    balls.update({"inverse": B(connection["inverse"]), "volume": B(np.asarray(connection["volume"])),
                  "hessian_inverse": B(np.linalg.inv(connection["hessian"]))})
    return balls


def connection_balls(prepared, balls):
    e = FirstJet(balls["e"], [balls["de"][r] for r in range(4)])
    de = FirstJet(balls["de"], [balls["dde"][r] for r in range(4)])
    inverse, volume = balls["inverse"], balls["volume"]
    dinverse = -c("ma,rav,vb->rmb", inverse, balls["de"], inverse)
    dvolume = c(",ma,ram->r", volume, inverse, balls["de"])
    inv = FirstJet(inverse, [dinverse[r] for r in range(4)])
    vol = FirstJet(volume, [dvolume[r] for r in range(4)])
    psi = FirstJet(balls["psi"], [balls["dp"][r] for r in range(4)])
    lam = FirstJet(balls["lam"], [balls["dl"][r] for r in range(4)])
    forms, eta = prepared["component_forms"], general.prolong.ETA
    components = jc("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = jc(",ma,pam->p", vol, inv, components)
    response = jc("ui,pamij,uj->amp", psi.conjugate(), forms, jc("uv,vj->uj", general.prolong.Q, psi)).real().scale(-1)
    hessian = jc(",ma,nb,pqmnab->pq", vol, inv, inv, prepared["curvature_hessian"]).scale(.5)
    hinv = balls["hessian_inverse"]
    inverse_hessian = FirstJet(hinv, [-c("pa,ab,bq->pq", hinv, dh, hinv) for dh in hessian.derivatives])
    k = jc("pq,q->p", inverse_hessian, -source+jc("amp,am->p", response, lam))
    metric_inverse = jc("ma,ab,nb->mn", inv, eta, inv)
    metric_first = jc("ram,ab,bv->rmv", de, eta, e)+jc("am,ab,rbv->rmv", e, eta, de)
    lower = (metric_first.transpose(1, 0, 2)+metric_first.transpose(1, 2, 0)-metric_first).scale(.5)
    gamma = jc("as,sbc->abc", metric_inverse, lower)
    lc = jc("ab,mbv,vc->mac", eta, jc("ap,pmq->maq", e, gamma)-de, inv)
    omega = lc+jc("p,pmab->mab", k, general.cartan.OMEGA_BASIS)
    spin = jc("mab,aij,bjk->mik", omega, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    weights = jc(",ma,aij->mij", vol, inv, general.prolong.FLAT_WEIGHTS)+jc("am,aij->mij", lam, general.prolong.Q_WEIGHTS)
    return omega, spin, weights, vol


def residual_ball(prepared, balls):
    """Enclose all 80 actual residuals without assuming their Taylor cancellations."""
    omega, spin, weights, volume_jet = connection_balls(prepared, balls)
    e, de, psi, dp, lam = (balls[key] for key in ("e", "de", "psi", "dp", "lam"))
    inverse, volume = balls["inverse"], volume_jet.value
    eta, selector, frame_weights = general.prolong.ETA, general.prolong.Q, general.prolong.WEIGHTS
    covariant = dp+c("mij,uj->mui", spin.value, psi)
    constraint = c("ui,uv,mvj,aij->am", psi.conjugate(), selector, covariant, frame_weights).imag()-e
    spin_full = c("uv,mij->muivj", np.eye(3), spin.value).reshape(4, 12, 12)
    divergence = weights.derivatives[0][0]
    for r in range(1, 4):
        divergence = divergence+weights.derivatives[r][r]
    defect = divergence-c("mji,mjk->ik", spin_full.conjugate(), weights.value)-c("mij,mjk->ik", weights.value, spin_full)
    probe = (c("mij,mj->i", weights.value, covariant.reshape(4, 12)).scale(1j)
             -c(",ij,j->i", volume, general.prior.joint.prior.MASS_WEIGHT, psi.reshape(12))
             +c("ij,j->i", defect, psi.reshape(12)).scale(.5j))
    real_probe = B(np.r_[probe.center.real, probe.center.imag], probe.radius)
    mixed = c("ab,mbc->mac", eta, omega.value)
    commutator = c("mac,ncb->mnab", mixed, mixed)
    curvature = c("mnac,cb->mnab", commutator-commutator.transpose(1, 0, 2, 3), eta)
    first = stack(omega.derivatives)
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
    return vectorize(list(blocks.values())), blocks


def evaluate():
    fingerprints = input_fingerprints()
    case = previous.load_case()
    parent_report = json.loads(Path(__file__).with_name("HC_Cartan_Quartic_Derivative_Control.json").read_text(encoding="utf-8"))
    if parent_report["input_sha256"] != previous.input_fingerprints():
        raise ValueError("Derivative control has stale inputs")
    chart_radius = parent_report["refreshed_normal_chart"]["radius"]
    origin_fields, _ = previous.fields_and_higher(case, np.zeros(4))
    origin_actual = common.lower.lower_residual(case[0], origin_fields)

    def bound_at(radius):
        bound, blocks = residual_ball(case[0], field_balls(case, radius))
        checks = []
        for direction in (np.eye(4)[0], np.array([.5, -.5, .5, -.5])):
            fields, _ = previous.fields_and_higher(case, radius*direction)
            actual = common.lower.lower_residual(case[0], fields)
            checks.append({"direction": direction.tolist(), "residual_norm": float(np.linalg.norm(actual)),
                "distance_from_ball_center": float(np.linalg.norm(actual-bound.center))})
        return {"radius": radius, "variation_majorant": bound.radius,
            "center_norm": float(np.linalg.norm(bound.center)),
            "origin_center_match_error": float(np.linalg.norm(bound.center-origin_actual)),
            "full_residual_upper_estimate": float(np.linalg.norm(bound.center)+bound.radius),
            "blocks": {key: {"center_norm": float(np.linalg.norm(value.center)), "variation_majorant": value.radius}
                       for key, value in blocks.items()}, "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        bounds = list(pool.map(bound_at, [common.RADIUS, common.RADIUS/2, chart_radius, chart_radius/2]))
    point_checks = []
    for direction in (np.zeros(4), np.eye(4)[0], np.array([.2, -.3, .1, .4])):
        fields, _ = previous.fields_and_higher(case, common.RADIUS*direction)
        actual = common.lower.lower_residual(case[0], fields)
        point, _ = residual_ball(case[0], point_balls(case[0], fields))
        point_checks.append({"direction": direction.tolist(), "zero_radius": point.radius,
            "match_error": float(np.linalg.norm(actual-point.center)), "actual_norm": float(np.linalg.norm(actual))})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Uniform residual inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "natural whole-ball majorant for all 80 residuals of the rounded polynomial",
        "bounds": bounds, "point_controls": point_checks, "two_bounded_local_workers": True,
        "no_new_coefficients_fitted": True, "retains_nonzero_origin_residual": True,
        "not_a_fifth_order_Taylor_remainder_bound": True, "not_outward_rounded_or_interval_certified": True,
        "not_distance_to_exact_solution_or_convergence_proof": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
