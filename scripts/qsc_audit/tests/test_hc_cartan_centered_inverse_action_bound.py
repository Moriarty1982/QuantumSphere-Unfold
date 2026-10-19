"""Certified center bounds and retained matrix/vector uncertainty."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("centered_inverse_test", ROOT / "analysis/HC_Cartan_Centered_Inverse_Action_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CenteredMatrixTests(unittest.TestCase):
    def test_reference_certificate_includes_nonzero_actual_center_error(self):
        center = np.diag([1., .5])
        center[0, 1] = 2.**-53
        cache = {}
        bound = model.fixed_matrix_bound(center, cache)
        self.assertIs(bound, model.fixed_matrix_bound(center.copy(), cache))
        self.assertTrue(bound["reference_gram_polynomial_verified"])
        error_squared = Fraction(bound["reference_error_squared"])
        self.assertGreater(error_squared, 0)
        excess = Fraction.from_float(bound["upper"])-1
        self.assertGreaterEqual(excess**2, error_squared)
        np.testing.assert_array_equal(center, np.array([[1., 2.**-53], [0., .5]]))

    def test_fallback_invalid_centers_and_exact_upward_sum(self):
        bound = model.fixed_matrix_bound(np.eye(2)*2, {})
        self.assertFalse(bound["reference_gram_polynomial_verified"])
        self.assertEqual(bound["upper"], 2.)
        for center in (np.eye(2)*1j, np.ones(2), np.zeros((0, 0)), np.array([[np.inf]])):
            with self.assertRaises(ValueError):
                model.fixed_matrix_bound(center, {})
        value = Fraction(1)+Fraction(1, 2**100)
        self.assertGreaterEqual(Fraction.from_float(model.upper_float(value)), value)
        for value in (Fraction(-1), Fraction(2)**2000):
            with self.assertRaises(ValueError):
                model.upper_float(value)

    def test_identity_center_vector_tail_does_not_get_frobenius_factor(self):
        vector = model.T(model.core.tensor(np.array([1., 2., 3.])).coefficients, .2)
        matrix = model.core.tensor(np.eye(3))
        result = model.matrix_vector(matrix, vector, {})
        self.assertEqual(result.tail, .2)
        self.assertGreater(model.c("pq,q->p", matrix, vector).tail, .3)
        with self.assertRaises(ValueError):
            model.matrix_vector(matrix, model.core.tensor(np.zeros(2)), {})

    def test_variable_matrix_cross_terms_discarded_products_and_tails_enclosed(self):
        rng = np.random.default_rng(191801)
        matrix = model.core.tensor(np.eye(3))
        vector = model.core.tensor(rng.normal(size=3)+1j*rng.normal(size=3))
        matrix.coefficients[model.core.INDEX[(3, 0, 0, 0)]] = rng.normal(size=(3, 3))*.03
        vector.coefficients[model.core.INDEX[(0, 2, 0, 0)]] = rng.normal(size=3)*.02
        matrix.tail, vector.tail = .001, .002
        result = model.matrix_vector(matrix, vector, {})
        for y in (np.ones(4), np.array([-.3, .4, .1, -.2])):
            da = rng.normal(size=(3, 3))
            db = rng.normal(size=3)+1j*rng.normal(size=3)
            actual = ((matrix.evaluate(y)+da*matrix.tail/np.linalg.norm(da))
                @ (vector.evaluate(y)+db*vector.tail/np.linalg.norm(db)))
            self.assertLess(np.linalg.norm(actual-result.evaluate(y)), result.tail)
        self.assertGreater(np.linalg.norm(result.coefficients[model.core.INDEX[(3, 0, 0, 0)]]), .001)

    def test_nonzero_off_shell_connection_and_derivatives_match_original(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        omega, _, _, _, pieces = model.connection_models(case[0], model.full.point_models(fields), {})
        original = model.general.connection_jets(case[0], fields)
        np.testing.assert_allclose(omega.value.center, original["omega"], atol=2e-12, rtol=1e-13)
        self.assertEqual(omega.value.tail, 0.)
        for actual, expected in zip(omega.derivatives, original["first"]):
            np.testing.assert_allclose(actual.center, expected, atol=2e-12, rtol=1e-13)
            self.assertEqual(actual.tail, 0.)
        self.assertLess(pieces["derivative_coefficient_identity_error"], 1e-12)


class CenteredInverseReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Centered_Inverse_Action_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_exact_production_reference_polynomial_and_full_center_error(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for report in self.report["reports"]:
            self.assertEqual(len(report["fixed_matrix_certificates"]), 1)
            bound = report["fixed_matrix_certificates"][0]
            reference = sp.Matrix([[sp.Rational(v) for v in row] for row in bound["reference"]])
            exact = sp.Matrix([[sp.Rational(v) for v in row] for row in bound["exact_center"]])
            gram = reference.T*reference
            self.assertEqual(gram*gram-sp.Rational(5, 4)*gram+sp.eye(24)/4, sp.zeros(24))
            self.assertEqual(sum(v*v for v in exact-reference), sp.Rational(bound["reference_error_squared"]))
            self.assertEqual(bound["upper"], 1.)

    def test_scope_low_order_defects_and_coefficients_preserved(self):
        for flag in ("actual_center_matrix_not_rounded_or_replaced", "all_variable_matrix_cross_terms_retained",
                     "reference_bound_checked_not_assumed", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "only_fixed_matrix_constants_are_exactly_certified", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        for report in self.report["reports"]:
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            for degree in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][degree], 1e-12)

    def test_bounds_improve_and_independent_original_point_controls_pass(self):
        for report, previous in zip(self.report["reports"], self.parent["reports"]):
            for key in ("constraint", "probe", "coframe", "curl", "combined"):
                self.assertLess(report[key]["tail_bound"], previous[key]["tail_bound"])
            pieces = report["connection_diagnostics"]
            self.assertLess(pieces["new_connection_value_tail"], pieces["old_connection_value_tail"])
            for old, new in zip(pieces["old_connection_derivative_tails"], pieces["new_connection_derivative_tails"]):
                self.assertLess(new, old)
                self.assertGreater(new, 0.)
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["connection_value_discrepancy"], pieces["new_connection_value_tail"])
                for error, tail in zip(check["connection_derivative_discrepancies"], pieces["new_connection_derivative_tails"]):
                    self.assertLess(error, tail)
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])


if __name__ == "__main__":
    unittest.main()
