"""Recomputed coefficient-domain bounds for the compatible shifted finite jet."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def local_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lift = local_module("compatible_regularity_lift", "HC_Cartan_Compatible_Tangential_Lift.py")
cartan_regular = local_module("compatible_regularity_cartan", "HC_Cartan_Joint_Cartan_Regularity.py")
prior = lift.prior
temporal = prior.source.neighborhood


def input_fingerprints():
    result = lift.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Compatible_Tangential_Lift.json",
                 "HC_Cartan_Joint_Cartan_Regularity.py", "HC_Cartan_Joint_Neighborhood.json",
                 "HC_Cartan_Joint_Cartan_Regularity.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def load_data():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Compatible_Tangential_Lift.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != lift.input_fingerprints():
        raise ValueError("Compatible lift report has stale inputs")
    if not report["numerically_completed"]:
        raise ValueError("A failed finite fit is not a compatible lift")
    prepared, point, _, _, _ = prior.source.neighborhood.load_data()
    sources = prior.source.normal.build_reduction(prepared, point)["sources"]
    changed = prior.source.normal.remaining.normal_point(point, sources @ np.asarray(report["source_values"]))
    c = prior.source.normal.cartan.checks._real(report["fitted_coordinates"], (1200,), "compatible earlier jets")
    h = prior.source.normal.cartan.checks._real(report["fitted_highest"], (1720,), "compatible highest jets")
    jets = prior.regular.unpack(c)
    p4 = np.array([prior.joint.third.prior.complexify(v, (3, 4)) for v in h[880:].reshape(35, 24)])
    unique = {"e4": h[:560].reshape(35, 4, 4), "l3": h[560:880].reshape(20, 4, 4), "p4": p4}
    full = {"e4": temporal.unpack_fourth(unique["e4"]),
            "l3": prior.joint.third.prolong.unpack_third(h[560:880]),
            "p4": temporal.unpack_fourth(p4)}
    return prepared, changed, jets, unique, full, report


def sample_checks(prepared, point, jets, unique, full, radius):
    base = temporal.rank_model.probe_constraint_block(np.eye(4), prepared["data"]["psi"], point["multiplier"])
    rng = np.random.default_rng(19101114)
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4), rng.normal(size=(8, 4))))
    directions[1:] /= np.linalg.norm(directions[1:], axis=1, keepdims=True)
    rows = []
    for direction in directions:
        x = radius*direction
        fields = temporal.fields(prepared, point, jets, full, x)
        independent = cartan_regular.fields(prepared, point, jets, unique, x)
        block = temporal.rank_model.probe_constraint_block(fields["coframe"], fields["psi"], fields["multiplier"])
        hessian = fields["Cartan_hessian"]
        metric = fields["bundle"]["metric"]
        rows.append({"direction": direction.tolist(),
            "coframe_change": float(np.linalg.norm(fields["coframe"]-np.eye(4), 2)),
            "spinor_change": float(np.linalg.norm(fields["psi"]-prepared["data"]["psi"])),
            "temporal_multiplier_change": float(np.linalg.norm(fields["multiplier"][:, 0]-point["multiplier"][:, 0])),
            "probe_weight_change": float(np.linalg.norm(block["weights"]-base["weights"], 2)),
            "constraint_block_change": float(np.linalg.norm(block["block"]-base["block"], 2)),
            "probe_minimum_eigenvalue": float(block["weight_eigenvalues"][0]),
            "constraint_minimum_singular_value": float(block["singular_values"][-1]),
            "inverse_metric_time_component": float(np.linalg.inv(metric)[0, 0]),
            "spatial_metric_minimum_eigenvalue": float(np.linalg.eigvalsh(metric[1:, 1:])[0]),
            "Cartan_minimum_singular_value": float(np.linalg.svd(hessian, compute_uv=False)[-1]),
            "Cartan_inverse_norm": float(np.linalg.norm(np.linalg.inv(hessian), 2)),
            "Cartan_congruence_error": float(np.linalg.norm(hessian-cartan_regular.congruence_hessian(prepared, fields["coframe"]), 2)),
            "independent_coframe_error": float(np.linalg.norm(fields["coframe"]-independent["coframe"])),
            "independent_spinor_error": float(np.linalg.norm(fields["psi"]-independent["psi"])),
            "independent_multiplier_error": float(np.linalg.norm(fields["multiplier"]-independent["multiplier"])),
            "independent_connection_error": float(np.linalg.norm(fields["omega"]-independent["omega"])),
            "constraint_residual": float(np.linalg.norm(fields["constraint"])),
            "probe_residual": float(np.linalg.norm(fields["probe"])),
            "Cartan_residual": float(np.linalg.norm(fields["Cartan"]))})
    return rows


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, unique, full, report = load_data()
    coefficients = temporal.coefficient_norms(prepared, point, jets, full)
    cartan_coefficients = cartan_regular.coefficient_norms(prepared, point, jets, unique)
    temporal_estimate = temporal.select_radius(coefficients)
    cartan_estimate = cartan_regular.select_radius(cartan_coefficients)
    radius = min(temporal_estimate["radius"], cartan_estimate["radius"])
    common_temporal = temporal.bound(coefficients, radius)
    common_cartan = cartan_regular.bound(cartan_coefficients, radius)
    if not common_temporal["resolved"] or not common_cartan["resolved"]:
        raise ValueError("No common regular coefficient domain")
    c, h = np.array(report["fitted_coordinates"]), np.array(report["fitted_highest"])
    actual = prior.evaluate_fields(prepared, point, c, h, prior.joint.third.lc_cubic(prepared, point))
    normal = prior.source.normal.build_reduction(prepared, point)
    old_temporal = json.loads(Path(__file__).with_name("HC_Cartan_Joint_Neighborhood.json").read_text(encoding="utf-8"))
    old_cartan = json.loads(Path(__file__).with_name("HC_Cartan_Joint_Cartan_Regularity.json").read_text(encoding="utf-8"))
    checks = sample_checks(prepared, point, jets, unique, full, radius)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Compatible regularity inputs changed")
    return {"scope": "Uniform coefficient-domain estimates on the new shifted quartic finite-jet fields",
        "input_sha256": fingerprints, "source_values": report["source_values"],
        "origin": prior.norm_report(actual),
        "coefficient_norms": coefficients, "Cartan_coefficient_norms": cartan_coefficients,
        "selected_temporal_bound": temporal_estimate, "selected_Cartan_bound": cartan_estimate,
        "common_radius": radius, "common_temporal_bound": common_temporal, "common_Cartan_bound": common_cartan,
        "parent_temporal_bound": temporal.bound(coefficients, 2*temporal_estimate["radius"]),
        "parent_Cartan_bound": cartan_regular.bound(cartan_coefficients, 2*cartan_estimate["radius"]),
        "original_radii_comparison_not_inherited": {
            "temporal": old_temporal["regular_neighborhood"]["radius"],
            "Cartan": old_cartan["regular_neighborhood"]["radius"]},
        "origin_normal_rank": normal["rank"],
        "origin_normal_inverse_norm": float(np.linalg.norm(normal["inverse"], 2)),
        "origin_normal_smallest_retained_singular": float(normal["singular"][normal["rank"]-1]),
        "sample_checks_not_the_proof": checks,
        "not_interval_certified": True, "not_uniform_full_normal_rank_or_PDE_hyperbolicity": True,
        "not_neighborhood_solution_or_Cauchy_existence": True, "no_physical_length_units": True,
        "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("origin", "common_radius", "common_temporal_bound",
                                                  "common_Cartan_bound", "origin_normal_rank")}))


if __name__ == "__main__":
    main()
