"""Compatible finite jets are not an evolved solution of the odd-cross Cartan parent."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_compatible_jets", ROOT / "analysis/HC_Cartan_Compatible_Jets.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanCompatibleJetsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.constructed = model.solve_compatible_first()
        cls.data = cls.constructed["data"]
        cls.second = cls.constructed["second"]
        cls.report = model.evaluate(cls.constructed)
        cls.fields = model.taylor_fields(cls.constructed, np.zeros(4))

    def assertClose(self, actual, expected, atol=1e-10, rtol=2e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_complex_real_coordinates_roundtrip(self):
        z = np.arange(48).reshape(4, 3, 4)*(1+0.4j)
        self.assertClose(model.complexify(model.realify(z), z.shape), z)

    def test_bad_real_vector_dimension_is_rejected(self):
        with self.assertRaises(ValueError):
            model.complexify(np.zeros(95), (4, 3, 4))

    def test_no_resonance_matrix_or_readout_weight_was_changed(self):
        self.assertClose(model.MASS, [[0.6, 0, 4], [0, 0.6, 0.7], [4, 0.7, 0.6]])
        self.assertClose(model.Q, model.odd.Q_PHASE)

    def test_weighted_mass_uses_the_hermitian_part_not_a_complex_ordered_expectation(self):
        p = self.data["psi"]
        h = (model.Q @ model.MASS+model.MASS @ model.Q)/2
        self.assertClose(model.weighted_mass(p), np.vdot(p, h @ p @ model.BETA.T).real)

    def test_preparation_fixes_the_required_minus_four_by_amplitude_not_by_masses(self):
        p = self.data["psi"]
        self.assertClose(model.weighted_mass(p), -4)
        self.assertClose(model.normalize_probe(0.3*p), p)

    def test_positive_or_zero_weighted_mass_is_not_silently_normalized(self):
        for p in (self.data["psi"].conj(), np.zeros((3, 4))):
            with self.assertRaises(ValueError):
                model.normalize_probe(p)

    def test_wrong_spinor_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            model.normalize_probe(np.ones((4, 4)))

    def test_first_linear_system_has_39_conditions_and_57_free_derivatives(self):
        self.assertEqual(self.data["matrix"].shape, (40, 96))
        self.assertEqual(self.data["rank"], 39)
        self.assertEqual(self.data["nullspace"].shape, (96, 57))
        self.assertClose(self.data["matrix"] @ self.data["nullspace"], 0)

    def test_weighted_mass_identity_is_the_exact_missing_linear_equation(self):
        chi = model.Q @ self.data["psi"]
        left = np.concatenate((np.eye(4).reshape(-1), model.realify(chi)))
        self.assertClose(left @ self.data["matrix"], 0)
        self.assertClose(left @ self.data["rhs"], 4+model.weighted_mass(self.data["psi"]))

    def test_unnormalized_first_data_do_not_satisfy_both_equations(self):
        p = self.data["psi"]*0.7
        wrong = model.first_jet(p)
        self.assertGreater(np.linalg.norm(wrong["linear_residual"]), 0.1)

    def test_final_covariant_jet_reconstructs_its_own_coframe(self):
        c = model.odd.channels(self.data["psi"], self.data["covariant"])["odd"]
        self.assertClose(c, np.eye(4))
        self.assertEqual(np.linalg.matrix_rank(c), 4)

    def test_same_connection_and_metric_solve_the_complete_real_probe_residual(self):
        result = model.probe_check(self.data, self.second["multiplier_first"])
        self.assertClose(result["symmetric"], 0)
        self.assertClose(result["covariant"].reshape(4, 3, 4), self.data["covariant"])

    def test_real_action_defect_is_checked_not_assumed_from_the_ordered_equation(self):
        result = model.probe_check(self.data, self.second["multiplier_first"])
        self.assertClose(result["defect"], 0)
        self.assertClose(model.covariant_probe_residual(self.data["psi"], self.data["covariant"]), 0)

    def test_point_cartan_equation_uses_the_same_probe_source(self):
        _, source = model.cartan.spin_maps(np.eye(4), self.data["psi"])
        h = model.cartan.contorsion_hessian(np.eye(4))
        self.assertClose(h @ model.cartan.pack(self.data["omega"])+source, 0)
        self.assertGreater(np.linalg.norm(self.data["omega"]), 0.1)

    def test_state_is_in_the_previous_spacelike_weighted_axial_domain(self):
        _, a = model.cartan.axial_currents(self.data["psi"])
        self.assertGreater(a @ model.ETA @ a, 3.)

    def test_raw_least_norm_first_jet_fails_the_next_compatibility_gate(self):
        self.assertGreater(self.constructed["history"][0], 8.)
        self.assertGreater(np.linalg.norm(self.constructed["parameters"]), 0.1)

    def test_compatibility_correction_uses_only_free_first_derivatives(self):
        original = model.first_jet(self.data["psi"])
        changed = model.change_first(original, self.constructed["parameters"])
        self.assertClose(changed["first"], self.data["first"])
        self.assertClose(changed["psi"], original["psi"])
        self.assertClose(changed["omega"], original["omega"])

    def test_full_symmetric_second_jet_and_multiplier_system_sizes(self):
        self.assertEqual(self.second["matrix"].shape, (84, 464))
        self.assertEqual(self.second["rank"], 68)
        self.assertEqual(self.constructed["left_null"].shape, (84, 16))

    def test_second_derivatives_are_holonomic_not_independent_ordered_mixed_partials(self):
        self.assertClose(self.second["coframe_second"], self.second["coframe_second"].swapaxes(0, 1))
        self.assertClose(self.second["psi_second"], self.second["psi_second"].swapaxes(0, 1))

    def test_first_derivative_of_constraint_is_satisfied_in_all_four_directions(self):
        self.assertClose(self.second["constraint_first_residual"], 0)
        self.assertClose(model.prolonged_constraint(self.data, self.second["psi_second"], self.second["omega_first"]), 0)

    def test_all_independent_coframe_euler_components_are_satisfied(self):
        self.assertClose(self.second["coframe_Euler_residual"], 0)
        r = model.cartan.curvature_upper(self.data["omega"], self.second["omega_first"])
        fe = model.cartan.coframe_euler(np.eye(4), self.data["psi"], self.data["first"], self.data["omega"],
                                       r, model.MASS, np.zeros((4, 4)))
        self.assertClose(fe, 0)

    def test_multiplier_gradient_is_nonzero_but_has_the_declared_zero_divergence(self):
        self.assertGreater(np.linalg.norm(self.second["multiplier_first"]), 1.)
        self.assertClose(np.einsum("mam->a", self.second["multiplier_first"]), 0)

    def test_successful_solver_is_not_just_a_small_projected_residual(self):
        self.assertTrue(self.constructed["converged"])
        self.assertLess(np.linalg.norm(self.second["residual"]), 1e-10)
        self.assertLess(self.constructed["history"][-1], 1e-10)
        self.assertTrue(all(a > b for a, b in zip(self.constructed["history"], self.constructed["history"][1:])))

    def test_taylor_fields_match_all_origin_values_and_first_probe_derivatives(self):
        self.assertClose(self.fields["psi"], self.data["psi"])
        self.assertClose(self.fields["first_psi"], self.data["first"])
        self.assertClose(self.fields["coframe"], np.eye(4))
        self.assertClose(self.fields["first_coframe"], 0)
        self.assertClose(self.fields["omega"], self.data["omega"])
        self.assertClose(self.fields["multiplier"], 0)

    def test_taylor_fields_have_own_frame_constraint_and_real_probe_residual_zero_at_origin(self):
        self.assertClose(self.fields["constraint"], 0)
        self.assertClose(self.fields["probe"]["symmetric"], 0)
        self.assertClose(self.fields["Cartan_residual"], 0)

    def test_cartan_equation_is_differentiated_through_the_same_auxiliary_connection(self):
        self.assertLess(self.report["independent_Taylor_field_checks"]["independent_connection_first_difference_error"], 1e-7)

    def test_coframe_equation_survives_independent_finite_difference_curvature(self):
        self.assertLess(self.report["independent_Taylor_field_checks"]["coframe_Euler_with_independent_curvature_error"], 1e-7)

    def test_current_ward_identity_includes_the_nonconstant_multiplier_density(self):
        fields = model.taylor_fields(self.constructed, np.array([0.001, 0, 0, 0]))
        r = fields["probe"]
        p = fields["psi"].reshape(-1)
        self.assertClose(r["current_divergence"], 2*np.vdot(p, r["symmetric"]).imag)

    def test_canonical_metric_value_does_not_mean_flat_geometry(self):
        self.assertClose(self.fields["bundle"]["metric"], model.ETA)
        self.assertGreater(abs(self.fields["bundle"]["curvature"]["scalar"]), 3.)
        self.assertGreater(np.linalg.norm(self.fields["bundle"]["curvature"]["riemann"]), 8.)

    def test_probe_temporal_form_is_strictly_positive_at_the_point(self):
        self.assertClose(self.fields["weights"][0], np.eye(12))
        self.assertGreater(np.linalg.eigvalsh(self.fields["weights"][0])[0], 0.9)

    def test_conservative_temporal_bound_is_strictly_positive(self):
        bound = model.temporal_ball_bound(self.constructed)
        self.assertGreater(bound["radius_in_unscaled_comparison_coordinates"], 0.1)
        self.assertLessEqual(bound["coframe_perturbation_bound"], 0.1)
        self.assertGreater(bound["temporal_eigenvalue_lower_bound"], 0.3)

    def test_temporal_bound_holds_on_multiple_directions_at_its_ball_boundary(self):
        bound = model.temporal_ball_bound(self.constructed)
        radius = bound["radius_in_unscaled_comparison_coordinates"]
        for direction in (*np.eye(4), np.ones(4)/2):
            field = model.taylor_fields(self.constructed, radius*direction)
            self.assertGreaterEqual(np.linalg.eigvalsh(field["weights"][0])[0], bound["temporal_eigenvalue_lower_bound"])
            self.assertEqual(np.linalg.matrix_rank(field["coframe"]), 4)

    def test_cartan_auxiliary_equation_remains_solved_away_from_origin(self):
        for sample in self.report["independent_Taylor_field_checks"]["samples_off_shell_away_from_origin"]:
            self.assertLess(sample["Cartan_residual_norm"], 1e-11)

    def test_constraint_remainder_is_quadratic_not_claimed_identically_zero(self):
        samples = self.report["independent_Taylor_field_checks"]["samples_off_shell_away_from_origin"]
        for left, right in zip(samples, samples[1:]):
            self.assertGreater(left["constraint_norm"]/right["constraint_norm"], 3.9)
            self.assertLess(left["constraint_norm"]/right["constraint_norm"], 4.1)
        self.assertGreater(samples[-1]["constraint_norm"], 1e-6)

    def test_probe_equation_has_only_linear_remainder_not_an_evolved_solution(self):
        samples = self.report["independent_Taylor_field_checks"]["samples_off_shell_away_from_origin"]
        for left, right in zip(samples, samples[1:]):
            self.assertGreater(left["probe_residual_norm"]/right["probe_residual_norm"], 1.9)
            self.assertLess(left["probe_residual_norm"]/right["probe_residual_norm"], 2.1)
        self.assertGreater(samples[-1]["probe_residual_norm"], 0.01)

    def test_smooth_field_first_derivatives_match_the_saved_taylor_jets(self):
        step, u = 1e-5, np.eye(4)[1]
        plus, minus = model.taylor_fields(self.constructed, step*u), model.taylor_fields(self.constructed, -step*u)
        self.assertClose((plus["psi"]-minus["psi"])/(2*step), self.data["first"][1], atol=1e-9)
        self.assertClose((plus["multiplier"]-minus["multiplier"])/(2*step), self.second["multiplier_first"][1])

    def test_saved_arrays_are_the_actual_completed_jets(self):
        saved = json.loads((ROOT / "analysis/HC_Cartan_Compatible_Jets.json").read_text(encoding="utf-8"))
        arrays = saved["Taylor_data"]
        for name, actual in (("psi", self.data["psi"]), ("psi_first", self.data["first"]), ("psi_second", self.second["psi_second"])):
            self.assertClose(np.array(arrays[name+"_real"])+1j*np.array(arrays[name+"_imag"]), actual)
        self.assertClose(arrays["coframe_second"], self.second["coframe_second"])
        self.assertClose(arrays["multiplier_first"], self.second["multiplier_first"])

    def test_report_explicitly_preserves_native_evolution_and_scale_obligations(self):
        self.assertIn("not a Cauchy-surface or evolved solution", self.report["status"])
        self.assertTrue(self.report["compatible_second_jet_found"])
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["positive_temporal_ball"]["not_a_stability_or_full_constrained_hyperbolicity_theorem"])
        self.assertIn("actual local evolution", " ".join(self.report["remaining"]))


if __name__ == "__main__":
    unittest.main()
