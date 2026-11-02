"""Candidate antisymmetric ART/QFT readout and its phase-current reaction.

New constitutive choice from existing cross ingredients, not the native full coframe.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "antisymmetric_cross_readouts", Path(__file__).with_name("HC_Gauge_Invariant_Geometry_Readouts.py"))
readouts = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(readouts)
SPEC = importlib.util.spec_from_file_location(
    "antisymmetric_cross_real_law", Path(__file__).with_name("HC_Probe_Law_Revision_Audit.py"))
real_law = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(real_law)
dirac, checks = readouts.dirac, readouts.checks
background = dirac.parent.background
ETA, WEIGHTS, BETA = dirac.ETA, dirac.WEIGHTS, dirac.BETA
SELECTOR = np.zeros((3, 3), complex)
SELECTOR[0, 1] = 1
R_MINUS = (SELECTOR-SELECTOR.conj().T)/2
Q_PHASE = 1j*R_MINUS
POINT = np.array([0.1, 0.02, -0.03, 0.01])


def channels(psi, covariant, selector=SELECTOR):
    """Directed, exchange-even/odd readouts and the odd local phase response."""
    selector = checks._finite(selector, "directed internal readout selector")
    reverse = selector.conj().T
    left, right = (readouts.pairing(psi, covariant, r) for r in (selector, reverse))
    q = 0.5j*(selector-reverse)
    charge = np.array([np.vdot(psi, q @ psi @ k.T).real for k in WEIGHTS])
    return {"directed": left.real, "reverse": right.real, "even": (left+right).real/2,
            "odd": (left-right).real/2, "phase_charge": charge}


def affine_probe_jet(point=POINT):
    """Analytic derivatives through third order of the prepared exact reference solution."""
    point = checks._real(point, (4,), "reference spacetime point")
    data = background.polynomial_background(point)
    psi, first, mass = data["psi"], data["derivatives"], data["mass_operator"]
    h = np.kron(mass, BETA)
    alpha = np.array([np.kron(np.eye(3), k) for k in WEIGHTS[1:]])
    b1 = np.array([-1j*h @ d.reshape(-1) for d in first[1:]])
    b2 = np.array([-1j*h @ d for d in b1])
    second = np.zeros((4, 4, 3, 4), complex)
    second[0, 0] = (-sum(a @ b for a, b in zip(alpha, b1))-1j*h @ first[0].reshape(-1)).reshape(3, 4)
    third = np.zeros((4, 4, 4, 3, 4), complex)
    third[0, 0, 0] = (-sum(a @ b for a, b in zip(alpha, b2))-1j*h @ second[0, 0].reshape(-1)).reshape(3, 4)
    for i in range(1, 4):
        second[0, i] = second[i, 0] = b1[i-1].reshape(3, 4)
        for permutation in set(itertools.permutations((0, 0, i))):
            third[permutation] = b2[i-1].reshape(3, 4)
    return {"point": point, "psi": psi, "first": first, "second": second, "third": third,
            "mass": mass, "reference_residual": data["reference_residual"]}


def odd_coframe_jet(data):
    psi, first, second, third = (data[k] for k in ("psi", "first", "second", "third"))
    frame = readouts.pairing(psi, first, R_MINUS).real
    dframe = np.array([(readouts.pairing(first[r], first, R_MINUS)
                       +readouts.pairing(psi, second[r], R_MINUS)).real for r in range(4)])
    ddframe = np.array([[(readouts.pairing(second[r, s], first, R_MINUS)
                         +readouts.pairing(first[r], second[s], R_MINUS)
                         +readouts.pairing(first[s], second[r], R_MINUS)
                         +readouts.pairing(psi, third[r, s], R_MINUS)).real
                        for s in range(4)] for r in range(4)])
    return frame, dframe, ddframe


def reference_geometry(point=POINT):
    data = affine_probe_jet(point)
    frame, first, second = odd_coframe_jet(data)
    if np.linalg.matrix_rank(frame) < 4:
        raise ValueError("Candidate cross coframe is degenerate at this reference point")
    bundle = dirac.bundle(frame, first, second)
    induced = dirac.dirac_data(data["psi"], data["first"], data["mass"],
                               gamma=bundle["gamma"], metric=bundle["metric"], spin=bundle["spin"])
    rebuilt = channels(data["psi"], induced["covariant"])["odd"]
    return {"data": data, "frame": frame, "first": first, "second": second, "bundle": bundle,
            "induced_residual": induced["residual"], "rebuilt_with_induced_spin": rebuilt}


def effective_weights(volume, multiplier, selector=SELECTOR):
    """Density-valued kinetic weights of the cross-constraint parent in a flat reference."""
    volume = checks._scalar(volume, "positive reference volume")
    multiplier = checks._real(multiplier, (4, 4), "real multiplier density [frame,coordinate]")
    selector = checks._finite(selector, "internal readout selector")
    if volume <= 0 or selector.shape != (3, 3):
        raise ValueError("Positive volume and a three-channel selector required")
    q = 0.5j*(selector-selector.conj().T)
    return np.array([volume*np.kron(np.eye(3), WEIGHTS[mu])
                     +np.kron(q, np.einsum("a,aij->ij", multiplier[:, mu], WEIGHTS)) for mu in range(4)])


def temporal_margin(volume, multiplier):
    """Exact smallest eigenvalue for the declared selector, not a full hyperbolicity theorem."""
    volume = checks._scalar(volume, "positive volume")
    multiplier = checks._real(multiplier, (4, 4), "multiplier density")
    if volume <= 0:
        raise ValueError("Positive volume required")
    return float(volume-(abs(multiplier[0, 0])+np.linalg.norm(multiplier[1:, 0]))/2)


def parent_variation_check(count=65):
    """Direct independent variation of the same real Dirac plus odd-cross constraint action."""
    fixture = real_law.periodic_fixture(count)
    x, differentiate = fixture["x"], fixture["differentiate"]
    rng = np.random.default_rng(23119)
    vectors = rng.normal(size=(4, 12))+1j*rng.normal(size=(4, 12))
    psi = vectors[0]+0.1*np.sin(x[:, None])*vectors[1]+0.1j*np.cos(2*x[:, None])*vectors[2]
    variation = 0.2*np.cos(3*x[:, None])*vectors[3]
    first, dfirst = np.zeros((count, 4, 12), complex), np.zeros((count, 4, 12), complex)
    first[:, 0], dfirst[:, 0] = differentiate(psi), differentiate(variation)
    multiplier = 0.06*np.sin(x[:, None, None]+np.arange(16).reshape(4, 4)/3)
    volume = 1+0.1*np.cos(x)
    weights = np.array([effective_weights(v, lam) for v, lam in zip(volume, multiplier)])
    divergence = differentiate(weights[:, 0])
    divergence = (divergence+divergence.conj().swapaxes(-1, -2))/2
    mass = np.kron(background.triadic_mass(), BETA)
    connection = np.zeros((count, 4, 12, 12), complex)
    coefficient = np.diag([0.1, -0.2, 0.3])
    connection[:, 1] = 1j*np.kron(coefficient, np.eye(4))
    reference_weights = np.array([np.kron(np.eye(3), k) for k in WEIGHTS])
    operators = [real_law.real_operator(p, dp, k, b, v*mass, div)
                 for p, dp, k, b, v, div in zip(psi, first, weights, connection, volume, divergence)]
    dx = 2*np.pi/count

    def direct_action(p, dp):
        result = 0.
        for i in range(count):
            base = real_law.action_density(p[i], dp[i], reference_weights, connection[i], mass)
            covariant = (dp[i]+connection[i] @ p[i]).reshape(4, 3, 4)
            cross = channels(p[i].reshape(3, 4), covariant)["odd"]
            result += volume[i]*base-np.sum(multiplier[i]*cross)
        return float(dx*result)

    def density_action(p, dp):
        return float(dx*sum(real_law.action_density(p[i], dp[i], weights[i], connection[i], volume[i]*mass)
                            for i in range(count)))

    predicted = 2*dx*sum(np.vdot(v, op["symmetric"]).real for v, op in zip(variation, operators))
    step = 1e-5
    numeric = (direct_action(psi+step*variation, first+step*dfirst)
               -direct_action(psi-step*variation, first-step*dfirst))/(2*step)
    ward = max(abs(op["current_divergence"]-2*np.vdot(p, op["symmetric"]).imag) for p, op in zip(psi, operators))
    return {"grid_points": count, "direct_parent_density_action_error": abs(direct_action(psi, first)-density_action(psi, first)),
            "independent_probe_variation_error": float(abs(numeric-predicted)),
            "phase_Ward_identity_max_error": float(ward),
            "minimum_temporal_weight_eigenvalue": float(min(np.linalg.eigvalsh(k[0])[0] for k in weights)),
            "off_shell_variation_not_joint_field_solution": True}


def kinetic_volume_control(data):
    """Algebraic stress/volume test with the SAME derivative; not a compatible induced solution."""
    kinetic_frame = -readouts.pairing(data["psi"], data["first"]).imag
    inverse = np.linalg.inv(kinetic_frame)
    metric = kinetic_frame.T @ ETA @ kinetic_frame
    gamma = np.einsum("ma,aij->mij", inverse, dirac.GAMMA)
    result = dirac.dirac_data(data["psi"], data["first"], data["mass"], gamma=gamma, metric=metric)
    return {"frame": kinetic_frame, "metric": metric, "probe": result,
            "volume_identity_error": abs(result["lagrangian"]+result["mass_bilinear"].real-4),
            "pure_trace_stress_error": float(np.linalg.norm(result["stress"]-(result["lagrangian"]-1)*metric))}


def evaluate():
    g = reference_geometry()
    d = g["data"]
    sourced = readouts.spectral.field_data()
    r6 = np.kron(np.eye(2), SELECTOR)
    sourced_channels = channels(sourced["psi"], readouts.covariant_jet(sourced), r6)
    kinetic = kinetic_volume_control(d)
    return {
        "status": "candidate antisymmetric existing-cross readout, reference on-shell curved diagnostic and parent-current variation; NOT native full-coframe replacement or a joint induced/gauge/Einstein solution",
        "source": {"path": "sources/research/parts/v470/12_structural_core.tex", "ingredient": "Cross-bilinear geometry channel and similarly with probes exchanged",
                   "new_choice": "C_minus=Re(B_ART,QFT-B_QFT,ART)/2; its adoption as a coframe remains additional"},
        "identities": {"exchange_even": "C_plus=(covariant derivative of Re(bar psi_ART Gamma^a psi_QFT))/2 for the compatible common transport",
                       "exchange_odd": "C_minus=Re(Psi^dagger R_minus K^a D_mu Psi)=Im(Psi^dagger Q K^a D_mu Psi), Q=i R_minus Hermitian",
                       "fixed_connection_local_phase": "delta C_minus^a_mu=q^a partial_mu alpha, q^a=Psi^dagger Q K^a Psi",
                       "parent_conserved_flux_density": "volume J_D^mu+lambda_a^mu q^a",
                       "kinetic_density_weights": "volume K_coordinate^mu+lambda_a^mu (Q tensor K_frame^a)"},
        "existing_sourced_stationary_branch": {"odd_rank": int(np.linalg.matrix_rank(sourced_channels["odd"], tol=1e-10)),
                                               "odd_singular_values": np.linalg.svd(sourced_channels["odd"], compute_uv=False).tolist(),
                                               "angular_columns_norm": float(np.linalg.norm(sourced_channels["odd"][:, 1:3])),
                                               "still_not_four_dimensional_geometry": True},
        "reference_on_shell_curved_diagnostic": {"point": d["point"].tolist(), "coframe": g["frame"].tolist(),
                                                "coframe_singular_values": np.linalg.svd(g["frame"], compute_uv=False).tolist(),
                                                "metric_eigenvalues": np.linalg.eigvalsh(g["bundle"]["metric"]).tolist(),
                                                "reference_probe_residual_norm": float(np.linalg.norm(d["reference_residual"])),
                                                "coframe_determinant": float(np.linalg.det(g["frame"])),
                                                "Ricci_scalar_not_physically_calibrated": g["bundle"]["curvature"]["scalar"],
                                                "Riemann_component_norm_not_invariant": float(np.linalg.norm(g["bundle"]["curvature"]["riemann"])),
                                                "induced_probe_residual_norm": float(np.linalg.norm(g["induced_residual"])),
                                                "own_spin_changes_readout_norm": float(np.linalg.norm(g["rebuilt_with_induced_spin"]-g["frame"])),
                                                "neutral_reference_equation_has_no_solved_charged_Gauss_or_Einstein_sector": True},
        "parent_action_check": parent_variation_check(),
        "flat_reference_temporal_positivity": {"exact_condition": "abs(lambda_0^0)+norm(lambda_spatial^0)<2 volume",
                                               "not_derived_multiplier_dynamics_or_general_hyperbolicity": True},
        "quadrature_locked_kinetic_limit": {"identity": "psi_QFT=exp(i delta) psi_ART gives C_minus=-sin(delta) Im(bar psi_ART Gamma^a D_mu psi_ART)",
                                           "quadrature_not_derived_or_preserved_by_real_triadic_coupling": True,
                                           "same_derivative_kinetic_volume_identity_error": kinetic["volume_identity_error"],
                                           "same_derivative_pure_trace_stress_identity_error": kinetic["pure_trace_stress_error"],
                                           "on_shell_fixed_metric_Dirac_stress_if_kinetic_frame_is_own_frame": "T_ab=-eta_ab/s; not generic matter and not a derived cosmological constant"},
        "remaining_obligations": ["justify the exchange-odd observable and its physical normalization",
                                  "transport the readout covariantly under the actual gauge group and retain its reaction",
                                  "solve coframe, multiplier, probe, gauge and geometry variations together with the same connection",
                                  "check positive temporal weights, constraints, boundary data and physical scale calibration"],
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
