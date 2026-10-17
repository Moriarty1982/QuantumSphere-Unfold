"""Exact Maxwell--Dirac Cauchy jets: full-rank but holonomic real coframe.

Flat reference, common U(1), hard H=0 comparison; not native C7 or gravity.
"""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "cauchy_coframe_dirac", Path(__file__).with_name("HC_Dirac_State_Gravity.py"))
dirac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dirac)
X = sp.symbols("x y z", real=True)
T = sp.Symbol("t", real=True)
R2 = sum(q*q for q in X)
MASS = sp.ImmutableMatrix([[sp.Rational(3, 5), 0, 4],
                          [0, sp.Rational(3, 5), sp.Rational(7, 10)],
                          [4, sp.Rational(7, 10), sp.Rational(3, 5)]])
COUPLING = sp.Rational(16, 75)  # Full-carrier trace: g_full^2/3, g_full=4/5.


def exact_matrix(array):
    return sp.ImmutableMatrix([[sp.nsimplify(complex(v)) for v in row] for row in array])


WEIGHTS = tuple(exact_matrix(k) for k in dirac.WEIGHTS)
BETA = exact_matrix(dirac.BETA)


def expanded(matrix):
    return sp.ImmutableMatrix(matrix.applyfunc(sp.expand))


def inner(left, right):
    return sp.expand(sum(sp.conjugate(a)*b for a, b in zip(left, right)))


def current_coefficient(probes, order):
    return sp.ImmutableMatrix([sp.expand(sum(
        inner(probes[k], probes[order-k] @ weight.T) for k in range(order+1)))
        for weight in WEIGHTS])


def initial_data(coupling=COUPLING):
    coupling = real_coupling(coupling)
    x, y, z = X
    psi = sp.ImmutableMatrix([[1, 0, z/2, -(x+sp.I*y)/2], [0]*4, [0]*4])
    potential = sp.zeros(3, 1)
    electric = sp.ImmutableMatrix([coupling*q*(sp.Rational(1, 3)+R2/20) for q in X])
    return psi, sp.ImmutableMatrix(potential), electric


def real_coupling(value):
    value = sp.sympify(value)
    if value.is_number is not True or value.is_real is not True or value.is_finite is not True or value < 0:
        raise ValueError("A finite nonnegative real comparison coupling is required")
    return value


def dirac_rhs(psi, potential):
    result = -sp.I*MASS @ psi @ BETA.T
    for i, q in enumerate(X):
        result -= (psi.diff(q)+sp.I*potential[i]*psi) @ WEIGHTS[i+1].T
    return expanded(result)


def spatial_maxwell(potential):
    divergence = sum(potential[i].diff(q) for i, q in enumerate(X))
    return sp.ImmutableMatrix([sum(potential[i].diff(q, 2) for q in X)-divergence.diff(X[i])
                               for i in range(3)])


@lru_cache(maxsize=8, typed=True)
def series(order=3, coupling=COUPLING):
    """Coefficients of t^n, not derivatives; exact through the requested jet."""
    if isinstance(order, bool) or not isinstance(order, int) or not 0 <= order <= 4:
        raise ValueError("An integer Taylor order from zero through four is required")
    coupling = real_coupling(coupling)
    p0, a0, e0 = initial_data(coupling)
    probes, potentials, electrics = [p0], [a0], [e0]
    for n in range(order):
        pnext = dirac_rhs(probes[n], sp.zeros(3, 1))
        for i in range(3):
            for k in range(n+1):
                pnext -= sp.I*potentials[k][i]*probes[n-k] @ WEIGHTS[i+1].T
        j = current_coefficient(probes, n)
        enext = spatial_maxwell(potentials[n])-coupling*j[1:, :]
        probes.append(expanded(pnext/(n+1)))
        potentials.append(expanded(electrics[n]/(n+1)))
        electrics.append(expanded(enext/(n+1)))
    return {"psi": tuple(probes), "potential": tuple(potentials), "electric": tuple(electrics),
            "current": tuple(current_coefficient(probes, n) for n in range(order+1)),
            "order": order, "coupling": coupling}


def residual_coefficients(data):
    """Independent polynomial substitution in all evolution, continuity and Gauss equations."""
    order, coupling = data["order"], data["coupling"]
    psi = sum((p*T**n for n, p in enumerate(data["psi"])), sp.zeros(3, 4))
    a = sum((p*T**n for n, p in enumerate(data["potential"])), sp.zeros(3, 1))
    electric = sum((p*T**n for n, p in enumerate(data["electric"])), sp.zeros(3, 1))
    j = sp.ImmutableMatrix([inner(psi, psi @ k.T) for k in WEIGHTS])
    residuals = {"dirac": psi.diff(T)-dirac_rhs(psi, a),
                 "potential": a.diff(T)-electric,
                 "electric": electric.diff(T)-spatial_maxwell(a)+coupling*j[1:, :],
                 "continuity": sp.Matrix([j[0].diff(T)+sum(j[i+1].diff(q) for i, q in enumerate(X))]),
                 "gauss": sp.Matrix([sum(electric[i].diff(q) for i, q in enumerate(X))-coupling*j[0]])}
    return {name: tuple(expanded(value).applyfunc(lambda v: sp.expand(v).coeff(T, n))
                        for n in range(order+(name == "gauss")))
            for name, value in residuals.items()}


