"""Repair lower equations and spatial curls with fixed normal coordinates.

Independent local jets, not an integrable regional field or full higher completion.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def import_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prior = import_path("lower_repair_attribution", Path(__file__).with_name("HC_Cartan_First_Compatibility_Attribution.py"))
TOOL_PATH = Path(__file__).resolve().parents[1] / "skills/finite-jet-compatibility/scripts/compatibility.py"
tool = import_path("lower_repair_compatibility_tool", TOOL_PATH)
general, source = prior.general, prior.source
PAIRS = list(source.prior.PAIR2)


def input_fingerprints():
    result = prior.input_fingerprints()
    for name, path in ((Path(__file__).name, Path(__file__)),
                       ("skills/finite-jet-compatibility/scripts/compatibility.py", TOOL_PATH)):
        result[name] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def lower_values(fields):
    return np.r_[np.array([fields["coframe_second"][pair] for pair in PAIRS]).ravel(),
                 general.prior.joint.prior.realify(fields["psi_first"]),
                 fields["multiplier_first"].ravel()]


def with_lower_values(fields, values):
    values = general.cartan.checks._real(values, (320,), "lower derivative coordinates")
    changed = dict(fields)
    second = np.empty((4, 4, 4, 4))
    for pair, value in zip(PAIRS, values[:160].reshape(10, 4, 4)):
        second[pair[0], pair[1]] = value
        second[pair[1], pair[0]] = value
    changed["coframe_second"] = second
    changed["psi_first"] = general.prior.joint.prior.complexify(values[160:256], (4, 3, 4))
    changed["multiplier_first"] = values[256:].reshape(4, 4, 4).copy()
    return changed


def normal_selector():
    indices = list(range(16))+list(range(160, 172))+list(range(208, 220))+list(range(256, 272))
    return np.eye(320)[indices]


def free_basis(coordinate_rows):
    fixed = coordinate_rows @ normal_selector()
    _, singular, right = np.linalg.svd(fixed, full_matrices=True)
    if np.sum(singular > 1e-10) != 16:
        raise ValueError("Sixteen independent normal coordinate rows required")
    return right[16:].T


def lower_residual(prepared, fields):
    evaluated = general.equations(prepared, fields)
    return np.r_[evaluated["vector"], prior.constitutive_curls(fields, evaluated)[12:]]


def lower_jacobian(prepared, fields, basis):
    values = lower_values(fields)
    columns = []
    for direction in basis.T:
        plus = lower_residual(prepared, with_lower_values(fields, values+16*direction))
        minus = lower_residual(prepared, with_lower_values(fields, values-16*direction))
        columns.append((plus-minus)/32)
    return np.column_stack(columns)


def repair_lower(prepared, fields, coordinate_rows, services, fingerprints):
    basis = free_basis(coordinate_rows)
    original = lower_values(fields)
    values = original.copy()
    history = []
    for _ in range(3):
        current = with_lower_values(fields, values)
        residual = lower_residual(prepared, current)
        if np.linalg.norm(residual) < 1e-10:
            break
        jacobian = services.cached("Cartan.lower-spatial-repair-jacobian/v1", {
            "sources": fingerprints, "prepared": prepared, "numpy": np.__version__,
            "fields": {key: current[key] for key in prior.previous.FIELD_KEYS}, "basis": basis},
            lambda: {"matrix": lower_jacobian(prepared, current, basis)})["matrix"]
        system = tool.eliminate(jacobian, services=services)
        fit = tool.fit_sources(system, residual)
        correction = basis @ fit["higher_increment"]
        candidates = [(fraction, values+fraction*correction) for fraction in (1., .5, .25, .125)]
        fraction, proposed = min(candidates, key=lambda entry: np.linalg.norm(
            lower_residual(prepared, with_lower_values(fields, entry[1]))))
        after = float(np.linalg.norm(lower_residual(prepared, with_lower_values(fields, proposed))))
        history.append({"before": float(np.linalg.norm(residual)), "after": after,
                        "jacobian_rank": system["rank"], "step_fraction": fraction,
                        "linear_remainder": fit["residual_norm"]})
        if after >= np.linalg.norm(residual):
            break
        values = proposed
    repaired = with_lower_values(fields, values)
    return repaired, {"history": history, "initial_norm": float(np.linalg.norm(lower_residual(prepared, fields))),
        "final_norm": float(np.linalg.norm(lower_residual(prepared, repaired))),
        "lower_increment_norm": float(np.linalg.norm(values-original)),
        "fixed_coordinate_error": float(np.linalg.norm(coordinate_rows @ normal_selector() @ (values-original))),
        "fitted_lower_coordinates": values.tolist()}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    _, original_point, _, _, _ = source.neighborhood.load_data()
    reduction = source.normal.build_reduction(prepared, original_point)
    coordinate_rows = np.column_stack((reduction["gauge"], reduction["sources"])).T
    services = prior.previous.first.prior.create_container().services()

    def sample(x):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        higher = prior.previous.translated_higher(jets, full, x)
        repaired, lower = repair_lower(prepared, fields, coordinate_rows, services, fingerprints)
        evaluated = general.equations(prepared, repaired)
        matrix = prior.cached_matrix(services, prepared, repaired, np.arange(720), fingerprints)
        actual = prior.previous.first_prolongation(prepared, repaired, higher)
        system = tool.eliminate(matrix, services=services)
        fit = tool.fit_sources(system, actual)
        delta = source.regular.unpack(np.r_[fit["higher_increment"], np.zeros(480)])
        corrected_higher = {key: higher[key]+delta[key] for key in higher}
        direct = prior.previous.first_prolongation(prepared, repaired, corrected_higher)
        half = prior.previous.first_prolongation(prepared, repaired, corrected_higher, step=5e-5)
        attribution = tool.attribute_left_space(system, prior.known_rows(repaired),
                                               prior.known_rhs(repaired, evaluated), actual)
        return {"coordinate": x.tolist(), "lower_repair": lower,
            "fixed_normal_coordinates": (coordinate_rows @ general.normal_values(fields)).tolist(),
            "primary_residual_norm": float(np.linalg.norm(evaluated["vector"])),
            "all_constitutive_curls_norm": float(np.linalg.norm(prior.constitutive_curls(repaired, evaluated))),
            "known_identity_sources_norm": float(np.linalg.norm(prior.known_rhs(repaired, evaluated))),
            "higher_rank": system["rank"], "attribution": attribution,
            "first_before_higher_correction": float(np.linalg.norm(actual)),
            "first_after_higher_correction": float(np.linalg.norm(direct)),
            "first_after_half_step": float(np.linalg.norm(half)),
            "higher_direct_affinity_error": float(np.linalg.norm(direct-fit["residual"])),
            "higher_increment_norm": float(np.linalg.norm(fit["higher_increment"])),
            "higher_increment": fit["higher_increment"].tolist(),
            "known_identity_sources_not_assumed_zero": True}

    with ThreadPoolExecutor(max_workers=2) as pool:
        samples = list(pool.map(sample, (np.eye(4)[0]/16384, np.eye(4)[1]/16384)))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Lower repair inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "independent pointwise lower/spatial repairs and first prolongation",
            "fixed_fields": ["coframe", "coframe_first", "psi", "multiplier"],
            "lower_coordinates": 320, "fixed_normal_coordinates": 16, "free_lower_coordinates": 304,
            "primary_plus_spatial_curl_rows": 80, "samples": samples,
            "no_integrable_regional_field_or_1114_completion": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps([{key: value for key, value in sample.items() if key != "higher_increment" and key != "fixed_normal_coordinates"}
                     | {"lower_repair": {key: value for key, value in sample["lower_repair"].items()
                                           if key != "fitted_lower_coordinates"}} for sample in result["samples"]], indent=2))
