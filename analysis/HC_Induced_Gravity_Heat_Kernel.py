"""Regulated Dirac induced-gravity comparison; not a native HC metric derivation."""
import argparse
import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "induced_background", Path(__file__).with_name("HC_Background_Coframe_Origin.py"))
background = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(background)


def mass_spectrum(matrix):
    matrix = np.asarray(matrix, complex)
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] == 0
            or not np.isfinite(matrix).all()
            or not np.allclose(matrix, matrix.conj().T, atol=1e-12, rtol=0)):
        raise ValueError("A nonempty finite Hermitian mass matrix required")
    return np.linalg.eigvalsh(matrix)


def window(uv, ir):
    uv, ir = float(uv), float(ir)
    if not math.isfinite(uv) or not math.isfinite(ir) or not 0 <= ir < uv:
        raise ValueError("Finite cutoff scales UV > IR >= 0 required")
    return uv, ir


def proper_time_integral(mass, uv, ir=0.0, power=2, quadrature=False):
    """Integral s^(-power) exp(-mass^2 s) over [UV^-2, IR^-2]."""
    uv, ir = window(uv, ir)
    mass = float(mass)
    if not math.isfinite(mass) or isinstance(power, bool) or power not in (2, 3):
        raise ValueError("Finite real mass and power 2 or 3 required")
    with mp.workdps(35):
        u, v, q = mp.mpf(uv), mp.mpf(ir), mp.mpf(mass)**2
        a, b = 1/u**2, (1/v**2 if ir else mp.inf)
        if quadrature:
            # Map the unbounded proper-time interval to a finite interval.
            return float(mp.quad(lambda z: z**(power-2)*mp.exp(-q/z) if z else 0,
                                 [v**2, u**2]))
        if not q:
            return float((u**(2*power-2)-v**(2*power-2))/(power-1))
        return float(q**(power-1)*mp.gammainc(1-power, q*a, q*b))


def coefficients(matrix, uv, ir=0.0):
    """Gamma_E = integral sqrt(g) [rho - A R + ...], for complex Dirac fields."""
    uv, ir = window(uv, ir)
    masses = mass_spectrum(matrix)
    i = np.array([proper_time_integral(m, uv, ir, 2) for m in masses])
    j = np.array([proper_time_integral(m, uv, ir, 3) for m in masses])
    a = float(np.sum(i)/(96*np.pi**2))
    rho = float(np.sum(j)/(8*np.pi**2))
    if a <= 0 or not math.isfinite(a) or not math.isfinite(rho):
        raise ValueError("Positive representable induced curvature coefficient required")
    return {"masses": masses.tolist(), "I": i.tolist(), "J": j.tolist(),
            "UV": uv, "IR": ir, "A": a, "rho_vac": rho,
            "inverse_G": 16*np.pi*a, "kappa": 1/(2*a),
            "Lambda_cos_truncated": rho/(2*a),
            "R_vac_truncated": 2*rho/a,
            "Lambda_cos_over_UV_squared": rho/(2*a*uv**2)}


def heat_density(s, curvature, matrix):
    """Only the a0+a2 density, not the exact heat kernel on a general geometry."""
    s, curvature = float(s), float(curvature)
    if not math.isfinite(s) or s <= 0 or not math.isfinite(curvature):
        raise ValueError("Positive proper time and finite scalar curvature required")
    weights = np.exp(-s*mass_spectrum(matrix)**2)
    return float(np.sum(weights)*(4-curvature*s/3)/(4*np.pi*s)**2)


def action_density(curvature, matrix, uv, ir=0.0):
    """Independent quadrature of the truncated heat density times 1/(2s)."""
    uv, ir = window(uv, ir)
    curvature = float(curvature)
    masses = mass_spectrum(matrix)
    if not math.isfinite(curvature):
        raise ValueError("Finite scalar curvature required")
    with mp.workdps(35):
        r = mp.mpf(curvature)
        q = [mp.mpf(float(m))**2 for m in masses]

        def integrand(z):
            if not z:
                return mp.mpf(0)
            return sum(mp.exp(-m/z) for m in q)*(4*z-r/3)/(32*mp.pi**2)

        return float(mp.quad(integrand, [mp.mpf(ir)**2, mp.mpf(uv)**2]))


