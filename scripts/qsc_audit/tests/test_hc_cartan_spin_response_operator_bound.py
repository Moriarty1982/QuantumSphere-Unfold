"""Exact response operator, saturation and unchanged-equation controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("spin_response_operator_test", ROOT / "analysis/HC_Cartan_Spin_Response_Operator_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class FixedResponseOperatorTests(unittest.TestCase):
    def test_exact_gram_matrix_is_four_times_antisymmetric_projector(self):
        operator = sp.Matrix([[sp.Rational(float(z.real))+sp.I*sp.Rational(float(z.imag)) for z in row]
                              for row in model.RESPONSE_OPERATOR])
        swap = sp.zeros(16)
        for i in range(4):
            for j in range(4):
                swap[4*i+j, 4*j+i] = 1
        gram = operator.H*operator
        self.assertEqual(gram, 2*(sp.eye(16)-swap))
        self.assertEqual(gram.eigenvals(), {sp.Integer(0): 10, sp.Integer(4): 6})

    def test_norm_two_is_attained_and_cannot_be_replaced_by_one(self):
        omega = np.zeros((4, 4))
        omega[0, 1], omega[1, 0] = 1/np.sqrt(2), -1/np.sqrt(2)
        self.assertAlmostEqual(np.linalg.norm(omega), 1.)
        result = model.response_model(model.core.tensor(omega))
        self.assertAlmostEqual(np.linalg.norm(result.center), 2.)

    def test_batched_complex_models_match_direct_response_contraction(self):
        rng = np.random.default_rng(161122)
        coefficients = np.zeros((70, 3, 2, 4, 4), complex)
        coefficients[0] = rng.normal(size=(3, 2, 4, 4))+1j*rng.normal(size=(3, 2, 4, 4))
        coefficients[model.core.INDEX[(0, 1, 0, 0)]] = rng.normal(size=(3, 2, 4, 4))*.1
        omega = model.T(coefficients, .03)
        result = model.response_model(omega)
        self.assertEqual(result.center.shape, (3, 2, 4, 4, 4))
        self.assertEqual(result.tail, .06)
        y = np.array([.2, -.3, .1, .4])
        expected = np.einsum("...bc,abcij->...aij", omega.evaluate(y), model.hermitian.RESPONSE)
        np.testing.assert_allclose(result.evaluate(y), expected, atol=1e-15)

    def test_tail_constant_does_not_grow_with_batch_count(self):
        omega = model.T(model.core.tensor(np.zeros((4, 4, 4))).coefficients, .1)
        old = model.c("mbc,abcij->maij", omega, model.hermitian.RESPONSE)
        new = model.response_model(omega)
        self.assertEqual(new.tail, .2)
        self.assertAlmostEqual(old.tail, .1*np.sqrt(24))
        self.assertLess(new.tail, old.tail)

    def test_bad_connection_shape_rejected(self):
        with self.assertRaises(ValueError):
            model.response_model(model.core.tensor(np.zeros((3, 3))))


class ResponseOperatorReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Spin_Response_Operator_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()
        cls.curl_parent = model.prior.load_parent()

    def test_fingerprints_and_all_coefficients_remain_unchanged(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["gram_projector_error"], 0.)
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"]), np.asarray(parent["coefficients"]))
            self.assertEqual(report["coefficient_identity_error"], 0.)

    def test_predecessor_curl_comparison_uses_latest_regrouped_bound(self):
        for report, parent in zip(self.report["reports"], self.curl_parent["reports"]):
            self.assertEqual(report["previous_curl_tail"], parent["curl"]["tail_bound"])
            self.assertLess(report["previous_curl_tail"], 1.)

    def test_bounds_improve_without_interpreting_them_as_solution_distance(self):
        a, b = self.report["reports"]
        self.assertGreater(a["combined"]["whole_cube_upper_estimate"], .46)
        self.assertLess(a["combined"]["whole_cube_upper_estimate"], .47)
        self.assertGreater(b["combined"]["whole_cube_upper_estimate"], .014)
        self.assertLess(b["combined"]["whole_cube_upper_estimate"], .015)
        for report in (a, b):
            self.assertLess(report["curl"]["tail_bound"], report["previous_curl_tail"])
            self.assertLess(report["coframe"]["tail_bound"], report["previous_coframe_tail"])
            self.assertGreater(report["previous_combined_upper_estimate"]/report["combined"]["whole_cube_upper_estimate"], 1.9)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][4], 1e-12)

    def test_actual_cube_samples_are_not_changed_by_the_operator_bound(self):
        for report in self.report["reports"]:
            polynomial = model.T(np.asarray(report["coefficients"]), report["combined"]["tail_bound"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["combined_tail_discrepancy"], polynomial.tail)
                self.assertLess(check["curl_tail_discrepancy"], report["curl"]["tail_bound"])
                self.assertLess(check["coframe_tail_discrepancy"], report["coframe"]["tail_bound"])
                self.assertGreater(polynomial.tail, 1e4*check["actual_norm"])

    def test_constant_off_shell_curl_and_coframe_still_match_original_equations(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(1+.3j)*.001
        fields["multiplier"] = fields["multiplier"]+.01*np.eye(4)
        connection = model.general.connection_jets(case[0], fields)
        omega = model.full.TaylorJet(model.core.tensor(connection["omega"]), [model.core.tensor(v) for v in connection["first"]])
        inputs = model.full.point_models(fields)
        curls = model.curl_model(inputs, omega)
        coframe, _ = model.coframe_model(inputs, omega, model.core.tensor(np.asarray(connection["volume"])),
                                        model.core.tensor(connection["inverse"]))
        actual = model.common.lower.lower_residual(case[0], fields)
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        np.testing.assert_allclose(curls.center, actual[56:], atol=1e-12, rtol=0)
        np.testing.assert_allclose(coframe.center.ravel(), actual[40:56], atol=1e-12, rtol=0)

    def test_scope_does_not_identify_response_rank_with_sources(self):
        for flag in ("no_coefficients_fitted_or_zeroed", "not_a_source_gate_identification",
                     "not_outward_rounded_or_interval_certified", "not_exact_low_order_closure_or_regional_solution"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
