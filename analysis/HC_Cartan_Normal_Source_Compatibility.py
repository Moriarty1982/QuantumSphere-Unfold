"""Eliminate free higher jets before testing six unresolved normal sources.

Current C1/R1/FE1/C2 compatibility only, not regional source evolution.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "source_compatibility_normal", Path(__file__).with_name("HC_Cartan_Normal_Source_Reduction.py"))
normal = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(normal)
regular, spatial, prior, neighborhood = normal.regular, normal.spatial, normal.prior, normal.neighborhood


def changed_fields(point, jets, source_basis, q, z):
    q = normal.cartan.checks._real(q, (6,), "six normal source coordinates")
    z = normal.cartan.checks._real(z, (1200,), "1200 higher increments")
    changed = normal.remaining.normal_point(point, source_basis @ q)
    delta = regular.unpack(z)
    return changed, {key: jets[key]+delta[key] for key in jets}


def assemble(prepared, point, jets, reduction):
    base = regular.equations(prepared, point, jets)["vector"]
    matrix = np.column_stack([
        regular.equations(prepared, point, {key: jets[key]+value
                                          for key, value in regular.unpack(v).items()})["vector"]-base
        for v in np.eye(1200)])
    source, affinity = normal.higher_source_response(prepared, point, jets, reduction)
    return {"base": base, "matrix": matrix, "source": source, "source_affinity_error": affinity}


def elimination(matrix, source, base):
    left, singular, right = np.linalg.svd(matrix, full_matrices=False)
    cutoff = max(1e-9, singular[0]*1e-10)
    rank = int(np.sum(singular > cutoff))
    inverse = (right[:rank].T/singular[:rank]) @ left[:, :rank].T
    null_left = left[:, rank:]
    gate = null_left.T @ source
    gate_singular = np.linalg.svd(gate, compute_uv=False)
    return {"rank": rank, "singular": singular, "cutoff": cutoff,
            "inverse": inverse, "left_null": null_left,
            "gate": gate, "gate_singular": gate_singular,
            "gate_rank": int(np.sum(gate_singular > 1e-8)),
            "base_gate": null_left.T @ base,
            "source_lift": -inverse @ source, "base_lift": -inverse @ base}


def input_fingerprints():
    result = normal.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def allowed_cauchy_coordinates():
    """Freeze tangential jets of E,E_t,psi,lambda at t=0; no surface existence claim."""
    pairs = [i for i, indices in enumerate(prior.PAIR2) if 0 in indices]
    triples = list(regular.prolong.PAIR3)
    e_triples = [i for i, indices in enumerate(triples) if indices.count(0) >= 2]
    p_triples = [i for i, indices in enumerate(triples) if 0 in indices]
    psi2 = [offset+12*i+j for offset in (0, 120) for i in pairs for j in range(12)]
    lambda2 = [240+16*i+j for i in pairs for j in range(16)]
    e3 = [400+16*i+j for i in e_triples for j in range(16)]
    psi3 = [720+offset+12*i+j for offset in (0, 240) for i in p_triples for j in range(12)]
    return {"psi2": psi2, "lambda2": lambda2, "e3": e3, "psi3": psi3}


def restriction_report(result, allowed):
    rank = result["gate_rank"]
    u, singular, vh = np.linalg.svd(result["gate"], full_matrices=False)
    particular = np.zeros(6)
    reduced_rhs = np.empty(0)
    if rank:
        reduced_rhs = -(u[:, :rank].T @ result["base_gate"])/singular[:rank]
        particular = vh[:rank].T @ reduced_rhs
    return {"allowed_higher_coordinates": len(allowed),
            "allowed_coordinate_indices": list(allowed),
            "higher_rank": result["rank"], "gate_rank": rank,
            "gate_singular_values": result["gate_singular"].tolist(),
            "base_gate_norm": float(np.linalg.norm(result["base_gate"])),
            "source_particular_solution": particular.tolist(),
            "gate_consistency_error": float(np.linalg.norm(result["gate"] @ particular+result["base_gate"])),
            "reduced_gate_rows": vh[:rank].tolist(), "reduced_gate_rhs": reduced_rhs.tolist()}


def prescribed_source_law(system, free_model, allowed, prescribed, tolerance=1e-8):
    """Unique q from compatible fixed higher data, only when the six-source gate is injective."""
    allowed = np.asarray(allowed, int)
    fixed = np.setdiff1d(np.arange(1200), allowed)
    data = normal.cartan.checks._real(prescribed, (len(fixed),), "prescribed tangential higher data")
    if free_model["gate_rank"] != 6:
        raise ValueError("A rank-six source gate is required for a unique source law")
    target = system["base"]+system["matrix"][:, fixed] @ data
    gate_rhs = -free_model["left_null"].T @ target
    q = np.linalg.lstsq(free_model["gate"], gate_rhs, rcond=1e-10)[0]
    compatibility = free_model["gate"] @ q-gate_rhs
    if np.linalg.norm(compatibility) > tolerance*(1+np.linalg.norm(target)):
        raise ValueError("Prescribed higher data violate source-law compatibility")
    z = np.zeros(1200)
    z[fixed] = data
    z[allowed] = -free_model["inverse"] @ (target+system["source"] @ q)
    return {"source": q, "higher_increment": z, "compatibility_norm": float(np.linalg.norm(compatibility))}


def later_residual(prepared, changed, z, starting_report):
    """Keep saved fourth/third multiplier data, but recompute changed LC cubic."""
    joint = neighborhood.joint
    coordinates = np.asarray(starting_report["jet_coordinates"])+z
    return joint.full_residual(
        prepared, changed, coordinates, np.asarray(starting_report["connection_coordinates"]),
        np.asarray(starting_report["fourth_spinor_real"]), joint.third.lc_cubic(prepared, changed))


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, starting_report = neighborhood.load_data()
    reduction = normal.build_reduction(prepared, point)
    system = assemble(prepared, point, jets, reduction)
    full = elimination(system["matrix"], system["source"], system["base"])
    restrictions = {}
    cauchy_blocks = allowed_cauchy_coordinates()
    spatial_psi2_free = cauchy_blocks["psi2"]+list(range(240, 1200))
    cauchy_free = sum(cauchy_blocks.values(), [])
    masks = {"psi2_fixed": list(range(240, 1200)),
             "psi2_and_lambda2_fixed": list(range(400, 1200)),
             "spatial_psi2_fixed": spatial_psi2_free,
             "tangential_Cauchy_jet_fixed": cauchy_free}
    for name, allowed in masks.items():
        result = elimination(system["matrix"][:, allowed], system["source"], system["base"])
        restrictions[name] = restriction_report(result, allowed)
        if name == "tangential_Cauchy_jet_fixed":
            cauchy_model = result
    pattern = np.array([1., -.5, .3, .2, .4, -.1])
    rows, next_control = [], None
    source_law_controls = []
    fixed = np.setdiff1d(np.arange(1200), cauchy_free)
    for amplitude in (0., .01, -.01, .02):
        q = amplitude*pattern
        z = full["base_lift"]+full["source_lift"] @ q
        changed, higher = changed_fields(point, jets, reduction["sources"], q, z)
        result = regular.equations(prepared, changed, higher)
        rows.append({"amplitude": amplitude,
                     "all_68_normal_equations_norm": float(np.linalg.norm(normal.normal_equations(prepared, changed))),
                     "all_384_higher_equations_norm": float(np.linalg.norm(result["vector"])),
                     "constraint_first_norm": float(np.linalg.norm(result["constraint_first"])),
                     "probe_first_norm": float(np.linalg.norm(result["probe_first"])),
                     "coframe_Euler_first_norm": float(np.linalg.norm(result["coframe_Euler_first"])),
                     "constraint_second_full_symmetric_norm": float(np.linalg.norm(result["constraint_second"])),
                     "higher_increment_norm": float(np.linalg.norm(z)),
                     "affine_prediction_error": float(np.linalg.norm(result["vector"]-system["base"]
                         -system["source"] @ q-system["matrix"] @ z))})
        if amplitude == .01:
            later = later_residual(prepared, changed, z, starting_report)
            next_control = {"all_1114_norm": float(np.linalg.norm(later["vector"])),
                            "old_394_norm": float(np.linalg.norm(later["old"])),
                            "R2_norm": float(np.linalg.norm(later["probe"])),
                            "FE2_norm": float(np.linalg.norm(later["gravity"])),
                            "C3_norm": float(np.linalg.norm(later["constraint"]))}
        law = prescribed_source_law(system, cauchy_model, cauchy_free, z[fixed])
        law_point, law_jets = changed_fields(point, jets, reduction["sources"],
                                            law["source"], law["higher_increment"])
        source_law_controls.append({"amplitude": amplitude,
                                    "recovered_source_error": float(np.linalg.norm(law["source"]-q)),
                                    "prescribed_data_error": float(np.linalg.norm(law["higher_increment"][fixed]-z[fixed])),
                                    "all_384_residual_norm": float(np.linalg.norm(
                                        regular.equations(prepared, law_point, law_jets)["vector"])),
                                    "all_68_normal_residual_norm": float(np.linalg.norm(
                                        normal.normal_equations(prepared, law_point))),
                                    "compatibility_norm": law["compatibility_norm"]})
    projected_fixed = cauchy_model["left_null"].T @ system["matrix"][:, fixed]
    source_law_matrix = -np.linalg.pinv(cauchy_model["gate"], rcond=1e-10) @ projected_fixed
    tangential_compatibility = projected_fixed+cauchy_model["gate"] @ source_law_matrix
    if fingerprints != input_fingerprints():
        raise RuntimeError("Normal source compatibility inputs changed")
    return {"scope": "Six normal-source values after eliminating current 1200 higher-jet increments",
            "input_sha256": fingerprints, "higher_matrix_shape": list(system["matrix"].shape),
            "higher_rank": full["rank"], "higher_singular_values": full["singular"].tolist(),
            "higher_rank_cutoff": full["cutoff"], "left_gate_shape": list(full["gate"].shape),
            "remaining_source_gate_rank": full["gate_rank"], "source_gate_absolute_cutoff": 1e-8,
            "source_gate_singular_values": full["gate_singular"].tolist(),
            "base_higher_norm": float(np.linalg.norm(system["base"])),
            "base_left_compatibility_norm": float(np.linalg.norm(full["base_gate"])),
            "all_six_lift_residual_norm": float(np.linalg.norm(
                system["matrix"] @ full["source_lift"]+system["source"])),
            "source_lift_column_norms": np.linalg.norm(full["source_lift"], axis=0).tolist(),
            "frozen_block_controls": restrictions, "witnesses": rows,
            "example_source_values": (.01*pattern).tolist(),
            "example_higher_increment": (full["base_lift"]+full["source_lift"] @ (.01*pattern)).tolist(),
            "Cauchy_prescribed_coordinate_count": len(fixed),
            "Cauchy_source_law_shape": list(source_law_matrix.shape),
            "Cauchy_prescribed_compatibility_rank": int(np.linalg.matrix_rank(tangential_compatibility, tol=1e-8)),
            "Cauchy_source_law_controls": source_law_controls,
            "later_frozen_highest_control": next_control,
            "six_source_values_not_fixed_at_this_order": full["gate_rank"] == 0,
            "not_free_regional_functions_or_gauge_classification": True,
            "not_preservation_of_all_1114_equations": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "higher_rank", "remaining_source_gate_rank", "frozen_block_controls", "witnesses", "later_frozen_highest_control")}))


if __name__ == "__main__":
    main()
