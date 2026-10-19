"""Exact polynomial complex controls and nonzero floating defect diagnostics."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("low_exterior_test", ROOT / "analysis/HC_Cartan_Low_Order_Exterior_Compatibility.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class PolynomialComplexTests(unittest.TestCase):
    def test_d_squared_zero_in_multiple_orders(self):
        for degree in range(1, 6):
            for order in range(3):
                result = model.integer_product(model.derivative_matrix(degree-1, order+1),
                    model.derivative_matrix(degree, order))
                self.assertFalse(np.any(result))

    def test_integer_radial_homotopy_on_complete_coefficient_spaces(self):
        for degree in range(1, 5):
            for order in range(1, 4):
                exact = model.integer_product(model.derivative_matrix(degree+1, order-1),
                    model.contraction_matrix(degree, order))
                remainder = model.integer_product(model.contraction_matrix(degree-1, order+1),
                    model.derivative_matrix(degree, order))
                np.testing.assert_array_equal(exact+remainder, (degree+order)*np.eye(exact.shape[0], dtype=np.int64))

    def test_exact_quartic_projector_dimensions(self):
        certificate = model.exact_quartic_certificate()
        self.assertEqual(certificate["single_component_two_form_dimension"], 210)
        self.assertEqual(certificate["single_component_closed_dimension"], 140)
        self.assertEqual(certificate["four_component_curl_dimension"], 840)
        self.assertEqual(certificate["four_component_closed_dimension"], 560)
        self.assertEqual(certificate["four_component_compatibility_rank"], 280)
        self.assertTrue(certificate["projector_need_not_be_orthogonal"])

    def test_closed_curl_is_reproduced_by_homotopy(self):
        rng = np.random.default_rng(191930)
        one_form = rng.integers(-3, 4, size=(len(model.powers(5))*4, 4), dtype=np.int64)
        curls = model.integer_product(model.derivative_matrix(5, 1), one_form)
        self.assertFalse(np.any(model.integer_product(model.derivative_matrix(4, 2), curls)))
        potential_six = model.integer_product(model.contraction_matrix(4, 2), curls)
        np.testing.assert_array_equal(model.integer_product(model.derivative_matrix(5, 1), potential_six), 6*curls)

    def test_nonclosed_control_is_not_silently_declared_a_potential(self):
        curls = np.zeros((len(model.powers(4))*6, 1), dtype=np.int64)
        index = model.powers(4).index((4, 0, 0, 0))*6+model.form_indices(2).index((1, 2))
        curls[index] = 1
        derivative = model.integer_product(model.derivative_matrix(4, 2), curls)
        self.assertGreater(np.linalg.norm(derivative), 0.)
        obstruction_six = model.integer_product(model.contraction_matrix(3, 3), derivative)
        represented_six = model.integer_product(model.derivative_matrix(5, 1),
            model.integer_product(model.contraction_matrix(4, 2), curls))
        self.assertGreater(np.linalg.norm(obstruction_six), 0.)
        np.testing.assert_array_equal(represented_six+obstruction_six, 6*curls)

    def test_correction_order_barrier_and_invalid_domains(self):
        self.assertEqual(model.lowest_possible_residual_degree(7, 6, 6), 5)
        self.assertEqual(model.lowest_possible_residual_degree(6, 5, 5), 4)
        for degrees in ((1, 6, 6), (7, 6.5, 6)):
            with self.assertRaises(ValueError):
                model.lowest_possible_residual_degree(*degrees)
        with self.assertRaises(ValueError):
            model.derivative_matrix(2, 4)
        with self.assertRaises(ValueError):
            model.contraction_matrix(2, 0)
        with self.assertRaises(ValueError):
            model.integer_product(np.array([[2**62]], dtype=np.int64), np.array([[4]], dtype=np.int64))


class ExteriorReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Low_Order_Exterior_Compatibility.json").read_text(encoding="utf-8"))

    def test_saved_inputs_scope_and_nonzero_defects(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        for flag in ("next_order_extensions_cannot_remove_existing_degree_four_defects",
                "formal_potential_realizability_by_allowed_fields_not_established", "no_new_fit_field_or_low_order_coefficient_change",
                "floating_identity_discrepancies_are_not_exact_incompatibility_certificates", "not_regional_existence_or_native_identification"):
            self.assertTrue(self.report[flag])
        for report in self.report["reports"]:
            self.assertGreater(report["quartic_curl_norm"], 1e-12)
            self.assertGreater(report["homotopy_obstruction_norm"], 0.)
            self.assertLess(report["homotopy_reconstruction_discrepancy"], 1e-24)
            self.assertGreater(report["formal_constitutive_degree_five_target_norm"], 0.)
            for control in report["lower_coefficient_identity_controls"]:
                self.assertLess(control["identity_discrepancy_norm"], 1e-12)
            self.assertEqual(np.shape(report["formal_constitutive_degree_five_potential"]), (56, 4, 4))

    def test_reproduction_and_homogeneous_radius_scaling(self):
        parent = json.loads((ROOT / "analysis/HC_Cartan_Centered_Spinor_Source_Bound.json").read_text(encoding="utf-8"))
        for original, saved in zip(parent["reports"], self.report["reports"]):
            recomputed = model.analyze_report(original)
            self.assertEqual(recomputed, saved)
        large, small = self.report["reports"]
        self.assertAlmostEqual(small["quartic_curl_norm"]/large["quartic_curl_norm"], 1/16)
        self.assertAlmostEqual(small["formal_constitutive_degree_five_target_norm"]/large["formal_constitutive_degree_five_target_norm"], 1/32)


if __name__ == "__main__":
    unittest.main()
