"""Closed-sector HC jets and a gauge-checked comparison Hessian, not native quantization."""
import argparse
import importlib.util
import json
from pathlib import Path

import mpmath as mp
import numpy as np


def _module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


phase = _module("hessian_phase", "Phase_Selection_Derivation.py")
checks = _module("hessian_null", "HC_Null_Axis_Action_Check.py")
heat = _module("hessian_heat", "HC_Induced_Gravity_Heat_Kernel.py")


def projector(value):
    p = checks._generator(value)
    if not np.allclose(p @ p, p, atol=1e-12, rtol=0):
        raise ValueError("An orthogonal projector required")
    return p


def hermitian_basis(size):
    if isinstance(size, bool) or not isinstance(size, int) or size < 1:
        raise ValueError("A positive integer carrier size required")
    eye = np.eye(size)
    basis = [np.outer(e, e) for e in eye]
    for i in range(size):
        for j in range(i+1, size):
            upper = np.outer(eye[i], eye[j])
            basis.extend([(upper+upper.T)/np.sqrt(2), -1j*(upper-upper.T)/np.sqrt(2)])
    return np.asarray(basis, complex)


def tangent_basis(p):
    p = projector(p)
    values, vectors = np.linalg.eigh(p)
    result = []
    for i in np.flatnonzero(values > 0.5):
        for j in np.flatnonzero(values < 0.5):
            upper = np.outer(vectors[:, i], vectors[:, j].conj())
            result.extend([(upper+upper.conj().T)/np.sqrt(2),
                           -1j*(upper-upper.conj().T)/np.sqrt(2)])
    return np.asarray(result, complex).reshape(-1, len(p), len(p))


def closed_jets(m0, p0, dm, dp, rho=0.5, sigma=0.5):
    """Lambda(e)=e^2 Lambda2+O(e^3) on a closed Hermitian background."""
    p0 = projector(p0)
    m0, dm, dp = [checks._generator(x) for x in (m0, dm, dp)]
    if any(x.shape != p0.shape for x in (m0, dm, dp)):
        raise ValueError("One common finite carrier required")
    if (np.linalg.norm(m0 @ p0-p0 @ m0) > 1e-11
            or np.linalg.norm(p0 @ dp+dp @ p0-dp) > 1e-11):
        raise ValueError("A closed background and a projector-tangent variation required")
    rho, sigma = checks._scalar(rho, "rho"), checks._scalar(sigma, "sigma")
    if rho < 0 or sigma < 0:
        raise ValueError("Nonnegative closure coefficients required")
    q0 = np.eye(len(p0))-p0
    c1 = dm @ p0-p0 @ dm+m0 @ dp-dp @ m0
    r1 = (q0 @ dm @ p0+p0 @ dm @ q0+m0 @ dp+dp @ m0
          -2*dp @ m0 @ p0-2*p0 @ m0 @ dp)
    second = rho*c1.conj().T @ c1+sigma*r1.conj().T @ r1
    return {"commutator_first": c1, "residue_first": r1,
            "Lambda_first": np.zeros_like(p0), "Lambda_quadratic_coefficient": second}


def projector_path(p0, generator, epsilon):
    p0, generator = projector(p0), checks._generator(generator)
    if generator.shape != p0.shape:
        raise ValueError("One common finite carrier required")
    epsilon = checks._scalar(epsilon, "path parameter")
    w, v = np.linalg.eigh(generator)
    unitary = (v*np.exp(1j*epsilon*w)) @ v.conj().T
    return unitary @ p0 @ unitary.conj().T


