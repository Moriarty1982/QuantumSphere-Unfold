"""Purely spatial C3 compatibility and an exact frozen-coefficient scalar check."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "spatial_trace_quadratic", Path(__file__).with_name("HC_Cartan_Complete_Quadratic_Gate.py"))
quadratic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quadratic)
prior = quadratic.prior


def input_fingerprints():
    result = quadratic.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def spatial_rows():
    return [794+16*t+4*a+mu for t, triple in enumerate(prior.joint.third.TRIPLES)
            if 0 not in triple for a in range(4) for mu in (1, 2, 3)]


def rational(value):
    value = complex(value)
    return sp.Rational(value.real)+sp.I*sp.Rational(value.imag)


def matrix(values):
    values = np.asarray(values)
    return sp.Matrix(values.shape[0], values.shape[1], [rational(v) for v in values.flat])


def real(value):
    return sp.expand(value).as_real_imag()[0]


def imag(value):
    return sp.expand(value).as_real_imag()[1]


def bilinear(left, form, right):
    """Sum over the internal index, with sparse spin-form contraction."""
    return sp.expand(sum(left[u, i].conjugate()*form[i, j]*right[u, j]
                         for i in range(4) for j in range(4) if form[i, j] != 0
                         for u in range(left.rows)))


def linear_connection(derivatives, mu):
    flat = sp.Matrix([rational(v) for v in np.asarray(derivatives).flat])
    image = matrix(prior.regular.LC_LINEAR).T*flat
    return sp.Matrix(4, 4, list(image[16*mu:16*(mu+1), 0]))


def exact_repeated_spatial_component(prepared, point, coordinates, highest, *,
                                     axis=3, mu=2, a=0, rebuild_spin_maps=False):
    """Exact rational evaluation for fixed prepared constants and binary jet values.

    Optionally rebuild the spin-dependent source/response maps from rational
    psi and forms, rather than freeze their precomputed floating-point values.
    """
    if axis not in (1, 2, 3) or mu not in (1, 2, 3) or a not in range(4):
        raise ValueError("A spatial repeated derivative, spatial component and valid frame row required")
    third = prior.joint.third
    scalar, cartan = third.scalar, third.cartan
    jets = prior.regular.unpack(coordinates)
    psi = matrix(prepared["data"]["psi"])
    p1 = matrix(point["psi_first"][axis])
    p2 = matrix(jets["p2"][axis, axis])
    p3 = matrix(jets["p3"][axis, axis, axis])
    selector = matrix(scalar.Q)
    forms = [matrix(v) for v in prepared["source_forms"]]
    component = [[[matrix(prepared["component_forms"][p, b, n]) for n in range(4)]
                  for b in range(4)] for p in range(24)]
    source = sp.Matrix([rational(v) for v in prepared["source"]])
    response = matrix(prepared["response"])
    inverse = matrix(prepared["inverse_hessian"])
    if matrix(prepared["hessian"])*inverse != sp.eye(24):
        raise ValueError("Frozen Cartan inverse is not exact")
    source_components = [[[rational(prepared["source_components"][p, b, n])
                           for n in range(4)] for b in range(4)] for p in range(24)]
    if rebuild_spin_maps:
        weights = [matrix(v) for v in scalar.odd.readouts.dirac.WEIGHTS]
        gammas = [matrix(v) for v in cartan.GAMMA]
        for p in range(24):
            for n in range(4):
                omega = matrix(cartan.OMEGA_BASIS[p, n])
                spin = -sum((omega[b, c]*gammas[b]*gammas[c]
                             for b in range(4) for c in range(4)), sp.zeros(4, 4))/4
                for b in range(4):
                    term = weights[b]*spin
                    exact_form = sp.I*(term-term.conjugate().T)/2
                    if exact_form != component[p][b][n]:
                        raise ValueError("Prepared component forms are not exact Clifford forms")
                    source_components[p][b][n] = real(bilinear(psi, exact_form, psi))
                    response[4*b+n, p] = -real(bilinear(selector*psi, exact_form, psi))
            if forms[p] != sum((component[p][b][b] for b in range(4)), sp.zeros(4, 4)):
                raise ValueError("Source form is not the exact component trace")
            source[p] = sum(source_components[p][b][b] for b in range(4))
    lam0 = sp.Matrix([rational(v) for v in point["multiplier"].flat])
    lam1 = sp.Matrix([rational(v) for v in point["multiplier_first"][axis].flat])
    lam2 = sp.Matrix([rational(v) for v in jets["l2"][axis, axis].flat])
    triple = third.TRIPLES.index((axis, axis, axis))
    lam3 = sp.Matrix([rational(v) for v in highest[560:880].reshape(20, 4, 4)[triple].flat])
    e2 = matrix(point["coframe_second"][axis, axis])
    e3 = matrix(jets["e3"][axis, axis, axis])

    s1 = sp.Matrix([2*real(bilinear(psi, f, p1)) for f in forms])
    r1 = sp.zeros(16, 24)
    r2 = sp.zeros(16, 24)
    r3 = sp.zeros(16, 24)
    component_first = []
    for p in range(24):
        first = sp.zeros(4, 4)
        for b in range(4):
            for n in range(4):
                f = component[p][b][n]
                first[b, n] = 2*real(bilinear(psi, f, p1))
                r1[4*b+n, p] = -2*real(bilinear(selector*psi, f, p1))
                r2[4*b+n, p] = -2*real(bilinear(selector*psi, f, p2)
                                                    +bilinear(selector*p1, f, p1))
                r3[4*b+n, p] = -2*real(bilinear(selector*psi, f, p3)
                                                    +3*bilinear(selector*p1, f, p2))
        component_first.append(first)
    s2 = sp.Matrix([2*real(bilinear(psi, f, p2)+bilinear(p1, f, p1))
        +sp.trace(e2)*source[p]-sum(e2[n, b]*source_components[p][b][n]
                                   for b in range(4) for n in range(4))
        for p, f in enumerate(forms)])
    s3 = sp.Matrix([2*real(bilinear(psi, f, p3)+3*bilinear(p1, f, p2))
        +sp.trace(e3)*source[p]-sum(e3[n, b]*source_components[p][b][n]
                                   for b in range(4) for n in range(4))
        +3*(sp.trace(e2)*s1[p]-sum(e2[n, b]*component_first[p][b, n]
                                   for b in range(4) for n in range(4)))
        for p, f in enumerate(forms)])

    def hessian_derivative(coframe):
        return sum((coframe[b, n]*matrix(prepared["hessian_first"][b, n])
                    for b in range(4) for n in range(4)), sp.zeros(24, 24))

    h2, h3 = hessian_derivative(e2), hessian_derivative(e3)
    k0 = inverse*(-source+response.T*lam0)
    k1 = inverse*(-s1+r1.T*lam0+response.T*lam1)
    k2 = inverse*(-s2+r2.T*lam0+2*r1.T*lam1+response.T*lam2-h2*k0)
    k3 = inverse*(-s3+r3.T*lam0+3*r2.T*lam1+3*r1.T*lam2
                  +response.T*lam3-h3*k0-3*h2*k1)

    eta = matrix(third.prolong.ETA)
    lower_e2 = point["coframe_second"]
    w1 = linear_connection(lower_e2[axis], mu)

    def g4(n):
        cross = matrix(lower_e2[axis, n])
        return 3*(e2.T*eta*cross+cross.T*eta*e2)

    lc3 = sp.Matrix(4, 4, lambda b, c: (g4(mu)[b, c]+g4(c)[b, mu]-g4(b)[mu, c])/2)
    lc3 -= 3*(e2.T*(w1+eta*matrix(lower_e2[axis, mu]))+w1*e2)
    e4 = highest[:560].reshape(35, 4, 4)
    fourth = np.array([e4[third.diagnostic.QUADS.index(tuple(sorted((axis, axis, axis, n))))]
                       for n in range(4)])
    lc3 += linear_connection(fourth, mu)
    omega_basis = [matrix(v[mu]) for v in cartan.OMEGA_BASIS]
    gammas = [matrix(v) for v in cartan.GAMMA]

    def spin(k, lc):
        omega = lc+sum((v*b for v, b in zip(k, omega_basis)), sp.zeros(4, 4))
        return -sum((omega[b, c]*gammas[b]*gammas[c]
                     for b in range(4) for c in range(4)), sp.zeros(4, 4))/4

    b0 = spin(k0, sp.zeros(4, 4))
    b1 = spin(k1, w1)
    b2 = spin(k2, linear_connection(jets["e3"][axis, axis], mu))
    b3 = spin(k3, lc3)
    quartet = third.diagnostic.QUADS.index(tuple(sorted((axis, axis, axis, mu))))
    packed = highest[880:].reshape(35, 24)[quartet]
    p4 = matrix((packed[:12]+1j*packed[12:]).reshape(3, 4))
    d0 = matrix(point["psi_first"][mu])+psi*b0.T
    d1 = matrix(jets["p2"][axis, mu])+psi*b1.T+p1*b0.T
    d2 = matrix(jets["p3"][axis, axis, mu])+psi*b2.T+2*p1*b1.T+p2*b0.T
    d3 = p4+psi*b3.T+3*p1*b2.T+3*p2*b1.T+p3*b0.T
    weight = matrix(scalar.odd.readouts.dirac.WEIGHTS[a])
    # bilinear uses the same right spin action as the readout pairing.
    def pair(left, right):
        transformed = selector*right*weight.T
        return sum(left[u, i].conjugate()*transformed[u, i] for u in range(3) for i in range(4))
    return imag(pair(p3, d0)+pair(psi, d3)+3*pair(p1, d2)+3*pair(p2, d1))-e3[a, mu]


def evaluate(*, services=None):
    services = prior._resolve_services(services)
    fingerprints = input_fingerprints()
    prepared, assembled, residual = quadratic.load_problem(services)
    before = json.loads(Path(__file__).with_name("HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
    _, point, _, _, saved = prior.source.neighborhood.load_data()
    reduction = prior.source.normal.build_reduction(prepared, point)
    changed = prior.source.normal.remaining.normal_point(point, reduction["sources"] @ np.array(before["source_values"]))
    coordinates, highest = np.array(before["starting_coordinates"]), np.array(before["starting_highest"])
    rows = spatial_rows()
    base = residual(np.zeros(96))
    original_c = np.array(saved["jet_coordinates"])
    original_h = np.concatenate((saved["connection_coordinates"], np.array(saved["fourth_spinor_real"]).reshape(-1)))
    original = prior.evaluate_fields(prepared, point, original_c, original_h,
                                     prior.joint.third.lc_cubic(prepared, point))["vector"]
    shifted = prior.evaluate_fields(prepared, changed, original_c, original_h,
                                    prior.joint.third.lc_cubic(prepared, changed))["vector"]
    exact = exact_repeated_spatial_component(prepared, changed, coordinates, highest)
    rebuilt = exact_repeated_spatial_component(
        prepared, changed, coordinates, highest, rebuild_spin_maps=True)
    numerator, denominator = exact.as_numer_denom()
    rebuilt_numerator, rebuilt_denominator = rebuilt.as_numer_denom()
    row = 794+16*prior.joint.third.TRIPLES.index((3, 3, 3))+2
    rng = np.random.default_rng(1910120)
    controls = [float(np.linalg.norm(residual(rng.normal(size=96)*scale,
                   rng.normal(size=1168)*scale)[rows]-base[rows])) for scale in (.03, .3, 1.)]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Spatial trace inputs changed")
    return {"scope": "Purely spatial C3 trace of the fixed-data finite comparison",
        "input_sha256": fingerprints, "spatial_row_count": len(rows), "spatial_rows": rows,
        "fixed_spatial_C3_norm": float(np.linalg.norm(base[rows])),
        "allowed_response_norm": float(np.linalg.norm(assembled.matrix[rows])),
        "normal_variation_controls": controls,
        "original_spatial_norm": float(np.linalg.norm(original[rows])),
        "source_only_spatial_norm": float(np.linalg.norm(shifted[rows])),
        "source_only_spatial_change": float(np.linalg.norm(shifted[rows]-original[rows])),
        "chosen_row": row, "chosen_indices": {"derivative": [3, 3, 3], "frame": 0, "component": 2},
        "chosen_float_value": float(base[row]), "chosen_exact_decimal": str(sp.N(exact, 45)),
        "chosen_exact_numerator": str(numerator), "chosen_exact_denominator": str(denominator),
        "exact_nonzero": bool(exact != 0), "exact_exceeds_15": bool(exact > 15),
        "float_exact_difference": float(abs(float(exact)-base[row])),
        "exact_scope": "Frozen prepared binary coefficients and saved binary jets, interpreted as exact rationals",
        "rebuilt_spin_maps_exact_decimal": str(sp.N(rebuilt, 45)),
        "rebuilt_spin_maps_numerator": str(rebuilt_numerator),
        "rebuilt_spin_maps_denominator": str(rebuilt_denominator),
        "rebuilt_spin_maps_exceeds_15": bool(rebuilt > 15),
        "rebuilt_minus_frozen_decimal": str(sp.N(rebuilt-exact, 20)),
        "rebuilt_scope": "Exact rational seed and jets; source/response rebuilt from verified Clifford forms",
        "not_unrounded_action_or_interval_certificate": True,
        "not_general_nonexistence_or_regional_evolution": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate(services=prior.create_container().services())
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in (
        "input_sha256", "spatial_rows", "chosen_exact_numerator", "chosen_exact_denominator",
        "rebuilt_spin_maps_numerator", "rebuilt_spin_maps_denominator")}))


if __name__ == "__main__":
    main()
