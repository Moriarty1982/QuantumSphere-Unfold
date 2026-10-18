"""General-coframe normal equations and local chart samples for the compatible jet.

The neighborhood radius for a full normal inverse is not certified here.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "general_normal_regularity", Path(__file__).with_name("HC_Cartan_Compatible_Lift_Regularity.py"))
domain = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(domain)
prior = domain.prior
cartan, prolong = prior.joint.cartan, prior.joint.prolong


def input_fingerprints():
    result = domain.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Compatible_Lift_Regularity.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def connection_jets(prepared, fields):
    e, de, dde = (fields[k] for k in ("coframe", "coframe_first", "coframe_second"))
    psi, dp, lam, dl = (fields[k] for k in ("psi", "psi_first", "multiplier", "multiplier_first"))
    inverse, volume = np.linalg.inv(e), abs(np.linalg.det(e))
    dinverse = -np.einsum("ma,rav,vb->rmb", inverse, de, inverse)
    dvolume = volume*np.einsum("ma,ram->r", inverse, de)
    hessian, response, source = prolong.fast_cartan_data(prepared, e, psi)
    forms = prepared["component_forms"]
    components = np.einsum("ui,pamij,uj->pam", psi.conj(), forms, psi).real
    dcomponents = 2*np.einsum("ui,pamij,ruj->rpam", psi.conj(), forms, dp).real
    dsource = (np.einsum("r,ma,pam->rp", dvolume, inverse, components)
               +volume*np.einsum("rma,pam->rp", dinverse, components)
               +volume*np.einsum("ma,rpam->rp", inverse, dcomponents))
    dresponse = -2*np.einsum("ui,pamij,ruj->ramp", (prolong.Q @ psi).conj(), forms, dp).real
    dhessian = (np.einsum("r,pq->rpq", dvolume/volume, hessian)
        +volume*(np.einsum("rma,nb,pqmnab->rpq", dinverse, inverse, prepared["curvature_hessian"])
                 +np.einsum("ma,rnb,pqmnab->rpq", inverse, dinverse, prepared["curvature_hessian"]))/2)
    k = np.linalg.solve(hessian, -source+response.T @ lam.reshape(-1))
    rhs = (-dsource+np.einsum("ramp,am->rp", dresponse, lam)
           +dl.reshape(4, 16) @ response-np.einsum("rpq,q->rp", dhessian, k))
    dk = np.linalg.solve(hessian, rhs.T).T
    bundle = prolong.dirac.bundle(e, de, dde)
    gamma = bundle["curvature"]["connection"]
    dgamma = bundle["curvature"]["connection_derivative"]
    dlc = np.empty((4, 4, 4, 4))
    for r, mu in np.ndindex((4, 4)):
        middle = e @ gamma[:, mu, :]-de[mu]
        dlc[r, mu] = (prolong.ETA @ (de[r] @ gamma[:, mu, :]+e @ dgamma[r, :, mu, :]-dde[r, mu]) @ inverse
                       +prolong.ETA @ middle @ dinverse[r])
    omega = bundle["omega"]+cartan.unpack(k)
    first = dlc+np.einsum("rp,pmab->rmab", dk, cartan.OMEGA_BASIS)
    return {"omega": omega, "first": first, "bundle": bundle,
            "hessian": hessian, "response": response, "source": source,
            "k": k, "dk": dk, "dsource": dsource, "dresponse": dresponse,
            "dhessian": dhessian, "inverse": inverse, "volume": volume,
            "dinverse": dinverse, "dvolume": dvolume}


def equations(prepared, fields):
    connection = connection_jets(prepared, fields)
    e, de, psi, dp, lam, dl = (fields[k] for k in (
        "coframe", "coframe_first", "psi", "psi_first", "multiplier", "multiplier_first"))
    omega, first = connection["omega"], connection["first"]
    spin = prolong.spin_lift(omega)
    dspin = prolong.spin_lift(first)
    covariant = cartan.covariant_jet(psi, dp, omega)
    pair = prior.joint.third.scalar.odd.readouts.pairing
    constraint = pair(psi, covariant, prolong.Q).imag-e
    weights = cartan.kinetic_weights(e, lam)
    dweights = (np.einsum("r,ma,aij->rmij", connection["dvolume"], connection["inverse"], prolong.FLAT_WEIGHTS)
        +connection["volume"]*np.einsum("rma,aij->rmij", connection["dinverse"], prolong.FLAT_WEIGHTS)
        +np.einsum("ram,aij->rmij", dl, prolong.Q_WEIGHTS))
    spin_full = np.array([np.kron(np.eye(3), b) for b in spin])
    probe = prior.joint.third.scalar.odd.real_law.real_operator(
        psi.reshape(-1), dp.reshape(4, 12), weights, spin_full,
        connection["volume"]*prior.joint.prior.MASS_WEIGHT,
        np.einsum("mmij->ij", dweights))["symmetric"]
    curvature = cartan.curvature_upper(omega, first)
    gravity = cartan.coframe_euler(e, psi, dp, omega, curvature, prolong.MASS, lam)
    mixed = []
    for r, s in ((0, 1), (0, 2), (0, 3)):
        difference = np.einsum("ij,uj->ui", dspin[r, s]-dspin[s, r], psi)
        difference += dp[r] @ spin[s].T-dp[s] @ spin[r].T
        derivative = pair(psi, np.array([difference]*4), prolong.Q)[:, 0]
        # Use four identical slots above only to reuse the established pairing API.
        cross = []
        for a in range(4):
            weight = prior.joint.third.scalar.odd.readouts.dirac.WEIGHTS[a]
            cross.append(np.vdot(dp[r], (prolong.Q @ covariant[s]) @ weight.T)
                         -np.vdot(dp[s], (prolong.Q @ covariant[r]) @ weight.T))
        mixed.append((np.asarray(cross)+derivative).imag-de[r, :, s]+de[s, :, r])
    vector = np.r_[constraint.reshape(-1), prior.joint.prior.realify(probe), gravity.reshape(-1), np.asarray(mixed).reshape(-1)]
    return {"vector": vector, "constraint": constraint, "probe": probe, "gravity": gravity,
            "mixed_curl": np.asarray(mixed), "connection": connection}


def normal_values(fields):
    return np.r_[fields["coframe_second"][0, 0].reshape(-1),
                 prior.joint.prior.realify(fields["psi_first"][0]),
                 fields["multiplier_first"][0].reshape(-1)]


def with_normal_values(fields, values):
    values = cartan.checks._real(values, (56,), "general normal values")
    changed = dict(fields)
    for key in ("coframe_second", "psi_first", "multiplier_first"):
        changed[key] = fields[key].copy()
    changed["coframe_second"][0, 0] = values[:16].reshape(4, 4)
    changed["psi_first"][0] = prior.joint.prior.complexify(values[16:40], (3, 4))
    changed["multiplier_first"][0] = values[40:].reshape(4, 4)
    return changed


def normal_system(prepared, fields, *, services=None):
    def build():
        base_fields = with_normal_values(fields, np.zeros(56))
        base = equations(prepared, base_fields)["vector"]
        step = 16.
        columns = [(equations(prepared, with_normal_values(fields, step*e))["vector"]-base)/step for e in np.eye(56)]
        return {"matrix": np.column_stack(columns), "base": base}
    if services is None:
        return build()
    inputs = {key: fields[key] for key in ("coframe", "coframe_first", "coframe_second",
                                           "psi", "psi_first", "multiplier", "multiplier_first")}
    return services.cached("Cartan.general-normal-system/v1", {
        "fields": inputs, "prepared": prepared, "sources": input_fingerprints(),
        "numpy": np.__version__}, build)


def chart_report(matrix, coordinate_rows, *, services=None):
    if matrix.shape != (68, 56) or coordinate_rows.shape != (16, 56):
        raise ValueError("The normal chart requires a 68-by-56 matrix and 16 coordinate rows")
    if not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(coordinate_rows)):
        raise ValueError("Finite normal-chart coefficients required")
    singular = np.linalg.svd(matrix, compute_uv=False)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    augmented = np.vstack((matrix, coordinate_rows))
    if services is None:
        left, values, right = np.linalg.svd(augmented, full_matrices=False)
    else:
        left, values, right = services.svd(augmented, full_matrices=False)
    if values[-1] <= max(1e-10, values[0]*1e-10):
        raise ValueError("The augmented normal-coordinate chart is numerically singular")
    inverse = (right.T/values) @ left.T
    return {"rank": rank, "rank_cutoff": cutoff, "singular_40": float(singular[39]),
            "singular_41": float(singular[40]),
            "augmented_minimum_singular": float(values[-1]),
            "augmented_inverse_norm": float(1/values[-1]),
            "augmented_inverse_error": float(np.linalg.norm(inverse @ augmented-np.eye(56))),
            "inverse": inverse}


def evaluate(*, workers=2, services=None):
    services = prior.create_container().services() if services is None else services
    fingerprints = input_fingerprints()
    prepared, point, jets, unique, full, lift_report = domain.load_data()
    regularity = json.loads(Path(__file__).with_name("HC_Cartan_Compatible_Lift_Regularity.json").read_text(encoding="utf-8"))
    if regularity["input_sha256"] != domain.input_fingerprints():
        raise ValueError("Regularity report has stale inputs")
    radius = regularity["common_radius"]
    original = prior.source.normal.build_reduction(prepared, point)
    coordinate_rows = np.column_stack((original["gauge"], original["sources"])).T
    origin_fields = domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    origin = normal_system(prepared, origin_fields, services=services)
    origin_chart = chart_report(origin["matrix"], coordinate_rows, services=services)
    reference = prior.source.normal.normal_equations(prepared, point)
    rng = np.random.default_rng(19106856)
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4), rng.normal(size=(4, 4))))
    directions[1:] /= np.linalg.norm(directions[1:], axis=1, keepdims=True)

    def sample(direction):
        fields = domain.temporal.fields(prepared, point, jets, full, radius*direction)
        system = normal_system(prepared, fields, services=services)
        values = normal_values(fields)
        actual = equations(prepared, fields)["vector"]
        chart = chart_report(system["matrix"], coordinate_rows, services=services)
        target = np.r_[-system["base"], coordinate_rows @ values]
        proposed = chart["inverse"] @ target
        compatibility = np.vstack((system["matrix"], coordinate_rows)) @ proposed-target
        trial = values+np.random.default_rng(191056).normal(size=56)*.02
        affine = equations(prepared, with_normal_values(fields, trial))["vector"]-system["base"]-system["matrix"] @ trial
        return dict({k: v for k, v in chart.items() if k != "inverse"}, direction=direction.tolist(),
            matrix_change_norm=float(np.linalg.norm(system["matrix"]-origin["matrix"], 2)),
            full_68_residual_norm=float(np.linalg.norm(actual)),
            affine_error=float(np.linalg.norm(affine)),
            origin_chart_compatibility_residual=float(np.linalg.norm(compatibility)),
            proposed_actual_equations_norm=float(np.linalg.norm(equations(prepared, with_normal_values(fields, proposed))["vector"])))

    with ThreadPoolExecutor(max_workers=workers) as pool:
        samples = list(pool.map(sample, directions))
    if fingerprints != input_fingerprints():
        raise RuntimeError("General normal chart inputs changed")
    return {"scope": "General-coframe affine 68-by-56 normal system, samples not uniform radius proof",
        "input_sha256": fingerprints, "radius_used_for_samples": radius,
        "source_values": lift_report["source_values"],
        "origin_matrix_match_error": float(np.linalg.norm(origin["matrix"]-original["matrix"])),
        "origin_equations_match_error": float(np.linalg.norm(equations(prepared, origin_fields)["vector"]-reference)),
        "origin_chart": {k: v for k, v in origin_chart.items() if k != "inverse"},
        "fixed_coordinate_rows": coordinate_rows.tolist(), "samples": samples,
        "fixed_rows_are_not_a_transported_gauge_or_source_classification": True,
        "qualitative_augmented_chart_openness_not_quantified_radius": True,
        "not_uniform_rank_certificate_or_regional_solution": True,
        "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    result = evaluate(workers=args.workers)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_sha256", "fixed_coordinate_rows", "samples")}))
    print(json.dumps({"sample_ranks": [s["rank"] for s in result["samples"]],
        "maximum_affine_error": max(s["affine_error"] for s in result["samples"]),
        "minimum_augmented_singular": min(s["augmented_minimum_singular"] for s in result["samples"])}))


if __name__ == "__main__":
    main()
