"""Shared polynomial jets, origin preservation and non-solution controls."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "common_polynomial_germ_test", ROOT / "analysis/HC_Cartan_Common_Polynomial_Germ.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class PolynomialJetTests(unittest.TestCase):
    def test_origin_derivatives_vanish_through_preserved_orders(self):
        for degree, powers, amplitude in ((4, model.E5, model.RADIUS**2),
                                          (4, model.E5, model.RADIUS),
                                          (3, model.L4, model.RADIUS)):
            for order in range(degree+1):
                for indices in itertools.combinations_with_replacement(range(4), order):
                    np.testing.assert_array_equal(model.derivative_weights(powers, np.zeros(4), indices, amplitude), 0)

    def test_independent_monomial_value_and_derivative_packing(self):
        coefficients = np.zeros(model.COUNT)
        ei = model.E5.index((5, 0, 0, 0))
        li = model.L4.index((0, 4, 0, 0))
        coefficients[16*ei] = 2
        coefficients[16*len(model.E5)+24*ei] = 3
        coefficients[40*len(model.E5)+16*li] = 4
        pi = model.E5.index((0, 5, 0, 0))
        coefficients[16*len(model.E5)+24*pi+14] = 1
        fields = model.unpack_fields(model.field_map(model.RADIUS*np.array([.25, .5, 0, 0])) @ coefficients)
        self.assertAlmostEqual(fields["coframe"][0, 0], 2*model.RADIUS**2*.25**5)
        self.assertAlmostEqual(fields["coframe_first"][0, 0, 0], 10*model.RADIUS*.25**4)
        self.assertAlmostEqual(fields["coframe_second"][0, 0, 0, 0], 40*.25**3)
        self.assertAlmostEqual(fields["psi"][0, 0].real, 3*model.RADIUS*.25**5)
        self.assertAlmostEqual(fields["psi_first"][0, 0, 0].real, 15*.25**4)
        self.assertAlmostEqual(fields["psi_first"][1, 0, 2].imag, 5*.5**4)
        self.assertAlmostEqual(fields["multiplier_first"][1, 0, 0], 16*.5**3)

    def test_all_seven_blocks_are_derivatives_of_the_same_polynomial(self):
        coefficients = np.random.default_rng(20261024).normal(size=model.COUNT)*1e-7
        x = model.RADIUS*np.array([.3, -.2, .4, .1])
        fields = model.unpack_fields(model.field_map(x) @ coefficients)
        higher = model.higher_correction(x, coefficients)
        derivatives = model.lower.prior.previous.field_derivatives(fields, higher)
        step = model.RADIUS*1e-4
        for r, direction in enumerate(np.eye(4)):
            plus = model.field_map(x+step*direction) @ coefficients
            minus = model.field_map(x-step*direction) @ coefficients
            np.testing.assert_allclose((plus-minus)/(2*step), model.pack_fields(derivatives[r]), atol=1e-8, rtol=1e-6)

    def test_field_round_trip_and_normal_coordinate_selector(self):
        prepared, point, jets, _, full, _ = model.general.domain.load_data()
        fields = model.general.domain.temporal.fields(prepared, point, jets, full, np.eye(4)[0]/16384)
        np.testing.assert_array_equal(model.pack_fields(model.unpack_fields(model.pack_fields(fields))), model.pack_fields(fields))
        rows = np.random.default_rng(20261025).normal(size=(16, 56))
        np.testing.assert_allclose(model.normal_coordinate_rows(rows) @ model.pack_fields(fields), rows @ model.general.normal_values(fields), atol=1e-12)


class CommonFieldReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Common_Polynomial_Germ.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_dimensions(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["coefficient_count"], 2800)
        self.assertEqual(len(self.report["coefficients"]), 2800)
        self.assertEqual(self.report["history"][0]["rank"], 270)

    def test_collocation_is_satisfied_but_not_promoted_to_a_regional_solution(self):
        for point in self.report["training"]:
            self.assertLess(point["corrected_lower_norm"], 1e-10)
            self.assertLess(point["normal_coordinate_drift"], 1e-12)
        self.assertTrue(self.report["first_prolongation_not_fitted"])
        self.assertTrue(self.report["no_regional_PDE_solution_or_uniform_error_bound"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_held_out_failures_and_first_derivatives_are_retained(self):
        for point in self.report["held_out"][:3]:
            self.assertGreater(point["corrected_lower_norm"], point["baseline_lower_norm"])
        for point in self.report["training"]:
            self.assertGreater(point["first_prolongation_norm"], .01)

    def test_saved_coefficients_reproduce_actual_lower_equations(self):
        prepared, point, jets, _, full, _ = model.general.domain.load_data()
        coefficients = np.asarray(self.report["coefficients"])
        for sample in self.report["training"]+self.report["held_out"]:
            x = np.asarray(sample["coordinate"])
            baseline = model.general.domain.temporal.fields(prepared, point, jets, full, x)
            fields = model.unpack_fields(model.pack_fields(baseline)+model.field_map(x) @ coefficients)
            norm = np.linalg.norm(model.lower.lower_residual(prepared, fields))
            self.assertAlmostEqual(norm, sample["corrected_lower_norm"], delta=1e-12)


if __name__ == "__main__":
    unittest.main()
