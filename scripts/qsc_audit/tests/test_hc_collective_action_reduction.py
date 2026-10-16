"""Retain the canonical hidden partners and check normal equations, not just the ansatz."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_collective", ROOT / "analysis/HC_Collective_Action_Reduction.py")
action = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(action)
projected, phase, readout = action.projected, action.phase, action.readout


class HCCollectiveActionReductionTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def coordinates(self):
        return np.array([1.2, 2.15, 0.2, -0.1])

    def hamiltonian(self):
        return np.array([[2, 0.1-0.4j], [0.1+0.4j, 1]])

    def test_collective_chart_round_trips_every_complex_mode_with_nonzero_residual(self):
        rng = np.random.default_rng(91)
        for _ in range(20):
            f = rng.normal(size=2)+1j*rng.normal(size=2)
            self.assertClose(action.modal_state(action.modal_coordinates(f)), f)

    def test_chart_contains_all_four_real_directions_not_just_the_odd_plane(self):
        tangents = action.modal_tangents(self.coordinates())
        real_jacobian = np.vstack([tangents.real, tangents.imag])
        self.assertEqual(np.linalg.matrix_rank(real_jacobian), 4)
        self.assertAlmostEqual(abs(np.linalg.det(real_jacobian)), self.coordinates()[0]/2)

    def test_full_norm_separates_residual_amplitude_and_both_hidden_partners(self):
        q = self.coordinates()
        f = action.modal_state(q)
        self.assertAlmostEqual(np.vdot(f, f).real, q[0]**2+q[2]**2+q[3]**2)

    def test_modal_tangents_match_independent_finite_differences(self):
        q, step = self.coordinates(), 1e-6
        columns = []
        for delta in step*np.eye(4):
            columns.append((action.modal_state(q+delta)-action.modal_state(q-delta))/(2*step))
        self.assertClose(action.modal_tangents(q), np.column_stack(columns), atol=2e-10)

    def test_kinetic_one_form_is_the_exact_pullback_of_the_complex_probe_term(self):
        q = self.coordinates()
        expected = -(action.modal_state(q).conj() @ action.modal_tangents(q)).imag
        self.assertClose(action.kinetic_one_form(q), expected)

    def test_symplectic_form_matches_the_complex_tangent_gram(self):
        q = self.coordinates()
        tangents = action.modal_tangents(q)
        self.assertClose(action.symplectic_form(q), -2*(tangents.conj().T @ tangents).imag)

    def test_symplectic_form_is_the_exterior_derivative_of_the_one_form(self):
        q, step = self.coordinates(), 1e-6
        derivative = np.column_stack([(action.kinetic_one_form(q+delta)-action.kinetic_one_form(q-delta))/(2*step)
                                      for delta in step*np.eye(4)])
        self.assertClose(action.symplectic_form(q), derivative.T-derivative, atol=2e-10)

    def test_symplectic_determinant_is_nonzero_precisely_on_the_declared_amplitude_chart(self):
        for amplitude in [0.2, 1, 2.4]:
            q = self.coordinates()
            q[0] = amplitude
            self.assertAlmostEqual(np.linalg.det(action.symplectic_form(q)), 4*amplitude**2)

    def test_collective_lagrangian_equals_the_original_complex_modal_lagrangian(self):
        q, rates, h = self.coordinates(), np.array([0.3, -0.2, 0.1, 0.4]), self.hamiltonian()
        f, fdot = action.modal_state(q), action.modal_tangents(q) @ rates
        expected = -np.vdot(f, fdot).imag-np.vdot(f, h @ f).real
        self.assertAlmostEqual(action.collective_lagrangian(q, rates, h), expected)

    def test_tangent_action_equations_are_the_pullback_of_the_full_modal_residual(self):
        q, rates, h = self.coordinates(), np.array([0.3, -0.2, 0.1, 0.4]), self.hamiltonian()
        f, jacobian = action.modal_state(q), action.modal_tangents(q)
        _, gradient = action.probe_energy_gradient(q, h)
        expected = 2*(jacobian.conj().T @ (1j*jacobian @ rates-h @ f)).real
        self.assertClose(action.symplectic_form(q) @ rates-gradient, expected)

    def test_full_collective_equations_reproduce_the_hermitian_probe_evolution(self):
        q, h = self.coordinates(), self.hamiltonian()
        rates = action.collective_rhs(q, h)
        self.assertClose(action.modal_tangents(q) @ rates, -1j*h @ action.modal_state(q))

    def test_collective_flow_conserves_its_autonomous_energy(self):
        q, h = self.coordinates(), self.hamiltonian()
        _, gradient = action.probe_energy_gradient(q, h)
        self.assertAlmostEqual(gradient @ action.collective_rhs(q, h), 0)

    def test_collective_flow_conserves_the_full_norm_not_necessarily_the_residual_amplitude(self):
        q, h = self.coordinates(), self.hamiltonian()
        rates = action.collective_rhs(q, h)
        self.assertAlmostEqual(2*(q[0]*rates[0]+q[2]*rates[2]+q[3]*rates[3]), 0)
        self.assertGreater(abs(rates[0]), 0.01)

    def test_restricting_to_the_odd_plane_erases_the_pulled_back_kinetic_form(self):
        q = np.array([1, 2.1, 0, 0])
        self.assertClose(action.kinetic_one_form(q)[:2], np.zeros(2))
        self.assertClose(action.symplectic_form(q)[:2, :2], np.zeros((2, 2)))

    def test_a_pure_odd_ansatz_has_nonzero_normal_velocity_for_a_scalar_probe_H(self):
        q = np.array([1, 2.1, 0, 0])
        rates = action.collective_rhs(q, 2*np.eye(2))
        self.assertAlmostEqual(rates[0], 0)
        self.assertAlmostEqual(rates[1], 0)
        self.assertAlmostEqual(rates[2], 2)

    def test_zero_restricted_action_does_not_determine_the_actual_odd_phase_velocity(self):
        q, h = np.array([1, 2.1, 0, 0]), 0.3*phase.SIGMA_Y
        self.assertAlmostEqual(action.collective_lagrangian(q, [0.1, 0.2, 0, 0], h), 0)
        rates = action.collective_rhs(q, h)
        self.assertAlmostEqual(rates[1], 0.6)
        self.assertClose(rates[[0, 2, 3]], np.zeros(3))

    def test_canonical_partner_formula_differs_only_by_the_boundary_term(self):
        b, _, a, c = q = self.coordinates()
        rates = np.array([0.3, -0.2, 0.1, 0.4])
        canonical = -2*a*rates[0]-b*c*rates[1]
        boundary_derivative = b*rates[2]+a*rates[0]
        self.assertAlmostEqual(action.kinetic_one_form(q) @ rates, canonical+boundary_derivative)

    def test_hidden_solution_satisfies_the_algebraic_action_equation_not_static_energy_minimization(self):
        b, velocity = 1.3, np.array([0.2, -0.1])
        w, j = np.array([[3, 0.2], [0.2, 2]]), np.array([0.1, -0.2])
        hidden = action.stationary_hidden(b, velocity, w, j)
        self.assertClose(w @ hidden+np.diag([2, b]) @ velocity+j, np.zeros(2))
        self.assertGreater(np.linalg.norm(hidden+np.linalg.solve(w, j)), 0.1)

    def test_eliminated_lagrangian_equals_direct_substitution_with_all_signs_retained(self):
        b, velocity, potential = 1.3, np.array([0.2, -0.1]), 0.7
        w, j = np.array([[3, 0.2], [0.2, 2]]), np.array([0.1, -0.2])
        hidden = action.stationary_hidden(b, velocity, w, j)
        original = -hidden @ np.diag([2, b]) @ velocity-potential-j @ hidden-hidden @ w @ hidden/2
        self.assertAlmostEqual(action.effective_lagrangian(b, velocity, w, j, potential), original)

    def test_positive_hidden_Hessian_induces_a_positive_kinetic_metric(self):
        w = np.array([[3, 0.2], [0.2, 2]])
        data = action.effective_coefficients(1.3, w, [0.1, -0.2], 0.7)
        self.assertGreater(np.linalg.eigvalsh(data["kinetic_metric"])[0], 0)
        self.assertClose(data["kinetic_metric"], data["kinetic_metric"].T)

    def test_expanded_effective_coefficients_reproduce_the_completed_square(self):
        b, velocity, potential = 1.3, np.array([0.2, -0.1]), 0.7
        w, j = np.array([[3, 0.2], [0.2, 2]]), np.array([0.1, -0.2])
        data = action.effective_coefficients(b, w, j, potential)
        expected = velocity @ data["kinetic_metric"] @ velocity/2+data["velocity_one_form"] @ velocity-data["potential"]
        self.assertAlmostEqual(action.effective_lagrangian(b, velocity, w, j, potential), expected)

    def test_isotropic_hidden_energy_is_exactly_the_original_probe_energy(self):
        b, _, a, c = q = self.coordinates()
        m, omega = 2, 0.3
        expected = m*(a*a+b*b+c*c)-2*omega*b*c
        self.assertAlmostEqual(action.probe_energy_gradient(q, m*np.eye(2)+omega*phase.SIGMA_Y)[0], expected)

    def test_isotropic_effective_lagrangian_has_the_derived_inertia_and_rotation_shift(self):
        b, velocity, m, omega = 1.3, np.array([0.2, -0.1]), 2, 0.3
        result = action.effective_lagrangian(b, velocity, 2*m*np.eye(2), [0, -2*omega*b], m*b*b)
        expected = velocity[0]**2/m+b*b*(velocity[1]-2*omega)**2/(4*m)-m*b*b
        self.assertAlmostEqual(result, expected)

    def test_phase_inertia_and_invariant_phase_conversion_are_not_input_parameters(self):
        b, m = 1.3, 2
        data = action.effective_coefficients(b, 2*m*np.eye(2), [0, -0.6*b], m*b*b)
        self.assertAlmostEqual(data["kinetic_metric"][1, 1], b*b/(2*m))
        self.assertAlmostEqual(data["kinetic_metric"][1, 1]/9, b*b/(18*m))

    def test_isotropic_hidden_reconstruction_recovers_both_canonical_partners(self):
        q, m, omega = self.coordinates(), 2, 0.3
        velocity = action.collective_rhs(q, m*np.eye(2)+omega*phase.SIGMA_Y)[:2]
        self.assertClose(action.isotropic_reconstruction(q[:2], velocity, m, omega), q)

    def test_isotropic_second_order_equations_match_the_full_first_order_flow(self):
        q, step, m, omega = self.coordinates(), 1e-6, 2, 0.3
        h = m*np.eye(2)+omega*phase.SIGMA_Y
        rates = action.collective_rhs(q, h)
        acceleration = (action.collective_rhs(q+step*rates, h)-action.collective_rhs(q-step*rates, h))/(2*step)
        self.assertClose(action.isotropic_accelerations(q[:2], rates[:2], m, omega), acceleration[:2], atol=4e-10)

    def test_effective_energy_equals_full_probe_energy_after_reconstruction(self):
        q, m, omega = self.coordinates(), 2, 0.3
        h = m*np.eye(2)+omega*phase.SIGMA_Y
        velocity = action.collective_rhs(q, h)[:2]
        b = q[0]
        data = action.effective_coefficients(b, 2*m*np.eye(2), [0, -2*omega*b], m*b*b)
        effective = velocity @ data["kinetic_metric"] @ velocity/2+data["potential"]
        self.assertAlmostEqual(effective, action.probe_energy_gradient(q, h)[0])

    def test_phase_momentum_is_conserved_in_the_reversible_amplitude_phase_exchange(self):
        q, m, omega = self.coordinates(), 2, 0.3
        velocity = action.collective_rhs(q, m*np.eye(2)+omega*phase.SIGMA_Y)[:2]
        acceleration = action.isotropic_accelerations(q[:2], velocity, m, omega)
        b, bdot, relative = q[0], velocity[0], velocity[1]-2*omega
        self.assertAlmostEqual(2*b*bdot*relative+b*b*acceleration[1], 0)
        self.assertAlmostEqual(b*b*relative/(2*m), -b*q[3])

    def test_apparent_angular_damping_changes_sign_when_the_amplitude_velocity_reverses(self):
        positive = action.isotropic_accelerations([1, 2.1], [0.2, 1.0])[1]
        negative = action.isotropic_accelerations([1, 2.1], [-0.2, 1.0])[1]
        self.assertLess(positive, 0)
        self.assertGreater(negative, 0)
        self.assertAlmostEqual(positive, -negative)

    def test_exact_unitary_solution_matches_joint_amplitude_phase_and_hidden_motion(self):
        initial = action.modal_state([1, 2*math.pi/3, 0, 0])
        m, omega, time = 2, 0.3, 0.5
        state = projected.unitary_state(m*np.eye(2)+omega*phase.SIGMA_Y, initial, time)
        expected = [math.cos(m*time), 2*math.pi/3+2*omega*time, math.sin(m*time), 0]
        self.assertClose(action.modal_coordinates(state), expected)
        self.assertAlmostEqual(np.vdot(state, state).real, 1)

    def test_consistent_modal_motion_can_still_exit_the_root_chamber(self):
        data = action.evaluate()["isotropic_probe_example"]
        self.assertGreater(data["minimum_principal_root_before"], 0)
        self.assertLess(data["minimum_signed_root_after"], 0)
        self.assertAlmostEqual(data["probe_energy"], data["effective_energy"])

    def test_restricted_equations_can_hold_while_an_omitted_normal_equation_fails(self):
        h = np.zeros((3, 3), dtype=complex)
        h[:2, :2] = self.hamiltonian()
        h[2, 2], h[0, 2], h[2, 0] = 5, 0.1, 0.1
        self.assertGreater(np.linalg.eigvalsh(h)[0], 0)
        f = phase.aligned_mode(0)
        embedding = np.vstack([np.eye(2), np.zeros((1, 2))])
        result = action.embedding_residual(f, -1j*h[:2, :2] @ f, h, embedding)
        self.assertClose(result["tangent"], np.zeros(2))
        self.assertAlmostEqual(np.linalg.norm(result["normal"]), 0.05)

    def test_no_omitted_mode_residual_remains_when_the_embedding_is_invariant(self):
        h = np.zeros((3, 3), dtype=complex)
        h[:2, :2], h[2, 2] = self.hamiltonian(), 5
        f = phase.aligned_mode(0)
        embedding = np.vstack([np.eye(2), np.zeros((1, 2))])
        result = action.embedding_residual(f, -1j*h[:2, :2] @ f, h, embedding)
        self.assertClose(result["full"], np.zeros(3))

    def test_general_cartesian_elimination_preserves_the_original_hidden_initial_data(self):
        h = self.hamiltonian()
        f = action.modal_state(self.coordinates())
        rdot = (-1j*h @ f).imag
        reconstructed = np.linalg.solve(h.real, h.imag @ f.imag-rdot)
        self.assertClose(reconstructed, f.real)
        original_after_boundary = -2*f.real @ rdot-np.vdot(f, h @ f).real
        self.assertAlmostEqual(action.cartesian_effective_lagrangian(f.imag, rdot, h), original_after_boundary)

    def test_general_cartesian_second_order_equation_matches_exact_complex_transport(self):
        h = self.hamiltonian()
        f = action.modal_state(self.coordinates())
        rate = (-1j*h @ f).imag
        expected = (-h @ h @ f).imag
        self.assertClose(action.cartesian_acceleration(f.imag, rate, h), expected)

    def test_guards_reject_singular_charts_nonpositive_hidden_blocks_and_invalid_embeddings(self):
        for q in [[0, 0, 0, 0], [1, 2], [1, math.nan, 0, 0]]:
            with self.assertRaises(ValueError):
                action.modal_state(q)
        with self.assertRaises(ValueError):
            action.modal_coordinates([1, 2])
        for w in [np.zeros((2, 2)), np.diag([1, -1]), [[1, 1], [0, 1]]]:
            with self.assertRaises(ValueError):
                action.stationary_hidden(1, [0, 0], w, [0, 0])
        with self.assertRaises(ValueError):
            action.cartesian_effective_lagrangian([1, 0], [0, 0], phase.SIGMA_Y)
        with self.assertRaises(ValueError):
            action.embedding_residual([1, 0], [0, 0], np.eye(3), np.ones((3, 2)))
        with self.assertRaises(ValueError):
            action.probe_energy_gradient(self.coordinates(), np.eye(3))

    def test_saved_report_marks_the_native_and_transverse_obligations_as_open(self):
        data = action.evaluate()
        with patch.object(projected.backreaction.phase.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(action.evaluate(), data)
        self.assertFalse(data["main_TeX_changed"])
        self.assertFalse(data["historical_masses_or_target_phase_used"])
        self.assertTrue(data["full_native_action_contract"]["native_field_profiles_and_real_positive_kinetic_reduction_missing"])
        self.assertTrue(data["normal_equation_countercheck"]["normal_equation_would_be_missed_by_restricting_the_action_first"])
        saved = json.loads((ROOT / "analysis/HC_Collective_Action_Reduction.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, data)
