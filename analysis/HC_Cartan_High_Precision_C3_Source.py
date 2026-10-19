"""Fresh nonlinear C3 sources from independent high-precision matrix series."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import mpmath
import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "high_precision_source_parent", Path(__file__).with_name("HC_Cartan_Origin_Rounding_Attribution.py"))
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
cubic, common = prior.prior, prior.common
GENERAL = cubic.prior.prior.general
POWERS = tuple(common.exponents(3))
ORDER = 3


def input_fingerprints():
    result = prior.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cartan_Origin_Rounding_Attribution.json"):
        data = Path(__file__).with_name(name).read_bytes()
        if name.endswith(".py"):
            data = data.replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def number(ctx, value):
    if isinstance(value, Fraction):
        return ctx.mpf(value.numerator)/value.denominator
    if isinstance(value, tuple) and len(value) == 2:
        return ctx.mpc(number(ctx, value[0]), number(ctx, value[1]))
    if hasattr(value, "_mpf_"):
        return ctx.mpf(value)
    if hasattr(value, "_mpc_"):
        return ctx.mpc(value)
    value = complex(value)
    real, imag = Fraction.from_float(value.real), Fraction.from_float(value.imag)
    real_value = ctx.mpf(real.numerator)/real.denominator
    return ctx.mpc(real_value, ctx.mpf(imag.numerator)/imag.denominator) if imag else real_value


def matrix(ctx, value):
    value = np.asarray(value, dtype=object)
    if value.ndim != 2:
        raise ValueError("Two-dimensional matrix input required")
    return ctx.matrix([[number(ctx, v) for v in row] for row in value])


def reshape_matrix(ctx, value, rows, columns):
    flat = list(value)
    if rows*columns != len(flat):
        raise ValueError("Matrix reshape must preserve size")
    return ctx.matrix([flat[i*columns:(i+1)*columns] for i in range(rows)])


class Series:
    """Degree-three matrix polynomial in a real formal parameter, without tails."""
    def __init__(self, ctx, coefficients):
        self.ctx, self.coefficients = ctx, tuple(coefficients)
        if len(self.coefficients) != ORDER+1:
            raise ValueError("Four matrix coefficients required")
        shape = (self.coefficients[0].rows, self.coefficients[0].cols)
        if any((v.rows, v.cols) != shape for v in self.coefficients):
            raise ValueError("Matching matrix coefficient shapes required")
        self.active = tuple(any(v != 0 for v in a) for a in self.coefficients)

    @classmethod
    def constant(cls, ctx, value):
        return cls(ctx, [value]+[ctx.zeros(value.rows, value.cols) for _ in range(ORDER)])

    def __add__(self, other):
        return Series(self.ctx, [a+b for a, b in zip(self.coefficients, other.coefficients)])

    def __sub__(self, other):
        return self+other.scale(-1)

    def scale(self, value):
        return Series(self.ctx, [a*value for a in self.coefficients])

    def __matmul__(self, other):
        out = []
        for n in range(ORDER+1):
            value = self.ctx.zeros(self.coefficients[0].rows, other.coefficients[0].cols)
            for j in range(n+1):
                if self.active[j] and other.active[n-j]:
                    value += self.coefficients[j]*other.coefficients[n-j]
            out.append(value)
        return Series(self.ctx, out)

    def transpose(self, conjugate=False):
        return Series(self.ctx, [a.H if conjugate else a.T for a in self.coefficients])

    def reshape(self, rows, columns):
        if rows*columns != self.coefficients[0].rows*self.coefficients[0].cols:
            raise ValueError("Matrix series reshape must preserve size")
        return Series(self.ctx, [reshape_matrix(self.ctx, a, rows, columns) for a in self.coefficients])

    def times_scalar(self, scalar):
        if (scalar.coefficients[0].rows, scalar.coefficients[0].cols) != (1, 1):
            raise ValueError("Scalar matrix series required")
        result = []
        for n in range(ORDER+1):
            value = self.ctx.zeros(self.coefficients[0].rows, self.coefficients[0].cols)
            for j in range(n+1):
                if self.active[j] and scalar.active[n-j]:
                    value += self.coefficients[j]*scalar.coefficients[n-j][0, 0]
            result.append(value)
        return Series(self.ctx, result)

    def inverse(self):
        first = self.coefficients[0]**-1
        result = [first]
        for n in range(1, ORDER+1):
            value = self.ctx.zeros(first.rows, first.cols)
            for j in range(1, n+1):
                if self.active[j]:
                    value += self.coefficients[j]*result[n-j]
            result.append(-first*value)
        return Series(self.ctx, result)

    def determinant(self):
        inverse = self.inverse()
        first = self.ctx.det(self.coefficients[0])
        logs = []
        for n in range(ORDER):
            value = self.ctx.zeros(self.coefficients[0].rows)
            for j in range(n+1):
                value += inverse.coefficients[j]*self.coefficients[n-j+1]*(n-j+1)
            logs.append(sum(value[i, i] for i in range(value.rows)))
        values = [first]
        for n in range(1, ORDER+1):
            values.append(sum(values[j]*logs[n-1-j] for j in range(n))/n)
        return Series(self.ctx, [self.ctx.matrix([[v]]) for v in values])


def directional(ctx, tensors, y):
    out = []
    for n, tensor in enumerate(tensors):
        if n == 0:
            out.append(matrix(ctx, tensor))
            continue
        shape = np.asarray(tensor).shape[n:]
        value = ctx.zeros(*shape)
        for indices in itertools.product(range(4), repeat=n):
            weight = math.prod(y[i] for i in indices)/math.factorial(n)
            if weight:
                value += matrix(ctx, tensor[indices])*weight
        out.append(value)
    return Series(ctx, out)


def highest_coefficient(ctx, unique, y, order, derivative=None):
    tuples = tuple(itertools.combinations_with_replacement(range(4), order))
    lookup = {p: i for i, p in enumerate(tuples)}
    remaining = order-(derivative is not None)
    value = ctx.zeros(*np.asarray(unique[0]).shape)
    for indices in itertools.product(range(4), repeat=remaining):
        weight = math.prod(y[i] for i in indices)/math.factorial(remaining)
        if weight:
            full = tuple(sorted(indices if derivative is None else (derivative, *indices)))
            value += matrix(ctx, unique[lookup[full]])*weight
    return value


class Evaluator:
    def __init__(self, ctx, bundle):
        self.ctx, self.bundle = ctx, bundle
        self.eta, self.q = matrix(ctx, GENERAL.prolong.ETA), matrix(ctx, GENERAL.prolong.Q)
        self.forms = [[matrix(ctx, bundle["forms"][l, a]) for a in range(4)] for l in range(6)]
        self.weights = [matrix(ctx, a) for a in GENERAL.prolong.WEIGHTS]
        self.flat_inverse = matrix(ctx, bundle["flat_inverse"])
        self.basis = matrix(ctx, GENERAL.cartan.OMEGA_BASIS.reshape(24, 64).T)
        gamma = [matrix(ctx, g) for g in GENERAL.cartan.GAMMA]
        self.spin_map = ctx.zeros(16, 16)
        for a, b in itertools.product(range(4), repeat=2):
            product = -gamma[a]*gamma[b]/4
            for i, j in itertools.product(range(4), repeat=2):
                self.spin_map[4*i+j, 4*a+b] = product[i, j]

    def constant(self, value):
        return Series.constant(self.ctx, value)

    def fields(self, direction, mode):
        ctx, d = self.ctx, self.bundle
        y = [number(ctx, a) for a in direction]
        e = directional(ctx, [np.eye(4), np.zeros((4, 4, 4)), d["e2"], d["e3"]], y)
        psi = directional(ctx, [d["psi"], d["p1"], d["p2"], d["p3"]], y)
        lam = directional(ctx, [d["l0"], d["l1"], d["l2"], np.zeros((4, 4, 4, 4, 4))], y)
        de, dp = [], []
        for mu in range(4):
            de.append(directional(ctx, [np.zeros((4, 4)), d["e2"][mu], d["e3"][mu], np.zeros((4, 4, 4, 4, 4))], y))
            dp.append(directional(ctx, [d["p1"][mu], d["p2"][mu], d["p3"][mu], np.zeros((4, 4, 4, 3, 4))], y))
        if mode not in ("lower", "highest", "full"):
            raise ValueError("Unknown source series mode")
        if mode == "highest":
            e, psi = self.constant(ctx.eye(4)), self.constant(matrix(ctx, d["psi"]))
            lam = self.constant(matrix(ctx, d["l0"]))
            de = [self.constant(ctx.zeros(4)) for _ in range(4)]
            dp = [self.constant(ctx.zeros(3, 4)) for _ in range(4)]
        if mode != "lower":
            for mu in range(4):
                de[mu] = Series(ctx, [*de[mu].coefficients[:3], highest_coefficient(ctx, d["e4"], y, 4, mu)])
                if mode == "full":
                    dp[mu] = Series(ctx, [*dp[mu].coefficients[:3], highest_coefficient(ctx, d["parametric_p4"], y, 4, mu)])
            lam = Series(ctx, [*lam.coefficients[:3], highest_coefficient(ctx, d["l3"], y, 3)])
        return e, de, psi, dp, lam

    def geometry(self, e, de):
        inverse = e.inverse()
        metric_inverse = inverse @ self.constant(self.eta) @ inverse.transpose()
        metric_first = [v.transpose() @ self.constant(self.eta) @ e+e.transpose() @ self.constant(self.eta) @ v for v in de]
        lc = []
        for mu in range(4):
            lower = []
            for n in range(4):
                lower.append(self.ctx.matrix([[ (metric_first[mu].coefficients[n][s, v]
                    +metric_first[v].coefficients[n][s, mu]-metric_first[s].coefficients[n][mu, v])/2
                    for v in range(4)] for s in range(4)]))
            gamma = metric_inverse @ Series(self.ctx, lower)
            lc.append(self.constant(self.eta) @ (e @ gamma-de[mu]) @ inverse)
        return lc

    def source_bilinear(self, psi, selector):
        density = psi.transpose(True) @ self.constant(selector) @ psi
        coefficients = []
        for value in density.coefficients:
            coefficients.append(self.ctx.matrix([[self.ctx.re(sum(value[i, j]*self.forms[l][a][i, j]
                for i, j in itertools.product(range(4), repeat=2))) for l in range(6)] for a in range(4)]))
        return Series(self.ctx, coefficients)

    def constraint(self, direction, mode):
        e, de, psi, dp, lam = self.fields(direction, mode)
        volume = e.determinant()
        if self.ctx.re(volume.coefficients[0][0, 0]) <= 0:
            raise ValueError("Positive origin volume required")
        direct = self.source_bilinear(psi, self.ctx.eye(3))
        weighted = self.source_bilinear(psi, self.q)
        channel = (lam @ e.transpose()).transpose() @ weighted
        effective = direct+channel.times_scalar(volume.inverse())
        body = self.constant(self.flat_inverse) @ effective.reshape(24, 1)
        k = (e.transpose() @ body.reshape(4, 6)).reshape(24, 1).scale(-1)
        omega = self.constant(self.basis) @ k
        lc = self.geometry(e, de)
        result = [self.ctx.zeros(4) for _ in range(4)]
        for mu in range(4):
            local = Series(self.ctx, [reshape_matrix(self.ctx, list(v)[16*mu:16*(mu+1)], 4, 4) for v in omega.coefficients])+lc[mu]
            spin = (self.constant(self.spin_map) @ local.reshape(16, 1)).reshape(4, 4)
            derivative = dp[mu]+psi @ spin.transpose()
            density = psi.transpose(True) @ self.constant(self.q) @ derivative
            for n, value in enumerate(density.coefficients):
                for a in range(4):
                    result[n][a, mu] = self.ctx.im(sum(value[i, j]*self.weights[a][i, j]
                        for i, j in itertools.product(range(4), repeat=2)))-e.coefficients[n][a, mu]
        return result


def reconstruction():
    v = sp.Matrix([[math.prod(y[i]**p[i] for i in range(4)) for p in POWERS] for y in POWERS])
    inverse = v.inv()
    if inverse*v != sp.eye(20):
        raise ValueError("Exact directional coefficient reconstruction failed")
    return [[Fraction(str(value)) for value in row] for row in inverse.tolist()]


def spinor_image_split(ctx, vector, groups):
    if len(vector) != 320 or sorted(4*t+mu for rows in groups for t, mu in rows) != list(range(80)):
        raise ValueError("Complete unique-triple/fourth-jet partition required")
    image = [ctx.mpf(0)]*320
    for rows in groups:
        for a in range(4):
            mean = ctx.fsum(vector[16*t+4*a+mu] for t, mu in rows)/len(rows)
            for t, mu in rows:
                image[16*t+4*a+mu] = mean
    return image, [v-p for v, p in zip(vector, image)]


def load_bundle():
    report = json.loads(Path(__file__).with_name("HC_Cartan_Origin_Rounding_Attribution.json").read_text(encoding="utf-8"))
    if report["input_sha256"] != prior.input_fingerprints():
        raise ValueError("Origin attribution report has stale inputs")
    data = prior.load_inputs()
    if sp.Matrix([[sp.Rational(str(v)) for v in row] for row in data["readout"]]).rank() != 4:
        raise ValueError("Surjective four-output frozen spinor readout required")
    cauchy = common.lower.prior.previous.first.prior
    prepared, point, _, _, _, lift = GENERAL.domain.load_data()
    highest = np.asarray(lift["fitted_highest"])
    jets = cauchy.joint.regular.unpack(np.asarray(lift["fitted_coordinates"]))
    centered = cubic.prior.prior
    inverse, _ = centered.frame.factorization_certificate(prepared["curvature_hessian"])
    forms, _ = centered.prior.source_support_certificate(prepared["component_forms"])
    def complex_blocks(blocks):
        result = []
        for block in blocks:
            result.append(np.array([complex(0)]*12, object).reshape(3, 4))
            for i in range(12):
                # Keep rational real/imaginary parts separate until context conversion.
                result[-1].flat[i] = (block[i], block[12+i])
        return result
    parametric = complex_blocks(data["parametric"])
    return {"psi": prepared["data"]["psi"], "p1": point["psi_first"], "p2": jets["p2"], "p3": jets["p3"],
        "e2": point["coframe_second"], "e3": jets["e3"], "e4": highest[:560].reshape(35, 4, 4),
        "l0": point["multiplier"], "l1": point["multiplier_first"], "l2": jets["l2"], "l3": highest[560:880].reshape(20, 4, 4),
        "forms": forms, "flat_inverse": inverse, "parametric_p4": parametric, "readout_data": data}


def precision_evaluation(digits, bundle, inverse):
    ctx = mpmath.mp.clone()
    ctx.dps = digits
    evaluator = Evaluator(ctx, bundle)
    values = {mode: [evaluator.constraint(y, mode)[3] for y in POWERS] for mode in ("lower", "highest")}
    triples, data = bundle["readout_data"]["triples"], bundle["readout_data"]
    def recover(samples):
        coefficients = [sum((samples[j]*number(ctx, row[j]) for j in range(20)), ctx.zeros(4)) for row in inverse]
        lookup = {p: i for i, p in enumerate(POWERS)}
        return [coefficients[lookup[tuple(triple.count(i) for i in range(4))]]*
            math.prod(math.factorial(triple.count(i)) for i in range(4)) for triple in triples]
    s0, s1 = (recover(values[k]) for k in ("lower", "highest"))
    source = [a+b for left, right in zip(s0, s1) for a, b in zip(left, right)]
    def principal(blocks):
        a = [[number(ctx, v) for v in row] for row in data["readout"]]
        p = [[number(ctx, v) for v in block] for block in blocks]
        return cubic.stable.c3_entries([[ctx.fsum(x*y for x, y in zip(row, block)) for row in a] for block in p], data["quads"], triples)
    base, exact, rounded = (principal(data[k]) for k in ("baseline", "parametric", "rounded"))
    residual = [s+p for s, p in zip(source, exact)]
    groups = common.lower.prior.previous.first.prior.joint.third.diagnostic.groups()
    image, compatibility = spinor_image_split(ctx, residual, groups)
    frozen = [number(ctx, v) for v in data["source"]]
    norm = lambda vector: ctx.sqrt(ctx.fsum(abs(v)**2 for v in vector))
    held = (1, -1, 2, 0)
    full = evaluator.constraint(held, "full")[3]
    predicted = evaluator.constraint(held, "lower")[3]+evaluator.constraint(held, "highest")[3]
    # Full directional principal contribution from the actual fourth jet.
    for mu in range(4):
        dp = highest_coefficient(ctx, bundle["parametric_p4"], [number(ctx, y) for y in held], 4, mu)
        density = matrix(ctx, bundle["psi"]).H*evaluator.q*dp
        for a in range(4):
            predicted[a, mu] += ctx.im(sum(density[i, j]*evaluator.weights[a][i, j] for i, j in itertools.product(range(4), repeat=2)))
    def encode(values):
        if any(ctx.im(v) != 0 for v in values):
            raise ValueError("Real source coefficient vectors required")
        return [ctx.nstr(ctx.re(v), digits-5) for v in values]
    print(f"Fresh nonlinear C3 evaluated at {digits} digits: {ctx.nstr(norm(residual), 16)}", flush=True)
    return {"digits": digits, "fresh_C3_norm": ctx.nstr(norm(residual), 24),
        "source0_norm": ctx.nstr(norm([v for a in s0 for v in a]), 24),
        "source1_norm": ctx.nstr(norm([v for a in s1 for v in a]), 24),
        "fresh_minus_frozen_source_norm": ctx.nstr(norm([a-b for a, b in zip(source, frozen)]), 24),
        "parametric_minus_baseline_C3_norm": ctx.nstr(norm([a-b for a, b in zip(exact, base)]), 24),
        "fresh_sources_with_rounded_inputs_C3_norm": ctx.nstr(norm([s+p for s, p in zip(source, rounded)]), 24),
        "unrestricted_spinor4_image_norm": ctx.nstr(norm(image), 24),
        "fixed_other_data_compatibility_norm": ctx.nstr(norm(compatibility), 24),
        "orthogonal_image_split_squared_norm_discrepancy": ctx.nstr(abs(norm(residual)**2-norm(image)**2-norm(compatibility)**2), 24),
        "held_out_full_series_split_discrepancy": ctx.nstr(norm(list(full-predicted)), 24),
        "source0_vector": encode([v for a in s0 for v in a]), "source1_vector": encode([v for a in s1 for v in a]),
        "C3_vector": encode(residual), "constant_constraint_norm": ctx.nstr(norm(list(evaluator.constraint((1, 0, 0, 0), "lower")[0])), 24)}


def evaluate():
    fingerprints, bundle, inverse = input_fingerprints(), load_bundle(), reconstruction()
    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(lambda digits: precision_evaluation(digits, bundle, inverse), (40, 80)))
    ctx = mpmath.mp.clone()
    ctx.dps = 80
    discrepancies = {key: ctx.nstr(ctx.sqrt(ctx.fsum((ctx.mpf(a)-ctx.mpf(b))**2 for a, b in zip(reports[0][key], reports[1][key]))), 24)
        for key in ("source0_vector", "source1_vector", "C3_vector")}
    if fingerprints != input_fingerprints():
        raise RuntimeError("High precision source inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "neutral commuting-spinor odd-cross Cartan comparison only",
        "reports": reports, "cross_precision_vector_discrepancies": discrepancies,
        "nonlinear_sources_recomputed_before_rounding_not_promoted_from_saved_values": True,
        "independent_matrix_series_not_parent_third_derivative_formula": True,
        "exact_directional_reconstruction_checked": True, "formal_series_not_finite_difference_steps": True,
        "fitted_input_coordinates_still_interpreted_as_stored_binary64": True,
        "exact_kernel_coordinates_used_before_high_precision_arithmetic": True,
        "unrestricted_spinor4_image_dimension": 140, "fixed_other_C3_compatibility_dimension": 180,
        "spinor_image_split_is_diagnostic_not_a_release_of_kernel_constraints": True,
        "other_794_origin_equations_not_recomputed_at_high_precision": True,
        "no_new_fit_interval_certificate_regional_solution_or_native_identification": True,
        "parent_polynomials_reports_and_main_TeX_PDF_unchanged": True}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({**{k: v for k, v in result.items() if k not in ("input_sha256", "reports")},
        "reports": [{k: v for k, v in r.items() if not k.endswith("_vector")} for r in result["reports"]]}, indent=2))
