"""Selective flat-vacuum compensation and boundaries of a native identification."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "vacuum_heat_kernel", ROOT / "analysis/HC_Induced_Gravity_Heat_Kernel.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCVacuumBalanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = model.background.triadic_mass()
        cls.partners = np.repeat(model.mass_spectrum(cls.matrix)**2, 4)
        cls.fermion = model.coefficients(cls.matrix, 20, 2)
        cls.paired = model.mixed_coefficients(cls.matrix, cls.partners)
        cls.examples = model.vacuum_balance_examples(cls.matrix)

    def assertClose(self, actual, expected, rtol=2e-9, atol=1e-11):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_fermion_only_extension_matches_previous_coefficients(self):
        mixed = model.mixed_coefficients(self.matrix)
        self.assertClose(mixed["A"], self.fermion["A"])
        self.assertClose(mixed["rho_vac"], self.fermion["rho_vac"])

    def test_one_dirac_requires_four_real_scalar_modes_in_flat_kernel(self):
        for count in range(6):
            w = model.graded_heat_coefficients(0.03, [[2]], [4]*count)["W0"]
            self.assertClose(w, (4-count)*np.exp(-0.12))

    def test_equal_counts_alone_do_not_match_a_mass_spectrum(self):
        value = model.graded_heat_coefficients(0.2, [[2]], [1]*4)
        self.assertGreater(abs(value["W0"]), 0.5)

    def test_paired_flat_kernel_vanishes_for_all_sampled_proper_times(self):
        for s in (0, 1e-5, 0.003, 0.03, 0.3, 3, 30):
            self.assertClose(model.graded_heat_coefficients(s, self.matrix, self.partners)["W0"], 0)

    def test_paired_vacuum_cancels_for_different_windows(self):
        for uv, ir in ((2, 0), (20, 2), (80, 4), (20, 19)):
            c = model.mixed_coefficients(self.matrix, self.partners, uv=uv, ir=ir)
            self.assertClose(c["rho_vac"], 0)

    def test_paired_minimal_scalars_keep_a_positive_einstein_term(self):
        self.assertClose(self.paired["A"], 3*self.fermion["A"])
        self.assertTrue(self.paired["positive_Einstein_coefficient"])
        self.assertEqual(self.paired["Lambda_cos_truncated"], 0)

    def test_conformal_scalar_coupling_keeps_the_dirac_einstein_coefficient(self):
        c = model.mixed_coefficients(self.matrix, self.partners, xi=1/6)
        self.assertClose(c["A"], self.fermion["A"])
        self.assertEqual(c["rho_vac"], 0)

    def test_quarter_coupling_cancels_the_einstein_term_as_well(self):
        c = model.mixed_coefficients(self.matrix, self.partners, xi=1/4)
        self.assertClose(c["A"], 0)
        self.assertFalse(c["Einstein_coefficient_numerically_resolved"])
        self.assertIsNone(c["Lambda_cos_truncated"])

    def test_larger_scalar_curvature_coupling_has_wrong_einstein_sign(self):
        c = model.mixed_coefficients(self.matrix, self.partners, xi=0.3)
        self.assertLess(c["A"], 0)
        self.assertFalse(c["positive_Einstein_coefficient"])
        self.assertEqual(c["rho_vac"], 0)

    def test_common_xi_formula_for_the_complete_prepared_spectrum(self):
        for xi in (-0.2, 0, 0.1, 1/6, 0.25, 0.3):
            c = model.mixed_coefficients(self.matrix, self.partners, xi=xi)
            self.assertClose(c["A"], 3*(1-4*xi)*self.fermion["A"])

    def test_curvature_kernel_does_not_follow_from_flat_kernel_cancellation(self):
        minimal = model.graded_heat_coefficients(0.03, self.matrix, self.partners)
        quarter = model.graded_heat_coefficients(0.03, self.matrix, self.partners, 0.25)
        self.assertClose(minimal["W0"], quarter["W0"])
        self.assertGreater(minimal["B2"], 1)
        self.assertClose(quarter["B2"], 0)

    def test_nonuniform_curvature_couplings_match_independent_quadrature(self):
        xi = np.linspace(-0.1, 0.2, 12)
        c = model.mixed_coefficients(self.matrix, self.partners, xi)
        self.assertClose(model.mixed_action_density(0.01, self.matrix, self.partners, xi),
                         c["rho_vac"]-0.01*c["A"])

    def test_unpaired_action_matches_independent_quadrature(self):
        q = self.partners+0.13
        c = model.mixed_coefficients(self.matrix, q, 0.07)
        self.assertClose(model.mixed_action_density(-0.02, self.matrix, q, 0.07),
                         c["rho_vac"]+0.02*c["A"])

    def test_paired_truncated_action_matches_independent_quadrature(self):
        self.assertClose(model.mixed_action_density(0.01, self.matrix, self.partners),
                         -0.01*self.paired["A"])

    def test_one_missing_partner_leaves_a_positive_vacuum_density(self):
        c = model.mixed_coefficients(self.matrix, self.partners[:-1])
        expected = model.proper_time_integral(np.sqrt(self.partners[-1]), 20, 2, 3)/(32*np.pi**2)
        self.assertClose(c["rho_vac"], expected)
        self.assertGreater(c["Lambda_cos_truncated"], 0)

    def test_small_mass_splitting_restores_vacuum_density_at_first_order(self):
        delta = 1e-4
        plus = model.mixed_coefficients(self.matrix, self.partners+delta)
        minus = model.mixed_coefficients(self.matrix, self.partners-delta)
        derivative = (plus["rho_vac"]-minus["rho_vac"])/(2*delta)
        self.assertClose(derivative, 12*self.fermion["A"], rtol=1e-7)

    def test_cosmological_splitting_sensitivity_depends_on_curvature_coupling(self):
        delta = 1e-4
        for xi in (0, 0.1, 1/6):
            plus = model.mixed_coefficients(self.matrix, self.partners+delta, xi)
            minus = model.mixed_coefficients(self.matrix, self.partners-delta, xi)
            derivative = (plus["Lambda_cos_truncated"]-minus["Lambda_cos_truncated"])/(2*delta)
            self.assertClose(derivative, 2/(1-4*xi), rtol=2e-7)

    def test_three_divergence_moments_do_not_imply_zero_finite_density(self):
        c = self.examples["first_three_mass_moments_cancel_but_vacuum_does_not"]
        self.assertClose(c["signed_mass_moments_0_1_2"], [0, 0, 0])
        self.assertGreater(c["rho_vac"], 0.002)

    def test_moment_counterexample_has_an_exact_nonzero_heat_weight(self):
        matrix = np.diag([0, np.sqrt(2), np.sqrt(2), np.sqrt(2)])
        bosons = np.repeat([1, 3], [12, 4])
        for s in (0.03, 0.3, 1, 3):
            self.assertClose(model.graded_heat_coefficients(s, matrix, bosons)["W0"],
                             4*(1-np.exp(-s))**3)

    def test_constant_internal_unitaries_cannot_supply_the_missing_partners(self):
        u = np.diag(np.exp(1j*np.array([0.2, -0.7, 0.9])))
        c = model.mixed_coefficients(u @ self.matrix @ u.conj().T, self.partners)
        self.assertClose(c["A"], self.paired["A"])
        self.assertClose(c["rho_vac"], 0)
        unpaired = model.mixed_coefficients(u @ self.matrix @ u.conj().T)
        self.assertGreater(unpaired["rho_vac"], 2000)

    def test_negative_dirac_mass_does_not_create_a_negative_determinant_weight(self):
        a = model.graded_heat_coefficients(0.03, self.matrix)
        b = model.graded_heat_coefficients(0.03, -self.matrix)
        self.assertClose(a["W0"], b["W0"])
        self.assertGreater(a["W0"], 0)

    def test_scalar_negative_squared_mass_is_not_silently_euclideanized(self):
        for q in ([-1], [np.nan], [np.inf], [1j], [[1]], 1):
            with self.subTest(q=q), self.assertRaises(ValueError):
                model.mixed_coefficients(self.matrix, q)

    def test_invalid_scalar_curvature_couplings(self):
        for xi in (np.nan, np.inf, 1j, [0, 0]):
            with self.subTest(xi=xi), self.assertRaises(ValueError):
                model.mixed_coefficients(self.matrix, [1, 2, 3], xi)

    def test_invalid_heat_proper_time(self):
        for s in (-1, np.nan, np.inf):
            with self.subTest(s=s), self.assertRaises(ValueError):
                model.graded_heat_coefficients(s, self.matrix)

    def test_ordinary_common_rescaling_preserves_dimensionless_hierarchy(self):
        c = model.mixed_coefficients(self.matrix, self.partners+0.1)
        f = 3.0
        d = model.mixed_coefficients(f*self.matrix, f*f*(self.partners+0.1), uv=60, ir=6)
        self.assertClose(d["A"], f*f*c["A"])
        self.assertClose(d["rho_vac"], f**4*c["rho_vac"])
        self.assertClose(d["Lambda_cos_truncated"]/d["inverse_G"],
                         c["Lambda_cos_truncated"]/c["inverse_G"])

    def test_source_values_do_not_turn_beta_squared_into_observed_planck_units(self):
        d = self.examples["source_value_unit_check"]
        self.assertClose(d["observed_dimensionless_Lambda_ellP_squared"],
                         2.8726016e-122, atol=0)
        self.assertGreater(d["ratio_between_written_and_observed_dimensionless_values"], 1e121)

    def test_fixed_reference_subtraction_does_not_change_volume_variation(self):
        rho, t, dt = 2.3, 0.07, 1e-5
        fixed_reference_value = 10.0
        reference_subtracted = lambda x: rho*np.exp(4*x)-fixed_reference_value
        derivative = (reference_subtracted(t+dt)-reference_subtracted(t-dt))/(2*dt)
        self.assertClose(derivative, 4*rho*np.exp(4*t), rtol=1e-8)

    def test_volume_counterterm_cancels_vacuum_variation_but_is_extra_input(self):
        rho, t, dt = 2.3, 0.07, 1e-5
        counterterm_subtracted = lambda x: rho*np.exp(4*x)-rho*np.exp(4*x)
        self.assertEqual((counterterm_subtracted(t+dt)-counterterm_subtracted(t-dt))/(2*dt), 0)
        self.assertTrue(self.examples["not_a_native_spectrum_or_a_higher_loop_protection_mechanism"])

    def test_native_vacuum_anchors_exist_without_being_identified_as_scalar_partners(self):
        for item in self.examples["native_anchors"]:
            text = (ROOT / item["path"]).read_text(encoding="utf-8")
            self.assertIn("\\label{"+item["label"]+"}", text)
        self.assertIn("NOT native HC fields", self.examples["status"])
        self.assertEqual(len(self.paired["scalar_squared_masses"]), 12)

    def test_report_records_full_mirror_and_native_scope_boundaries(self):
        self.assertIn("both the vacuum and the Einstein term", self.examples["full_operator_mirror_warning"])
        note = (ROOT / "analysis/HC_Induced_Gravity_Heat_Kernel.md").read_text(encoding="utf-8")
        for text in ("rank-one principal tensor", "No twelve-scalar extension", "unit-system artifact"):
            self.assertIn(text, note)


if __name__ == "__main__":
    unittest.main()