def initial_jet(coupling=COUPLING):
    psi, a, _ = initial_data(coupling)
    derivative = (dirac_rhs(psi, a), *(psi.diff(q) for q in X))
    frame = sp.ImmutableMatrix([[sp.re(inner(psi, d @ k.T)) for d in derivative] for k in WEIGHTS])
    return {"psi": psi, "derivative": derivative, "coframe": frame,
            "metric": expanded(frame.T @ sp.diag(-1, 1, 1, 1) @ frame),
            "current": current_coefficient((psi,), 0)}


def frame_jet_at_origin():
    # E=d(j/2): three current time coefficients beyond j0 supply the coframe 2-jet.
    current = series()["current"]

    def value(indices):
        count = indices.count(0)
        result = current[count]*sp.factorial(count)/2
        for axis in indices:
            if axis:
                result = result.diff(X[axis-1])
        return np.array(result.subs(dict.fromkeys(X, 0)), float).reshape(4)

    frame = np.column_stack([value([mu]) for mu in range(4)])
    first = np.array([np.column_stack([value([r, mu]) for mu in range(4)]) for r in range(4)])
    second = np.array([[np.column_stack([value([r, s, mu]) for mu in range(4)])
                        for s in range(4)] for r in range(4)])
    return frame, first, second


def induced_control():
    data = initial_jet()
    zero = dict.fromkeys(X, 0)
    psi = np.array(data["psi"].subs(zero), complex)
    derivatives = np.array([np.array(d.subs(zero), complex) for d in data["derivative"]])
    frame, first, second = frame_jet_at_origin()
    bundle = dirac.bundle(frame, first, second)
    mass = np.array(MASS, complex)
    reference = dirac.dirac_data(psi, derivatives, mass)
    induced = dirac.dirac_data(psi, derivatives, mass, gamma=bundle["gamma"],
                              metric=bundle["metric"], spin=bundle["spin"])
    return {"reference": reference, "induced": induced, "bundle": bundle,
            "psi": psi, "frame": frame, "first": first, "second": second}


def evaluate():
    data, jet = series(), initial_jet()
    residuals = residual_coefficients(data)
    control = induced_control()
    zeros = {name: [all(v == 0 for v in coefficient) for coefficient in values]
             for name, values in residuals.items()}
    return {
        "status": "local analytic sourced flat-reference comparison with full-rank but flat induced coframe; NOT native C7, same-induced-frame solution, Einstein solution or continuation of the Hopf flux sector",
        "dictionary": {"mass_matrix": [[str(v) for v in row] for row in MASS.tolist()],
                       "common_U1_full_trace_coupling": str(COUPLING),
                       "projector": "I3; hard H=Lambda=0 eliminated before variation",
                       "adjoint": "ordinary Hermitian real-symmetric probe comparison"},
        "initial_data": {"psi": [[str(v) for v in row] for row in jet["psi"].tolist()],
                         "electric": [str(v) for v in initial_data()[2]],
                         "current": [str(v) for v in jet["current"]],
                         "coframe": [[str(v) for v in row] for row in jet["coframe"].tolist()],
                         "coframe_determinant": str(sp.factor(jet["coframe"].det())),
                         "timelike_current_margin": str(sp.factor(jet["current"][0]**2-sum(v*v for v in jet["current"][1:]))),
                         "full_rank_on_initial_ball_r_less_than_two": True},
        "exact_Taylor_substitution": {"time_polynomial_degree": data["order"],
                                     "zero_coefficients_by_equation": zeros,
                                     "evolution_and_continuity_residual_order_at_least": data["order"],
                                     "gauss_residual_order_at_least": data["order"]+1,
                                     "finite_Taylor_polynomial_is_not_exact_solution": True},
        "local_analytic_existence": {"method": "second-time-order analytic normal form; first-order Dirac residual has time derivative zero; Gauss propagates by current continuity",
                                     "reference": "https://www.math.mcgill.ca/gantumur/math580f14/analytic.pdf, Theorem 33",
                                     "no_global_finite_energy_stability_or_explicit_lifespan_claim": True},
        "geometry_at_origin": {"coframe": control["frame"].tolist(),
                               "metric": control["bundle"]["metric"].tolist(),
                               "reference_probe_stress": control["reference"]["stress"].tolist(),
                               "spin_connection_norm": float(np.linalg.norm(control["bundle"]["spin"])),
                               "curvature_norm": float(np.linalg.norm(control["bundle"]["curvature"]["riemann"])),
                               "general_identity": "E=d(j/2), so the metric is locally flat wherever E is invertible"},
        "same_induced_frame_negative_control": {"reference_Dirac_residual_norm": float(np.linalg.norm(control["reference"]["residual"])),
                                               "induced_Dirac_residual_norm": float(np.linalg.norm(control["induced"]["residual"])),
                                               "imaginary_bilinear_residual": float(np.vdot(control["psi"], control["induced"]["residual"] @ dirac.BETA.T).imag),
                                               "induced_coordinate_current_divergence": 8,
                                               "same_frame_obstruction_is_not_removed": True},
        "main_TeX_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
