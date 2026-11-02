"""Sample the first source gate in a general-coframe coordinate chart.

Directional numerical derivatives and sampled ranks, not a regional solution.
"""
from concurrent.futures import ThreadPoolExecutor
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


first = local_module("general_first_previous", "HC_Cartan_First_Compatibility_Source_Gate.py")
split = local_module("general_first_split", "HC_Cartan_Normal_Compatibility_Split.py")
general, source = split.general, first.source
FIELD_KEYS = ("coframe", "coframe_first", "coframe_second", "psi", "psi_first",
              "multiplier", "multiplier_first")


def input_fingerprints():
    result = first.input_fingerprints()
    result.update(split.input_fingerprints())
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def translated_higher(jets, full, x):
    return {"e3": jets["e3"]+np.einsum("u,rstuam->rstam", x, full["e4"]),
            "p2": jets["p2"]+np.einsum("t,rstij->rsij", x, jets["p3"])
                  +np.einsum("t,u,rstuij->rsij", x, x, full["p4"])/2,
            "l2": jets["l2"]+np.einsum("t,rstam->rsam", x, full["l3"])}


def field_derivatives(fields, higher):
    return [{"coframe": fields["coframe_first"][r],
             "coframe_first": fields["coframe_second"][r],
             "coframe_second": higher["e3"][r], "psi": fields["psi_first"][r],
             "psi_first": higher["p2"][r], "multiplier": fields["multiplier_first"][r],
             "multiplier_first": higher["l2"][r]} for r in range(4)]


def displaced_fields(fields, derivative, distance):
    return {key: fields[key]+distance*derivative.get(key, 0) for key in FIELD_KEYS}


def first_prolongation(prepared, fields, higher, step=1e-4):
    """Five-point directional derivatives along each holonomic first jet."""
    rows = []
    for derivative in field_derivatives(fields, higher):
        values = [general.equations(prepared, displaced_fields(fields, derivative, k*step))["vector"]
                  for k in (-2, -1, 1, 2)]
        rows.append((values[0]-8*values[1]+8*values[2]-values[3])/(12*step))
    return np.concatenate(rows)


def normal_higher_matrix(prepared, fields, allowed):
    """Differentiate only the polynomial highest-jet dependence; no small step."""
    columns = []
    for index in allowed:
        vector = np.zeros(1200)
        vector[index] = 1
        delta = source.regular.unpack(vector)
        rows = []
        for r in range(4):
            derivative = {"coframe_second": delta["e3"][r],
                          "psi_first": delta["p2"][r],
                          "multiplier_first": delta["l2"][r]}
            if not any(np.any(value) for value in derivative.values()):
                rows.append(np.zeros(68))
                continue
            plus = general.equations(prepared, displaced_fields(fields, derivative, 16.))["vector"]
            minus = general.equations(prepared, displaced_fields(fields, derivative, -16.))["vector"]
            rows.append((plus-minus)/32.)
        columns.append(np.concatenate(rows))
    return np.column_stack(columns)


def transported_sources(matrix, coordinate_rows):
    chart = general.chart_report(matrix, coordinate_rows)
    target = np.zeros((84, 6))
    target[-6:] = np.eye(6)
    return chart["inverse"] @ target, chart["augmented_minimum_singular"]


def source_response(prepared, fields, higher, directions, step=1e-4, source_step=.002):
    values = general.normal_values(fields)
    columns = []
    for direction in directions.T:
        plus = general.with_normal_values(fields, values+source_step*direction)
        minus = general.with_normal_values(fields, values-source_step*direction)
        columns.append((first_prolongation(prepared, plus, higher, step)
                        -first_prolongation(prepared, minus, higher, step))/(2*source_step))
    return np.column_stack(columns)


