"""Common-metric triadic Dirac stress and a local first-order Einstein--Dirac comparison.

No scalar matter is added. The native composite coframe, HC and closure are not imposed.
"""
import argparse
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "dirac_state_scalar_utilities", Path(__file__).with_name("HC_Quantum_State_Gravity.py"))
state = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(state)
parent, geometry, checks = state.parent, state.geometry, state.checks
ETA = geometry.ETA
WEIGHTS, BETA = geometry.spin_weights()
GAMMA = BETA @ WEIGHTS
GAMMA_LOWER = np.einsum("mn,nij->mij", ETA, GAMMA)


def dirac_data(psi, derivative, mass_operator, gamma=GAMMA, metric=ETA, spin=None):
    """Real symmetric Dirac action, its residual, symmetric stress and ordinary phase current."""
    psi = checks._finite(psi, "probe")
    derivative = checks._finite(derivative, "probe derivative")
    metric = state._metric(metric)
    mass_operator = checks._finite(mass_operator, "internal mass operator")
    gamma = checks._finite(gamma, "coordinate gamma matrices")
    if (psi.ndim != 2 or psi.shape[1] != 4 or derivative.shape != (4, *psi.shape)
            or mass_operator.shape != (len(psi), len(psi)) or gamma.shape != (4, 4, 4)
            or not np.allclose(mass_operator, mass_operator.conj().T, atol=1e-12, rtol=0)):
        raise ValueError("Compatible triadic/spin data and a Hermitian internal mass required")
    spin = np.zeros((4, 4, 4), complex) if spin is None else checks._finite(spin, "spin connection")
    if spin.shape != (4, 4, 4):
        raise ValueError("Four spin connection matrices required")
    covariant = derivative+np.einsum("rj,mkj->mrk", psi, spin)
    image = mass_operator @ psi
    residual = 1j*np.einsum("mrj,mkj->rk", covariant, gamma)-image
    bilinear = complex(np.vdot(psi, image @ BETA.T))
    kinetic_contraction = sum(np.vdot(psi, d @ (BETA @ g).T) for d, g in zip(covariant, gamma))
    lagrangian = float(-kinetic_contraction.imag-bilinear.real)
    lower = np.einsum("mn,nij->mij", metric, gamma)
    ordered = np.array([[np.vdot(psi, d @ (BETA @ g).T) for d in covariant] for g in lower])
    stress = (ordered+ordered.T).imag/2+metric*lagrangian
    current = np.array([np.vdot(psi, psi @ (BETA @ g).T).real for g in gamma])
    return {"covariant": covariant, "residual": residual, "lagrangian": lagrangian,
            "mass_bilinear": bilinear, "stress": stress,
            "trace": float(np.sum(np.linalg.inv(metric)*stress)), "current": current}


def bundle(coframe, first, second=None):
    """Torsion-free spin lift from the same coframe used in g and the coordinate gammas."""
    e = checks._real(coframe, (4, 4), "coframe")
    de = checks._real(first, (4, 4, 4), "coframe first jet")
    dde = np.zeros((4, 4, 4, 4)) if second is None else checks._real(second, (4, 4, 4, 4), "coframe second jet")
    inverse = np.linalg.inv(e)
    metric = e.T @ ETA @ e
    gfirst = np.array([d.T @ ETA @ e+e.T @ ETA @ d for d in de])
    gsecond = np.array([[dd.T @ ETA @ e+e.T @ ETA @ dd+de[r].T @ ETA @ de[s]+de[s].T @ ETA @ de[r]
                         for s, dd in enumerate(row)] for r, row in enumerate(dde)])
    curvature = geometry.metric_curvature(metric, gfirst, gsecond)
    christoffel = curvature["connection"]
    omega = np.array([ETA @ (e @ christoffel[:, mu, :]-de[mu]) @ inverse for mu in range(4)])
    spin = -np.einsum("mab,aij,bjk->mik", omega, GAMMA, GAMMA)/4
    gamma = np.einsum("ma,aij->mij", inverse, GAMMA)
    dinverse = -np.einsum("ma,lav,vb->lmb", inverse, de, inverse)
    dgamma = np.einsum("lma,aij->lmij", dinverse, GAMMA)
    compatibility = np.empty((4, 4, 4, 4), complex)
    for mu, nu in np.ndindex((4, 4)):
        compatibility[mu, nu] = (dgamma[mu, nu]+np.einsum("r,rij->ij", christoffel[nu, mu], gamma)
                                  +spin[mu] @ gamma[nu]-gamma[nu] @ spin[mu])
    return {"metric": metric, "first": gfirst, "second": gsecond, "curvature": curvature,
            "omega": omega, "spin": spin, "gamma": gamma, "gamma_first": dgamma,
            "gamma_compatibility": compatibility}


