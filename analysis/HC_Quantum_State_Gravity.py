"""State-dependent scalar stress, weak massive response and a sourced neutral null parent.

These are declared comparison models, not native HC operator identification.
"""
import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "state_gravity_parent", Path(__file__).with_name("HC_Derived_Background_Curved_Parent.py"))
parent = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(parent)
geometry, checks = parent.geometry, parent.checks
ETA, N_COV, L_VECTOR = geometry.ETA, geometry.N_COV, geometry.L_VECTOR


def _metric(metric):
    metric = checks._real(metric, (4, 4), "metric")
    if not np.allclose(metric, metric.T, atol=1e-12, rtol=0):
        raise ValueError("A symmetric metric required")
    eigenvalues = np.linalg.eigvalsh(metric)
    if np.count_nonzero(eigenvalues < -1e-12) != 1 or np.count_nonzero(eigenvalues > 1e-12) != 3:
        raise ValueError("A nondegenerate mostly-positive Lorentzian metric required")
    return metric


def scalar_stress(metric, value, derivative, mass=0.0):
    """Metric variation of -sqrt|g| (g^{mn} partial_m phi* partial_n phi+m^2 |phi|^2)."""
    metric = _metric(metric)
    value = checks._finite(value, "complex scalar value")
    derivative = checks._finite(derivative, "complex scalar gradient")
    mass = checks._scalar(mass, "scalar mass")
    if value.shape != () or derivative.shape != (4,) or mass < 0:
        raise ValueError("One complex value, four derivatives and nonnegative mass required")
    inverse = np.linalg.inv(metric)
    kinetic = float(np.vdot(derivative, inverse @ derivative).real)
    energy = kinetic+mass**2*float(abs(value)**2)
    stress = 2*np.outer(derivative.conj(), derivative).real-metric*energy
    return {"stress": stress, "kinetic": kinetic,
            "density": -np.sqrt(abs(np.linalg.det(metric)))*energy,
            "trace": float(np.sum(inverse*stress))}


def scalar_equations(metric, first, value, derivative, second, mass=0.0):
    """Klein--Gordon residual and independently differentiated covariant stress divergence."""
    metric = _metric(metric)
    first = checks._real(first, (4, 4, 4), "metric first derivatives")
    derivative = checks._finite(derivative, "scalar gradient")
    second = checks._finite(second, "scalar Hessian")
    if derivative.shape != (4,) or second.shape != (4, 4) or not np.allclose(second, second.T):
        raise ValueError("Four derivatives and a symmetric scalar Hessian required")
    data = scalar_stress(metric, value, derivative, mass)
    inverse = np.linalg.inv(metric)
    di = -np.einsum("ap,lpq,qb->lab", inverse, first, inverse)
    log_volume = np.einsum("ab,lba->l", inverse, first)/2
    kg = (np.einsum("ab,ab", inverse, second)
          +np.einsum("m,mn,n", log_volume, inverse, derivative)
          +np.einsum("mmn,n", di, derivative)-mass**2*value)
    connection = np.empty((4, 4, 4))
    for a, b, c in np.ndindex((4, 4, 4)):
        connection[a, b, c] = sum(inverse[a, d]*(first[b, d, c]+first[c, d, b]-first[d, b, c])/2
                                  for d in range(4))
    energy = data["kinetic"]+mass**2*abs(value)**2
    energy_first = (np.einsum("a,lab,b->l", derivative.conj(), di, derivative).real
                    +2*np.einsum("la,ab,b->l", second.conj(), inverse, derivative).real
                    +2*mass**2*(np.conj(value)*derivative).real)
    dt = np.array([2*(np.outer(dd.conj(), derivative)+np.outer(derivative.conj(), dd)).real
                   -first[l]*energy-metric*energy_first[l] for l, dd in enumerate(second)])
    covariant = (dt-np.einsum("srm,sn->rmn", connection, data["stress"])
                 -np.einsum("srn,ms->rmn", connection, data["stress"]))
    divergence = np.einsum("mr,rmn->n", inverse, covariant)
    return {**data, "KG": kg, "stress_first": dt, "divergence": divergence,
            "Ward_rhs": 2*(np.conj(kg)*derivative).real}


