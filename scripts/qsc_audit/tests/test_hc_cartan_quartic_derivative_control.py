"""Independent derivative, coefficient-majorant and saved-witness controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "quartic_derivative_control_test", ROOT / "analysis/HC_Cartan_Quartic_Derivative_Control.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class DerivativeAndMajorantTests(unittest.TestCase):
    def test_coordinate_derivative_on_mixed_polynomial(self):
        x = np.array([.2, -.3, .4, -.1])

        def function(y):
            return np.array([y[0]**4+y[1]*y[2]**2, y[0]*y[3]**3])

        expected = np.array([[4*x[0]**3, x[3]**3], [x[2]**2, 0],
                             [2*x[1]*x[2], 0], [0, 3*x[0]*x[3]**2]])
        np.testing.assert_allclose(model.coordinate_derivative(function, x, .01), expected, atol=2e-14)

    def test_extrapolation_removes_fifth_degree_derivative_stencil_error(self):
        x = np.array([.2, .1, -.3, .4])
        function = lambda y: np.array([sum(y**5)])
        coarse = model.coordinate_derivative(function, x, .125)
        fine = model.coordinate_derivative(function, x, .0625)
        np.testing.assert_allclose((16*fine-coarse)/15, (5*x**4)[:, None], atol=2e-15)
        self.assertGreater(np.linalg.norm(coarse-fine), 1e-4)

    def test_majorant_retains_ordered_tensor_multiplicities(self):
        value = model.polynomial_bound([(1, 1, 0, 0)], np.array([[3., 4.]]),
                                       model.common.RADIUS**2, model.common.RADIUS, order=2)
        self.assertAlmostEqual(value, 5*np.sqrt(2))

    def test_majorant_controls_random_polynomial_derivatives(self):
        rng = np.random.default_rng(241114)
        coefficients = rng.normal(size=(len(model.parent.P5), 3))
        radius = .7*model.common.RADIUS
        for order in (0, 1, 2):
            bound = model.polynomial_bound(model.parent.P5, coefficients, model.common.RADIUS, radius, order)
            for _ in range(6):
                y = rng.uniform(-.7, .7, size=4)
                derivatives = [model.common.derivative_weights(model.parent.P5, y, indices,
                    model.common.RADIUS) @ coefficients for indices in model.itertools.product(range(4), repeat=order)]
                self.assertLessEqual(np.linalg.norm(derivatives), bound*(1+1e-14))

    def test_invalid_bound_inputs_rejected(self):
        for radius in (-1., float("nan")):
            with self.assertRaises(ValueError):
                model.polynomial_bound([(1, 0, 0, 0)], np.ones((1, 2)), 1., radius)
        with self.assertRaises(ValueError):
            model.polynomial_bound([(1, 0, 0, 0)], np.ones((2, 2)), 1., 0.)


class QuarticDerivativeReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Quartic_Derivative_Control.json").read_text(encoding="utf-8"))
        cls.case = model.load_case()

    def test_fingerprints_and_unchanged_fit_contract(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertTrue(self.report["no_new_coefficients_fitted"])
        self.assertEqual(len(self.report["checks"]), 5)

    def test_first_prolongation_changes_from_cubic_to_quartic_radial_decay(self):
        for check in self.report["checks"]:
            for first, second in zip(check["samples"], check["samples"][1:]):
                self.assertAlmostEqual(first["first_norm"]/second["first_norm"], 16., delta=.1)
                self.assertAlmostEqual(first["before_first_norm"]/second["before_first_norm"], 8., delta=.1)
            for sample in check["samples"]:
                self.assertLess(sample["first_norm"], sample["before_first_norm"])
                self.assertLess(sample["jet_step_change"], 5e-9)

    def test_actual_coordinate_derivative_is_an_independent_control_not_exact_agreement(self):
        for check in self.report["checks"]:
            for sample in check["samples"]:
                self.assertLess(sample["coordinate_derivative_discrepancy"], 3e-7)
                self.assertLess(sample["coordinate_derivative_discrepancy"], .2*sample["first_norm"])
            self.assertLess(check["samples"][0]["coordinate_derivative_discrepancy"], 5e-8)

    def test_euler_degree_five_fits_better_than_degree_four(self):
        for check in self.report["checks"]:
            for sample in check["samples"][:2]:
                self.assertLess(sample["euler_fifth_remainder"], .02*sample["primary_norm"])
                self.assertLess(sample["euler_fifth_remainder"], sample["euler_fourth_after_remainder"])

    def test_saved_first_prolongation_reproduces_actual_fields(self):
        for check in self.report["checks"][:2]:
            x = model.common.RADIUS*np.asarray(check["direction"])
            fields, higher = model.fields_and_higher(self.case, x)
            actual = model.prolongation.first_prolongation(self.case[0], fields, higher)
            self.assertAlmostEqual(np.linalg.norm(actual), check["samples"][0]["first_norm"], delta=1e-10)

    def test_refreshed_field_balls_enclose_changed_polynomial_samples(self):
        radius = model.common.RADIUS
        balls, _ = model.refreshed_balls(self.case, radius)
        rng = np.random.default_rng(241115)
        for _ in range(5):
            direction = rng.normal(size=4)
            direction /= np.linalg.norm(direction)
            fields, _ = model.fields_and_higher(self.case, radius*direction)
            spatial = fields["psi_first"].copy()
            spatial[0] = 0
            for name, actual in (("e", fields["coframe"]), ("de", fields["coframe_first"]),
                                 ("psi", fields["psi"]), ("spatial_dp", spatial), ("lam", fields["multiplier"])):
                self.assertLessEqual(np.linalg.norm(actual-balls[name].center), balls[name].radius*(1+1e-10)+1e-14)

    def test_refreshed_chart_majorant_has_small_but_positive_domain(self):
        report = self.report["refreshed_normal_chart"]
        self.assertLess(report["radius"], model.common.RADIUS/10000)
        matrix, _ = model.uniform.coefficient_matrix(self.case[0], **model.refreshed_balls(self.case, report["radius"])[0])
        self.assertAlmostEqual(matrix.radius, report["matrix_change_majorant"], delta=1e-12)
        self.assertGreater(report["augmented_singular_lower_bound"], .05)
        self.assertLess(report["inverse_norm_upper_bound"], 20.)
        self.assertGreater(report["selection_trials"][0]["matrix_change_majorant"], report["center_augmented_minimum_singular"])
        for check in report["sample_checks_not_the_proof"]:
            self.assertLess(check["matrix_change"], report["matrix_change_majorant"])
            self.assertGreater(check["augmented_minimum_singular"], report["augmented_singular_lower_bound"])

    def test_scope_remains_explicit(self):
        self.assertTrue(self.report["not_regional_PDE_solution_or_all_order_convergence"])
        self.assertTrue(self.report["exact_parent_kernel_certificate_remains_authoritative"])
        self.assertTrue(self.report["refreshed_normal_chart"]["not_outward_rounded_or_interval_certified"])
        self.assertTrue(self.report["refreshed_normal_chart"]["not_uniform_exact_normal_rank_or_compatibility_propagation"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
