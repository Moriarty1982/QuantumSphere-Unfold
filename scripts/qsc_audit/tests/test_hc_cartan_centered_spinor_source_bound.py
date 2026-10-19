"""Centered quadratic source controls, including nonzero deviations at zero center."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("centered_source_test", ROOT / "analysis/HC_Cartan_Centered_Spinor_Source_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CenteredSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.control.load_case()
        cls.forms, _ = model.prior.source_support_certificate(cls.case[0]["component_forms"])
        cls.inverse, _ = model.frame.factorization_certificate(cls.case[0]["curvature_hessian"])

    def psi(self, seed=191920, uncertain=False):
        rng = np.random.default_rng(seed)
        value = model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
        derivatives = [model.core.tensor(.02*(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))) for _ in range(4)]
        if uncertain:
            value = model.T(value.coefficients, .001)
            derivatives = [model.T(d.coefficients, .0001) for d in derivatives]
        return model.J(value, derivatives)

    def original(self, psi, forms, selector):
        return model.jc("ui,uv,laij,vj->la", psi.conjugate(), selector, forms, psi).real()

    def test_realification_isometry_and_domain_guard(self):
        psi = self.psi(uncertain=True)
        result = model.realify(psi.value)
        self.assertEqual(result.tail, psi.value.tail)
        self.assertAlmostEqual(np.linalg.norm(result.coefficients), np.linalg.norm(psi.value.coefficients))
        with self.assertRaises(ValueError):
            model.realify(model.core.tensor(np.zeros(12)))

    def test_exact_fixed_map_gram_bound_and_cache_identity(self):
        center, cache = self.psi().value.center, {}
        fixed = model.frozen_source(center, self.forms, model.general.prolong.Q, cache)
        self.assertIs(fixed, model.frozen_source(center.copy(), self.forms.copy(), model.general.prolong.Q.copy(), cache))
        exact = sp.Matrix([[sp.Rational(v) for v in row] for row in fixed["exact_coefficients"]])
        gram = exact*exact.T
        bound = max(sum(abs(gram[i, j]) for j in range(24)) for i in range(24))
        self.assertEqual(str(bound), fixed["exact_gram_row_bound"])
        self.assertGreaterEqual(Fraction.from_float(fixed["upper"])**2, Fraction(int(bound.p), int(bound.q)))
        model.frozen_source(center, self.forms, np.eye(3), cache)
        model.frozen_source(center+.01, self.forms, np.eye(3), cache)
        model.frozen_source(center, self.forms*2, np.eye(3), cache)
        self.assertEqual(len(cache), 4)

    def test_arbitrary_off_shell_sources_and_derivatives(self):
        psi = self.psi()
        rng = np.random.default_rng(191921)
        forms = self.forms+.01*(rng.normal(size=self.forms.shape)+1j*rng.normal(size=self.forms.shape))
        for selector in (np.eye(3), model.general.prolong.Q):
            result = model.centered_source(psi, forms, selector, {})
            original = self.original(psi, forms, selector)
            for a, b in zip((result.value, *result.derivatives), (original.value, *original.derivatives)):
                np.testing.assert_allclose(a.center, b.center, atol=2e-13, rtol=2e-13)
                self.assertEqual(a.tail, 0.)

    def test_zero_center_does_not_freeze_nonzero_quadratic_deviations(self):
        psi = self.psi()
        coefficients = np.zeros_like(psi.value.coefficients)
        index = model.core.INDEX[(1, 0, 0, 0)]
        coefficients[index] = psi.value.center
        delta = model.J(model.T(coefficients, .001), psi.derivatives)
        result = model.centered_source(delta, self.forms, model.general.prolong.Q, {})
        original = self.original(delta, self.forms, model.general.prolong.Q)
        self.assertGreater(np.linalg.norm(result.value.evaluate(np.array([1., 0., 0., 0.]))), .01)
        self.assertGreater(result.value.tail, 0.)
        for a, b in zip((result.value, *result.derivatives), (original.value, *original.derivatives)):
            np.testing.assert_allclose(a.coefficients, b.coefficients, atol=2e-13)

    def test_nonhermitian_nonfinite_and_wrong_shapes_rejected(self):
        center = self.psi().value.center
        bad = np.eye(3, dtype=complex)
        bad[0, 1] = .01j
        for z, f, q in ((center, self.forms, bad), (center*np.nan, self.forms, np.eye(3)),
                (center, self.forms[:1], np.eye(3)), (center, self.forms, np.eye(2))):
            with self.assertRaises(ValueError):
                model.frozen_source(z, f, q, {})

    def test_uncertain_value_and_derivative_inputs_are_enclosed(self):
        psi = self.psi(uncertain=True)
        result = model.centered_source(psi, self.forms, model.general.prolong.Q, {})
        rng = np.random.default_rng(191922)
        def perturb(value):
            error = rng.normal(size=value.center.shape)+1j*rng.normal(size=value.center.shape)
            return value.center+error*(value.tail/np.linalg.norm(error))
        for _ in range(4):
            point = model.J(perturb(psi.value), [model.core.tensor(perturb(d)) for d in psi.derivatives])
            actual = self.original(point, self.forms, model.general.prolong.Q)
            for a, b in zip((result.value, *result.derivatives), (actual.value, *actual.derivatives)):
                self.assertGreater(a.tail, 0.)
                self.assertLess(np.linalg.norm(a.center-b.center), a.tail)

    def test_independent_original_connection_on_nonzero_background(self):
        fields, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        omega, _, _, _ = model.connection_models(self.case[0], model.full.point_models(fields), self.inverse, {})
        original = model.general.connection_jets(self.case[0], fields)
        np.testing.assert_allclose(omega.value.center, original["omega"], atol=2e-12, rtol=1e-13)
        for a, b in zip(omega.derivatives, original["first"]):
            np.testing.assert_allclose(a.center, b, atol=2e-12, rtol=1e-13)
        previous, _, _, _ = model.prior.connection_models(self.case[0], model.full.point_models(fields), self.inverse, {})
        for a, b in zip(omega.derivatives, previous.derivatives):
            np.testing.assert_array_equal(a.coefficients, b.coefficients)
            self.assertEqual(a.tail, b.tail)


class CenteredSourceReportTests(unittest.TestCase):
    def test_report_bounds_coefficients_scope_and_original_equations(self):
        report = json.loads((ROOT / "analysis/HC_Cartan_Centered_Spinor_Source_Bound.json").read_text(encoding="utf-8"))
        self.assertEqual(report["input_sha256"], model.input_fingerprints())
        self.assertFalse(report["main_TeX_PDF_changed"])
        for flag in ("quadratic_deviations_and_all_physical_derivatives_retained", "hermitian_selector_checked_not_assumed",
                "complete_parent_derivative_models_retained_not_tail_swapped",
                "realification_tail_isometry_used", "no_coefficients_fitted_or_low_order_defects_zeroed",
                "only_fixed_map_norm_constants_exactly_certified", "not_a_full_outward_rounded_certificate",
                "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(report[flag])
        for current, previous in zip(report["reports"], model.load_parent()["reports"]):
            self.assertLess(current["coefficient_identity_error"], 1e-12)
            self.assertEqual(len(current["frozen_sources"]), 2)
            for block in ("constraint", "probe", "coframe", "curl", "combined"):
                self.assertLess(current[block]["tail_bound"], previous[block]["tail_bound"])
            for degree in (3, 4):
                self.assertGreater(current["combined"]["coefficient_level_bounds"][degree], 1e-12)
            pieces = current["connection_diagnostics"]
            self.assertEqual(pieces["new_derivative_tails"], pieces["old_derivative_tails"])
            self.assertEqual(pieces["derivative_coefficient_error"], 0.)
            self.assertLess(pieces["new_value_tail"], pieces["old_value_tail"])
            self.assertTrue(any(a > b for a, b in zip(current["centered_candidate_derivative_tails"], pieces["old_derivative_tails"])))
            for check in current["sample_checks_not_the_proof"]:
                self.assertLess(check["combined_tail_discrepancy"], current["combined"]["tail_bound"])
                self.assertLess(check["connection_value_discrepancy"], pieces["new_value_tail"])
                for error, tail in zip(check["connection_derivative_discrepancies"], pieces["new_derivative_tails"]):
                    self.assertLess(error, tail)


if __name__ == "__main__":
    unittest.main()
