"""Exact trace-map constants, centered operators and off-shell coframe checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("trace_coframe_test", ROOT / "analysis/HC_Cartan_Trace_Reversed_Coframe_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CoframeLinearMapTests(unittest.TestCase):
    def test_trace_map_constants_are_exact_without_matrix_symmetry(self):
        basis = [sp.eye(16)[:, i].reshape(4, 4) for i in range(16)]
        gravity = sp.Matrix.hstack(*[(sp.trace(a)*sp.eye(4)/2-a).reshape(16, 1) for a in basis])
        matter = sp.Matrix.hstack(*[(a-sp.trace(a)*sp.eye(4)).reshape(16, 1) for a in basis])
        self.assertEqual(gravity.T*gravity, sp.eye(16))
        self.assertEqual((matter.T*matter).eigenvals(), {sp.Integer(1): 15, sp.Integer(9): 1})

    def test_identity_center_ricci_pullback_has_exact_norm_two(self):
        basis = np.eye(256).reshape(256, 4, 4, 4, 4)
        operator = np.einsum("ma,kb,tmkcb->tac", np.eye(4), np.eye(4), basis).reshape(256, 16).T
        exact = sp.Matrix(operator.astype(int))
        self.assertEqual(exact*exact.T, 4*sp.eye(16))

    def test_trace_map_preserves_complex_nonsymmetric_norm_and_tail(self):
        rng = np.random.default_rng(161119)
        matrix = rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4))
        value = model.T(model.core.tensor(matrix).coefficients, .7)
        gravity = model.trace_map(value, .5, -1.)
        self.assertAlmostEqual(np.linalg.norm(gravity.center), np.linalg.norm(matrix))
        self.assertEqual(gravity.tail, .7)
        self.assertAlmostEqual(model.trace_map(value, -1., 1.).tail, 2.1)
        with self.assertRaises(ValueError):
            model.trace_map(model.core.tensor(np.eye(3)), .5, -1.)

    def test_constant_identity_multiplication_does_not_double_tail(self):
        value = model.T(model.core.tensor(np.eye(4)*2).coefficients, .2)
        result = model.matrix_product(value, model.core.tensor(np.eye(4)))
        self.assertEqual(result.tail, .2)
        self.assertEqual(model.c("ij,jk->ik", value, np.eye(4)).tail, .4)

    def test_nonconstant_matrix_product_encloses_discarded_and_uncertain_terms(self):
        rng = np.random.default_rng(161120)
        a = model.core.tensor(np.eye(2))
        b = model.core.tensor(np.array([[1., .2], [.1, 2.]]))
        a.coefficients[model.core.INDEX[(3, 0, 0, 0)]] = rng.normal(size=(2, 2))*.03
        b.coefficients[model.core.INDEX[(0, 2, 0, 0)]] = rng.normal(size=(2, 2))*.02
        a.tail, b.tail = .01, .02
        result = model.matrix_product(a, b)
        for y in (np.ones(4), np.array([-.3, .4, .2, .1])):
            da, db = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
            da *= a.tail/np.linalg.norm(da)
            db *= b.tail/np.linalg.norm(db)
            actual = (a.evaluate(y)+da) @ (b.evaluate(y)+db)
            self.assertLess(np.linalg.norm(actual-result.evaluate(y)), result.tail)

    def test_centered_ricci_pullback_reduces_linear_tail(self):
        curvature = model.T(model.core.tensor(np.zeros((4, 4, 4, 4))).coefficients, .3)
        result, norm = model.ricci_pullback(model.core.tensor(np.eye(4)), curvature)
        self.assertEqual(norm, 2.)
        self.assertEqual(result.tail, .6)
        self.assertEqual(model.c("ma,kb,mkcb->ac", np.eye(4), np.eye(4), curvature).tail, 1.2)


class CoframeOffShellTests(unittest.TestCase):
    def test_factorization_matches_independent_parent_for_nonsymmetric_ricci(self):
        rng = np.random.default_rng(161121)
        e = np.eye(4)+rng.normal(size=(4, 4))*.08
        inverse, volume = np.linalg.inv(e), abs(np.linalg.det(e))
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        dp = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        omega = rng.normal(size=(4, 4, 4))
        omega = (omega-omega.swapaxes(1, 2))/2
        curvature = rng.normal(size=(4, 4, 4, 4))
        curvature = (curvature-curvature.swapaxes(0, 1))/2
        curvature = (curvature-curvature.swapaxes(2, 3))/2
        multiplier = rng.normal(size=(4, 4))
        cartan = model.general.cartan
        covariant = cartan.covariant_jet(psi, dp, omega)
        imag = cartan.odd.readouts.pairing(psi, covariant).imag
        mass = np.vdot(psi, model.general.prolong.MASS @ psi @ cartan.BETA.T).real
        expected = cartan.coframe_euler(e, psi, dp, omega, curvature, model.general.prolong.MASS, multiplier)
        result, _ = model.factorized_euler(*(model.core.tensor(v) for v in
            (inverse, np.asarray(volume), imag, np.asarray(mass), curvature, multiplier)))
        ricci, _ = model.ricci_pullback(model.core.tensor(inverse), model.core.tensor(curvature))
        self.assertGreater(np.linalg.norm(ricci.center-ricci.center.T), 1.)
        self.assertGreater(np.linalg.norm(expected), 1.)
        self.assertEqual(result.tail, 0.)
        np.testing.assert_allclose(result.center, expected, atol=2e-13, rtol=2e-14)

    def test_actual_perturbed_field_keeps_nonzero_coframe_equation(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, np.zeros(4))
        fields["multiplier"] = fields["multiplier"]+np.eye(4)*.02
        expected = model.general.equations(case[0], fields)["gravity"]
        self.assertGreater(np.linalg.norm(expected), .01)
        np.testing.assert_allclose(model.compact_at_point(case[0], fields), expected, atol=2e-12, rtol=0)


class CoframeTraceReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Trace_Reversed_Coframe_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("ricci_symmetry_not_assumed", "no_coefficients_fitted_or_zeroed",
                     "not_outward_rounded_or_interval_certified", "not_exact_low_order_closure_or_regional_solution"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_64_rows_are_unchanged(self):
        indices = list(range(40))+list(range(56, 80))
        for report, original in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, indices], np.asarray(original["coefficients"])[:, indices])
            self.assertLess(report["coefficient_identity_error"], 1e-12)

    def test_estimate_improves_without_discarding_low_order_defects(self):
        for report in self.report["reports"]:
            self.assertGreater(report["previous_coframe_tail"]/report["coframe"]["tail_bound"], 6.)
            self.assertGreater(report["previous_combined_upper_estimate"]/report["combined"]["whole_cube_upper_estimate"], 2.)
            self.assertGreater(report["coframe"]["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["coframe"]["coefficient_level_bounds"][4], 1e-12)
            self.assertEqual(report["tail_diagnostics"]["ricci_frame_tail"], report["tail_diagnostics"]["trace_reversed_gravity_tail"])
            self.assertEqual(report["tail_diagnostics"]["centered_ricci_pullback_operator_norm"], 2.)
            self.assertEqual(report["tail_diagnostics"]["centered_right_inverse_operator_norm"], 1.)

    def test_two_radii_and_independent_point_controls(self):
        a, b = self.report["reports"]
        self.assertLess(a["combined"]["whole_cube_upper_estimate"], .94)
        self.assertGreater(a["combined"]["whole_cube_upper_estimate"], .9)
        self.assertLess(b["combined"]["whole_cube_upper_estimate"], .03)
        self.assertGreater(a["coframe"]["tail_bound"]/b["coframe"]["tail_bound"], 31.)
        self.assertLess(a["coframe"]["tail_bound"]/b["coframe"]["tail_bound"], 34.)
        for report in (a, b):
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["point_identity_error"], 1e-12)
                self.assertLess(check["coframe_tail_discrepancy"], report["coframe"]["tail_bound"])
                self.assertGreater(report["coframe"]["tail_bound"], 1e5*check["actual_coframe_norm"])


if __name__ == "__main__":
    unittest.main()