def mode_jets(point, coefficients, covectors):
    point = checks._real(point, (4,), "point")
    coefficients = checks._finite(coefficients, "mode coefficients")
    covectors = checks._finite(covectors, "mode covectors")
    if (coefficients.ndim != 1 or covectors.shape != (len(coefficients), 4)
            or np.max(np.abs(covectors.imag), initial=0) > 1e-12):
        raise ValueError("Compatible finite coefficients and real mode covectors required")
    covectors = covectors.real
    values = coefficients*np.exp(1j*covectors @ point)
    return (complex(np.sum(values)), 1j*np.einsum("r,rm->m", values, covectors),
            -np.einsum("r,rm,rn->mn", values, covectors, covectors))


def mode_source(point, covectors, occupation, mass, volume):
    """Normal-ordered particle-sector <T> of a free complex scalar in a flat periodic box.

    occupation[r,s]=<a_r^dagger a_s>; both one-particle and coherent states can share it.
    Antiparticles and the fixed flat vacuum subtraction are explicit zero inputs.
    """
    point = checks._real(point, (4,), "point")
    covectors = checks._finite(covectors, "mode covectors")
    occupation = checks._finite(occupation, "occupation covariance")
    mass, volume = [checks._scalar(v, "mode normalization") for v in (mass, volume)]
    n = len(covectors)
    if (covectors.shape != (n, 4) or occupation.shape != (n, n) or mass < 0 or volume <= 0
            or np.max(np.abs(covectors.imag), initial=0) > 1e-12
            or not np.allclose(occupation, occupation.conj().T, atol=1e-12, rtol=0)
            or np.min(np.linalg.eigvalsh(occupation)) < -1e-12):
        raise ValueError("Real on-shell modes, positive Hermitian occupation and positive volume required")
    covectors = covectors.real
    if np.any(covectors[:, 0] >= 0) or not np.allclose(
            np.einsum("rm,mn,rn->r", covectors, ETA, covectors), -mass**2, atol=1e-12, rtol=0):
        raise ValueError("Future positive-frequency massive or null modes required")
    values = np.exp(1j*covectors @ point)/np.sqrt(-2*covectors[:, 0]*volume)
    result = np.zeros((4, 4), dtype=complex)
    for r, s in np.ndindex((n, n)):
        p, q = covectors[r], covectors[s]
        kernel = np.outer(p, q)+np.outer(q, p)-ETA*(p @ ETA @ q+mass**2)
        result += occupation[r, s]*values[r].conj()*values[s]*kernel
    if np.linalg.norm(result.imag) > 1e-11:
        raise ValueError("The expectation must be real")
    return {"stress": result.real, "total_box_energy": float(np.sum(-covectors[:, 0]*occupation.diagonal().real)),
            "mean_number": float(np.trace(occupation).real)}


def linearized_einstein(second):
    second = checks._real(second, (4, 4, 4, 4), "metric perturbation second jet")
    ricci = (np.einsum("ab,bman->mn", ETA, second)+np.einsum("ab,bnam->mn", ETA, second)
             -np.einsum("ab,abmn->mn", ETA, second)-np.einsum("ab,mnab->mn", ETA, second))/2
    return ricci-ETA*np.sum(ETA*ricci)/2