def sphere_heat(s, radius=1.0, tolerance=1e-14):
    """Exact S4 Dirac-square spectrum, with an integral bound on the discarded tail."""
    s, radius, tolerance = float(s), float(radius), float(tolerance)
    if (not all(math.isfinite(x) for x in (s, radius, tolerance))
            or s <= 0 or radius <= 0 or not 0 < tolerance < 1):
        raise ValueError("Positive proper time/radius and tolerance in (0,1) required")
    alpha = s/radius**2
    leading = 2/(3*alpha**2)
    cutoff = max(2, math.ceil(math.sqrt(max(3/2, -math.log(tolerance)+5)/alpha)))

    def tail(k):
        return 2/(3*alpha**2)*(alpha*k*k+1)*math.exp(-alpha*k*k)

    while tail(cutoff) > tolerance*leading:
        cutoff += 1
    value = 4/3*math.fsum((k**3-k)*math.exp(-alpha*k*k) for k in range(2, cutoff+1))
    volume, curvature = 8*np.pi**2*radius**4/3, 12/radius**2
    return {"heat_trace": value, "tail_bound": tail(cutoff), "cutoff_k": cutoff,
            "radius": radius, "s": s,
            "a2_per_scalar_curvature": ((4*np.pi*s)**2*value/volume-4)/(s*curvature),
            "a4_remainder": value-2/(3*alpha**2)+2/(3*alpha)}


def matching(induced, bare_a=0.0, bare_rho=0.0):
    """Local counterterms are independent inputs; cancellation is not a mechanism."""
    a, rho = induced["A"]+float(bare_a), induced["rho_vac"]+float(bare_rho)
    if not math.isfinite(a) or not math.isfinite(rho) or a <= 0:
        raise ValueError("A positive finite total Einstein coefficient required")
    return {"A_total": a, "rho_total": rho, "inverse_G": 16*np.pi*a,
            "kappa": 1/(2*a), "Lambda_cos": rho/(2*a)}


def _boson_data(squared_masses, xi):
    q = np.asarray(squared_masses)
    if q.ndim != 1 or np.any(q.imag != 0):
        raise ValueError("A real vector of scalar squared masses required")
    q = np.asarray(q.real, float)
    couplings = np.asarray(xi)
    if np.any(couplings.imag != 0):
        raise ValueError("Real scalar curvature couplings required")
    couplings = np.broadcast_to(np.asarray(couplings.real, float), q.shape)
    if not np.isfinite(q).all() or np.any(q < 0) or not np.isfinite(couplings).all():
        raise ValueError("Finite nonnegative scalar squared masses and finite xi required")
    return q, couplings


def graded_heat_coefficients(s, matrix, scalar_squared_masses=(), xi=0.0):
    """Signed heat coefficients W0-s R B2; ordinary real bosons, not HC labels."""
    s = float(s)
    if not math.isfinite(s) or s < 0:
        raise ValueError("Finite nonnegative proper time required")
    qf = mass_spectrum(matrix)**2
    qb, xi = _boson_data(scalar_squared_masses, xi)
    ef, eb = np.exp(-s*qf), np.exp(-s*qb)
    return {"W0": math.fsum([*(4*ef), *(-eb)]),
            "B2": math.fsum([*(ef/3), *((1/6-xi)*eb)])}


def mixed_coefficients(matrix, scalar_squared_masses=(), xi=0.0, uv=20.0, ir=2.0):
    """Additional scalar determinant comparison, NOT an identified native spectrum."""
    uv, ir = window(uv, ir)
    qf = mass_spectrum(matrix)**2
    qb, xi = _boson_data(scalar_squared_masses, xi)
    fi = [proper_time_integral(np.sqrt(q), uv, ir, 2) for q in qf]
    fj = [proper_time_integral(np.sqrt(q), uv, ir, 3) for q in qf]
    bi = [proper_time_integral(np.sqrt(q), uv, ir, 2) for q in qb]
    bj = [proper_time_integral(np.sqrt(q), uv, ir, 3) for q in qb]
    a_terms = [*(np.asarray(fi)/3), *((1/6-xi)*bi)]
    a = math.fsum(a_terms)/(32*np.pi**2)
    rho = math.fsum([*(4*np.asarray(fj)), *(-np.asarray(bj))])/(32*np.pi**2)
    a_scale = math.fsum(abs(x) for x in a_terms)/(32*np.pi**2)
    # Report an unresolved near-zero coefficient rather than divide numerical cancellation noise.
    resolved = abs(a) > 1e-13*max(a_scale, 1e-300)
    moments = [math.fsum([*(4*qf**n), *(-qb**n)]) for n in range(3)]
    return {"fermion_squared_masses": qf.tolist(), "scalar_squared_masses": qb.tolist(),
            "scalar_xi": xi.tolist(), "UV": uv, "IR": ir,
            "A": a, "rho_vac": rho, "inverse_G": 16*np.pi*a,
            "Einstein_coefficient_numerically_resolved": resolved,
            "positive_Einstein_coefficient": bool(a > 0 and resolved),
            "kappa": 1/(2*a) if resolved else None,
            "Lambda_cos_truncated": rho/(2*a) if resolved else None,
            "signed_mass_moments_0_1_2": moments,
            "heat_samples": [{"s": s, **graded_heat_coefficients(s, matrix, qb, xi)}
                             for s in (0.003, 0.03, 0.3, 3.0)]}


