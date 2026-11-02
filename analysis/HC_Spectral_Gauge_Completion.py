"""Sourced maximal fixed-resonance gauge comparison, without channel-label locks.

This is not a native gauge-group, C7, physical mass or metric identification.
"""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "spectral_gauge_intertwiners", Path(__file__).with_name("HC_Triadic_Intertwiner_Classification.py"))
intertwiners = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(intertwiners)
factor = intertwiners.factor
source, checks, dirac = factor.source, factor.checks, factor.dirac
commutator, OMEGA, GAUGE = factor.commutator, factor.OMEGA, factor.GAUGE


def modal_basis(high_precision=False):
    with mp.workdps(60):
        r, root_two = mp.sqrt(mp.mpf("16.49")), mp.sqrt(2)
        mass = [mp.mpf(".6")-r, mp.mpf(".6"), mp.mpf(".6")+r]
        vectors = [[4/r/root_two, -mp.mpf(".7")/r, 4/r/root_two],
                   [mp.mpf(".7")/r/root_two, 4/r, mp.mpf(".7")/r/root_two],
                   [-1/root_two, mp.mpf(0), 1/root_two]]
        if high_precision:
            return mass, vectors
        return np.array([float(x) for x in mass]), np.array([[float(x) for x in row] for row in vectors])


def modal_projectors():
    _, vectors = modal_basis()
    return np.array([np.kron(np.eye(2), np.outer(x, x)) for x in vectors.T])


def spectral_projection(matrix):
    matrix = checks._finite(matrix, "six-dimensional matrix")
    if matrix.shape[-2:] != (6, 6):
        raise ValueError("A C2 tensor C3 matrix required")
    return sum(p @ matrix @ p for p in modal_projectors())


def cross_readout_operator():
    channel = np.zeros((3, 3))
    channel[0, 1] = 1
    return np.kron(np.eye(2), channel)


def readout_test():
    mass = np.kron(np.eye(2), factor.TRIAD)
    cross = cross_readout_operator()
    generator = modal_projectors()[0]
    unitary = np.eye(6)+(np.exp(0.4j)-1)*generator
    x, y = np.eye(6)[:, 0], np.eye(6)[:, 1]
    return {"resonance_only_dimension": intertwiners.commutant([mass])["dimension"],
            "resonance_and_fixed_cross_readout_dimension": intertwiners.commutant([mass, cross])["dimension"],
            "allowed_resonance_generator_commutator_norm": float(np.linalg.norm(commutator(generator, mass))),
            "same_generator_fixed_readout_commutator_norm": float(np.linalg.norm(commutator(generator, cross))),
            "fixed_readout_before": float(np.vdot(x, cross @ y).real),
            "fixed_readout_after": float(np.vdot(unitary @ x, cross @ (unitary @ y)).real),
            "covariantly_transformed_readout_after": float(np.vdot(unitary @ x, unitary @ cross @ unitary.conj().T @ (unitary @ y)).real),
            "source": "12_structural_core.tex, Cross-bilinear geometry channel: Re(bar Psi_ART Gamma^a D_mu Psi_QFT), with probes exchanged",
            "state_independent_fixed_observable_invariance_is_a_condition_not_yet_a_native_gauge_law": True}


def initial_modes():
    _, vectors = modal_basis()
    return np.column_stack((0.5*vectors[0], 0.1*vectors[0], np.zeros(3), np.full(3, 0.03)))


def rhs(state):
    y = checks._real(state, (3, 4), "three modal (u,v,a,a') states")
    mass, _ = modal_basis()
    u, v, a, electric = y.T
    return np.column_stack(((OMEGA-a+mass)*v, (mass-OMEGA+a)*u,
                            electric, -GAUGE*GAUGE*(u*u+v*v)))


def jacobian(state):
    y = checks._real(state, (3, 4), "modal states")
    mass, _ = modal_basis()
    result = np.zeros((12, 12))
    for i, ((u, v, a, electric), m) in enumerate(zip(y, mass)):
        result[4*i:4*i+4, 4*i:4*i+4] = [[0, OMEGA-a+m, -v, 0],
                                                [m-OMEGA+a, 0, u, 0],
                                                [0, 0, 0, 1],
                                                [-2*GAUGE*GAUGE*u, -2*GAUGE*GAUGE*v, 0, 0]]
    return result


