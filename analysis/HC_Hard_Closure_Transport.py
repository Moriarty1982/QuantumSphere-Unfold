"""Hard-closure transport, induced bundle curvature and connection nonuniqueness."""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


def _module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


hessian = _module("hard_closure_hessian", "HC_Closure_Fluctuation_Hessian.py")
dirac = _module("hard_closure_dirac", "HC_Dirac_State_Gravity.py")
checks, GAMMA = hessian.checks, dirac.GAMMA
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)


def commutator(a, b):
    return a @ b-b @ a


def _projector_jet(p, first):
    p = hessian.projector(p)
    first = checks._finite(first, "projector first jet")
    if (first.shape != (4, *p.shape)
            or not np.allclose(first, first.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)
            or not np.allclose(p @ first+first @ p, first, atol=1e-11, rtol=0)):
        raise ValueError("Four Hermitian projector-tangent derivatives required")
    return p, first


def normal_operator(p, first, connection, omega):
    """Off-sector unmodified master operator for a spin/internal factorization."""
    p, first = _projector_jet(p, first)
    b, omega = checks._finite(connection, "connection"), checks._finite(omega, "resonance")
    if b.shape != first.shape or omega.shape != p.shape:
        raise ValueError("Connection and spin-scalar resonance on the projector carrier required")
    q = np.eye(len(p))-p
    dp = first+commutator(b, p)
    transport, mass = q @ dp @ p, q @ omega @ p
    operator = sum(1j*np.kron(x, g) for x, g in zip(transport, GAMMA))-np.kron(mass, np.eye(4))
    return {"covariant_projector_first": dp, "transport_leakage": transport,
            "resonance_leakage": mass, "operator": operator,
            "norm_squared": float(np.vdot(operator, operator).real),
            "coefficient_norm_squared": float(4*(np.vdot(transport, transport).real+np.vdot(mass, mass).real))}


def compatible_connection(p, first, diagonal=None):
    """General anti-Hermitian solution D P=0, relative to the fixed trivial derivative."""
    p, first = _projector_jet(p, first)
    diagonal = np.zeros_like(first) if diagonal is None else checks._finite(diagonal, "block connection")
    if (diagonal.shape != first.shape
            or not np.allclose(diagonal, -diagonal.conj().swapaxes(-1, -2), atol=1e-12, rtol=0)
            or np.linalg.norm(commutator(diagonal, p)) > 1e-11):
        raise ValueError("Four anti-Hermitian block-diagonal additions required")
    return commutator(p, first)+diagonal


def compressed_curvature(p, first, connection, curvature):
    """Curvature of P D on the subbundle, including its extrinsic term when D P != 0."""
    p, first = _projector_jet(p, first)
    b, f = checks._finite(connection, "connection"), checks._curvature(curvature)
    if b.shape != first.shape or f.shape != (4, 4, *p.shape):
        raise ValueError("Compatible connection/curvature on the projector carrier required")
    dp = first+commutator(b, p)
    extra = dp[:, None] @ dp[None, :]-dp[None, :] @ dp[:, None]
    return p @ (f+extra) @ p


def reduce_frame(frame, first, second, connection, connection_first, omega):
    """Explicit local frame connection and curvature, independent of compression formula."""
    v, dv, ddv, b, db, omega = [checks._finite(x, name) for x, name in
                               ((frame, "isometric frame"), (first, "frame first jet"),
                                (second, "frame second jet"), (connection, "connection"),
                                (connection_first, "connection first jet"), (omega, "resonance"))]
    if (v.ndim != 2 or v.shape[1] == 0 or dv.shape != (4, *v.shape)
            or ddv.shape != (4, 4, *v.shape) or b.shape != (4, v.shape[0], v.shape[0])
            or db.shape != (4, *b.shape) or omega.shape != b.shape[1:]
            or not np.allclose(v.conj().T @ v, np.eye(v.shape[1]), atol=1e-11, rtol=0)):
        raise ValueError("Compatible local isometry, jets and connection required")
    a = np.array([v.conj().T @ (d+bb @ v) for d, bb in zip(dv, b)])
    da = np.array([[dv[nu].conj().T @ dv[mu]+v.conj().T @ ddv[nu, mu]
                    +dv[nu].conj().T @ b[mu] @ v+v.conj().T @ db[nu, mu] @ v
                    +v.conj().T @ b[mu] @ dv[nu] for mu in range(4)] for nu in range(4)])
    f = checks.connection_curvature(a, da)
    return {"connection": a, "first": da, "curvature": f,
            "omega": v.conj().T @ omega @ v}


