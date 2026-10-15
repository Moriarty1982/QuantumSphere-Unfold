"""Finite mechanism tests are not a native lepton interaction identification."""
from pathlib import Path
import importlib.util
import json
import math
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "physical_candidate", ROOT / "analysis/Coupling_Scale_Candidate.py")
candidate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(candidate)


class CouplingPhysicalOriginTests(unittest.TestCase):
    def setUp(self):
        self.v = np.array([[0.2, 0.1j], [-0.1j, 0.3], [0.15, -0.1]])
        self.d = np.array([[3, 0.2j, 0], [-0.2j, 4, 0.1], [0, 0.1, 5]])

    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def test_schur_response_matches_explicit_inverse(self):
        n, k = candidate.schur_response(self.v, self.d, 0.1)
        r = np.linalg.inv(self.d-0.1*np.eye(3))
        self.assertClose(n, self.v.conj().T @ r @ self.v)
        self.assertClose(k, self.v.conj().T @ r @ r @ self.v)

    def test_response_derivative_has_positive_sign(self):
        step = 1e-5
        plus = candidate.schur_response(self.v, self.d, step)[0]
        minus = candidate.schur_response(self.v, self.d, -step)[0]
        _, k = candidate.schur_response(self.v, self.d)
        self.assertClose((plus-minus)/(2*step), k)
        self.assertGreater(np.linalg.eigvalsh(k)[0], 0)

    def test_reconstructed_full_state_has_derived_norm(self):
        energy = -0.1
        x = np.array([1, 0.7j])
        y = -np.linalg.solve(self.d-energy*np.eye(3), self.v @ x)
        _, k = candidate.schur_response(self.v, self.d, energy)
        self.assertClose(np.vdot(x, x)+np.vdot(y, y), np.vdot(x, (np.eye(2)+k) @ x))

    def test_schur_equation_matches_full_eigenproblem(self):
        a = np.diag([0.1, -0.2])
        omega = np.block([[a, self.v.conj().T], [self.v, self.d]])
        energies, vectors = np.linalg.eigh(omega)
        for index in range(2):
            energy, x = energies[index], vectors[:2, index]
            n, _ = candidate.schur_response(self.v, self.d, energy)
            self.assertClose((a-n) @ x, energy*x)

    def test_norm_response_obeys_decoupling_bound(self):
        energy = 0.2
        _, k = candidate.schur_response(self.v, self.d, energy)
        gap = np.linalg.eigvalsh(self.d)[0]
        bound = np.linalg.norm(self.v, 2)**2/(gap-energy)**2
        self.assertLessEqual(np.linalg.norm(k, 2), bound)

    def test_linear_energy_remainder_is_controlled(self):
        n0, k0 = candidate.schur_response(self.v, self.d)
        gap = np.linalg.eigvalsh(self.d)[0]
        for energy in [-0.1, 0.1]:
            n, _ = candidate.schur_response(self.v, self.d, energy)
            remainder = np.linalg.norm(n-n0-energy*k0, 2)
            bound = np.linalg.norm(self.v, 2)**2*energy**2/(gap**2*(gap-abs(energy)))
            self.assertLessEqual(remainder, bound)

    def test_zero_cross_block_induces_neither_mass_nor_norm_response(self):
        n, k = candidate.schur_response(np.zeros((3, 2)), self.d)
        self.assertClose(n, np.zeros((2, 2)))
        self.assertClose(k, np.zeros((2, 2)))

    def test_invalid_response_inputs_rejected(self):
        cases = [(self.v, self.d, np.nan), (self.v, self.d, np.inf),
                 (self.v, self.d, 10), (self.v, np.diag([-1, 2, 3]), 0),
                 (self.v, np.ones((2, 2)), 0), (np.ones(3), self.d, 0),
                 (np.zeros((3, 0)), self.d, 0), (np.full((3, 2), np.nan), self.d, 0)]
        for v, d, energy in cases:
            with self.subTest(energy=energy), self.assertRaises(ValueError):
                candidate.schur_response(v, d, energy)

    def test_minimal_penalty_cross_block_leaves_only_triadic_interaction(self):
        p = np.diag([1, 1, 0, 0])
        m = np.array([[1, 1j, 2, 0], [-1j, 2, 0, 1], [2, 0, 3, 0], [0, 1, 0, 4]])
        commutator = m @ p-p @ m
        hc = commutator.conj().T @ commutator
        triad = np.ones((4, 4))
        coefficient = 0.7
        omega = 0.2*np.eye(4)+0.3*p @ m @ p+coefficient*triad+0.4*hc
        self.assertClose((np.eye(4)-p) @ omega @ p,
                         coefficient*(np.eye(4)-p) @ triad @ p)

    def test_planck_norm_dressing_is_too_small_in_both_declared_scenarios(self):
        result = candidate.physical_origin_diagnosis()["induced_kinetic_dressing"]
        self.assertLess(result["planck_gap_electroweak_mu_max_delta_K"], 2e-34)
        self.assertLess(result["planck_gap_tau_calibrated_mu_max_delta_K"], 2e-19)
        self.assertGreater(result["minimum_delta_K_norm_for_aligned_kinetic_only_ratio_fit"], 0.15)

    def test_response_tensor_has_propagator_origin_not_arbitrary_kinetic_weight(self):
        result = candidate.physical_origin_diagnosis()["response_tensor_from_inverse_gaps"]
        self.assertLess(result["relative_gram_identity_error"], 2e-12)
        self.assertTrue(result["not_a_kinetic_metric_redefinition"])
        self.assertTrue(result["fit_uses_target_masses"])
        self.assertClose(result["historical_leading_fit_gap_weights"], [0.872585831152, 1.012646679754, 1])

    def test_inverse_gap_response_decreases_with_heavier_complement(self):
        small = candidate.schur_response(self.v, self.d)[0]
        large = candidate.schur_response(self.v, 2*self.d)[0]
        self.assertClose(large, small/2)

    def test_small_relative_phase_correction_is_not_common_phase(self):
        result = candidate.physical_origin_diagnosis()["coherent_phase_test"]
        self.assertAlmostEqual(result["relative_Frobenius_coupling_change"], 0.0018144372442)
        errors = result["remaining_relative_ratio_errors"]
        self.assertLess(abs(errors[0]), 0.0005)
        self.assertLess(abs(errors[1]), 0.00003)
        self.assertTrue(result["phase_change_is_historical_calibration_not_prediction"])
        _, b, q = candidate.cyclic_candidate()
        self.assertClose((np.exp(0.3j)*b).conj().T @ (np.exp(0.3j)*b), q)

    def test_singular_spectrum_witness_excludes_unitary_rephasing_explanation(self):
        _, b, q = candidate.cyclic_candidate()
        phase = candidate.matrix_diagnosis()["benchmark_phase_radians"]
        corrected = candidate.normalized_cyclic_root(1/math.sqrt(2), phase)
        self.assertGreater(abs(np.linalg.det(corrected.conj().T @ corrected)
                               /np.linalg.det(q)-1), 0.1)

    def test_orthogonal_uncoupled_frame_channels_do_not_interfere(self):
        samples = candidate.physical_origin_diagnosis()["coherent_phase_test"]["disconnected_complement_mass_response"]
        self.assertClose(samples, np.full(3, 0.05))

    def test_interacting_channels_can_retain_a_relative_phase(self):
        samples = candidate.physical_origin_diagnosis()["coherent_phase_test"]["coupled_complement_mass_response"]
        self.assertGreater(np.ptp(samples), 0.005)

    def test_shared_virtual_mediator_changes_all_schur_blocks_consistently(self):
        a, d, mediator = np.diag([0.1, 0.2]), np.diag([2.0, 2.5]), np.diag([4.0, 5.0])
        v = np.array([[0.2, 0.1j], [0, 0.3]])
        x = np.array([[0.1, 0.05], [0, 0.2j]])
        y = np.array([[0.1j, 0], [0.1, 0.2]])
        omega = np.block([[a, v.conj().T, x.conj().T],
                          [v, d, y.conj().T], [x, y, mediator]])
        energies, vectors = np.linalg.eigh(omega)
        for index in range(2):
            energy = energies[index]
            r = np.linalg.inv(mediator-energy*np.eye(2))
            veff = v-y.conj().T @ r @ x
            effective = np.block([[a-x.conj().T @ r @ x, veff.conj().T],
                                  [veff, d-y.conj().T @ r @ y]])
            self.assertClose(effective @ vectors[:4, index], energy*vectors[:4, index])

    def test_qed_matching_has_wrong_sign_pattern_for_full_discrepancy(self):
        result = candidate.physical_origin_diagnosis()["ordinary_one_loop_qed_matching_check"]
        self.assertTrue(all(x > 0 for x in result["relative_ratio_changes_first_order"][:2]))
        needed = result["needed_relative_ratio_changes"]
        self.assertGreater(needed[0], 0)
        self.assertLess(needed[1], 0)
        self.assertTrue(result["native_scheme_and_matching_scale_not_assigned"])

    def test_universal_redshift_of_entire_operator_preserves_exact_ratios(self):
        q = np.array([0.01, 0.2, 0.9])
        original = candidate.light_masses(q, 0.5, 3)
        redshift = candidate.light_masses(q, 0.7*0.5, 0.7*3)
        self.assertClose(original/original[-1], redshift/redshift[-1])

    def test_saved_physical_diagnosis_matches_evaluation(self):
        report = json.loads((ROOT / "analysis/Coupling_Scale_Candidate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["physical_origin_diagnosis"], candidate.physical_origin_diagnosis())
