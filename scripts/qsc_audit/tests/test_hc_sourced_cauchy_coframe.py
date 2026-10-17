"""Exact sourced Cauchy jets, rank recovery, flatness and same-frame obstruction."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "sourced_cauchy_coframe", ROOT / "analysis/HC_Sourced_Cauchy_Coframe.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCSourcedCauchyCoframeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.series()
        cls.jet = model.initial_jet()
        cls.residuals = model.residual_coefficients(cls.data)
        cls.control = model.induced_control()

    def assertZero(self, value):
        if not isinstance(value, sp.MatrixBase):
            value = sp.Matrix([value])
        self.assertTrue(all(sp.expand(v) == 0 for v in value), str(value))

    def at(self, value, point=(0, 0, 0)):
        return np.array(value.subs(dict(zip(model.X, point))), complex)

    def test_clifford_weights_are_the_prepared_exact_representation(self):
        for a, b in zip(model.WEIGHTS, model.dirac.WEIGHTS):
            np.testing.assert_array_equal(np.array(a, complex), b)
        for i in range(1, 4):
            self.assertZero(model.WEIGHTS[i] @ model.BETA+model.BETA @ model.WEIGHTS[i])

    def test_mass_is_hermitian_and_commutes_with_common_gauge_generator(self):
        self.assertZero(model.MASS-model.MASS.conjugate().T)
        self.assertZero(model.MASS @ sp.eye(3)-sp.eye(3) @ model.MASS)
        np.testing.assert_allclose(np.array(model.MASS, float), model.dirac.parent.background.triadic_mass())

    def test_source_coupling_keeps_full_trace_factor_three(self):
        self.assertEqual(model.COUPLING, sp.Rational(4, 5)**2/3)

    def test_initial_current_is_the_actual_probe_contraction(self):
        x, y, z = model.X
        self.assertZero(self.jet["current"]-sp.Matrix([1+model.R2/4, -x, -y, z]))

    def test_timelike_current_margin_is_positive_inside_ball(self):
        j = self.jet["current"]
        self.assertZero(j[0]**2-sum(v*v for v in j[1:])-(1-model.R2/4)**2)
        for point in ((0, 0, 0), (1, 1, 1), (-1.9, 0, 0)):
            value = self.at(j, point).real.ravel()
            self.assertGreater(value[0], np.linalg.norm(value[1:]))

    def test_initial_gauss_constraint_holds_exactly_as_spatial_polynomial(self):
        self.assertZero(self.residuals["gauss"][0])

    def test_initial_electric_field_is_not_erased_by_zero_initial_potential(self):
        _, a, electric = model.initial_data()
        self.assertZero(a)
        self.assertGreater(np.linalg.norm(self.at(electric, (1, 0, 0))), 0.08)

    def test_initial_magnetic_field_and_electric_curl_vanish(self):
        _, a, electric = model.initial_data()
        for i in range(3):
            for j in range(3):
                self.assertZero(a[j].diff(model.X[i])-a[i].diff(model.X[j]))
                self.assertZero(electric[j].diff(model.X[i])-electric[i].diff(model.X[j]))

    def test_dirac_time_jet_is_fixed_by_reference_equation(self):
        for point in ((0, 0, 0), (sp.Rational(1, 4), -sp.Rational(1, 3), sp.Rational(1, 5))):
            psi = self.at(self.jet["psi"], point)
            derivative = np.array([self.at(d, point) for d in self.jet["derivative"]])
            residual = model.dirac.dirac_data(psi, derivative, np.array(model.MASS, complex))["residual"]
            self.assertLess(np.linalg.norm(residual), 2e-15)

    def test_all_dirac_evolution_coefficients_through_t_squared_vanish(self):
        for coefficient in self.residuals["dirac"]:
            self.assertZero(coefficient)
        self.assertEqual(len(self.residuals["dirac"]), 3)

    def test_all_potential_evolution_coefficients_through_t_squared_vanish(self):
        for coefficient in self.residuals["potential"]:
            self.assertZero(coefficient)

    def test_all_maxwell_evolution_coefficients_through_t_squared_vanish(self):
        for coefficient in self.residuals["electric"]:
            self.assertZero(coefficient)

    def test_reference_current_continuity_through_t_squared(self):
        for coefficient in self.residuals["continuity"]:
            self.assertZero(coefficient)

    def test_gauss_constraint_propagates_through_cubic_order(self):
        self.assertEqual(len(self.residuals["gauss"]), 4)
        for coefficient in self.residuals["gauss"]:
            self.assertZero(coefficient)

    def test_corrupted_initial_charge_field_is_detected(self):
        corrupt = dict(model.series(0))
        corrupt["electric"] = (sp.ImmutableMatrix.zeros(3, 1),)
        residual = model.residual_coefficients(corrupt)["gauss"][0]
        self.assertZero(residual[0]+model.COUPLING*self.jet["current"][0])
        self.assertNotEqual(residual[0], 0)

    def test_third_probe_channel_is_populated_at_first_time_order(self):
        self.assertZero(self.data["psi"][1][2, :]+4*sp.I*self.jet["psi"][0, :] @ model.BETA.T)

    def test_second_probe_channel_is_populated_at_second_time_order(self):
        self.assertZero(self.data["psi"][2][1, :]+sp.Rational(7, 5)*self.jet["psi"][0, :])

    def test_gauge_backreaction_enters_probe_second_coefficient(self):
        neutral = model.series(2, sp.Integer(0))
        shift = self.data["psi"][2]-neutral["psi"][2]
        psi, _, electric = model.initial_data()
        expected = -sp.I*sum((electric[i]*psi @ model.WEIGHTS[i+1].T for i in range(3)), sp.zeros(3, 4))/2
        self.assertZero(shift-expected)
        self.assertTrue(any(v != 0 for v in shift))

    def test_electric_response_uses_same_spatial_current(self):
        self.assertZero(self.data["electric"][1]+model.COUPLING*self.jet["current"][1:, :])

    def test_coframe_agrees_with_half_full_current_gradient(self):
        current = self.data["current"]
        gradient = sp.Matrix.hstack(current[1], *(current[0].diff(q) for q in model.X))/2
        self.assertZero(self.jet["coframe"]-gradient)

    def test_coframe_determinant_has_analytic_rank_four_bound(self):
        self.assertZero(self.jet["coframe"].det()-(1-model.R2/4)/16)
        for point in ((0, 0, 0), (1, 1, 1), (1.9, 0, 0)):
            self.assertEqual(np.linalg.matrix_rank(self.at(self.jet["coframe"], point)), 4)

    def test_ball_boundary_has_a_real_rank_defect(self):
        self.assertEqual(np.linalg.matrix_rank(self.at(self.jet["coframe"], (2, 0, 0))), 3)

    def test_origin_coframe_is_oriented_and_time_oriented(self):
        expected = np.diag([0.5, -0.5, -0.5, 0.5])
        np.testing.assert_allclose(self.control["frame"], expected)
        self.assertGreater(np.linalg.det(self.control["frame"]), 0)
        self.assertGreater(self.control["frame"][0, 0], 0)

    def test_induced_metric_has_lorentz_signature_not_rank_one(self):
        eigenvalues = np.linalg.eigvalsh(self.control["bundle"]["metric"])
        np.testing.assert_allclose(eigenvalues, [-0.25, 0.25, 0.25, 0.25])

    def test_coframe_is_closed_through_its_checked_two_jet(self):
        first, second = self.control["first"], self.control["second"]
        for mu in range(4):
            for nu in range(4):
                np.testing.assert_allclose(first[mu, :, nu], first[nu, :, mu], atol=1e-13)
                for r in range(4):
                    np.testing.assert_allclose(second[r, mu, :, nu], second[r, nu, :, mu], atol=1e-13)

    def test_induced_spin_connection_of_holonomic_coframe_is_zero(self):
        self.assertLess(np.linalg.norm(self.control["bundle"]["spin"]), 1e-13)

    def test_induced_curvature_is_zero_with_all_time_and_spatial_second_jets(self):
        self.assertLess(np.linalg.norm(self.control["bundle"]["curvature"]["riemann"]), 2e-12)

    def test_zero_curvature_does_not_satisfy_einstein_with_nonzero_probe_stress(self):
        np.testing.assert_allclose(self.control["reference"]["stress"], np.diag([0.6, 0, 0, 0]), atol=1e-13)
        _, _, electric = model.initial_data()
        self.assertZero(electric.subs(dict.fromkeys(model.X, 0)))

    def test_same_induced_frame_dirac_residual_remains_nonzero(self):
        result = self.control["induced"]["residual"]
        expected = np.zeros((3, 4), complex)
        expected[:, 0] = 4j*np.array([1, 0, 0])+np.array(model.MASS[:, 0], float).ravel()
        np.testing.assert_allclose(result, expected, atol=1e-13)
        self.assertAlmostEqual(np.linalg.norm(result)**2, 32.36)

    def test_same_frame_trace_residual_is_exactly_four_not_zero(self):
        value = np.vdot(self.control["psi"], self.control["induced"]["residual"] @ model.dirac.BETA.T)
        self.assertAlmostEqual(value.imag, 4)

    def test_induced_coordinate_current_divergence_is_eight(self):
        e, de = self.control["frame"], self.control["first"]
        inverse = np.linalg.inv(e)
        current = self.at(self.jet["current"]).real.ravel()
        coordinate = inverse @ current
        divergence = 0
        for mu in range(4):
            di = -inverse @ de[mu] @ inverse
            divergence += di[mu] @ current+inverse[mu] @ (2*e[:, mu])
            divergence += np.trace(inverse @ de[mu])*coordinate[mu]
        self.assertAlmostEqual(divergence, 8)

    def test_common_local_phase_does_not_change_full_real_coframe(self):
        psi = self.jet["psi"]
        for k in model.WEIGHTS:
            self.assertZero(sp.re(model.inner(psi, sp.I*psi @ k.T)))

    def test_internal_antihermitian_connection_cannot_change_current_gradient_identity(self):
        psi = sum(self.data["psi"][:3], sp.zeros(3, 4))
        generators = (sp.I*sp.diag(1, -1, 2), sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]]),
                      sp.I*sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]))
        for generator in generators:
            for k in model.WEIGHTS:
                self.assertZero(sp.re(model.inner(psi, generator @ psi @ k.T)))

    def test_second_order_normal_form_has_correct_dirac_residual_propagation(self):
        psi = sum((p*model.T**n for n, p in enumerate(self.data["psi"])), sp.zeros(3, 4))
        a = sum((p*model.T**n for n, p in enumerate(self.data["potential"])), sp.zeros(3, 1))
        first_residual = psi.diff(model.T)-model.dirac_rhs(psi, a)
        second_residual = psi.diff(model.T, 2)-model.dirac_rhs(psi.diff(model.T), a)
        second_residual += sp.I*sum((a[i].diff(model.T)*psi @ model.WEIGHTS[i+1].T
                                    for i in range(3)), sp.zeros(3, 4))
        self.assertZero(first_residual.diff(model.T)-second_residual)

    def test_input_validation_rejects_invalid_order_and_coupling(self):
        model.series(1, model.COUPLING)
        for order in (-1, 5, 1.5, True):
            with self.assertRaises(ValueError):
                model.series(order)
        with self.assertRaises(ValueError):
            model.series(True, model.COUPLING)
        for coupling in (-1, sp.I, sp.oo, sp.nan, sp.Symbol("q")):
            with self.assertRaises(ValueError):
                model.initial_data(coupling)

    def test_report_preserves_local_comparison_and_negative_controls(self):
        report = model.evaluate()
        self.assertFalse(report["main_TeX_changed"])
        self.assertIn("NOT native C7", report["status"])
        self.assertTrue(report["same_induced_frame_negative_control"]["same_frame_obstruction_is_not_removed"])
        saved = json.loads((ROOT / "analysis/HC_Sourced_Cauchy_Coframe.json").read_text(encoding="utf-8"))
        for key in ("status", "dictionary", "initial_data", "exact_Taylor_substitution", "local_analytic_existence", "main_TeX_changed"):
            self.assertEqual(saved[key], report[key])
        for key in ("coframe", "metric", "reference_probe_stress", "spin_connection_norm", "curvature_norm"):
            np.testing.assert_allclose(saved["geometry_at_origin"][key], report["geometry_at_origin"][key], atol=2e-12)
        for key in ("reference_Dirac_residual_norm", "induced_Dirac_residual_norm", "imaginary_bilinear_residual"):
            self.assertAlmostEqual(saved["same_induced_frame_negative_control"][key], report["same_induced_frame_negative_control"][key])


if __name__ == "__main__":
    unittest.main()