def mixed_action_density(curvature, matrix, scalar_squared_masses=(), xi=0.0,
                         uv=20.0, ir=2.0):
    """Independent high-precision integral of the mixed a0+a2 heat density."""
    uv, ir = window(uv, ir)
    curvature = float(curvature)
    if not math.isfinite(curvature):
        raise ValueError("Finite scalar curvature required")
    qf = mass_spectrum(matrix)**2
    qb, xi = _boson_data(scalar_squared_masses, xi)
    with mp.workdps(35):
        f, b = [mp.mpf(float(q)) for q in qf], [mp.mpf(float(q)) for q in qb]
        weights = [mp.mpf(1)/6-mp.mpf(float(x)) for x in xi]
        r = mp.mpf(curvature)

        def integrand(z):
            if not z:
                return mp.mpf(0)
            ef, eb = [mp.exp(-q/z) for q in f], [mp.exp(-q/z) for q in b]
            w0 = 4*sum(ef)-sum(eb)
            b2 = sum(ef)/3+sum(w*e for w, e in zip(weights, eb))
            return (z*w0-r*b2)/(32*mp.pi**2)

        return float(mp.quad(integrand, [mp.mpf(ir)**2, mp.mpf(uv)**2]))


def vacuum_balance_examples(matrix):
    q = mass_spectrum(matrix)**2
    partners = np.repeat(q, 4)
    paired = mixed_coefficients(matrix, partners)
    delta = 1e-5
    moment_matrix = np.diag([0, np.sqrt(2), np.sqrt(2), np.sqrt(2)])
    moment_bosons = np.repeat([1.0, 3.0], [12, 4])
    lp, observed, beta = 1.616e-35, 1.1e-52, 0.5493
    return {
        "status": "ordinary scalar/Dirac determinant comparison; added scalar partners are NOT native HC fields",
        "mass_matched_minimal_scalars": paired,
        "curvature_coupling_control": [mixed_coefficients(matrix, partners, x)
                                       for x in (1/6, 1/4, 0.3)],
        "squared_mass_splitting": {
            "delta_q": delta,
            "computed": mixed_coefficients(matrix, partners+delta),
            "predicted_rho_derivative_at_matching": 12*coefficients(matrix, 20, 2)["A"]},
        "one_missing_partner": mixed_coefficients(matrix, partners[:-1]),
        "first_three_mass_moments_cancel_but_vacuum_does_not": mixed_coefficients(
            moment_matrix, moment_bosons),
        "independent_paired_action_at_R_0_01": mixed_action_density(0.01, matrix, partners),
        "full_operator_mirror_warning": "opposite equal COMPLETE metric-dependent heat kernels cancel both the vacuum and the Einstein term",
        "native_anchors": [
            {"path": "sources/research/parts/v470/10_sphaera_and_physics.tex", "label": "thm:string-lqg-duality",
             "gap": "J parity labels do not provide independent integration variables, Grassmann statistics or matched Hessian spectra"},
            {"path": "sources/research/parts/v470/10_sphaera_and_physics.tex", "label": "thm:variational-form",
             "gap": "full real gauge-fixed Hessian, constraint measure and ghosts are not evaluated; the tested null HC principal tensor is rank one"},
            {"path": "sources/research/parts/v470/23_physical_readouts.tex", "label": "def:tr-balance",
             "gap": "no identification of the trace-formula balance with the signed four-dimensional determinant coefficients W0 and B2"}],
        "source_value_unit_check": {
            "historical_paper_values_not_new_measurements": {"ell_P_m": lp, "Lambda_obs_per_m2": observed, "beta": beta},
            "observed_dimensionless_Lambda_ellP_squared": observed*lp**2,
            "written_beta_squared": beta**2,
            "ratio_between_written_and_observed_dimensionless_values": beta**2/(observed*lp**2),
            "dimensionless_hierarchy_cannot_be_changed_by_unit_conversion": True},
        "not_a_native_spectrum_or_a_higher_loop_protection_mechanism": True}


