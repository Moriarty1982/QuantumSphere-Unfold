"""Stress-derived weak metric, full variational reaction, free radiation and causality."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("stress_metric_pullback", ROOT / "analysis/HC_Stress_Metric_Pullback.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCStressMetricPullbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grid = model.grid_probe()
        cls.psi, cls.first = cls.grid["psi"], cls.grid["first"]
        cls.mass = cls.grid["modes"]["mass"]
        cls.stress = model.grid_stress(cls.psi, cls.first, cls.mass)["stress"]
        cls.response = model.periodic_response(cls.stress)
        cls.point = np.array([0.08, 0.2, -0.3, 0.1])

    def setUp(self):
        self.rng = np.random.default_rng(738)

    def assertClose(self, actual, expected, atol=3e-10):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=3e-8)

    def variation(self):
        points = self.grid["points"]
        coefficients = self.rng.normal(size=(3, 4))+1j*self.rng.normal(size=(3, 4))
        momenta = np.array([[2, -1], [-1, 2], [1, 0]])
        factors = np.exp(1j*np.einsum("rm,...m->r...", momenta, points[..., 1:3]))
        amplitudes = factors[..., None]*coefficients[:, None, None, :]/10
        value = np.sum(amplitudes, axis=0)
        covectors = np.column_stack((-self.grid["modes"]["energy"]*np.ones(3), momenta, np.zeros(3)))
        first = 1j*np.einsum("rm,r...i->m...i", covectors, amplitudes)
        return value, first

    def test_trace_reversal_is_an_involutive_self_adjoint_operator(self):
        a, b = self.rng.normal(size=(4, 4)), self.rng.normal(size=(4, 4))
        a, b = (a+a.T)/2, (b+b.T)/2
        self.assertClose(model.reverse(model.reverse(a)), a)
        self.assertClose(model.pairing(model.reverse(a), b), model.pairing(a, model.reverse(b)))

    def test_static_response_inverts_the_gauge_fixed_operator_on_nonzero_modes(self):
        self.assertClose(model.gauge_fixed_operator(self.response["h"]), self.response["projected_source"])
        self.assertClose(np.mean(self.response["h"], axis=(0, 1)), np.zeros((4, 4)))

    def test_harmonic_constraint_and_full_einstein_tensor_for_the_on_shell_projected_source(self):
        modes = self.grid["modes"]
        q = modes["covectors"][1]-modes["covectors"][0]
        h_at_origin = self.response["h"][0, 0]
        self.assertClose((model.ETA @ q) @ model.reverse(h_at_origin), np.zeros(4))
        actual = model.dirac.state.linearized_einstein(self.response["second"][:, :, 0, 0])
        self.assertClose(actual, self.response["projected_source"][0, 0])

    def test_nonconserved_off_shell_source_does_not_automatically_solve_unfixed_einstein(self):
        scalar = np.cos(self.grid["points"][..., 1])
        tensor = scalar[..., None, None]*np.diag([0, 1, 0, 0])
        response = model.periodic_response(tensor)
        self.assertClose(model.gauge_fixed_operator(response["h"]), tensor)
        actual = model.dirac.state.linearized_einstein(response["second"][:, :, 0, 0])
        self.assertGreater(np.linalg.norm(actual-tensor[0, 0]), 0.5)

    def test_zero_mode_is_recorded_and_cannot_be_erased_as_a_full_positive_source_solution(self):
        self.assertGreater(np.linalg.norm(self.response["omitted_zero_mode"]), 0.01)
        constant = np.broadcast_to(np.diag([1, 0, 0, 0]), self.stress.shape)
        response = model.periodic_response(constant)
        self.assertClose(response["h"], np.zeros_like(constant))
        self.assertClose(response["omitted_zero_mode"], np.diag([1, 0, 0, 0]))

    def test_periodic_response_is_self_adjoint_with_the_lorentz_tensor_pairing(self):
        x, y = self.grid["points"][..., 1], self.grid["points"][..., 2]
        a, b = self.rng.normal(size=(4, 4)), self.rng.normal(size=(4, 4))
        a = (a+a.T)/2*np.cos(x-y)[..., None, None]
        b = (b+b.T)/2*(np.cos(x-y)+np.sin(2*x))[..., None, None]
        self.assertClose(model.pairing(a, model.periodic_response(b)["h"]),
                         model.pairing(model.periodic_response(a)["h"], b))

    def test_response_jets_are_independent_spectral_derivatives(self):
        size = self.stress.shape[0]
        k = np.fft.fftfreq(size, 1/size)
        coefficients = np.fft.fftn(self.response["h"], axes=(0, 1))
        for mu, frequency in ((1, k[:, None]), (2, k[None, :])):
            actual = np.fft.ifftn(1j*frequency[..., None, None]*coefficients, axes=(0, 1)).real
            self.assertClose(actual, self.response["first"][mu])

    def test_stationary_parent_value_equals_the_one_quarter_induced_action(self):
        h = 0.2*self.response["h"]
        self.assertClose(model.parent_action(self.stress, h), model.induced_action(self.stress))
        self.assertClose(model.pairing(h, self.stress)/4, model.induced_action(self.stress))

    def test_parent_metric_variation_vanishes_on_the_eliminated_metric(self):
        h = 0.2*self.response["h"]
        delta = np.cos(self.grid["points"][..., 1]-self.grid["points"][..., 2])[..., None, None]*np.eye(4)
        step = 1e-5
        actual = (model.parent_action(self.stress, h+step*delta)-model.parent_action(self.stress, h-step*delta))/(2*step)
        self.assertClose(actual, 0)

    def test_reduced_source_variation_has_the_envelope_one_half_factor(self):
        delta = np.cos(self.grid["points"][..., 1]-self.grid["points"][..., 2])[..., None, None]*np.diag([1, 0.4, -0.1, 0])
        step = 1e-5
        actual = (model.induced_action(self.stress+step*delta)-model.induced_action(self.stress-step*delta))/(2*step)
        predicted = model.pairing(0.2*self.response["h"], delta)/2
        self.assertClose(actual, predicted)
        self.assertGreater(abs(predicted), 1e-5)

    def test_naive_substitution_into_only_the_matter_coupling_doubles_the_reaction(self):
        delta = self.response["projected_source"]
        step = 1e-4
        def naive(stress):
            return model.pairing(0.2*model.periodic_response(stress)["h"], stress)/2
        actual = (naive(self.stress+step*delta)-naive(self.stress-step*delta))/(2*step)
        correct = model.pairing(0.2*self.response["h"], delta)/2
        self.assertClose(actual, 2*correct)
        self.assertGreater(abs(correct), 1e-7)

    def test_batch_stress_and_operator_match_the_existing_single_point_dirac_implementation(self):
        for i, j in ((0, 0), (3, 5), (12, 7)):
            data = model.dirac.dirac_data(self.psi[i, j][None], self.first[:, i, j, None], np.array([[self.mass]]))
            self.assertClose(data["stress"], self.stress[i, j])
            direct = model.dirac.operator_change(self.psi[i, j], self.first[:, i, j], self.response["h"][i, j], self.response["first"][:, i, j])
            batch = model.grid_operator_change(self.psi, self.first, self.response["h"], self.response["first"])
            self.assertClose(direct, batch[i, j])

    def test_actual_spinor_variation_matches_the_common_metric_dirac_reaction(self):
        variation, derivative = self.variation()
        def action(scale):
            return model.induced_action(model.grid_stress(self.psi+scale*variation, self.first+scale*derivative, self.mass)["stress"])
        step = 1e-5
        actual = (action(step)-action(-step))/(2*step)
        reaction = model.grid_operator_change(self.psi, self.first, 0.2*self.response["h"], 0.2*self.response["first"])
        predicted = 2*np.mean(np.einsum("...i,ij,...j->...", variation.conj(), model.BETA, reaction).real)
        self.assertClose(actual, predicted, atol=2e-9)
        self.assertGreater(abs(predicted), 1e-7)

    def test_off_shell_spinor_variation_also_keeps_the_measure_times_flat_residual(self):
        variation, derivative = self.variation()
        psi, first = self.psi+0.3*variation, self.first+0.3*derivative
        data = model.grid_stress(psi, first, self.mass)
        response = model.periodic_response(data["stress"])
        h = 0.2*response["h"]
        def action(scale):
            return model.induced_action(model.grid_stress(psi+scale*variation, first+scale*derivative, self.mass)["stress"])
        step = 1e-5
        actual = (action(step)-action(-step))/(2*step)
        reaction = model.grid_operator_change(psi, first, h, 0.2*response["first"])
        measure = np.einsum("mn,...mn->...", model.ETA, h)[..., None]*data["residual"]/2
        predicted = 2*np.mean(np.einsum("...i,ij,...j->...", variation.conj(), model.BETA, reaction+measure).real)
        naive = 2*np.mean(np.einsum("...i,ij,...j->...", variation.conj(), model.BETA, reaction).real)
        self.assertClose(actual, predicted, atol=3e-8)
        self.assertGreater(abs(predicted-naive), 1e-6)

    def test_global_common_phase_leaves_source_metric_and_induced_action_unchanged(self):
        phase = np.exp(1.7j)
        shifted = model.grid_stress(phase*self.psi, phase*self.first, self.mass)["stress"]
        self.assertClose(shifted, self.stress)
        self.assertClose(model.periodic_response(shifted)["h"], self.response["h"])
        self.assertClose(model.induced_action(shifted), model.induced_action(self.stress))

    def test_bilinear_metric_and_quartic_induced_action_have_the_right_amplitude_scaling(self):
        scale = 1.4
        stress = model.grid_stress(scale*self.psi, scale*self.first, self.mass)["stress"]
        self.assertClose(model.periodic_response(stress)["h"], scale**2*self.response["h"])
        self.assertClose(model.induced_action(stress), scale**4*model.induced_action(self.stress))

    def test_relative_phase_moves_the_local_metric_but_not_this_translation_invariant_integrated_action(self):
        other = model.grid_probe(phase=np.pi)
        stress = model.grid_stress(other["psi"], other["first"], self.mass)["stress"]
        response = model.periodic_response(stress)
        self.assertGreater(np.linalg.norm(response["h"]-self.response["h"]), 0.01)
        self.assertClose(model.induced_action(stress), model.induced_action(self.stress))

    def test_free_wave_has_zero_einstein_tensor_but_nonzero_gauge_invariant_linear_curvature(self):
        wave = model.wave_jets(self.point)
        self.assertClose(model.dirac.state.linearized_einstein(wave[2]), np.zeros((4, 4)))
        riemann = model.linear_riemann(wave[2])
        self.assertGreater(abs(riemann[0, 1, 0, 1]), 0.01)
        self.assertClose(riemann[0, 1, 0, 1], -wave[2][0, 0, 1, 1]/2)

    def test_free_wave_riemann_agrees_with_the_independent_nonlinear_connection_to_first_order(self):
        h, first, second = model.wave_jets(self.point)
        epsilon = 1e-5
        curvature = model.dirac.geometry.metric_curvature(model.ETA+epsilon*h, epsilon*first, epsilon*second)
        self.assertClose(curvature["lower_riemann"]/epsilon, model.linear_riemann(second), atol=2e-8)

    def test_free_wave_jets_match_independent_differences(self):
        h, first, second = model.wave_jets(self.point)
        step = 1e-5
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = model.wave_jets(self.point+delta), model.wave_jets(self.point-delta)
            self.assertClose((plus[0]-minus[0])/(2*step), first[mu])
            self.assertClose((plus[1]-minus[1])/(2*step), second[mu])

    def test_two_weak_metrics_with_the_same_source_have_different_curvature(self):
        original = model.dirac.metric_jets(self.point)["h"][2]
        changed = original+model.wave_jets(self.point)[2]
        self.assertClose(model.dirac.state.linearized_einstein(changed), model.dirac.state.linearized_einstein(original))
        self.assertGreater(np.linalg.norm(model.linear_riemann(changed)-model.linear_riemann(original)), 0.01)

    def test_free_wave_probe_reaction_has_zero_correction_initial_data(self):
        value, first = model.wave_probe_correction(np.array([0, 0.2, -0.3, 0.1]))
        self.assertClose(value, np.zeros(4))
        self.assertGreater(np.linalg.norm(first[0]), 1e-5)

    def test_free_wave_probe_reaction_derivatives_match_independent_differences(self):
        value, first = model.wave_probe_correction(self.point)
        step = 1e-5
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = model.wave_probe_correction(self.point+delta)[0], model.wave_probe_correction(self.point-delta)[0]
            self.assertClose((plus-minus)/(2*step), first[mu])

    def test_free_wave_reaction_satisfies_the_full_linear_dirac_equation(self):
        modes, psi, first, _ = model.dirac.probe_jets(self.point)
        h, dh, _ = model.wave_jets(self.point)
        value, derivative = model.wave_probe_correction(self.point)
        residual = (1j*np.einsum("mij,mj->i", model.GAMMA, derivative)-modes["mass"]*value
                    +model.dirac.operator_change(psi, first, h, dh))
        self.assertClose(residual, np.zeros(4))
        self.assertGreater(np.linalg.norm(value), 1e-5)

    def test_complete_wave_plus_source_branch_keeps_all_first_order_equations(self):
        result = model.with_free_wave(self.point)
        self.assertClose(result["linear_Einstein_residual"], np.zeros((4, 4)))
        self.assertClose(result["linear_Dirac_residual"], np.zeros(4))

    def test_wave_plus_source_has_second_order_full_equation_remainders(self):
        samples = [model.with_free_wave(self.point, strength=s) for s in (0.04, 0.02, 0.01)]
        for field in ("Einstein_residual", "Dirac_residual"):
            errors = [np.linalg.norm(s[field]) for s in samples]
            self.assertClose(errors[0]/errors[1], 4, atol=0.005)
            self.assertClose(errors[1]/errors[2], 4, atol=0.005)

    def test_retarded_kernel_is_lower_triangular_and_has_the_correct_weighted_adjoint(self):
        times = np.linspace(0, 2, 31)**1.2
        data = model.retarded_kernel(times)
        self.assertClose(np.triu(data["response"]), np.zeros((31, 31)))
        a, b = self.rng.normal(size=31), self.rng.normal(size=31)
        self.assertClose(np.sum(a*data["weights"]*(data["response"] @ b)),
                         np.sum(data["adjoint"] @ a*data["weights"]*b))

    def test_future_source_has_no_retarded_past_response_but_has_an_advanced_adjoint_response(self):
        data = model.retarded_kernel(np.linspace(0, 2, 31))
        source = np.zeros(31)
        source[-1] = 1
        self.assertClose((data["response"] @ source)[:-1], np.zeros(30))
        self.assertGreater(np.linalg.norm((data["adjoint"] @ source)[:-1]), 0.01)

    def test_single_history_retarded_action_variation_is_time_symmetric_not_causal(self):
        data = model.retarded_kernel(np.linspace(0, 2, 31))
        source, direction = self.rng.normal(size=(2, 31))
        def action(scale):
            varied = source+scale*direction
            return 0.2*np.sum(varied*data["weights"]*(data["response"] @ varied))/4
        step = 1e-5
        actual = (action(step)-action(-step))/(2*step)
        symmetric = 0.2*(data["response"]+data["adjoint"]) @ source/4
        self.assertClose(actual, np.sum(direction*data["weights"]*symmetric))
        self.assertGreater(np.linalg.norm(symmetric-0.2*data["response"] @ source/2), 0.001)

    def test_doubled_action_vanishes_physically_but_its_physical_left_variation_does_not(self):
        data = model.retarded_kernel(np.linspace(0, 2, 31))
        source, direction = self.rng.normal(size=(2, 31))
        self.assertEqual(model.doubled_action(source, source, data["response"], data["weights"]), 0)
        step = 1e-5
        actual = (model.doubled_action(source+step*direction, source, data["response"], data["weights"])
                  -model.doubled_action(source-step*direction, source, data["response"], data["weights"] ))/(2*step)
        prediction = 0.2*np.sum(direction*data["weights"]*(data["response"] @ source))/2
        self.assertClose(actual, prediction)
        self.assertGreater(abs(prediction), 1e-5)

    def test_doubled_physical_variation_has_no_future_source_contribution(self):
        data = model.retarded_kernel(np.linspace(0, 2, 31))
        source, direction = np.zeros(31), np.zeros(31)
        source[-1], direction[3] = 1, 1
        step = 1e-5
        actual = (model.doubled_action(source+step*direction, source, data["response"], data["weights"])
                  -model.doubled_action(source-step*direction, source, data["response"], data["weights"] ))/(2*step)
        self.assertClose(actual, 0)

    def test_doubled_off_physical_variation_keeps_both_average_and_difference_terms(self):
        data = model.retarded_kernel(np.linspace(0, 2, 31))
        left, right, direction = self.rng.normal(size=(3, 31))
        step = 1e-5
        actual = (model.doubled_action(left+step*direction, right, data["response"], data["weights"])
                  -model.doubled_action(left-step*direction, right, data["response"], data["weights"] ))/(2*step)
        gradient = 0.2*(data["response"] @ ((left+right)/2)+data["adjoint"] @ (left-right)/2)/2
        self.assertClose(actual, np.sum(direction*data["weights"]*gradient))

    def test_retarded_quadrature_converges_to_an_independent_forced_oscillator_solution(self):
        errors = []
        omega, nu = 1.3, 0.7
        for size in (31, 61, 121):
            t = np.linspace(0, 2, size)
            actual = model.retarded_kernel(t, omega)["response"] @ np.sin(nu*t)
            expected = (np.sin(nu*t)-nu/omega*np.sin(omega*t))/(omega**2-nu**2)
            errors.append(abs(actual[-1]-expected[-1]))
        self.assertClose(errors[0]/errors[1], 4, atol=0.01)
        self.assertClose(errors[1]/errors[2], 4, atol=0.01)

    def test_invalid_grid_tensor_and_time_data_are_rejected(self):
        with self.assertRaises(ValueError):
            model.periodic_response(np.zeros((8, 8, 4, 4)))
        with self.assertRaises(ValueError):
            model.retarded_kernel([0, 1, 0.5])
        with self.assertRaises(ValueError):
            model.pairing(np.zeros((4, 4)), 1j*np.ones((4, 4)))

    def test_saved_report_retains_native_gauge_zero_mode_and_causal_scope(self):
        saved = json.loads((ROOT / "analysis/HC_Stress_Metric_Pullback.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, model.evaluate())
        self.assertFalse(saved["main_TeX_changed"])
        self.assertTrue(saved["reconstruction"]["boundary_gauge_and_free_radiation_data_are_required"])
        self.assertTrue(saved["causal_variation_test"]["no_native_tensor_or_two_frame_identification_is_assumed"])


if __name__ == "__main__":
    unittest.main()
