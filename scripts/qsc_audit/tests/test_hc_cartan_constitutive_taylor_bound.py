"""Taylor cancellation, product tails, inverse bounds and field controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "constitutive_taylor_bound_test", ROOT / "analysis/HC_Cartan_Constitutive_Taylor_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def monomial(power, value):
    coefficients = np.zeros((len(model.POWERS), *np.asarray(value).shape), dtype=np.asarray(value).dtype)
    coefficients[model.INDEX[power]] = value
    return model.TaylorTensor(coefficients)


class TaylorAlgebraTests(unittest.TestCase):
    def test_basis_and_convolution_indices_cover_all_retained_pairs(self):
        self.assertEqual(len(model.POWERS), 70)
        self.assertEqual(len(model.PAIRS), 495)
        for i, j, k in model.PAIRS:
            self.assertEqual(tuple(a+b for a, b in zip(model.POWERS[i], model.POWERS[j])), model.POWERS[k])

    def test_polynomial_cancellation_is_retained_before_norms(self):
        value = monomial((1, 0, 0, 0), np.array([1., -3.]))
        difference = value-value
        np.testing.assert_array_equal(difference.coefficients, 0)
        self.assertEqual(difference.polynomial_norm()+difference.tail, 0.)
        uncertain = model.TaylorTensor(value.coefficients, .1)
        self.assertEqual((uncertain-uncertain).tail, .2)

    def test_high_degree_product_is_included_in_tail(self):
        a = monomial((3, 0, 0, 0), 2.)
        b = monomial((2, 0, 0, 0), -3.)
        product = model.contract(",->", a, b)
        np.testing.assert_array_equal(product.coefficients, 0)
        self.assertEqual(product.tail, 6.)

    def test_multilinear_contraction_matches_independent_complex_polynomial(self):
        a = model.tensor(np.array([[1., 2j], [3., 4.]]))+monomial((1, 0, 0, 0), np.array([[.2, .3], [.4j, .1]]))
        b = model.tensor(np.array([[.1, .2], [.3, .4]]))+monomial((0, 2, 0, 0), np.eye(2))
        weight = np.array([[2., 1.], [-1., 3.]])
        result = model.contract("ij,jk,kl->il", a.conjugate(), weight, b)
        y = np.array([.3, -.4, .2, .1])
        np.testing.assert_allclose(result.evaluate(y), a.evaluate(y).conj() @ weight @ b.evaluate(y), atol=2e-15)
        self.assertEqual(result.tail, 0.)

    def test_summed_single_operand_indices_include_trace_factor(self):
        a = model.TaylorTensor(model.tensor(np.zeros(3)).coefficients, 1.)
        result = model.contract("i,->", a, 2.)
        self.assertAlmostEqual(result.tail, 2*np.sqrt(3))

    def test_scalar_matrix_inverse_matches_geometric_remainder(self):
        value = model.tensor(np.ones((1, 1)))+monomial((1, 0, 0, 0), np.array([[-.1]]))
        inverse, q = model.matrix_inverse(value)
        self.assertAlmostEqual(q, .1)
        self.assertAlmostEqual(inverse.tail, .1**5/.9)
        for y0 in (-1., -.2, .5, 1.):
            y = np.array([y0, 0, 0, 0])
            error = np.linalg.norm(inverse.evaluate(y)-np.linalg.inv(value.evaluate(y)))
            self.assertLessEqual(error, inverse.tail+1e-15)

    def test_matrix_inverse_controls_noncommuting_coefficients(self):
        value = (model.tensor(np.array([[2., .1], [.2, 1.]]))
                 +monomial((1, 0, 0, 0), np.array([[.01, .03], [-.02, .01]]))
                 +monomial((0, 1, 0, 0), np.array([[.02, -.01], [.03, -.02]])))
        inverse, q = model.matrix_inverse(value)
        self.assertLess(q, 1.)
        for y in (np.array([1., -1., 0, 0]), np.array([-.3, .4, .1, .2])):
            self.assertLess(np.linalg.norm(inverse.evaluate(y)-np.linalg.inv(value.evaluate(y))), inverse.tail+1e-14)

    def test_unresolved_inverse_and_outside_domain_rejected(self):
        with self.assertRaises(ValueError):
            model.matrix_inverse(model.tensor(np.ones((1, 1)))+monomial((1, 0, 0, 0), np.ones((1, 1))))
        with self.assertRaises(ValueError):
            model.tensor(1.).evaluate([2., 0, 0, 0])
        with self.assertRaises(ValueError):
            model.contract("ii,j->j", np.eye(2), np.ones(2))

    def test_monomial_derivative_and_discarded_field_term(self):
        value = model.monomial_terms([(6, 0, 0, 0)], np.array([[2.]]),
                                    model.common.RADIUS**2, model.common.RADIUS, (0,))
        self.assertEqual(value.polynomial_norm(), 0.)
        self.assertAlmostEqual(value.tail, 12*model.common.RADIUS)
        second = model.monomial_terms([(5, 0, 0, 0)], np.array([[2.]]),
                                     model.common.RADIUS, model.common.RADIUS, (0,))
        self.assertAlmostEqual(second.evaluate([.5, 0, 0, 0])[0], 10*.5**4)


class ConstitutiveTaylorReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Constitutive_Taylor_Bound.json").read_text(encoding="utf-8"))
        cls.case = model.control.load_case()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertTrue(self.report["no_coefficients_fitted_or_zeroed"])
        self.assertTrue(self.report["not_all_80_equations"])
        self.assertTrue(self.report["not_outward_rounded_or_interval_certified"])
        self.assertTrue(self.report["not_exact_low_order_vanishing_or_regional_solution"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_field_polynomials_reproduce_saved_field_with_declared_tails(self):
        fields = model.field_models(self.case, model.common.RADIUS)
        mapping = {"e": "coframe", "de": "coframe_first", "psi": "psi", "dp": "psi_first", "lam": "multiplier"}
        for y in (np.array([.3, -.2, .1, .4]), np.eye(4)[0], np.array([-.5, .5, .5, -.5])):
            actual, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*y)
            for key, name in mapping.items():
                self.assertLessEqual(np.linalg.norm(actual[name]-fields[key].evaluate(y)), fields[key].tail+1e-13)

    def test_constant_off_shell_models_match_independent_constraint_equation(self):
        fields, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        rng = np.random.default_rng(161114)
        fields["coframe"] = fields["coframe"]+rng.normal(size=(4, 4))*1e-3
        fields["psi"] = fields["psi"]+rng.normal(size=(3, 4))*1e-3
        mapping = {"e": "coframe", "de": "coframe_first", "psi": "psi", "dp": "psi_first", "lam": "multiplier"}
        result, _ = model.constitutive_model(self.case[0], {k: model.tensor(fields[v]) for k, v in mapping.items()})
        actual = model.general.equations(self.case[0], fields)["constraint"]
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        np.testing.assert_allclose(result.center, actual, atol=1e-12, rtol=0)
        self.assertEqual(result.tail, 0.)

    def test_bound_improves_natural_enclosure_but_remains_conservative(self):
        a, b = self.report["reports"]
        self.assertLess(a["whole_cube_upper_estimate"], .03)
        self.assertGreater(a["whole_cube_upper_estimate"], .01)
        self.assertGreater(2362./a["whole_cube_upper_estimate"], 80000.)
        self.assertGreater(a["tail_bound"]/b["tail_bound"], 31.)
        self.assertLess(a["tail_bound"]/b["tail_bound"], 34.)
        self.assertGreater(a["coefficient_level_bounds"][4], 1e-12)
        for report in (a, b):
            self.assertLess(report["coframe_neumann_ratio"], 1.)
            self.assertLess(report["hessian_neumann_ratio"], 1.)
            self.assertAlmostEqual(sum(report["coefficient_level_bounds"])+report["tail_bound"], report["whole_cube_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["tail_discrepancy"], report["tail_bound"])
                self.assertGreater(report["tail_bound"], 1e5*check["actual_norm"])

    def test_stored_coefficients_reproduce_residual_polynomial(self):
        report = self.report["reports"][0]
        polynomial = model.TaylorTensor(np.asarray(report["coefficients"]), report["tail_bound"])
        for check in report["sample_checks_not_the_proof"]:
            self.assertAlmostEqual(np.linalg.norm(polynomial.evaluate(check["direction"])), check["polynomial_norm"], delta=1e-20)


if __name__ == "__main__":
    unittest.main()
