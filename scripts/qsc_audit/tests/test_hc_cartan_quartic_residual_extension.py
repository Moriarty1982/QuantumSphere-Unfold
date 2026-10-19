"""Quartic coefficients, shared polynomial derivatives and next-order controls."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("quartic_extension_test", ROOT / "analysis/HC_Cartan_Quartic_Residual_Extension.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class QuarticPolynomialTests(unittest.TestCase):
    def test_fourth_coefficient_stencil_and_sixth_order_extrapolation(self):
        def polynomial(t):
            return np.array([3+5*t+2*t*t+7*t**3+11*t**4+13*t**5+17*t**6,
                             1-t+3*t*t-2*t**4+5*t**6])
        coarse, fine = model.quartic_estimates(polynomial)
        np.testing.assert_allclose(coarse, [11, -2], atol=1e-12)
        np.testing.assert_allclose(fine, [11, -2], atol=1e-11)

    def test_new_corrections_leave_retained_and_cubic_origin_orders_unchanged(self):
        for powers, maximum, amplitude in ((model.E6, 5, model.common.RADIUS**2),
                                            (model.P5, 4, model.common.RADIUS)):
            for order in range(maximum+1):
                for indices in itertools.combinations_with_replacement(range(4), order):
                    np.testing.assert_array_equal(model.common.derivative_weights(powers, np.zeros(4), indices, amplitude), 0)

    def test_independent_monomial_packing(self):
        coefficients = np.zeros(model.COUNT)
        coefficients[16*model.E6.index((6, 0, 0, 0))] = 2
        start = 16*len(model.E6)
        pi = model.P5.index((0, 5, 0, 0))
        coefficients[start+24*pi] = 3
        coefficients[start+24*pi+14] = 1
        coefficients[start+24*len(model.P5)+16*model.P5.index((5, 0, 0, 0))] = 4
        x = model.common.RADIUS*np.array([.25, .5, 0, 0])
        fields = model.common.unpack_fields(model.field_correction(x, coefficients))
        self.assertAlmostEqual(fields["coframe_second"][0, 0, 0, 0], 60*.25**4)
        self.assertAlmostEqual(fields["psi_first"][1, 0, 0].real, 15*.5**4)
        self.assertAlmostEqual(fields["psi_first"][1, 0, 2].imag, 5*.5**4)
        self.assertAlmostEqual(fields["multiplier_first"][0, 0, 0], 20*.25**4)

    def test_new_field_and_higher_jets_come_from_one_polynomial(self):
        coefficients = np.random.default_rng(20261029).normal(size=model.COUNT)*1e-7
        x = model.common.RADIUS*np.array([.2, .3, -.1, .4])
        fields = model.common.unpack_fields(model.field_correction(x, coefficients))
        derivatives = model.common.lower.prior.previous.field_derivatives(fields, model.higher_correction(x, coefficients))
        step = model.common.RADIUS*1e-4
        for r, direction in enumerate(np.eye(4)):
            plus = model.field_correction(x+step*direction, coefficients)
            minus = model.field_correction(x-step*direction, coefficients)
            np.testing.assert_allclose((plus-minus)/(2*step), model.common.pack_fields(derivatives[r]), atol=1e-8, rtol=1e-6)


class QuarticExtensionReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Quartic_Residual_Extension.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_dimensions(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["shape"], [3360, 3584])
        self.assertEqual((self.report["unknown_count"], self.report["quartic_monomials"]), (3584, 35))

    def test_quartic_fit_resolves_only_to_observed_extraction_accuracy(self):
        self.assertLess(self.report["predicted_quartic_remainder_norm"], 1e-10)
        self.assertLess(self.report["fine_estimate_remainder_norm"], 2*self.report["baseline_estimate_step_change"])
        self.assertLess(self.report["fixed_coordinate_quartic_drift"], 1e-12)
        self.assertGreater(self.report["retained_condition_estimate"], 1e8)
        self.assertTrue(np.isfinite(self.report["fine_fit_coefficient_change_norm"]))
        for check in self.report["checks"]:
            self.assertLess(check["response_prediction_error"], 2e-10)

    def test_radial_residuals_are_consistent_with_fifth_order(self):
        for check in self.report["checks"]:
            radii = check["radius_checks"]
            for first, second in zip(radii, radii[1:]):
                ratio = first["after"]/second["after"]
                self.assertGreater(ratio, 29)
                self.assertLess(ratio, 35)
            for sample in radii:
                self.assertLess(sample["after"], sample["before"])
                self.assertLess(sample["fine_fit_after"], sample["before"])
                self.assertLess(sample["new_normal_coordinate_drift"], 1e-12)
            self.assertLess(check["cubic_change_norm"], 1e-9)

    def test_stored_polynomial_reproduces_independent_equation_checks(self):
        prepared, point, jets, full, ordinary, spinor = model.load_background()
        coefficients = np.asarray(self.report["coefficients"])
        for check in self.report["checks"]:
            x = model.common.RADIUS*np.asarray(check["direction"])
            fields = model.background_fields(prepared, point, jets, full, ordinary, spinor, x)
            corrected = model.common.unpack_fields(model.common.pack_fields(fields)+model.field_correction(x, coefficients))
            actual = np.linalg.norm(model.common.lower.lower_residual(prepared, corrected))
            self.assertAlmostEqual(actual, check["radius_checks"][0]["after"], delta=1e-12)

    def test_scope_does_not_promote_samples_to_regional_solution(self):
        self.assertTrue(self.report["origin_and_cubic_preserved_by_degree"])
        self.assertTrue(self.report["exact_parent_kernel_certificate_remains_authoritative"])
        self.assertTrue(self.report["sample_extraction_can_reach_two_times_previous_radius"])
        self.assertTrue(self.report["no_regional_PDE_solution_or_interval_certificate"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
