"""Cubic coefficient extraction and frozen-fourth-spinor controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cubic_residual_gate_test", ROOT / "analysis/HC_Cartan_Cubic_Residual_Gate.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CubicExtractionTests(unittest.TestCase):
    def test_stencil_cancels_lower_orders_and_extrapolation_cancels_fifth(self):
        def polynomial(t):
            return np.array([3+2*t+4*t*t+7*t**3+11*t**5, -2+t-3*t**3+2*t**5])
        coarse, fine = model.cubic_estimates(polynomial)
        np.testing.assert_allclose(coarse, [7, -3], atol=1e-12)
        np.testing.assert_allclose(fine, [7, -3], atol=1e-11)

    def test_cubic_map_is_homogeneous_and_has_no_spinor_first_change(self):
        y = np.array([.3, .2, -.1, .4])
        matrix = model.cubic_field_map(y)
        self.assertEqual(matrix.shape, (440, 1456))
        np.testing.assert_allclose(model.cubic_field_map(y/2), matrix/8, atol=1e-14)
        np.testing.assert_array_equal(matrix[240:360], 0)

    def test_full_cubic_sampling_is_unisolvent(self):
        vandermonde = np.array([[np.prod(y**np.asarray(p)) for p in model.CUBICS] for y in model.DIRECTIONS])
        self.assertEqual(np.linalg.matrix_rank(vandermonde), 20)
        self.assertLess(np.linalg.cond(vandermonde), 40)


class FrozenSpinorGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Cubic_Residual_Gate.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_free_coordinate_control_does_not_remove_cubic_obstruction(self):
        fixed, free = self.report["cases"]
        self.assertAlmostEqual(fixed["predicted_cubic_norm"], free["predicted_cubic_norm"], delta=1e-14)
        self.assertGreater(fixed["predicted_cubic_norm"], 1000*self.report["baseline_estimate_step_change"])
        self.assertLess(fixed["coordinate_cubic_drift"], 1e-12)
        self.assertGreater(free["coordinate_cubic_drift"], 1e-9)

    def test_prediction_is_checked_on_actual_equations(self):
        for case in self.report["cases"]:
            for check in case["checks"]:
                self.assertLess(check["response_prediction_error"], 1e-10)
                self.assertLess(check["estimate_step_change"], 1e-9)

    def test_resolved_rank_gaps_and_scope(self):
        for case in self.report["cases"]:
            self.assertGreater(case["retained_minimum_singular"], .01)
            self.assertLess(case["first_omitted_singular"], 1e-9)
        self.assertTrue(self.report["no_exact_or_regional_nonexistence_claim"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
