"""Conditional channel-intertwiner classification and local-frame covariance.

Neither fixed channel projectors nor the numerical links are native C7 data.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "classified_triadic_factorization", Path(__file__).with_name("HC_Triadic_Gauge_Factorization.py"))
factor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(factor)
checks, dirac, commutator = factor.checks, factor.dirac, factor.commutator
PAULI = factor.source.transport.PAULI


def hermitian_basis(size):
    if isinstance(size, bool) or not isinstance(size, int) or not 1 <= size <= 12:
        raise ValueError("Positive finite carrier size at most 12 required")
    basis = [np.diag(np.eye(size)[i]).astype(complex) for i in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            entry = np.zeros((size, size), complex)
            entry[i, j] = entry[j, i] = 1/np.sqrt(2)
            basis.append(entry)
            basis.append(1j*(np.triu(entry)-np.tril(entry)))
    return np.array(basis)


def commutant(operators):
    operators = [checks._finite(x, "fixed operator") for x in operators]
    if (not operators or operators[0].ndim != 2 or operators[0].shape[0] == 0
            or operators[0].shape[0] != operators[0].shape[1]
            or any(x.shape != operators[0].shape for x in operators)):
        raise ValueError("Nonempty list of compatible square fixed operators required")
    basis = hermitian_basis(operators[0].shape[0])
    columns = []
    for candidate in basis:
        residual = np.concatenate([commutator(candidate, x).ravel() for x in operators])
        columns.append(np.r_[residual.real, residual.imag])
    linear = np.column_stack(columns)
    _, singular, vh = np.linalg.svd(linear, full_matrices=False)
    threshold = 1e-10*max(1, singular[0])
    rank = int(np.sum(singular > threshold))
    kernel = np.einsum("ab,bij->aij", vh[rank:], basis)
    residual = max((np.linalg.norm(commutator(x, op)) for x in kernel for op in operators), default=0)
    return {"basis": kernel, "dimension": len(kernel), "max_basis_residual": float(residual),
            "singular_values": singular, "numerical_rank_threshold": float(threshold)}


def channel_projectors(size=2):
    hermitian_basis(size)
    return np.array([np.kron(np.diag(np.eye(3)[i]), np.eye(size)) for i in range(3)])


def coupled_operator(first=None, second=None, direct=None):
    first = 4*np.eye(2) if first is None else checks._finite(first, "first link")
    second = 0.7*np.eye(2) if second is None else checks._finite(second, "second link")
    if (first.ndim != 2 or first.shape[0] == 0 or first.shape[0] != first.shape[1]
            or second.shape != first.shape):
        raise ValueError("Square equal-size comparison links required")
    size = first.shape[0]
    direct = np.zeros_like(first) if direct is None else checks._finite(direct, "direct link")
    if direct.shape != first.shape:
        raise ValueError("Compatible optional direct link required")
    result = 0.6*np.eye(3*size, dtype=complex)
    result[:size, 2*size:] = first
    result[size:2*size, 2*size:] = second
    result[:size, size:2*size] = direct
    result = result+result.conj().T-np.diag(np.diag(result))
    return result


def classify(first=None, second=None, direct=None, lock_channels=True):
    if not isinstance(lock_channels, bool):
        raise ValueError("Explicit fixed-channel-lock choice required")
    omega = coupled_operator(first, second, direct)
    operators = [omega]
    if lock_channels:
        operators.extend(channel_projectors(len(omega)//3))
    return commutant(operators)


def root_obstructions(first, second, direct=None):
    first, second = (checks._finite(x, "invertible link") for x in (first, second))
    coupled_operator(first, second, direct)
    if min(np.linalg.svd(first, compute_uv=False)[-1], np.linalg.svd(second, compute_uv=False)[-1]) < 1e-10:
        raise ValueError("Root reduction requires invertible links; use full constraints for kernels")
    result = [first.conj().T @ first, second.conj().T @ second]
    if direct is not None:
        result.append(np.linalg.solve(first, direct @ second))
    return result


def reference_cases():
    identity = np.eye(2)
    rotation = np.array([[1, -1], [1, 1]])/np.sqrt(2)
    phase = np.diag(np.exp(1j*np.array([0.3, -0.3])))
    return {
        "scalar_tree_locked": classify(),
        "same_resonance_without_channel_locks": classify(lock_channels=False),
        "one_anisotropic_link": classify(np.diag([4, 2]), 0.7*identity),
        "two_noncommuting_link_grams": classify(np.diag([4, 2]), rotation @ np.diag([0.7, 0.3]) @ rotation.T),
        "scalar_cycle_phase": classify(direct=0.2*np.exp(0.3j)*identity),
        "matrix_cycle_phase": classify(direct=0.2*phase),
        "rank_deficient_first_link": classify(np.diag([4, 0]), 0.7*identity),
        "disconnected_first_channel": classify(np.zeros((2, 2)), 0.7*identity)}


def local_frame_jet(point):
    """Independent channel bases, not extra elements of the original common gauge group."""
    point = checks._real(point, (4,), "product coordinates")
    s, ds, dds = np.zeros((6, 6), complex), np.zeros((4, 6, 6), complex), np.zeros((4, 4, 6, 6), complex)
    entries = [(0, 0.4, PAULI[0]), (3, 0.7, PAULI[2]), (0, 0.0, np.eye(2))]
    for channel, (mu, rate, generator) in enumerate(entries):
        angle = rate*point[mu]
        unitary = np.cos(angle)*np.eye(2)+1j*np.sin(angle)*generator
        selector = np.diag(np.eye(3)[channel])
        s += np.kron(unitary, selector)
        ds[mu] += np.kron(1j*rate*generator @ unitary, selector)
        dds[mu, mu] += np.kron(-rate*rate*unitary, selector)
    return s, ds, dds


def framed_data(point=(0.4, 0.9, 0.4, 0.02), connection_shift=True, rotate_mass=True, **kwargs):
    if not isinstance(connection_shift, bool) or not isinstance(rotate_mass, bool):
        raise ValueError("Explicit frame-transformation choices required")
    d = factor.field_data(point, **kwargs)
    s, ds, dds = local_frame_jet(point)
    dagger, dd = s.conj().T, ds.conj().swapaxes(-1, -2)
    b = s @ d["connection"] @ dagger
    db = np.array([[ds[mu] @ d["connection"][nu] @ dagger
                    +s @ d["connection_first"][mu, nu] @ dagger
                    +s @ d["connection"][nu] @ dd[mu] for nu in range(4)] for mu in range(4)])
    if connection_shift:
        b -= ds @ dagger
        db -= dds @ dagger+np.einsum("nij,mjk->mnik", ds, dd)
    p = s @ d["P"] @ dagger
    dp = ds @ d["P"] @ dagger+s @ d["P_first"] @ dagger+s @ d["P"] @ dd
    mass = s @ d["mass_operator"] @ dagger if rotate_mass else d["mass_operator"]
    return {"base": d, "S": s, "S_first": ds, "P": p, "P_first": dp,
            "connection": b, "connection_first": db, "F": checks.connection_curvature(b, db),
            "psi": s @ d["psi"], "psi_first": ds @ d["psi"]+s @ d["psi_first"],
            "mass_operator": mass, "current": s @ d["current"] @ dagger,
            "scalar": s @ d["scalar"] @ dagger}


def framed_projection(matrix, frame):
    frame = checks._finite(frame, "unitary frame")
    if frame.shape != (6, 6) or not np.allclose(frame.conj().T @ frame, np.eye(6), atol=1e-12, rtol=0):
        raise ValueError("A unitary six-dimensional frame required")
    return frame @ factor.gauge_projection(frame.conj().T @ matrix @ frame) @ frame.conj().T


def frame_checks(point=(0.4, 0.9, 0.4, 0.02), step=1e-5, **kwargs):
    step = checks._scalar(step, "coordinate derivative step")
    if step <= 0:
        raise ValueError("Positive coordinate derivative step required")
    d = framed_data(point, **kwargs)
    base, s = d["base"], d["S"]
    inverse = factor.source.load.inverse_metric(base["point"][1], base["radius"])
    raised = inverse[:, None, None, None]*inverse[None, :, None, None]*d["F"]
    divergence = np.sum(commutator(d["connection"][:, None], raised), axis=0)
    volume = base["radius"]**2*np.sin(base["point"][1])
    for mu, direction in enumerate(np.eye(4)):
        samples = []
        for sign in (1, -1):
            other = framed_data(base["point"]+sign*step*direction, **kwargs)
            inv = factor.source.load.inverse_metric(other["base"]["point"][1], base["radius"])
            density = base["radius"]**2*np.sin(other["base"]["point"][1])
            samples.append(density*inv[mu]*inv[:, None, None]*other["F"][mu])
        divergence += (samples[0]-samples[1])/(2*step*volume)
    current_lower = np.einsum("mn,nij->mij", base["bundle"]["metric"], d["current"])
    full = divergence/inverse[:, None, None]-1j*factor.GAUGE**2*current_lower
    probe = dirac.dirac_data(d["psi"], d["psi_first"]+d["connection"] @ d["psi"], d["mass_operator"],
                            gamma=base["bundle"]["gamma"], metric=base["bundle"]["metric"],
                            spin=base["bundle"]["spin"])["residual"]
    return {"Dirac": probe, "projected_gauge": framed_projection(full, s),
            "curvature_covariance": d["F"]-s @ base["F"] @ s.conj().T,
            "projector_transport": d["P_first"]+commutator(d["connection"], d["P"])}


def evaluate():
    cases = reference_cases()
    cycle_zero = coupled_operator(direct=0.2*np.eye(2))
    cycle_quarter = coupled_operator(direct=0.2j*np.eye(2))
    checks_correct = frame_checks()
    missing_connection = frame_checks(connection_shift=False)
    frozen_mass = frame_checks(rotate_mass=False)
    return {
        "status": "conditional fixed-link/readout classification and simultaneous local basis change; NOT native gauge charges, C7 embedding or a new physical frame effect",
        "native_audit": {"actual_T_i_and_T_i_perp_entries_not_supplied_in_probe_block": True,
                         "source": "10_sphaera_and_physics.tex prop:triadic-two-probe; 12_structural_core.tex sec:theorem7; 16_master_model.tex prop:structural-matter-gauge-mass",
                         "readouts_in_source_are_general_maps_not_fixed_orthogonal_channel_projectors": True,
                         "fixed_readout_locks_are_an_additional_hypothesis": True},
        "relative_representation_theorem": "A nonzero fixed equivariant link between irreducible complex unitary representations is a positive scale times a unitary intertwiner; connected channels are equivalent, not necessarily written in the same basis",
        "invertible_link_reduction": "At root T0=T0^dagger, require [T0,K1^dagger K1]=[T0,K2^dagger K2]=0 and, if present, [T0,K1^{-1}K12 K2]=0; Ti=Ki T0 Ki^{-1}",
        "finite_reference_dimensions": {name: {"real_Hermitian_dimension": value["dimension"],
                                              "max_basis_commutator_residual": value["max_basis_residual"]}
                                        for name, value in cases.items()},
        "scalar_cycle_spectral_control": {
            "same_common_algebra_dimension": 4,
            "spectrum_difference_norm": float(np.linalg.norm(np.linalg.eigvalsh(cycle_zero)-np.linalg.eigvalsh(cycle_quarter))),
            "trace_cube_difference": float(np.trace(cycle_zero @ cycle_zero @ cycle_zero
                                                     -cycle_quarter @ cycle_quarter @ cycle_quarter).real),
            "not_a_simultaneous_basis_change_or_a_physical_mass_identification": True},
        "local_basis_checks": {"frame": "S=sum_i Ui(x) tensor |i><i|, U_ART=exp(.4 i t sigma1), U_QFT=exp(.7 i z sigma3), U_perp=I",
                               "connection": "B'=S B S^dagger-(partial S)S^dagger; Omega', P', Psi' and the gauge embedding all transformed",
                               "correct_residual_norms": {name: float(np.linalg.norm(value)) for name, value in checks_correct.items()},
                               "missing_connection_shift_Dirac_residual": float(np.linalg.norm(missing_connection["Dirac"])),
                               "untransformed_mass_Dirac_residual": float(np.linalg.norm(frozen_mass["Dirac"])),
                               "not_independent_physical_gauge_transformations_of_the_original_fixed_embedding": True},
        "limits": ["same absolute charge and the actual gauge group are not determined by this commutant calculation",
                   "kernel/disconnected sectors need not inherit the connected representation",
                   "scalar phase/gain changes do not reduce the locked common algebra; noncentral loop maps or anisotropic link grams can",
                   "a scalar cycle phase can nevertheless change the resonance spectrum; algebra invariance is not spectral invariance",
                   "position-dependent basis changes require connection and gauge-embedding transport; they do not derive the paper's physical frame shifts",
                   "all cases are finite comparisons, not evaluated native intertwiners, physical masses or gravitational closure"],
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
