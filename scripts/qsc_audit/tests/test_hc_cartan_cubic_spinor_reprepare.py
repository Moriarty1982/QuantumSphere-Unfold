"""Cubic improvement, exact retained-origin kernel and binary64 warnings."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cubic_spinor_test", ROOT / "analysis/HC_Cartan_Cubic_Spinor_Reprepare.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class SpinorCoordinateTests(unittest.TestCase):
    def test_fourth_coordinate_conversion_round_trip(self):
        quads = list(model.common.lower.prior.previous.first.prior.joint.third.diagnostic.QUADS)
        coefficients = np.random.default_rng(20261026).normal(size=840)*1e-7
        values = model.fourth_coordinates(coefficients, quads)
        np.testing.assert_allclose(model.from_fourth_coordinates(values, quads), coefficients, atol=1e-20)

    def test_spinor_value_and_first_derivatives_share_one_polynomial(self):
        coefficients = np.random.default_rng(20261027).normal(size=840)*1e-7
        x = model.common.RADIUS*np.array([.2, .3, -.1, .4])
        fields = model.common.unpack_fields(model.spinor_fields(x, coefficients))
        step = model.common.RADIUS*1e-4
        for r, direction in enumerate(np.eye(4)):
            plus = model.spinor_fields(x+step*direction, coefficients)[240:264]
            minus = model.spinor_fields(x-step*direction, coefficients)[240:264]
            expected = model.general.prior.joint.prior.realify(fields["psi_first"][r])
            np.testing.assert_allclose((plus-minus)/(2*step), expected, atol=1e-12, rtol=1e-6)


class SpinorReprepareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Cubic_Spinor_Reprepare.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_exact_certificate_reconstructs_all_35_zero_updates(self):
        certificate = self.report["exact_origin_preservation_certificate"]
        matrix = sp.Matrix([[sp.Rational(value) for value in row] for row in certificate["readout_matrix"]])
        pivots = sp.Matrix([[sp.Rational(value) for value in row] for row in certificate["pivot_map"]])
        self.assertEqual(matrix.rank(), 4)
        for values in certificate["free_monomial_coefficients"]:
            free = sp.Matrix([sp.Rational(value) for value in values])
            dependent = pivots @ free
            vector = [sp.S.Zero]*24
            for index, value in zip(certificate["free_columns"], free):
                vector[index] = value
            for index, value in zip(certificate["pivot_columns"], dependent):
                vector[index] = value
            self.assertEqual(matrix @ sp.Matrix(vector), sp.zeros(4, 1))
        self.assertTrue(certificate["all_35_readout_updates_exactly_zero"])

    def test_certificate_uses_actual_frozen_readout_inputs(self):
        prepared, point, jets, _, full, _ = model.general.domain.load_data()
        origin = model.general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
        actual = model.exact_readout_matrix(origin)
        saved = sp.Matrix([[sp.Rational(value) for value in row] for row in
                           self.report["exact_origin_preservation_certificate"]["readout_matrix"]])
        self.assertEqual(actual, saved)
        self.assertEqual(self.report["highest_nonC3_spinor_response_norm"], 0)
        self.assertLess(self.report["origin_C3_symbol_match_error"], 1e-12)

    def test_cubic_remainder_is_at_observed_extraction_floor(self):
        self.assertEqual((self.report["spinor_preservation_rank"], self.report["spinor_kernel_dimension"]), (140, 700))
        self.assertLess(self.report["predicted_cubic_norm_after_origin_refinement"], 1e-10)
        self.assertLess(self.report["fine_cubic_remainder_norm"], 2*self.report["baseline_estimate_step_change"])
        self.assertLess(self.report["normal_coordinate_cubic_drift"], 1e-12)

    def test_radial_decay_changes_to_approximately_fourth_order(self):
        for check in self.report["checks"]:
            self.assertLess(check["actual_cubic_norm"], 1e-10)
            self.assertLess(check["cubic_prediction_error"], 1e-10)
            radii = check["radius_checks"]
            for first, second in zip(radii, radii[1:]):
                self.assertGreater(first["corrected"]/second["corrected"], 15)
                self.assertLess(first["corrected"]/second["corrected"], 17)

    def test_rounded_origin_failure_is_not_hidden(self):
        self.assertLess(self.report["old_origin_1114_norm"], 1e-8)
        self.assertGreater(self.report["new_origin_1114_norm"], 1e-8)
        self.assertFalse(self.report["rounded_origin_passes_1e_minus_8"])
        self.assertGreater(self.report["spinor_fourth_jet_change_norm"], 1e8)

    def test_scope_excludes_regional_solution(self):
        self.assertTrue(self.report["no_regional_PDE_solution_or_all_order_extension"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