def evaluate():
    fingerprints = input_fingerprints()
    services = first.prior.create_container().services()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    _, original_point, _, _, _ = source.neighborhood.load_data()
    reduction = source.normal.build_reduction(prepared, original_point)
    coordinate_rows = np.column_stack((reduction["gauge"], reduction["sources"])).T
    blocks = source.allowed_cauchy_coordinates()
    allowed = np.array(blocks["psi2"]+blocks["lambda2"]+blocks["e3"])
    original = first.load_system()
    origin_matrix = first.extraction_matrix() @ original[7][:, allowed]
    origin_response = first.extraction_matrix() @ original[8]
    origin_expected = first.extraction_matrix() @ source.regular.equations(prepared, point, jets)["vector"]
    radius = 1/16384

    def sample(x):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        higher = translated_higher(jets, full, x)
        normal = split.direct_normal_matrix(prepared, fields)
        directions, minimum = transported_sources(normal, coordinate_rows)
        matrix = services.cached("Cartan.general-first-normal-higher/v1", {
            "sources": fingerprints, "numpy": np.__version__, "prepared": prepared,
            "fields": {key: fields[key] for key in FIELD_KEYS}, "allowed": allowed},
            lambda: {"matrix": normal_higher_matrix(prepared, fields, allowed)})["matrix"]
        response = source_response(prepared, fields, higher, directions)
        response_half = source_response(prepared, fields, higher, directions, step=5e-5)
        model = first.eliminate(matrix, response)
        model_half = first.eliminate(matrix, response_half)
        actual = first_prolongation(prepared, fields, higher)
        actual_half = first_prolongation(prepared, fields, higher, step=5e-5)
        projected = model["left_null"].T @ actual
        correction = -np.linalg.lstsq(model["gate"], projected, rcond=1e-10)[0]
        remainder = projected+model["gate"] @ correction
        primary = general.equations(prepared, fields)["vector"]
        trial = general.with_normal_values(fields, general.normal_values(fields)+directions @ correction)
        result = {"coordinate": x.tolist(), "normal_rank": general.chart_report(normal, coordinate_rows)["rank"],
            "augmented_minimum_singular": minimum,
            "normal_kernel_error": float(np.linalg.norm(normal @ directions)),
            "coordinate_transport_error": float(np.linalg.norm(coordinate_rows @ directions-np.vstack((np.zeros((10, 6)), np.eye(6))))),
            "higher_rank": model["rank"], "source_gate_rank": model["gate_rank"],
            "gate_singular_values": model["gate_singular"].tolist(),
            "half_step_gate_singular_values": model_half["gate_singular"].tolist(),
            "source_response_step_change": float(np.linalg.norm(response-response_half)),
            "primary_residual_norm": float(np.linalg.norm(primary)),
            "first_prolongation_norm": float(np.linalg.norm(actual)),
            "first_prolongation_step_change": float(np.linalg.norm(actual-actual_half)),
            "linear_source_correction": correction.tolist(),
            "projected_residual_before": float(np.linalg.norm(projected)),
            "projected_residual_after_linear_source_correction": float(np.linalg.norm(remainder)),
            "primary_change_after_source_correction": float(np.linalg.norm(general.equations(prepared, trial)["vector"]-primary))}
        if not np.any(x):
            result.update(origin_higher_matrix_error=float(np.linalg.norm(matrix-origin_matrix)),
                          origin_source_response_error=float(np.linalg.norm(response-origin_response)),
                          origin_prolongation_error=float(np.linalg.norm(actual-origin_expected)))
        return result

    # Independent point diagnostics share immutable prepared coefficients only.
    with ThreadPoolExecutor(max_workers=2) as pool:
        samples = list(pool.map(sample, (np.zeros(4), radius*np.eye(4)[0], radius*np.eye(4)[1])))
    if fingerprints != input_fingerprints():
        raise RuntimeError("General first source gate inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "sampled general first-prolongation source tangent gate",
            "sample_radius_not_uniform_source_gate_certificate": radius,
            "source_directions_are_coordinate_kernel_sections_not_physical_classification": True,
            "directional_derivatives_are_numerical": True, "main_TeX_PDF_changed": False,
            "samples": samples}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps(result["samples"], indent=2))
