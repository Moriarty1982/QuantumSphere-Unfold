"""Independent matrix-series arithmetic and fresh nonlinear C3 controls."""
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import unittest

import mpmath
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("high_precision_c3_test", ROOT / "analysis/HC_Cartan_High_Precision_C3_Source.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class MatrixSeriesTests(unittest.TestCase):
    def setUp(self):
        self.ctx = mpmath.mp.clone()
        self.ctx.dps = 60

    def test_exact_input_conversion_before_arithmetic(self):
        value = model.number(self.ctx, (Fraction(1, 3), Fraction(1, 7)))
        self.assertLess(abs(value.real-self.ctx.mpf(1)/3), self.ctx.mpf("1e-58"))
        self.assertLess(abs(value.imag-self.ctx.mpf(1)/7), self.ctx.mpf("1e-58"))
        self.assertEqual(model.number(self.ctx, value), value)
        with self.assertRaises(ValueError):
            model.matrix(self.ctx, np.zeros(4))

    def test_matrix_reshape_keeps_all_entries_and_roundtrips(self):
        value = model.matrix(self.ctx, np.arange(1, 7).reshape(2, 3))
        series = model.Series.constant(self.ctx, value)
        reshaped = series.reshape(6, 1)
        self.assertEqual(list(reshaped.coefficients[0]), list(value))
        self.assertEqual(reshaped.reshape(2, 3).coefficients[0], value)
        with self.assertRaises(ValueError):
            series.reshape(3, 3)

    def test_matrix_inverse_and_product_coefficient_recurrence(self):
        coefficients = [self.ctx.eye(2), self.ctx.matrix([[1, 2], [-1, 3]]),
            self.ctx.matrix([[2, 0], [0, -1]]), self.ctx.matrix([[0, 1], [2, 0]])]
        series = model.Series(self.ctx, coefficients)
        for product in (series @ series.inverse(), series.inverse() @ series):
            self.assertEqual(product.coefficients[0], self.ctx.eye(2))
            for a in product.coefficients[1:]:
                self.assertLess(self.ctx.norm(a), self.ctx.mpf("1e-55"))

    def test_determinant_and_scalar_reciprocal_are_formal_series(self):
        series = model.Series(self.ctx, [self.ctx.matrix([[1, 0], [0, 2]]),
            self.ctx.matrix([[1, 0], [0, 0]]), self.ctx.matrix([[0, 0], [0, 3]]), self.ctx.zeros(2)])
        determinant = series.determinant()
        self.assertEqual([v[0, 0] for v in determinant.coefficients], [2, 2, 3, 3])
        identity = determinant @ determinant.inverse()
        self.assertEqual([v[0, 0] for v in identity.coefficients], [1, 0, 0, 0])
        with self.assertRaises(ValueError):
            series.times_scalar(series)

    def test_directional_derivatives_and_exact_reconstruction(self):
        y = [self.ctx.mpf(v) for v in (1, -1, 2, 1)]
        arrays = [np.ones((*(4,)*n, 2, 2)) for n in range(4)]
        values = model.directional(self.ctx, arrays, y)
        for n, value in enumerate(values.coefficients):
            self.assertEqual(value[0, 0], sum(y)**n/math.factorial(n))
        inverse = model.reconstruction()
        v = [[math.prod(y[i]**p[i] for i in range(4)) for p in model.POWERS] for y in model.POWERS]
        for i in range(20):
            for j in range(20):
                self.assertEqual(sum(inverse[i][k]*v[k][j] for k in range(20)), int(i == j))

    def test_spinor_image_projection_preserves_nonimage_controls(self):
        groups = model.common.lower.prior.previous.first.prior.joint.third.diagnostic.groups()
        vector = [self.ctx.mpf(i % 7) for i in range(320)]
        image, remainder = model.spinor_image_split(self.ctx, vector, groups)
        twice, zero = model.spinor_image_split(self.ctx, image, groups)
        self.assertLess(self.ctx.norm(self.ctx.matrix(twice)-self.ctx.matrix(image)), self.ctx.mpf("1e-55"))
        self.assertLess(self.ctx.norm(self.ctx.matrix(zero)), self.ctx.mpf("1e-55"))
        self.assertGreater(self.ctx.norm(self.ctx.matrix(remainder)), 0.)
        self.assertLess(abs(self.ctx.fsum(a*b for a, b in zip(image, remainder))), self.ctx.mpf("1e-55"))
        with self.assertRaises(ValueError):
            model.spinor_image_split(self.ctx, vector, groups[:1])


class HighPrecisionSourceReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_High_Precision_C3_Source.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_fresh_source_proof_boundary(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("nonlinear_sources_recomputed_before_rounding_not_promoted_from_saved_values",
                "independent_matrix_series_not_parent_third_derivative_formula", "exact_directional_reconstruction_checked",
                "formal_series_not_finite_difference_steps", "fitted_input_coordinates_still_interpreted_as_stored_binary64",
                "exact_kernel_coordinates_used_before_high_precision_arithmetic", "other_794_origin_equations_not_recomputed_at_high_precision",
                "spinor_image_split_is_diagnostic_not_a_release_of_kernel_constraints",
                "no_new_fit_interval_certificate_regional_solution_or_native_identification", "parent_polynomials_reports_and_main_TeX_PDF_unchanged"):
            self.assertTrue(self.report[flag])

    def test_two_precisions_full_series_and_rounded_negative_control(self):
        low, high = self.report["reports"]
        self.assertEqual((low["digits"], high["digits"]), (40, 80))
        for report in (low, high):
            for key in ("source0_vector", "source1_vector", "C3_vector"):
                self.assertEqual(len(report[key]), 320)
            self.assertGreater(float(report["fresh_C3_norm"]), 0.)
            self.assertGreater(float(report["fixed_other_data_compatibility_norm"]), 1e-12)
            self.assertLess(float(report["orthogonal_image_split_squared_norm_discrepancy"]), 1e-45)
            self.assertGreater(float(report["fresh_sources_with_rounded_inputs_C3_norm"]), 1e-8)
            self.assertLess(float(report["held_out_full_series_split_discrepancy"]), 1e-25)
            self.assertLess(float(report["parametric_minus_baseline_C3_norm"]), 1e-25)
            self.assertLess(float(report["fresh_minus_frozen_source_norm"]), 1e-8)
        for value in self.report["cross_precision_vector_discrepancies"].values():
            self.assertLess(float(value), 1e-25)

    def test_fresh_series_origin_value_matches_independent_equations(self):
        ctx = mpmath.mp.clone()
        ctx.dps = 40
        bundle = model.load_bundle()
        evaluator = model.Evaluator(ctx, bundle)
        values = evaluator.constraint((1, 0, 0, 0), "lower")
        case = model.cubic.control.load_case()
        fields, _ = model.cubic.control.fields_and_higher(case, np.zeros(4))
        original = model.common.lower.lower_residual(case[0], fields)[:16].reshape(4, 4)
        self.assertLess(np.linalg.norm(np.asarray(values[0].tolist(), complex)-original), 2e-13)
        cauchy = model.common.lower.prior.previous.first.prior
        prepared, point, _, _, _, lift = model.GENERAL.domain.load_data()
        jets = cauchy.joint.regular.unpack(np.asarray(lift["fitted_coordinates"]))
        lc = cauchy.joint.third.lc_cubic(prepared, point)
        source = cauchy.joint.third.constraint_third(prepared, point, jets, lc)
        self.assertLess(np.linalg.norm(np.asarray(values[3].tolist(), complex)*6-source[0]), 1e-8)
        precise = self.report["reports"][1]
        self.assertLess(np.linalg.norm(np.asarray([float(x) for x in precise["source0_vector"]])-source.ravel()), 1e-8)
        highest = np.asarray(lift["fitted_highest"])
        highest_source = cauchy.joint.third.diagnostic.connection_image(prepared,
            highest[:560].reshape(35, 4, 4), highest[560:880].reshape(20, 4, 4))
        self.assertLess(np.linalg.norm(np.asarray([float(x) for x in precise["source1_vector"]])-highest_source.ravel()), 1e-8)


if __name__ == "__main__":
    unittest.main()