def linear_spin(first):
    first = np.asarray(first, complex)
    if first.shape != (4, 4, 4):
        raise ValueError("A metric first jet required")
    omega = np.array([[[(first[b, a, mu]-first[a, mu, b])/2 for b in range(4)]
                       for a in range(4)] for mu in range(4)])
    return -np.einsum("mab,aij,bjk->mik", omega, GAMMA, GAMMA)/4


def operator_change(psi, derivative, perturbation, first):
    """Coefficient D1[h] in (i Gamma(E).D(E)-M)=D0+epsilon D1+O(epsilon^2)."""
    psi, derivative = np.asarray(psi, complex), np.asarray(derivative, complex)
    h = np.asarray(perturbation, complex)
    if psi.shape != (4,) or derivative.shape != (4, 4) or h.shape != (4, 4):
        raise ValueError("One spinor, its first jet and a metric perturbation required")
    dgamma = -np.einsum("mr,ra,aij->mij", ETA, h, GAMMA)/2
    spin = linear_spin(first)
    return 1j*(np.einsum("mij,mj->i", dgamma, derivative)+np.einsum("mij,mjk,k->i", GAMMA, spin, psi))


def mode_family(phase=0.4):
    """Positive-energy spin modes in one eigenchannel of the PREVIOUS Hermitian triadic matrix."""
    phase = checks._scalar(phase, "relative phase")
    mass_operator = parent.background.triadic_mass()
    eigenvalues, eigenvectors = np.linalg.eigh(mass_operator)
    mass, internal = float(eigenvalues[-1]), eigenvectors[:, -1]
    energy, volume = np.sqrt(mass**2+1), (2*np.pi)**3
    momenta = np.array([[1, 0, 0], [0, 1, 0]])
    covectors = np.column_stack((-energy*np.ones(2), momenta))
    spinors = []
    for k in momenta:
        hamiltonian = np.einsum("i,ijk->jk", k, WEIGHTS[1:])+mass*BETA
        spinor = (np.eye(4)+hamiltonian/energy) @ np.eye(4)[0]/2
        spinors.append(spinor/np.linalg.norm(spinor))
    spinors = np.array(spinors)
    coefficients = np.array([np.sqrt(0.8), np.sqrt(0.2)*np.exp(1j*phase)])
    kernels = np.empty((2, 2, 4, 4), complex)
    for r, s in np.ndindex((2, 2)):
        b = np.array([np.vdot(spinors[r], BETA @ g @ spinors[s]) for g in GAMMA_LOWER])
        p = covectors[r]+covectors[s]
        kernels[r, s] = (np.outer(b, p)+np.outer(p, b))/4
    occupation = np.outer(coefficients.conj(), coefficients)
    diagonal = sum(occupation[r, r].real*kernels[r, r].real for r in range(2))/volume
    cross = occupation[0, 1]*kernels[0, 1]/volume
    beta_gram = spinors.conj() @ BETA @ spinors.T
    scalar_lower = (np.sum(abs(coefficients)**2*beta_gram.diagonal().real)
                    -2*abs(coefficients[0]*coefficients[1]*beta_gram[0, 1]))/volume
    return {"mass_operator": mass_operator, "mass": mass, "internal": internal,
            "energy": energy, "volume": volume, "momenta": momenta, "covectors": covectors,
            "spinors": spinors, "coefficients": coefficients, "occupation": occupation,
            "kernels": kernels, "diagonal_stress": diagonal, "cross_stress": cross,
            "mass_bilinear_lower_bound_all_phases": float(mass*scalar_lower)}


