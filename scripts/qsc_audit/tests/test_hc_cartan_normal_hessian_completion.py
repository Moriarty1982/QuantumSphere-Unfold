"""Normal Hessian gate: analytic helper and independently replayed residuals."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "normal_hessian_test", ROOT / "analysis/HC_Cartan_Normal_Hessian_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CentralJacobianTests(unittest.TestCase):
    def test_quadratic_derivative_at_nonzero_point(self):
        def function(p):
            x, y = p
            return np.array([x*x+3*x*y, y*y-2*x, 7.])
        actual = model.central_jacobian(function, np.array([2., -3.]))
        np.testing.assert_allclose(actual, [[-5., 6.], [-2., -6.], [0., 0.]], atol=1e-12)


class NormalHessianCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Normal_Hessian_Completion.json").read_text(encoding="utf-8"))
        cls.before = json.loads((ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_normal_mask_and_gate_dimensions(self):
        self.assertEqual(self.report["normal_psi2_count"], 96)
        self.assertEqual(self.report["affine_response_shape"], [1114, 1168])
        self.assertEqual(self.report["affine_response_rank"], 568)
        self.assertEqual(self.report["left_gate_dimension"], 546)

    def test_response_and_degree_controls(self):
        self.assertLess(self.report["mixed_response_error"], 1e-7)
        self.assertLess(self.report["third_difference_norm"], 1e-7)
        self.assertLess(self.report["elimination_error"], 1e-7)
        for control in self.report["quadratic_controls"]:
            self.assertLess(control["old_and_euler_quadratic_norm"], 1e-7)
            self.assertLess(control["projected_quadratic_norm"], 1e-7)

    def test_failed_fit_is_not_reported_as_solution(self):
        self.assertGreater(self.report["final"]["all_1114_norm"], 30.)
        self.assertGreater(self.report["final"]["old_394_norm"], .1)
        self.assertLess(self.report["final_gate_norm"], self.report["initial_gate_norm"])
        self.assertEqual(self.report["history"][0]["rank"], 96)

    def test_tangential_coordinates_unchanged(self):
        c = np.array(self.report["fitted_coordinates"])
        h = np.array(self.report["fitted_highest"])
        allowed = sum(model.prior.source.allowed_cauchy_coordinates().values(), [])
        mask = sum(model.prior.highest_mask().values(), [])
        fixed_c = np.setdiff1d(np.arange(1200), allowed)
        fixed_h = np.setdiff1d(np.arange(1720), mask)
        np.testing.assert_array_equal(c[fixed_c], np.array(self.before["starting_coordinates"])[fixed_c])
        np.testing.assert_array_equal(h[fixed_h], np.array(self.before["starting_highest"])[fixed_h])

    def test_replay_all_1114_actual_equations(self):
        prepared, point, _, _, _ = model.prior.source.neighborhood.load_data()
        reduction = model.prior.source.normal.build_reduction(prepared, point)
        changed = model.prior.source.normal.remaining.normal_point(
            point, reduction["sources"] @ np.array(self.before["source_values"]))
        lc = model.prior.joint.third.lc_cubic(prepared, changed)
        actual = model.prior.evaluate_fields(prepared, changed,
            np.array(self.report["fitted_coordinates"]), np.array(self.report["fitted_highest"]), lc)
        for key, value in model.prior.norm_report(actual).items():
            self.assertAlmostEqual(value, self.report["final"][key], places=8)
        self.assertTrue(self.report["not_general_nonexistence_or_regional_evolution"])


if __name__ == "__main__":
    unittest.main()
