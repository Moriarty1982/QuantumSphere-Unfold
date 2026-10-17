"""Full-triad coframe, cross-readout covariance and intrinsic matrix diagnostics.

No native coframe is replaced, and the prescribed product metric is not induced.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "geometry_spectral_completion", Path(__file__).with_name("HC_Spectral_Gauge_Completion.py"))
spectral = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(spectral)
factor, checks, dirac = spectral.factor, spectral.checks, spectral.dirac
ETA = np.diag([-1.0, 1, 1, 1])


def covariant_jet(data):
    return (data["psi_first"]+data["connection"] @ data["psi"]
            +np.einsum("rj,mkj->mrk", data["psi"], data["bundle"]["spin"]))


def pairing(psi, derivative, selector=None):
    psi = checks._finite(psi, "internal-by-spin probe")
    derivative = checks._finite(derivative, "full covariant probe jet")
    if psi.ndim != 2 or psi.shape[1] != 4 or derivative.shape != (4, *psi.shape):
        raise ValueError("Four-spin probe and four matching covariant derivatives required")
    selector = np.eye(len(psi)) if selector is None else checks._finite(selector, "internal readout selector")
    if selector.shape != (len(psi), len(psi)):
        raise ValueError("Compatible internal readout selector required")
    return np.array([[np.vdot(psi, (selector @ value) @ weight.T) for value in derivative]
                     for weight in dirac.WEIGHTS])


def geometry(psi, derivative, selector=None):
    frame = pairing(psi, derivative, selector).real
    singular = np.linalg.svd(frame, compute_uv=False)
    metric = frame.T @ ETA @ frame
    return {"coframe": frame, "singular_values": singular, "metric": metric,
            "coframe_rank_at_1e_minus_10": int(np.sum(singular > 1e-10)),
            "metric_eigenvalues": np.linalg.eigvalsh(metric)}


def gauge_unitary(angle=0.4):
    angle = checks._scalar(angle, "spectral gauge phase")
    return np.eye(6)+(np.exp(1j*angle)-1)*spectral.modal_projectors()[0]


def fixed_selector_algebras():
    projectors = spectral.modal_projectors()
    rotations = [np.eye(2), *spectral.intertwiners.PAULI]
    common = [np.kron(x, np.eye(3)) for x in rotations]
    maximal = [p @ x for p in projectors for x in common]
    return {"common": spectral.intertwiners.commutant(common),
            "spectral": spectral.intertwiners.commutant(maximal)}


def pair_tensors(current):
    current = checks._finite(current, "matrix four-current")
    if current.shape != (4, 6, 6):
        raise ValueError("Four compatible six-dimensional current matrices required")
    result = np.empty((3, 3, 4, 4), complex)
    for a, p in enumerate(spectral.modal_projectors()):
        for b, q in enumerate(spectral.modal_projectors()):
            for mu in range(4):
                for nu in range(4):
                    result[a, b, mu, nu] = np.trace(p @ current[mu] @ q @ current[nu])
    return result


def loop_tensor(current):
    current = checks._finite(current, "matrix four-current")
    if current.shape != (4, 6, 6):
        raise ValueError("Four compatible six-dimensional current matrices required")
    p, q, r = spectral.modal_projectors()
    return np.array([[[np.trace(p @ x @ q @ y @ r @ z) for z in current]
                      for y in current] for x in current])


def complex_loop_control():
    _, rotation = spectral.modal_basis()
    spins = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1j, 0, 0]], complex)
    spins[1:] /= np.sqrt(2)
    psi = sum(np.outer(np.kron([1, 0], rotation[:, i]), spin) for i, spin in enumerate(spins))
    return factor.source.probe.probe_currents(psi, dirac.WEIGHTS, dirac.BETA)["gauge"]


def full_rank_cross_control():
    # Free point jets test the observable, not the Dirac or connection equations.
    psi, derivative = np.zeros((6, 4), complex), np.zeros((4, 6, 4), complex)
    psi[0, 0] = 1
    derivative[0, 1, 0], derivative[1, 1, 3] = 1, 1
    derivative[2, 1, 3], derivative[3, 1, 2] = 1j, 1
    return psi, derivative


def evaluate():
    d = spectral.field_data()
    covariant = covariant_jet(d)
    g = gauge_unitary()
    cross = spectral.cross_readout_operator()
    before = geometry(d["psi"], covariant)
    after = geometry(g @ d["psi"], g @ covariant)
    psi, derivative = full_rank_cross_control()
    bare = geometry(psi, derivative, cross)
    bare_changed = geometry(g @ psi, g @ derivative, cross)
    transported = geometry(g @ psi, g @ derivative, g @ cross @ g.conj().T)
    pair, loop = pair_tensors(d["current"]), loop_tensor(d["current"])
    transformed = g @ d["current"] @ g.conj().T
    complex_control = complex_loop_control()
    algebras = fixed_selector_algebras()
    mass, _ = spectral.modal_basis()
    y, dy = d["state"], d["state_first"]
    rho_first = 2*np.sum(y[:, 0]*dy[:, 0]+y[:, 1]*dy[:, 1])
    real_frame_target = np.zeros((4, 4))
    real_frame_target[0, 3] = rho_first/2
    return {
        "status": "full-triad metric/readout audit and candidate internal-gauge invariants; NOT induced product geometry, a new native readout law or quantum coherence certification",
        "native_source_distinction": {
            "metric_source": "10_sphaera_and_physics.tex prop:bilinear-einstein-reconstruction: E from the complete Psi_triangle, no fixed ART/QFT selector",
            "cross_source": "12_structural_core.tex Cross-bilinear geometry channel: additional ART/QFT mixed readout with heuristic focusing functional",
            "full_metric_alone_does_not_force_common_internal_gauge_factor": True},
        "full_coframe_on_spectral_solution": {
            "coframe": before["coframe"].tolist(), "singular_values": before["singular_values"].tolist(),
            "rank": before["coframe_rank_at_1e_minus_10"], "metric": before["metric"].tolist(),
            "invariant_coframe_residual": float(np.linalg.norm(after["coframe"]-before["coframe"])),
            "invariant_metric_residual": float(np.linalg.norm(after["metric"]-before["metric"])),
            "analytic_rank_one_residual": float(np.linalg.norm(before["coframe"]-real_frame_target)),
            "rho_first": float(rho_first), "two_sum_m_uv": float(2*np.sum(mass*y[:, 0]*y[:, 1])),
            "prescribed_metric_rank": int(np.linalg.matrix_rank(d["bundle"]["metric"])),
            "prescribed_metric_is_not_the_reconstructed_metric": True},
        "fixed_bilinear_selector_classification": {
            "Hermitian_selectors_invariant_under_common_factor": algebras["common"]["dimension"],
            "Hermitian_selectors_invariant_under_maximal_spectral_factor": algebras["spectral"]["dimension"],
            "spectral_result": "R=sum_r c_r (I2 tensor q_r); fixed bilinear inter-mode selectors are not invariant"},
        "bare_cross_metric_negative_control": {
            "off_shell_free_point_jet_not_a_field_solution": True,
            "original_coframe_rank": bare["coframe_rank_at_1e_minus_10"],
            "transformed_coframe_rank": bare_changed["coframe_rank_at_1e_minus_10"],
            "bare_metric_change_norm": float(np.linalg.norm(bare_changed["metric"]-bare["metric"])),
            "transported_selector_metric_change_norm": float(np.linalg.norm(transported["metric"]-bare["metric"]))},
        "candidate_matrix_readouts": {
            "pair_tensor": "C_rs^{mu nu}=Tr(E_r J^mu E_s J^nu); internal-gauge invariant, real part symmetric in mu/nu for Hermitian currents",
            "loop_tensor": "L^{mu nu lambda}=Tr(E_1 J^mu E_2 J^nu E_3 J^lambda)",
            "pair_covariance_residual": float(np.linalg.norm(pair_tensors(transformed)-pair)),
            "loop_covariance_residual": float(np.linalg.norm(loop_tensor(transformed)-loop)),
            "time_chart_pair_components": pair[:, :, 0, 0].real.tolist(),
            "on_shell_time_loop_real_imag": [float(loop[0, 0, 0].real), float(loop[0, 0, 0].imag)],
            "off_shell_complex_time_loop_real_imag": [float(loop_tensor(complex_control)[0, 0, 0].real),
                                                       float(loop_tensor(complex_control)[0, 0, 0].imag)],
            "time_components_are_not_Lorentz_scalars": True,
            "current_angular_components_norm": float(np.linalg.norm(d["current"][1:3])),
            "pair_tensors_and_internal_linear_combinations_have_rank_at_most_two": True,
            "quartic_sextic_classical_products_not_native_metric_replacements_or_quantum_observables": True},
        "remaining_obligations": ["specify whether cross-readouts are fixed invariants, covariant references or part of another invariant functional",
                                  "the complete native coframe is internally gauge invariant but degenerate on this stationary single-polarization branch",
                                  "new angular/spin structure is needed to escape this rank deficiency; more internal phases alone cannot do it",
                                  "the earlier same-induced-frame real-bilinear trace obstruction still applies under its hypotheses; rank alone is not the entire geometry problem",
                                  "no physical C7 embedding, quantum ordering, scale calibration or metric backreaction is derived"],
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