def texture(point=(0.0, 0.2, -0.1, 0.0), mix=0.0, eta=0.7,
            offset=0.25, slope=0.3, rate=0.8):
    """Two-channel local patch; same P with a continuous family of compatible curvatures."""
    point = checks._real(point, (4,), "point")
    mix, eta, offset, slope, rate = [checks._scalar(x, name) for x, name in
                                   ((mix, "connection mixing"), (eta, "closure load"),
                                    (offset, "offset"), (slope, "slope"), (rate, "phase rate"))]
    u, phi = offset-slope*point[1], rate*point[2]
    if abs(u) >= 1:
        raise ValueError("Texture patch requires |offset-slope*x|<1")
    s, cosine, sine = np.sqrt(1-u*u), np.cos(phi), np.sin(phi)
    n = np.array([s*cosine, s*sine, u])
    dn = np.zeros((4, 3))
    dn[1] = [slope*u*cosine/s, slope*u*sine/s, -slope]
    dn[2] = [-rate*s*sine, rate*s*cosine, 0]
    ddn = np.zeros((4, 4, 3))
    ddn[1, 1] = [-slope**2*cosine/s**3, -slope**2*sine/s**3, 0]
    ddn[1, 2] = ddn[2, 1] = [-rate*slope*u*sine/s, rate*slope*u*cosine/s, 0]
    ddn[2, 2] = [-rate**2*s*cosine, -rate**2*s*sine, 0]
    p = (np.eye(2)+np.einsum("a,aij->ij", n, PAULI))/2
    dp, ddp = np.einsum("ma,aij->mij", dn, PAULI)/2, np.einsum("mna,aij->mnij", ddn, PAULI)/2
    c, h, phase = np.sqrt((1+u)/2), np.sqrt((1-u)/2), np.exp(1j*phi)
    cx, hx = -slope/(4*c), slope/(4*h)
    cxx, hxx = -slope**2/(16*c**3), -slope**2/(16*h**3)
    unitary = np.array([[c, -phase.conjugate()*h], [phase*h, c]])
    du, ddu = np.zeros((4, 2, 2), complex), np.zeros((4, 4, 2, 2), complex)
    du[1] = [[cx, -phase.conjugate()*hx], [phase*hx, cx]]
    du[2] = [[0, 1j*rate*phase.conjugate()*h], [1j*rate*phase*h, 0]]
    ddu[1, 1] = [[cxx, -phase.conjugate()*hxx], [phase*hxx, cxx]]
    ddu[1, 2] = ddu[2, 1] = [[0, 1j*rate*phase.conjugate()*hx], [1j*rate*phase*hx, 0]]
    ddu[2, 2] = [[0, rate**2*phase.conjugate()*h], [-rate**2*phase*h, 0]]
    geometric = commutator(p, dp)
    geometric_first = np.array([[commutator(dp[nu], dp[mu])+commutator(p, ddp[nu, mu])
                                 for mu in range(4)] for nu in range(4)])
    flat = -du @ unitary.conj().T
    flat_first = np.array([[-ddu[nu, mu] @ unitary.conj().T-du[mu] @ du[nu].conj().T
                            for mu in range(4)] for nu in range(4)])
    axis = np.array([-1.0, 0, 0, 1.0])
    b = (1-mix)*geometric+mix*flat+eta*axis[:, None, None]*(np.eye(2)-p)
    db = (1-mix)*geometric_first+mix*flat_first-eta*axis[None, :, None, None]*dp[:, None]
    f = checks.connection_curvature(b, db)
    expected = np.zeros_like(f)
    expected[1, 2] = (1-mix)*1j*slope*rate*(2*p-np.eye(2))/2
    expected[2, 1] = -expected[1, 2]
    return {"P": p, "P_first": dp, "P_second": ddp, "U": unitary, "U_first": du,
            "U_second": ddu, "geometric": geometric, "flat": flat, "connection": b,
            "connection_first": db, "curvature": f, "expected_curvature": expected,
            "frame": unitary[:, :1], "frame_first": du[:, :, :1], "frame_second": ddu[:, :, :, :1],
            "reduced_expected": np.array([0, 0, (1-mix)*1j*rate*(1-u)/2, 0]),
            "constant_flux": (1-mix)*slope*rate/2}