def probe_jets(point, phase=0.4):
    point = checks._real(point, (4,), "point")
    modes = mode_family(phase)
    amplitudes = (modes["coefficients"]*np.exp(1j*modes["covectors"] @ point)/np.sqrt(modes["volume"]))[:, None]*modes["spinors"]
    value = np.sum(amplitudes, axis=0)
    first = 1j*np.einsum("rm,ri->mi", modes["covectors"], amplitudes)
    second = -np.einsum("rm,rn,ri->mni", modes["covectors"], modes["covectors"], amplitudes)
    return modes, value, first, second


def homogeneous_bar_jets(point, stress):
    """A local Lorenz-gauge polynomial particular solution Box bar_h=-2 T, including Tr T."""
    x = checks._real(point, (4,), "point")
    t = checks._real(stress, (4, 4), "constant symmetric stress")
    if not np.allclose(t, t.T, atol=1e-12, rtol=0):
        raise ValueError("A symmetric source required")
    xl, tx = ETA @ x, t @ x
    square, contraction, trace = x @ ETA @ x, x @ t @ x, np.sum(ETA*t)
    bar = -t*square/4+ETA*contraction/4+trace*np.outer(xl, xl)/36-5*trace*ETA*square/72
    first = np.empty((4, 4, 4))
    second = np.empty((4, 4, 4, 4))
    for r in range(4):
        first[r] = (-t*xl[r]/2+ETA*tx[r]/2
                    +trace*(np.outer(ETA[:, r], xl)+np.outer(xl, ETA[:, r]))/36
                    -5*trace*ETA*xl[r]/36)
        for s in range(4):
            second[r, s] = (-t*ETA[r, s]/2+ETA*t[r, s]/2
                            +trace*(np.outer(ETA[:, r], ETA[:, s])+np.outer(ETA[:, s], ETA[:, r]))/36
                            -5*trace*ETA*ETA[r, s]/36)
    return bar, first, second


def trace_reverse(jets):
    return tuple(a-np.einsum("mn,...->...mn", ETA, np.einsum("mn,...mn->...", ETA, a))/2 for a in jets)


def metric_jets(point, phase=0.4):
    point = checks._real(point, (4,), "point")
    modes = mode_family(phase)
    q = modes["covectors"][1]-modes["covectors"][0]
    q_squared = float(q @ ETA @ q)
    cross = 2*modes["cross_stress"]*np.exp(1j*q @ point)/q_squared
    oscillatory = ((2*cross).real, 2*np.einsum("r,mn->rmn", 1j*q, cross).real,
                   -2*np.einsum("r,s,mn->rsmn", q, q, cross).real)
    homogeneous = homogeneous_bar_jets(point, modes["diagonal_stress"])
    bar = tuple(a+b for a, b in zip(homogeneous, oscillatory))
    return {"h": trace_reverse(bar), "bar_h": bar, "homogeneous_bar_h": homogeneous,
            "oscillatory_bar_h": oscillatory, "modes": modes}


