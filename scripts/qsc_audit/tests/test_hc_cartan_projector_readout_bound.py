"""Exact projector norm certificates, fallback and unchanged variable readouts."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("projector_readout_test", ROOT / "analysis/HC_Cartan_Projector_Readout_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ProjectorNormTests(unittest.TestCase):
    def test_exact_scaled_projector_and_zero_map(self):
        for scale in (sp.Rational(0), sp.Rational(3, 2)):
            matrix = sp.diag(scale, scale, scale, 0)
            result = model.certified_gram_norm(matrix)
            self.assertTrue(result["projector_identity_verified"])
            self.assertEqual(sp.Rational(result["exact_scale"]), scale**2)
            self.assertGreaterEqual(Fraction.from_float(result["upper"])**2, Fraction(scale**2))

    def test_nonprojector_fallback_and_invalid_inputs(self):
        result = model.certified_gram_norm(sp.diag(1, 2, 3, 4))
        self.assertFalse(result["projector_identity_verified"])
        self.assertEqual(result["upper"], 4.)
        self.assertEqual(result["exact_squared_norm_or_upper"], "16")
        for value in (sp.eye(3), sp.diag(1, 1, 1, sp.I), sp.diag(1, 1, 1, sp.sqrt(2))):
            with self.assertRaises(ValueError):
                model.certified_gram_norm(value)

    def test_cache_uses_full_inputs_and_never_modifies_parent_entry(self):
        rng = np.random.default_rng(191601)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        cache = {}
        a = model.frozen_map(psi, psi, np.eye(3), cache)
        self.assertIs(a, model.frozen_map(psi.copy(), psi.copy(), np.eye(3), cache))
        altered = psi.copy()
        altered[0, 0] += .001
        self.assertIsNot(a, model.frozen_map(altered, psi, np.eye(3), cache))
        self.assertEqual(len(cache), 2)
        old = model.readout.frozen_map(psi, psi, np.eye(3), {})
        self.assertEqual(old["upper"], a["previous_upper"])
        self.assertLessEqual(a["upper"], old["upper"])

    def test_variable_and_zero_center_cross_terms_are_unchanged(self):
        rng = np.random.default_rng(191602)
        for zero in (False, True):
            center = np.zeros((3, 4), complex) if zero else rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
            psi = model.core.tensor(center)
            psi.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
            omega = model.core.tensor(rng.normal(size=(6, 4, 4)))
            omega.tail = .001
            result = model.centered_readout(psi, psi, omega, model.general.prolong.Q, {})
            old = model.readout.centered_readout(psi, psi, omega, model.general.prolong.Q, {})
            np.testing.assert_array_equal(result.coefficients, old.coefficients)
            self.assertLessEqual(result.tail, old.tail)
            self.assertGreater(np.linalg.norm(result.evaluate(np.ones(4))), .01)
            self.assertGreater(result.tail, 0.)

    def test_nonzero_off_shell_curl_matches_independent_original(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        inputs = model.full.point_models(fields)
        omega, _, _, _, _ = model.connection_core.connection_models(case[0], inputs)
        result, _ = model.curl_model(inputs, omega, {})
        expected = model.common.lower.lower_residual(case[0], fields)[56:]
        self.assertGreater(np.linalg.norm(expected), 1e-4)
        np.testing.assert_allclose(result.center, expected, atol=2e-12, rtol=0)
        self.assertEqual(result.tail, 0.)


class ProjectorReadoutReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Projector_Readout_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_five_exact_gram_identities_and_upper_constants(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(len(self.report["frozen_maps"]), 5)
        for entry in self.report["frozen_maps"]:
            exact = sp.Matrix([[sp.Rational(v) for v in row] for row in entry["exact_coefficients"]])
            gram = exact*exact.T
            scale = sp.Rational(entry["exact_scale"])
            self.assertEqual(gram*gram, scale*gram)
            self.assertEqual(gram.rank(), 3)
            self.assertEqual(scale, sp.trace(gram)/3)
            self.assertGreaterEqual(sp.Rational(entry["upper"])**2, scale)
            self.assertLess(entry["upper"], entry["previous_upper"])
            self.assertTrue(entry["projector_identity_verified"])

    def test_coefficients_unchanged_low_order_errors_retained_and_bounds_improve(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"]).view(np.uint8), np.asarray(parent["coefficients"]).view(np.uint8))
            self.assertEqual(report["coefficient_identity_error"], 0.)
            for key in ("constraint", "probe", "coframe"):
                self.assertEqual(report[key], parent[key])
            self.assertLess(report["curl"]["tail_bound"], report["previous_curl_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for degree in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][degree], 1e-12)
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["curl_tail_discrepancy"], report["curl"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])

    def test_scope_and_proof_boundary(self):
        for flag in ("exact_gram_identity_checked_not_assumed", "nonprojector_maps_use_row_bound_fallback",
                     "all_variable_spinor_cross_terms_retained", "other_56_components_and_enclosures_unchanged",
                     "no_coefficients_fitted_or_low_order_defects_zeroed", "projector_rank_not_a_source_gate_identification",
                     "only_fixed_map_constants_are_exactly_certified", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