@lru_cache(maxsize=8)
def coefficients(order=32):
    if isinstance(order, bool) or not isinstance(order, int) or not 2 <= order <= 80:
        raise ValueError("Taylor order between 2 and 80 required")
    with mp.workdps(60):
        masses, vectors = modal_basis(high_precision=True)
        omega, gauge = mp.mpf(str(OMEGA)), mp.mpf(str(GAUGE))
        all_modes = []
        for i, mass in enumerate(masses):
            initial = [mp.mpf(".5")*vectors[0][i], mp.mpf(".1")*vectors[0][i], mp.mpf(0), mp.mpf(".03")]
            c = [[x]+[mp.mpf(0)]*order for x in initial]

            def product(a, b, n):
                return sum(c[a][k]*c[b][n-k] for k in range(n+1))

            for n in range(order):
                values = [(omega+mass)*c[1][n]-product(2, 1, n),
                          (mass-omega)*c[0][n]+product(2, 0, n), c[3][n],
                          -gauge*gauge*(product(0, 0, n)+product(1, 1, n))]
                for row, value in zip(c, values):
                    row[n+1] = value/(n+1)
            all_modes.append(tuple(tuple(row) for row in c))
        return tuple(all_modes)


def series_jet(z=0.02, order=32, high_precision=False):
    z = checks._scalar(z, "local normal coordinate")
    if abs(z) > 0.03:
        raise ValueError("Only the proved |z|<=.03 comparison interval is evaluated")
    with mp.workdps(60):
        z = mp.mpf(str(z))
        jets = [[], [], []]
        for mode in coefficients(order):
            values = [[], [], []]
            for row in mode:
                polynomials = [row, [i*row[i] for i in range(1, len(row))],
                               [i*(i-1)*row[i] for i in range(2, len(row))]]
                for value, polynomial in zip(values, polynomials):
                    value.append(mp.polyval(list(reversed(polynomial)), z))
            for result, value in zip(jets, values):
                result.append(value)
        return jets if high_precision else tuple(np.array([[float(x) for x in row] for row in value]) for value in jets)


def series_defect(z=0.02, order=32):
    with mp.workdps(60):
        masses, _ = modal_basis(high_precision=True)
        y, dy, _ = series_jet(z, order, high_precision=True)
        result = []
        for m, (u, v, a, electric), derivative in zip(masses, y, dy):
            target = [(mp.mpf(".9")-a+m)*v, (m-mp.mpf(".9")+a)*u,
                      electric, -mp.mpf(".64")*(u*u+v*v)]
            result.extend(abs(x-t) for x, t in zip(derivative, target))
        return float(max(result))


def existence_box():
    initial = initial_modes()
    mass, _ = modal_basis()
    umax, vmax = abs(initial[:, 0])+0.1, abs(initial[:, 1])+0.1
    plus, minus = abs(OMEGA+mass)+0.1, abs(mass-OMEGA)+0.1
    bounds = np.column_stack((plus*vmax, minus*umax, np.full(3, 0.13),
                              GAUGE*GAUGE*(umax*umax+vmax*vmax)))
    lipschitz = float(max(np.max(plus+vmax), np.max(minus+umax),
                          1, np.max(2*GAUGE*GAUGE*(umax+vmax))))
    return {"lower": (initial-0.1).tolist(), "upper": (initial+0.1).tolist(),
            "rhs_abs_bounds": bounds.tolist(), "Jacobian_infinity_norm_bound": lipschitz,
            "interval": 0.03, "available_box_radius": 0.1,
            "max_displacement_bound": float(0.03*np.max(bounds)), "Picard_contraction_bound": 0.03*lipschitz}


def spatial_integrals(state):
    y = checks._real(state, (3, 4), "modal states")
    mass, _ = modal_basis()
    u, v, a, electric = y.T
    return -(OMEGA-a)*(u*u+v*v)+mass*(u*u-v*v)+electric*electric/(2*GAUGE*GAUGE)


