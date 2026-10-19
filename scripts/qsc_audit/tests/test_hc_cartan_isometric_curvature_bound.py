"""Signed metric isometries and unchanged off-shell curvature/coframe rows."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("isometric_curvature_test", ROOT / "analysis/HC_Cartan_Isometric_Curvature_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CurvatureIsometryTests(unittest.TestCase):
    def test_fixed_signature_gram_is_exact_identity(self):
        eta = sp.Matrix(model.general.prolong.ETA.astype(int))
        self.assertEqual(eta.T*eta, sp.eye(4))
        both = sp.kronecker_product(eta, eta)
        self.assertEqual(both.T*both, sp.eye(16))

    def test_signed_axis_preserves_complex_norms_and_tail(self):
        rng = np.random.default_rng(191201)
        value = model.core.tensor(rng.normal(size=(4, 4, 4))+1j*rng.normal(size=(4, 4, 4)))
        value.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(4, 4, 4))
        value.tail = .123
        for axis in (0, 1, 2, -1):
            raised = model.signed_axis(value, model.general.prolong.ETA, axis)
            self.assertEqual(raised.tail, value.tail)
            np.testing.assert_array_equal(raised.coefficient_norms(), value.coefficient_norms())
            np.testing.assert_array_equal(model.signed_axis(raised, model.general.prolong.ETA, axis).coefficients, value.coefficients)

    def test_non_signature_metrics_and_invalid_axes_rejected(self):
        value = model.core.tensor(np.zeros((4, 4)))
        for metric in (np.eye(3), np.diag([2., 1., 1., 1.]), np.eye(4)+.01*np.ones((4, 4))):
            with self.assertRaises(ValueError):
                model.signed_axis(value, metric, 0)
        for axis in (2, -3):
            with self.assertRaises(ValueError):
                model.signed_axis(value, np.eye(4), axis)
        with self.assertRaises(ValueError):
            model.signed_axis(model.core.tensor(np.zeros((3, 4))), np.eye(4), 0)

    def test_constant_and_variable_curvature_coefficients_match_predecessor(self):
        rng = np.random.default_rng(191202)
        value = model.core.tensor(rng.normal(size=(4, 4, 4)))
        value.coefficients[model.core.INDEX[(0, 0, 3, 0)]] = rng.normal(size=(4, 4, 4))*.01
        derivatives = [model.core.tensor(rng.normal(size=(4, 4, 4))) for _ in range(4)]
        for r, derivative in enumerate(derivatives):
            derivative.coefficients[model.core.INDEX[(0, 2, 0, 0)]] = rng.normal(size=(4, 4, 4))*.01
            derivative.tail = .003*(r+1)
        value.tail = .002
        omega = model.full.TaylorJet(value, derivatives)
        result, pieces = model.curvature_model(omega)
        expected = model.ricci.trace.curvature_model(omega)
        np.testing.assert_array_equal(result.coefficients, expected.coefficients)
        self.assertLess(result.tail, expected.tail)
        self.assertEqual(pieces["curvature_derivative_tail"], 2*np.linalg.norm([v.tail for v in derivatives]))

    def test_curvature_encloses_discarded_products_and_all_uncertain_jets(self):
        rng = np.random.default_rng(191203)
        value = model.core.tensor(rng.normal(size=(4, 4, 4)))
        value.coefficients[model.core.INDEX[(0, 0, 3, 0)]] = rng.normal(size=(4, 4, 4))*.02
        value.tail = .003
        derivatives = [model.core.tensor(rng.normal(size=(4, 4, 4))) for _ in range(4)]
        for r, derivative in enumerate(derivatives):
            derivative.tail = .001*(r+1)
        result, _ = model.curvature_model(model.full.TaylorJet(value, derivatives))
        for y in (np.ones(4), np.array([.2, -.3, -.4, .1])):
            actual = []
            for v in (value, *derivatives):
                error = rng.normal(size=(4, 4, 4))
                actual.append(model.core.tensor(v.evaluate(y)+error*v.tail/np.linalg.norm(error)))
            exact = model.ricci.trace.curvature_model(model.full.TaylorJet(actual[0], actual[1:]))
            self.assertLess(np.linalg.norm(exact.center-result.evaluate(y)), result.tail)
            self.assertEqual(exact.tail, 0.)

    def test_actual_nonzero_off_shell_coframe_matches_original(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        connection = model.general.connection_jets(case[0], fields)
        omega = model.full.TaylorJet(model.core.tensor(connection["omega"]), [model.core.tensor(v) for v in connection["first"]])
        result, _ = model.coframe_model(model.full.point_models(fields), omega,
            model.core.tensor(np.asarray(connection["volume"])), model.core.tensor(connection["inverse"]), {})
        actual = model.general.equations(case[0], fields)["gravity"]
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        np.testing.assert_allclose(result.center, actual, atol=2e-12, rtol=0)
        self.assertEqual(result.tail, 0.)


class IsometricCurvatureReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Isometric_Curvature_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["signed_metric_action_exact_euclidean_operator_norm"], 1)
        for flag in ("not_an_indefinite_lorentz_norm_claim", "all_connection_value_and_derivative_tails_retained",
                     "no_coefficients_fitted_or_low_order_defects_zeroed", "only_fixed_linear_constants_are_exactly_certified",
                     "not_a_full_outward_rounded_certificate", "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_64_rows_and_low_order_defects_retained(self):
        indices = list(range(40))+list(range(56, 80))
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, indices], np.asarray(parent["coefficients"])[:, indices])
            self.assertEqual(report["curl"], parent["curl"])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertEqual(report["curvature_coefficient_identity_error"], 0.)
            for level in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][level], 1e-12)

    def test_recomputed_bounds_improve_and_samples_are_only_controls(self):
        for report in self.report["reports"]:
            pieces = report["tail_diagnostics"]
            self.assertGreater(pieces["curvature_commutator_tail"], 0.)
            self.assertGreater(pieces["curvature_derivative_tail"], 0.)
            self.assertGreater(pieces["connection_value_tail"], 0.)
            self.assertLess(pieces["curvature_tail"], report["previous_curvature_tail"])
            self.assertLess(report["coframe"]["tail_bound"], report["previous_coframe_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["coframe_tail_discrepancy"], report["coframe"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e4*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