def symbol(momentum, p0, axis=(1, 0, 0, 0), kappa=0.4, eta=0.7,
           penalty=1.2, gauge_fix=1.0, principal_only=False):
    """Positive Euclidean dagger comparison with REAL axis, not a Wick rotation of null n."""
    p0 = projector(p0)
    k, n = [checks._real(x, (4,), label) for x, label in
            ((momentum, "momentum"), (axis, "Euclidean axis"))]
    if np.linalg.norm(k) == 0 or np.linalg.norm(n) == 0:
        raise ValueError("Nonzero momentum and Euclidean axis required")
    kappa, eta, penalty = [checks._scalar(x, name) for x, name in
                           ((kappa, "kappa"), (eta, "eta"), (penalty, "penalty"))]
    if penalty < 0:
        raise ValueError("Nonnegative matching penalty required")
    if gauge_fix is not None:
        gauge_fix = checks._scalar(gauge_fix, "gauge parameter")
        if gauge_fix <= 0:
            raise ValueError("Positive gauge parameter required")
    basis, tangent = hermitian_basis(len(p0)), tangent_basis(p0)
    d, t = len(basis), len(tangent)
    count = 5*d+t
    identity, q0 = np.eye(d), np.eye(len(p0))-p0
    embedding = np.einsum("aij,bji->ab", basis, tangent).real
    commutator = 1j*(q0 @ basis-basis @ q0)
    c = np.einsum("aij,bji->ab", basis, commutator).real
    derivative = np.zeros((4, d, count), complex)
    for mu in range(4):
        if not principal_only:
            derivative[mu, :, mu*d:(mu+1)*d] = -eta*c
        derivative[mu, :, 4*d:5*d] = 1j*k[mu]*kappa*identity
        derivative[mu, :, 5*d:] = -1j*k[mu]*eta*embedding
    maxwell, load = [], []
    for mu in range(4):
        for nu in range(mu+1, 4):
            f = np.zeros((d, count), complex)
            f[:, nu*d:(nu+1)*d] += 1j*k[mu]*identity
            f[:, mu*d:(mu+1)*d] -= 1j*k[nu]*identity
            maxwell.append(f)
            load.append(n[nu]*derivative[mu]-n[mu]*derivative[nu])
    f, x = np.concatenate(maxwell), np.concatenate(load)
    hessian = f.conj().T @ f+x.conj().T @ x
    if not principal_only:
        hessian[4*d:5*d, 4*d:5*d] += 2*penalty*identity
    gauge = np.zeros((d, count), complex)
    for mu in range(4):
        gauge[:, mu*d:(mu+1)*d] = 1j*k[mu]*identity
    if gauge_fix is not None:
        hessian += gauge.conj().T @ gauge/gauge_fix
    gauge_directions = np.zeros((count, d), complex)
    for mu in range(4):
        gauge_directions[mu*d:(mu+1)*d] = -1j*k[mu]*identity
    gauge_directions[5*d:] = embedding.T @ c
    return {"H": hessian, "F_map": f, "X_map": x, "gauge_map": gauge,
            "gauge_directions": gauge_directions, "ghost": float(k @ k)*identity,
            "basis": basis, "tangent_basis": tangent, "tangent_embedding": embedding,
            "commutator_map": c, "momentum": k, "axis": n,
            "kappa": kappa, "eta": eta, "penalty": penalty, "gauge_fix": gauge_fix,
            "axis_wedge_square": float((n @ n)*(k @ k)-(n @ k)**2)}


def _projector_jet(p0, generator, generator_first, epsilon):
    """Frechet derivative via the standard block exponential, retaining noncommutation."""
    with mp.workdps(25):
        size = len(p0)
        a = 1j*epsilon*generator
        unitary = np.array(mp.expm(mp.matrix(a.tolist())).tolist(), complex)
        first = []
        for derivative in generator_first:
            block = np.block([[a, 1j*epsilon*derivative], [np.zeros_like(a), a]])
            du = np.array(mp.expm(mp.matrix(block.tolist())).tolist(), complex)[:size, size:]
            first.append(du @ p0 @ unitary.conj().T+unitary @ p0 @ du.conj().T)
    return unitary @ p0 @ unitary.conj().T, np.asarray(first)


