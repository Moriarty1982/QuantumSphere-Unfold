"""Exact polynomial frame identity and curved-solve derivative controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("frame_solve_test", ROOT / "analysis/HC_Cartan_Frame_Factorized_Solve_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def direct_solve(tensor, e, volume, rhs, de, dv, df):
    inverse = np.linalg.inv(e)
    h = .5*volume*np.einsum("ma,nb,pqmnab->pq", inverse, inverse, tensor)
    k = np.linalg.solve(h, rhs)
    derivatives = []
    for r in range(4):
        da = -inverse @ de[r] @ inverse
        dh = (dv[r]/volume*h+.5*volume*(np.einsum("ma,nb,pqmnab->pq", da, inverse, tensor)
            +np.einsum("ma,nb,pqmnab->pq", inverse, da, tensor)))
        derivatives.append(np.linalg.solve(h, df[r]-dh @ k))
    return k, derivatives


class FrameSolveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.control.load_case()
        cls.tensor = cls.case[0]["curvature_hessian"]
        cls.inverse, cls.certificate = model.factorization_certificate(cls.tensor)

    def test_all_quadratic_coefficients_and_flat_inverse_are_exact(self):
        self.assertEqual(self.certificate["diagonal_coefficient_checks"], 16)
        self.assertEqual(self.certificate["mixed_coefficient_checks"], 120)
        self.assertLess(self.certificate["integer_intermediate_bound"], 2**63)
        flat = sp.Matrix(self.certificate["twice_flat_hessian"])/2
        inverse = sp.Matrix([[sp.Rational(v) for v in row] for row in self.certificate["exact_flat_inverse"]])
        self.assertEqual(flat*inverse, sp.eye(24))
        self.assertEqual(sp.Matrix([[sp.Rational(float(v)) for v in row] for row in self.inverse]), inverse)

    def test_independent_rational_nonidentity_frame_and_inverse(self):
        numerator = np.eye(4, dtype=np.int64)*3
        numerator[0, 1], numerator[2, 3] = 1, -1
        a = sp.Matrix(numerator.tolist())/3
        direct = sp.Matrix(np.einsum("ma,nb,pqmnab->pq", numerator, numerator, self.tensor.astype(np.int64)).tolist())/18
        flat = sp.Matrix(self.certificate["twice_flat_hessian"])/2
        b = sp.kronecker_product(a.T, sp.eye(6))
        self.assertEqual(direct, b.T*flat*b)
        e, volume = a.inv(), sp.Rational(3, 2)
        flat_inverse = sp.Matrix([[sp.Rational(v) for v in row] for row in self.certificate["exact_flat_inverse"]])
        curved_inverse = sp.kronecker_product(e.T, sp.eye(6))*flat_inverse*sp.kronecker_product(e, sp.eye(6))/volume
        self.assertEqual(volume*direct*curved_inverse, sp.eye(24))

    def test_corrupt_nonintegral_singular_and_overflow_coefficients_rejected(self):
        corrupt = self.tensor.copy()
        corrupt[0, 0, 1, 1, 0, 0] += 1
        for value in (corrupt, self.tensor*.5, np.zeros_like(self.tensor), self.tensor*1e15):
            with self.assertRaises(ValueError):
                model.factorization_certificate(value)

    def test_lift_and_volume_reciprocal_keep_errors_and_domain_guards(self):
        e = model.T(model.core.tensor(np.eye(4)).coefficients, .01)
        lifted = model.lift(e)
        np.testing.assert_array_equal(lifted.center, np.eye(24))
        self.assertEqual(lifted.tail, model.LIFT_NORM_UPPER*.01)
        for value in (0., -1., 1.+.01j):
            with self.assertRaises(ValueError):
                model.reciprocal_volume(model.J(np.asarray(value)))
        with self.assertRaises(ValueError):
            model.reciprocal_volume(model.J(model.T(model.core.tensor(np.asarray(1.)).coefficients, 1.)))

    def test_off_shell_curved_solve_and_all_derivatives(self):
        rng = np.random.default_rng(191901)
        e = np.eye(4)+rng.normal(size=(4, 4))*.05
        de = rng.normal(size=(4, 4, 4))*.03
        volume, dv = np.asarray(1.3), rng.normal(size=4)*.02
        rhs, df = rng.normal(size=24), rng.normal(size=(4, 24))
        result, _ = model.frame_solve(model.J(e, [model.core.tensor(v) for v in de]),
            model.J(volume, [model.core.tensor(np.asarray(v)) for v in dv]),
            model.J(rhs, [model.core.tensor(v) for v in df]), self.inverse, {})
        expected, derivatives = direct_solve(self.tensor, e, volume, rhs, de, dv, df)
        np.testing.assert_allclose(result.value.center, expected, atol=1e-13)
        self.assertEqual(result.value.tail, 0.)
        for actual, wanted in zip(result.derivatives, derivatives):
            np.testing.assert_allclose(actual.center, wanted, atol=1e-13)
            self.assertEqual(actual.tail, 0.)

    def test_uncertain_frame_volume_source_and_derivatives_enclosed(self):
        rng = np.random.default_rng(191902)
        def uncertain(array, tail):
            return model.T(model.core.tensor(array).coefficients, tail)
        e = model.J(uncertain(np.eye(4), .001), [uncertain(rng.normal(size=(4, 4))*.01, .0001) for _ in range(4)])
        volume = model.J(uncertain(np.asarray(1.2), .001), [uncertain(np.asarray(.01), .0001) for _ in range(4)])
        rhs = model.J(uncertain(rng.normal(size=24), .002), [uncertain(rng.normal(size=24)*.02, .0001) for _ in range(4)])
        result, _ = model.frame_solve(e, volume, rhs, self.inverse, {})
        def perturb(value):
            error = rng.normal(size=value.center.shape)
            return value.center+error*value.tail/np.linalg.norm(error)
        for _ in range(3):
            actual_e, actual_v, actual_f = (perturb(v.value) for v in (e, volume, rhs))
            de, dv, df = ([perturb(d) for d in v.derivatives] for v in (e, volume, rhs))
            wanted, derivatives = direct_solve(self.tensor, actual_e, actual_v, actual_f, de, dv, df)
            self.assertLess(np.linalg.norm(wanted-result.value.center), result.value.tail)
            for actual, expected in zip(result.derivatives, derivatives):
                self.assertLess(np.linalg.norm(expected-actual.center), actual.tail)

    def test_independent_original_connection_on_nonzero_background(self):
        fields, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        omega, _, _, _ = model.connection_models(self.case[0], model.full.point_models(fields), self.inverse, {})
        original = model.general.connection_jets(self.case[0], fields)
        np.testing.assert_allclose(omega.value.center, original["omega"], atol=2e-12, rtol=1e-13)
        for actual, expected in zip(omega.derivatives, original["first"]):
            np.testing.assert_allclose(actual.center, expected, atol=2e-12, rtol=1e-13)
            self.assertEqual(actual.tail, 0.)


class FrameSolveReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Frame_Factorized_Solve_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_scope_and_retained_low_order_defects(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("all_quadratic_coefficients_checked_not_sampled", "flat_inverse_exactly_verified", "curved_hessian_not_frozen",
                     "all_frame_volume_rhs_derivatives_and_tails_retained", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "not_a_full_outward_rounded_certificate", "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        for report in self.report["reports"]:
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            for degree in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][degree], 1e-12)

    def test_recomputed_bounds_improve_and_original_equation_controls_pass(self):
        for report, old in zip(self.report["reports"], self.parent["reports"]):
            for key in ("constraint", "probe", "coframe", "curl", "combined"):
                self.assertLess(report[key]["tail_bound"], old[key]["tail_bound"])
            pieces = report["connection_diagnostics"]
            for a, b in zip(pieces["new_derivative_tails"], pieces["old_derivative_tails"]):
                self.assertLess(a, b)
                self.assertGreater(a, 0.)
            self.assertGreater(report["volume_reciprocal_neumann_ratio"], 0.)
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["connection_value_discrepancy"], pieces["new_value_tail"])
                for error, tail in zip(check["connection_derivative_discrepancies"], pieces["new_derivative_tails"]):
                    self.assertLess(error, tail)
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])


if __name__ == "__main__":
    unittest.main()
