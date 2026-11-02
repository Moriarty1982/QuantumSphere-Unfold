"""Direct frozen-source C3 reassembly and exact vector rounding attribution."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import mpmath
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "origin_rounding_parent", Path(__file__).with_name("HC_Cartan_Cubic_Kernel_Coefficient_Refinement.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
stable, common = prior.stable, prior.common


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Cubic_Kernel_Coefficient_Refinement.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def rational_array(value):
    value = np.asarray(value)
    if value.dtype.kind not in "fiu" or not np.all(np.isfinite(value)):
        raise ValueError("Finite real numeric array required")
    return [Fraction.from_float(float(v)) for v in value.flat]


def principal_vector(readout, fourth, quads, triples):
    if len(readout) != 4 or any(len(row) != 24 for row in readout) or len(fourth) != 35 or any(len(row) != 24 for row in fourth):
        raise ValueError("Rational readout and fourth-spinor blocks have incompatible shapes")
    values = stable.contract_readouts(readout, fourth)
    return stable.c3_entries(values, quads, triples)


def subtract(left, right):
    if len(left) != len(right):
        raise ValueError("Equal vector lengths required")
    return [a-b for a, b in zip(left, right)]


def reassemble(source, readout, fourth, quads, triples):
    principal = principal_vector(readout, fourth, quads, triples)
    if len(source) != len(principal):
        raise ValueError("Frozen source and principal row counts differ")
    return [a+b for a, b in zip(source, principal)]


def attribution(parametric, exact_rounded, matrix_rounded, raw):
    inputs = subtract(exact_rounded, parametric)
    matrix = subtract(matrix_rounded, exact_rounded)
    arithmetic = subtract(raw, matrix_rounded)
    total = subtract(raw, parametric)
    closure = [t-a-b-c for t, a, b, c in zip(total, inputs, matrix, arithmetic)]
    return {"rounded_input_vector": inputs, "rounded_matrix_vector": matrix,
        "arithmetic_vector": arithmetic, "total_vector": total,
        "exact_vector_decomposition_verified": all(v == 0 for v in closure)}


def precision_control(digits, readout, baseline, parametric, rounded, source, quads, triples):
    context = mpmath.mp.clone()
    context.dps = digits
    def number(v):
        return context.mpf(v.numerator)/v.denominator
    a = [[number(v) for v in row] for row in readout]
    src = [number(v) for v in source]
    def evaluate(blocks):
        converted = [[number(v) for v in row] for row in blocks]
        paired = [[context.fsum(x*y for x, y in zip(row, block)) for row in a] for block in converted]
        image = stable.c3_entries(paired, quads, triples)
        return [v+s for v, s in zip(image, src)]
    base, exact, raw_input = (evaluate(v) for v in (baseline, parametric, rounded))
    def norm(v):
        return context.sqrt(context.fsum(abs(x)**2 for x in v))
    return {"digits": digits, "direct_frozen_source_C3_norm": context.nstr(norm(exact), 22),
        "parametric_minus_baseline_C3_norm": context.nstr(norm([a-b for a, b in zip(exact, base)]), 22),
        "rounded_input_C3_norm": context.nstr(norm(raw_input), 22),
        "rounded_minus_parametric_C3_norm": context.nstr(norm([a-b for a, b in zip(raw_input, exact)]), 22)}


def load_inputs():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Cubic_Kernel_Coefficient_Refinement.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Cubic kernel refinement report has stale inputs")
    cauchy = common.lower.prior.previous.first.prior
    prepared, point, _, _, _, lift = prior.prior.prior.general.domain.load_data()
    coordinates, highest = np.asarray(lift["fitted_coordinates"]), np.asarray(lift["fitted_highest"])
    lc = cauchy.joint.third.lc_cubic(prepared, point)
    jets = cauchy.joint.regular.unpack(coordinates)
    source0 = cauchy.joint.third.constraint_third(prepared, point, jets, lc)
    source1 = cauchy.joint.third.diagnostic.connection_image(prepared,
        highest[:560].reshape(35, 4, 4), highest[560:880].reshape(20, 4, 4))
    source = [a+b for a, b in zip(rational_array(source0), rational_array(source1))]
    certificate = report["updated_exact_kernel_certificate"]
    readout, _, _, blocks = stable.reconstruct_certificate(certificate)
    if [[str(v) for v in row] for row in prior.reprepare.exact_readout_matrix({"psi": prepared["data"]["psi"]}).tolist()] != certificate["readout_matrix"]:
        raise ValueError("Exact readout does not match the actual origin spinor")
    floating_map = cauchy.joint.third.spatial.constraint_principal_map(prepared["data"]["psi"])
    rounded_map = [rational_array(row) for row in floating_map]
    quads, triples = list(cauchy.joint.third.diagnostic.QUADS), list(cauchy.joint.third.TRIPLES)
    baseline = [rational_array(row) for row in highest[880:].reshape(35, 24)]
    update = stable.exact_fourth_update(blocks, quads)
    parametric = [[a+b for a, b in zip(base, delta)] for base, delta in zip(baseline, update)]
    monomial_blocks = [rational_array(row) for row in np.asarray(report["candidate_rounded_spinor_coefficients"]).reshape(35, 24)]
    monomial_update = stable.exact_fourth_update(monomial_blocks, quads)
    monomial_rounded = [[a+b for a, b in zip(base, delta)] for base, delta in zip(baseline, monomial_update)]
    changed = highest.copy()
    changed[880:] += prior.reprepare.fourth_coordinates(np.asarray(report["candidate_rounded_spinor_coefficients"]), quads)
    rounded = [rational_array(row) for row in changed[880:].reshape(35, 24)]
    old_result = cauchy.evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
    new_result = cauchy.evaluate_fields(prepared, point, coordinates, changed, lc)["vector"]
    return {"readout": readout, "rounded_map": rounded_map, "baseline": baseline,
        "parametric": parametric, "monomial_rounded": monomial_rounded, "rounded": rounded,
        "source": source, "quads": quads, "triples": triples,
        "old_result": old_result, "new_result": new_result,
        "source_norms": [float(np.linalg.norm(source0)), float(np.linalg.norm(source1))]}


def evaluate():
    fingerprints, data = input_fingerprints(), load_inputs()
    a, base, exact, rounded, source, quads, triples = (data[k] for k in
        ("readout", "baseline", "parametric", "rounded", "source", "quads", "triples"))
    baseline = reassemble(source, a, base, quads, triples)
    parametric = reassemble(source, a, exact, quads, triples)
    input_rounded = reassemble(source, a, rounded, quads, triples)
    matrix_rounded = reassemble(source, data["rounded_map"], rounded, quads, triples)
    raw = rational_array(data["new_result"][-320:])
    pieces = attribution(parametric, input_rounded, matrix_rounded, raw)
    monomial_rounded = reassemble(source, a, data["monomial_rounded"], quads, triples)
    pieces["monomial_rounding_vector"] = subtract(monomial_rounded, parametric)
    pieces["highest_assembly_vector"] = subtract(input_rounded, monomial_rounded)
    input_split_exact = all(a == b+c for a, b, c in zip(pieces["rounded_input_vector"],
        pieces["monomial_rounding_vector"], pieces["highest_assembly_vector"]))
    if not pieces["exact_vector_decomposition_verified"] or not input_split_exact or baseline != parametric:
        raise ValueError("Direct kernel preservation or vector attribution failed")
    with ThreadPoolExecutor(max_workers=2) as pool:
        controls = list(pool.map(lambda digits: precision_control(digits, a, base, exact, rounded, source, quads, triples), (40, 80)))
    other = rational_array(data["old_result"][:-320])
    changed = [row.copy() for row in exact]
    changed[0][2] += Fraction(1, 2**20)
    nonkernel = subtract(reassemble(source, a, changed, quads, triples), parametric)
    if fingerprints != input_fingerprints():
        raise RuntimeError("Origin rounding attribution inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "frozen_nonlinear_source_component_norms": data["source_norms"],
        "direct_reassembled_baseline_C3_norm": stable.rational_norm(baseline),
        "direct_parametric_C3_norm": stable.rational_norm(parametric),
        "direct_parametric_matches_baseline_exactly": baseline == parametric,
        "exact_readout_rounded_input_C3_norm": stable.rational_norm(input_rounded),
        "rounded_readout_rounded_input_exact_arithmetic_C3_norm": stable.rational_norm(matrix_rounded),
        "raw_binary64_C3_norm": float(np.linalg.norm(data["new_result"][-320:])),
        "raw_binary64_1114_norm": float(np.linalg.norm(data["new_result"])),
        "direct_frozen_source_hybrid_1114_norm": stable.rational_norm(other+parametric),
        "other_794_rows_bitwise_unchanged": bool(np.array_equal(data["old_result"][:-320], data["new_result"][:-320])),
        "rounding_attribution_norms_not_additive": {name.replace("_vector", "_norm"): stable.rational_norm(value)
            for name, value in pieces.items() if name.endswith("_vector")},
        "exact_vector_decomposition_verified": pieces["exact_vector_decomposition_verified"],
        "input_rounding_subdecomposition_verified": input_split_exact,
        "exact_attribution_vectors": {name: [str(v) for v in value] for name, value in pieces.items() if name.endswith("_vector")},
        "nonkernel_perturbation_C3_change_norm": stable.rational_norm(nonkernel),
        "precision_controls": controls, "no_residual_anchor_added": True,
        "nonlinear_source_terms_recomputed_in_binary64_then_frozen": True,
        "not_a_high_precision_nonlinear_source_or_full_1114_solve": True,
        "no_interval_certificate_regional_solution_or_native_identification": True,
        "parent_polynomials_reports_and_main_TeX_PDF_unchanged": True}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_sha256", "exact_attribution_vectors")}, indent=2))
