"""Full Taylor residual, physical derivative models and whole-cube controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("full_taylor_bound_test", ROOT / "analysis/HC_Cartan_Full_Taylor_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class TaylorJetTests(unittest.TestCase):
    def test_product_rule_preserves_nonconstant_models(self):
        indices = model.core.INDEX
        coefficients = np.zeros((70, 2, 2), complex)
        coefficients[0] = np.array([[1., .2j], [.3, 2.]])
        coefficients[indices[(1, 0, 0, 0)]] = np.eye(2)*.1
        value = model.T(coefficients)
        derivative = model.core.tensor(np.eye(2)*.1)
        zero = model.core.tensor(np.zeros((2, 2)))
        a = model.TaylorJet(value, [derivative, zero, zero, zero])
        result = model.jc("ij,jk->ik", a.conjugate(), a).real().transpose(1, 0)
        y = np.array([.3, .1, .2, -.1])
        actual = value.evaluate(y)
        expected = (.1*np.eye(2) @ actual+actual.conj() @ (.1*np.eye(2))).real.T
        np.testing.assert_allclose(result.derivatives[0].evaluate(y), expected, atol=1e-15)
        np.testing.assert_allclose(result.value.evaluate(y), (actual.conj() @ actual).real.T, atol=1e-15)

    def test_bad_derivative_shapes_rejected(self):
        with self.assertRaises(ValueError):
            model.TaylorJet(np.ones(2), [model.core.tensor(np.zeros(3)) for _ in range(4)])

    def test_reshape_and_vectorization_preserve_joint_norms(self):
        a = model.T(model.core.tensor(np.eye(2)).coefficients, 3.)
        b = model.T(model.core.tensor(np.ones(2)).coefficients, 4.)
        full = model.vectorize([a, b])
        self.assertEqual(full.coefficients.shape, (70, 6))
        self.assertEqual(full.tail, 5.)
        self.assertEqual(model.reshape(a, (4,)).tail, 3.)

    def test_second_derivative_base_field_has_both_derivative_axes(self):
        fourth = np.ones((4, 4, 4, 4, 4, 4))
        derivatives = {2: np.zeros((4, 4, 4, 4)), 3: np.zeros((4, 4, 4, 4, 4)), 4: fourth}
        value = model.base_derivative(derivatives, 2., 2)
        self.assertEqual(value.center.shape, (4, 4, 4, 4))
        np.testing.assert_allclose(value.evaluate([.2, 0, 0, 0]), .08)


class FullTaylorReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.control.load_case()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Full_Taylor_Bound.json").read_text(encoding="utf-8"))

    def test_fingerprints_packing_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["row_count"], 80)
        for report in self.report["reports"]:
            self.assertEqual(np.asarray(report["coefficients"]).shape, (70, 80))
        for flag in ("physical_derivative_models_built_from_original_polynomial", "no_coefficients_fitted_or_zeroed",
                     "not_outward_rounded_or_interval_certified", "not_exact_low_order_vanishing_or_regional_solution",
                     "not_distance_to_solution_or_PDE_convergence"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_all_input_models_match_original_field_on_cube_including_corners(self):
        fields = model.field_models(self.case, model.common.RADIUS)
        mapping = {"e": "coframe", "de": "coframe_first", "dde": "coframe_second", "psi": "psi",
                   "dp": "psi_first", "lam": "multiplier", "dl": "multiplier_first"}
        for y in (np.ones(4), np.array([-1., 1., -1., 1.]), np.array([.2, -.3, .1, .4])):
            actual, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*y)
            for key, name in mapping.items():
                error = np.linalg.norm(actual[name]-fields[key].evaluate(y))
                self.assertLessEqual(error, fields[key].tail+2e-13)

    def test_saved_zero_tail_points_match_independent_80_equations(self):
        for point in self.report["point_controls"]:
            self.assertEqual(point["tail"], 0.)
            self.assertLess(point["match_error"], 2e-12)

    def test_off_shell_all_blocks_match_parent_evaluator(self):
        fields, _ = model.control.fields_and_higher(self.case, np.zeros(4))
        rng = np.random.default_rng(801116)
        for key, value in fields.items():
            delta = rng.normal(size=value.shape)*1e-4
            if np.iscomplexobj(value):
                delta = delta+1j*rng.normal(size=value.shape)*1e-4
            if key == "coframe_second":
                delta = (delta+delta.swapaxes(0, 1))/2
            fields[key] = value+delta
        actual = model.common.lower.lower_residual(self.case[0], fields)
        full, blocks, _ = model.residual_models(self.case[0], model.point_models(fields))
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        self.assertEqual([value.center.size for value in blocks.values()], [16, 24, 16, 24])
        self.assertEqual(full.tail, 0.)
        np.testing.assert_allclose(full.center, actual, atol=3e-12, rtol=0)

    def test_constitutive_coefficients_and_tail_preserve_predecessor(self):
        prior = json.loads((ROOT / "analysis/HC_Cartan_Constitutive_Taylor_Bound.json").read_text(encoding="utf-8"))
        self.assertEqual(prior["input_sha256"], model.core.input_fingerprints())
        for report, original in zip(self.report["reports"], prior["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, :16], np.asarray(original["coefficients"]).reshape(70, 16))
            self.assertEqual(report["blocks"]["constraint"]["tail_bound"], original["tail_bound"])

    def test_rescaling_preserves_all_coefficients_and_physical_orders(self):
        a, b = self.report["reports"]
        expected = np.asarray(a["coefficients"])*2.**(-model.core.DEGREES[:, None])
        np.testing.assert_allclose(np.asarray(b["coefficients"]), expected, atol=2e-18, rtol=1e-12)

    def test_tail_improvement_curl_dominance_and_fifth_order_behavior(self):
        a, b = self.report["reports"]
        self.assertGreater(2495517./a["whole_cube_upper_estimate"], 200000.)
        self.assertLess(a["whole_cube_upper_estimate"], 11.)
        self.assertGreater(a["whole_cube_upper_estimate"], 10.)
        self.assertLess(b["whole_cube_upper_estimate"], .4)
        for key in a["blocks"]:
            ratio = a["blocks"][key]["tail_bound"]/b["blocks"][key]["tail_bound"]
            self.assertGreater(ratio, 31.)
            self.assertLess(ratio, 34.)
        self.assertGreater(a["blocks"]["curls"]["tail_bound"], 4*a["blocks"]["coframe"]["tail_bound"])
        self.assertAlmostEqual(a["tail_bound"], np.linalg.norm([r["tail_bound"] for r in a["blocks"].values()]))

    def test_actual_points_and_cube_corners_remain_within_conservative_tail(self):
        for report in self.report["reports"]:
            polynomial = model.T(np.asarray(report["coefficients"]), report["tail_bound"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["tail_discrepancy"], report["tail_bound"])
                self.assertGreater(report["tail_bound"], 1e5*check["actual_norm"])
                self.assertAlmostEqual(np.linalg.norm(polynomial.evaluate(check["direction"])), check["polynomial_norm"], delta=1e-20)

    def test_low_order_defects_are_retained_not_assumed_exactly_zero(self):
        for report in self.report["reports"]:
            self.assertGreater(report["coefficient_level_bounds"][0], 0.)
            self.assertGreater(report["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["coefficient_level_bounds"][4], 1e-12)
            self.assertAlmostEqual(sum(report["coefficient_level_bounds"])+report["tail_bound"], report["whole_cube_upper_estimate"])


if __name__ == "__main__":
    unittest.main()
