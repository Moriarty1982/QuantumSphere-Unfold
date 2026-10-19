"""Source cancellation with independent off-shell and multiplier controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("source_cancel_test", ROOT / "analysis/HC_Cartan_Frame_Source_Cancellation_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class SourceCancellationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.control.load_case()
        cls.forms = cls.case[0]["component_forms"]
        cls.inverse, _ = model.prior.factorization_certificate(cls.case[0]["curvature_hessian"])

    def inputs(self, zero_multiplier=False):
        rng = np.random.default_rng(191910)
        t, j = model.core.tensor, model.J
        e = j(np.eye(4)+rng.normal(size=(4, 4))*.03,
            [t(rng.normal(size=(4, 4))*.02) for _ in range(4)])
        psi = j(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)),
            [t(rng.normal(size=(3, 4))*.02+1j*rng.normal(size=(3, 4))*.02) for _ in range(4)])
        lam = j(np.zeros((4, 4)) if zero_multiplier else rng.normal(size=(4, 4))*.03,
            [t(rng.normal(size=(4, 4))*.01) for _ in range(4)])
        volume = j(np.asarray(1.3), [t(np.asarray(v)) for v in rng.normal(size=4)*.02])
        return e, volume, psi, lam

    def original_solve(self, e, volume, psi, lam):
        inverse, _ = model.core.matrix_inverse(e.value)
        inv = model.J(inverse, [-model.c("ma,ab,bn->mn", inverse, d, inverse) for d in e.derivatives])
        components = model.jc("ui,pamij,uj->pam", psi.conjugate(), self.forms, psi).real()
        source = model.jc(",ma,pam->p", volume, inv, components)
        response = model.jc("ui,pamij,uj->amp", psi.conjugate(), self.forms,
            model.jc("uv,vj->uj", model.general.prolong.Q, psi)).real().scale(-1)
        rhs = -source+model.jc("amp,am->p", response, lam)
        return model.prior.frame_solve(e, volume, rhs, self.inverse, {})[0]

    def test_exact_support_and_corrupt_inputs(self):
        flat, certificate = model.source_support_certificate(self.forms)
        self.assertEqual(flat.shape, (6, 4, 4, 4))
        self.assertEqual(certificate["coordinate_blocks_checked"], 16)
        corrupt = self.forms.copy()
        corrupt[7, 1, 0, 0, 0] += .125j
        for forms in (corrupt, self.forms[:1], self.forms*np.nan):
            with self.assertRaises(ValueError):
                model.source_support_certificate(forms)

    def test_arbitrary_off_shell_sources_and_four_derivatives(self):
        values = self.inputs()
        result, _ = model.source_solve(*values, self.forms, self.inverse, {})
        original = self.original_solve(*values)
        for a, b in zip((result.value, *result.derivatives), (original.value, *original.derivatives)):
            np.testing.assert_allclose(a.center, b.center, atol=2e-13, rtol=2e-13)
            self.assertEqual(a.tail, 0.)

    def test_independent_rational_source_transport_identity(self):
        e = sp.eye(4)
        e[0, 1], e[2, 3], e[3, 0] = sp.Rational(1, 3), sp.Rational(-1, 5), sp.Rational(2, 7)
        inverse, volume = e.inv(), sp.Rational(7, 3)
        spinor = sp.Matrix(6, 4, lambda l, a: sp.Rational(l-2*a, 7))
        weighted = sp.Matrix(6, 4, lambda l, a: sp.Rational(2*l+a-3, 11))
        lam = sp.Matrix(4, 4, lambda a, m: sp.Rational(a+2*m-4, 13))
        source = -volume*inverse*spinor.T-lam.T*weighted.T
        transported = -volume*spinor.T-(lam*e.T).T*weighted.T
        self.assertEqual(e*source, transported)
        h0inv = sp.Matrix([[sp.Rational(float(v)) for v in row] for row in self.inverse])
        flatten = lambda matrix: sp.Matrix(list(matrix))
        original = sp.kronecker_product(e.T, sp.eye(6))*h0inv*sp.kronecker_product(e, sp.eye(6))*flatten(source)/volume
        reduced = -sp.kronecker_product(e.T, sp.eye(6))*h0inv*flatten(
            spinor.T+(lam*e.T).T*weighted.T/volume)
        self.assertEqual(original, reduced)

    def test_zero_multiplier_jet_cancels_volume_but_not_domain_guard(self):
        e, volume, psi, _ = self.inputs()
        zero = model.J(np.zeros((4, 4)))
        a, _ = model.source_solve(e, volume, psi, zero, self.forms, self.inverse, {})
        b, _ = model.source_solve(e, model.J(np.asarray(2.7), [model.core.tensor(np.asarray(.1))]*4),
            psi, zero, self.forms, self.inverse, {})
        for x, y in zip((a.value, *a.derivatives), (b.value, *b.derivatives)):
            np.testing.assert_array_equal(x.coefficients, y.coefficients)
        with self.assertRaises(ValueError):
            model.source_solve(e, model.J(np.asarray(0.)), psi, zero, self.forms, self.inverse, {})

    def test_zero_multiplier_center_does_not_erase_its_gradient(self):
        e, volume, psi, lam = self.inputs(zero_multiplier=True)
        a, _ = model.source_solve(e, volume, psi, lam, self.forms, self.inverse, {})
        b, _ = model.source_solve(e, volume, psi, model.J(np.zeros((4, 4))), self.forms, self.inverse, {})
        np.testing.assert_array_equal(a.value.coefficients, b.value.coefficients)
        self.assertGreater(np.linalg.norm(a.derivatives[0].center-b.derivatives[0].center), 1e-4)
        expected = self.original_solve(e, volume, psi, lam)
        for x, y in zip(a.derivatives, expected.derivatives):
            np.testing.assert_allclose(x.center, y.center, atol=2e-13)

    def test_uncertain_fields_and_derivative_tails_retained(self):
        values = self.inputs()
        uncertain = [model.J(model.T(v.value.coefficients, 1e-5),
            [model.T(d.coefficients, 1e-6) for d in v.derivatives]) for v in values]
        result, _ = model.source_solve(*uncertain, self.forms, self.inverse, {})
        rng = np.random.default_rng(191911)
        def perturb(v):
            error = rng.normal(size=v.center.shape)
            return v.center+error*(v.tail/np.linalg.norm(error))
        for _ in range(3):
            points = [model.J(perturb(v.value), [model.core.tensor(perturb(d)) for d in v.derivatives])
                for v in uncertain]
            original = self.original_solve(*points)
            for a, b in zip((result.value, *result.derivatives), (original.value, *original.derivatives)):
                self.assertGreater(a.tail, 0.)
                self.assertLess(np.linalg.norm(a.center-b.center), a.tail)

    def test_independent_original_connection(self):
        fields, _ = model.control.fields_and_higher(self.case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        omega, _, _, _ = model.connection_models(self.case[0], model.full.point_models(fields), self.inverse, {})
        original = model.general.connection_jets(self.case[0], fields)
        np.testing.assert_allclose(omega.value.center, original["omega"], atol=2e-12, rtol=1e-13)
        for actual, expected in zip(omega.derivatives, original["first"]):
            np.testing.assert_allclose(actual.center, expected, atol=2e-12, rtol=1e-13)


class SourceReportTests(unittest.TestCase):
    def test_report_fingerprints_coefficients_bounds_and_scope(self):
        report = json.loads((ROOT / "analysis/HC_Cartan_Frame_Source_Cancellation_Bound.json").read_text(encoding="utf-8"))
        self.assertEqual(report["input_sha256"], model.input_fingerprints())
        self.assertFalse(report["main_TeX_PDF_changed"])
        for flag in ("spinor_source_volume_and_inverse_cancelled_algebraically",
                "multiplier_channel_and_all_its_derivatives_retained", "all_frame_spinor_volume_derivatives_and_tails_retained",
                "no_coefficients_fitted_or_low_order_defects_zeroed", "not_a_full_outward_rounded_certificate",
                "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(report[flag])
        for current, previous in zip(report["reports"], model.load_parent()["reports"]):
            self.assertLess(current["coefficient_identity_error"], 1e-12)
            for block in ("constraint", "probe", "coframe", "curl", "combined"):
                self.assertLess(current[block]["tail_bound"], previous[block]["tail_bound"])
            for degree in (3, 4):
                self.assertGreater(current["combined"]["coefficient_level_bounds"][degree], 1e-12)
            diagnostics = current["connection_diagnostics"]
            for check in current["sample_checks_not_the_proof"]:
                self.assertLess(check["combined_tail_discrepancy"], current["combined"]["tail_bound"])
                self.assertLess(check["connection_value_discrepancy"], diagnostics["new_value_tail"])
                for error, tail in zip(check["connection_derivative_discrepancies"], diagnostics["new_derivative_tails"]):
                    self.assertLess(error, tail)


if __name__ == "__main__":
    unittest.main()