def field_data(point=(0.4, 0.9, 0.4, 0.02), radius=1.0, eta=0.7):
    point = checks._real(point, (4,), "product coordinates")
    t, theta, phi, z = point
    state, first, second = series_jet(z)
    radius, _ = source.load.flux._scale(radius, 1)
    eta = checks._scalar(eta, "closure coupling")
    _, rotation = modal_basis()
    base = source.load.flux.sphere_data(theta, phi)
    p0, dp0 = base["P"], base["P_first"]
    p, dp = np.kron(p0, np.eye(3)), np.array([np.kron(x, np.eye(3)) for x in dp0])
    a = rotation @ np.diag(state[:, 2]) @ rotation.T
    electric = rotation @ np.diag(state[:, 3]) @ rotation.T
    unitary = np.array([np.kron(x, np.eye(3)) for x in base["connection"]])
    derivative = np.array([[np.kron(x, np.eye(3)) for x in row] for row in base["connection_first"]])
    unitary[0] += 1j*np.kron(p0, a)
    derivative[:, 0] += 1j*np.array([np.kron(x, a) for x in dp0])
    derivative[3, 0] += 1j*np.kron(p0, electric)
    axis = source.dynamics.AXIS
    connection = unitary+eta*axis[:, None, None]*(np.eye(6)-p)
    dconnection = derivative-eta*dp[:, None]*axis[None, :, None, None]
    angular = np.array([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)])
    dangular = np.zeros((4, 2), complex)
    dangular[1], dangular[2] = [-np.sin(theta/2)/2, np.exp(1j*phi)*np.cos(theta/2)/2], [0, 1j*angular[1]]
    phase = np.exp(-1j*(OMEGA*t+phi/2))
    chi = np.zeros((3, 4), complex)
    chi[:, 1], chi[:, 3] = phase*(rotation @ state[:, 0]), 1j*phase*(rotation @ state[:, 1])
    dchi = np.zeros((4, 3, 4), complex)
    dchi[0], dchi[2] = -1j*OMEGA*chi, -0.5j*chi
    dchi[3, :, 1], dchi[3, :, 3] = phase*(rotation @ first[:, 0]), 1j*phase*(rotation @ first[:, 1])
    psi = np.einsum("a,bs->abs", angular, chi).reshape(6, 4)
    dpsi = (np.einsum("ma,bs->mabs", dangular, chi)+np.einsum("a,mbs->mabs", angular, dchi)).reshape(4, 6, 4)
    bundle = source.product_spin_bundle(theta, radius)
    currents = source.probe.probe_currents(psi, dirac.BETA @ bundle["gamma"], dirac.BETA)
    return {"P": p, "P_first": dp, "unitary": unitary, "connection": connection,
            "connection_first": dconnection, "F": checks.connection_curvature(connection, dconnection),
            "psi": psi, "psi_first": dpsi, "current": currents["gauge"], "scalar": currents["scalar"],
            "mass_operator": np.kron(np.eye(2), factor.TRIAD), "bundle": bundle,
            "state": state, "state_first": first, "state_second": second,
            "potential_channel_matrix": a, "point": point, "radius": radius}


def residuals(point=(0.4, 0.9, 0.4, 0.02), step=1e-5, **kwargs):
    step = checks._scalar(step, "coordinate derivative step")
    if step <= 0:
        raise ValueError("Positive coordinate derivative step required")
    d = field_data(point, **kwargs)
    inverse = source.load.inverse_metric(d["point"][1], d["radius"])
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["F"]
    resonance = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    divergence = np.sum(commutator(d["unitary"], d["current"]), axis=0)
    volume = d["radius"]**2*np.sin(d["point"][1])
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = field_data(d["point"]+sign*step*direction, **kwargs)
            inv = source.load.inverse_metric(other["point"][1], d["radius"])
            density = d["radius"]**2*np.sin(other["point"][1])
            samples.append((density*inv[mu]*inv[:, None, None]*other["F"][mu], density*other["current"][mu]))
        resonance += (samples[0][0]-samples[1][0])/(2*step*volume)
        divergence += (samples[0][1]-samples[1][1])/(2*step*volume)
    lower = np.einsum("mn,nij->mij", d["bundle"]["metric"], d["current"])
    full = resonance/inverse[:, None, None]-1j*GAUGE*GAUGE*lower
    probe = dirac.dirac_data(d["psi"], d["psi_first"]+d["connection"] @ d["psi"], d["mass_operator"],
                            gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])["residual"]
    return {"Dirac": probe, "spectral_gauge": spectral_projection(full),
            "spectral_current_divergence": spectral_projection(divergence),
            "full_Ward": divergence+1j*commutator(d["mass_operator"], d["scalar"]),
            "unprojected_U6_equation_not_imposed": full}