def massive_interference(point=(0.1, 0.2, -0.3, 0.1), phase=0.4, mass=0.6, einstein_coupling=0.2):
    """Exact flat-space stress; only its zero-mean interference part has a linear metric witness."""
    point = checks._real(point, (4,), "point")
    phase, mass, coupling = [checks._scalar(v, "massive comparison parameter")
                             for v in (phase, mass, einstein_coupling)]
    if mass <= 0:
        raise ValueError("This test uses a positive fixed mass")
    energy, volume = np.sqrt(1+mass**2), (2*np.pi)**3
    covectors = np.array([[-energy, 1, 0, 0], [-energy, 0, 1, 0]])
    coefficients = np.array([np.sqrt(0.8), np.sqrt(0.2)*np.exp(1j*phase)])
    occupation = np.outer(coefficients.conj(), coefficients)
    coherent = mode_source(point, covectors, occupation, mass, volume)
    mixed = mode_source(point, covectors, np.diag(occupation.diagonal()), mass, volume)
    jets = mode_jets(point, coefficients/np.sqrt(2*energy*volume), covectors)
    scalar = scalar_equations(ETA, np.zeros((4, 4, 4)), *jets, mass)
    difference = coherent["stress"]-mixed["stress"]
    q = covectors[1]-covectors[0]
    q_squared = float(q @ ETA @ q)
    kernel = (np.outer(covectors[0], covectors[1])+np.outer(covectors[1], covectors[0])
              -ETA*(covectors[0] @ ETA @ covectors[1]+mass**2))
    complex_cross = occupation[0, 1]*np.exp(1j*q @ point)/(2*energy*volume)
    difference_first = 2*np.einsum("l,mn->lmn", (1j*q*complex_cross).real, kernel)
    factor = 2*coupling/q_squared
    bar_h = factor*difference
    h = bar_h-ETA*np.sum(ETA*bar_h)/2
    bar_h_first = factor*difference_first
    first = bar_h_first-np.einsum("mn,l->lmn", ETA, np.einsum("mn,lmn->l", ETA, bar_h_first))/2
    second = -np.einsum("a,b,mn->abmn", q, q, h)
    return {"point": point, "mass": mass, "covectors": covectors, "coefficients": coefficients,
            "occupation": occupation, "volume": volume, "scalar_jets": jets, "scalar": scalar,
            "coherent_stress": coherent["stress"], "mixed_stress": mixed["stress"],
            "interference_stress": difference, "interference_first": difference_first,
            "total_energy": coherent["total_box_energy"], "mixed_total_energy": mixed["total_box_energy"],
            "wavevector": q, "wavevector_squared": q_squared, "bar_h": bar_h,
            "h": h, "h_first": first, "h_second": second,
            "linearized_Einstein": linearized_einstein(second), "einstein_coupling": coupling}


def null_wave(u, phase=0.0, amplitudes=(0.3, 0.1), frequencies=(1.0, 2.0)):
    u, phase = [checks._scalar(v, "null mode parameter") for v in (u, phase)]
    amplitudes = checks._real(amplitudes, (2,), "null amplitudes")
    frequencies = checks._real(frequencies, (2,), "null frequencies")
    modes = amplitudes*np.exp(1j*np.array([0, phase])-1j*frequencies*u)
    jets = [complex(np.sum((-1j*frequencies)**order*modes)) for order in range(4)]
    rho = 2*abs(jets[1])**2
    rho_first = 4*(np.conj(jets[1])*jets[2]).real
    rho_second = 4*(abs(jets[2])**2+(np.conj(jets[1])*jets[3]).real)
    return {"jets": jets, "rho": float(rho), "rho_first": float(rho_first), "rho_second": float(rho_second)}


def sourced_profile(point, phase=0.0, coupling=0.4, einstein_coupling=1.0,
                    intercept=2.0, amplitudes=(0.3, 0.1)):
    """Positive local Helmholtz witness w=F0 cos(k(u) X), h=log(w)/(kappa_eff kappa)."""
    point = checks._real(point, (4,), "target point")
    coupling, ec, intercept = [checks._scalar(v, "profile coefficient")
                                for v in (coupling, einstein_coupling, intercept)]
    if coupling == 0 or ec <= 0 or intercept <= 0:
        raise ValueError("Nonzero HC coupling and positive Einstein coupling/intercept required")
    wave = null_wave(N_COV @ point, phase, amplitudes)
    rho, dr, ddr = [wave[k] for k in ("rho", "rho_first", "rho_second")]
    if rho <= 0:
        if rho != 0 or dr != 0 or ddr != 0:
            raise ValueError("Use a positive-flux patch or the identically zero source")
        k = dk = ddk = 0.0
    else:
        k = ec*np.sqrt(rho)
        dk = ec*dr/(2*np.sqrt(rho))
        ddk = ec*(ddr/(2*np.sqrt(rho))-dr**2/(4*rho**1.5))
    x, a = point[1], ec*coupling
    angle = k*x
    if abs(angle) >= np.pi/2:
        raise ValueError("The chosen local positive-cosine patch has ended")
    tangent, sec_squared = np.tan(angle), 1/np.cos(angle)**2
    h = np.log(intercept*np.cos(angle))/a
    hu, hx = -tangent*dk*x/a, -tangent*k/a
    huu = -(sec_squared*(dk*x)**2+tangent*ddk*x)/a
    hux = -(sec_squared*dk*x*k+tangent*dk)/a
    hxx = -sec_squared*k**2/a
    transverse = np.eye(4)[1]
    gradient = hu*N_COV+hx*transverse
    hessian = (huu*np.outer(N_COV, N_COV)+hux*(np.outer(N_COV, transverse)+np.outer(transverse, N_COV))
               +hxx*np.outer(transverse, transverse))
    return {"amplitude": float(h), "gradient": gradient, "hessian": hessian,
            "wave": wave, "w": float(intercept*np.cos(angle)), "k": float(k),
            "Helmholtz_residual": float((-k**2+ec**2*rho)*intercept*np.cos(angle)),
            "profile_residual": float(hxx+a*hx**2+ec*rho/coupling)}


