"""Stable retained-origin updates from exact free/pivot kernel coordinates.

Anchored affine update, not a fresh high-precision evaluation of all 1114 rows.
"""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import mpmath
import numpy as np


SPEC = importlib.util.spec_from_file_location("stable_kernel_spinor", Path(__file__).with_name("HC_Cartan_Cubic_Spinor_Reprepare.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
common, general = prior.common, prior.general


def input_fingerprints():
    result = prior.input_fingerprints()
    for path in (Path(__file__), Path(__file__).with_name("HC_Cartan_Cubic_Spinor_Reprepare.json")):
        result[path.name] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def rational_matrix(values, rows, columns):
    if len(values) != rows or any(len(row) != columns for row in values):
        raise ValueError("Invalid rational certificate matrix dimensions")
    return [[Fraction(value) for value in row] for row in values]


def reconstruct_certificate(certificate):
    pivots, free = certificate["pivot_columns"], certificate["free_columns"]
    if (len(pivots) != 4 or len(free) != 20
            or sorted(pivots+free) != list(range(24))):
        raise ValueError("Invalid free/pivot partition")
    readout = rational_matrix(certificate["readout_matrix"], 4, 24)
    pivot_map = rational_matrix(certificate["pivot_map"], 4, 20)
    free_values = rational_matrix(certificate["free_monomial_coefficients"], 35, 20)
    for a in range(4):
        for j in range(20):
            if sum(readout[a][pivots[k]]*pivot_map[k][j] for k in range(4))+readout[a][free[j]]:
                raise ValueError("Pivot map does not satisfy the exact readout kernel")
    blocks = []
    for values in free_values:
        block = [Fraction(0)]*24
        for index, value in zip(free, values):
            block[index] = value
        for k, index in enumerate(pivots):
            block[index] = sum(pivot_map[k][j]*values[j] for j in range(20))
        blocks.append(block)
    return readout, pivot_map, free_values, blocks


def exact_fourth_update(blocks, quads):
    radius = Fraction.from_float(common.RADIUS)
    result = []
    for quad in quads:
        power = tuple(quad.count(i) for i in range(4))
        factor = Fraction(math.prod(math.factorial(n) for n in power), 1)/radius**3
        result.append([factor*value for value in blocks[common.L4.index(power)]])
    return result


def contract_readouts(readout, blocks):
    return [[sum(a*b for a, b in zip(row, block)) for row in readout] for block in blocks]


def c3_entries(readouts, quads, triples):
    lookup = {tuple(quad): i for i, quad in enumerate(quads)}
    return [readouts[lookup[tuple(sorted((*triple, mu)))]][a]
            for triple in triples for a in range(4) for mu in range(4)]


def rational_norm(values, digits=80):
    context = mpmath.mp.clone()
    context.dps = digits
    numbers = [context.mpf(value.numerator)/value.denominator for value in values]
    return float(context.sqrt(context.fsum(value*value for value in numbers)))


def precision_evaluation(digits, certificate, readout, pivot_map, free_values,
                         old_blocks, rounded_blocks, old_vector, quads, triples):
    context = mpmath.mp.clone()
    context.dps = digits

    def number(value):
        return context.mpf(value.numerator)/value.denominator

    a = [[number(value) for value in row] for row in readout]
    pm = [[number(value) for value in row] for row in pivot_map]
    monomials = []
    for values in free_values:
        fv = [number(value) for value in values]
        block = [context.mpf(0)]*24
        for i, value in zip(certificate["free_columns"], fv):
            block[i] = value
        for k, i in enumerate(certificate["pivot_columns"]):
            block[i] = context.fsum(pm[k][j]*fv[j] for j in range(20))
        monomials.append(block)
    radius = number(Fraction.from_float(common.RADIUS))
    delta = []
    for quad in quads:
        power = tuple(quad.count(i) for i in range(4))
        scale = math.prod(math.factorial(n) for n in power)/radius**3
        delta.append([scale*value for value in monomials[common.L4.index(power)]])
    old = [[number(value) for value in row] for row in old_blocks]
    rounded = [[number(value) for value in row] for row in rounded_blocks]

    def read(block):
        return [context.fsum(row[j]*block[j] for j in range(24)) for row in a]

    incremental = [read(block) for block in delta]
    direct, rounded_direct = [], []
    for base, change, rounded_new in zip(old, delta, rounded):
        before = read(base)
        after = read([x+y for x, y in zip(base, change)])
        rounded_after = read(rounded_new)
        direct.append([x-y for x, y in zip(after, before)])
        rounded_direct.append([x-y for x, y in zip(rounded_after, before)])
    direct_vector = c3_entries(direct, quads, triples)
    incremental_vector = c3_entries(incremental, quads, triples)
    rounded_vector = c3_entries(rounded_direct, quads, triples)

    def norm(values):
        return context.sqrt(context.fsum(abs(value)**2 for value in values))

    anchor = [number(Fraction.from_float(float(value))) for value in old_vector]
    anchored = anchor.copy()
    rounded_anchored = anchor.copy()
    for i in range(320):
        anchored[794+i] += direct_vector[i]
        rounded_anchored[794+i] += rounded_vector[i]
    return {"decimal_digits": digits,
        "parametric_incremental_C3_update_norm": context.nstr(norm(incremental_vector), 18),
        "parametric_direct_C3_update_norm": context.nstr(norm(direct_vector), 18),
        "direct_incremental_difference_norm": context.nstr(norm([x-y for x, y in zip(direct_vector, incremental_vector)]), 18),
        "stable_anchored_1114_norm": context.nstr(norm(anchored), 18),
        "rounded_input_high_precision_C3_update_norm": context.nstr(norm(rounded_vector), 18),
        "rounded_input_anchored_1114_norm": context.nstr(norm(rounded_anchored), 18)}


def load_case():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Cubic_Spinor_Reprepare.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Spinor reprepare report is stale")
    prepared, point, jets, _, full, lift = general.domain.load_data()
    origin = general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
    certificate = report["exact_origin_preservation_certificate"]
    readout, pm, free, blocks = reconstruct_certificate(certificate)
    actual = prior.exact_readout_matrix(origin)
    if any(readout[a][j] != Fraction(str(actual[a, j])) for a in range(4) for j in range(24)):
        raise ValueError("Certificate readout does not match the frozen origin")
    cauchy = common.lower.prior.previous.first.prior
    quads, triples = list(cauchy.joint.third.diagnostic.QUADS), list(cauchy.joint.third.TRIPLES)
    coordinates = np.asarray(lift["fitted_coordinates"])
    highest = np.asarray(lift["fitted_highest"])
    lc = cauchy.joint.third.lc_cubic(prepared, point)
    old_vector = cauchy.evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
    rounded = highest.copy()
    rounded[880:] += prior.fourth_coordinates(np.asarray(report["spinor_degree_four_coefficients"]), quads)
    rounded_vector = cauchy.evaluate_fields(prepared, point, coordinates, rounded, lc)["vector"]
    old_blocks = [[Fraction.from_float(float(value)) for value in row] for row in highest[880:].reshape(35, 24)]
    rounded_blocks = [[Fraction.from_float(float(value)) for value in row] for row in rounded[880:].reshape(35, 24)]
    return certificate, readout, pm, free, blocks, old_blocks, rounded_blocks, old_vector, rounded_vector, quads, triples


def evaluate():
    fingerprints = input_fingerprints()
    certificate, readout, pm, free, blocks, old, rounded, old_vector, rounded_vector, quads, triples = load_case()
    exact_delta = exact_fourth_update(blocks, quads)
    exact_c3 = c3_entries(contract_readouts(readout, exact_delta), quads, triples)
    rounded_delta = [[x-y for x, y in zip(new, base)] for new, base in zip(rounded, old)]
    rounded_exact_c3 = c3_entries(contract_readouts(readout, rounded_delta), quads, triples)
    with ThreadPoolExecutor(max_workers=2) as pool:
        checks = list(pool.map(lambda digits: precision_evaluation(
            digits, certificate, readout, pm, free, old, rounded, old_vector, quads, triples), (40, 80)))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Stable kernel inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "stable retained-equation affine update anchored to the inherited residual",
        "exact_parametric_C3_update_zero": all(value == 0 for value in exact_c3),
        "rounded_input_exact_C3_update_zero": all(value == 0 for value in rounded_exact_c3),
        "rounded_input_exact_C3_update_norm": rational_norm(rounded_exact_c3),
        "binary64_update_discrepancy_from_exact_rounded_input": float(np.linalg.norm(
            (rounded_vector-old_vector)[-320:]-np.array([float(value) for value in rounded_exact_c3]))),
        "old_binary64_anchor_1114_norm": float(np.linalg.norm(old_vector)),
        "rounded_binary64_recomputed_1114_norm": float(np.linalg.norm(rounded_vector)),
        "precision_checks": checks, "numerical_libraries": {"mpmath": mpmath.__version__, "numpy": np.__version__},
        "anchor_is_binary64_residual_not_full_high_precision_recomputation": True,
        "not_an_independent_full_1114_high_precision_solve": True,
        "no_regional_solution_or_new_order_solved": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
