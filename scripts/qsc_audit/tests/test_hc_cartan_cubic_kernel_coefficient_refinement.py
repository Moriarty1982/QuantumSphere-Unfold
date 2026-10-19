"""Exact kernel increments, independent coefficient maps and refreshed orders."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cubic_kernel_coeff_test", ROOT / "analysis/HC_Cartan_Cubic_Kernel_Coefficient_Refinement.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CubicKernelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        report = json.loads((ROOT / "analysis/HC_Cartan_Cubic_Spinor_Reprepare.json").read_text(encoding="utf-8"))
        cls.certificate = report["exact_origin_preservation_certificate"]
        cls.basis, cls.exact = model.kernel_basis(cls.certificate)

    def test_exact_basis_and_dependent_pivot_integrity(self):
        readout, _, _, _ = model.stable.reconstruct_certificate(self.certificate)
        self.assertEqual(self.basis.shape, (24, 20))
        for row in readout:
            for j in range(20):
                self.assertEqual(sum(row[i]*self.exact[i][j] for i in range(24)), 0)
        corrupt = {**self.certificate, "pivot_map": [row.copy() for row in self.certificate["pivot_map"]]}
        corrupt["pivot_map"][0][0] = str(Fraction(corrupt["pivot_map"][0][0])+1)
        with self.assertRaises(ValueError):
            model.kernel_basis(corrupt)

    def test_free_increment_is_added_rationally_before_pivot_reconstruction(self):
        rng = np.random.default_rng(191950)
        increment = rng.normal(size=(35, 20))*1e-8
        updated, blocks, delta = model.update_kernel_certificate(self.certificate, increment)
        old_free = self.certificate["free_monomial_coefficients"]
        for i in range(35):
            for j in range(20):
                expected = Fraction(old_free[i][j])+Fraction.from_float(float(increment[i, j]))
                self.assertEqual(Fraction(updated["free_monomial_coefficients"][i][j]), expected)
        readout, _, _, _ = model.stable.reconstruct_certificate(updated)
        self.assertTrue(all(v == 0 for row in model.stable.contract_readouts(readout, blocks) for v in row))
        self.assertTrue(all(v == 0 for row in model.stable.contract_readouts(readout, delta) for v in row))
        self.assertGreater(sum(abs(v) for row in delta for v in row), 0)

    def test_coefficient_map_matches_independent_old_node_maps(self):
        rng = np.random.default_rng(191951)
        jacobian, coordinates = rng.normal(size=(80, 440)), rng.normal(size=(16, 440))
        matrix = model.coefficient_response(jacobian, coordinates, self.basis)
        increment = rng.normal(size=model.COUNT)*1e-6
        leading = (matrix @ increment).reshape(20, 96)
        full_spinor = (increment[model.E_COUNT:model.E_COUNT+model.FREE_COUNT].reshape(35, 20) @ self.basis.T).ravel()
        ordinary = np.r_[increment[:model.E_COUNT], increment[model.E_COUNT+model.FREE_COUNT:]]
        for y in (np.eye(4)[0], np.eye(4)[3], np.array([.2, -.3, .1, .4])):
            field = (model.reprepare.gate.cubic_field_map(y) @ ordinary
                +model.reprepare.spinor_map(y) @ full_spinor)
            expected = np.vstack((jacobian, coordinates)) @ field
            monomials = np.array([np.prod(y**np.asarray(p)) for p in model.CUBICS])
            np.testing.assert_allclose(monomials @ leading, expected, atol=1e-17, rtol=1e-11)

    def test_invalid_shapes_and_nonfinite_inputs_rejected(self):
        with self.assertRaises(ValueError):
            model.update_kernel_certificate(self.certificate, np.zeros((35, 24)))
        with self.assertRaises(ValueError):
            model.update_kernel_certificate(self.certificate, np.full((35, 20), np.nan))
        with self.assertRaises(ValueError):
            model.coefficient_response(np.zeros((80, 440)), np.zeros((16, 440)), self.basis[:, :1])
        with self.assertRaises(ValueError):
            model.coefficient_response(np.full((80, 440), np.inf), np.zeros((16, 440)), self.basis)


class CubicKernelReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Cubic_Kernel_Coefficient_Refinement.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_distinct_exact_rounded_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["cubic_matrix_shape"], [1920, 2156])
        for flag in ("exact_free_pivot_representation_authoritative", "all_bounds_and_samples_use_rounded_representative",
                "kernel_readout_checked_against_actual_frozen_origin",
                "exact_origin_identity_and_rounded_neighborhood_are_not_a_single_certified_solution",
                "coordinate_constraints_not_released", "quartic_system_refreshed_after_cubic_change",
                "no_exact_low_order_closure_regional_solution_or_native_identification", "parent_polynomials_reports_and_main_TeX_PDF_unchanged"):
            self.assertTrue(self.report[flag])

    def test_exact_origin_update_and_negative_rounded_controls(self):
        controls = self.report["origin_controls"]
        self.assertTrue(controls["exact_parametric_C3_increment_zero"])
        self.assertTrue(controls["exact_parametric_total_C3_update_zero"])
        self.assertEqual(controls["exact_C3_rows_checked"], 320)
        self.assertEqual(controls["origin_lower_field_change"], 0.)
        self.assertEqual(controls["origin_higher_through_used_orders_change"], 0.)
        self.assertGreater(controls["raw_rounded_before_1114_norm"], 1e-8)
        self.assertGreater(controls["raw_rounded_after_1114_norm"], 1e-8)
        self.assertTrue(controls["not_a_new_high_precision_nonlinear_origin_solve"])
        readout, _, _, blocks = model.stable.reconstruct_certificate(self.report["updated_exact_kernel_certificate"])
        self.assertTrue(all(v == 0 for row in model.stable.contract_readouts(readout, blocks) for v in row))

    def test_updated_orders_and_refreshed_enclosures(self):
        for report in self.report["reports"]:
            self.assertLess(report["after_cubic_norm"], report["before_cubic_norm"])
            self.assertLess(report["after_quartic_norm"], report["before_quartic_norm"])
            self.assertEqual(report["lower_than_cubic_coefficient_change"], 0.)
            self.assertLess(report["cubic_prediction_error"], max(1e-15, report["before_cubic_norm"]*1e-3))
            self.assertLess(report["quartic_prediction_error"], 1e-13)
            self.assertGreater(report["refreshed_combined_enclosure"]["tail_bound"], 0.)
            for witness in report["sample_controls_not_a_regional_proof"]:
                self.assertLess(witness["Taylor_tail_discrepancy"], report["refreshed_combined_enclosure"]["tail_bound"])
        self.assertLess(self.report["cubic_coordinate_increment_norm"], 1e-12)
        self.assertLess(self.report["quartic_coordinate_increment_norm"], 1e-12)

    def test_shared_polynomial_reproduces_original_equation_witness(self):
        case = model.control.load_case()
        candidate = (*case[:4], np.asarray(self.report["candidate_ordinary_coefficients"]),
            np.asarray(self.report["candidate_rounded_spinor_coefficients"]), np.asarray(self.report["candidate_quartic_coefficients"]))
        saved = self.report["reports"][0]["sample_controls_not_a_regional_proof"][0]
        fields, _ = model.control.fields_and_higher(candidate, model.common.RADIUS*np.asarray(saved["direction"]))
        norm = np.linalg.norm(model.common.lower.lower_residual(case[0], fields))
        self.assertAlmostEqual(norm, saved["after_norm"], delta=1e-12)


if __name__ == "__main__":
    unittest.main()
