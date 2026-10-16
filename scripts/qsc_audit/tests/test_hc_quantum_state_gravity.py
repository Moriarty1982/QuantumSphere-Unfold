"""State-dependent sources, massive linear response and enlarged null-parent scope."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("quantum_state_gravity", ROOT / "analysis/HC_Quantum_State_Gravity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCQuantumStateGravityTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(616)

    def assertClose(self, actual, expected, atol=2e-10):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-8)

    def test_stress_is_the_full_independent_inverse_metric_variation(self):
        metric = model.ETA+0.03*np.ones((4, 4))
        inverse = np.linalg.inv(metric)
        value, derivative = 0.7+0.2j, self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        data = model.scalar_stress(metric, value, derivative, 0.6)
        variation = self.rng.normal(size=(4, 4))
        variation = (variation+variation.T)/2
        step = 1e-6
        plus = model.scalar_stress(np.linalg.inv(inverse+step*variation), value, derivative, 0.6)["density"]
        minus = model.scalar_stress(np.linalg.inv(inverse-step*variation), value, derivative, 0.6)["density"]
        prediction = -np.sqrt(abs(np.linalg.det(metric)))*np.sum(data["stress"]*variation)/2
        self.assertClose((plus-minus)/(2*step), prediction, atol=2e-8)

    def test_global_constant_phase_does_not_change_stress(self):
        d = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        phase = np.exp(1.37j)
        self.assertClose(model.scalar_stress(model.ETA, 0.3j, d, 0.6)["stress"],
                         model.scalar_stress(model.ETA, phase*0.3j, phase*d, 0.6)["stress"])

    def test_off_shell_covariant_ward_identity_keeps_nonzero_reaction(self):
        metric = model.ETA+0.02*np.ones((4, 4))
        first = self.rng.normal(size=(4, 4, 4))*0.1
        first = (first+first.swapaxes(1, 2))/2
        derivative = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        second = self.rng.normal(size=(4, 4))+1j*self.rng.normal(size=(4, 4))
        second = (second+second.T)/2
        data = model.scalar_equations(metric, first, 0.3+0.2j, derivative, second, 0.6)
        self.assertGreater(abs(data["KG"]), 0.1)
        self.assertGreater(np.linalg.norm(data["divergence"]), 0.1)
        self.assertClose(data["divergence"], data["Ward_rhs"])

    def test_stress_derivatives_match_finite_differences_off_shell(self):
        value = 0.2+0.3j
        d = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        dd = self.rng.normal(size=(4, 4))+1j*self.rng.normal(size=(4, 4))
        dd = (dd+dd.T)/2
        first = self.rng.normal(size=(4, 4, 4))*0.03
        first = (first+first.swapaxes(1, 2))/2
        data = model.scalar_equations(model.ETA, first, value, d, dd, 0.6)
        step = 1e-6
        for mu in range(4):
            plus = model.scalar_stress(model.ETA+step*first[mu], value+step*d[mu], d+step*dd[mu], 0.6)
            minus = model.scalar_stress(model.ETA-step*first[mu], value-step*d[mu], d-step*dd[mu], 0.6)
            self.assertClose((plus["stress"]-minus["stress"])/(2*step), data["stress_first"][mu], atol=2e-8)

    def test_scalar_euler_equation_from_periodic_field_variation(self):
        # Spectral differentiation keeps this independent of the local jet/connection implementation.
        x = 2*np.pi*np.arange(64)/64
        k = np.fft.fftfreq(len(x), 1/len(x))
        diff = lambda f: np.fft.ifft(1j*k*np.fft.fft(f))
        phi = np.sin(x)+0.3j*np.cos(2*x)
        variation = np.cos(x)+0.2*np.sin(3*x)+0.4j*np.sin(2*x)
        metric = np.broadcast_to(model.ETA, (len(x), 4, 4)).copy()
        metric[:, 0, 0] = -(1+0.2*np.cos(x))**2
        volume = 1+0.2*np.cos(x)
        dphi = diff(phi)
        kg = diff(volume*dphi)/volume-0.6**2*phi
        for i in range(0, len(x), 8):
            first, gradient, hessian = np.zeros((4, 4, 4)), np.zeros(4, complex), np.zeros((4, 4), complex)
            first[1, 0, 0] = 0.4*volume[i]*np.sin(x[i])
            gradient[1], hessian[1, 1] = dphi[i], diff(dphi)[i]
            local = model.scalar_equations(metric[i], first, phi[i], gradient, hessian, 0.6)
            self.assertClose(local["KG"], kg[i])
        def action(f):
            return -np.mean(volume*(abs(diff(f))**2+0.6**2*abs(f)**2))
        step = 1e-6
        prediction = 2*np.mean(volume*(np.conj(variation)*kg).real)
        self.assertClose((action(phi+step*variation)-action(phi-step*variation))/(2*step), prediction, atol=1e-8)

    def test_real_and_imaginary_scalar_parts_have_the_declared_complex_normalization(self):
        value = 0.4+0.2j
        d = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        real = model.scalar_stress(model.ETA, value.real, d.real, 0.6)["stress"]
        imag = model.scalar_stress(model.ETA, value.imag, d.imag, 0.6)["stress"]
        self.assertClose(real+imag, model.scalar_stress(model.ETA, value, d, 0.6)["stress"])

    def test_one_particle_covariance_and_zero_mean_field_in_finite_fock_space(self):
        data = model.massive_interference()
        annihilator = np.diag(np.sqrt(np.arange(1, 3)), 1)
        operators = [np.kron(annihilator, np.eye(3)), np.kron(np.eye(3), annihilator)]
        state = np.zeros(9, complex)
        state[3], state[1] = data["coefficients"]
        occupation = np.array([[np.vdot(state, a.conj().T @ b @ state) for b in operators] for a in operators])
        self.assertClose(occupation, data["occupation"])
        self.assertClose([np.vdot(state, a @ state) for a in operators], [0, 0])
        self.assertClose(np.vdot(state, state), 1)

    def test_normal_ordered_stress_matches_an_independent_fock_operator(self):
        data = model.massive_interference()
        annihilator = np.diag(np.sqrt(np.arange(1, 3)), 1)
        operators = np.array([np.kron(annihilator, np.eye(3)), np.kron(np.eye(3), annihilator)])
        state = np.zeros(9, complex)
        state[3], state[1] = data["coefficients"]
        p = data["covectors"]
        u = np.exp(1j*p @ data["point"])/np.sqrt(-2*p[:, 0]*data["volume"])
        phi = np.einsum("r,rij->ij", u, operators)
        dphi = 1j*np.einsum("r,rm,rij->mij", u, p, operators)
        energy = (np.einsum("mn,mji,njk->ik", model.ETA, dphi.conj(), dphi)
                  +data["mass"]**2*phi.conj().T @ phi)
        stress = np.array([[np.vdot(state, (dm.conj().T @ dn+dn.conj().T @ dm-model.ETA[m, n]*energy) @ state).real
                            for n, dn in enumerate(dphi)] for m, dm in enumerate(dphi)])
        self.assertClose(stress, data["coherent_stress"])

    def test_rank_one_occupation_matches_the_classical_solution_stress_not_its_field_mean(self):
        data = model.massive_interference()
        self.assertClose(data["scalar"]["stress"], data["coherent_stress"])
        self.assertGreater(np.linalg.norm(data["coherent_stress"]), 0)

    def test_massive_modes_are_on_shell_and_the_source_is_conserved(self):
        for phase in (0, 0.7, np.pi):
            data = model.massive_interference(phase=phase)
            self.assertClose(data["scalar"]["KG"], 0)
            self.assertClose(data["scalar"]["divergence"], np.zeros(4))

    def test_relative_phase_changes_local_stress_without_changing_mass_number_or_total_energy(self):
        plus, minus = [model.massive_interference(point=(0, 0, 0, 0), phase=p) for p in (0, np.pi)]
        self.assertEqual(plus["mass"], minus["mass"])
        self.assertClose(np.trace(plus["occupation"]), np.trace(minus["occupation"]))
        self.assertEqual(plus["total_energy"], minus["total_energy"])
        self.assertGreater(plus["coherent_stress"][0, 0], 2*minus["coherent_stress"][0, 0])

    def test_spatial_average_recovers_phase_independent_box_energy(self):
        for phase in (0, 1.1, np.pi):
            sources = [model.massive_interference(point=(0, x, 0, 0), phase=phase) for x in 2*np.pi*np.arange(16)/16]
            self.assertClose(np.mean([s["coherent_stress"][0, 0] for s in sources])*sources[0]["volume"],
                             sources[0]["total_energy"])

    def test_phase_average_is_the_incoherent_mixture(self):
        samples = [model.massive_interference(phase=p) for p in 2*np.pi*np.arange(8)/8]
        self.assertClose(np.mean([s["coherent_stress"] for s in samples], axis=0), samples[0]["mixed_stress"])

    def test_orthogonal_independent_fields_have_no_interference_cross_term(self):
        data = model.massive_interference()
        stresses = []
        for c, p in zip(data["coefficients"], data["covectors"]):
            values = model.mode_jets(data["point"], [c/np.sqrt(-2*p[0]*data["volume"])], [p])
            stresses.append(model.scalar_stress(model.ETA, values[0], values[1], data["mass"])["stress"])
        self.assertClose(sum(stresses), data["mixed_stress"])
        self.assertGreater(np.linalg.norm(sum(stresses)-data["coherent_stress"]), 1e-4)

    def test_interference_has_zero_mean_and_a_conserved_spacelike_fourier_wavevector(self):
        data = model.massive_interference()
        self.assertGreater(data["wavevector_squared"], 0)
        self.assertClose((model.ETA @ data["wavevector"]) @ data["interference_stress"], np.zeros(4))
        self.assertGreater(abs(np.sum(model.ETA*data["interference_stress"])), 1e-5)

    def test_linear_metric_is_in_harmonic_gauge_and_solves_all_linear_einstein_components(self):
        data = model.massive_interference()
        self.assertClose((model.ETA @ data["wavevector"]) @ data["bar_h"], np.zeros(4))
        self.assertClose(data["linearized_Einstein"], data["einstein_coupling"]*data["interference_stress"])

    def test_linear_response_agrees_with_the_independent_nonlinear_curvature_to_first_order(self):
        data = model.massive_interference()
        errors = []
        for epsilon in (0.2, 0.1, 0.05):
            actual = model.geometry.metric_curvature(model.ETA+epsilon*data["h"],
                                                     epsilon*data["h_first"], epsilon*data["h_second"])
            errors.append(np.linalg.norm(actual["einstein"]/epsilon-data["linearized_Einstein"]))
        self.assertGreater(errors[0], errors[1]*1.8)
        self.assertGreater(errors[1], errors[2]*1.8)

    def test_linear_witness_does_not_claim_to_solve_the_homogeneous_positive_source(self):
        data = model.massive_interference()
        residual = data["linearized_Einstein"]-data["einstein_coupling"]*data["coherent_stress"]
        self.assertClose(residual, -data["einstein_coupling"]*data["mixed_stress"])
        self.assertGreater(np.linalg.norm(residual), 1e-4)

    def test_null_flux_and_its_two_derivatives_match_independent_differences(self):
        u, step = 0.3, 1e-4
        middle = model.null_wave(u, phase=0.7)
        plus, minus = [model.null_wave(u+s*step, phase=0.7) for s in (1, -1)]
        self.assertClose((plus["rho"]-minus["rho"])/(2*step), middle["rho_first"], atol=2e-8)
        self.assertClose((plus["rho_first"]-minus["rho_first"])/(2*step), middle["rho_second"], atol=2e-8)

    def test_sourced_h_profile_jets_match_finite_differences(self):
        point, step = np.array([0.1, 0.3, -0.2, 0.4]), 1e-5
        profile = model.sourced_profile(point, phase=0.7)
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = [model.sourced_profile(point+s*delta, phase=0.7) for s in (1, -1)]
            self.assertClose((plus["amplitude"]-minus["amplitude"])/(2*step), profile["gradient"][mu])
            self.assertClose((plus["gradient"]-minus["gradient"])/(2*step), profile["hessian"][mu], atol=1e-9)

    def test_cole_hopf_and_full_sourced_profile_equations_hold(self):
        for phase in (0, 0.8, np.pi):
            profile = model.sourced_profile((0.1, 0.2, 0, 0.3), phase=phase)
            self.assertClose(profile["profile_residual"], 0)
            self.assertClose(profile["Helmholtz_residual"], 0)

    def test_independent_full_einstein_equations_include_both_matter_and_hc_stress(self):
        for phase in (0, 0.8, np.pi):
            data = model.sourced_branch(phase=phase)
            self.assertClose(data["Einstein_residual"], np.zeros((4, 4)))
            self.assertGreater(np.linalg.norm(data["hc"]["stress"]), 1e-6)
            self.assertGreater(np.linalg.norm(data["matter"]["stress"]), 0.01)

    def test_null_matter_and_both_axis_scalar_equations_are_solved_without_freezing_u(self):
        data = model.sourced_branch()
        self.assertClose(data["matter"]["KG"], 0)
        self.assertClose(data["matter"]["divergence"], np.zeros(4))
        self.assertClose([data["hc"]["h_EL"], data["hc"]["u_EL"]], [0, 0])
        self.assertGreater(np.linalg.norm(data["hc"]["axis_reaction_if_independent"]), 1e-6)

    def test_source_changes_the_previous_harmonic_law_instead_of_being_appended_to_it(self):
        data = model.sourced_branch()
        profile = data["profile"]
        old_residual = profile["hessian"][1, 1]+0.4*profile["gradient"][1]**2
        self.assertGreater(abs(old_residual), 0.1)
        self.assertClose(old_residual, -profile["wave"]["rho"]/0.4)

    def test_same_massless_mode_populations_can_change_null_curvature_by_relative_phase(self):
        plus, minus = [model.sourced_branch(point=(0, 0, 0, 0), phase=p) for p in (0, np.pi)]
        self.assertClose(plus["profile"]["wave"]["rho"], 0.5)
        self.assertClose(minus["profile"]["wave"]["rho"], 0.02)
        self.assertClose(plus["geometry"]["einstein"][0, 0]/minus["geometry"]["einstein"][0, 0], 25)

    def test_probe_derived_pullbacks_keep_all_declared_parent_equations(self):
        for readout in ("symmetric_cross", "ART"):
            data = model.sourced_branch(point=(0.01, 0.02, -0.03, 0.01), readout=readout)
            self.assertClose(data["coframe_constraint"], np.zeros((4, 4)))
            self.assertClose(data["background"]["reference_residual"], np.zeros((3, 4)))
            self.assertClose(data["Einstein_residual"], np.zeros((4, 4)), atol=5e-9)
            self.assertClose([data["hc"]["h_EL"], data["hc"]["u_EL"], abs(data["matter"]["KG"])], [0, 0, 0], atol=2e-9)

    def test_adding_mass_invalidates_the_unchanged_null_wave_and_transverse_einstein_equations(self):
        data = model.sourced_branch()
        p = data["profile"]
        phi, dphi, ddphi = p["wave"]["jets"][:3]
        restored = model.scalar_equations(data["metric_jets"]["metric"], data["metric_jets"]["first"],
                                          phi, dphi*model.N_COV, ddphi*np.outer(model.N_COV, model.N_COV), 0.6)
        self.assertClose(restored["KG"], -0.6**2*phi)
        self.assertGreater(abs(restored["KG"]), 0.01)
        self.assertClose(restored["stress"][1, 1]-data["matter"]["stress"][1, 1], -0.6**2*abs(phi)**2)

    def test_zero_source_limit_is_a_flat_constant_harmonic_branch(self):
        data = model.sourced_branch(amplitudes=(0, 0))
        self.assertClose(data["total_stress"], np.zeros((4, 4)))
        self.assertClose(data["geometry"]["riemann"], np.zeros((4, 4, 4, 4)))

    def test_positive_cosine_patch_cannot_be_extended_across_its_zero(self):
        with self.assertRaises(ValueError):
            model.sourced_profile((0, 4, 0, 0))

    def test_invalid_metric_negative_mass_and_nonpositive_occupation_are_rejected(self):
        with self.assertRaises(ValueError):
            model.scalar_stress(np.eye(4), 1, np.zeros(4))
        with self.assertRaises(ValueError):
            model.scalar_stress(model.ETA, 1, np.zeros(4), -1)
        data = model.massive_interference()
        with self.assertRaises(ValueError):
            model.mode_source(data["point"], data["covectors"], np.diag([1, -0.1]), 0.6, data["volume"])

    def test_off_shell_modes_cannot_be_labeled_as_the_quantum_free_source(self):
        data = model.massive_interference()
        with self.assertRaises(ValueError):
            model.mode_source(data["point"], data["covectors"]+0.1, data["occupation"], 0.6, data["volume"])

    def test_saved_report_is_reproducible_and_retains_quantum_and_native_scope(self):
        saved = json.loads((ROOT / "analysis/HC_Quantum_State_Gravity.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, model.evaluate())
        self.assertFalse(saved["main_TeX_changed"])
        self.assertTrue(saved["quantum_scope"]["reference_vacuum_stress_counterterms_and_stress_fluctuations_not_computed"])
        self.assertTrue(saved["massive_linear_response"]["no_semiclassical_validity_certificate_for_the_one_particle_state"])


if __name__ == "__main__":
    unittest.main()
