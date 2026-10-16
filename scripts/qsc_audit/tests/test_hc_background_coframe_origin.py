"""Background provenance, exact triadic evolution and the total/readout boundary."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("background_origin", ROOT / "analysis/HC_Background_Coframe_Origin.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class HCBackgroundCoframeOriginTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(337)
        self.bg = audit.polynomial_background()

    def assertClose(self, actual, expected, atol=5e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=3e-9)

    def expansion(self, delta=None):
        fluctuation = 0.1*(self.rng.normal(size=(3, 4))+1j*self.rng.normal(size=(3, 4)))
        derivative = 0.1*(self.rng.normal(size=(4, 3, 4))+1j*self.rng.normal(size=(4, 3, 4)))
        return fluctuation, derivative, audit.background_expansion(
            self.bg["psi"], fluctuation, self.bg["derivatives"], derivative, self.bg["weights"], delta)

    def test_triadic_mass_operator_is_hermitian_with_a_real_bare_mass(self):
        omega = self.bg["mass_operator"]
        self.assertClose(omega, omega.conj().T)
        self.assertClose(np.diag(omega), [0.6, 0.6, 0.6])

    def test_two_probe_channels_couple_through_the_third_not_a_direct_entry(self):
        omega = self.bg["mass_operator"]
        self.assertEqual(omega[0, 1], 0)
        self.assertEqual(omega[0, 2], 4)
        self.assertEqual(omega[1, 2], 0.7)

    def test_reference_time_generator_is_hermitian(self):
        self.assertClose(self.bg["hamiltonian"], self.bg["hamiltonian"].conj().T)

    def test_mass_hamiltonian_anticommutes_with_the_spatial_alpha_matrices(self):
        h = self.bg["hamiltonian"]
        for k in self.bg["weights"][1:]:
            alpha = np.kron(np.eye(3), k)
            self.assertClose(h @ alpha+alpha @ h, np.zeros_like(h))

    def test_analytic_field_is_on_shell_at_the_origin(self):
        self.assertClose(self.bg["reference_residual"], np.zeros((3, 4)))

    def test_analytic_field_is_on_shell_away_from_the_origin(self):
        for _ in range(8):
            point = self.rng.uniform(-0.2, 0.2, 4)
            self.assertClose(audit.polynomial_background(point)["reference_residual"], np.zeros((3, 4)))

    def test_analytic_time_derivative_matches_independent_finite_differences(self):
        point, step = np.array([0.03, 0.02, -0.01, 0.04]), 1e-6
        field = audit.polynomial_background(point)
        delta = np.array([step, 0, 0, 0])
        numerical = (audit.polynomial_background(point+delta)["psi"]
                     -audit.polynomial_background(point-delta)["psi"])/(2*step)
        self.assertClose(field["derivatives"][0], numerical, atol=5e-10)

    def test_spatial_derivatives_match_independent_finite_differences(self):
        point, step = np.array([0.03, 0.02, -0.01, 0.04]), 1e-6
        field = audit.polynomial_background(point)
        for mu in range(1, 4):
            delta = step*np.eye(4)[mu]
            numerical = (audit.polynomial_background(point+delta)["psi"]
                         -audit.polynomial_background(point-delta)["psi"])/(2*step)
            self.assertClose(field["derivatives"][mu], numerical, atol=2e-10)

    def test_exact_zero_mass_eigenvalues_are_handled_without_dividing_by_zero(self):
        result = audit.polynomial_background([0.1, 0.02, -0.01, 0.03], mass=0, art_coupling=0, qft_coupling=0)
        self.assertTrue(np.all(np.isfinite(result["psi"])))
        self.assertClose(result["reference_residual"], np.zeros((3, 4)))

    def test_real_bare_mass_does_not_remove_the_channel_exchange(self):
        for mass in [0, 0.6, -1.0, 3.0]:
            result = audit.polynomial_background(mass=mass)
            self.assertClose(result["coframes"][0], np.eye(4))
            self.assertClose(result["mass_bilinears"].imag, [4, 0, -4])

    def test_phase_controls_the_channel_trace_not_an_imaginary_mass_parameter(self):
        for phase in [0, 0.3, np.pi/2, np.pi, -np.pi/2]:
            result = audit.polynomial_background(phase=phase)
            expected = 4*np.sin(phase)
            self.assertClose(np.trace(result["coframes"][0]), expected)
            self.assertClose(result["coframes"][0, 0, 0], expected-3)

    def test_selected_art_background_is_full_rank_identity_at_the_sample(self):
        self.assertClose(self.bg["coframes"][0], np.eye(4))
        self.assertEqual(np.linalg.matrix_rank(self.bg["coframes"][0]), 4)

    def test_selected_background_stays_nondegenerate_on_a_declared_local_patch(self):
        for t in [-0.01, 0, 0.01]:
            result = audit.polynomial_background([t, 0.02, -0.03, 0.01])
            self.assertGreater(np.linalg.det(result["coframes"][0]), 0.9)

    def test_local_selected_metric_has_lorentz_signature(self):
        result = audit.polynomial_background([0.01, 0.02, -0.03, 0.01])
        self.assertEqual(np.sum(np.linalg.eigvalsh(result["background_metric"]) < 0), 1)

    def test_selected_coframe_is_half_the_gradient_of_its_current(self):
        for point in [[0, 0, 0, 0], [0.03, 0.02, -0.01, 0.04]]:
            result = audit.polynomial_background(point)
            self.assertClose(result["coframes"][0], result["current_derivative"][0].T/2)

    def test_flat_background_coordinate_map_has_the_expected_jacobian(self):
        point, step = np.array([0.01, 0.02, -0.03, 0.01]), 1e-6
        jacobian = []
        for delta in step*np.eye(4):
            plus = audit.polynomial_background(point+delta)["currents"][0]/2
            minus = audit.polynomial_background(point-delta)["currents"][0]/2
            jacobian.append((plus-minus)/(2*step))
        self.assertClose(np.array(jacobian).T, audit.polynomial_background(point)["coframes"][0], atol=3e-10)

    def test_channel_current_divergence_equals_the_hermitian_coupling_exchange(self):
        for point in [[0, 0, 0, 0], [0.04, 0.02, 0.03, -0.01]]:
            result = audit.polynomial_background(point)
            self.assertClose(result["channel_divergence"], result["channel_exchange"])
        self.assertClose(self.bg["channel_divergence"], [8, 0, -8])

    def test_total_phase_current_is_conserved_even_when_channel_current_is_not(self):
        for t in [-0.1, 0, 0.1]:
            result = audit.polynomial_background([t, 0.02, -0.01, 0.03])
            self.assertClose(np.sum(result["channel_divergence"]), 0)

    def test_projector_commutator_gives_the_channel_imaginary_mass_bilinear(self):
        for point in [[0, 0, 0, 0], [0.04, 0.02, 0.03, -0.01]]:
            result = audit.polynomial_background(point)
            self.assertClose(result["ART_commutator_imaginary_mass"], result["mass_bilinears"][0].imag)

    def test_channel_complex_bilinears_sum_to_a_real_total(self):
        self.assertGreater(abs(self.bg["mass_bilinears"][0].imag), 3.9)
        self.assertClose(np.sum(self.bg["mass_bilinears"]).imag, 0)

    def test_original_full_coframe_is_not_solved_by_the_selected_background(self):
        self.assertClose(self.bg["total_coframe"], np.zeros((4, 4)))
        self.assertClose(self.bg["coframes"][2], -np.eye(4))

    def test_sum_of_channel_readouts_equals_the_full_original_bilinear(self):
        result = audit.polynomial_background([0.02, 0.03, -0.01, 0.04])
        total = audit.coframe(result["psi"], result["derivatives"], result["weights"])
        self.assertClose(total, result["total_coframe"])

    def test_common_global_phase_leaves_the_full_coframe_unchanged(self):
        phase = np.exp(0.3j)
        total = audit.coframe(phase*self.bg["psi"], phase*self.bg["derivatives"], self.bg["weights"])
        self.assertClose(total, self.bg["total_coframe"])

    def test_selected_readout_is_covariant_when_its_projector_is_transported(self):
        result = audit.polynomial_background([0.02, 0.03, -0.01, 0.04])
        raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
        u, _ = np.linalg.qr(raw)
        psi, derivative = u @ result["psi"], u @ result["derivatives"]
        p = u @ np.diag([1, 0, 0]) @ u.conj().T
        selected = np.array([[np.vdot(psi, p @ d @ k.T).real for d in derivative]
                             for k in result["weights"]])
        self.assertClose(selected, result["coframes"][0])

    def test_decoupling_art_from_the_mediator_removes_its_exchange_not_every_possible_rank(self):
        result = audit.polynomial_background(art_coupling=0)
        self.assertClose(result["mass_bilinears"][0].imag, 0)
        self.assertClose(np.trace(result["coframes"][0]), 0)
        self.assertEqual(np.linalg.matrix_rank(result["coframes"][0]), 4)

    def test_qft_channel_is_dynamically_populated_only_when_its_mediator_coupling_is_present(self):
        coupled = audit.polynomial_background([0.02, 0, 0, 0])
        decoupled = audit.polynomial_background([0.02, 0, 0, 0], qft_coupling=0)
        self.assertGreater(np.linalg.norm(coupled["psi"][1]), 0.01)
        self.assertClose(decoupled["psi"][1], np.zeros(4))

    def test_nonzero_real_mass_and_both_mediator_couplings_keep_all_reference_equations(self):
        result = audit.polynomial_background([0.07, 0.03, -0.01, 0.02], mass=1.2,
                                             art_coupling=3.1, qft_coupling=-0.8, phase=0.7)
        self.assertClose(result["reference_residual"], np.zeros((3, 4)))

    def test_readout_scale_is_an_explicit_extra_normalization(self):
        first = audit.coframe(self.bg["psi"][0:1], self.bg["derivatives"][:, 0:1], self.bg["weights"])
        second = audit.coframe(self.bg["psi"][0:1], self.bg["derivatives"][:, 0:1], self.bg["weights"], 2)
        self.assertClose(second, 2*first)

    def test_prepared_cross_coframe_is_full_rank_on_a_nonzero_time_patch(self):
        result = audit.polynomial_background([0.01, 0.02, -0.03, 0.01])
        for name in ("cross_ART_QFT", "symmetric_cross_coframe"):
            self.assertEqual(np.linalg.matrix_rank(result[name]), 4)
            self.assertGreater(abs(np.linalg.det(result[name])), 1e-8)

    def test_cross_coframe_is_not_automatically_nondegenerate_at_every_point(self):
        self.assertLess(np.linalg.matrix_rank(self.bg["cross_ART_QFT"], tol=1e-12), 4)
        self.assertLess(np.linalg.matrix_rank(self.bg["symmetric_cross_coframe"], tol=1e-12), 4)

    def test_symmetric_cross_readout_is_half_a_cross_current_gradient(self):
        point, step = np.array([0.01, 0.02, -0.03, 0.01]), 1e-6

        def coordinates(x):
            result = audit.polynomial_background(x)
            a, q = result["psi"][:2]
            return np.array([np.vdot(a, k @ q).real for k in result["weights"]])/2

        jacobian = [(coordinates(point+d)-coordinates(point-d))/(2*step) for d in step*np.eye(4)]
        self.assertClose(np.array(jacobian).T, audit.polynomial_background(point)["symmetric_cross_coframe"],
                         atol=3e-10)

    def test_cross_readout_disappears_when_the_qft_mediator_link_is_off(self):
        result = audit.polynomial_background([0.02, 0.03, -0.01, 0.04], qft_coupling=0)
        self.assertClose(result["cross_ART_QFT"], np.zeros((4, 4)))
        self.assertClose(result["cross_QFT_ART"], np.zeros((4, 4)))

    def test_background_expansion_is_exact_at_fixed_connection(self):
        _, _, result = self.expansion()
        self.assertClose(result["expansion_residual"], np.zeros((4, 4)))

    def test_background_expansion_keeps_all_connection_change_terms(self):
        delta = self.rng.normal(size=(4, 3, 3))+1j*self.rng.normal(size=(4, 3, 3))
        _, _, result = self.expansion(delta)
        self.assertClose(result["expansion_residual"], np.zeros((4, 4)))
        self.assertGreater(np.linalg.norm(result["connection_change"]), 0.1)

    def test_naive_background_plus_quadratic_fluctuation_misses_linear_cross_terms(self):
        _, _, result = self.expansion()
        error = result["total"]-result["background"]-result["quadratic_fluctuation"]
        self.assertClose(error, result["cross"])
        self.assertGreater(np.linalg.norm(error), 0.1)

    def test_fixed_connection_sign_average_cancels_linear_cross_terms(self):
        phi, dphi, first = self.expansion()
        second = audit.background_expansion(self.bg["psi"], -phi, self.bg["derivatives"], -dphi,
                                            self.bg["weights"])
        self.assertClose((first["total"]+second["total"])/2,
                         first["background"]+first["quadratic_fluctuation"])

    def test_correlated_connection_fluctuations_survive_the_same_sign_average(self):
        delta = self.rng.normal(size=(4, 3, 3))+1j*self.rng.normal(size=(4, 3, 3))
        phi, dphi, first = self.expansion(delta)
        second = audit.background_expansion(self.bg["psi"], -phi, self.bg["derivatives"], -dphi,
                                            self.bg["weights"], -delta)
        difference = (first["total"]+second["total"])/2-first["background"]-first["quadratic_fluctuation"]
        self.assertGreater(np.linalg.norm(difference), 0.1)

    def test_displayed_kernel_modulus_has_seven_real_directions_before_a_slice_is_chosen(self):
        q = audit.kernel_real_slice()["displayed_real_form"]
        self.assertEqual(q.shape, (7, 7))
        self.assertEqual(np.sum(np.linalg.eigvalsh(q) < 0), 1)
        self.assertEqual(np.sum(np.linalg.eigvalsh(q) > 0), 6)

    def test_declared_fixed_phase_real_slices_give_a_lorentz_pullback(self):
        for phases in [[0, 0, 0], [0.2, -0.7, 1.1]]:
            self.assertClose(audit.kernel_real_slice(phases)["pullback"], audit.geometry.ETA)

    def test_one_clock_covector_alone_cannot_form_a_rank_four_coframe(self):
        clock, direction = self.rng.normal(size=4), self.rng.normal(size=4)
        self.assertEqual(np.linalg.matrix_rank(np.outer(direction, clock)), 1)

    def test_all_native_source_anchor_labels_are_real(self):
        for anchor in audit.evaluate()["source_anchors"]:
            text = (ROOT / anchor["path"]).read_text(encoding="utf-8")
            self.assertIn(r"\label{"+anchor["label"]+"}", text)

    def test_native_lensing_source_already_has_the_mixed_readout_but_labels_geometry_hypothetical(self):
        source = (ROOT / "sources/research/parts/v470/12_structural_core.tex").read_text(encoding="utf-8")
        self.assertIn("E^{a}_{\\mu,\\mathrm{cross}}", source)
        self.assertIn("Hypothesis-grade; not yet theorem-level", source)

    def test_saved_report_reproduces_the_calculation_and_retains_the_scope_boundary(self):
        report = audit.evaluate()
        saved = json.loads((ROOT / "analysis/HC_Background_Coframe_Origin.json").read_text(encoding="utf-8"))
        self.assertEqual(report, saved)
        self.assertFalse(report["main_TeX_changed"])
        self.assertTrue(report["remaining_native_burdens"]["no_native_gauge_Gauss_projector_or_Einstein_solution_claim"])
        self.assertIn("degenerate", report["exact_reference_Dirac_example"]["does_not_solve_the_original_full_bilinear_coframe"])

    def test_bad_shapes_and_nonreal_coefficients_are_rejected(self):
        with self.assertRaises(ValueError):
            audit.polynomial_background([0, 0, 0])
        with self.assertRaises(ValueError):
            audit.triadic_mass(mass=1j)
        with self.assertRaises(ValueError):
            audit.background_expansion(self.bg["psi"], np.zeros((2, 4)), self.bg["derivatives"],
                                       self.bg["derivatives"], self.bg["weights"])
        with self.assertRaises(ValueError):
            audit.coframe(self.bg["psi"], self.bg["derivatives"], self.bg["weights"], scale=0)


if __name__ == "__main__":
    unittest.main()
