"""Exact triadic reduction and invariant phases, with native-data guards."""
from pathlib import Path
import importlib.util
import json
import math
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "triadic_candidate", ROOT / "analysis/Coupling_Scale_Candidate.py")
candidate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(candidate)


class TriadicPropagatorTests(unittest.TestCase):
    def setUp(self):
        self.a1 = np.diag([0.2, 0.4])
        self.a2 = np.array([[0.7]])
        self.c = np.array([[0.12], [0.07j]])
        self.w1 = np.array([[0.1, 0.2j], [0.03, 0.1]])
        self.w2 = np.array([[0.12j], [0.14]])
        self.d = np.array([[3, 0.1j], [-0.1j, 4]])

    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def reduce(self, energy=0):
        return candidate.triadic_response(self.a1, self.a2, self.c,
                                          self.w1, self.w2, self.d, energy)

    def test_all_four_reduced_blocks_and_norm_use_the_same_resolvent(self):
        energy = 0.15
        effective, norm, response = self.reduce(energy)
        r = np.linalg.inv(self.d-energy*np.eye(2))
        n11 = self.w1.conj().T @ r @ self.w1
        n12 = self.w1.conj().T @ r @ self.w2
        n22 = self.w2.conj().T @ r @ self.w2
        self.assertClose(effective[:2, :2], self.a1-n11)
        self.assertClose(effective[:2, 2:], self.c-n12)
        self.assertClose(effective[2:, :2], (self.c-n12).conj().T)
        self.assertClose(effective[2:, 2:], self.a2-n22)
        w = np.hstack([self.w1, self.w2])
        self.assertClose(response, w.conj().T @ r @ w)
        self.assertClose(norm, w.conj().T @ r @ r @ w)

    def test_full_scalar_triad_poles_obey_energy_dependent_reduction(self):
        report = candidate.triadic_propagator_diagnosis()["exact_pole_test_arbitrary_energy_units"]
        self.assertLess(max(report["low_pole_schur_residuals"]), 2e-12)
        self.assertTrue(report["not_a_charged_lepton_prediction"])

    def test_noncommuting_matrix_blocks_reproduce_low_poles_and_norms(self):
        direct = np.block([[self.a1, self.c], [self.c.conj().T, self.a2]])
        w = np.hstack([self.w1, self.w2])
        full = np.block([[direct, w.conj().T], [w, self.d]])
        energies, vectors = np.linalg.eigh(full)
        for i in range(3):
            x = vectors[:3, i]
            effective, norm, _ = self.reduce(energies[i])
            self.assertClose(effective @ x, energies[i]*x)
            self.assertClose(np.vdot(x, (np.eye(3)+norm) @ x), 1)

    def test_cross_response_obeys_cauchy_schwarz_for_probe_vectors(self):
        _, _, n = self.reduce()
        for x, y in [(np.array([1, 1j]), np.array([0.3j])),
                     (np.array([0.2j, 1]), np.array([1]))]:
            cross = np.vdot(x, n[:2, 2:] @ y)
            diagonal = (np.vdot(x, n[:2, :2] @ x)*np.vdot(y, n[2:, 2:] @ y)).real
            self.assertLessEqual(abs(cross)**2, diagonal+1e-14)

    def test_no_cross_response_if_one_mediator_link_is_zero(self):
        effective, _, n = candidate.triadic_response(
            self.a1, self.a2, self.c, np.zeros_like(self.w1), self.w2, self.d)
        self.assertClose(n[:2, 2:], np.zeros((2, 1)))
        self.assertClose(effective[:2, 2:], self.c)

    def test_off_diagonal_only_response_is_not_positive(self):
        fake_response = np.array([[0, 0.1j], [-0.1j, 0]])
        self.assertLess(np.linalg.eigvalsh(fake_response)[0], 0)

    def test_one_mediator_witness_rotates_link_with_mandatory_diagonal_shifts(self):
        witness = candidate.triadic_propagator_diagnosis()["phase_rotated_link_existence_witness"]
        self.assertAlmostEqual(witness["effective_link_real"], witness["target_link_real"])
        self.assertAlmostEqual(witness["effective_link_imag"], witness["target_link_imag"])
        self.assertGreater(min(witness["mandatory_diagonal_response"]), 0)
        self.assertAlmostEqual(witness["response_determinant_real"], 0)
        self.assertGreater(max(witness["mandatory_norm_response_eigenvalues"]), 0)

    def test_unequal_probe_dimensions_are_admissible_but_not_identified(self):
        effective, norm, _ = self.reduce()
        self.assertEqual(effective.shape, (3, 3))
        self.assertEqual(norm.shape, (3, 3))
        self.assertClose(effective, effective.conj().T)

    def test_malformed_and_nonhermitian_probe_blocks_rejected(self):
        defaults = [self.a1, self.a2, self.c, self.w1, self.w2, self.d]
        for index, bad in [(0, np.ones((2, 3))), (0, np.array([[1, 1j], [0, 1]])),
                           (1, np.zeros((0, 0))), (2, np.ones((1, 2))),
                           (3, np.ones((3, 2))), (4, np.ones((2, 2))),
                           (5, np.ones((2, 3))), (5, np.diag([-1, 2])),
                           (2, np.array([1, 2])), (2, np.full((2, 1), np.nan))]:
            values = defaults.copy()
            values[index] = bad
            with self.subTest(index=index, bad=bad), self.assertRaises(ValueError):
                candidate.triadic_response(*values)

    def test_energy_at_or_above_complementary_gap_rejected(self):
        with self.assertRaises(ValueError):
            self.reduce(np.linalg.eigvalsh(self.d)[0])
        with self.assertRaises(ValueError):
            self.reduce(5)

    def test_scalar_loop_phase_invariant_under_three_independent_rephasings(self):
        c, w1, w2 = 0.2*np.exp(0.4j), 0.15*np.exp(-0.1j), 0.12*np.exp(0.8j)
        phases = np.array([0.7, -0.3, 1.1])
        transformed = [c*np.exp(1j*(phases[1]-phases[0])),
                       w1*np.exp(1j*(phases[0]-phases[2])),
                       w2*np.exp(1j*(phases[1]-phases[2]))]
        self.assertAlmostEqual(candidate.triadic_loop_phase(*transformed),
                               candidate.triadic_loop_phase(c, w1, w2))

    def test_scalar_loop_phase_undefined_when_any_edge_is_absent(self):
        for edges in [(0, 1, 1), (1, 0, 1), (1, 1, 0), (np.inf, 1, 1), (1, np.nan, 1)]:
            with self.subTest(edges=edges), self.assertRaises(ValueError):
                candidate.triadic_loop_phase(*edges)

    def test_written_frame_values_do_not_make_a_loop_flux_by_rephasing(self):
        result = candidate.triadic_propagator_diagnosis()["independent_frame_rephasing_test"]
        self.assertLess(result["maximum_eigenvalue_difference"], 2e-12)
        self.assertAlmostEqual(result["oriented_loop_phase_after_rephasing"], 0)
        self.assertTrue(result["not_a_source_derived_three_link_phase_law"])

    def test_real_hopping_magnitudes_can_have_different_physical_loop_phases(self):
        samples = candidate.triadic_propagator_diagnosis()["fixed_moduli_nontrivial_loop_examples"]
        determinants = [sample["determinant_real"] for sample in samples]
        self.assertGreater(np.ptp(determinants), 0.001)

    def test_scalar_determinant_exposes_only_the_invariant_loop_phase(self):
        e1, e2, d = 0.5, 0.9, 3
        c, w1, w2 = 0.2*np.exp(0.3j), 0.15*np.exp(-0.2j), 0.12*np.exp(0.7j)
        full = np.array([[e1, c, np.conj(w1)], [np.conj(c), e2, np.conj(w2)], [w1, w2, d]])
        phi = candidate.triadic_loop_phase(c, w1, w2)
        formula = (e1*e2*d-e1*abs(w2)**2-e2*abs(w1)**2-d*abs(c)**2
                   +2*abs(c*w1*w2)*math.cos(phi))
        self.assertAlmostEqual(np.linalg.det(full).real, formula)

    def test_cyclic_candidate_loop_is_three_times_the_coefficient_phase(self):
        theta, b, _ = candidate.cyclic_candidate()
        phi = candidate.triadic_loop_phase(b[0, 1], b[2, 0], b[2, 1])
        self.assertClose(np.exp(1j*phi), np.exp(3j*theta))
        result = candidate.triadic_propagator_diagnosis()["cyclic_root_loop_requirement"]
        self.assertAlmostEqual(result["benchmark_calibrated_loop_phase_change_degrees"], -0.441063334017)
        self.assertTrue(result["not_a_native_phase_prediction"])

    def test_scalar_phase_gauge_has_one_unfixed_cycle(self):
        c, w1, w2 = np.exp(0.2j), 0.1*np.exp(0.4j), 0.2*np.exp(0.7j)
        self.assertNotAlmostEqual(candidate.triadic_loop_phase(c, w1, w2),
                                  candidate.triadic_loop_phase(c, w1, w2*np.exp(0.3j)))

    def test_cyclic_symmetry_and_hermiticity_do_not_fix_the_phase(self):
        theta, b, _ = candidate.cyclic_candidate()
        alternative = candidate.normalized_cyclic_root(1/math.sqrt(2), theta-0.001)
        u = np.roll(np.eye(3), 1, axis=0)
        self.assertClose(alternative, alternative.conj().T)
        self.assertClose(alternative @ u, u @ alternative)
        self.assertGreater(np.linalg.eigvalsh(alternative)[0], 0)
        self.assertFalse(np.allclose(np.linalg.eigvalsh(b), np.linalg.eigvalsh(alternative)))

    def test_planck_mediator_with_electroweak_links_is_too_weak_in_declared_case(self):
        result = candidate.triadic_propagator_diagnosis()["conditional_planck_mediator_phase_bound"]
        self.assertLess(result["max_phase_change_radians_bound"], 1e-15)
        self.assertGreater(result["link_change_shortfall_factor"], 1e13)
        self.assertTrue(result["does_not_exclude_other_gaps_or_couplings"])

    def test_disk_bound_on_phase_of_a_perturbed_nonzero_link(self):
        c, radius = 0.2, 0.01
        for theta in np.linspace(0, 2*math.pi, 100):
            perturbed = c-radius*np.exp(1j*theta)
            self.assertLessEqual(abs(np.angle(perturbed/c)), math.asin(radius/c)+1e-12)

    def test_real_compensator_terms_are_not_automatically_internal_unitary_transport(self):
        a = np.array([[1, 0.1j], [-0.1j, 2]])
        hc, complement = np.diag([0, 0.3]), np.diag([0, 1])
        connection = 1j*a+0.2*hc+0.1*complement
        self.assertGreater(np.linalg.norm(connection+connection.conj().T), 0.1)
        self.assertClose(1j*a+(1j*a).conj().T, np.zeros((2, 2)))

    def test_flat_abelian_connection_has_trivial_contractible_loop_phase(self):
        vertices = np.array([[0, 0], [1, 0], [0.3, 0.8], [0, 0]])
        potentials = vertices @ np.array([0.2, -0.3])
        endpoint_phase_sum = np.diff(potentials).sum()
        self.assertAlmostEqual(endpoint_phase_sum, 0)

    def test_constant_abelian_curvature_gives_area_dependent_loop_phase(self):
        # a=(0,f*x), counterclockwise unit triangle; U_loop=exp(-i integral a).
        f = 0.3
        vertices = np.array([[0, 0], [1, 0], [0, 1], [0, 0]])
        integral = sum(f*(p[0]+q[0])/2*(q[1]-p[1]) for p, q in zip(vertices[:-1], vertices[1:]))
        self.assertAlmostEqual(integral, f/2)
        self.assertClose(np.exp(-1j*integral), np.exp(-0.5j*f))

    def test_saved_triadic_report_matches_evaluation(self):
        report = json.loads((ROOT / "analysis/Coupling_Scale_Candidate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["triadic_propagator_diagnosis"], candidate.triadic_propagator_diagnosis())

    def test_fixed_exchange_defect_matches_prepared_op5_identity(self):
        a1, a2 = 0.5, 0.9
        c, w1, w2 = 0.2+0.03j, 0.15-0.02j, 0.12+0.01j
        full = np.array([[a1, c, np.conj(w1)], [np.conj(c), a2, np.conj(w2)], [w1, w2, 3]])
        j = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        defect = np.linalg.norm(full @ j-j @ full, "fro")**2
        self.assertAlmostEqual(defect, 2*(a1-a2)**2+8*c.imag**2+4*abs(w1-w2)**2)

    def test_scalar_exact_exchange_only_allows_real_cycle_phase(self):
        for c in [0.2, -0.2]:
            phase = candidate.triadic_loop_phase(c, 0.1+0.03j, 0.1+0.03j)
            self.assertAlmostEqual(abs(math.cos(phase)), 1)

    def test_internal_generation_phase_preserves_fixed_exchange_and_changes_spectrum(self):
        report = candidate.triadic_propagator_diagnosis()["internal_generation_tensor_witness"]
        samples = report["phase_samples"]
        for sample in samples:
            self.assertLess(sample["fixed_exchange_commutator_frobenius"], 2e-12)
            self.assertLess(sample["odd_even_coupling_frobenius"], 2e-12)
        self.assertFalse(np.allclose(samples[0]["light_magnitudes_arbitrary_energy_units"],
                                     samples[1]["light_magnitudes_arbitrary_energy_units"], atol=1e-9))
        self.assertTrue(report["phase_and_zero_direct_block_are_chosen_not_derived"])

    def test_internal_even_witness_recovers_exact_six_dimensional_mass_model(self):
        samples = candidate.triadic_propagator_diagnosis()["internal_generation_tensor_witness"]["phase_samples"]
        for sample in samples:
            self.assertLess(sample["compressed_gap_model_error_frobenius"], 2e-12)
            self.assertLess(sample["maximum_exact_mass_formula_error"], 2e-12)
        _, t, _ = candidate.cyclic_candidate()
        chi = 0.3+0.2j
        v = math.sqrt(2)*chi*t
        mu = np.linalg.norm(v, "fro")
        self.assertAlmostEqual(mu, math.sqrt(2)*abs(chi)*np.linalg.norm(t, "fro"))
        normalized = v/mu
        self.assertClose(normalized.conj().T @ normalized, t.conj().T @ t)

    def test_even_witness_does_not_hide_visible_projector_leakage(self):
        samples = candidate.triadic_propagator_diagnosis()["internal_generation_tensor_witness"]["phase_samples"]
        for sample in samples:
            self.assertGreater(sample["visible_projector_commutator_frobenius"], 0.1)

    def test_noncommuting_gap_vertex_and_energy_variation_matches_finite_difference(self):
        energy, de, step = 0.1, 0.02, 1e-5
        dw1, dw2 = 0.03*self.w1, -0.02j*self.w2
        dd = np.array([[0.1, 0.03j], [-0.03j, -0.1]])
        r1 = np.linalg.solve(self.d-energy*np.eye(2), self.w1)
        r2 = np.linalg.solve(self.d-energy*np.eye(2), self.w2)
        analytic = (dw1.conj().T @ r2+r1.conj().T @ dw2
                    -r1.conj().T @ (dd-de*np.eye(2)) @ r2)

        def cross_response(eps):
            v1, v2 = self.w1+eps*dw1, self.w2+eps*dw2
            r = np.linalg.solve(self.d+eps*dd-(energy+eps*de)*np.eye(2), v2)
            return v1.conj().T @ r

        numerical = (cross_response(step)-cross_response(-step))/(2*step)
        self.assertClose(analytic, numerical)

    def test_one_scalar_gap_changes_interference_strength_not_cycle_phase(self):
        c, w1, w2 = 0.2, 0.15, 0.12j
        phases, effective_phases = [], []
        for gap in [3, 4]:
            u = np.conj(w1)*w2/gap
            phases.append(np.angle(u/c))
            effective_phases.append(np.angle(c-u))
        self.assertAlmostEqual(phases[0], phases[1])
        self.assertGreater(abs(effective_phases[0]-effective_phases[1]), 0.001)

    def test_two_hidden_gaps_can_change_phase_with_fixed_vertices(self):
        v1, v2 = np.array([0.2, 0.15]), np.array([0.1, 0.12j])
        d, dd, eps = np.diag([3.0, 5.0]), np.diag([0.1, -0.07]), 1e-5
        up = np.vdot(v1, np.linalg.solve(d+eps*dd, v2))
        um = np.vdot(v1, np.linalg.solve(d-eps*dd, v2))
        numerical = np.angle(up/um)/(2*eps)
        report = candidate.triadic_propagator_diagnosis()["gap_to_phase_derivative_example"]
        self.assertAlmostEqual(numerical, report["d_loop_phase_per_parameter"], places=9)
        self.assertGreater(abs(numerical), 0.001)

    def test_simple_pole_response_uses_full_state_norm(self):
        report = candidate.triadic_propagator_diagnosis()["pole_response_example"]
        self.assertLess(report["absolute_derivative_difference"], 2e-12)

    def test_op5_preparation_is_cited_without_conflating_index_spaces(self):
        report = candidate.triadic_propagator_diagnosis()["prepared_op5_interface"]
        source = (ROOT / report["source"]).read_text(encoding="utf-8")
        for section in report["sections"]:
            self.assertIn(section, source)
        self.assertTrue(report["relay_and_loop_phase_already_prepared"])
        self.assertTrue(report["native_global_involution_not_identified_with_probe_exchange"])