def finite_action_average(amplitudes, data, p0, m0, epsilon, phases=8):
    """Independent nonlinear curvature/penalty along exact projector paths; soft closure only."""
    p0, m0 = projector(p0), checks._generator(m0)
    if p0.shape != m0.shape or np.linalg.norm(m0 @ p0-p0 @ m0) > 1e-11:
        raise ValueError("A closed background on one carrier required")
    amplitudes = checks._finite(amplitudes, "Fourier amplitudes")
    if amplitudes.shape != (len(data["H"]),) or not isinstance(phases, int) or phases < 4:
        raise ValueError("Compatible Fourier amplitudes and at least four phases required")
    epsilon = checks._scalar(epsilon, "perturbation size")
    basis, tangent, k, n = [data[x] for x in ("basis", "tangent_basis", "momentum", "axis")]
    d = len(basis)
    average = 0.0
    for angle in 2*np.pi*np.arange(phases)/phases:
        factor = np.exp(1j*angle)
        # Real Fourier coefficients, not entrywise real parts of Hermitian matrices.
        a = epsilon*np.einsum("ma,aij->mij", (amplitudes[:4*d].reshape(4, d)*factor).real, basis)
        da = epsilon*np.einsum("n,ma,aij->nmij", k, (1j*amplitudes[:4*d].reshape(4, d)*factor).real, basis)
        h = epsilon*np.einsum("a,aij->ij", (amplitudes[4*d:5*d]*factor).real, basis)
        dh = epsilon*np.einsum("m,a,aij->mij", k, (1j*amplitudes[4*d:5*d]*factor).real, basis)
        pi = np.einsum("a,aij->ij", (amplitudes[5*d:]*factor).real, tangent)
        dpi = np.einsum("m,a,aij->mij", k, (1j*amplitudes[5*d:]*factor).real, tangent)
        generator = -1j*(pi @ p0-p0 @ pi)
        dg = -1j*(dpi @ p0-p0 @ dpi)
        p, dp = _projector_jet(p0, generator, dg, epsilon)
        load = data["kappa"]*h+data["eta"]*(np.eye(len(p0))-p)
        dload = data["kappa"]*dh-data["eta"]*dp
        connection = 1j*a+n[:, None, None]*load
        derivative = 1j*da+n[None, :, None, None]*dload[:, None]
        curvature = checks.connection_curvature(connection, derivative)
        target = phase.minimal_native_closure(m0, p)
        value = np.vdot(curvature, curvature).real/4+data["penalty"]*np.vdot(h-target, h-target).real
        if data["gauge_fix"] is not None:
            divergence = np.einsum("mmij->ij", da)
            value += np.vdot(divergence, divergence).real/(2*data["gauge_fix"])
        average += float(value)/phases
    return average


def maxwell_dirac_control(dirac_count=1, vector_count=2, uv=20.0, ir=2.0):
    """Massless free Maxwell+FP control, not the native connection/HC determinant."""
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in (dirac_count, vector_count)):
        raise ValueError("Nonnegative integer free-field counts required")
    i, j = [heat.proper_time_integral(0, uv, ir, p) for p in (2, 3)]
    return {"Dirac_count": dirac_count, "Maxwell_count": vector_count,
            "vacuum_weight": 4*dirac_count-2*vector_count,
            "curvature_weight": dirac_count/3-2*vector_count/3,
            "rho": (4*dirac_count-2*vector_count)*j/(32*np.pi**2),
            "A": (dirac_count/3-2*vector_count/3)*i/(32*np.pi**2)}


