"""Focused stencil, extrapolation and frozen-report reproducibility checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "second_probe_diagnostic", ROOT / "analysis/HC_Cartan_Second_Probe_Diagnostic.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def decode(value):
    return np.asarray(value["real"])+1j*np.asarray(value["imag"])


class SecondDifferenceTests(unittest.TestCase):
    def test_polynomial_diagonal_mixed_and_complex_channels(self):
        hessian = np.array([[2., -3., 4., 0.], [-3., 6., 2., 1.],
                            [4., 2., -4., 5.], [0., 1., 5., 8.]])

        def polynomial(x):
            value = 7+np.sum(x)+x @ hessian @ x/2
            return np.array([value, (2-3j)*value])

        actual = model.second_difference(polynomial, .025)
        np.testing.assert_allclose(actual, hessian[:, :, None]*np.array([1, 2-3j]), atol=3e-11)

    def test_richardson_cancels_quartic_error_in_all_pairs(self):
        def polynomial(x):
            a, b = x
            return np.array([a*a+3*a*b+2*b*b+5*a**4+7*a**3*b+11*a*b**3+13*b**4])

        expected = np.array([[2., 3.], [3., 4.]])[:, :, None]
        coarse = model.second_difference(polynomial, .1, dimension=2)
        fine = model.second_difference(polynomial, .05, dimension=2)
        np.testing.assert_allclose(coarse-expected, 4*(fine-expected), atol=1e-13)
        np.testing.assert_allclose(model.richardson(coarse, fine), expected, atol=1e-13)

    def test_invalid_steps(self):
        for step in (0., -1., np.inf, np.nan):
            with self.assertRaises(ValueError):
                model.second_difference(lambda x: x, step)


class SavedDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((ROOT / "analysis/HC_Cartan_Second_Probe_Diagnostic.json").read_text(encoding="utf-8"))
        cls.actual = model.evaluate()

    def test_source_hashes_and_frozen_inputs(self):
        self.assertEqual(self.actual["input_sha256"], self.saved["input_sha256"])
        self.assertEqual(self.actual["jet_source"], self.saved["jet_source"])
        self.assertEqual(self.actual["fixed_lower_point_and_couplings"], self.saved["fixed_lower_point_and_couplings"])
        self.assertEqual(self.actual["truncation"], self.saved["truncation"])
        self.assertEqual(self.actual["interpretation"], self.saved["interpretation"])

    def test_all_saved_tensor_levels_reproduce(self):
        self.assertEqual(len(self.actual["history"]), len(self.saved["history"]))
        for actual, saved in zip(self.actual["history"], self.saved["history"]):
            self.assertEqual(actual["step"], saved["step"])
            for key in ("R2", "Richardson_R2"):
                if key in saved:
                    # Absolute slack covers small components after h^-2 cancellation.
                    np.testing.assert_allclose(decode(actual[key]), decode(saved[key]), rtol=2e-7, atol=2e-4)
        np.testing.assert_allclose(decode(self.actual["result"]["R2"]),
                                   decode(self.saved["result"]["R2"]), rtol=2e-7, atol=2e-4)

    def test_initial_steps_refinement_and_symmetric_layout(self):
        history = self.actual["history"]
        self.assertEqual([entry["step"] for entry in history[:3]], list(model.INITIAL_STEPS))
        self.assertLessEqual(len(history), model.MAX_LEVELS)
        result = decode(self.actual["result"]["R2"])
        self.assertEqual(result.shape, (4, 4, 12))
        np.testing.assert_array_equal(result, result.swapaxes(0, 1))
        for index in range(1, len(history)):
            np.testing.assert_allclose(decode(history[index]["Richardson_R2"]),
                                       model.richardson(decode(history[index-1]["R2"]),
                                                        decode(history[index]["R2"])))

    def test_scalar_gate_and_frozen_probe_are_distinct(self):
        self.assertLess(self.actual["origin"]["scalar_hessian_norm"], 1e-6)
        self.assertLess(self.actual["origin"]["probe_norm"], 1e-8)
        self.assertGreater(self.actual["result"]["full_symmetric_norm"], 1.)
        self.assertTrue(self.actual["result"]["converged_by_change_criterion"])


if __name__ == "__main__":
    unittest.main()