def sourced_branch(point=(0.0, 0.2, 0.0, 0.3), phase=0.0, readout=None,
                   coupling=0.4, einstein_coupling=1.0, amplitudes=(0.3, 0.1)):
    """All geometric/scalar equations of a declared enlarged parent, not native gravity."""
    if readout is None:
        bg, y = None, [np.array(point), np.eye(4), np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))]
    else:
        bg, y = parent.coordinate_jets(point, readout)
    profile = sourced_profile(y[0], phase, coupling, einstein_coupling, amplitudes=amplitudes)
    h, p, pp = [profile[k] for k in ("amplitude", "gradient", "hessian")]
    nn, theta = np.outer(N_COV, N_COV), y[1].T
    target = ETA+2*coupling*h*nn
    target_first = 2*coupling*np.einsum("l,mn->lmn", p, nn)
    target_second = 2*coupling*np.einsum("ls,mn->lsmn", pp, nn)
    metric = parent.pullback_metric(y, target, target_first, target_second)
    geometry_data = geometry.metric_curvature(metric["metric"], metric["first"], metric["second"])
    px, qx = theta.T @ p, theta.T @ N_COV
    ppx = theta.T @ pp @ theta+np.einsum("a,lsa->ls", p, y[2])
    qqx = np.einsum("a,lsa->ls", N_COV, y[2])
    hc = parent.paired_scalar_equations(metric["metric"], metric["first"], px, ppx, qx, qqx, coupling)
    phi, dphi, ddphi = profile["wave"]["jets"][:3]
    matter = scalar_equations(metric["metric"], metric["first"], phi, dphi*qx,
                              ddphi*np.outer(qx, qx)+dphi*qqx)
    total_stress = hc["stress"]+matter["stress"]
    expected = (-coupling*(pp[1, 1]+pp[2, 2]))*np.outer(qx, qx)
    frame = (np.eye(4)+coupling*h*np.outer(L_VECTOR, N_COV)) @ theta
    return {"profile": profile, "background": bg, "coordinate_jets": y, "theta": theta,
            "coframe": frame, "metric_jets": metric, "geometry": geometry_data,
            "hc": hc, "matter": matter, "total_stress": total_stress,
            "Einstein_residual": geometry_data["einstein"]-einstein_coupling*total_stress,
            "curvature_pullback_error": geometry_data["einstein"]-expected,
            "coframe_constraint": frame-theta-coupling*h*np.outer(L_VECTOR, qx),
            "potential_constraint": 0.0, "multipliers": [0.0, 0.0]}


