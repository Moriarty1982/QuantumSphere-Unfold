"""Analytic Frobenius-ball majorants for the general normal coefficient matrix.

Uniform real-arithmetic estimates evaluated in floats, not interval arithmetic.
"""
import argparse
from dataclasses import dataclass
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "uniform_normal_general", Path(__file__).with_name("HC_Cartan_General_Normal_Chart.py"))
general = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(general)
prior = general.prior


@dataclass(frozen=True, slots=True)
class TensorBall:
    center: np.ndarray
    radius: float = 0.

    def __post_init__(self):
        value = np.asarray(self.center)
        if not np.all(np.isfinite(value)) or not np.isfinite(self.radius) or self.radius < 0:
            raise ValueError("Finite tensor center and nonnegative Frobenius radius required")
        object.__setattr__(self, "center", value)

    def __add__(self, other):
        other = ball(other)
        if self.center.shape != other.center.shape:
            raise ValueError("Tensor-ball addition does not broadcast")
        return TensorBall(self.center+other.center, self.radius+other.radius)

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+-ball(other)

    def scale(self, value):
        return TensorBall(self.center*value, self.radius*abs(value))

    def reshape(self, *shape):
        return TensorBall(self.center.reshape(*shape), self.radius)

    def transpose(self, *axes):
        return TensorBall(self.center.transpose(*axes), self.radius)

    def conjugate(self):
        return TensorBall(self.center.conj(), self.radius)

    def real(self):
        return TensorBall(self.center.real, self.radius)

    def imag(self):
        return TensorBall(self.center.imag, self.radius)

    def __getitem__(self, index):
        # Only basic slices/integers: advanced indexing can duplicate entries.
        indices = index if isinstance(index, tuple) else (index,)
        if any(not isinstance(i, (slice, int)) for i in indices):
            raise ValueError("Only contractive basic tensor slices supported")
        return TensorBall(self.center[index], self.radius)


def ball(value):
    return value if isinstance(value, TensorBall) else TensorBall(np.asarray(value))


def contract(expression, *values):
    """Multilinear Frobenius bound, excluding within-operand diagonal traces."""
    values = tuple(ball(v) for v in values)
    inputs, output = expression.split("->")
    labels = inputs.split(",")
    if len(labels) != len(values):
        raise ValueError("Wrong number of tensor contraction operands")
    dimensions, occurrences = {}, {}
    for name, value in zip(labels, values):
        if len(name) != value.center.ndim or len(set(name)) != len(name):
            raise ValueError("Explicit distinct indices in each operand required")
        for label, size in zip(name, value.center.shape):
            if label in dimensions and dimensions[label] != size:
                raise ValueError("Tensor contraction dimensions disagree")
            dimensions[label] = size
            occurrences[label] = occurrences.get(label, 0)+1
    factor = np.prod([np.sqrt(dimensions[k]) for k, count in occurrences.items()
                      if count == 1 and k not in output])
    radius, product = 0., 1.
    for value in values:
        norm = float(np.linalg.norm(value.center))
        radius = radius*(norm+value.radius)+product*value.radius
        product *= norm
    return TensorBall(np.einsum(expression, *(v.center for v in values), optimize=True), float(factor*radius))


def stack_blocks(blocks):
    return TensorBall(np.concatenate([b.center for b in blocks], axis=1),
                      float(np.sqrt(sum(b.radius*b.radius for b in blocks))))


def input_fingerprints():
    result = general.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_General_Normal_Chart.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def normal_basis():
    p, lam, dde = np.zeros((56, 3, 4), complex), np.zeros((56, 4, 4)), np.zeros((56, 4, 4, 4, 4))
    for n, value in enumerate(np.eye(24)):
        p[16+n] = prior.joint.prior.complexify(value, (3, 4))
    lam[40:] = np.eye(16).reshape(16, 4, 4)
    dde[:16, 0, 0] = np.eye(16).reshape(16, 4, 4)
    return ball(p), ball(lam), ball(dde)