def forcing_system(phase=0.4):
    """Closed polynomial/Fourier representation of the forced first-order Dirac equation."""
    modes = mode_family(phase)
    spatial_basis = sorted([v for v in itertools.product(range(3), repeat=3) if sum(v) <= 2], key=lambda v: (sum(v), v))
    zero, empty_first = np.zeros((4, 4)), np.zeros((4, 4, 4))
    hom_second = trace_reverse(homogeneous_bar_jets(np.zeros(4), modes["diagonal_stress"]))[2]
    forcing = {}

    def add(k, time_power, powers, vector):
        terms = forcing.setdefault(tuple(int(v) for v in k), {})
        key = (time_power, tuple(powers))
        terms[key] = terms.get(key, np.zeros(4, complex))+vector

    q = modes["covectors"][1]-modes["covectors"][0]
    hc = trace_reverse((2*modes["cross_stress"]/(q @ ETA @ q),))[0]
    for r in range(2):
        k, p = modes["momenta"][r], modes["covectors"][r]
        psi = modes["coefficients"][r]*modes["spinors"][r]/np.sqrt(modes["volume"])
        derivative = 1j*np.outer(p, psi)
        for rho in range(4):
            powers = [int(rho == j+1) for j in range(3)]
            change = operator_change(psi, derivative, zero, hom_second[:, rho])
            add(k, int(rho == 0), powers, -BETA @ change)
            for sigma in range(4):
                powers2 = [int(rho == j+1)+int(sigma == j+1) for j in range(3)]
                change = operator_change(psi, derivative, hom_second[rho, sigma]/2, empty_first)
                add(k, int(rho == 0)+int(sigma == 0), powers2, -BETA @ change)
        for sign in (1, -1):
            h = hc if sign == 1 else hc.conj()
            change = operator_change(psi, derivative, h, 1j*np.einsum("m,ij->mij", sign*q, h))
            add(k+sign*q[1:], 0, (0, 0, 0), -BETA @ change)
    systems = {}
    for k, terms in forcing.items():
        degree = max(sum(powers) for _, powers in terms)
        basis = [v for v in spatial_basis if sum(v) <= degree]
        size = 4*len(basis)
        hamiltonian = np.zeros((size, size), complex)
        b = np.zeros((size, 3), complex)
        for i, powers in enumerate(basis):
            hamiltonian[4*i:4*i+4, 4*i:4*i+4] = (np.einsum("i,ijk->jk", k, WEIGHTS[1:])
                                                               +modes["mass"]*BETA-modes["energy"]*np.eye(4))
            for j in range(3):
                if powers[j] > 0:
                    lower = tuple(v-int(l == j) for l, v in enumerate(powers))
                    target = basis.index(lower)
                    hamiltonian[4*target:4*target+4, 4*i:4*i+4] += -1j*powers[j]*WEIGHTS[j+1]
            for time_power in range(3):
                b[4*i:4*i+4, time_power] = terms.get((time_power, powers), np.zeros(4))
        generator = np.zeros((size+3, size+3), complex)
        generator[:size, :size], generator[:size, size:] = -1j*hamiltonian, -1j*b
        generator[size+1, size], generator[size+2, size+1] = 1, 2
        systems[k] = {"basis": basis, "generator": generator, "size": size, "forcing": b,
                      "hamiltonian": hamiltonian}
    return {"systems": systems, "modes": modes}


@lru_cache(maxsize=24)
def correction_flow(time, phase=0.4):
    """Use the installed mpmath matrix exponential, not a custom time integrator."""
    data = forcing_system(phase)
    result = {}
    for k, system in data["systems"].items():
        size = system["size"]
        if time == 0:
            vector = np.zeros(size+3, complex)
            vector[size] = 1
        else:
            with mp.workdps(25):
                exponential = mp.expm(mp.matrix(system["generator"].tolist())*time)
                vector = np.array([complex(exponential[i, size]) for i in range(size+3)])
        dot = system["generator"] @ vector
        result[k] = {"basis": system["basis"], "value": vector[:size].reshape(-1, 4),
                     "dot": dot[:size].reshape(-1, 4), "clock": vector[size:]}
    return result


def correction_jets(point, phase=0.4):
    point = checks._real(point, (4,), "point")
    modes = mode_family(phase)
    value, derivative = np.zeros(4, complex), np.zeros((4, 4), complex)
    for k, data in correction_flow(float(point[0]), float(phase)).items():
        factor = np.exp(-1j*modes["energy"]*point[0]+1j*np.array(k) @ point[1:])
        for powers, z, dz in zip(data["basis"], data["value"], data["dot"]):
            polynomial = np.prod(point[1:]**powers)
            value += factor*polynomial*z
            derivative[0] += factor*polynomial*(dz-1j*modes["energy"]*z)
            for j in range(3):
                pd = 0.0
                if powers[j] > 0:
                    reduced = tuple(v-int(l == j) for l, v in enumerate(powers))
                    pd = powers[j]*np.prod(point[1:]**reduced)
                derivative[j+1] += factor*(1j*k[j]*polynomial+pd)*z
    return value, derivative


