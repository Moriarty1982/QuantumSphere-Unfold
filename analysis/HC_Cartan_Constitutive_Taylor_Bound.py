"""Cancellation-preserving degree-four Taylor models for 16 constraints.

Polynomial coefficients and a whole-cube tail, evaluated in binary64 only.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "constitutive_taylor_parent", Path(__file__).with_name("HC_Cartan_Uniform_Residual_Bound.py"))
previous = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(previous)
control, common, general = previous.previous, previous.common, previous.general
POWERS = [p for degree in range(5) for p in common.exponents(degree)]
INDEX = {p: i for i, p in enumerate(POWERS)}
DEGREES = np.array([sum(p) for p in POWERS])
PAIRS = [(i, j, INDEX[tuple(a+b for a, b in zip(p, q))])
         for i, p in enumerate(POWERS) for j, q in enumerate(POWERS) if sum(p)+sum(q) <= 4]
LEFT, RIGHT, OUTPUT = np.asarray(PAIRS).T
HIGH = DEGREES[:, None]+DEGREES[None, :] > 4


def input_fingerprints():
    result = previous.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


class TaylorTensor:
    """P(y) plus a Frobenius tail on |y_i| <= 1; no rounding enclosure."""

    def __init__(self, coefficients, tail=0.):
        self.coefficients = np.asarray(coefficients)
        if (self.coefficients.ndim < 1 or len(self.coefficients) != len(POWERS)
                or not np.all(np.isfinite(self.coefficients)) or not np.isfinite(tail) or tail < 0):
            raise ValueError("Seventy finite coefficient tensors and a nonnegative tail required")
        self.tail = float(tail)

    @property
    def center(self):
        return self.coefficients[0]

    def coefficient_norms(self):
        return np.linalg.norm(self.coefficients.reshape(len(POWERS), -1), axis=1)

    def polynomial_norm(self):
        return float(sum(self.coefficient_norms()))

    def is_constant(self):
        return self.tail == 0 and not np.any(self.coefficients[1:])

    def __add__(self, other):
        other = tensor(other)
        if self.center.shape != other.center.shape:
            raise ValueError("Taylor addition does not broadcast")
        return TaylorTensor(self.coefficients+other.coefficients, self.tail+other.tail)

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+-tensor(other)

    def scale(self, value):
        return TaylorTensor(self.coefficients*value, abs(value)*self.tail)

    def conjugate(self):
        return TaylorTensor(self.coefficients.conj(), self.tail)

    def real(self):
        return TaylorTensor(self.coefficients.real, self.tail)

    def imag(self):
        return TaylorTensor(self.coefficients.imag, self.tail)

    def transpose(self, *axes):
        return TaylorTensor(self.coefficients.transpose(0, *(i+1 for i in axes)), self.tail)

    def __getitem__(self, index):
        indices = index if isinstance(index, tuple) else (index,)
        if any(not isinstance(i, (slice, int)) for i in indices):
            raise ValueError("Only basic contractive Taylor slices supported")
        return TaylorTensor(self.coefficients[(slice(None), *indices)], self.tail)

    def evaluate(self, y):
        y = np.asarray(y, float)
        if y.shape != (4,) or not np.all(np.isfinite(y)) or np.max(abs(y)) > 1:
            raise ValueError("Evaluation requires a point in the normalized four-cube")
        weights = np.array([np.prod(y**p) for p in POWERS])
        return np.tensordot(weights, self.coefficients, axes=1)


def tensor(value):
    if isinstance(value, TaylorTensor):
        return value
    value = np.asarray(value)
    coefficients = np.zeros((len(POWERS), *value.shape), dtype=value.dtype)
    coefficients[0] = value
    return TaylorTensor(coefficients)


def binary_contract(a_labels, b_labels, output, a, b):
    dimensions, occurrences = {}, {}
    for labels, value in ((a_labels, a), (b_labels, b)):
        if len(labels) != value.center.ndim or len(set(labels)) != len(labels) or "Z" in labels:
            raise ValueError("Explicit unique tensor indices required; Z is reserved")
        for label, size in zip(labels, value.center.shape):
            if label in dimensions and dimensions[label] != size:
                raise ValueError("Taylor contraction dimensions disagree")
            dimensions[label] = size
            occurrences[label] = occurrences.get(label, 0)+1
    factor = float(np.prod([np.sqrt(dimensions[k]) for k, count in occurrences.items() if count == 1 and k not in output]))
    if a.is_constant():
        coefficients = np.einsum(f"{a_labels},Z{b_labels}->Z{output}", a.center, b.coefficients, optimize=True)
    elif b.is_constant():
        coefficients = np.einsum(f"Z{a_labels},{b_labels}->Z{output}", a.coefficients, b.center, optimize=True)
    else:
        products = np.einsum(f"Z{a_labels},Z{b_labels}->Z{output}",
                             a.coefficients[LEFT], b.coefficients[RIGHT], optimize=True)
        coefficients = np.zeros((len(POWERS), *products.shape[1:]), dtype=products.dtype)
        np.add.at(coefficients, OUTPUT, products)
    an, bn = a.coefficient_norms(), b.coefficient_norms()
    discarded = float(np.sum((an[:, None]*bn[None, :])[HIGH]))
    tail = factor*(discarded+a.tail*(sum(bn)+b.tail)+sum(an)*b.tail)
    return TaylorTensor(coefficients, tail)


def contract(expression, *values):
    labels, output = expression.split("->")
    labels = labels.split(",")
    if len(labels) != len(values) or len(values) < 2:
        raise ValueError("At least two operands matching the expression required")
    values = [tensor(value) for value in values]
    result, current = values[0], labels[0]
    for i in range(1, len(values)):
        needed = output+"".join(labels[i+1:])
        retained = "".join(dict.fromkeys(k for k in current+labels[i] if k in needed))
        if i == len(values)-1:
            retained = output
        result = binary_contract(current, labels[i], retained, result, values[i])
        current = retained
    return result


def matrix_inverse(value):
    """Truncated Neumann series, including discarded terms and geometric tail."""
    if value.center.ndim != 2 or value.center.shape[0] != value.center.shape[1]:
        raise ValueError("Square Taylor matrix required")
    inverse = np.linalg.inv(value.center)
    delta = value-tensor(value.center)
    z = contract("ij,jk->ik", -inverse, delta)
    q = z.polynomial_norm()+z.tail
    if q >= 1:
        raise ValueError("Neumann majorant is unresolved")
    power = tensor(np.eye(len(inverse)))
    total = power
    for _ in range(4):
        power = contract("ij,jk->ik", power, z)
        total = total+power
    result = contract("ij,jk->ik", total, inverse)
    result.tail += q**5/(1-q)*float(np.linalg.norm(inverse))
    return result, q


def stack(values):
    return TaylorTensor(np.stack([v.coefficients for v in values], axis=1), float(np.linalg.norm([v.tail for v in values])))


def monomial_terms(powers, coefficients, amplitude, radius, derivative=()):
    coefficients = np.asarray(coefficients)
    output = np.zeros((len(POWERS), *coefficients.shape[1:]), dtype=coefficients.dtype)
    tail = 0.
    counts = [derivative.count(i) for i in range(4)]
    for p, coefficient in zip(powers, coefficients):
        if any(p[i] < counts[i] for i in range(4)):
            continue
        remaining = tuple(p[i]-counts[i] for i in range(4))
        factor = amplitude/common.RADIUS**len(derivative)*(radius/common.RADIUS)**sum(remaining)
        for i in range(4):
            factor *= math.factorial(p[i])/math.factorial(remaining[i])
        value = factor*coefficient
        if sum(remaining) <= 4:
            output[INDEX[remaining]] += value
        else:
            tail += float(np.linalg.norm(value))
    return TaylorTensor(output, tail)


def base_field(derivatives, radius, order=0):
    sample = derivatives[order]
    shape = sample.shape[order:]
    if order:
        shape = (4, *shape)
    coefficients = np.zeros((len(POWERS), *shape), dtype=sample.dtype)
    for p in POWERS:
        degree = sum(p)
        if degree+order not in derivatives:
            continue
        indices = tuple(i for i in range(4) for _ in range(p[i]))
        value = derivatives[degree+order][indices] if indices else derivatives[degree+order]
        coefficients[INDEX[p]] = value*radius**degree/math.prod(math.factorial(a) for a in p)
    return TaylorTensor(coefficients)


def field_models(case, radius):
    if not np.isfinite(radius) or radius <= 0:
        raise ValueError("Positive finite coordinate radius required")
    prepared, point, jets, full, ordinary, spinor, coefficients = case
    ed = {0: np.eye(4), 1: np.zeros((4, 4, 4)), 2: point["coframe_second"], 3: jets["e3"], 4: full["e4"]}
    pd = {0: prepared["data"]["psi"], 1: point["psi_first"], 2: jets["p2"], 3: jets["p3"], 4: full["p4"]}
    ld = {0: point["multiplier"], 1: point["multiplier_first"], 2: jets["l2"], 3: full["l3"]}
    result = {"e": base_field(ed, radius), "de": base_field(ed, radius, 1),
              "psi": base_field(pd, radius), "dp": base_field(pd, radius, 1), "lam": base_field(ld, radius)}
    old_e, old_p = 16*len(common.E5), 40*len(common.E5)
    new_e, new_p = 16*len(control.parent.E6), 16*len(control.parent.E6)+24*len(control.parent.P5)
    complex_blocks = lambda values: np.array([general.prior.joint.prior.complexify(v, (3, 4)) for v in values.reshape(-1, 24)])
    e_terms = [(common.E5, ordinary[:old_e].reshape(-1, 4, 4)),
               (control.parent.E6, coefficients[:new_e].reshape(-1, 4, 4))]
    p_terms = [(common.E5, complex_blocks(ordinary[old_e:old_p])), (common.L4, complex_blocks(spinor)),
               (control.parent.P5, complex_blocks(coefficients[new_e:new_p]))]
    l_terms = [(common.L4, ordinary[old_p:].reshape(-1, 4, 4)),
               (control.parent.P5, coefficients[new_p:].reshape(-1, 4, 4))]
    for key, derivative_key, terms, amplitude in (("e", "de", e_terms, common.RADIUS**2),
                                                ("psi", "dp", p_terms, common.RADIUS),
                                                ("lam", None, l_terms, common.RADIUS)):
        for powers, values in terms:
            result[key] = result[key]+monomial_terms(powers, values, amplitude, radius)
            if derivative_key:
                result[derivative_key] = result[derivative_key]+stack([
                    monomial_terms(powers, values, amplitude, radius, (r,)) for r in range(4)])
    return result


def determinant(e):
    result = tensor(0.)
    for permutation in itertools.permutations(range(4)):
        inversions = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i+1, 4))
        term = tensor(float((-1)**inversions))
        for r in range(4):
            term = contract(",->", term, e[r, permutation[r]])
        result = result+term
    return result


def constitutive_model(prepared, fields):
    e, de, psi, dp, lam = (fields[k] for k in ("e", "de", "psi", "dp", "lam"))
    inverse, e_ratio = matrix_inverse(e)
    if np.linalg.det(e.center) <= 0:
        raise ValueError("Positive coframe orientation required for the volume polynomial")
    volume = determinant(e)
    eta, forms, selector = general.prolong.ETA, prepared["component_forms"], general.prolong.Q
    hessian = contract(",ma,nb,pqmnab->pq", volume, inverse, inverse, prepared["curvature_hessian"]).scale(.5)
    hinverse, h_ratio = matrix_inverse(hessian)
    components = contract("ui,pamij,uj->pam", psi.conjugate(), forms, psi).real()
    source = contract(",ma,pam->p", volume, inverse, components)
    response = contract("ui,pamij,uj->amp", psi.conjugate(), forms, contract("uv,vj->uj", selector, psi)).real().scale(-1)
    k = contract("pq,q->p", hinverse, -source+contract("amp,am->p", response, lam))
    metric_inverse = contract("ma,ab,nb->mn", inverse, eta, inverse)
    metric_first = contract("ram,ab,bv->rmv", de, eta, e)+contract("am,ab,rbv->rmv", e, eta, de)
    lower = (metric_first.transpose(1, 0, 2)+metric_first.transpose(1, 2, 0)-metric_first).scale(.5)
    gamma = contract("as,sbc->abc", metric_inverse, lower)
    lc = contract("ab,mbv,vc->mac", eta, contract("ap,pmq->maq", e, gamma)-de, inverse)
    omega = lc+contract("p,pmab->mab", k, general.cartan.OMEGA_BASIS)
    spin = contract("mab,aij,bjk->mik", omega, general.cartan.GAMMA, general.cartan.GAMMA).scale(-.25)
    covariant = dp+contract("mij,uj->mui", spin, psi)
    residual = contract("ui,uv,mvj,aij->am", psi.conjugate(), selector, covariant, general.prolong.WEIGHTS).imag()-e
    return residual, {"coframe_neumann_ratio": e_ratio, "hessian_neumann_ratio": h_ratio}


def evaluate():
    fingerprints = input_fingerprints()
    case = control.load_case()

    def run(radius):
        fields = field_models(case, radius)
        model, ratios = constitutive_model(case[0], fields)
        norms = model.coefficient_norms()
        levels = [float(sum(norms[DEGREES == k])) for k in range(5)]
        checks = []
        for y in (np.eye(4)[0], np.array([.5, -.5, .5, -.5]), np.array([.2, -.3, .1, .4])):
            actual_fields, _ = control.fields_and_higher(case, radius*y)
            actual = general.equations(case[0], actual_fields)["constraint"]
            checks.append({"direction": y.tolist(), "actual_norm": float(np.linalg.norm(actual)),
                "polynomial_norm": float(np.linalg.norm(model.evaluate(y))),
                "tail_discrepancy": float(np.linalg.norm(actual-model.evaluate(y)))})
        return {"radius": radius, "coefficient_level_bounds": levels, "tail_bound": model.tail,
            "whole_cube_upper_estimate": sum(levels)+model.tail, **ratios,
            "coefficients": model.coefficients.tolist(), "sample_checks_not_the_proof": checks}

    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(run, [common.RADIUS, common.RADIUS/2]))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Constitutive Taylor inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "normalized Taylor polynomial and whole-cube tail for 16 constitutive equations only",
        "retained_degree": 4, "coefficient_count": len(POWERS), "reports": reports,
        "no_coefficients_fitted_or_zeroed": True, "not_all_80_equations": True,
        "not_outward_rounded_or_interval_certified": True,
        "not_exact_low_order_vanishing_or_regional_solution": True, "main_TeX_PDF_changed": False}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: [{a: b for a, b in r.items() if a != "coefficients"} for r in v] if k == "reports" else v
                      for k, v in result.items() if k != "input_sha256"}, indent=2))