def evaluate():
    p0, m0 = np.diag([1.0, 0.0]), np.diag([0.4, 1.3])
    generator = np.array([[0, 1-0.3j], [1+0.3j, 0]])
    dp = 1j*(generator @ p0-p0 @ generator)
    jets = closed_jets(m0, p0, np.zeros((2, 2)), dp)
    generic = symbol([0.3, 0.8, -0.4, 0.5], p0)
    parallel = symbol([1, 0, 0, 0], p0)
    principal = symbol(generic["momentum"], p0, principal_only=True)
    raw = symbol(generic["momentum"], p0, gauge_fix=None)
    rng = np.random.default_rng(932)
    amplitudes = (rng.normal(size=len(generic["H"]))+1j*rng.normal(size=len(generic["H"])))/5
    quadratic = np.vdot(amplitudes, generic["H"] @ amplitudes).real
    sizes = [0.04, 0.02, 0.01]
    approximations = [4*finite_action_average(amplitudes, generic, p0, m0, e)/e**2 for e in sizes]
    return {
        "status": "native closed-sector Taylor identities plus a FULL finite constant-background Euclidean dagger-comparison Hessian; NOT native quantization",
        "native_gaussian_jets": {
            "projector_tangent": "P0 pi+pi P0=pi; pi has only off-diagonal P0/Q0 blocks",
            "Lambda_first": jets["Lambda_first"].real.tolist(),
            "Lambda_quadratic_coefficient": jets["Lambda_quadratic_coefficient"].real.tolist(),
            "independent_H_penalty": "lambda ||H-Lambda||^2=epsilon^2 lambda ||h||^2+O(epsilon^3), no h/pi quadratic mixing",
            "dependent_H": "H=Lambda implies delta H=0 on an exactly closed background; no independent HC Gaussian field",
            "fixed_M_gapped_example": "(a_i-d_j) pi_ij=0 under linearized exact closure; all cross gaps in the sample nonzero, hence pi=0",
            "M_is_not_the_earlier_prepared_triadic_Dirac_mass_matrix": True,
            "positive_H_at_zero_is_a_cone_boundary_not_an_unconstrained_Hermitian_Gaussian": True},
        "comparison_assumptions": ["finite U(N) carrier, ordinary Hermitian fields and Hilbert-Schmidt norm",
                                   "Euclidean real nonzero fixed axis, NOT a justified continuation of a real null Lorentzian axis",
                                   "positive Tr(F^dagger F)/4, different from the literal printed Tr(F F) action",
                                   "flat B0=eta Q0 n, empty probe background; independent unconstrained H with soft matching penalty",
                                   "projector tangent kept, exact closure constraint NOT imposed on off-shell fluctuation integration",
                                   "full unitary gauge directions concern the curvature/matching quadratic form; fixed noncentral M restricts actual admissible symmetries"],
        "quadratic_dictionary": {
            "u": "kappa h-eta pi",
            "f": "i(k_mu a_nu-k_nu a_mu)",
            "d": "d_mu=i k_mu u-eta C a_mu, C=i[Q0,.]",
            "X": "n_nu d_mu-n_mu d_nu",
            "H": "F_map^dagger F_map+X_map^dagger X_map+2 lambda H_block+(gauge_map^dagger gauge_map)/zeta",
            "ghost": "k^2 per complex FP ghost in the declared unitary comparison",
            "q": "|n|^2 |k|^2-(n.k)^2, zero for all k parallel n",
            "no_valid_native_heat_trace_or_physical_mode_count_follows": True},
        "example": {
            "N": 2, "P_rank": 1, "Hermitian_color_dimension": 4,
            "projector_tangent_dimension": len(generic["tangent_basis"]),
            "real_field_component_count": len(generic["H"]),
            "generic_gauge_fixed_rank": int(np.linalg.matrix_rank(generic["H"], tol=1e-10)),
            "generic_principal_rank": int(np.linalg.matrix_rank(principal["H"], tol=1e-10)),
            "parallel_gauge_fixed_rank": int(np.linalg.matrix_rank(parallel["H"], tol=1e-10)),
            "parallel_eigenvalues": np.linalg.eigvalsh(parallel["H"]).tolist(),
            "quadratic_gauge_null_error": float(np.linalg.norm(raw["H"] @ raw["gauge_directions"])),
            "ghost_variation_error": float(np.linalg.norm(raw["gauge_map"] @ raw["gauge_directions"]-raw["ghost"])),
            "independent_finite_action": {"epsilon": sizes, "predicted_quadratic": float(quadratic),
                                          "finite_action_quotients": approximations,
                                          "absolute_errors": [float(abs(a-quadratic)) for a in approximations]}},
        "massless_Maxwell_plus_Dirac_negative_control": maxwell_dirac_control(),
        "remaining_obligations": ["choose the native real action, adjoint and field integration domain",
                                  "decide hard H=Lambda/closure versus an independent soft HC integration; do not count both",
                                  "derive admissible gauge group, constraint measure and all ghost factors",
                                  "find an allowed background and a controlled elliptic/causal operator or a different valid quantization",
                                  "evaluate the actual bosonic and fermionic spectra and metric heat coefficients together",
                                  "supply physical scales, renormalization and vacuum-matching protection"],
        "main_TeX_changed": False,
        "sources": ["sources/research/parts/v470/10_sphaera_and_physics.tex: thm:variational-form, prop:equivalent-closure-criteria, thm:closed-master-system",
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