def yang_mills_check(point=(0.0, 0.2, -0.1, 0.0), mix=0.0, eta=0.7, step=1e-5):
    point = checks._real(point, (4,), "point")
    step = checks._scalar(step, "derivative step")
    if step <= 0:
        raise ValueError("Positive derivative step required")
    data = texture(point, mix, eta)
    first = np.array([(texture(point+step*e, mix, eta)["curvature"]
                       -texture(point-step*e, mix, eta)["curvature"])/(2*step) for e in np.eye(4)])
    covariant = first+data["connection"][:, None, None] @ data["curvature"][None]-data["curvature"][None] @ data["connection"][:, None, None]
    return np.einsum("m,mmnij->nij", np.diag(dirac.ETA), covariant)


def lifted_residual(data, chi, chi_first, mass=0.6):
    v, dv, b = data["frame"], data["frame_first"], data["connection"]
    reduced = reduce_frame(v, dv, data["frame_second"], b, data["connection_first"], mass*np.eye(2))
    psi = v @ chi
    first = dv @ chi+v @ chi_first
    full = dirac.dirac_data(psi, first+b @ psi, mass*np.eye(2))["residual"]
    small = dirac.dirac_data(chi, chi_first+reduced["connection"] @ chi, reduced["omega"])["residual"]
    return {"full": full, "reduced": small, "lift_error": full-v @ small}


def loop_transport(mix=0.0, steps=64, eta=0.7):
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 4:
        raise ValueError("At least four midpoint steps per edge required")
    corners = np.array([[0, -0.3, -0.2, 0], [0, 0.4, -0.2, 0],
                        [0, 0.4, 0.5, 0], [0, -0.3, 0.5, 0], [0, -0.3, -0.2, 0]])
    transport = np.eye(2, dtype=complex)
    for start, end in zip(corners, corners[1:]):
        delta = (end-start)/steps
        for j in range(steps):
            b = texture(start+(j+0.5)*delta, mix, eta)["connection"]
            hermitian = -1j*np.einsum("m,mij->ij", delta, b)
            if not np.allclose(hermitian, hermitian.conj().T, atol=1e-12, rtol=0):
                raise ValueError("This loop integrator requires a unitary spatial connection")
            eigenvalues, vectors = np.linalg.eigh(hermitian)
            increment = (vectors*np.exp(-1j*eigenvalues)) @ vectors.conj().T
            transport = increment @ transport
    frame = texture(corners[0], mix, eta)["frame"]
    phase = complex((frame.conj().T @ transport @ frame)[0, 0])
    expected = np.exp(-1j*(1-mix)*0.3*0.8*0.7*0.7/2)
    return {"transport": transport, "phase": phase, "expected_phase": expected,
            "error": float(abs(phase-expected)), "steps_per_edge": steps}


def quartic_energy(epsilon):
    p0 = np.diag([1.0, 0.0])
    x, y = hessian.hermitian_basis(2)[2:]
    generators = np.zeros((4, 2, 2), complex)
    generators[1], generators[2] = x, y
    p, dp = hessian._projector_jet(p0, 0.2*x-0.1*y, generators, epsilon)
    f = dp[:, None] @ dp[None]-dp[None] @ dp[:, None]
    return float(np.vdot(f, f).real/4)


