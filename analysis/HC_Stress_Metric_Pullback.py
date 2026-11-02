"""Weak stress-to-metric pullback, variational normalization and causal/data limitations.

The Einstein response is an input, not a derivation of the native HC coframe.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import mpmath as mp
import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "stress_metric_dirac", Path(__file__).with_name("HC_Dirac_State_Gravity.py"))
dirac = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dirac)
ETA, GAMMA, BETA = dirac.ETA, dirac.GAMMA, dirac.BETA


def pairing(a, b):
    """Real Lorentzian tensor pairing, averaged over the declared spatial sample grid."""
    a, b = np.asarray(a), np.asarray(b)
    if a.shape != b.shape or a.shape[-2:] != (4, 4) or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError("Compatible finite tensor fields required")
    if np.max(np.abs(a.imag), initial=0) > 1e-11 or np.max(np.abs(b.imag), initial=0) > 1e-11:
        raise ValueError("Real tensor fields required")
    return float(np.mean(np.einsum("...mn,ma,nb,...ab->...", a.real, ETA, ETA, b.real)))


def reverse(tensor):
    return dirac.trace_reverse((np.asarray(tensor),))[0]


def _periodic_data(tensor):
    tensor = np.asarray(tensor)
    if (tensor.ndim != 4 or tensor.shape[0] != tensor.shape[1] or tensor.shape[0] < 5
            or tensor.shape[0] % 2 == 0 or tensor.shape[2:] != (4, 4)
            or not np.isfinite(tensor).all() or np.max(np.abs(tensor.imag), initial=0) > 1e-11
            or not np.allclose(tensor, tensor.swapaxes(-1, -2), atol=1e-11, rtol=0)):
        raise ValueError("A real symmetric tensor on an odd square periodic grid required")
    size = tensor.shape[0]
    k = np.fft.fftfreq(size, 1/size)
    kx, ky = np.meshgrid(k, k, indexing="ij")
    return tensor.real, np.fft.fftn(tensor.real, axes=(0, 1)), kx, ky


def periodic_response(stress):
    """R=2 P/|k|^2 on nonzero static modes; the homogeneous source is NOT solved here."""
    stress, coefficients, kx, ky = _periodic_data(stress)
    square = kx**2+ky**2
    factor = np.divide(2.0, square, out=np.zeros_like(square), where=square > 0)
    h_coefficients = reverse(coefficients)*factor[..., None, None]
    h = np.fft.ifftn(h_coefficients, axes=(0, 1)).real
    frequencies = [np.zeros_like(kx), kx, ky, np.zeros_like(kx)]
    first = np.array([np.fft.ifftn(1j*k[..., None, None]*h_coefficients, axes=(0, 1)).real for k in frequencies])
    second = np.array([[np.fft.ifftn(-k[..., None, None]*l[..., None, None]*h_coefficients, axes=(0, 1)).real
                        for l in frequencies] for k in frequencies])
    return {"h": h, "first": first, "second": second,
            "projected_source": stress-np.mean(stress, axis=(0, 1)),
            "omitted_zero_mode": np.mean(stress, axis=(0, 1))}


def gauge_fixed_operator(h):
    """E_gf h=-Box P h/2, not the unfixed Einstein operator for arbitrary off-shell sources."""
    _, coefficients, kx, ky = _periodic_data(h)
    return np.fft.ifftn(reverse(coefficients)*(kx**2+ky**2)[..., None, None]/2, axes=(0, 1)).real


def grid_probe(size=17, phase=0.4):
    modes = dirac.mode_family(phase)
    coordinate = 2*np.pi*np.arange(size)/size
    x, y = np.meshgrid(coordinate, coordinate, indexing="ij")
    points = np.stack([np.zeros_like(x), x, y, np.zeros_like(x)], axis=-1)
    factors = modes["coefficients"][:, None, None]*np.exp(1j*np.einsum("rm,...m->r...", modes["covectors"], points))/np.sqrt(modes["volume"])
    amplitudes = factors[..., None]*modes["spinors"][:, None, None, :]
    value = np.sum(amplitudes, axis=0)
    first = 1j*np.einsum("rm,r...i->m...i", modes["covectors"], amplitudes)
    return {"psi": value, "first": first, "points": points, "modes": modes}


def grid_stress(psi, first, mass):
    """Batch version of the existing OFF-SHELL real Dirac stress, including g L_D."""
    psi, first = np.asarray(psi, complex), np.asarray(first, complex)
    if psi.ndim != 3 or psi.shape[-1] != 4 or first.shape != (4, *psi.shape):
        raise ValueError("A spinor and first jet on a square spatial grid required")
    ordered = np.einsum("...i,mij,n...j->...mn", psi.conj(), BETA @ dirac.GAMMA_LOWER, first)
    kinetic = np.einsum("...i,mij,m...j->...", psi.conj(), BETA @ GAMMA, first)
    w = mass*np.einsum("...i,ij,...j->...", psi.conj(), BETA, psi).real
    lagrangian = -kinetic.imag-w
    stress = (ordered+ordered.swapaxes(-1, -2)).imag/2+np.einsum("mn,...->...mn", ETA, lagrangian)
    residual = 1j*np.einsum("mij,m...j->...i", GAMMA, first)-mass*psi
    return {"stress": stress, "lagrangian": lagrangian, "residual": residual}


def grid_operator_change(psi, first, h, h_first):
    gamma_change = -np.einsum("mr,...ra,aij->m...ij", ETA, h, GAMMA)/2
    spin = np.zeros((4, *psi.shape[:-1], 4, 4), complex)
    for mu, a, b in np.ndindex((4, 4, 4)):
        omega = (h_first[b, ..., a, mu]-h_first[a, ..., mu, b])/2
        spin[mu] -= omega[..., None, None]*(GAMMA[a] @ GAMMA[b])/4
    return 1j*(np.einsum("m...ij,m...j->...i", gamma_change, first)
               +np.einsum("mij,m...jk,...k->...i", GAMMA, spin, psi))


def induced_action(stress, strength=0.2):
    response = periodic_response(stress)
    return strength*pairing(stress, response["h"])/4


def parent_action(stress, metric_perturbation, strength=0.2):
    if strength <= 0:
        raise ValueError("A positive gravitational comparison strength required")
    return (-pairing(metric_perturbation, gauge_fixed_operator(metric_perturbation))/(4*strength)
            +pairing(metric_perturbation, stress)/2)


def wave_jets(point, amplitude=0.03, frequency=1.1):
    point = dirac.checks._real(point, (4,), "point")
    amplitude, frequency = [dirac.checks._scalar(v, "free wave parameter") for v in (amplitude, frequency)]
    q = frequency*np.array([1, 0, 0, -1])
    polarization = np.diag([0, 1, -1, 0])
    phase = q @ point
    return (amplitude*np.cos(phase)*polarization,
            -amplitude*np.einsum("r,mn->rmn", q, polarization)*np.sin(phase),
            -amplitude*np.einsum("r,s,mn->rsmn", q, q, polarization)*np.cos(phase))


def linear_riemann(second):
    second = np.asarray(second)
    return np.array([[[[(second[c, b, a, d]+second[d, a, b, c]-second[c, a, b, d]-second[d, b, a, c])/2
                         for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)])


def wave_probe_correction(point, phase=0.4, amplitude=0.03, frequency=1.1):
    """Zero-initial-data Dirac reaction to the extra free gravitational wave, at first order."""
    point = dirac.checks._real(point, (4,), "point")
    modes = dirac.mode_family(phase)
    q, polarization = frequency*np.array([1, 0, 0, -1]), amplitude*np.diag([0, 1, -1, 0])/2
    value, first = np.zeros(4, complex), np.zeros((4, 4), complex)
    for r in range(2):
        psi = modes["coefficients"][r]*modes["spinors"][r]/np.sqrt(modes["volume"])
        derivative = 1j*np.outer(modes["covectors"][r], psi)
        for sign in (1, -1):
            forcing = -BETA @ dirac.operator_change(psi, derivative, polarization,
                                                    1j*np.einsum("m,ij->mij", sign*q, polarization))
            k = modes["momenta"][r]+sign*q[1:]
            a = np.einsum("i,ijk->jk", k, dirac.WEIGHTS[1:])+modes["mass"]*BETA-modes["energy"]*np.eye(4)
            generator = np.zeros((5, 5), complex)
            generator[:4, :4], generator[:4, 4], generator[4, 4] = -1j*a, -1j*forcing, 1j*sign*q[0]
            with mp.workdps(25):
                exponential = mp.expm(mp.matrix(generator.tolist())*float(point[0]))
                z = np.array([complex(exponential[i, 4]) for i in range(5)])
            dz = generator @ z
            factor = np.exp(-1j*modes["energy"]*point[0]+1j*k @ point[1:])
            value += factor*z[:4]
            first[0] += factor*(dz[:4]-1j*modes["energy"]*z[:4])
            first[1:] += 1j*np.outer(k, factor*z[:4])
    return value, first


def with_free_wave(point=(0.08, 0.2, -0.3, 0.1), phase=0.4, strength=0.01, amplitude=0.03):
    modes, psi0, first0, _ = dirac.probe_jets(point, phase)
    metric = tuple(a+b for a, b in zip(dirac.metric_jets(point, phase)["h"], wave_jets(point, amplitude)))
    reaction = tuple(a+b for a, b in zip(dirac.correction_jets(point, phase), wave_probe_correction(point, phase, amplitude)))
    h, dh, ddh = metric
    coframe = np.eye(4)+strength*ETA @ h/2
    geometric = dirac.bundle(coframe, strength*np.einsum("ab,lbc->lac", ETA, dh)/2,
                             strength*np.einsum("ab,lsbc->lsac", ETA, ddh)/2)
    psi = np.outer(modes["internal"], psi0+strength*reaction[0])
    first = np.einsum("r,mi->mri", modes["internal"], first0+strength*reaction[1])
    matter = dirac.dirac_data(psi, first, modes["mass_operator"], geometric["gamma"], geometric["metric"], geometric["spin"])
    original = dirac.dirac_data(psi0[None], first0[:, None], np.array([[modes["mass"]]]))
    return {"linear_Einstein_residual": dirac.state.linearized_einstein(ddh)-original["stress"],
            "linear_Dirac_residual": (1j*np.einsum("mij,mj->i", GAMMA, reaction[1])-modes["mass"]*reaction[0]
                                      +dirac.operator_change(psi0, first0, h, dh)),
            "Einstein_residual": geometric["curvature"]["einstein"]-strength*matter["stress"],
            "Dirac_residual": matter["residual"], "metric": geometric, "matter": matter}


def retarded_kernel(times, frequency=1.3):
    times = np.asarray(times, float)
    if times.ndim != 1 or len(times) < 3 or not np.isfinite(times).all() or np.any(np.diff(times) <= 0) or frequency <= 0:
        raise ValueError("Increasing finite sample times and positive frequency required")
    weights = np.empty_like(times)
    weights[0], weights[-1] = (times[1]-times[0])/2, (times[-1]-times[-2])/2
    weights[1:-1] = (times[2:]-times[:-2])/2
    lag = times[:, None]-times[None, :]
    kernel = np.where(lag >= 0, np.sin(frequency*lag)/frequency, 0)*weights[None, :]
    adjoint = kernel.T*weights[None, :]/weights[:, None]
    return {"response": kernel, "adjoint": adjoint, "weights": weights}


def doubled_action(left, right, response, weights, strength=0.2):
    difference, average = np.asarray(left)-np.asarray(right), (np.asarray(left)+np.asarray(right))/2
    return float(strength*np.sum(difference*weights*(response @ average))/2)


def evaluate():
    grid = grid_probe()
    stress = grid_stress(grid["psi"], grid["first"], grid["modes"]["mass"])["stress"]
    response = periodic_response(stress)
    metric = 0.2*response["h"]
    induced = induced_action(stress)
    total = parent_action(stress, metric)
    rng = np.random.default_rng(717)
    variation = rng.normal(size=stress.shape[-2:])
    variation = (variation+variation.T)/2
    scalar = np.cos(grid["points"][..., 1]-grid["points"][..., 2])
    delta_stress = scalar[..., None, None]*variation
    predicted = pairing(metric, delta_stress)/2
    step = 1e-5
    actual = (induced_action(stress+step*delta_stress)-induced_action(stress-step*delta_stress))/(2*step)
    points, energy = grid["points"], grid["modes"]["energy"]
    zeta = np.exp(1j*(2*points[..., 1]-points[..., 2]))[..., None]*np.array([0.2+0.1j, -0.3j, 0.1, 0.15j])
    zeta_first = 1j*np.einsum("m,...i->m...i", [-energy, 2, -1, 0], zeta)
    def varied_probe_action(scale):
        varied = grid_stress(grid["psi"]+scale*zeta, grid["first"]+scale*zeta_first, grid["modes"]["mass"])
        return induced_action(varied["stress"])
    probe_actual = (varied_probe_action(step)-varied_probe_action(-step))/(2*step)
    probe_change = grid_operator_change(grid["psi"], grid["first"], metric, 0.2*response["first"])
    probe_predicted = float(2*np.mean(np.einsum("...i,ij,...j->...", zeta.conj(), BETA, probe_change).real))
    point = (0.08, 0.2, -0.3, 0.1)
    wave = wave_jets(point)
    modes, psi0, first0, _ = dirac.probe_jets(point)
    reaction = wave_probe_correction(point)
    wave_dirac = (1j*np.einsum("mij,mj->i", GAMMA, reaction[1])-modes["mass"]*reaction[0]
                  +dirac.operator_change(psi0, first0, wave[0], wave[1]))
    free = [with_free_wave(point, strength=s) for s in (0.04, 0.02, 0.01)]
    times = np.linspace(0, 2, 31)
    causal = retarded_kernel(times)
    future_source = np.zeros(len(times))
    future_source[-1] = 1
    ordinary = (causal["response"]+causal["adjoint"]) @ future_source/2
    physical = causal["response"] @ future_source
    return {
        "status": "conditional weak stress-to-metric pullback with correct action, causal completion and free-data obstruction; NOT a native HC/coframe derivation",
        "reconstruction": {
            "map": "h[Psi;B]=kappa R_B T_flat[Psi]+h_free[B], R_B=-2 P Box_B^(-1)",
            "P": "four-dimensional trace reversal, not a native closure projector",
            "boundary_gauge_and_free_radiation_data_are_required": True,
            "not_an_algebraic_pointwise_probe_bilinear": True,
            "assumes_Einstein_Hilbert_response_and_does_not_derive_it_from_native_quantum_properties": True,
        },
        "self_adjoint_variational_sector": {
            "action": "S_reduced=S_D0+kappa <T,R_B T>/4, for a declared self-adjoint gauge-fixed inverse and compatible boundary terms",
            "variation": "delta S_ind=<h,delta T>/2, not the doubled reaction from substituting into the matter term alone",
            "periodic_test_scope": "nonzero static spatial Fourier modes only; zero-mean gauge-fixed variational check, not the full positive source or retarded evolution",
            "induced_action": induced, "eliminated_parent_action": total,
            "action_value_error": abs(induced-total), "directional_variation_error": abs(predicted-actual),
            "full_spinor_variation_vs_common_Dirac_reaction_error": abs(probe_actual-probe_predicted),
            "omitted_constant_source_norm": float(np.linalg.norm(response["omitted_zero_mode"])),
        },
        "free_wave_counterexample": {
            "same_zeroth_order_probe_and_source_different_curvature": True,
            "free_Einstein_residual_norm": float(np.linalg.norm(dirac.state.linearized_einstein(wave[2]))),
            "free_tidal_component_R_0x0x": float(linear_riemann(wave[2])[0, 1, 0, 1]),
            "additional_probe_reaction_norm": float(np.linalg.norm(reaction[0])),
            "additional_linear_Dirac_residual_norm": float(np.linalg.norm(wave_dirac)),
            "strengths": [0.04, 0.02, 0.01],
            "full_Einstein_residual_norms_with_wave": [float(np.linalg.norm(x["Einstein_residual"])) for x in free],
            "full_Dirac_residual_norms_with_wave": [float(np.linalg.norm(x["Dirac_residual"])) for x in free],
            "not_just_a_coordinate_gauge_wave": True,
        },
        "causal_variation_test": {
            "single_history_variation_symmetrizes_retarded_response": True,
            "future_source_retarded_past_response_norm": float(np.linalg.norm(physical[:-1])),
            "future_source_single_history_advanced_gradient_norm": float(np.linalg.norm(ordinary[:-1])),
            "response_norms_omit_the_overall_strength_over_two": True,
            "doubled_action": "S_ind,CTP=kappa <T_difference,R_ret T_average>/2; vary before setting both histories equal",
            "physical_left_variation": "kappa (DT)^* R_ret T/2, with no advanced contribution",
            "oscillator_kernel_test_is_not_a_gravitational_data_or_noise_kernel_measurement": True,
            "no_native_tensor_or_two_frame_identification_is_assumed": True,
        },
        "remaining_native_obligations": ["derive or justify the nonlocal/coarse-grained stress readout instead of silently replacing E=Re(barPsi Gamma D Psi)",
                                         "specify gauge, physical initial/boundary radiation data, zero modes and a causal variational prescription",
                                         "derive Einstein coefficients and native C7/M16/HC/gauge/projector operator matching without double counting",
                                         "higher orders, quantum-state renormalization, fluctuations, physical scale and stability"],
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
