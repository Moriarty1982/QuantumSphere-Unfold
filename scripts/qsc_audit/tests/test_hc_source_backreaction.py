"""Source coherence and positive-cone phase selection retain their model boundary."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "hc_source", ROOT / "analysis/HC_Source_Backreaction.py")
hc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hc)


class HCSourceBackreactionTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def test_spin_source_reproduces_the_real_bilinear_variation(self):
        rng = np.random.default_rng(61)
        psi = rng.normal(size=(3, 2))+1j*rng.normal(size=(3, 2))
        c = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
        delta = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
        delta = (delta+delta.conj().T)/2
        source = hc.spin_bilinear_source(psi, c)
        expected = np.vdot(psi.ravel(), np.kron(delta, c) @ psi.ravel()).real
        self.assertAlmostEqual(np.trace(source @ delta).real, expected)

    def test_source_is_the_hermitian_part_of_the_spin_partial_trace(self):
        psi = np.array([[1, 0.2j], [0.3, 0.4], [-0.2j, 0.1]])
        c = np.array([[0.2j, 0.4], [0.3j, 1]])
        raw = np.array([[sum(c[s, t]*psi[i, t]*psi[j, s].conjugate()
                             for s in range(2) for t in range(2))
                         for j in range(3)] for i in range(3)])
        self.assertClose(hc.spin_bilinear_source(psi, c), (raw+raw.conj().T)/2)

    def test_spin_source_transforms_with_the_generation_chart(self):
        rng = np.random.default_rng(62)
        psi = rng.normal(size=(3, 2))+1j*rng.normal(size=(3, 2))
        v, _ = np.linalg.qr(rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)))
        c = np.diag([1, -1])
        self.assertClose(hc.spin_bilinear_source(v.conj().T @ psi, c),
                         v.conj().T @ hc.spin_bilinear_source(psi, c) @ v)

    def test_identical_scalar_currents_need_not_fix_cycle_coherence(self):
        report = hc.evaluate()["same_scalar_current_different_coherence_witness"]
        self.assertClose(report["scalar_bilinears"], [1, 1])
        self.assertClose(report["cycle_source_coherences"], [0, 1])

    def test_equal_generation_density_has_zero_cycle_source(self):
        source = hc.spin_bilinear_source(np.eye(3), np.eye(3))
        self.assertClose(source, np.eye(3))
        self.assertAlmostEqual(np.trace(source @ hc.U), 0)

    def test_spin_source_rejects_bad_shapes_and_nonfinite_data(self):
        for psi, c in [([], np.eye(2)), ([[1, 2]], np.eye(3)),
                       ([[np.nan, 0]], np.eye(2)), ([[1, 0]], [1, 2])]:
            with self.subTest(psi=psi), self.assertRaises(ValueError):
                hc.spin_bilinear_source(psi, c)

    def test_selfconsistent_density_term_does_not_change_its_own_commutator(self):
        q, _ = hc.cyclic_gram_and_derivative(0.4)
        rho = np.diag([1, 0.3, 0.1])
        self.assertClose(hc.selfconsistent_source_rhs(rho, q, 0.7, 0.4),
                         -0.7j*(q @ rho-rho @ q))

    def test_circulant_coupling_preserves_the_needed_coherence(self):
        q, _ = hc.cyclic_gram_and_derivative(0.4)
        rho = np.array([[0.6, 0.1j, 0], [-0.1j, 0.3, 0], [0, 0, 0.1]])
        derivative = hc.selfconsistent_source_rhs(rho, q)
        self.assertClose(np.trace(derivative @ hc.U), 0)
        self.assertAlmostEqual(np.trace(derivative).real, 0)
        self.assertAlmostEqual(np.trace(rho @ derivative).real, 0)

    def test_zero_cycle_coherence_can_coexist_with_growing_local_coherence(self):
        q, _ = hc.cyclic_gram_and_derivative(0.4)
        values, vectors = np.linalg.eigh(q)
        transport = (vectors*np.exp(-1j*values*0.8)) @ vectors.conj().T
        rho = transport @ np.diag([1, 0, 0]) @ transport.conj().T
        self.assertGreater(np.linalg.norm(rho-np.diag(np.diag(rho))), 0.1)
        self.assertClose(np.trace(rho @ hc.U), 0)

    def test_equal_density_is_a_stationary_mean_field_state(self):
        q, _ = hc.cyclic_gram_and_derivative(0.4)
        self.assertClose(hc.selfconsistent_source_rhs(np.eye(3), q), np.zeros((3, 3)))

    def test_noncirculant_interaction_can_supply_a_cycle_torque(self):
        rho = np.diag([1, 0, 0]).astype(complex)
        interaction = np.zeros((3, 3), dtype=complex)
        interaction[0, 1], interaction[1, 0] = 0.2j, -0.2j
        derivative = -1j*(interaction @ rho-rho @ interaction)
        self.assertGreater(abs(np.trace(derivative @ hc.U)), 0.1)

    def test_mean_field_rejects_unlicensed_data(self):
        for rho, q, g, penalty in [(np.diag([-1, 1]), np.eye(2), 1, 1),
                                   (np.eye(2), np.eye(3), 1, 1),
                                   (np.eye(2), np.eye(2), np.nan, 1),
                                   (np.eye(2), np.eye(2), 1, 0)]:
            with self.subTest(g=g, penalty=penalty), self.assertRaises(ValueError):
                hc.selfconsistent_source_rhs(rho, q, g, penalty)

    def test_general_noncommuting_positive_cone_solution_satisfies_KKT(self):
        closure = np.array([[0.1, 0.03j], [-0.03j, 0.8]])
        source = np.array([[0.4, 0.1], [0.1, 0.2]])
        self.assertGreater(np.linalg.norm(closure @ source-source @ closure), 0.01)
        h, slack, _ = hc.positive_hc_minimum(closure, source, 0.7)
        self.assertGreaterEqual(np.linalg.eigvalsh(h)[0], -1e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(slack)[0], -1e-12)
        self.assertClose(h @ slack, np.zeros_like(h))
        self.assertClose(2*0.7*(h-closure)+source-slack, np.zeros_like(h))

    def test_positive_projection_is_better_than_random_positive_competitors(self):
        closure, _ = hc.cyclic_gram_and_derivative(0.4)
        source, penalty = 0.1*np.eye(3), 0.7
        _, _, energy = hc.positive_hc_minimum(closure, source, penalty)
        rng = np.random.default_rng(63)
        for _ in range(40):
            x = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
            h = x @ x.conj().T/10
            competitor = penalty*np.linalg.norm(h-closure, "fro")**2+np.trace(source @ h).real
            self.assertLessEqual(energy, competitor+1e-12)

    def test_interior_positive_solution_matches_unconstrained_elimination(self):
        closure = np.diag([0.3, 0.8])
        source = 0.1*np.eye(2)
        h, slack, energy = hc.positive_hc_minimum(closure, source)
        old_h, _, old_energy = hc.phase.relaxed_hc(closure, source)
        self.assertClose(h, old_h)
        self.assertClose(slack, np.zeros_like(slack))
        self.assertAlmostEqual(energy, old_energy)

    def test_zero_source_recovers_the_zero_matching_penalty(self):
        closure, _ = hc.cyclic_gram_and_derivative(0.4)
        h, slack, energy = hc.positive_hc_minimum(closure, np.zeros_like(closure))
        self.assertClose(h, closure)
        self.assertClose(slack, np.zeros_like(slack))
        self.assertAlmostEqual(energy, 0)

    def test_isotropic_cone_solution_is_the_spectral_positive_part(self):
        q, _ = hc.cyclic_gram_and_derivative(0.4)
        h, _, _, _ = hc.symmetric_cone_energy(0.4, 0.05)
        self.assertClose(np.linalg.eigvalsh(h), np.maximum(np.linalg.eigvalsh(q)-0.05, 0))

    def test_piecewise_energy_and_derivative_match_direct_matrix_minimization(self):
        for phi in [0.1, 0.4, 0.7]:
            for k in [0.005, 0.05, 0.2, 1.1]:
                _, _, energy, derivative = hc.symmetric_cone_energy(phi, k)
                q = np.linalg.eigvalsh(hc.cyclic_gram_and_derivative(phi)[0])
                expected = np.where(q <= k, q*q, 2*k*q-k*k).sum()
                self.assertAlmostEqual(energy, expected)
                eps = 1e-5
                plus = hc.symmetric_cone_energy(phi+eps, k)[2]
                minus = hc.symmetric_cone_energy(phi-eps, k)[2]
                self.assertAlmostEqual(derivative, (plus-minus)/(2*eps), places=9)

    def test_positivity_changes_the_unconstrained_isotropic_flatness_result(self):
        unbounded, bounded = [], []
        for phi in [0.1, 0.4, 0.7]:
            q, _ = hc.cyclic_gram_and_derivative(phi)
            unbounded.append(hc.phase.relaxed_hc(q, 0.1*np.eye(3))[2])
            bounded.append(hc.symmetric_cone_energy(phi, 0.05)[2])
        self.assertClose(unbounded, np.full(3, unbounded[0]))
        self.assertGreater(np.ptp(bounded), 1e-4)

    def test_symmetric_source_phase_force_is_the_constraint_reaction(self):
        phi, k = 0.4, 0.05
        h, slack, _, derivative = hc.symmetric_cone_energy(phi, k)
        q, qp = hc.cyclic_gram_and_derivative(phi)
        self.assertAlmostEqual(np.trace(0.1*np.eye(3) @ qp).real, 0)
        self.assertAlmostEqual(derivative, -np.trace(slack @ qp).real)
        self.assertClose(h @ slack, np.zeros_like(h))

    def test_exact_threshold_endpoints_match_the_phase_law(self):
        self.assertAlmostEqual(hc.critical_threshold(0), hc.LOWER_THRESHOLD)
        self.assertAlmostEqual(hc.critical_threshold(math.pi/4), hc.UPPER_THRESHOLD)
        self.assertLess(hc.LOWER_THRESHOLD, hc.UPPER_THRESHOLD)

    def test_threshold_law_is_strictly_increasing_in_the_positive_chamber(self):
        phases = np.linspace(0, math.pi/4, 101)
        values = [hc.critical_threshold(phi) for phi in phases]
        self.assertTrue(all(a < b for a, b in zip(values, values[1:])))
        self.assertTrue(all(hc.critical_threshold_derivative(phi) > 0 for phi in phases[1:]))

    def test_computed_interior_phase_solves_the_stationarity_equation(self):
        for k in [0.045, 0.05, 0.06, 0.065]:
            result = hc.solve_positive_cone_phase(k)
            self.assertAlmostEqual(hc.critical_threshold(result["phase_radians"]), k)
            self.assertLess(abs(result["phase_force_per_lambda_t_squared"]), 1e-12)

    def test_interior_phase_curvature_is_positive_and_matches_energy(self):
        result = hc.solve_positive_cone_phase(0.05)
        phi, eps = result["phase_radians"], 1e-4
        values = [hc.symmetric_cone_energy(phi+d, 0.05)[2] for d in [-eps, 0, eps]]
        numerical = (values[0]-2*values[1]+values[2])/eps**2
        self.assertGreater(result["phase_curvature_per_lambda_t_squared"], 0)
        self.assertAlmostEqual(numerical, result["phase_curvature_per_lambda_t_squared"], places=7)

    def test_selected_phase_is_a_global_minimum_over_the_declared_chamber(self):
        for k in [0.045, 0.05, 0.06, 0.065]:
            result = hc.solve_positive_cone_phase(k)
            for phi in np.linspace(0, math.pi/4, 101):
                self.assertLessEqual(result["energy_per_lambda_t_squared"],
                                     hc.symmetric_cone_energy(phi, k)[2]+1e-12)

    def test_stationary_branch_really_has_two_clamped_modes(self):
        for phi in np.linspace(0.01, math.pi/4-0.01, 30):
            k = hc.critical_threshold(phi)
            q = np.linalg.eigvalsh(hc.cyclic_gram_and_derivative(phi)[0])
            self.assertLess(q[1], k)
            self.assertLess(k, q[2])

    def test_gram_has_three_positive_modes_but_compensator_has_only_one(self):
        result = hc.solve_positive_cone_phase(0.05)
        self.assertGreater(min(result["gram_eigenvalues"]), 0)
        hvalues = result["positive_compensator_eigenvalues_per_t"]
        self.assertEqual(sum(value > 1e-12 for value in hvalues), 1)
        self.assertEqual(result["compensator_rank"], 1)

    def test_conjugate_phases_have_identical_minimized_energy(self):
        result = hc.solve_positive_cone_phase(0.05)
        self.assertAlmostEqual(hc.symmetric_cone_energy(result["phase_radians"], 0.05)[2],
                               hc.symmetric_cone_energy(result["conjugate_phase_radians"], 0.05)[2])

    def test_only_the_dimensionless_threshold_selects_the_phase(self):
        result = hc.solve_positive_cone_phase(0.05)
        phi = result["phase_radians"]
        h, _, energy, derivative = hc.symmetric_cone_energy(phi, 0.05, scale=3, penalty=0.7)
        self.assertAlmostEqual(energy, 0.7*9*result["energy_per_lambda_t_squared"])
        self.assertLess(abs(derivative), 1e-12)
        self.assertClose(np.linalg.eigvalsh(h), 3*np.array(result["positive_compensator_eigenvalues_per_t"]))

    def test_phase_solver_rejects_boundaries_and_outside_thresholds(self):
        for k in [0, hc.LOWER_THRESHOLD, hc.UPPER_THRESHOLD, 0.2, np.nan, np.inf]:
            with self.subTest(k=k), self.assertRaises(ValueError):
                hc.solve_positive_cone_phase(k)

    def test_cone_reductions_reject_incompatible_parameters(self):
        for phi, k, scale, penalty in [(1, 0.05, 1, 1), (0.4, -0.1, 1, 1),
                                       (0.4, 0.05, 0, 1), (0.4, 0.05, 1, -1)]:
            with self.subTest(phi=phi, k=k), self.assertRaises(ValueError):
                hc.symmetric_cone_energy(phi, k, scale, penalty)
        with self.assertRaises(ValueError):
            hc.positive_hc_minimum(np.eye(2), [[1, 1], [0, 1]])
        for phi in [-0.1, np.nan, math.pi/4+0.01]:
            with self.subTest(phi=phi), self.assertRaises(ValueError):
                hc.critical_threshold(phi)

    def test_historical_inputs_do_not_enter_the_source_or_threshold_calculation(self):
        before = hc.evaluate()
        with patch.object(hc.phase.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(hc.evaluate(), before)
        report = before["positive_cone_model"]
        self.assertTrue(report["requires_independent_positive_H_instead_of_exact_H_equals_Lambda"])
        self.assertFalse(before["historical_masses_or_target_phase_used"])

    def test_positive_cone_solution_does_not_satisfy_exact_matching(self):
        result = hc.solve_positive_cone_phase(0.05)
        self.assertGreater(result["matching_residual_norm_per_t"], 0.01)

    def test_saved_source_report_reproduces_the_calculation(self):
        saved = json.loads((ROOT / "analysis/HC_Source_Backreaction.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, hc.evaluate())


class HCRadiusAndClosureTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def selected(self):
        result = hc.solve_positive_cone_phase(0.05)
        q, _ = hc.cyclic_gram_and_derivative(result["phase_radians"])
        return result, q

    def test_variable_radius_preserves_cyclic_positive_unit_normalization(self):
        for ratio in [0, 0.3, 0.5, 1/math.sqrt(2)]:
            b = hc.cyclic_root_with_radius(0.4, ratio)
            self.assertClose(b, b.conj().T)
            self.assertGreaterEqual(np.linalg.eigvalsh(b)[0], 0)
            self.assertAlmostEqual(np.linalg.norm(b, "fro"), 1)
            self.assertClose(b @ hc.U-hc.U @ b, np.zeros_like(b))

    def test_original_root_is_the_fixed_radius_slice(self):
        for phi in [0, 0.4, 0.7]:
            self.assertClose(hc.cyclic_root_with_radius(phi, 1/math.sqrt(2)),
                             hc.phase.cyclic_tensor(phi))

    def test_analytic_radial_force_matches_finite_difference(self):
        result, _ = self.selected()
        phi, s, eps = result["phase_radians"], 1/math.sqrt(2), 1e-5
        _, derivative = hc.radius_energy_and_derivative(phi, s, 0.05)
        plus = hc.radius_energy_and_derivative(phi, s+eps, 0.05)[0]
        minus = hc.radius_energy_and_derivative(phi, s-eps, 0.05)[0]
        self.assertAlmostEqual(derivative, (plus-minus)/(2*eps), places=9)

    def test_fixed_phase_minimum_has_a_pure_radius_descent_direction(self):
        result, _ = self.selected()
        phi, s = result["phase_radians"], 1/math.sqrt(2)
        old, derivative = hc.radius_energy_and_derivative(phi, s, 0.05)
        shifted = hc.radius_energy_and_derivative(phi, s-0.001, 0.05)[0]
        self.assertGreater(derivative, 0.007)
        self.assertLess(shifted, old)

    def test_mixing_descent_stays_inside_the_positive_cyclic_gram_class(self):
        _, q = self.selected()
        for eps in [0, 0.05, 0.2, 1]:
            mixed = hc.mix_toward_equal_modes(q, eps)
            self.assertAlmostEqual(np.trace(mixed).real, 1)
            self.assertGreater(np.linalg.eigvalsh(mixed)[0], 0)
            self.assertClose(mixed @ hc.U-hc.U @ mixed, np.zeros_like(q))

    def test_descent_has_a_positive_cyclic_root_with_no_norm_change(self):
        _, q = self.selected()
        mixed = hc.mix_toward_equal_modes(q, 0.2)
        b = hc.positive_root(mixed)
        self.assertClose(b @ b, mixed)
        self.assertAlmostEqual(np.linalg.norm(b, "fro"), 1)
        a, z = np.trace(b).real/3, np.trace(hc.U.conj().T @ b)/3
        self.assertClose(b, a*np.eye(3)+z*hc.U+z.conjugate()*hc.U.T)

    def test_trace_energy_identity_is_exact_for_each_spectral_active_set(self):
        q = np.diag([0.01, 0.2, 0.79])
        values = np.diag(q)
        for k in [0.005, 0.05, 0.3, 0.8, 1.1]:
            _, _, energy = hc.positive_hc_minimum(q, 2*k*np.eye(3))
            expected = 2*k-3*k*k+np.maximum(k-values, 0) @ np.maximum(k-values, 0)
            self.assertAlmostEqual(energy, expected)

    def test_nonuniform_global_plateau_does_not_select_a_unique_shape(self):
        k = 0.05
        for values in [[0.1, 0.3, 0.6], [0.2, 0.3, 0.5], [1/3]*3]:
            _, _, energy = hc.positive_hc_minimum(np.diag(values), 2*k*np.eye(3))
            self.assertAlmostEqual(energy, hc.fixed_trace_minimum(k))

    def test_global_trace_bound_for_arbitrary_positive_spectra(self):
        rng = np.random.default_rng(64)
        for k in [0.01, 0.05, 1/3, 0.4, 1.1]:
            for _ in range(15):
                values = rng.dirichlet(np.ones(3))
                energy = hc.positive_hc_minimum(np.diag(values), 2*k*np.eye(3))[2]
                self.assertGreaterEqual(energy+1e-12, hc.fixed_trace_minimum(k))

    def test_at_or_above_one_third_equal_modes_are_the_unique_trace_minimum(self):
        for k in [1/3, 0.4, 1.1]:
            equal_energy = hc.positive_hc_minimum(np.eye(3)/3, 2*k*np.eye(3))[2]
            unequal_energy = hc.positive_hc_minimum(np.diag([0.1, 0.3, 0.6]), 2*k*np.eye(3))[2]
            self.assertAlmostEqual(equal_energy, 1/3)
            self.assertGreater(unequal_energy, equal_energy)

    def test_shape_descent_slope_matches_the_matrix_energy(self):
        _, q = self.selected()
        report = hc.radius_and_closure_audit()["radius_relaxation"]
        eps = 1e-4
        energy = hc.positive_hc_minimum(q, 0.1*np.eye(3))[2]
        moved = hc.positive_hc_minimum(hc.mix_toward_equal_modes(q, eps), 0.1*np.eye(3))[2]
        twice = hc.positive_hc_minimum(hc.mix_toward_equal_modes(q, 2*eps), 0.1*np.eye(3))[2]
        self.assertAlmostEqual((-3*energy+4*moved-twice)/(2*eps),
                               report["mixing_descent_derivative"], places=9)
        self.assertLess(report["mixing_descent_derivative"], 0)

    def test_shape_path_decreases_until_it_reaches_the_global_plateau(self):
        _, q = self.selected()
        energies = [hc.positive_hc_minimum(hc.mix_toward_equal_modes(q, eps), 0.1*np.eye(3))[2]
                    for eps in np.linspace(0, 0.3, 21)]
        self.assertTrue(all(a >= b-1e-12 for a, b in zip(energies, energies[1:])))
        self.assertAlmostEqual(energies[-1], hc.fixed_trace_minimum(0.05))

    def test_first_global_plateau_fraction_is_the_smallest_deficit_crossing(self):
        _, q = self.selected()
        fraction = hc.radius_and_closure_audit()["radius_relaxation"]["minimum_mixing_fraction_for_global_plateau"]
        before = hc.mix_toward_equal_modes(q, fraction-1e-3)
        at = hc.mix_toward_equal_modes(q, fraction)
        self.assertLess(np.linalg.eigvalsh(before)[0], 0.05)
        self.assertAlmostEqual(np.linalg.eigvalsh(at)[0], 0.05)
        self.assertAlmostEqual(hc.positive_hc_minimum(at, 0.1*np.eye(3))[2], hc.fixed_trace_minimum(0.05))

    def test_descent_releases_exactly_the_unproved_Koide_radius_condition(self):
        _, q = self.selected()
        original = hc.positive_root(q)
        mixed = hc.positive_root(hc.mix_toward_equal_modes(q, 0.2))
        self.assertAlmostEqual(1/np.trace(original).real**2, 2/3)
        self.assertLess(1/np.trace(mixed).real**2, 2/3)
        a, z = np.trace(mixed).real/3, np.trace(hc.U.conj().T @ mixed)/3
        self.assertAlmostEqual(1/np.trace(mixed).real**2, (1+2*(abs(z)/a)**2)/3)

    def test_scale_derivative_holds_g_fixed_rather_than_threshold(self):
        _, q = self.selected()
        eps = 1e-5
        _, derivative = hc.scale_energy_and_derivative(q, 1, 0.1, 0.7)
        plus = hc.scale_energy_and_derivative(q, 1+eps, 0.1, 0.7)[0]
        minus = hc.scale_energy_and_derivative(q, 1-eps, 0.1, 0.7)[0]
        self.assertAlmostEqual(derivative, (plus-minus)/(2*eps), places=9)

    def test_free_scale_energy_has_no_nonzero_stationary_point(self):
        _, q = self.selected()
        scales = [0.01, 0.1, 0.5, 1, 2]
        results = [hc.scale_energy_and_derivative(q, scale) for scale in scales]
        self.assertTrue(all(derivative > 0 for _, derivative in results))
        self.assertTrue(all(a[0] < b[0] for a, b in zip(results, results[1:])))

    def test_zero_scale_is_the_global_zero_energy_endpoint(self):
        _, q = self.selected()
        energy, derivative = hc.scale_energy_and_derivative(q, 0)
        self.assertAlmostEqual(energy, 0)
        self.assertAlmostEqual(derivative, 0)

    def test_field_units_preserve_energy_and_the_selecting_ratio(self):
        _, q = self.selected()
        source, c = 0.1*np.eye(3), 3.7
        h, _, energy = hc.positive_hc_minimum(q, source)
        changed, _, after = hc.positive_hc_minimum(c*q, source/c, 1/c**2)
        self.assertClose(changed, c*h)
        self.assertAlmostEqual(after, energy)
        self.assertAlmostEqual((0.1/c)/(2*(1/c**2)*c), 0.05)

    def test_stiff_matching_limit_leaves_the_interior_selection_interval(self):
        penalty, g = 1e5, 0.1
        k = g/(2*penalty)
        self.assertLess(k, hc.LOWER_THRESHOLD)
        energies = []
        for phi in [0.2, 0.4, 0.6]:
            q, qp = hc.cyclic_gram_and_derivative(phi)
            h, slack, energy = hc.positive_hc_minimum(q, g*np.eye(3), penalty)
            self.assertGreater(np.linalg.eigvalsh(h)[0], 0)
            self.assertClose(slack, np.zeros_like(slack), atol=1e-10)
            self.assertLess(abs(-2*penalty*np.vdot(h-q, qp).real), 1e-10)
            energies.append(energy)
        self.assertClose(energies, np.full(3, energies[0]))

    def test_phase_selection_requires_a_finite_relative_matching_residual(self):
        for k in [0.045, 0.05, 0.06, 0.065]:
            result = hc.solve_positive_cone_phase(k)
            phi = result["phase_radians"]
            q, _ = hc.cyclic_gram_and_derivative(phi)
            h = hc.symmetric_cone_energy(phi, k)[0]
            self.assertGreater(np.linalg.norm(h-q)/np.linalg.norm(q), hc.LOWER_THRESHOLD)

    def test_zero_positive_compression_removes_cross_action_not_the_hidden_core(self):
        h = np.diag([0, 0, 0, 1, 2])
        s = np.eye(5)[:, :3]
        self.assertClose(s.conj().T @ h @ s, np.zeros((3, 3)))
        self.assertClose(h @ s, np.zeros((5, 3)))
        self.assertGreater(np.linalg.norm(h), 0)
        # A zero positive diagonal cannot coexist with a nonzero cross entry.
        self.assertLess(np.linalg.eigvalsh([[0, 0.1], [0.1, 1]])[0], 0)

    def test_zero_mismatch_readout_still_allows_an_internal_positive_core(self):
        _, q = self.selected()
        h = np.block([[q, np.zeros((3, 2))], [np.zeros((2, 3)), np.eye(2)]])
        p = np.diag([1, 1, 1, 0, 0])
        self.assertClose(h @ p-p @ h, np.zeros_like(h))
        self.assertGreater(np.linalg.norm(p @ h @ p), 0)
        self.assertClose(hc.phase.minimal_native_closure(h, p), np.zeros_like(h))

    def test_deeper_generator_source_is_explicitly_hypothesis_grade(self):
        source = (ROOT / "sources/research/parts/v470/13_hc_hypotheses.tex").read_text(encoding="utf-8")
        self.assertIn(r"\label{hyp:frame-dependent-defect-readout}", source)
        self.assertIn("Hypothesis-grade; not yet theorem-level.", source)
        report = hc.radius_and_closure_audit()["source_boundary"]
        self.assertTrue(report["native_readout_map_is_not_evaluated"])

    def test_radius_scale_and_mixing_guards_reject_invalid_inputs(self):
        for phi, s in [(np.nan, 0.5), (0.4, -1), (0.4, np.inf), (0, 1.1)]:
            with self.subTest(phi=phi, s=s), self.assertRaises(ValueError):
                hc.cyclic_root_with_radius(phi, s)
        for q, eps in [(np.eye(3), 0.1), (np.diag([-0.1, 0.3, 0.8]), 0.1),
                       (np.eye(3)/3, -0.1), (np.eye(3)/3, 1.1)]:
            with self.subTest(eps=eps), self.assertRaises(ValueError):
                hc.mix_toward_equal_modes(q, eps)
        for scale, coupling in [(-1, 0.1), (1, 0), (1, np.nan)]:
            with self.subTest(scale=scale), self.assertRaises(ValueError):
                hc.scale_energy_and_derivative(np.eye(3)/3, scale, coupling)
        with self.assertRaises(ValueError):
            hc.positive_root(np.diag([-1, 1]))
        with self.assertRaises(ValueError):
            hc.fixed_trace_minimum(0)
