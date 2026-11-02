"""Conservative temporal regularity neighborhood of the saved comparison Taylor jet.

An analytic norm estimate evaluated numerically, not full PDE hyperbolicity or existence.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "cartan_regular_neighborhood_gravity", Path(__file__).with_name("HC_Cartan_Regular_Gravity.py"))
gravity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gravity)
rank_model = gravity.spatial.rank_model


def load_data():
    prepared, point, _ = gravity.load_data()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Regular_Gravity.json").read_text(encoding="utf-8"))
    return prepared, point, gravity.unpack(np.array(payload["joint_completion"]["jet_coordinates"]))


def coefficients(prepared, point, jets):
    base = rank_model.probe_constraint_block(np.eye(4), prepared["data"]["psi"], point["multiplier"])
    return {"coframe_second": float(np.linalg.norm(point["coframe_second"])),
            "coframe_third": float(np.linalg.norm(jets["e3"])),
            "spinor_value": float(np.linalg.norm(prepared["data"]["psi"])),
            "spinor_first": float(np.linalg.norm(point["psi_first"])),
            "spinor_second": float(np.linalg.norm(jets["p2"])),
            "spinor_third": float(np.linalg.norm(jets["p3"])),
            "multiplier_first_temporal_column": float(np.linalg.norm(point["multiplier_first"][:, :, 0])),
            "multiplier_second_temporal_column": float(np.linalg.norm(jets["l2"][:, :, :, 0])),
            "minimum_base_probe_eigenvalue": float(base["weight_eigenvalues"][0]),
            "minimum_base_constraint_singular_value": float(base["singular_values"][-1])}


def bound(data, radius):
    radius = gravity.cartan.checks._scalar(radius, "nonnegative coordinate radius")
    if radius < 0:
        raise ValueError("Nonnegative coordinate radius required")
    e = data["coframe_second"]*radius**2/2+data["coframe_third"]*radius**3/6
    p = (data["spinor_first"]*radius+data["spinor_second"]*radius**2/2
         +data["spinor_third"]*radius**3/6)
    ell = (data["multiplier_first_temporal_column"]*radius
           +data["multiplier_second_temporal_column"]*radius**2/2)
    if e >= 1:
        return {"radius": radius, "coframe_change_bound": e, "spinor_change_bound": p,
                "temporal_multiplier_change_bound": ell, "resolved": False,
                "reason": "coframe inverse bound unavailable"}
    volume_upper = (1+e)**4
    # The temporal Clifford norm is |a0|+|a_spatial| <= sqrt(2)|a|.
    volume_change = 4*e+6*e**2+4*e**3+e**4
    dk = volume_change+volume_upper*np.sqrt(2)*e/(1-e)+ell/np.sqrt(2)
    mu = data["minimum_base_probe_eigenvalue"]
    lower = mu-dk
    result = {"radius": radius, "coframe_change_bound": e, "spinor_change_bound": p,
              "temporal_multiplier_change_bound": ell, "probe_weight_change_bound": dk,
              "probe_eigenvalue_lower_bound": lower, "resolved": False}
    if lower <= 0:
        return dict(result, reason="positive temporal probe estimate unavailable")
    p0 = data["spinor_value"]
    # Four times the per-entry perturbation bounds the 4x4 operator norm.
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
                and estimate["constraint_singular_value_lower_bound"] >= data["minimum_base_constraint_singular_value"]/2):
            return estimate
        radius /= 2
    raise ValueError("No regular temporal neighborhood resolved")


def samples(prepared, point, jets, radius, count=12):
    data = coefficients(prepared, point, jets)
    estimate = bound(data, radius)
    base = rank_model.probe_constraint_block(np.eye(4), prepared["data"]["psi"], point["multiplier"])
    rng = np.random.default_rng(261018)
    directions = np.vstack((np.eye(4), -np.eye(4), rng.normal(size=(count, 4))))
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    result = []
    for direction in directions:
        fields = gravity.taylor_fields(prepared, point, jets, radius*direction)
        actual = rank_model.probe_constraint_block(fields["coframe"], fields["psi"], fields["multiplier"])
        result.append({"coframe_change": float(np.linalg.norm(fields["coframe"]-np.eye(4), 2)),
                       "spinor_change": float(np.linalg.norm(fields["psi"]-prepared["data"]["psi"])),
                       "probe_weight_change": float(np.linalg.norm(actual["weights"]-base["weights"], 2)),
                       "constraint_block_change": float(np.linalg.norm(actual["block"]-base["block"], 2)),
                       "probe_minimum_eigenvalue": float(actual["weight_eigenvalues"][0]),
                       "constraint_minimum_singular_value": float(actual["singular_values"][-1]),
                       "constraint_equation_residual": float(np.linalg.norm(fields["constraint"]))})
    return {"estimate": estimate, "samples": result}


def completed_scalar_neighborhood(prepared, point, completed):
    """Recompute the estimate only after matching every retained lower field/coupling."""
    kept = completed["fixed_lower_point_and_couplings"]
    expected = {"psi_real": prepared["data"]["psi"].real, "psi_imag": prepared["data"]["psi"].imag,
                "psi_first_real": point["psi_first"].real, "psi_first_imag": point["psi_first"].imag,
                "coframe_value": np.eye(4), "coframe_first": np.zeros((4, 4, 4)),
                "coframe_second": point["coframe_second"], "multiplier": point["multiplier"],
                "multiplier_first": point["multiplier_first"], "Q_real": gravity.Q.real,
                "Q_imag": gravity.Q.imag, "M_real": gravity.MASS.real, "M_imag": gravity.MASS.imag}
    for name, value in expected.items():
        if not np.array_equal(np.asarray(kept[name]), value):
            raise ValueError("Retained lower field/coupling mismatch: "+name)
    if kept["Einstein_coefficient"] != 1 or kept["vacuum"] != 0:
        raise ValueError("Retained gravitational coefficients changed")
    for name in ("HC_Cartan_Regular_Gravity.json", "HC_Cartan_Spatial_Propagation.json"):
        actual = hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        if completed["input_sha256"][name] != actual:
            raise ValueError("Scalar-completion input fingerprint mismatch: "+name)
    jets = gravity.unpack(np.array(completed["joint_394_system"]["jet_coordinates"]))
    data = coefficients(prepared, point, jets)
    estimate = select_radius(data)
    return {"retained_lower_point_and_couplings_verified": True,
            "coefficient_norms": data, "regular_neighborhood": estimate,
            "sample_checks_not_the_proof": samples(prepared, point, jets, estimate["radius"])["samples"]}


def evaluate(next_scalar_path=None):
    prepared, point, jets = load_data()
    data = coefficients(prepared, point, jets)
    estimate = select_radius(data)
    result = {"status": "analytic temporal-block neighborhood estimate on finite Taylor fields; not an evolved/full-PDE/native result",
            "regular_gravity_input_sha256": hashlib.sha256(Path(__file__).with_name("HC_Cartan_Regular_Gravity.json").read_bytes()).hexdigest(),
            "coefficient_norms": data, "regular_neighborhood": estimate,
            "sample_checks_not_the_proof": samples(prepared, point, jets, estimate["radius"])["samples"],
            "not_interval_certified_input_norms": True, "not_full_normal_rank_control": True,
            "not_Cauchy_existence_or_physical_scale": True, "main_TeX_changed": False}
    if next_scalar_path is not None:
        completed = json.loads(next_scalar_path.read_text(encoding="utf-8"))
        result["next_scalar_input_sha256"] = hashlib.sha256(next_scalar_path.read_bytes()).hexdigest()
        result["completed_scalar_jet"] = completed_scalar_neighborhood(prepared, point, completed)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--next-scalar", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(args.next_scalar), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
