"""Quartic Taylor-field regularity estimates for the joint 1114-component jet.

Uniform coefficient-domain estimates, not a solution on a spacetime neighborhood.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


def local_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


joint = local_module("joint_neighborhood_completion", "HC_Cartan_Next_Joint_Completion.py")
previous = local_module("joint_neighborhood_previous", "HC_Cartan_Regular_Neighborhood.py")
third, regular, prior, prolong, cartan = joint.third, joint.regular, joint.prior, joint.prolong, joint.cartan
rank_model = third.spatial.rank_model


def unpack_fourth(values):
    values = np.asarray(values)
    if values.shape[0] != 35 or not np.all(np.isfinite(values)):
        raise ValueError("35 finite unique symmetric fourth-derivative values required")
    result = np.empty((4, 4, 4, 4)+values.shape[1:], dtype=values.dtype)
    for indices, value in zip(third.diagnostic.QUADS, values):
        for permutation in set(itertools.permutations(indices)):
            result[permutation] = value
    return result


def load_data():
    path = Path(__file__).with_name("HC_Cartan_Next_Joint_Completion.json")
    report = json.loads(path.read_text(encoding="utf-8"))
    if report["input_sha256"] != joint.input_fingerprints():
        raise ValueError("Joint completion source inputs changed")
    prepared, point, saved, fingerprint = third.diagnostic.load_data()
    if report["input_scalar_completion_sha256"] != fingerprint:
        raise ValueError("Joint completion belongs to another lower-point source")
    jets = regular.unpack(np.array(report["jet_coordinates"]))
    if not np.array_equal(jets["p2"], saved["p2"]):
        raise ValueError("The retained spinor Hessian changed")
    connection = np.asarray(report["connection_coordinates"], float)
    p4 = np.array([prior.complexify(v, (3, 4)) for v in report["fourth_spinor_real"]])
    extras = {"e4": unpack_fourth(connection[:560].reshape(35, 4, 4)),
              "l3": prolong.unpack_third(connection[560:]), "p4": unpack_fourth(p4)}
    return prepared, point, jets, extras, report


def input_fingerprints():
    result = joint.input_fingerprints()
    for name in ("HC_Cartan_Next_Joint_Completion.py", "HC_Cartan_Next_Joint_Completion.json",
                 "HC_Cartan_Regular_Neighborhood.py", "HC_Cartan_Joint_Neighborhood.py"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def fields(prepared, point, jets, extras, displacement):
    x = cartan.checks._real(displacement, (4,), "joint Taylor displacement")
    e2, e3, e4 = point["coframe_second"], jets["e3"], extras["e4"]
    p1, p2, p3, p4 = point["psi_first"], jets["p2"], jets["p3"], extras["p4"]
    l1, l2, l3 = point["multiplier_first"], jets["l2"], extras["l3"]
    e = (np.eye(4)+np.einsum("r,s,rsam->am", x, x, e2)/2
         +np.einsum("r,s,t,rstam->am", x, x, x, e3)/6
         +np.einsum("r,s,t,u,rstuam->am", x, x, x, x, e4)/24)
    de = (np.einsum("s,rsam->ram", x, e2)+np.einsum("s,t,rstam->ram", x, x, e3)/2
          +np.einsum("s,t,u,rstuam->ram", x, x, x, e4)/6)
    dde = e2+np.einsum("t,rstam->rsam", x, e3)+np.einsum("t,u,rstuam->rsam", x, x, e4)/2
    psi = (prepared["data"]["psi"]+np.einsum("r,rij->ij", x, p1)
           +np.einsum("r,s,rsij->ij", x, x, p2)/2+np.einsum("r,s,t,rstij->ij", x, x, x, p3)/6
           +np.einsum("r,s,t,u,rstuij->ij", x, x, x, x, p4)/24)
    dp = (p1+np.einsum("s,rsij->rij", x, p2)+np.einsum("s,t,rstij->rij", x, x, p3)/2
          +np.einsum("s,t,u,rstuij->rij", x, x, x, p4)/6)
    lam = (point["multiplier"]+np.einsum("r,ram->am", x, l1)
           +np.einsum("r,s,rsam->am", x, x, l2)/2+np.einsum("r,s,t,rstam->am", x, x, x, l3)/6)
    dl = l1+np.einsum("s,rsam->ram", x, l2)+np.einsum("s,t,rstam->ram", x, x, l3)/2
    bundle = prolong.dirac.bundle(e, de, dde)
    h, response, source = prolong.fast_cartan_data(prepared, e, psi)
    k = np.linalg.solve(h, -source+response.T @ lam.reshape(-1))
    omega = bundle["omega"]+cartan.unpack(k)
    inverse, volume = np.linalg.inv(e), abs(np.linalg.det(e))
    inverse_first = -np.einsum("ma,rav,vb->rmb", inverse, de, inverse)
    volume_first = volume*np.einsum("ma,ram->r", inverse, de)
    dw = (np.einsum("r,ma,aij->rmij", volume_first, inverse, prolong.FLAT_WEIGHTS)
          +volume*np.einsum("rma,aij->rmij", inverse_first, prolong.FLAT_WEIGHTS)
          +np.einsum("ram,aij->rmij", dl, prolong.Q_WEIGHTS))
    spin = np.array([np.kron(np.eye(3), b) for b in prolong.spin_lift(omega)])
    probe = third.scalar.odd.real_law.real_operator(
        psi.reshape(-1), dp.reshape(4, 12), cartan.kinetic_weights(e, lam), spin,
        volume*prior.MASS_WEIGHT, np.einsum("mmij->ij", dw))["symmetric"]
    constraint = third.scalar.odd.channels(psi, cartan.covariant_jet(psi, dp, omega))["odd"]-e
    return {"coframe": e, "coframe_first": de, "coframe_second": dde, "psi": psi, "psi_first": dp,
            "multiplier": lam, "multiplier_first": dl, "omega": omega, "bundle": bundle,
            "Cartan_hessian": h, "Cartan": h @ k+source-response.T @ lam.reshape(-1),
            "constraint": constraint, "probe": probe}


def coefficient_norms(prepared, point, jets, extras):
    data = previous.coefficients(prepared, point, jets)
    data.update(coframe_fourth=float(np.linalg.norm(extras["e4"])),
                spinor_fourth=float(np.linalg.norm(extras["p4"])),
                multiplier_third_temporal_column=float(np.linalg.norm(extras["l3"][..., 0])))
    return data


def polynomial_changes(data, radius):
    radius = cartan.checks._scalar(radius, "nonnegative coordinate radius")
    if radius < 0:
        raise ValueError("Nonnegative coordinate radius required")
    e = (data["coframe_second"]*radius**2/2+data["coframe_third"]*radius**3/6
         +data["coframe_fourth"]*radius**4/24)
    p = (data["spinor_first"]*radius+data["spinor_second"]*radius**2/2
         +data["spinor_third"]*radius**3/6+data["spinor_fourth"]*radius**4/24)
    ell = (data["multiplier_first_temporal_column"]*radius
           +data["multiplier_second_temporal_column"]*radius**2/2
           +data["multiplier_third_temporal_column"]*radius**3/6)
    return float(e), float(p), float(ell)


def bound(data, radius):
    e, p, ell = polynomial_changes(data, radius)
    result = {"radius": float(radius), "coframe_change_bound": e, "spinor_change_bound": p,
              "temporal_multiplier_change_bound": ell, "resolved": False}
    if e >= 1:
        return dict(result, reason="coframe inverse bound unavailable")
    vu = (1+e)**4
    dk = 4*e+6*e**2+4*e**3+e**4+vu*np.sqrt(2)*e/(1-e)+ell/np.sqrt(2)
    mu = data["minimum_base_probe_eigenvalue"]
    lower = mu-dk
    result.update(volume_lower_bound=(1-e)**4, volume_upper_bound=vu,
                  coframe_inverse_norm_upper_bound=1/(1-e),
                  inverse_metric_change_bound=e*(2-e)/(1-e)**2,
                  spatial_metric_eigenvalue_lower_bound=1-e*(2+e),
                  probe_weight_change_bound=dk, probe_eigenvalue_lower_bound=lower)
    result["coordinate_time_timelike_margin"] = 1-result["inverse_metric_change_bound"]
    if lower <= 0:
        return dict(result, reason="positive temporal probe estimate unavailable")
    p0 = data["spinor_value"]
    dt = .5*((2*p0*p+p*p)/lower+p0*p0*dk/(lower*mu))
    tau = data["minimum_base_constraint_singular_value"]-dt
    result.update(constraint_block_change_bound=dt, constraint_singular_value_lower_bound=tau)
    if tau <= 0:
        return dict(result, reason="constraint inverse estimate unavailable")
    return dict(result, resolved=True, probe_inverse_norm_upper_bound=1/lower,
                constraint_inverse_norm_upper_bound=1/tau)


def select_radius(data):
    radius = 1.
    for _ in range(80):
        estimate = bound(data, radius)
        if (estimate["resolved"] and estimate["coframe_change_bound"] <= .1
                and estimate["probe_eigenvalue_lower_bound"] >= data["minimum_base_probe_eigenvalue"]/2
                and estimate["constraint_singular_value_lower_bound"] >= data["minimum_base_constraint_singular_value"]/2
                and estimate["coordinate_time_timelike_margin"] > 0
                and estimate["spatial_metric_eigenvalue_lower_bound"] > 0):
            return estimate
        radius /= 2
    raise ValueError("No joint temporal regularity ball resolved")


def sample_checks(prepared, point, jets, extras, radius, count=12):
    base = rank_model.probe_constraint_block(np.eye(4), prepared["data"]["psi"], point["multiplier"])
    rng = np.random.default_rng(11142610)
    directions = np.vstack((np.eye(4), -np.eye(4), rng.normal(size=(count, 4))))
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    result = []
    for direction in directions:
        value = fields(prepared, point, jets, extras, radius*direction)
        block = rank_model.probe_constraint_block(value["coframe"], value["psi"], value["multiplier"])
        inverse_metric = np.linalg.inv(value["bundle"]["metric"])
        result.append({"direction": direction.tolist(),
                       "coframe_change": float(np.linalg.norm(value["coframe"]-np.eye(4), 2)),
                       "spinor_change": float(np.linalg.norm(value["psi"]-prepared["data"]["psi"])),
                       "temporal_multiplier_change": float(np.linalg.norm(value["multiplier"][:, 0]-point["multiplier"][:, 0])),
                       "probe_weight_change": float(np.linalg.norm(block["weights"]-base["weights"], 2)),
                       "constraint_block_change": float(np.linalg.norm(block["block"]-base["block"], 2)),
                       "probe_minimum_eigenvalue": float(block["weight_eigenvalues"][0]),
                       "constraint_minimum_singular_value": float(block["singular_values"][-1]),
                       "metric_inverse_time_component": float(inverse_metric[0, 0]),
                       "spatial_metric_minimum_eigenvalue": float(np.linalg.eigvalsh(value["bundle"]["metric"][1:, 1:])[0]),
                       "constraint_residual": float(np.linalg.norm(value["constraint"])),
                       "probe_residual": float(np.linalg.norm(value["probe"])),
                       "Cartan_residual": float(np.linalg.norm(value["Cartan"]))})
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, extras, report = load_data()
    data = coefficient_norms(prepared, point, jets, extras)
    estimate = select_radius(data)
    check = joint.full_residual(prepared, point, np.array(report["jet_coordinates"]),
                                np.array(report["connection_coordinates"]), np.array(report["fourth_spinor_real"]),
                                third.lc_cubic(prepared, point))
    result = {"scope": "Uniform temporal-block and geometric estimates on finite quartic Taylor fields only",
              "input_sha256": fingerprints, "coefficient_norms": data, "regular_neighborhood": estimate,
              "parent_dyadic_radius_check": bound(data, 2*estimate["radius"]),
              "full_1114_origin_residual_norm": float(np.linalg.norm(check["vector"])),
              "sample_checks_not_the_proof": sample_checks(prepared, point, jets, extras, estimate["radius"]),
              "not_interval_certified": True, "not_full_normal_rank_or_PDE_hyperbolicity": True,
              "not_neighborhood_solution_or_Cauchy_existence": True, "no_physical_length_units": True,
              "main_TeX_PDF_changed": False}
    if fingerprints != input_fingerprints():
        raise RuntimeError("Inputs changed while checking joint neighborhood")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    encoded = json.dumps(result, indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps(result["regular_neighborhood"], indent=2))


if __name__ == "__main__":
    main()