def evaluate():
    massive = massive_interference()
    plus, minus = [massive_interference(point=(0, 0, 0, 0), phase=delta) for delta in (0, np.pi)]
    null_plus, null_minus = [sourced_branch(point=(0, 0, 0, 0), phase=delta) for delta in (0, np.pi)]
    branch = sourced_branch(readout="symmetric_cross", point=(0.01, 0.02, -0.03, 0.01))
    return {
        "status": "state-sensitive stress derived in explicit scalar comparisons; NOT a native HC derivation or a complete renormalized quantum-gravity solution",
        "fixed_mass_quantum_source": {
            "field": "free complex scalar, two equal-energy positive-frequency modes in a periodic flat box",
            "mass": massive["mass"], "one_particle_mean_number": 1,
            "occupation": "N_rs=conj(c_r)c_s, c=(sqrt(.8),sqrt(.2) exp(i delta)); compare its diagonal mixture",
            "one_particle_mean_field_is_zero_but_stress_is_not": True,
            "same_source_can_be_realized_by_a_bosonic_coherent_state": True,
            "fixed_total_energy_for_all_relative_phases": massive["total_energy"],
            "energy_density_at_origin_phase_zero": float(plus["coherent_stress"][0, 0]),
            "energy_density_at_origin_phase_pi": float(minus["coherent_stress"][0, 0]),
            "mixture_energy_density": float(massive["mixed_stress"][0, 0]),
            "KG_residual_norm": float(abs(massive["scalar"]["KG"])),
            "stress_divergence_norm": float(np.linalg.norm(massive["scalar"]["divergence"])),
            "global_phase_is_unobservable_and_no_direct_phase_gravity_term_is_added": True,
        },
        "massive_linear_response": {
            "scope": "zero-mean interference source only, on a fixed flat reference, first order in gravitational coupling; not the positive homogeneous source or a nonlinear massive solution",
            "equation": "Box bar_h_mn=-2 kappa_eff delta T_mn; bar_h=2 kappa_eff delta T/Q^2",
            "Q_squared": massive["wavevector_squared"],
            "Einstein_residual_norm": float(np.linalg.norm(massive["linearized_Einstein"]
                                                           -massive["einstein_coupling"]*massive["interference_stress"])),
            "source_conservation_norm": float(np.linalg.norm(np.einsum("m,mn->n", ETA @ massive["wavevector"], massive["interference_stress"]))),
            "no_semiclassical_validity_certificate_for_the_one_particle_state": True,
        },
        "sourced_null_parent": {
            "added_field": "independent minimally coupled complex scalar phi with S_phi=-integral sqrt|g(E)| |d phi|^2; the previous reference-Dirac probes remain fixed-reference probes",
            "source": "phi=f(u), rho(u)=2|f'(u)|^2, T_phi=rho du tensor du",
            "derived_profile_equation": "Delta_perp h+kappa_eff kappa |grad_perp h|^2=-kappa_eff rho/kappa",
            "Helmholtz_equation": "(Delta_perp+kappa_eff^2 rho) w=0, w=exp(kappa_eff kappa h)",
            "positive_local_witness": "w=2 cos(kappa_eff sqrt(rho(u)) Y^1), h=log(w)/(kappa_eff kappa)",
            "all_declared_fields_varied": "Psi,E,h,u,phi,lambda,zeta; lambda=zeta=0 solves the full independent equations on this branch",
            "phase_zero_flux_at_origin": null_plus["profile"]["wave"]["rho"],
            "phase_pi_flux_at_origin": null_minus["profile"]["wave"]["rho"],
            "sample_reference_probe_residual_norm": float(np.linalg.norm(branch["background"]["reference_residual"])),
            "sample_Einstein_residual_component_norm": float(np.linalg.norm(branch["Einstein_residual"])),
            "sample_independent_curvature_pullback_error": float(np.linalg.norm(branch["curvature_pullback_error"])),
            "sample_h_EL": branch["hc"]["h_EL"], "sample_u_EL": branch["hc"]["u_EL"],
            "sample_KG_residual_norm": float(abs(branch["matter"]["KG"])),
            "sample_coframe_constraint_norm": float(np.linalg.norm(branch["coframe_constraint"])),
            "adding_mass_breaks_the_unchanged_null_scalar_branch": "Box f(u)=0, so (Box-m^2)f=-m^2 f; its potential also adds transverse stress",
        },
        "quantum_scope": {
            "coherent_shift_identity": "on a fixed geometry and a zero-mean reference state, <T>_displaced,ren-<T>_reference,ren=T_classical[f] for the free scalar",
            "reference_vacuum_stress_counterterms_and_stress_fluctuations_not_computed": True,
            "interference_is_not_exclusively_quantum_and_does_not_prove_quantized_gravity": True,
            "orthogonal_uncoupled_channels_have_no_phase_interference_in_their_summed_stress": True,
        },
        "native_obligations": ["identify the scalar observable with an allowed native triadic operator, not a new unnamed field",
                               "derive common metric/gamma/readout and mass/Yukawa/gauge/projector equations",
                               "retain the prior HC current-span and null-cone exclusions until their hypotheses actually change",
                               "derive physical units, Newton coupling, quantum state, vacuum subtraction and controlled validity"],
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