def evaluate():
    matrix = background.triadic_mass()
    sample = coefficients(matrix, 20.0, 2.0)
    massless = coefficients(np.zeros((3, 3)), 20.0, 2.0)
    sphere = [sphere_heat(s) for s in (0.02, 0.01, 0.005, 0.0025)]
    r = 0.01
    return {
        "status": "conditional regulated one-loop Euclidean Dirac comparison, NOT native HC/trace-formula Einstein derivation",
        "assumptions": ["four-dimensional smooth Euclidean spin metric already supplied",
                        "torsion-free positive elliptic D_E^2=-nabla^2+R/4",
                        "constant finite Hermitian internal M commuting with D_E",
                        "parity-even determinant modulus only; determinant phase not computed",
                        "proper-time window is a regulator, not a native fast/slow projector"],
        "formulae": {"effective_action": "Gamma_E=-1/2 Tr log(D_E^2+M^2)=+1/2 integral ds/s Tr exp[-s(D_E^2+M^2)]",
                     "heat_density": "(4 pi s)^(-2) Tr_internal exp(-s M^2) [4-R s/3+O(s^2)]",
                     "A": "sum I/(96 pi^2), I=integral ds s^-2 exp(-m^2 s)",
                     "rho": "sum J/(8 pi^2), J=integral ds s^-3 exp(-m^2 s)",
                     "Einstein_normalization": "Gamma_E=int sqrt(g)[rho-A R]; 1/G=16 pi A, kappa=1/(2 A), Lambda_cos=kappa rho",
                     "unsubtracted_vacuum_bound": "3 (UV^2+IR^2) <= Lambda_cos_truncated < 6 UV^2 for nonnegative m_i^2",
                     "bound_is_not_a_solution_of_the_full_large_curvature_effective_action": True},
        "prepared_carrier": {"matrix": matrix.tolist(),
                             "mass_eigenvalues": sample["masses"],
                             "negative_eigenvalue_is_not_negative_mass_squared": True,
                             "dimensionless_example_not_native_C7_M16_spectrum": True},
        "sample": sample,
        "independent_truncated_action_quadrature": {
            "R": r, "direct": action_density(r, matrix, 20, 2),
            "coefficient_expression": sample["rho_vac"]-sample["A"]*r},
        "sphere_spectral_check": sphere,
        "massless_window": {"computed": massless,
                            "expected_inverse_G": 3*(20**2-2**2)/(6*np.pi),
                            "expected_Lambda_cos": 3*(20**2+2**2)},
        "UV_sensitivity_at_fixed_IR_2": [coefficients(matrix, u, 2) for u in (10, 20, 40, 80)],
        "explicit_vacuum_subtraction_INPUT_not_derivation": matching(sample, bare_rho=-sample["rho_vac"]),
        "finite_Einstein_counterterm_INPUT_not_prediction": matching(sample, bare_a=sample["A"], bare_rho=-sample["rho_vac"]),
        "vacuum_balance_follow_through": vacuum_balance_examples(matrix),
        "native_source_audit": [
            {"label": "thm:einstein", "gap": "unitary exp(-i tau L0) replaced by heat exp(-tau L0), without a four-dimensional metric-dependent elliptic operator/domain or regulated determinant"},
            {"label": "prop:bilinear-einstein-reconstruction", "gap": "the Einstein-Hilbert term is explicitly assumed after coarse-graining, not evaluated from closure"},
            {"label": "prop:bilinear-einstein-reconstruction", "gap": "constant action density and cosmological curvature coefficient require normalization; they are not the same Lambda"}],
        "remaining_obligations": ["derive the native metric/coframe, elliptic operator, domain and admissible Wick rotation",
                                  "derive the spectrum, physical UV/IR scales and renormalization/matching conditions",
                                  "justify vacuum cancellation or its replacement rather than erase rho by a frame label",
                                  "evaluate higher curvature/nonlocal terms and justify the weak-curvature regime",
                                  "avoid double-counting fields integrated out and explicit low-energy probes",
                                  "specify the Lorentzian state, retarded/in-in response and free gravitational data",
                                  "include native HC/gauge/projector/Yukawa sectors and test actual closure"],
        "main_TeX_changed": False,
        "sources": ["https://arxiv.org/html/1805.03148v1", "https://arxiv.org/pdf/gr-qc/9505009",
                    "https://arxiv.org/html/gr-qc/0204062v1"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
