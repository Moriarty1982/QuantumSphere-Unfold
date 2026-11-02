"""Polynomial exterior compatibility of retained constitutive and curl defects."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "exterior_compatibility_parent", Path(__file__).with_name("HC_Cartan_Centered_Spinor_Source_Bound.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
core, common = prior.core, prior.common


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Centered_Spinor_Source_Bound.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def powers(degree):
    if degree < 0:
        return ()
    return tuple(common.exponents(degree))


def form_indices(order):
    if order not in range(5):
        raise ValueError("Form order must lie between zero and four")
    return tuple(itertools.combinations(range(4), order))


def derivative_matrix(degree, order):
    if degree < 0 or order not in range(4):
        raise ValueError("Nonnegative degree and form order below four required")
    source, target = powers(degree), powers(degree-1)
    indices, outputs = form_indices(order), form_indices(order+1)
    target_index = {p: i for i, p in enumerate(target)}
    matrix = np.zeros((len(target)*len(outputs), len(source)*len(indices)), dtype=np.int64)
    for i, p in enumerate(source):
        for j, output in enumerate(outputs):
            for slot, axis in enumerate(output):
                if not p[axis]:
                    continue
                q = list(p)
                q[axis] -= 1
                column = indices.index(output[:slot]+output[slot+1:])
                matrix[target_index[tuple(q)]*len(outputs)+j, i*len(indices)+column] += (-1)**slot*p[axis]
    return matrix


def contraction_matrix(degree, order):
    if degree < 0 or order not in range(1, 5):
        raise ValueError("Nonnegative degree and positive form order required")
    source, target = powers(degree), powers(degree+1)
    indices, outputs = form_indices(order), form_indices(order-1)
    target_index = {p: i for i, p in enumerate(target)}
    matrix = np.zeros((len(target)*len(outputs), len(source)*len(indices)), dtype=np.int64)
    for i, p in enumerate(source):
        for j, output in enumerate(outputs):
            for axis in range(4):
                if axis in output:
                    continue
                combined = tuple(sorted((axis, *output)))
                sign = (-1)**combined.index(axis)
                q = list(p)
                q[axis] += 1
                matrix[target_index[tuple(q)]*len(outputs)+j, i*len(indices)+indices.index(combined)] += sign
    return matrix


def integer_product(left, right):
    if left.dtype != np.int64 or right.dtype != np.int64:
        raise ValueError("Integer coefficient maps required")
    bound = left.shape[1]*max((abs(int(v)) for v in left.flat), default=0)*max((abs(int(v)) for v in right.flat), default=0)
    if bound >= 2**63:
        raise ValueError("Integer product overflow bound unresolved")
    return left @ right


def exact_quartic_certificate():
    d1, d2 = derivative_matrix(5, 1), derivative_matrix(4, 2)
    i2, i3 = contraction_matrix(4, 2), contraction_matrix(3, 3)
    exact, remainder = integer_product(d1, i2), integer_product(i3, d2)
    identity = np.eye(exact.shape[0], dtype=np.int64)
    if (not np.array_equal(exact+remainder, 6*identity)
            or not np.array_equal(integer_product(exact, exact), 6*exact)
            or np.any(integer_product(d2, exact))):
        raise ValueError("Polynomial homotopy coefficient identity failed")
    trace = int(np.trace(exact))
    if trace % 6:
        raise ValueError("Homotopy projector trace is not integral")
    rank = trace//6
    return {"homogeneous_degree": 4, "form_order": 2, "homotopy_denominator": 6,
        "single_component_two_form_dimension": exact.shape[0],
        "single_component_closed_dimension": rank,
        "single_component_compatibility_rank": exact.shape[0]-rank,
        "four_component_curl_dimension": 4*exact.shape[0],
        "four_component_closed_dimension": 4*rank,
        "four_component_compatibility_rank": 4*(exact.shape[0]-rank),
        "integer_homotopy_and_projector_identities_verified": True,
        "projector_need_not_be_orthogonal": True,
        "coefficient_map_sha256": hashlib.sha256(b"".join(a.tobytes() for a in (d1, d2, i2, i3))).hexdigest()}


def lowest_possible_residual_degree(coframe_degree, spinor_degree, multiplier_degree):
    degrees = (coframe_degree, spinor_degree, multiplier_degree)
    if any(not isinstance(v, int) for v in degrees) or min(degrees) < 2:
        raise ValueError("Field correction degrees must be integers at least two")
    # The 80-row evaluator uses at most E'', psi' and lambda'; inverse centers are nonsingular.
    return min(coframe_degree-2, spinor_degree-1, multiplier_degree-1)


def homogeneous(coefficients, degree, block):
    values = np.stack([coefficients[core.INDEX[p], block] for p in powers(degree)])
    if block.start == 0:
        return values.reshape(-1, 4, 4).transpose(0, 2, 1).reshape(-1, 4)
    return values.reshape(-1, 4)


def analyze_report(report):
    coefficients, radius = np.asarray(report["coefficients"]), report["radius"]
    if coefficients.shape != (70, 80) or not np.all(np.isfinite(coefficients)) or radius <= 0:
        raise ValueError("Finite 70-by-80 coefficient array and positive radius required")
    levels = []
    for degree in range(4):
        constitutive = homogeneous(coefficients, degree+1, slice(0, 16))
        curls = homogeneous(coefficients, degree, slice(56, 80))
        predicted = derivative_matrix(degree+1, 1) @ constitutive/radius
        levels.append({"curl_degree": degree, "constitutive_degree": degree+1,
            "curl_coefficient_norm": float(np.linalg.norm(curls)),
            "d_constitutive_coefficient_norm": float(np.linalg.norm(predicted)),
            "identity_discrepancy_norm": float(np.linalg.norm(curls-predicted))})
    curls = homogeneous(coefficients, 4, slice(56, 80))
    derivative = derivative_matrix(4, 2) @ curls
    potential = radius*(contraction_matrix(4, 2) @ curls)/6
    represented = derivative_matrix(5, 1) @ potential/radius
    obstruction = contraction_matrix(3, 3) @ derivative/6
    return {"radius": radius, "lower_coefficient_identity_controls": levels,
        "quartic_curl_norm": float(np.linalg.norm(curls)),
        "dimensionless_d_curl_norm": float(np.linalg.norm(derivative)),
        "physical_d_curl_norm": float(np.linalg.norm(derivative)/radius),
        "formal_constitutive_degree_five_target_norm": float(np.linalg.norm(potential)),
        "closed_reconstruction_norm": float(np.linalg.norm(represented)),
        "homotopy_obstruction_norm": float(np.linalg.norm(obstruction)),
        "homotopy_reconstruction_discrepancy": float(np.linalg.norm(curls-represented-obstruction)),
        "formal_constitutive_degree_five_potential": potential.reshape(len(powers(5)), 4, 4).tolist(),
        "quartic_curl_coefficients": curls.reshape(len(powers(4)), 6, 4).tolist(),
        "potential_is_not_a_field_correction": True,
        "nonzero_floating_compatibility_defect_not_zeroed": True}


def evaluate():
    fingerprints = input_fingerprints()
    report = json.loads(Path(__file__).with_name("HC_Cartan_Centered_Spinor_Source_Bound.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Centered source report has stale inputs")
    certificate = exact_quartic_certificate()
    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(analyze_report, report["reports"]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Exterior compatibility inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "exact_polynomial_complex_certificate": certificate,
        "coefficient_relation": "curl = d_x C; d_x curl = 0",
        "homotopy_identity": "F4=d_y(i_y F4/6)+i_y(d_y F4)/6",
        "next_order_additions": {"coframe_degree": 7, "spinor_degree": 6, "multiplier_degree": 6,
            "lowest_possible_change_in_80_row_residual_degree": lowest_possible_residual_degree(7, 6, 6)},
        "next_order_extensions_cannot_remove_existing_degree_four_defects": True,
        "formal_potential_realizability_by_allowed_fields_not_established": True,
        "no_new_fit_field_or_low_order_coefficient_change": True,
        "floating_identity_discrepancies_are_not_exact_incompatibility_certificates": True,
        "not_regional_existence_or_native_identification": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"certificate": result["exact_polynomial_complex_certificate"], "reports": [
        {k: v for k, v in r.items() if k not in ("formal_constitutive_degree_five_potential", "quartic_curl_coefficients")}
        for r in result["reports"]]}, indent=2))
