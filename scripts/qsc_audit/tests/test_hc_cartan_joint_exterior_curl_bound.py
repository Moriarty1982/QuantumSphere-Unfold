"""Joint exterior operator and unchanged off-shell curl equations."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("joint_exterior_test", ROOT / "analysis/HC_Cartan_Joint_Exterior_Curl_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ExteriorOperatorTests(unittest.TestCase):
    def test_exact_gram_and_dyadic_upper(self):
        d = sp.Matrix(model.EXTERIOR_OPERATOR.reshape(6, 16).astype(int))
        self.assertEqual(d*d.T, 2*sp.eye(6))
        self.assertEqual(d.rank(), 6)
        self.assertGreaterEqual(Fraction.from_float(model.EXTERIOR_NORM_UPPER)**2, Fraction(2))

    def test_norm_is_saturated_not_a_frobenius_substitution(self):
        tensor = np.zeros((4, 4, 4, 4))
        tensor[0, 1, 0, 0], tensor[1, 0, 0, 0] = 1., -1.
        result = np.einsum("krs,rsab->kab", model.EXTERIOR_OPERATOR, tensor)
        self.assertEqual(np.vdot(result, result), 2*np.vdot(tensor, tensor))
        self.assertGreater(np.linalg.norm(model.EXTERIOR_OPERATOR), model.EXTERIOR_NORM_UPPER)

    def test_independently_controlled_derivative_errors_enclosed(self):
        rng = np.random.default_rng(191101)
        derivatives = [model.core.tensor(rng.normal(size=(4, 4, 4))) for _ in range(4)]
        for r, derivative in enumerate(derivatives):
            derivative.coefficients[model.core.INDEX[(0, 0, 0, 4)]] = rng.normal(size=(4, 4, 4))*.01
            derivative.tail = .01*(r+1)
        result = model.exterior_model(derivatives)
        for y in (np.ones(4), np.array([.2, -.3, .1, -.4])):
            first = []
            for derivative in derivatives:
                error = rng.normal(size=(4, 4, 4))
                first.append(derivative.evaluate(y)+error*derivative.tail/np.linalg.norm(error))
            actual = np.einsum("krs,rsab->kab", model.EXTERIOR_OPERATOR, np.asarray(first))
            self.assertLess(np.linalg.norm(actual-result.evaluate(y)), result.tail)
        self.assertAlmostEqual(result.tail, model.EXTERIOR_NORM_UPPER*np.linalg.norm([d.tail for d in derivatives]))

    def test_pair_order_and_validation(self):
        self.assertEqual(model.PAIRS, ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
        for values in ([], [model.core.tensor(np.zeros((4, 4)))]*4):
            with self.assertRaises(ValueError):
                model.exterior_model(values)

    def test_variable_spinor_and_connection_match_original_polynomial_expression(self):
        rng = np.random.default_rng(191102)
        for zero_center in (False, True):
            psi = model.core.tensor(np.zeros((3, 4), complex) if zero_center else
                rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
            psi.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
            omega = model.core.tensor(rng.normal(size=(4, 4, 4)))
            omega.coefficients[model.core.INDEX[(0, 1, 0, 0)]] = rng.normal(size=(4, 4, 4))*.1
            derivatives = [model.core.tensor(rng.normal(size=(4, 4, 4))) for _ in range(4)]
            for derivative in derivatives:
                derivative.coefficients[model.core.INDEX[(0, 0, 2, 0)]] = rng.normal(size=(4, 4, 4))*.1
            fields = {"psi": psi, "dp": model.core.tensor(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))),
                "de": model.core.tensor(rng.normal(size=(4, 4, 4)))}
            connection = model.full.TaylorJet(omega, derivatives)
            result, _ = model.curl_model(fields, connection, {})
            expected = model.readout.curl_model(fields, connection, {})
            np.testing.assert_allclose(result.coefficients, expected.coefficients, atol=1e-13, rtol=1e-13)
            self.assertEqual(result.tail, 0.)

    def test_nonzero_off_shell_curl_matches_original_evaluator(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        connection = model.general.connection_jets(case[0], fields)
        omega = model.full.TaylorJet(model.core.tensor(connection["omega"]), [model.core.tensor(v) for v in connection["first"]])
        result, _ = model.curl_model(model.full.point_models(fields), omega, {})
        actual = model.common.lower.lower_residual(case[0], fields)
        self.assertGreater(np.linalg.norm(actual[56:]), 1e-4)
        np.testing.assert_allclose(result.center, actual[56:], atol=2e-12, rtol=0)
        self.assertEqual(result.tail, 0.)


class JointExteriorReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Joint_Exterior_Curl_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("physical_derivative_models_retained_not_unknown_value_tail_differentiated",
                     "all_variable_spinor_readout_cross_terms_retained", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "only_fixed_linear_constants_are_exactly_certified", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_56_rows_and_nonzero_low_order_defects_unchanged(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, :56], np.asarray(parent["coefficients"])[:, :56])
            self.assertEqual(report["coframe"], parent["coframe"])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            for level in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][level], 1e-12)

    def test_bounds_improve_with_derivative_uncertainty_retained(self):
        for report in self.report["reports"]:
            pieces = report["tail_diagnostics"]
            self.assertGreater(pieces["joint_exterior_input_tail"], 0.)
            self.assertGreater(pieces["joint_differentiated_readout_tail"], 0.)
            self.assertGreater(pieces["other_curl_terms_tail"], 0.)
            self.assertAlmostEqual(report["curl"]["tail_bound"], pieces["joint_differentiated_readout_tail"]+pieces["other_curl_terms_tail"])
            self.assertLess(report["curl"]["tail_bound"], report["previous_curl_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["curl_tail_discrepancy"], report["curl"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e4*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
