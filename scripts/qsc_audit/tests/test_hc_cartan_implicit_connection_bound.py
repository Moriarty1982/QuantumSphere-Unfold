"""Implicit inverse derivative, fixed embedding and original-connection controls."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("implicit_connection_test", ROOT / "analysis/HC_Cartan_Implicit_Connection_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ImplicitConnectionTests(unittest.TestCase):
    def test_embedding_exact_gram_and_saturation(self):
        basis = model.BASIS_OPERATOR
        np.testing.assert_array_equal(basis, basis.astype(int))
        exact = sp.Matrix(basis.astype(int))
        self.assertEqual(exact.T*exact, 2*sp.eye(24))
        self.assertGreaterEqual(Fraction.from_float(model.BASIS_NORM_UPPER)**2, Fraction(2))
        vector = model.core.tensor(np.arange(24, dtype=float))
        vector.tail = .3
        result = model.embed(vector)
        self.assertEqual(np.vdot(result.center, result.center), 2*np.vdot(vector.center, vector.center))
        self.assertEqual(result.tail, model.BASIS_NORM_UPPER*vector.tail)
        with self.assertRaises(ValueError):
            model.embed(model.core.tensor(np.zeros(23)))

    def test_implicit_polynomial_agrees_with_product_rule_without_zeroing(self):
        h = model.core.tensor(np.diag([2., 3.]))
        h.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = np.array([[.03, .02], [.01, -.02]])
        f = model.core.tensor(np.array([.7, -.3]))
        f.coefficients[model.core.INDEX[(0, 1, 0, 0)]] = [.1, .2]
        dh = [model.core.tensor(h.coefficients[model.core.INDEX[(1, 0, 0, 0)]]),
              *[model.core.tensor(np.zeros((2, 2))) for _ in range(3)]]
        df = [model.core.tensor(np.zeros(2)), model.core.tensor(np.array([.1, .2])),
              model.core.tensor(np.zeros(2)), model.core.tensor(np.zeros(2))]
        result, old, _ = model.implicit_solve(model.J(h, dh), model.J(f, df))
        np.testing.assert_array_equal(result.value.coefficients, old.value.coefficients)
        for a, b in zip(result.derivatives, old.derivatives):
            np.testing.assert_allclose(a.coefficients, b.coefficients, atol=1e-16, rtol=1e-13)
        self.assertGreater(np.linalg.norm(result.derivatives[0].center), .001)

    def test_uncertain_inverse_and_physical_derivatives_enclosed(self):
        rng = np.random.default_rng(191301)
        h = model.core.tensor(np.diag([2., 3.]))
        h.coefficients[model.core.INDEX[(0, 0, 2, 0)]] = np.array([[.01, .02], [-.01, .01]])
        h.tail = .001
        f = model.core.tensor(np.array([.5, -.2]))
        f.coefficients[model.core.INDEX[(0, 0, 0, 3)]] = [.02, .03]
        f.tail = .002
        dh = [model.core.tensor(rng.normal(size=(2, 2))*.01) for _ in range(4)]
        df = [model.core.tensor(rng.normal(size=2)*.03) for _ in range(4)]
        for v in dh+df:
            v.tail = .0001
        result, _, _ = model.implicit_solve(model.J(h, dh), model.J(f, df))
        for y in (np.ones(4), np.array([-.2, .1, -.3, .4])):
            values = []
            for v in [h, f, *dh, *df]:
                error = rng.normal(size=v.center.shape)
                values.append(v.evaluate(y)+error*v.tail/np.linalg.norm(error))
            actual_h, actual_f = values[:2]
            actual_k = np.linalg.solve(actual_h, actual_f)
            self.assertLess(np.linalg.norm(actual_k-result.value.evaluate(y)), result.value.tail)
            for r in range(4):
                actual_dk = np.linalg.solve(actual_h, values[6+r]-values[2+r] @ actual_k)
                self.assertLess(np.linalg.norm(actual_dk-result.derivatives[r].evaluate(y)), result.derivatives[r].tail)

    def test_invalid_or_unresolved_implicit_inverse_rejected(self):
        with self.assertRaises(ValueError):
            model.implicit_solve(model.J(np.ones((2, 3))), model.J(np.zeros(2)))
        with self.assertRaises(ValueError):
            model.implicit_solve(model.J(np.eye(2)), model.J(np.zeros(3)))
        h = model.core.tensor(np.eye(2))
        h.tail = 1.
        with self.assertRaises(ValueError):
            model.implicit_solve(model.J(h), model.J(np.zeros(2)))

    def test_connection_matches_independent_original_jets_off_shell(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        inputs = model.full.point_models(fields)
        omega, _, _, _, pieces = model.connection_models(case[0], inputs)
        original = model.general.connection_jets(case[0], fields)
        np.testing.assert_allclose(omega.value.center, original["omega"], atol=2e-12, rtol=1e-13)
        for actual, expected in zip(omega.derivatives, original["first"]):
            np.testing.assert_allclose(actual.center, expected, atol=2e-12, rtol=1e-13)
            self.assertEqual(actual.tail, 0.)
        self.assertEqual(omega.value.tail, 0.)
        self.assertLess(pieces["connection_derivative_coefficient_error"], 1e-12)


class ImplicitConnectionReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Implicit_Connection_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("no_unknown_value_tail_differentiated", "all_inverse_and_product_tails_retained",
                     "constraint_and_probe_bounds_deliberately_inherited", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "only_fixed_linear_constants_are_exactly_certified", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_first_40_rows_unchanged_and_low_order_defects_retained(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, :40], np.asarray(parent["coefficients"])[:, :40])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            for level in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][level], 1e-12)

    def test_two_separate_improvement_controls_and_original_point_checks(self):
        for report in self.report["reports"]:
            pieces = report["connection_diagnostics"]
            for old, middle, new in zip(pieces["old_connection_derivative_tails"],
                    pieces["basis_only_connection_derivative_tails"], pieces["new_connection_derivative_tails"]):
                self.assertGreater(new, 0.)
                self.assertLess(new, middle)
                self.assertLess(middle, old)
            self.assertLess(pieces["connection_derivative_coefficient_error"], 1e-12)
            self.assertEqual(pieces["connection_value_coefficient_error"], 0.)
            self.assertLess(report["coframe"]["tail_bound"], report["previous_coframe_tail"])
            self.assertLess(report["curl"]["tail_bound"], report["previous_curl_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["connection_value_tail_discrepancy"], pieces["new_connection_value_tail"])
                for error, bound in zip(check["connection_derivative_tail_discrepancies"], pieces["new_connection_derivative_tails"]):
                    self.assertLess(error, bound)
                self.assertLess(check["coframe_tail_discrepancy"], report["coframe"]["tail_bound"])
                self.assertLess(check["curl_tail_discrepancy"], report["curl"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e3*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