def coefficient_matrix(prepared, e, inverse, volume, de, psi, spatial_dp, lam, hessian_inverse):
    """Direct normal coefficient formula; does not subtract uncertain residuals."""
    eta, weights = ball(general.prolong.ETA), ball(general.prolong.WEIGHTS)
    forms, selector = ball(prepared["component_forms"]), ball(general.prolong.Q)
    qpsi = contract("uv,vj->uj", selector, psi)
    response = contract("ui,pamij,uj->amp", psi.conjugate(), forms, qpsi).real().scale(-1)
    source_components = contract("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = contract("ma,pam->p", inverse, source_components)
    source = contract(",p->p", volume, source)
    rhs = -source+contract("amp,am->p", response, lam)
    k = contract("pq,q->p", hessian_inverse, rhs)

    metric_inverse = contract("ma,ab,nb->mn", inverse, eta, inverse)
    metric_first = (contract("ram,ab,bv->rmv", de, eta, e)
                    +contract("am,ab,rbv->rmv", e, eta, de))
    lower = (metric_first.transpose(1, 0, 2)+metric_first.transpose(1, 2, 0)-metric_first).scale(.5)
    gamma = contract("as,sbc->abc", metric_inverse, lower)
    middle = contract("ap,pmq->maq", e, gamma)-de
    lc = contract("ab,mbv,vc->mac", eta, middle, inverse)
    omega = lc+contract("p,pmab->mab", k, general.cartan.OMEGA_BASIS)
    spin = contract("mab,aij,bjk->mik", omega, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)

    p, dl, dde = normal_basis()
    delta_dp = contract("r,nuj->nruj", np.eye(4)[0], p)
    delta_components = contract("ui,pamij,nuj->npam", psi.conjugate(), forms, p).real().scale(2)
    delta_source = contract(",ma,npam->np", volume, inverse, delta_components)
    delta_response = contract("ui,pamij,nuj->namp", qpsi.conjugate(), forms, p).real().scale(-2)
    delta_rhs = (-delta_source+contract("namp,am->np", delta_response, lam)
                 +contract("nam,amp->np", dl, response))
    delta_k = contract("pq,nq->np", hessian_inverse, delta_rhs)
    delta_g2 = (contract("nrsam,ab,bv->nrsmv", dde, eta, e)
                 +contract("am,ab,nrsbv->nrsmv", e, eta, dde))
    delta_lower = (delta_g2.transpose(0, 1, 3, 2, 4)
                   +delta_g2.transpose(0, 1, 3, 4, 2)-delta_g2).scale(.5)
    delta_gamma = contract("as,nrsbc->nrabc", metric_inverse, delta_lower)
    delta_middle = contract("ap,nrpmq->nrmaq", e, delta_gamma)-dde
    delta_lc = contract("ab,nrmbv,vc->nrmac", eta, delta_middle, inverse)
    delta_first = delta_lc+contract("r,np,pmab->nrmab", np.eye(4)[0], delta_k, general.cartan.OMEGA_BASIS)
    delta_spin = contract("nrmab,aij,bjk->nrmik", delta_first, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    delta_curvature = contract("ac,nrmcd,db->nrmab", eta,
        delta_first-delta_first.transpose(0, 2, 1, 3, 4), eta)

    delta_constraint = contract("uj,uv,nmvk,ajk->nam", psi.conjugate(), selector, delta_dp, weights).imag()
    kinetic = (contract(",ma,aij->mij", volume, inverse, general.prolong.FLAT_WEIGHTS)
               +contract("am,aij->mij", lam, general.prolong.Q_WEIGHTS))
    delta_probe = (contract("ij,nj->ni", kinetic[0], p.reshape(56, 12)).scale(1j)
        +contract("na,aij,j->ni", dl[:, :, 0], general.prolong.Q_WEIGHTS, psi.reshape(12)).scale(.5j))
    real_probe = TensorBall(np.concatenate((delta_probe.center.real, delta_probe.center.imag), axis=1), delta_probe.radius)
    delta_imag = contract("uj,nmuk,ajk->nam", psi.conjugate(), delta_dp, weights).imag()
    delta_ld = contract(",ma,nam->n", volume, inverse, delta_imag).scale(-1)
    matter = (contract("n,va->nav", delta_ld, inverse)
        +contract(",ma,nab,bv->nmv", volume, inverse, delta_imag, inverse).transpose(0, 2, 1))
    delta_lg = contract(",ma,kb,tmkab->t", volume, inverse, inverse, delta_curvature).scale(.5)
    gravity = (contract("t,va->tav", delta_lg, inverse)
        -contract(",ma,vc,kb,tmkcb->tav", volume, inverse, inverse, inverse, delta_curvature).scale(.5)
        -contract(",mc,ka,vb,tmkcb->tav", volume, inverse, inverse, inverse, delta_curvature).scale(.5))
    coframe = matter+gravity

    covariant_spatial = spatial_dp[1:]+contract("uj,mkj->muk", psi, spin[1:])
    cross1 = contract("nuj,uv,ivk,ajk->nia", p.conjugate(), selector, covariant_spatial, weights)
    cross2 = contract("iuj,uv,nvk,ajk->nia", spatial_dp[1:].conjugate(), selector, p, weights)
    delta_covariant = (contract("nijk,uk->niuj", delta_spin[:, 0, 1:]-delta_spin[:, 1:, 0], psi)
                       +contract("ijk,nuk->niuj", spin[1:], p))
    cross3 = contract("uj,uv,nivk,ajk->nia", psi.conjugate(), selector, delta_covariant, weights)
    curl = (cross1-cross2+cross3).imag()
    blocks = [delta_constraint.reshape(56, 16), real_probe, coframe.reshape(56, 16), curl.reshape(56, 12)]
    return stack_blocks(blocks).transpose(1, 0), {name: b.radius for name, b in zip(
        ("constraint", "probe", "coframe", "mixed_curl"), blocks)}


def coefficient_norms(prepared, point, jets, full):
    return {"E2": float(np.linalg.norm(point["coframe_second"])),
        "E3": float(np.linalg.norm(jets["e3"])), "E4": float(np.linalg.norm(full["e4"])),
        "p1": float(np.linalg.norm(point["psi_first"])), "p2": float(np.linalg.norm(jets["p2"])),
        "p3": float(np.linalg.norm(jets["p3"])), "p4": float(np.linalg.norm(full["p4"])),
        "l1": float(np.linalg.norm(point["multiplier_first"])), "l2": float(np.linalg.norm(jets["l2"])),
        "l3": float(np.linalg.norm(full["l3"]))}


def field_balls(prepared, point, norms, radius):
    if not np.isfinite(radius) or radius < 0:
        raise ValueError("Finite nonnegative coordinate radius required")
    r = radius
    d = norms["E2"]*r*r/2+norms["E3"]*r**3/6+norms["E4"]*r**4/24
    if d >= 1:
        raise ValueError("Coframe inverse majorant requires distance below one")
    de = norms["E2"]*r+norms["E3"]*r*r/2+norms["E4"]*r**3/6
    psi = norms["p1"]*r+norms["p2"]*r*r/2+norms["p3"]*r**3/6+norms["p4"]*r**4/24
    dp = norms["p2"]*r+norms["p3"]*r*r/2+norms["p4"]*r**3/6
    lam = norms["l1"]*r+norms["l2"]*r*r/2+norms["l3"]*r**3/6
    volume_change = 4*d+6*d*d+4*d**3+d**4
    volume_lower = (1-d)**4
    inverse_volume_change = volume_change/volume_lower
    h_inverse_change = np.linalg.norm(prepared["inverse_hessian"])*(
        (2*d+d*d)/volume_lower+inverse_volume_change)
    spatial = point["psi_first"].copy()
    spatial[0] = 0
    return {"e": TensorBall(np.eye(4), d), "inverse": TensorBall(np.eye(4), d/(1-d)),
        "volume": TensorBall(np.array(1.), volume_change),
        "de": TensorBall(np.zeros((4, 4, 4)), de),
        "psi": TensorBall(prepared["data"]["psi"], psi),
        "spatial_dp": TensorBall(spatial, dp), "lam": TensorBall(point["multiplier"], lam),
        "hessian_inverse": TensorBall(prepared["inverse_hessian"], float(h_inverse_change))}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    parent = json.loads(Path(__file__).with_name("HC_Cartan_General_Normal_Chart.json").read_text(encoding="utf-8"))
    if parent["input_sha256"] != general.input_fingerprints():
        raise ValueError("General normal report has stale inputs")
    norms = coefficient_norms(prepared, point, jets, full)
    center, _ = coefficient_matrix(prepared, **field_balls(prepared, point, norms, 0.))
    coordinate_rows = np.array(parent["fixed_coordinate_rows"])
    normal_singular = np.linalg.svd(center.center, compute_uv=False)
    augmented = np.vstack((center.center, coordinate_rows))
    sigma = float(np.linalg.svd(augmented, compute_uv=False)[-1])
    r = parent["radius_used_for_samples"]
    trials = []
    for _ in range(70):
        estimate, blocks = coefficient_matrix(prepared, **field_balls(prepared, point, norms, r))
        trials.append({"radius": r, "matrix_change_majorant": estimate.radius})
        if estimate.radius < min(sigma, normal_singular[39])/2:
            break
        r /= 2
    else:
        raise ValueError("No positive augmented-chart majorant resolved")
    lower = sigma-estimate.radius
    rng = np.random.default_rng(19108456)
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4), rng.normal(size=(4, 4))))
    directions[1:] /= np.linalg.norm(directions[1:], axis=1, keepdims=True)
    services = prior.create_container().services()
    checks = []
    for direction in directions:
        fields = general.domain.temporal.fields(prepared, point, jets, full, r*direction)
        actual = general.normal_system(prepared, fields, services=services)["matrix"]
        chart = general.chart_report(actual, coordinate_rows, services=services)
        checks.append({"direction": direction.tolist(),
            "actual_matrix_change": float(np.linalg.norm(actual-center.center, 2)),
            "augmented_minimum_singular": chart["augmented_minimum_singular"],
            "rank": chart["rank"]})
    origin_fields = general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    reference = general.normal_system(prepared, origin_fields, services=services)["matrix"]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Uniform normal-bound inputs changed")
    return {"scope": "Analytic Frobenius majorant for a fixed-coordinate augmented normal chart",
        "input_sha256": fingerprints, "coefficient_norms": norms,
        "center_matrix_match_error": float(np.linalg.norm(center.center-reference)),
        "center_augmented_minimum_singular": sigma,
        "center_normal_singular_40": float(normal_singular[39]),
        "radius": r, "matrix_change_majorant": estimate.radius,
        "block_majorants": blocks, "augmented_singular_lower_bound": lower,
        "augmented_inverse_norm_upper_bound": 1/lower,
        "normal_singular_40_lower_bound": float(normal_singular[39]-estimate.radius),
        "selection_trials": trials, "sample_checks_not_the_proof": checks,
        "not_outward_rounded_or_interval_certified": True,
        "not_uniform_exact_rank_40_upper_bound": True,
        "not_gauge_source_transport_or_compatibility_propagation": True,
        "not_regional_PDE_solution_or_physical_length": True,
        "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in (
        "input_sha256", "coefficient_norms", "selection_trials", "sample_checks_not_the_proof")}))


if __name__ == "__main__":
    main()
