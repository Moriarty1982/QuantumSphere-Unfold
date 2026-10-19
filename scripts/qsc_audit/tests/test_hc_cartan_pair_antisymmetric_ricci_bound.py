"""Exact restricted Ricci norm, retained inverse terms and off-shell controls."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("pair_ricci_test", ROOT / "analysis/HC_Cartan_Pair_Antisymmetric_Ricci_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class RestrictedRicciTests(unittest.TestCase):
    def test_projection_is_exact_orthogonal_rank_36(self):
        basis = model.pair_projection(np.eye(256).reshape(256, 4, 4, 4, 4))
        p = sp.SparseMatrix(basis.reshape(256, 256).T)*4
        p = p.applyfunc(lambda x: sp.Rational(int(x), 4))
        self.assertEqual(p.T, p)
        self.assertEqual(p*p, p)
        self.assertEqual(sp.trace(p), 36)

    def test_exact_gram_spectrum_and_saturation(self):
        operator = model.centered_operator(np.eye(4))
        exact = sp.Matrix((operator*4).astype(int))/4
        identity = sp.eye(4).reshape(16, 1)
        self.assertEqual(exact*exact.T, sp.eye(16)/2+identity*identity.T/4)
        self.assertEqual((exact*exact.T).eigenvals(), {sp.Rational(3, 2): 1, sp.Rational(1, 2): 15})
        vector = exact.T*identity
        self.assertEqual((exact*vector).dot(exact*vector)/vector.dot(vector), sp.Rational(3, 2))
        self.assertGreaterEqual(Fraction.from_float(model.IDENTITY_CENTER_NORM_UPPER)**2, Fraction(3, 2))

    def test_antisymmetry_is_required_not_assumed_for_arbitrary_inputs(self):
        curvature = model.core.tensor(np.zeros((4, 4, 4, 4)))
        with self.assertRaises(ValueError):
            model.ricci_pullback(model.core.tensor(np.eye(4)), curvature, actual_pair_antisymmetry=False)
        with self.assertRaises(ValueError):
            model.pair_projection(np.zeros((4, 4)))

    def test_projected_polynomial_uses_existing_error_not_zero_error(self):
        polynomial = np.ones((4, 4, 4, 4))
        curvature = model.T(model.core.tensor(polynomial).coefficients, np.linalg.norm(polynomial))
        result, diagnostics = model.ricci_pullback(model.core.tensor(np.eye(4)), curvature, actual_pair_antisymmetry=True)
        np.testing.assert_array_equal(result.coefficients, 0.)
        self.assertGreater(diagnostics["curvature_coefficient_projection_error"], 1.)
        self.assertGreater(result.tail, curvature.tail)

    def test_variable_inverse_cross_terms_and_uncertain_curvature_are_enclosed(self):
        rng = np.random.default_rng(191005)
        inverse = model.core.tensor(np.eye(4))
        inverse.coefficients[model.core.INDEX[(2, 0, 0, 0)]] = rng.normal(size=(4, 4))*.03
        inverse.tail = .002
        curvature = model.core.tensor(model.pair_projection(rng.normal(size=(4, 4, 4, 4))))
        curvature.coefficients[model.core.INDEX[(0, 3, 0, 0)]] = model.pair_projection(rng.normal(size=(4, 4, 4, 4)))*.04
        curvature.tail = .007
        result, _ = model.ricci_pullback(inverse, curvature, actual_pair_antisymmetry=True)
        for y in (np.ones(4), np.array([-.7, .4, -.3, .2])):
            da = rng.normal(size=(4, 4))
            dr = model.pair_projection(rng.normal(size=(4, 4, 4, 4)))
            a = inverse.evaluate(y)+da*inverse.tail/np.linalg.norm(da)
            r = curvature.evaluate(y)+dr*curvature.tail/np.linalg.norm(dr)
            actual = np.einsum("ma,kb,mkcb->ac", a, a, r)
            self.assertLess(np.linalg.norm(actual-result.evaluate(y)), result.tail)
        self.assertGreater(np.linalg.norm(result.coefficients[model.core.INDEX[(2, 0, 0, 0)]]), .01)
        self.assertGreater(np.linalg.norm(result.coefficients[model.core.INDEX[(4, 0, 0, 0)]]), .0001)

    def test_off_shell_coframe_without_ricci_symmetry_and_nonidentity_fallback(self):
        rng = np.random.default_rng(191006)
        for e in (np.eye(4), np.eye(4)+rng.normal(size=(4, 4))*.08):
            psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
            dp = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
            omega = rng.normal(size=(4, 4, 4))
            omega = (omega-omega.swapaxes(1, 2))/2
            curvature = model.pair_projection(rng.normal(size=(4, 4, 4, 4)))
            multiplier = rng.normal(size=(4, 4))
            cartan = model.general.cartan
            covariant = cartan.covariant_jet(psi, dp, omega)
            imag = cartan.odd.readouts.pairing(psi, covariant).imag
            mass = np.vdot(psi, model.general.prolong.MASS @ psi @ cartan.BETA.T).real
            expected = cartan.coframe_euler(e, psi, dp, omega, curvature, model.general.prolong.MASS, multiplier)
            inputs = [model.core.tensor(v) for v in (np.linalg.inv(e), np.asarray(abs(np.linalg.det(e))),
                imag, np.asarray(mass), curvature, multiplier)]
            actual, pieces = model.factorized_euler(*inputs)
            ricci, _ = model.ricci_pullback(inputs[0], inputs[4], actual_pair_antisymmetry=True)
            self.assertGreater(np.linalg.norm(ricci.center-ricci.center.T), .1)
            self.assertEqual(pieces["exact_identity_center_constant_used"], np.array_equal(e, np.eye(4)))
            np.testing.assert_allclose(actual.center, expected, atol=3e-13, rtol=2e-14)
            self.assertEqual(actual.tail, 0.)


class PairRicciReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Pair_Antisymmetric_Ricci_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_exact_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("actual_curvature_pair_antisymmetry_required", "ricci_symmetry_pair_exchange_and_bianchi_not_assumed",
                     "all_variable_inverse_cross_terms_retained", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "only_identity_center_operator_constant_is_exactly_certified", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_64_rows_and_nonzero_low_order_defects_retained(self):
        indices = list(range(40))+list(range(56, 80))
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, indices], np.asarray(parent["coefficients"])[:, indices])
            self.assertEqual(report["curl"], parent["curl"])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][3], 1e-12)
            self.assertGreater(report["combined"]["coefficient_level_bounds"][4], 1e-12)

    def test_recomputed_bounds_improve_but_are_not_sampled_error_or_existence(self):
        for report in self.report["reports"]:
            pieces = report["tail_diagnostics"]
            self.assertTrue(pieces["exact_identity_center_constant_used"])
            self.assertLess(pieces["ricci_frame_tail"], report["previous_ricci_frame_tail"])
            self.assertLess(report["coframe"]["tail_bound"], report["previous_coframe_tail"])
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e4*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
