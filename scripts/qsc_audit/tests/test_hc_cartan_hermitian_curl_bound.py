"""Off-shell identities, frozen Clifford response and improved curl tail checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hermitian_curl_test", ROOT / "analysis/HC_Cartan_Hermitian_Curl_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def direct_curls(psi, dp, de, omega, first):
    spin = model.general.prolong.spin_lift(omega)
    dspin = model.general.prolong.spin_lift(first)
    covariant = dp+np.einsum("mij,uj->mui", spin, psi)
    values = []
    for r in range(4):
        for s in range(r+1, 4):
            difference = np.einsum("ij,uj->ui", dspin[r, s]-dspin[s, r], psi)
            difference += dp[r] @ spin[s].T-dp[s] @ spin[r].T
            for a, weight in enumerate(model.general.prolong.WEIGHTS):
                value = (np.vdot(dp[r], (model.general.prolong.Q @ covariant[s]) @ weight.T)
                    -np.vdot(dp[s], (model.general.prolong.Q @ covariant[r]) @ weight.T)
                    +np.vdot(psi, (model.general.prolong.Q @ difference) @ weight.T))
                values.append(value.imag-de[r, a, s]+de[s, a, r])
    return np.asarray(values)


class HermitianCurlIdentityTests(unittest.TestCase):
    def test_frozen_response_is_exactly_the_antihermitian_spin_weight(self):
        def exact(matrix):
            return sp.Matrix([[sp.Rational(float(z.real))+sp.I*sp.Rational(float(z.imag)) for z in row] for row in matrix])

        weights = [exact(v) for v in model.general.prolong.WEIGHTS]
        gamma = [exact(v) for v in model.general.cartan.GAMMA]
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    generator = -gamma[b]*gamma[c]/4
                    response = weights[a]*generator-generator.H*weights[a]
                    self.assertEqual(response, exact(model.RESPONSE[a, b, c]))
                    self.assertEqual(response+response.H, sp.zeros(4))

    def test_identity_matches_arbitrary_real_connections_off_shell(self):
        rng = np.random.default_rng(241118)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        dp = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        de = rng.normal(size=(4, 4, 4))
        omega = rng.normal(size=(4, 4, 4))
        first = rng.normal(size=(4, 4, 4, 4))
        fields = {"psi": model.core.tensor(psi), "dp": model.core.tensor(dp), "de": model.core.tensor(de)}
        connection = model.prior.TaylorJet(model.core.tensor(omega), [model.core.tensor(v) for v in first])
        result = model.curl_model(fields, connection)
        expected = direct_curls(psi, dp, de, omega, first)
        self.assertGreater(np.linalg.norm(expected), 1.)
        np.testing.assert_allclose(result.center, expected, atol=3e-13, rtol=2e-14)
        self.assertEqual(result.tail, 0.)

    def test_identity_does_not_force_nonzero_curls_to_zero(self):
        rng = np.random.default_rng(241119)
        psi = np.zeros((3, 4), complex)
        dp = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        de, omega, first = np.zeros((4, 4, 4)), np.zeros((4, 4, 4)), np.zeros((4, 4, 4, 4))
        connection = model.prior.TaylorJet(model.core.tensor(omega), [model.core.tensor(v) for v in first])
        fields = {"psi": model.core.tensor(psi), "dp": model.core.tensor(dp), "de": model.core.tensor(de)}
        result = model.curl_model(fields, connection)
        self.assertGreater(np.linalg.norm(result.center), 1.)
        np.testing.assert_allclose(result.center, direct_curls(psi, dp, de, omega, first), atol=1e-13)

    def test_nonhermitian_selector_or_weights_rejected(self):
        weights = model.general.prolong.WEIGHTS.copy()
        weights[0, 0, 1] += .01j
        with self.assertRaises(ValueError):
            model.hermitian_response(weights, model.general.cartan.GAMMA)
        selector = model.general.prolong.Q.copy()
        selector[0, 1] += .01
        with self.assertRaises(ValueError):
            model.curl_model({}, None, selector=selector)


class HermitianCurlReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Hermitian_Curl_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()
        cls.case = model.control.load_case()

    def test_fingerprints_and_response_structure(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["response_antihermitian_error"], 0.)
        self.assertEqual(self.report["response_antisymmetric_connection_index_error"], 0.)

    def test_first_56_coefficients_and_non_curl_bounds_are_unchanged(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, :56], np.asarray(parent["coefficients"])[:, :56])
            tails = [parent["blocks"][k]["tail_bound"] for k in ("constraint", "probe", "coframe")]
            self.assertAlmostEqual(report["combined"]["tail_bound"], np.linalg.norm([*tails, report["curl"]["tail_bound"]]))

    def test_all_curl_coefficients_preserve_original_polynomial(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            delta = np.asarray(report["coefficients"])[:, 56:]-np.asarray(parent["coefficients"])[:, 56:]
            self.assertAlmostEqual(np.linalg.norm(delta), report["coefficient_identity_error"], delta=1e-25)
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertGreater(report["curl"]["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["curl"]["coefficient_level_bounds"][4], 1e-12)

    def test_regrouping_improves_bounds_without_changing_actual_samples(self):
        for report in self.report["reports"]:
            self.assertGreater(report["previous_curl_tail"]/report["curl"]["tail_bound"], 11.)
            self.assertGreater(report["previous_combined_upper_estimate"]/report["combined"]["whole_cube_upper_estimate"], 4.)
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["point_identity_error"], 1e-12)
                self.assertLess(check["curl_tail_discrepancy"], report["curl"]["tail_bound"])
                self.assertGreater(report["curl"]["tail_bound"], 1e4*check["curl_actual_norm"])

    def test_coframe_is_now_the_largest_block_and_radius_behavior_persists(self):
        a, b = self.report["reports"]
        self.assertGreater(self.parent["reports"][0]["blocks"]["coframe"]["tail_bound"], a["curl"]["tail_bound"])
        self.assertGreater(a["curl"]["tail_bound"]/b["curl"]["tail_bound"], 31.)
        self.assertLess(a["curl"]["tail_bound"]/b["curl"]["tail_bound"], 34.)
        self.assertLess(a["combined"]["whole_cube_upper_estimate"], 2.4)
        self.assertLess(b["combined"]["whole_cube_upper_estimate"], .08)

    def test_actual_displaced_field_reproduces_saved_identity_control(self):
        report = self.report["reports"][0]
        check = report["sample_checks_not_the_proof"][2]
        fields, _ = model.control.fields_and_higher(self.case, report["radius"]*np.asarray(check["direction"]))
        actual = model.common.lower.lower_residual(self.case[0], fields)[56:]
        self.assertAlmostEqual(np.linalg.norm(actual), check["curl_actual_norm"], delta=1e-12)
        np.testing.assert_allclose(model.compact_at_point(self.case[0], fields), actual, atol=1e-12, rtol=0)

    def test_scope_retains_unsolved_equations_and_precision_boundary(self):
        for flag in ("no_coefficients_fitted_or_zeroed", "identity_does_not_require_field_equations",
                     "not_outward_rounded_or_interval_certified", "not_exact_low_order_closure_or_regional_solution"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