def evaluate():
    data, flat = texture(), texture(mix=1)
    omega = 0.6*np.eye(2)
    normal = normal_operator(data["P"], data["P_first"], data["connection"], omega)
    naive = normal_operator(data["P"], data["P_first"], np.zeros((4, 2, 2)), omega)
    reduced = reduce_frame(data["frame"], data["frame_first"], data["frame_second"],
                           data["connection"], data["connection_first"], omega)
    rng = np.random.default_rng(219)
    chi, derivative = rng.normal(size=(1, 4))+1j*rng.normal(size=(1, 4)), rng.normal(size=(4, 1, 4))+1j*rng.normal(size=(4, 1, 4))
    lifted = lifted_residual(data, chi, derivative)
    loops = [loop_transport(steps=s) for s in (32, 64, 128)]
    sizes = [0.04, 0.02, 0.01]
    return {
        "status": "hard-closure transport identities and local finite connection family; NOT a native metric/Einstein solution or vacuum cancellation",
        "normal_equation": {"formula": "N=sum_mu i (Q D_mu P P) tensor Gamma^mu-(Q Omega P) tensor I",
                            "norm_identity": "||N||_F^2=4 sum_mu ||Q D_mu P P||_F^2+4||Q Omega P||_F^2 in the declared normalized factorization",
                            "M_closure_alone_is_not_full_master_invariance": True,
                            "canonical_connection_normal_norm": float(np.linalg.norm(normal["operator"])),
                            "moving_P_with_zero_connection_normal_norm": float(np.linalg.norm(naive["operator"])),
                            "not_a_no_go_for_a_selected_single_probe_or_spin_dependent_resonance": True},
        "compatible_connection": {"general_unitary_solution": "B_mu=[P,partial_mu P]+C_mu, [C_mu,P]=0, C_mu^dagger=-C_mu",
                                  "curvature_at_C_zero": "F_mu_nu=[partial_mu P,partial_nu P]",
                                  "compression": "F^(P D)=P F P+P[D_mu P,D_nu P]P",
                                  "internal_bundle_curvature_is_not_Riemann_curvature": True},
        "local_source_free_family": {"assumptions": "fixed flat reference metric, empty probe, M=m I (degenerate), hard H=Lambda=0, constant null n; two-channel local patch only",
                                     "P": "P=U diag(1,0) U^dagger, u=0.25-0.3 x, phi=0.8 y, |u|<1",
                                     "B_t": "(1-t)[P,dP]-t dU U^dagger+eta Q n",
                                     "curvature": "F_xy=(1-t) i (0.3)(0.8)(2P-I)/2; all other independent components zero",
                                     "same_P_and_H_allow_different_non_gauge_equivalent_curvatures": True,
                                     "canonical_curvature_norm": float(np.linalg.norm(data["curvature"])),
                                     "flat_choice_curvature_norm": float(np.linalg.norm(flat["curvature"])),
                                     "curvature_formula_error": float(np.linalg.norm(data["curvature"]-data["expected_curvature"])),
                                     "finite_difference_D_F_norm": float(np.linalg.norm(yang_mills_check())),
                                     "closure_and_HC_printed_currents_zero_for_M_mI_empty_probe": True,
                                     "not_a_full_gravitational_or_global_finite_energy_solution": True},
        "reduced_probe": {"connection_formula": "b=V^dagger partial V+V^dagger B V",
                          "Berry_connection_y_imaginary": float(reduced["connection"][2, 0, 0].imag),
                          "Berry_curvature_xy_imaginary": float(reduced["curvature"][1, 2, 0, 0].imag),
                          "arbitrary_probe_residual_lift_error": float(np.linalg.norm(lifted["lift_error"])),
                          "this_is_an_operator_lift_identity_not_an_on_shell_backreacting_probe_solution": True},
        "spatial_holonomy": [{"steps_per_edge": x["steps_per_edge"],
                              "computed_phase": [x["phase"].real, x["phase"].imag],
                              "expected_phase": [x["expected_phase"].real, x["expected_phase"].imag],
                              "error": x["error"]} for x in loops],
        "canonical_projector_energy_near_constant_P": {"epsilon": sizes, "energy": [quartic_energy(e) for e in sizes],
                                                      "leading_order": "epsilon^4, not a free quadratic scalar kinetic term",
                                                      "positive_dagger_energy_is_a_comparison_not_a_silent_native_action_fix": True},
        "remaining_obligations": ["actual C7 representation, spin factorization, full Omega/triadic/gauge data",
                                  "native background selection and allowed projector/operator motion",
                                  "derive or prescribe block connection C with actual boundary/topological data",
                                  "full constrained real action, measure and gauge reduction before a determinant",
                                  "metric reconstruction, common backreaction, physical scales and vacuum matching"],
        "main_TeX_changed": False,
        "sources": ["sources/research/parts/v470/10_sphaera_and_physics.tex: thm:closed-master-system, prop:yang-mills-limit",
                    "https://authors.library.caltech.edu/records/2pepc-k9f58"]}


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
