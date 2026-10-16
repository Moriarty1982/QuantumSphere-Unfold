"""Check the curvature pullback, real-form obstruction and omitted normal equations."""
from pathlib import Path
import importlib.util
import itertools
import json
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_null_axis", ROOT / "analysis/HC_Null_Axis_Action_Check.py")
action = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(action)


class HCNullAxisActionCheckTests(unittest.TestCase):
    def setUp(self):
        self.n = action.NULL_COVECTOR.copy()
        self.t = np.diag([1.0, 2.0])
        self.kappa = 0.4
        self.rng = np.random.default_rng(192)

    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def hermitian_tensor(self):
        data = self.rng.normal(size=(4, 4, 2, 2))+1j*self.rng.normal(size=(4, 4, 2, 2))
        data = (data+data.conj().swapaxes(-1, -2))/2
        return (data-data.swapaxes(0, 1))/2

    def test_wedge_is_the_direct_curvature_of_the_fixed_axis_connection(self):
        gradient = self.rng.normal(size=4)
        connection = self.kappa*0.7*self.n[:, None, None]*self.t
        derivative = self.kappa*np.outer(gradient, self.n)[:, :, None, None]*self.t
        self.assertClose(action.connection_curvature(connection, derivative),
                         action.null_axis_curvature(gradient, self.n, self.t, self.kappa))

    def test_constant_commuting_closure_background_does_not_change_the_wedge(self):
        q = np.diag([0.0, 1.0])
        gradient = self.rng.normal(size=4)
        connection = self.n[:, None, None]*(0.7*self.kappa*self.t+0.3*q)
        derivative = self.kappa*np.outer(gradient, self.n)[:, :, None, None]*self.t
        self.assertClose(action.connection_curvature(connection, derivative),
                         action.null_axis_curvature(gradient, self.n, self.t, self.kappa))

    def test_general_connection_keeps_the_nonabelian_commutator(self):
        b = self.rng.normal(size=(4, 2, 2))+1j*self.rng.normal(size=(4, 2, 2))
        db = self.rng.normal(size=(4, 4, 2, 2))
        expected = np.zeros_like(db, dtype=complex)
        for mu in range(4):
            for nu in range(4):
                expected[mu, nu] = db[mu, nu]-db[nu, mu]+b[mu] @ b[nu]-b[nu] @ b[mu]
        self.assertClose(action.connection_curvature(b, db), expected)

    def test_curvature_and_its_ordinary_trace_contraction_match_the_general_wedge_identity(self):
        for _ in range(10):
            n, gradient = self.rng.normal(size=(2, 4))
            curvature = action.null_axis_curvature(gradient, n, self.t, self.kappa)
            n2, grad2 = n @ action.METRIC @ n, gradient @ action.METRIC @ gradient
            directional = n @ action.METRIC @ gradient
            expected = -self.kappa**2*np.trace(self.t @ self.t)*(n2*grad2-directional**2)/2
            self.assertClose(curvature, -curvature.swapaxes(0, 1))
            self.assertAlmostEqual(action.curvature_lagrangian(curvature).real, expected)
            self.assertAlmostEqual(action.scalar_lagrangian(gradient, n, self.t, self.kappa), expected)

    def test_null_lagrangian_is_only_the_squared_directional_derivative(self):
        gradient = self.rng.normal(size=4)
        derivative = (action.METRIC @ self.n) @ gradient
        expected = self.kappa**2*np.trace(self.t @ self.t)*derivative**2/2
        self.assertAlmostEqual(action.scalar_lagrangian(gradient, self.n, self.t, self.kappa), expected)

    def test_principal_tensor_is_the_gradient_hessian_of_the_action(self):
        gradient, step = self.rng.normal(size=4), 1e-4
        lagrangian = lambda value: action.scalar_lagrangian(value, self.n, self.t, self.kappa)
        actual = np.zeros((4, 4))
        for i, ei in enumerate(step*np.eye(4)):
            for j, ej in enumerate(step*np.eye(4)):
                actual[i, j] = (lagrangian(gradient+ei+ej)-lagrangian(gradient+ei-ej)
                                -lagrangian(gradient-ei+ej)+lagrangian(gradient-ei-ej))/(4*step**2)
        self.assertClose(actual, action.scalar_kinetic_tensor(self.n, self.t, self.kappa), atol=2e-8)

    def test_nonzero_null_principal_tensor_has_rank_one_not_a_wave_metric(self):
        kinetic = action.scalar_kinetic_tensor(self.n, self.t, self.kappa)
        self.assertEqual(np.linalg.matrix_rank(kinetic), 1)
        self.assertClose(np.linalg.eigvalsh(kinetic), [0, 0, 0, 1.6])

    def test_homogeneous_time_coefficient_is_positive_in_this_branch(self):
        coefficient = action.scalar_kinetic_tensor(self.n, self.t, self.kappa)[0, 0]
        self.assertAlmostEqual(coefficient, 0.8)
        self.assertAlmostEqual(action.scalar_lagrangian([2, 0, 0, 0], self.n, self.t, self.kappa), 2*coefficient)

    def test_nonzero_transverse_gradients_can_have_zero_null_action(self):
        gradient = np.array([0, 1, 2, 0])
        curvature = action.null_axis_curvature(gradient, self.n, self.t, self.kappa)
        self.assertGreater(np.linalg.norm(curvature), 1)
        self.assertAlmostEqual(action.curvature_lagrangian(curvature).real, 0)

    def test_nonnull_principal_tensors_instead_have_rank_three(self):
        for n in [[1, 0, 0, 0], [0, 1, 0, 0]]:
            self.assertEqual(np.linalg.matrix_rank(action.scalar_kinetic_tensor(n, self.t, self.kappa)), 3)

    def test_rescaling_the_axis_and_inverse_coupling_leaves_the_action_fixed(self):
        gradient = self.rng.normal(size=4)
        self.assertClose(action.null_axis_curvature(gradient, 3*self.n, self.t, self.kappa/3),
                         action.null_axis_curvature(gradient, self.n, self.t, self.kappa))
        self.assertClose(action.scalar_kinetic_tensor(3*self.n, self.t, self.kappa/3),
                         action.scalar_kinetic_tensor(self.n, self.t, self.kappa))

    def test_internal_unitary_basis_change_preserves_the_coefficient(self):
        raw = self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))
        unitary, _ = np.linalg.qr(raw)
        rotated = unitary @ self.t @ unitary.conj().T
        self.assertClose(action.scalar_kinetic_tensor(self.n, rotated, self.kappa),
                         action.scalar_kinetic_tensor(self.n, self.t, self.kappa))

    def test_zero_coupling_or_generator_has_no_hc_kinetic_contribution(self):
        self.assertClose(action.scalar_kinetic_tensor(self.n, self.t, 0), np.zeros((4, 4)))
        self.assertClose(action.scalar_kinetic_tensor(self.n, 0*self.t, self.kappa), np.zeros((4, 4)))

    def test_identically_zero_hc_branch_has_no_curvature_from_hc(self):
        self.assertClose(action.null_axis_curvature(np.zeros(4), self.n, self.t, self.kappa),
                         np.zeros((4, 4, 2, 2)))

    def test_zero_hc_value_at_one_point_does_not_remove_its_derivative_curvature(self):
        connection = np.zeros((4, 2, 2))
        derivative = self.kappa*np.outer([1, 0, 0, 0], self.n)[:, :, None, None]*self.t
        self.assertGreater(np.linalg.norm(action.connection_curvature(connection, derivative)), 0)

    def test_literal_gauge_and_compensator_electric_profiles_have_opposite_signs(self):
        electric = action.null_axis_curvature([1, 0, 0, 0], self.n, self.t, self.kappa)
        self.assertAlmostEqual(action.curvature_lagrangian(electric).real, 0.4)
        self.assertAlmostEqual(action.curvature_lagrangian(1j*electric).real, -0.4)

    def test_literal_mixed_action_is_generically_complex_before_any_real_projection(self):
        electric = action.null_axis_curvature([1, 0, 0, 0], self.n, self.t, self.kappa)
        self.assertClose(action.curvature_lagrangian((1+1j)*electric), 0.8j)

    def test_cross_term_is_purely_imaginary_for_arbitrary_hermitian_curvatures(self):
        gauge, hc = self.hermitian_tensor(), self.hermitian_tensor()
        combined = action.curvature_lagrangian(1j*gauge+hc)
        separate = action.curvature_lagrangian(1j*gauge)+action.curvature_lagrangian(hc)
        self.assertAlmostEqual(combined.real, separate.real)

    def test_dagger_comparison_changes_the_action_and_gives_same_electric_signs(self):
        electric = action.null_axis_curvature([1, 0, 0, 0], self.n, self.t, self.kappa)
        for curvature in [electric, 1j*electric]:
            self.assertAlmostEqual(action.curvature_lagrangian(curvature, "dagger_comparison").real, 0.4)
        self.assertAlmostEqual(action.curvature_lagrangian((1+1j)*electric, "dagger_comparison").real, 0.8)

    def test_profile_gradient_is_independently_differentiated(self):
        point, step = np.array([0.7, 0.0, 0.0, 0.4]), 1e-6
        actual = []
        for delta in step*np.eye(4):
            plus, minus = point+delta, point-delta
            actual.append((action.null_wave_profile(plus[0], plus[3], 1.3)["value"]
                           -action.null_wave_profile(minus[0], minus[3], 1.3)["value"])/(2*step))
        self.assertClose(actual, action.null_wave_profile(point[0], point[3], 1.3)["gradient"], atol=2e-10)

    def test_alternative_paired_equations_match_constant_matrix_action_variations(self):
        raw = self.rng.normal(size=(4, 2, 2))+1j*self.rng.normal(size=(4, 2, 2))
        gauge = (raw+raw.conj().swapaxes(-1, -2))/2
        raw = self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))
        hc = (raw+raw.conj().T)/2
        result = action.constant_paired_field_equations(gauge, hc, self.n, self.kappa)
        directions = [np.eye(2), np.diag([1, -1]), np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]])]
        step = 1e-5
        for direction in directions:
            p = action.constant_paired_field_equations(gauge, hc+step*direction, self.n, self.kappa)
            m = action.constant_paired_field_equations(gauge, hc-step*direction, self.n, self.kappa)
            self.assertClose((p["L"]-m["L"])/(2*step), np.trace(result["hc_EL"] @ direction).real, atol=2e-8)
            for mu in range(4):
                change = np.zeros_like(gauge)
                change[mu] = direction
                p = action.constant_paired_field_equations(gauge+step*change, hc, self.n, self.kappa)
                m = action.constant_paired_field_equations(gauge-step*change, hc, self.n, self.kappa)
                self.assertClose((p["L"]-m["L"])/(2*step), np.trace(result["gauge_EL"][mu] @ direction).real, atol=2e-8)

    def test_alternative_constant_field_curvature_matches_the_unsplit_connection(self):
        gauge = np.array([np.diag([1, -1]), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], np.eye(2)])
        result = action.constant_paired_field_equations(gauge, self.t, self.n, self.kappa)
        connection = 1j*gauge+self.kappa*self.n[:, None, None]*self.t
        expected = action.connection_curvature(connection, np.zeros((4, 4, 2, 2)))
        self.assertClose(result["curvature"], expected)

    def test_alternative_paired_action_and_equations_are_unitary_covariant(self):
        gauge = np.array([np.diag([1, -1]), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], np.eye(2)])
        raw = self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))
        unitary, _ = np.linalg.qr(raw)
        before = action.constant_paired_field_equations(gauge, self.t, self.n, self.kappa)
        after = action.constant_paired_field_equations(unitary @ gauge @ unitary.conj().T,
                                                       unitary @ self.t @ unitary.conj().T, self.n, self.kappa)
        self.assertAlmostEqual(before["L"], after["L"])
        self.assertClose(after["gauge_EL"], unitary @ before["gauge_EL"] @ unitary.conj().T)
        self.assertClose(after["hc_EL"], unitary @ before["hc_EL"] @ unitary.conj().T)

    def test_alternative_commuting_wave_satisfies_hc_and_gauge_curvature_only_equations(self):
        profile = action.null_wave_profile(0.7, 0.4, 1.3)
        full = action.abelian_residual(profile["hessian"], self.n, self.t, self.kappa)
        hc_el = self.kappa*np.einsum("n,nij->ij", action.METRIC @ self.n, full)
        self.assertClose(hc_el, np.zeros((2, 2)))
        x = action.null_axis_curvature(profile["gradient"], self.n, self.t, 1)
        h = profile["value"]*self.t
        self.assertClose(h @ x-x @ h, np.zeros_like(x))
        self.assertGreater(np.linalg.norm(full), 0.5)

    def test_alternative_constant_field_check_rejects_nonhermitian_gauge_inputs(self):
        gauge = np.zeros((4, 2, 2))
        gauge[0, 0, 1] = 1
        with self.assertRaises(ValueError):
            action.constant_paired_field_equations(gauge, self.t, self.n, self.kappa)

    def test_profile_hessian_and_third_derivative_are_independently_differentiated(self):
        point, step = np.array([0.7, 0.0, 0.0, 0.4]), 1e-6
        profile = action.null_wave_profile(point[0], point[3], 1.3)
        for axis, delta in enumerate(step*np.eye(4)):
            plus, minus = point+delta, point-delta
            p = action.null_wave_profile(plus[0], plus[3], 1.3)
            m = action.null_wave_profile(minus[0], minus[3], 1.3)
            self.assertClose((p["gradient"]-m["gradient"])/(2*step), profile["hessian"][axis], atol=2e-10)
            self.assertClose((p["hessian"]-m["hessian"])/(2*step), profile["third_derivative"][axis], atol=2e-10)

    def test_residual_is_the_direct_spacetime_divergence_of_curvature(self):
        point, step = np.array([0.7, 0.0, 0.0, 0.4]), 1e-6
        direct = np.zeros((4, 2, 2), dtype=complex)
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = point+delta, point-delta
            p = action.null_wave_profile(plus[0], plus[3], 1.3)
            m = action.null_wave_profile(minus[0], minus[3], 1.3)
            fp = action.null_axis_curvature(p["gradient"], self.n, self.t, self.kappa)
            fm = action.null_axis_curvature(m["gradient"], self.n, self.t, self.kappa)
            direct += action.METRIC[mu, mu]*(fp[mu]-fm[mu])/(2*step)
        profile = action.null_wave_profile(point[0], point[3], 1.3)
        self.assertClose(direct, action.abelian_residual(profile["hessian"], self.n, self.t, self.kappa), atol=2e-10)

    def test_scalar_el_is_only_the_connection_residual_projection_for_any_axis(self):
        for n in [self.n, self.rng.normal(size=4)]:
            hessian = self.rng.normal(size=(4, 4))
            hessian = (hessian+hessian.T)/2
            residual = action.abelian_residual(hessian, n, self.t, self.kappa)
            expected = self.kappa*np.einsum("n,ij,nji->", action.METRIC @ n, self.t, residual).real
            self.assertAlmostEqual(action.scalar_el(hessian, n, self.t, self.kappa), expected)

    def test_wave_witness_satisfies_restricted_el_at_all_sample_points(self):
        for time, z in self.rng.normal(size=(10, 2)):
            profile = action.null_wave_profile(time, z, 1.3, 2)
            self.assertAlmostEqual(action.scalar_el(profile["hessian"], self.n, self.t, self.kappa), 0)

    def test_wave_witness_fails_the_full_connection_equation(self):
        time, z, k = 0.7, 0.4, 1.3
        profile = action.null_wave_profile(time, z, k, 2)
        residual = action.abelian_residual(profile["hessian"], self.n, self.t, self.kappa)
        expected = self.kappa*k*np.sin(k*(z-time))*self.t
        self.assertClose(residual[0], expected)
        self.assertClose(residual[3], -expected)
        self.assertClose(residual[1:3], 0*residual[1:3])
        self.assertGreater(np.linalg.norm(residual), 0.5)
        self.assertGreater(profile["value"], 0)

    def test_abelian_differential_identity_holds_for_arbitrary_smooth_third_derivatives(self):
        raw = self.rng.normal(size=(4, 4, 4))
        third = sum(raw.transpose(p) for p in itertools.permutations(range(3)))/6
        for n in [self.n, self.rng.normal(size=4)]:
            derivative = action.abelian_residual_derivative(third, n, self.t, self.kappa)
            self.assertClose(np.einsum("dn,dnij->ij", action.METRIC, derivative), np.zeros((2, 2)))

    def test_differential_identity_holds_even_when_full_residual_is_nonzero(self):
        profile = action.null_wave_profile(0.7, 0.4, 1.3)
        derivative = action.abelian_residual_derivative(profile["third_derivative"], self.n, self.t, self.kappa)
        self.assertClose(np.einsum("dn,dnij->ij", action.METRIC, derivative), np.zeros((2, 2)))
        self.assertGreater(np.linalg.norm(action.abelian_residual(profile["hessian"], self.n, self.t, self.kappa)), 0.5)

    def test_homogeneous_commuting_profile_has_zero_gauss_component_not_arbitrary_charge(self):
        hessian = np.zeros((4, 4))
        hessian[0, 0] = 0.7
        residual = action.abelian_residual(hessian, self.n, self.t, self.kappa)
        self.assertClose(residual[0], np.zeros((2, 2)))
        self.assertGreater(np.linalg.norm(residual[3]), 0)

    def test_scalar_potential_changes_restricted_el_but_not_the_curvature_gauss_identity(self):
        hessian = np.zeros((4, 4))
        hessian[0, 0] = 0.7
        scalar_force = action.scalar_el(hessian, self.n, self.t, self.kappa)
        potential_derivative = scalar_force
        self.assertAlmostEqual(scalar_force-potential_derivative, 0)
        self.assertClose(action.abelian_residual(hessian, self.n, self.t, self.kappa)[0], np.zeros((2, 2)))

    def test_existing_matching_penalty_can_balance_a_conditional_homogeneous_oscillation(self):
        penalty, displacement = 0.3, 0.2
        frequency_squared = 2*penalty/(self.kappa**2*(action.METRIC @ self.n)[0]**2)
        hessian = np.zeros((4, 4))
        hessian[0, 0] = -frequency_squared*displacement
        curvature_el = action.scalar_el(hessian, self.n, self.t, self.kappa)
        potential_derivative = 2*penalty*np.trace(self.t @ self.t)*displacement
        self.assertAlmostEqual(curvature_el-potential_derivative, 0)
        self.assertGreater(frequency_squared, 0)

    def test_invalid_scalar_derivatives_and_axes_are_rejected(self):
        for gradient in [[1, 2], [1j, 0, 0, 0], [np.nan, 0, 0, 0]]:
            with self.assertRaises(ValueError):
                action.null_axis_curvature(gradient, self.n, self.t, self.kappa)
        with self.assertRaises(ValueError):
            action.scalar_kinetic_tensor([1, 2], self.t, self.kappa)
        with self.assertRaises(ValueError):
            action.scalar_kinetic_tensor(self.n, self.t, np.inf)

    def test_invalid_internal_generators_are_rejected(self):
        for generator in [[], np.zeros((2, 3)), [[0, 1], [0, 0]], [[np.nan]]]:
            with self.assertRaises(ValueError):
                action.scalar_kinetic_tensor(self.n, generator, self.kappa)

    def test_nonsymmetric_scalar_derivatives_are_rejected(self):
        hessian = np.zeros((4, 4))
        hessian[0, 1] = 1
        with self.assertRaises(ValueError):
            action.abelian_residual(hessian, self.n, self.t, self.kappa)
        third = np.zeros((4, 4, 4))
        third[0, 1, 2] = 1
        with self.assertRaises(ValueError):
            action.abelian_residual_derivative(third, self.n, self.t, self.kappa)

    def test_invalid_connection_and_curvature_contracts_are_rejected(self):
        with self.assertRaises(ValueError):
            action.connection_curvature(np.zeros((3, 2, 2)), np.zeros((4, 4, 2, 2)))
        with self.assertRaises(ValueError):
            action.connection_curvature(np.zeros((4, 2, 2)), np.zeros((3, 4, 2, 2)))
        with self.assertRaises(ValueError):
            action.curvature_lagrangian(np.ones((4, 4, 2, 2)))
        with self.assertRaises(ValueError):
            action.curvature_lagrangian(np.zeros((4, 4, 2, 2)), "silent_repair")

    def test_nonfinite_profile_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            action.null_wave_profile(0.7, 0.4, np.nan)

    def test_report_keeps_the_native_and_comparison_action_boundaries(self):
        report = action.evaluate()
        json.dumps(report, allow_nan=False)
        self.assertEqual(report["commuting_compensator_branch"]["null_tensor_rank"], 1)
        self.assertTrue(report["mixed_reality_diagnostic"]["dagger_pairing_is_a_different_action_not_a_silent_fix"])
        self.assertFalse(report["main_TeX_changed"])
        self.assertFalse(report["empirical_masses_target_phase_or_new_damping_coefficient_used"])
        self.assertGreater(report["full_equation_vs_null_projection"]["full_residual_norm"], 0.5)

    def test_committed_style_report_is_reproducible(self):
        stored = json.loads((ROOT / "analysis/HC_Null_Axis_Action_Check.json").read_text(encoding="utf-8"))
        self.assertEqual(stored, action.evaluate())


if __name__ == "__main__":
    unittest.main()
