"""Primary-equation refresh, complex packing and original off-shell controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("refreshed_probe_test", ROOT / "analysis/HC_Cartan_Refreshed_Probe_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class PrimaryModelTests(unittest.TestCase):
    def test_complex_to_real_packing_preserves_norm_and_entire_tail(self):
        rng = np.random.default_rng(191401)
        coefficients = rng.normal(size=(70, 12))+1j*rng.normal(size=(70, 12))
        source = model.T(coefficients, .17)
        result = model.realify_probe(source)
        np.testing.assert_array_equal(result.coefficients[:, :12], source.coefficients.real)
        np.testing.assert_array_equal(result.coefficients[:, 12:], source.coefficients.imag)
        np.testing.assert_allclose(result.coefficient_norms(), source.coefficient_norms(), atol=2e-15)
        self.assertEqual(result.tail, source.tail)

    def test_invalid_probe_shape_rejected(self):
        for value in (np.zeros(24), np.zeros((3, 4))):
            with self.assertRaises(ValueError):
                model.realify_probe(model.core.tensor(value))

    def test_nonzero_off_shell_primary_rows_and_multiplier_derivative(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        fields["multiplier_first"] = fields["multiplier_first"]+np.random.default_rng(191402).normal(size=(4, 4, 4))*.01
        inputs = model.full.point_models(fields)
        omega, volume, inverse, _, _ = model.prior.connection_models(case[0], inputs)
        constraint, probe, _ = model.primary_models(inputs, omega, volume, inverse)
        expected = model.common.lower.lower_residual(case[0], fields)
        self.assertGreater(np.linalg.norm(expected[:40]), 1e-3)
        np.testing.assert_allclose(constraint.center.ravel(), expected[:16], atol=2e-12, rtol=0)
        np.testing.assert_allclose(probe.center, expected[16:40], atol=2e-12, rtol=0)
        self.assertEqual(constraint.tail, 0.)
        self.assertEqual(probe.tail, 0.)
        without_dl = dict(inputs)
        without_dl["dl"] = model.core.tensor(np.zeros((4, 4, 4)))
        _, altered, _ = model.primary_models(without_dl, omega, volume, inverse)
        self.assertGreater(np.linalg.norm(probe.center-altered.center), 1e-3)

    def test_connection_derivatives_are_not_used_by_primary_equations(self):
        case = model.control.load_case()
        fields = model.full.field_models(case, model.common.RADIUS)
        omega, volume, inverse, _, _ = model.prior.connection_models(case[0], fields)
        original = model.primary_models(fields, omega, volume, inverse)
        random = np.random.default_rng(191403)
        changed = model.J(omega.value, [model.T(model.core.tensor(random.normal(size=(4, 4, 4))).coefficients, 1e6) for _ in range(4)])
        replacement = model.primary_models(fields, changed, volume, inverse)
        for a, b in zip(original[:2], replacement[:2]):
            np.testing.assert_array_equal(a.coefficients, b.coefficients)
            self.assertEqual(a.tail, b.tail)
        self.assertGreater(original[2]["weight_divergence_tail"], 0.)


class RefreshedProbeReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Refreshed_Probe_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("primary_equation_contractions_unchanged", "coframe_and_curl_enclosures_unchanged",
                     "no_connection_derivative_needed_by_primary_equations", "physical_weights_derivative_models_retained",
                     "complex_to_real_probe_packing_is_isometric", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "not_a_full_outward_rounded_certificate", "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_all_stored_coefficients_and_last_40_enclosures_unchanged(self):
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            a, b = np.asarray(report["coefficients"]), np.asarray(parent["coefficients"])
            np.testing.assert_array_equal(a.view(np.uint8), b.view(np.uint8))
            self.assertEqual(report["coefficient_identity_error"], 0.)
            self.assertEqual(report["coframe"], parent["coframe"])
            self.assertEqual(report["curl"], parent["curl"])
            for level in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][level], 1e-12)

    def test_primary_bounds_improve_and_all_probe_terms_remain(self):
        for report in self.report["reports"]:
            self.assertLess(report["constraint"]["tail_bound"], report["previous_constraint_tail"])
            self.assertLess(report["probe"]["tail_bound"], report["previous_probe_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            pieces = report["tail_diagnostics"]
            for key, value in pieces.items():
                self.assertTrue(np.all(np.asarray(value) > 0), key)
            self.assertAlmostEqual(report["probe"]["tail_bound"], sum(pieces[k] for k in
                ("kinetic_probe_tail", "mass_probe_tail", "balance_probe_tail")))

    def test_two_radii_and_original_equation_samples_not_existence(self):
        a, b = self.report["reports"]
        self.assertEqual(a["radius"], 2*b["radius"])
        self.assertGreater(a["combined"]["tail_bound"]/b["combined"]["tail_bound"], 31.)
        self.assertLess(a["combined"]["tail_bound"]/b["combined"]["tail_bound"], 34.)
        for report in (a, b):
            for check in report["sample_checks_not_the_proof"]:
                for key in ("constraint", "probe", "combined"):
                    self.assertLess(check[key+"_tail_discrepancy"], report[key]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e3*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