def evaluate():
    d, r = field_data(), residuals()
    old = factor.residuals()
    y = d["state"]
    modal_density = y[:, 0]**2+y[:, 1]**2
    masses, _ = modal_basis()
    equal = np.tile([0.5/np.sqrt(3), 0.1/np.sqrt(3), 0, 0.03], (3, 1))
    equal_first = rhs(equal)
    return {
        "status": "local maximal fixed-resonance centralizer comparison without fixed channel labels; NOT native gauge selection, C7, physical masses or metric backreaction",
        "gauge_field_space": {"algebra": "u(2) direct sum u(2) direct sum u(2), the maximal unitary commutant of I2 tensor prepared triad",
                              "projection": "Pi_Omega(X)=sum_r (I2 tensor q_r) X (I2 tensor q_r)",
                              "fixed_channel_projectors_not_required": True,
                              "maximal_compatible_algebra_is_a_declared_choice_not_the_native_gauge_group": True},
        "common_truncation_test": {"old_common_gauge_residual": float(np.linalg.norm(old["projected_gauge"])),
                                   "extra_spectral_gauge_residual": float(np.linalg.norm(spectral_projection(old["unprojected_equation_not_imposed"]))),
                                   "consistency_condition": "a_r=a for every spectral block requires rho_r=sum rho/3 pointwise when all blocks have the same full-trace coupling",
                                   "equal_initial_density_not_sufficient": True,
                                   "equal_density_first_derivatives": (2*np.sum(equal[:, :2]*equal_first[:, :2], axis=1)).tolist(),
                                   "source_covariance_is_not_source_invariance_and_does_not_select_a_gauge_group": True},
        "native_cross_readout_gate": readout_test(),
        "local_completion": {"ODEs": "u_r'=(omega-a_r+m_r)v_r; v_r'=(m_r-omega+a_r)u_r; a_r''=-g_full^2 rho_r",
                             "trace": "each spectral projector has rank one in channel space; each block has 1/g_full^2, not 3/g_full^2",
                             "same_initial_probe_potentials_and_electric_fields_as_common_branch": True,
                             "initial_modal_states": initial_modes().tolist(), "signed_resonance_eigenvalues": masses.tolist(),
                             "point": d["point"].tolist(), "modal_states": y.tolist(), "modal_densities": modal_density.tolist(),
                             "potential_splitting_norm": float(np.linalg.norm(y[:, 2]-np.mean(y[:, 2]))),
                             "potential_commutator_with_resonance_norm": float(np.linalg.norm(commutator(d["potential_channel_matrix"], factor.TRIAD))),
                             "potential_commutator_with_channel_label_norm": float(np.linalg.norm(commutator(d["potential_channel_matrix"], np.diag([1, 0, 0])))),
                             "full_matrix_residual_norms": {name: float(np.linalg.norm(value)) for name, value in r.items()},
                             "local_existence_bounds": existence_box(),
                             "ODE_defect_at_interval_edge": series_defect(0.03),
                             "spatial_first_integrals": spatial_integrals(y).tolist()},
        "remaining_obligations": ["identify native resonance/gauge/readout algebra and C7 embedding rather than either chosen comparison algebra",
                                  "the source forces different connection responses if the larger algebra is gauged; it does not remove those gauge directions",
                                  "signed finite resonance values are not measured masses, generations or tachyon-frame assignments",
                                  "hard-dependent HC, real action/source dictionary, product metric and separated spin/internal curvature remain assumptions",
                                  "global finite energy, causal/temporal stability, bilinear metric and metric/axis response remain unsolved"],
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