def common_sample(point=(0.08, 0.2, -0.3, 0.1), phase=0.4, strength=0.01):
    """Fully evaluated equations of the declared local comparison, accurate only through first order."""
    modes, value, derivative, _ = probe_jets(point, phase)
    h, dh, ddh = metric_jets(point, phase)["h"]
    first_value, first_derivative = correction_jets(point, phase)
    coframe = np.eye(4)+strength*ETA @ h/2
    coframe_first = strength*np.einsum("ab,lbc->lac", ETA, dh)/2
    coframe_second = strength*np.einsum("ab,lsbc->lsac", ETA, ddh)/2
    geometric = bundle(coframe, coframe_first, coframe_second)
    psi = np.outer(modes["internal"], value+strength*first_value)
    dpsi = np.einsum("r,mi->mri", modes["internal"], derivative+strength*first_derivative)
    matter = dirac_data(psi, dpsi, modes["mass_operator"], geometric["gamma"], geometric["metric"], geometric["spin"])
    original = dirac_data(np.outer(modes["internal"], value),
                          np.einsum("r,mi->mri", modes["internal"], derivative), modes["mass_operator"])
    correction_residual = (1j*np.einsum("mij,mj->i", GAMMA, first_derivative)-modes["mass"]*first_value
                           +operator_change(value, derivative, h, dh))
    return {"modes": modes, "metric": geometric, "matter": matter, "zeroth_matter": original,
            "Einstein_residual": geometric["curvature"]["einstein"]-strength*matter["stress"],
            "linear_Einstein_residual": state.linearized_einstein(ddh)-original["stress"],
            "linear_Dirac_residual": correction_residual,
            "correction": first_value, "correction_first": first_derivative, "metric_coframe": coframe}


def old_background_test(point=(0.01, 0.02, -0.03, 0.01)):
    old = parent.evaluate_branch(point)
    bg, y = old["background"], old["coordinate_jets"]
    py = np.r_[0, old["profile"]["gradient"], 0]
    ppy = np.zeros((4, 4))
    ppy[1:3, 1:3] = old["profile"]["hessian"]
    p = y[1] @ py
    pp = old["theta"].T @ ppy @ old["theta"]+np.einsum("a,lsa->ls", py, y[2])
    transform = np.eye(4)+0.4*old["profile"]["amplitude"]*np.outer(geometry.L_VECTOR, geometry.N_COV)
    theta_first = y[2].transpose(0, 2, 1)
    theta_second = y[3].transpose(0, 1, 3, 2)
    ln = np.outer(geometry.L_VECTOR, geometry.N_COV)
    first = np.array([transform @ dt+0.4*dp*np.outer(geometry.L_VECTOR, geometry.N_COV) @ old["theta"]
                      for dt, dp in zip(theta_first, p)])
    second = np.array([[transform @ theta_second[r, s]+0.4*(pp[r, s]*ln @ old["theta"]
                         +p[r]*ln @ theta_first[s]+p[s]*ln @ theta_first[r]) for s in range(4)] for r in range(4)])
    geometric = bundle(old["coframe"], first, second)
    curved = dirac_data(bg["psi"], bg["derivatives"], bg["mass_operator"],
                        geometric["gamma"], geometric["metric"], geometric["spin"])
    reference = dirac_data(bg["psi"], bg["derivatives"], bg["mass_operator"])
    return {"reference": reference, "curved": curved, "bundle": geometric,
            "metric_first_error": geometric["first"]-old["metric_jets"]["first"],
            "metric_second_error": geometric["second"]-old["metric_jets"]["second"]}


