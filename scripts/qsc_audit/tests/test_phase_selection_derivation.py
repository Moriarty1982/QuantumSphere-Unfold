"""Conditional selection rules must not be reported as a native prediction."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "phase_selection", ROOT / "analysis/Phase_Selection_Derivation.py")
selection = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(selection)


class PhaseSelectionDerivationTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def test_cyclic_family_is_hermitian_and_unit_normalized(self):
        for phi in np.linspace(-math.pi, math.pi, 15):
            b = selection.cyclic_tensor(phi)
            self.assertClose(b, b.conj().T)
            self.assertAlmostEqual(np.linalg.norm(b, "fro"), 1)

    def test_positive_family_matches_previous_candidate(self):
        theta, b, _ = selection.candidate.cyclic_candidate()
        self.assertClose(selection.cyclic_tensor(3*theta-2*math.pi), b)

    def test_chamber_boundary_is_a_zero_root_not_a_new_mass_prediction(self):
        for phi in [-math.pi/4, math.pi/4]:
            self.assertAlmostEqual(np.linalg.eigvalsh(selection.cyclic_tensor(phi))[0], 0)
        self.assertGreater(np.linalg.eigvalsh(selection.cyclic_tensor(0.5))[0], 0)
        self.assertLess(np.linalg.eigvalsh(selection.cyclic_tensor(0.9))[0], 0)

    def test_cyclic_period_and_phase_conjugation_preserve_spectra(self):
        for phi in [0.1, 0.5, 0.9]:
            q = np.linalg.eigvalsh(selection.cyclic_tensor(phi))
            self.assertClose(q, np.linalg.eigvalsh(selection.cyclic_tensor(phi+2*math.pi)))
            self.assertClose(q, np.linalg.eigvalsh(selection.cyclic_tensor(-phi)))

    def test_determinant_is_affine_in_cosine_of_cycle_phase(self):
        a, r = 1/math.sqrt(6), 1/math.sqrt(12)
        for phi in np.linspace(-math.pi, math.pi, 17):
            analytic = a**3-3*a*r*r+2*r**3*math.cos(phi)
            self.assertAlmostEqual(np.linalg.det(selection.cyclic_tensor(phi)).real, analytic)

    def test_linear_and_quadratic_spectral_invariants_are_phase_blind(self):
        for n in [1, 2]:
            result = selection.trace_harmonics(n)
            self.assertLess(abs(result["cos_phi"]), 2e-12)
            self.assertLess(abs(result["cos_2phi"]), 2e-12)

    def test_powers_three_through_five_have_only_first_phase_harmonic(self):
        for n in [3, 4, 5]:
            result = selection.trace_harmonics(n)
            self.assertGreater(abs(result["cos_phi"]), 0.01)
            self.assertLess(abs(result["cos_2phi"]), 2e-12)
            self.assertLess(result["max_sine_or_higher_harmonic"], 2e-12)

    def test_degree_six_supplies_the_second_phase_harmonic(self):
        result = selection.trace_harmonics(6)
        self.assertAlmostEqual(result["cos_2phi"], 6*(1/math.sqrt(12))**6)
        self.assertGreater(result["cos_2phi"], 0.003)

    def test_residual_projection_selects_a_stable_unfitted_example(self):
        with patch.object(selection.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            result = selection.phase_penalty_selection([-0.8, 0.2], [1, 0], np.eye(2))
        self.assertEqual(result["status"], "stable_interior_conditional")
        self.assertAlmostEqual(result["selected_cosine"], 0.8)
        self.assertAlmostEqual(result["phase_radians"], math.acos(0.8))
        self.assertAlmostEqual(result["minimum_penalty"], 0.04)

    def test_full_stationarity_derivative_includes_metric_variation(self):
        phi, eps = 0.5, 1e-5
        r0, r1 = np.array([-0.8, 0.2j]), np.array([1, 0.1])
        h = np.array([[0.1, 0.03j], [-0.03j, -0.05]])
        g = np.eye(2)+math.cos(phi)*h
        gp = -math.sin(phi)*h
        r, rp = r0+math.cos(phi)*r1, -math.sin(phi)*r1
        analytic = selection.penalty_derivative(r, rp, g, gp)
        def energy(p):
            return selection.phase_penalty(p, r0, r1, np.eye(2)+math.cos(p)*h)
        self.assertAlmostEqual(analytic, (energy(phi+eps)-energy(phi-eps))/(2*eps), places=9)
        self.assertGreater(abs(analytic-selection.penalty_derivative(r, rp, g)), 1e-4)

    def test_constant_metric_derivative_matches_finite_difference(self):
        phi, eps = 0.3, 1e-5
        r0, r1 = np.array([-0.8, 0.2j]), np.array([1, 0.1])
        g = np.array([[1, 0.1j], [-0.1j, 2]])
        analytic = selection.penalty_derivative(r0+math.cos(phi)*r1, -math.sin(phi)*r1, g)
        plus = selection.phase_penalty(phi+eps, r0, r1, g)
        minus = selection.phase_penalty(phi-eps, r0, r1, g)
        self.assertAlmostEqual(analytic, (plus-minus)/(2*eps), places=9)

    def test_selected_penalty_is_minimal_over_positive_chamber(self):
        r0, r1, g = [-0.8, 0.2], [1, 0], np.eye(2)
        result = selection.phase_penalty_selection(r0, r1, g)
        for phi in np.linspace(-math.pi/4, math.pi/4, 151):
            self.assertLessEqual(result["minimum_penalty"], selection.phase_penalty(phi, r0, r1, g)+1e-12)

    def test_phase_blind_residual_is_not_forced_to_one_phase(self):
        result = selection.phase_penalty_selection([1, 2], [0, 0], np.eye(2))
        self.assertEqual(result["status"], "phase_blind")
        self.assertIsNone(result["phase_radians"])

    def test_outside_stationary_projection_can_hit_zero_root_boundary(self):
        result = selection.phase_penalty_selection([-0.2, 0.1], [1, 0], np.eye(2))
        self.assertEqual(result["status"], "zero_root_boundary")
        self.assertAlmostEqual(result["phase_radians"], math.pi/4)

    def test_other_boundary_has_two_equal_root_eigenvalues(self):
        result = selection.phase_penalty_selection([-1.2, 0.1], [1, 0], np.eye(2))
        self.assertEqual(result["status"], "two_equal_roots")
        roots = np.linalg.eigvalsh(selection.cyclic_tensor(result["phase_radians"]))
        self.assertAlmostEqual(roots[0], roots[1])

    def test_phase_curvature_is_positive_and_matches_numerical_second_derivative(self):
        r0, r1, g = [-0.8, 0.2], [1, 0], np.eye(2)
        result = selection.phase_penalty_selection(r0, r1, g)
        phi, eps = result["phase_radians"], 1e-4
        second = (selection.phase_penalty(phi+eps, r0, r1, g)
                  -2*selection.phase_penalty(phi, r0, r1, g)
                  +selection.phase_penalty(phi-eps, r0, r1, g))/eps**2
        self.assertAlmostEqual(second, result["interior_phase_curvature"], places=7)

    def test_comparison_covariance_preserves_selection_even_for_nonunitary_chart(self):
        r0, r1 = np.array([-0.8, 0.2j]), np.array([1, 0])
        g = np.array([[1, 0.1], [0.1, 2]])
        d = np.array([[1.3, 0.1j], [0, 0.8]])
        before = selection.phase_penalty_selection(r0, r1, g)
        after = selection.phase_penalty_selection(np.linalg.solve(d, r0), np.linalg.solve(d, r1), d.conj().T @ g @ d)
        self.assertAlmostEqual(before["selected_cosine"], after["selected_cosine"])
        self.assertAlmostEqual(before["minimum_penalty"], after["minimum_penalty"])

    def test_harmonic_and_residual_selection_are_the_same_conditional_equation(self):
        result = selection.phase_penalty_selection([-0.8, 0.2], [1, 0], np.eye(2))
        phi = selection.stable_two_harmonic_phase(result["first_harmonic_coefficient"], result["second_harmonic_coefficient"])
        self.assertAlmostEqual(phi, result["phase_radians"])

    def test_invalid_or_boundary_harmonic_coefficients_do_not_give_interior_solution(self):
        for l1, l2 in [(0, 1), (-4, 1), (-2*math.sqrt(2), 1), (-3, 0),
                       (-3, -1), (np.nan, 1), (-3, np.inf)]:
            with self.subTest(l1=l1, l2=l2), self.assertRaises(ValueError):
                selection.stable_two_harmonic_phase(l1, l2)

    def test_invalid_residual_metrics_dimensions_and_variations_rejected(self):
        for r0, r1, g in [([], [], np.zeros((0, 0))), ([1], [1, 2], np.eye(2)),
                           ([np.nan], [1], np.eye(1)), ([1], [1], np.diag([-1])),
                           ([1], [1], np.eye(2)), ([1, 2], [1, 2], [[1, 1], [0, 1]])]:
            with self.subTest(r0=r0, r1=r1), self.assertRaises(ValueError):
                selection.phase_penalty_selection(r0, r1, g)
        with self.assertRaises(ValueError):
            selection.penalty_derivative([1, 2], [0, 0], np.eye(2), [[0, 1], [0, 0]])
        with self.assertRaises(ValueError):
            selection.cyclic_tensor(np.nan)

    def test_historical_target_only_calibrates_the_required_projection(self):
        result = selection.evaluate()["historical_target_condition_not_prediction"]
        phi = selection.stable_two_harmonic_phase(result["benchmark_required_lambda1_over_lambda2"], 1)
        self.assertAlmostEqual(phi, result["benchmark_inverted_phase_radians"])
        self.assertTrue(result["masses_enter_only_this_diagnostic_not_selection_functions"])

    def test_minimal_one_excitation_trimer_does_not_select_an_intermediate_phase(self):
        result = selection.trimer_ground_state_check()
        self.assertAlmostEqual(result["analytic_ground_energy_derivative"], result["full_matrix_derivative"])
        self.assertLess(result["analytic_ground_energy_derivative"], 0)
        self.assertLess(result["endpoint_low_energies"][1], result["endpoint_low_energies"][0])
        self.assertTrue(result["not_the_native_quantum_vacuum"])

    def test_zero_probe_does_not_create_an_independent_tensor_potential(self):
        psi = np.zeros(3)
        for phi in [0, 0.4, 0.7]:
            self.assertAlmostEqual(np.vdot(psi, selection.cyclic_tensor(phi) @ psi).real, 0)
        result = selection.evaluate()["source_action_audit"]
        self.assertTrue(result["T_as_external_operator_has_no_independent_Euler_Lagrange_equation"])
        self.assertTrue(result["could_be_closed_by_T_as_evaluated_function_of_existing_fields"])

    def test_nonzero_fixed_probe_can_exert_a_state_dependent_phase_force(self):
        psi = np.array([1, 1j, 0])/math.sqrt(2)
        values = [np.vdot(psi, selection.cyclic_tensor(phi) @ psi).real for phi in [0.1, 0.5]]
        self.assertGreater(abs(values[0]-values[1]), 0.001)

    def test_common_residual_scale_does_not_determine_new_phase_or_mass_scale(self):
        r0, r1, g = np.array([-0.8, 0.2]), np.array([1, 0]), np.eye(2)
        before = selection.phase_penalty_selection(r0, r1, g)
        after = selection.phase_penalty_selection(7*r0, 7*r1, g)
        self.assertAlmostEqual(before["phase_radians"], after["phase_radians"])
        self.assertAlmostEqual(after["minimum_penalty"], 49*before["minimum_penalty"])

    def test_saved_phase_derivation_matches_evaluation(self):
        report = json.loads((ROOT / "analysis/Phase_Selection_Derivation.json").read_text(encoding="utf-8"))
        self.assertEqual(report, selection.evaluate())


class MinimalNativeHCSubstitutionTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def test_general_nonhermitian_native_blocks_give_the_gram_identity(self):
        rng = np.random.default_rng(52)
        m = rng.normal(size=(5, 5))+1j*rng.normal(size=(5, 5))
        p = np.diag([1, 1, 0, 0, 0])
        f, g = m[:2, 2:], m[2:, :2]
        expected = np.zeros((5, 5), dtype=complex)
        expected[:2, :2], expected[2:, 2:] = g.conj().T @ g, f.conj().T @ f
        self.assertClose(selection.minimal_native_closure(m, p, 0.2, 0.8), expected)

    def test_native_identity_is_covariant_under_a_unitary_chart(self):
        rng = np.random.default_rng(53)
        m, p, closure, _ = selection.native_cyclic_closure(0.4)
        u, _ = np.linalg.qr(rng.normal(size=m.shape)+1j*rng.normal(size=m.shape))
        self.assertClose(selection.minimal_native_closure(u @ m @ u.conj().T, u @ p @ u.conj().T),
                         u @ closure @ u.conj().T)

    def test_exact_native_closure_has_zero_minimal_compensator(self):
        m, p = np.diag([1, 2, 3, 4, 5]), np.diag([1, 1, 0, 0, 0])
        self.assertClose(selection.minimal_native_closure(m, p), np.zeros((5, 5)))

    def test_two_source_coefficients_only_enter_through_their_sum(self):
        m, p, _, _ = selection.native_cyclic_closure(0.4)
        self.assertClose(selection.minimal_native_closure(m, p, 0.3, 0.7),
                         selection.minimal_native_closure(m, p, 0.8, 0.2))

    def test_minimal_compensator_is_positive_and_block_preserving(self):
        m, p, closure, _ = selection.native_cyclic_closure(0.4)
        self.assertGreater(np.linalg.eigvalsh(closure)[0], 0)
        self.assertClose(closure @ p-p @ closure, np.zeros_like(closure))
        self.assertGreater(np.linalg.norm(m @ p-p @ m), 1)

    def test_conditional_cyclic_bridge_evaluates_to_two_Q_blocks(self):
        phi, s, rho, sigma = 0.4, 0.7, 0.2, 0.9
        _, _, closure, _ = selection.native_cyclic_closure(phi, s, rho, sigma)
        b = selection.cyclic_tensor(phi)
        q, zero = b.conj().T @ b, np.zeros_like(b)
        self.assertClose(closure, (rho+sigma)*s*s*np.block([[q, zero], [zero, q]]))

    def test_native_cyclic_derivative_matches_direct_substitution(self):
        phi, eps = 0.4, 1e-5
        derivative = selection.native_cyclic_closure(phi, 0.7)[3]
        plus = selection.native_cyclic_closure(phi+eps, 0.7)[2]
        minus = selection.native_cyclic_closure(phi-eps, 0.7)[2]
        self.assertClose(derivative, (plus-minus)/(2*eps), atol=2e-11)

    def test_cyclic_Q_has_the_explicit_first_and_second_theta_harmonics(self):
        a, r = 1/math.sqrt(6), 1/math.sqrt(12)
        u = np.roll(np.eye(3), 1, axis=0)
        for phi in [-0.5, 0, 0.5]:
            theta = (2*math.pi+phi)/3
            c = 2*a*r*np.exp(1j*theta)+r*r*np.exp(-2j*theta)
            q = (a*a+2*r*r)*np.eye(3)+c*u+c.conjugate()*u.T
            b = selection.cyclic_tensor(phi)
            self.assertClose(q, b.conj().T @ b)

    def test_native_matrix_residual_is_not_the_assumed_affine_cosine(self):
        positive = selection.native_cyclic_closure(0.4)[2]
        negative = selection.native_cyclic_closure(-0.4)[2]
        # Equal cos(Phi), different matrices in this fixed generation chart.
        self.assertGreater(np.linalg.norm(positive-negative), 0.01)

    def test_native_quartic_trace_contains_only_the_first_loop_harmonic(self):
        for phi in np.linspace(-math.pi, math.pi, 17):
            b = selection.cyclic_tensor(phi)
            self.assertAlmostEqual(np.trace(np.linalg.matrix_power(b, 4)).real,
                                   17/24+math.sqrt(2)*math.cos(phi)/6)

    def test_frozen_isotropic_H_cannot_select_a_strict_interior_phase(self):
        hp, hq, t, penalty = 0.2, 0.3, 0.7, 1.3
        h = np.diag([hp]*3+[hq]*3)
        values = []
        for phi in np.linspace(0, math.pi/4, 21):
            closure = selection.native_cyclic_closure(phi, math.sqrt(t))[2]
            actual = penalty*np.linalg.norm(h-closure, "fro")**2
            expected = penalty*(3*(hp*hp+hq*hq)-2*t*(hp+hq)
                                +2*t*t*(17/24+math.sqrt(2)*math.cos(phi)/6))
            self.assertAlmostEqual(actual, expected)
            values.append(actual)
        self.assertTrue(all(left > right for left, right in zip(values, values[1:])))

    def test_self_consistent_matching_penalty_is_zero_at_every_phase(self):
        for phi in np.linspace(-math.pi/4, math.pi/4, 17):
            closure = selection.native_cyclic_closure(phi)[2]
            h, residual, energy = selection.relaxed_hc(closure, np.zeros_like(closure))
            self.assertClose(h, closure)
            self.assertAlmostEqual(np.linalg.norm(residual), 0)
            self.assertAlmostEqual(energy, 0)

    def test_frozen_curvature_cancels_when_H_is_eliminated(self):
        result = selection.native_hc_phase_audit()["source_free_relaxation_check"]
        self.assertGreater(result["frozen_H_second_derivative_at_match"], 0.01)
        self.assertAlmostEqual(result["frozen_H_second_derivative_at_match"],
                               result["elimination_Hessian_subtraction"])
        self.assertAlmostEqual(result["relaxed_second_derivative"], 0)
        phi, eps = 0.5, 1e-4
        h = selection.native_cyclic_closure(phi)[2]
        frozen = [np.linalg.norm(h-selection.native_cyclic_closure(phi+s)[2], "fro")**2
                  for s in [-eps, 0, eps]]
        self.assertAlmostEqual((frozen[0]-2*frozen[1]+frozen[2])/eps**2,
                               result["frozen_H_second_derivative_at_match"], places=8)

    def test_constant_connection_curvature_variation_includes_the_H_source(self):
        rng = np.random.default_rng(54)
        def hermitian():
            x = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
            return (x+x.conj().T)/2
        h, dh, a0, a1 = (hermitian() for _ in range(4))
        kappa, n = 0.4, [1.0, -0.3]
        def connection(value):
            return [1j*a0+kappa*n[0]*value, 1j*a1+kappa*n[1]*value]
        def curvature(g):
            return [[x @ y-y @ x for y in g] for x in g]
        def action(value):
            f = curvature(connection(value))
            return -sum(np.trace(f[mu][nu] @ f[mu][nu]).real
                        for mu in range(2) for nu in range(2))/4
        g = connection(h)
        f = curvature(g)
        force = sum(kappa*n[nu]*(g[mu] @ f[mu][nu]-f[mu][nu] @ g[mu])
                    for mu in range(2) for nu in range(2))
        eps = 1e-5
        self.assertAlmostEqual(np.trace(force @ dh).real,
                               (action(h+eps*dh)-action(h-eps*dh))/(2*eps), places=8)

    def test_linear_source_elimination_solves_H_equation_and_energy(self):
        closure = selection.native_cyclic_closure(0.5)[2]
        j = -0.2*np.eye(6, dtype=complex)
        j[0, 1], j[1, 0] = 0.03j, -0.03j
        penalty = 0.7
        h, residual, energy = selection.relaxed_hc(closure, j, penalty)
        self.assertClose(2*penalty*residual+j, np.zeros_like(h))
        self.assertGreater(np.linalg.eigvalsh(h)[0], 0)
        self.assertAlmostEqual(energy, np.vdot(j, closure).real-np.vdot(j, j).real/(4*penalty))
        delta = np.diag([0.1, -0.2, 0.3, -0.1, 0.2, -0.3])
        moved = penalty*np.linalg.norm(h+delta-closure, "fro")**2+np.vdot(j, h+delta).real
        self.assertAlmostEqual(moved-energy, penalty*np.linalg.norm(delta, "fro")**2)

    def test_generation_resolved_source_phase_force_matches_the_effective_energy(self):
        phi, eps, t = 0.4, 1e-5, 0.7
        j = -0.2*np.eye(6, dtype=complex)
        j[0, 1], j[1, 0] = 0.03+0.04j, 0.03-0.04j
        u = np.roll(np.eye(3), 1, axis=0)
        scalar = np.trace((j[:3, :3]+j[3:, 3:]) @ u)
        a, r, theta = 1/math.sqrt(6), 1/math.sqrt(12), (2*math.pi+phi)/3
        force = -(4*t/3)*(scalar*(a*r*np.exp(1j*theta)-r*r*np.exp(-2j*theta))).imag
        def energy(p):
            closure = selection.native_cyclic_closure(p, math.sqrt(t))[2]
            return selection.relaxed_hc(closure, j)[2]
        self.assertGreater(abs(force), 0.001)
        self.assertAlmostEqual(force, (energy(phi+eps)-energy(phi-eps))/(2*eps), places=9)

    def test_isotropic_block_source_does_not_select_a_phase(self):
        j = np.diag([-0.2]*3+[-0.4]*3)
        values = [selection.relaxed_hc(selection.native_cyclic_closure(p)[2], j)[2]
                  for p in [0.1, 0.4, 0.7]]
        self.assertClose(values, np.full(3, values[0]))

    def test_joint_unitary_transport_preserves_the_source_elimination(self):
        rng = np.random.default_rng(55)
        closure = selection.native_cyclic_closure(0.4)[2]
        j = -0.2*np.eye(6, dtype=complex)
        j[0, 1], j[1, 0] = 0.03+0.04j, 0.03-0.04j
        u, _ = np.linalg.qr(rng.normal(size=j.shape)+1j*rng.normal(size=j.shape))
        h, _, energy = selection.relaxed_hc(closure, j)
        transported, _, after = selection.relaxed_hc(u @ closure @ u.conj().T,
                                                    u @ j @ u.conj().T)
        self.assertClose(transported, u @ h @ u.conj().T)
        self.assertAlmostEqual(energy, after)

    def test_diagonal_generation_source_is_also_blind_in_this_cyclic_chart(self):
        j = np.diag([-0.1, -0.2, -0.3, -0.4, -0.5, -0.6])
        values = [selection.relaxed_hc(selection.native_cyclic_closure(p)[2], j)[2]
                  for p in [0.1, 0.4, 0.7]]
        self.assertClose(values, np.full(3, values[0]))

    def test_matching_H_is_not_stationary_with_an_uncancelled_source(self):
        closure = selection.native_cyclic_closure(0.5)[2]
        j, eps = -0.2*np.eye(6), 1e-5
        def energy(h):
            return np.linalg.norm(h-closure, "fro")**2+np.vdot(j, h).real
        derivative = (energy(closure+eps*j)-energy(closure-eps*j))/(2*eps)
        self.assertAlmostEqual(derivative, np.vdot(j, j).real)
        self.assertGreater(derivative, 0)

    def test_native_functions_reject_incompatible_or_unlicensed_data(self):
        for m, p, rho, sigma in [(np.eye(2), np.eye(3), 1, 1),
                                  (np.eye(2), np.diag([1, 0.5]), 1, 1),
                                  (np.eye(2), [[1, 1], [0, 0]], 1, 1),
                                  (np.eye(2), np.eye(2), -1, 1),
                                  (np.eye(2), np.eye(2), 1, np.nan),
                                  ([], [], 1, 1)]:
            with self.subTest(m=m, p=p), self.assertRaises(ValueError):
                selection.minimal_native_closure(m, p, rho, sigma)
        for closure, source, penalty in [(np.eye(2), np.eye(3), 1),
                                         (np.eye(2), [[0, 1], [0, 0]], 1),
                                         (np.eye(2), np.eye(2), 0),
                                         (np.eye(2), np.eye(2), np.inf)]:
            with self.subTest(penalty=penalty), self.assertRaises(ValueError):
                selection.relaxed_hc(closure, source, penalty)
        with self.assertRaises(ValueError):
            selection.native_cyclic_closure(0.4, bridge_scale=0)

    def test_explicit_native_audit_uses_no_historical_mass_input(self):
        before = selection.native_hc_phase_audit()
        with patch.object(selection.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(before, selection.native_hc_phase_audit())
        self.assertTrue(before["affine_cosine_matrix_residual_not_derived"])
        self.assertTrue(before["other_action_terms"]["H_equals_Lambda_requires_other_H_forces_to_cancel"])
