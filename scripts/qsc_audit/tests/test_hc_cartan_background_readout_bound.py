"""Exact upper square roots, fixed readout maps and retained deviations."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("background_readout_test", ROOT / "analysis/HC_Cartan_Background_Readout_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class FixedReadoutTests(unittest.TestCase):
    def test_dyadic_sqrt_upper_is_proved_by_exact_square(self):
        for value in (Fraction(0), Fraction(1), Fraction(2), Fraction(1, 3), Fraction(999, 7),
                      Fraction(2)**400/Fraction(3), Fraction(2)**-400/Fraction(7)):
            upper = model.rational_sqrt_upper(value)
            self.assertGreaterEqual(Fraction.from_float(upper)**2, value)
            if value:
                self.assertLess(Fraction.from_float(upper)**2, value*Fraction(100000000000001, 100000000000000))

    def test_negative_and_nonrepresentable_sqrt_bounds_rejected(self):
        for value in (Fraction(-1), Fraction(2)**2200, Fraction(2)**-2300):
            with self.assertRaises(ValueError):
                model.rational_sqrt_upper(value)

    def test_exact_map_and_complete_cache_keys(self):
        rng = np.random.default_rng(161123)
        left = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        right = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        cache = {}
        frozen = model.frozen_map(left, right, np.eye(3), cache)
        self.assertIs(frozen, model.frozen_map(left.copy(), right.copy(), np.eye(3), cache))
        changed = left.copy()
        changed[0, 0] += .001
        self.assertIsNot(frozen, model.frozen_map(changed, right, np.eye(3), cache))
        self.assertEqual(len(cache), 2)
        exact = sp.Matrix([[sp.Rational(v) for v in row] for row in frozen["exact_coefficients"]])
        gram = exact*exact.T
        bound = max(sum(abs(gram[i, j]) for j in range(4)) for i in range(4))
        self.assertEqual(str(bound), frozen["exact_gram_row_bound"])
        self.assertGreaterEqual(sp.Rational(frozen["upper"])**2, bound)

    def test_centered_polynomial_readout_matches_direct_variable_expression(self):
        rng = np.random.default_rng(161124)
        left = model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
        right = model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
        left.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(3, 4))*.1
        right.coefficients[model.core.INDEX[(0, 1, 0, 0)]] = rng.normal(size=(3, 4))*.1j
        omega = model.core.tensor(rng.normal(size=(4, 4, 4)))
        omega.coefficients[model.core.INDEX[(0, 0, 1, 0)]] = rng.normal(size=(4, 4, 4))*.1
        result = model.centered_readout(left, right, omega, model.general.prolong.Q, {})
        y = np.array([.3, -.2, .1, .4])
        response = np.einsum("mbc,abcij->maij", omega.evaluate(y), model.prior.hermitian.RESPONSE)
        expected = np.einsum("ui,uv,vj,maij->ma", left.evaluate(y).conj(), model.general.prolong.Q,
                             right.evaluate(y), response).imag
        np.testing.assert_allclose(result.evaluate(y), expected, atol=1e-13)
        self.assertEqual(result.tail, 0.)

    def test_zero_frozen_center_does_not_erase_variable_readout(self):
        rng = np.random.default_rng(161125)
        psi = model.core.tensor(np.zeros((3, 4), complex))
        psi.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        omega = model.core.tensor(rng.normal(size=(4, 4)))
        cache = {}
        result = model.centered_readout(psi, psi, omega, model.general.prolong.Q, cache)
        self.assertEqual(next(iter(cache.values()))["upper"], 0.)
        self.assertGreater(np.linalg.norm(result.evaluate([1, 0, 0, 0])), .1)
        self.assertEqual(result.tail, 0.)

    def test_complex_connection_and_nonhermitian_selector_rejected(self):
        zero = model.core.tensor(np.zeros((3, 4), complex))
        with self.assertRaises(ValueError):
            model.centered_readout(zero, zero, model.core.tensor(np.eye(4)*1j), np.eye(3), {})
        selector = np.eye(3)
        selector[0, 1] = .1
        with self.assertRaises(ValueError):
            model.frozen_map(zero.center, zero.center, selector, {})


class BackgroundReadoutReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Background_Readout_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_six_exact_map_bounds(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(len(self.report["frozen_maps"]), 6)
        for frozen in self.report["frozen_maps"]:
            exact = sp.Matrix([[sp.Rational(v) for v in row] for row in frozen["exact_coefficients"]])
            gram = exact*exact.T
            bound = max(sum(abs(gram[i, j]) for j in range(4)) for i in range(4))
            self.assertEqual(bound, sp.Rational(frozen["exact_gram_row_bound"]))
            self.assertGreaterEqual(sp.Rational(frozen["upper"])**2, bound)

    def test_only_expression_grouping_changes_not_the_field_or_fixed_rows(self):
        for report, original in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, :40], np.asarray(original["coefficients"])[:, :40])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][4], 1e-12)

    def test_bounds_improve_and_the_uncertainty_is_not_dropped(self):
        a, b = self.report["reports"]
        self.assertGreater(a["combined"]["whole_cube_upper_estimate"], .37)
        self.assertLess(a["combined"]["whole_cube_upper_estimate"], .38)
        self.assertGreater(b["combined"]["whole_cube_upper_estimate"], .011)
        self.assertLess(b["combined"]["whole_cube_upper_estimate"], .012)
        for report in (a, b):
            self.assertLess(report["curl"]["tail_bound"], report["previous_curl_tail"])
            self.assertLess(report["coframe"]["tail_bound"], report["previous_coframe_tail"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e4*check["actual_norm"])

    def test_constant_off_shell_readouts_keep_original_curl_and_coframe(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        connection = model.general.connection_jets(case[0], fields)
        omega = model.full.TaylorJet(model.core.tensor(connection["omega"]), [model.core.tensor(v) for v in connection["first"]])
        inputs = model.full.point_models(fields)
        cache = {}
        curls = model.curl_model(inputs, omega, cache)
        coframe, _ = model.coframe_model(inputs, omega, model.core.tensor(np.asarray(connection["volume"])),
            model.core.tensor(connection["inverse"]), cache)
        actual = model.common.lower.lower_residual(case[0], fields)
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        np.testing.assert_allclose(curls.center, actual[56:], atol=1e-12, rtol=0)
        np.testing.assert_allclose(coframe.center.ravel(), actual[40:56], atol=1e-12, rtol=0)

    def test_exact_fixed_map_does_not_promote_the_whole_enclosure_to_certificate(self):
        for flag in ("no_coefficients_fitted_or_zeroed", "not_a_frozen_spinor_approximation",
                     "only_fixed_map_norm_bounds_use_exact_rational_certificates",
                     "not_a_full_outward_rounded_certificate", "not_exact_closure_or_regional_solution"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