def evaluate():
    point, phase = (0.08, 0.2, -0.3, 0.1), 0.4
    sample = common_sample(point, phase)
    levels = [common_sample(point, phase, strength=s) for s in (0.04, 0.02, 0.01)]
    old = old_background_test()
    modes, psi, derivative, _ = probe_jets(point, phase)
    full_psi = np.outer(modes["internal"], psi)
    full_d = np.einsum("r,mi->mri", modes["internal"], derivative)
    coframe = parent.background.coframe(full_psi, full_d, WEIGHTS)
    return {
        "status": "common-metric massive triadic Dirac comparison through first gravitational order; NOT native HC/closure/composite-coframe completion",
        "common_action": {
            "action": "integral sqrt|g(E)| [R/(2 epsilon)+i/2 (barPsi Gamma(E).D(E)Psi-D(E)barPsi Gamma(E)Psi)-barPsi M Psi]",
            "signature_and_Clifford": "eta=(-,+,+,+), {Gamma^a,Gamma^b}=-2 eta^ab, barPsi=Psi^dagger beta",
            "spin_lift": "omega_mu=eta (E GammaChristoffel_mu-partial_mu E) E^(-1); S_mu=-omega_mu,ab Gamma^a Gamma^b/4",
            "stress_on_shell": "T_mn=-i/4 [barPsi Gamma_m <->D_n Psi+barPsi Gamma_n <->D_m Psi]",
            "trace_on_shell": "Tr_g T=-barPsi M Psi; a pure-null Einstein geometry requires this bilinear to vanish",
            "no_added_scalar_field": True,
            "independent_metric_not_native_bilinear_constraint": True,
            "torsion_free_metric_not_independent_Einstein_Cartan_connection": True,
        },
        "prepared_triadic_carrier": {
            "matrix": modes["mass_operator"].tolist(), "chosen_mass_eigenvalue": modes["mass"],
            "internal_eigenvector": modes["internal"].tolist(), "positive_energy": modes["energy"],
            "mass_bilinear_lower_bound_for_all_relative_phases": modes["mass_bilinear_lower_bound_all_phases"],
            "not_the_original_polynomial_background_or_an_evaluated_native_C7_representation": True,
        },
        "old_polynomial_background": {
            "reference_Dirac_residual_norm": float(np.linalg.norm(old["reference"]["residual"])),
            "common_effective_metric_Dirac_residual_norm": float(np.linalg.norm(old["curved"]["residual"])),
            "reference_stress_trace": old["reference"]["trace"],
            "reference_mass_bilinear": old["reference"]["mass_bilinear"].real,
            "common_gamma_compatibility_error": float(np.linalg.norm(old["bundle"]["gamma_compatibility"])),
            "switching_the_gamma_and_spin_connection_does_not_leave_the_old_probe_on_shell": True,
        },
        "local_weak_gravity_construction": {
            "complete_source": "constant diagonal stress plus phase-dependent conserved Fourier interference",
            "homogeneous_particular_solution": "bar_h=-T x^2/4+eta (x.T.x)/4+tau x_lower x_lower/36-5 tau eta x^2/72, tau=Tr_eta T",
            "oscillatory_solution": "bar_h_osc=2 T_osc/Q^2, Q=q-p, Q^2=2",
            "probe_correction": "D0 Psi1=-D1[h] Psi0 with zero correction data at t=0; finite Fourier/polynomial forced system solved by mpmath.expm",
            "sample_linear_Einstein_residual_norm": float(np.linalg.norm(sample["linear_Einstein_residual"])),
            "sample_linear_Dirac_residual_norm": float(np.linalg.norm(sample["linear_Dirac_residual"])),
            "sample_nonzero_probe_correction_norm": float(np.linalg.norm(sample["correction"])),
            "strengths": [0.04, 0.02, 0.01],
            "nonlinear_Einstein_residual_norms": [float(np.linalg.norm(x["Einstein_residual"])) for x in levels],
            "nonlinear_Dirac_residual_norms": [float(np.linalg.norm(x["matter"]["residual"])) for x in levels],
            "local_polynomial_metric_not_periodic_or_asymptotically_flat": True,
            "only_first_order_not_an_exact_nonlinear_solution": True,
        },
        "native_readout_negative_control": {
            "flat_probe_bilinear_coframe_rank": int(np.linalg.matrix_rank(coframe, tol=1e-12)),
            "flat_probe_bilinear_coframe_time_column_norm": float(np.linalg.norm(coframe[:, 0])),
            "this_coframe_is_not_the_required_nondegenerate_zeroth_order_metric_coframe": True,
            "prior_same_frame_trace_exclusion_is_not_evaded": True,
        },
        "remaining_obligations": ["native C7/M16/HC/Yukawa/gauge/projector and composite-metric dictionary",
                                  "do not double-count probes already integrated out in the native effective action",
                                  "derive physical masses and coupling, quantum state, renormalized vacuum and stress fluctuation control",
                                  "higher gravitational orders, global initial/boundary conditions, normalization and stability"],
        "main_TeX_changed": False,
    }


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
