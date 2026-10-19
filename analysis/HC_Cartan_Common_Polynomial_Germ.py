"""One holonomic polynomial correction, collocation and held-out PDE controls.

Finite collocation is not a regional field-equation solution.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

import importlib.util


SPEC = importlib.util.spec_from_file_location("common_polynomial_lower", Path(__file__).with_name("HC_Cartan_Lower_Spatial_Repair.py"))
lower = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lower)
general, tool = lower.general, lower.tool
RADIUS = 1/16384


def input_fingerprints():
    result = lower.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def exponents(degree):
    return [entry for entry in itertools.product(range(degree+1), repeat=4) if sum(entry) == degree]


E5, L4 = exponents(5), exponents(4)
COUNT = 16*len(E5)+24*len(E5)+16*len(L4)


def derivative_weights(powers, y, indices, amplitude):
    counts = [indices.count(i) for i in range(4)]
    values = []
    for power in powers:
        if any(power[i] < counts[i] for i in range(4)):
            values.append(0.)
            continue
        value = amplitude/RADIUS**len(indices)
        for i in range(4):
            value *= math.factorial(power[i])/math.factorial(power[i]-counts[i]) * y[i]**(power[i]-counts[i])
        values.append(value)
    return np.asarray(values)


def block_map(powers, y, indices, amplitude, components):
    return np.kron(derivative_weights(powers, y, indices, amplitude)[None, :], np.eye(components))


def field_map(x):
    y = np.asarray(x)/RADIUS
    matrix = np.zeros((440, COUNT))
    e_stop, p_stop = 16*len(E5), 40*len(E5)
    matrix[:16, :e_stop] = block_map(E5, y, (), RADIUS**2, 16)
    matrix[16:80, :e_stop] = np.vstack([block_map(E5, y, (r,), RADIUS**2, 16) for r in range(4)])
    matrix[80:240, :e_stop] = np.vstack([block_map(E5, y, pair, RADIUS**2, 16) for pair in lower.PAIRS])
    matrix[240:264, e_stop:p_stop] = block_map(E5, y, (), RADIUS, 24)
    raw = np.vstack([block_map(E5, y, (r,), RADIUS, 24) for r in range(4)])
    order = [24*r+12*part+j for part in range(2) for r in range(4) for j in range(12)]
    matrix[264:360, e_stop:p_stop] = raw[order]
    matrix[360:376, p_stop:] = block_map(L4, y, (), RADIUS, 16)
    matrix[376:, p_stop:] = np.vstack([block_map(L4, y, (r,), RADIUS, 16) for r in range(4)])
    return matrix


def pack_fields(fields):
    return np.r_[fields["coframe"].ravel(), fields["coframe_first"].ravel(),
        np.array([fields["coframe_second"][pair] for pair in lower.PAIRS]).ravel(),
        general.prior.joint.prior.realify(fields["psi"]), general.prior.joint.prior.realify(fields["psi_first"]),
        fields["multiplier"].ravel(), fields["multiplier_first"].ravel()]


def unpack_fields(values):
    values = general.cartan.checks._real(values, (440,), "common polynomial field values")
    fields = {"coframe": values[:16].reshape(4, 4), "coframe_first": values[16:80].reshape(4, 4, 4),
        "psi": general.prior.joint.prior.complexify(values[240:264], (3, 4)),
        "multiplier": values[360:376].reshape(4, 4)}
    return lower.with_lower_values(fields, np.r_[values[80:240], values[264:360], values[376:]])


def higher_correction(x, coefficients):
    y = np.asarray(x)/RADIUS
    e_stop, p_stop = 16*len(E5), 40*len(E5)
    ec = coefficients[:e_stop].reshape(len(E5), 4, 4)
    pc = coefficients[e_stop:p_stop].reshape(len(E5), 24)
    lc = coefficients[p_stop:].reshape(len(L4), 4, 4)
    p2, l2, e3 = [], [], []
    for r, s in itertools.product(range(4), repeat=2):
        real = derivative_weights(E5, y, (r, s), RADIUS) @ pc
        p2.append(general.prior.joint.prior.complexify(real, (3, 4)))
        l2.append(np.einsum("m,mab->ab", derivative_weights(L4, y, (r, s), RADIUS), lc))
    for r, s, t in itertools.product(range(4), repeat=3):
        e3.append(np.einsum("m,mab->ab", derivative_weights(E5, y, (r, s, t), RADIUS**2), ec))
    return {"p2": np.array(p2).reshape(4, 4, 3, 4), "l2": np.array(l2).reshape(4, 4, 4, 4),
            "e3": np.array(e3).reshape(4, 4, 4, 4, 4)}


def normal_coordinate_rows(rows):
    selector = np.zeros((56, 440))
    indices = list(range(80, 96))+list(range(264, 276))+list(range(312, 324))+list(range(376, 392))
    selector[:, indices] = np.eye(56)
    return rows @ selector


def field_jacobian(prepared, fields):
    values = pack_fields(fields)
    result = []
    for index in range(440):
        step = 16. if (80 <= index < 240 or 264 <= index < 360 or index >= 376) else 1e-4
        delta = np.zeros(440)
        delta[index] = step
        result.append((lower.lower_residual(prepared, unpack_fields(values+delta))
                      -lower.lower_residual(prepared, unpack_fields(values-delta)))/(2*step))
    return np.column_stack(result)


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    _, original, _, _, _ = lower.source.neighborhood.load_data()
    reduction = lower.source.normal.build_reduction(prepared, original)
    rows = normal_coordinate_rows(np.column_stack((reduction["gauge"], reduction["sources"])).T)
    services = lower.prior.previous.first.prior.create_container().services()
    training = RADIUS*np.array([[1., 0, 0, 0], [0, 1., 0, 0], [.5, .5, 0, 0]])
    controls = RADIUS*np.array([[.5, 0, 0, 0], [0, .5, 0, 0], [2**-.5, 2**-.5, 0, 0], [0, 0, 1., 0]])
    baselines = [pack_fields(general.domain.temporal.fields(prepared, point, jets, full, x)) for x in training]
    maps = [field_map(x) for x in training]
    coefficients = np.zeros(COUNT)
    history = []

    def residual(c):
        return np.concatenate([np.r_[lower.lower_residual(prepared, unpack_fields(base+matrix @ c)), rows @ (matrix @ c)]
                               for base, matrix in zip(baselines, maps)])

    for _ in range(2):
        before = residual(coefficients)
        if np.linalg.norm(before) < 1e-10:
            break

        def jacobian(entry):
            base, matrix = entry
            fields = unpack_fields(base+matrix @ coefficients)
            jac = services.cached("Cartan.common-polynomial-field-jacobian/v1", {
                "sources": fingerprints, "prepared": prepared, "numpy": np.__version__,
                "fields": fields}, lambda: {"matrix": field_jacobian(prepared, fields)})["matrix"]
            return np.vstack((jac @ matrix, rows @ matrix))

        with ThreadPoolExecutor(max_workers=2) as pool:
            jacobian_matrix = np.vstack(list(pool.map(jacobian, zip(baselines, maps))))
        system = tool.eliminate(jacobian_matrix, services=services)
        fit = tool.fit_sources(system, before)
        candidates = [(fraction, coefficients+fraction*fit["higher_increment"]) for fraction in (1., .5, .25, .125)]
        fraction, candidate = min(candidates, key=lambda entry: np.linalg.norm(residual(entry[1])))
        after = float(np.linalg.norm(residual(candidate)))
        history.append({"before": float(np.linalg.norm(before)), "after": after, "rank": system["rank"],
                        "fraction": fraction, "linear_remainder": fit["residual_norm"]})
        if after >= np.linalg.norm(before):
            break
        coefficients = candidate

    def check(x):
        base_fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        change = field_map(x) @ coefficients
        fields = unpack_fields(pack_fields(base_fields)+change)
        higher = lower.prior.previous.translated_higher(jets, full, x)
        delta = higher_correction(x, coefficients)
        changed_higher = {key: higher[key]+delta[key] for key in higher}
        first = lower.prior.previous.first_prolongation(prepared, fields, changed_higher)
        return {"coordinate": x.tolist(), "baseline_lower_norm": float(np.linalg.norm(lower.lower_residual(prepared, base_fields))),
                "corrected_lower_norm": float(np.linalg.norm(lower.lower_residual(prepared, fields))),
                "normal_coordinate_drift": float(np.linalg.norm(rows @ change)),
                "first_prolongation_norm": float(np.linalg.norm(first)),
                "field_change_norm": float(np.linalg.norm(change)),
                "base_value_changes": {"coframe": float(np.linalg.norm(change[:16])),
                    "psi": float(np.linalg.norm(change[240:264])), "multiplier": float(np.linalg.norm(change[360:376]))}}

    if fingerprints != input_fingerprints():
        raise RuntimeError("Common polynomial inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "one polynomial correction, finite lower collocation and held-out controls",
        "coefficient_count": COUNT, "coframe_spinor_degree": 5, "multiplier_degree": 4,
        "origin_jet_orders_preserved": {"coframe": 4, "psi": 4, "multiplier": 3},
        "coordinate_radius_not_physical_length": RADIUS, "history": history,
        "coefficients": coefficients.tolist(), "training": [check(x) for x in training],
        "held_out": [check(x) for x in controls], "first_prolongation_not_fitted": True,
        "no_regional_PDE_solution_or_uniform_error_bound": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in ("input_sha256", "coefficients")}, indent=2))
