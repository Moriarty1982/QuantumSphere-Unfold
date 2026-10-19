"""Hermitian constraint identity and retained variable/error contributions."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hermitian_constraint_test", ROOT / "analysis/HC_Cartan_Hermitian_Constraint_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def direct_constraint(psi, dp, e, omega):
    gamma = model.general.cartan.GAMMA
    spin = -.25*np.einsum("mbc,bij,cjk->mik", omega, gamma, gamma)
    covariant = dp+np.einsum("mij,uj->mui", spin, psi)
    return np.einsum("ui,uv,mvj,aij->am", psi.conj(), model.general.prolong.Q,
        covariant, model.general.prolong.WEIGHTS).imag-e


class HermitianConstraintTests(unittest.TestCase):
    def test_identity_requires_hermitian_weight_but_no_equation(self):
        rng = np.random.default_rng(191701)
        raw = rng.normal(size=(12, 12))+1j*rng.normal(size=(12, 12))
        h = raw+raw.conj().T
        s = rng.normal(size=(12, 12))+1j*rng.normal(size=(12, 12))
        psi = rng.normal(size=12)+1j*rng.normal(size=12)
        left = np.vdot(psi, h @ s @ psi).imag
        right = .5*np.vdot(psi, (h @ s-s.conj().T @ h) @ psi).imag
        self.assertAlmostEqual(left, right, places=11)
        bad_left = np.vdot(psi, raw @ s @ psi).imag
        bad_right = .5*np.vdot(psi, (raw @ s-s.conj().T @ raw) @ psi).imag
        self.assertGreater(abs(bad_left-bad_right), .1)

    def test_variable_polynomial_matches_original_readout(self):
        rng = np.random.default_rng(191702)
        fields = {"psi": model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))),
            "dp": model.core.tensor(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))),
            "e": model.core.tensor(np.eye(4))}
        omega = model.core.tensor(rng.normal(size=(4, 4, 4)))
        for value in [*fields.values(), omega]:
            value.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=value.center.shape)*.03
        result, _ = model.constraint_model(fields, model.full.TaylorJet(omega), {})
        for y in (np.ones(4), np.array([-.3, .1, .2, .4])):
            actual = direct_constraint(*(fields[k].evaluate(y) for k in ("psi", "dp", "e")), omega.evaluate(y))
            np.testing.assert_allclose(result.evaluate(y), actual, atol=2e-13, rtol=1e-13)
        self.assertEqual(result.tail, 0.)

    def test_zero_spinor_center_retains_variable_response_and_coframe_tail(self):
        rng = np.random.default_rng(191703)
        psi = model.core.tensor(np.zeros((3, 4), complex))
        psi.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        e = model.T(model.core.tensor(np.zeros((4, 4))).coefficients, .02)
        fields = {"psi": psi, "dp": model.core.tensor(np.zeros((4, 3, 4), complex)), "e": e}
        omega = model.full.TaylorJet(rng.normal(size=(4, 4, 4)))
        result, pieces = model.constraint_model(fields, omega, {})
        self.assertEqual(np.linalg.norm(result.center), 0.)
        self.assertGreater(np.linalg.norm(result.evaluate(np.ones(4))), .01)
        self.assertEqual(pieces["coframe_value_tail"], .02)
        self.assertEqual(result.tail, .02)

    def test_uncertain_readout_encloses_all_input_errors(self):
        rng = np.random.default_rng(191704)
        fields = {"psi": model.T(model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))).coefficients, .001),
            "dp": model.T(model.core.tensor(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))).coefficients, .002),
            "e": model.T(model.core.tensor(np.eye(4)).coefficients, .003)}
        omega = model.T(model.core.tensor(rng.normal(size=(4, 4, 4))).coefficients, .004)
        result, _ = model.constraint_model(fields, model.full.TaylorJet(omega), {})
        for _ in range(4):
            actual = []
            for index, value in enumerate([fields[k] for k in ("psi", "dp", "e")]+[omega]):
                error = rng.normal(size=value.center.shape)
                if index < 2:
                    error = error+1j*rng.normal(size=value.center.shape)
                actual.append(value.center+error*value.tail/np.linalg.norm(error))
            self.assertLess(np.linalg.norm(direct_constraint(*actual)-result.center), result.tail)

    def test_nonzero_off_shell_constraint_matches_independent_original(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        inputs = model.full.point_models(fields)
        omega, _, _, _, _ = model.prior.connection_core.connection_models(case[0], inputs)
        result, _ = model.constraint_model(inputs, omega, {})
        expected = model.common.lower.lower_residual(case[0], fields)[:16].reshape(4, 4)
        self.assertGreater(np.linalg.norm(expected), 1e-3)
        np.testing.assert_allclose(result.center, expected, atol=2e-12, rtol=0)
        self.assertEqual(result.tail, 0.)


class ConstraintReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Hermitian_Constraint_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_proof_boundary(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("identity_is_off_shell", "hermitian_fixed_weights_required",
                     "all_variable_spinor_cross_terms_and_coframe_tail_retained", "other_64_components_and_enclosures_unchanged",
                     "no_coefficients_fitted_or_low_order_defects_zeroed", "only_previously_certified_fixed_readout_constant_used",
                     "not_a_full_outward_rounded_certificate", "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_64_components_and_low_order_defects_retained(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, 16:], np.asarray(parent["coefficients"])[:, 16:])
            for key in ("probe", "coframe", "curl"):
                self.assertEqual(report[key], parent[key])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertGreater(report["constraint"]["coefficient_level_bounds"][4], 1e-12)
            for degree in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][degree], 1e-12)

    def test_improvement_keeps_all_tail_terms_and_original_samples(self):
        for report in self.report["reports"]:
            self.assertLess(report["constraint"]["tail_bound"], report["previous_constraint_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            self.assertAlmostEqual(report["constraint"]["tail_bound"], sum(report["tail_diagnostics"].values()))
            self.assertTrue(all(v > 0 for v in report["tail_diagnostics"].values()))
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["constraint_tail_discrepancy"], report["constraint"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])


if __name__ == "__main__":
    unittest.main()
