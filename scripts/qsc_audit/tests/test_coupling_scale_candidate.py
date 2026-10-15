"""Checks for the declared numerical candidate and its scale obstructions."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "coupling_scale_candidate", ROOT / "analysis/Coupling_Scale_Candidate.py")
candidate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(candidate)


class CouplingScaleCandidateTests(unittest.TestCase):
    def setUp(self):
        self.theta, self.b, self.qmatrix = candidate.cyclic_candidate()
        self.q = np.linalg.eigvalsh(self.qmatrix)

    def assertMatrixEqual(self, left, right):
        np.testing.assert_allclose(left, right, atol=2e-12, rtol=2e-12)

    def test_candidate_is_positive_hermitian_and_unit_frobenius(self):
        self.assertMatrixEqual(self.b, self.b.conj().T)
        self.assertGreater(np.linalg.eigvalsh(self.b)[0], 0)
        self.assertAlmostEqual(np.linalg.norm(self.b, ord="fro"), 1)
        self.assertAlmostEqual(np.trace(self.qmatrix).real, 1)

    def test_matrix_entries_and_eigenvalues_are_evaluated_from_written_inputs(self):
        self.assertAlmostEqual(self.theta, math.pi-math.sqrt(2)*math.asin(0.5493))
        self.assertAlmostEqual(self.b[0, 0].real, 0.4082482904638631)
        self.assertAlmostEqual(self.b[1, 0].real, -0.19643267266228367)
        self.assertAlmostEqual(self.b[1, 0].imag, 0.21153613980614627)
        self.assertMatrixEqual(self.q, [0.0002366350011586, 0.0567819436407, 0.9429814213581])
        u = np.roll(np.eye(3), 1, axis=0)
        self.assertMatrixEqual(self.b @ u, u @ self.b)

    def test_koide_in_candidate_follows_the_imposed_radius(self):
        self.assertAlmostEqual(candidate.koide_diagnostic(self.q), 2/3)
        self.assertMatrixEqual(np.diag(self.qmatrix), np.full(3, 1/3))

    def test_target_masses_do_not_enter_coupling_construction(self):
        with patch.object(candidate, "HISTORICAL_MASSES_MEV", np.array([1.0, 2.0, 3.0])):
            theta, b, q = candidate.cyclic_candidate()
        self.assertEqual(theta, self.theta)
        self.assertMatrixEqual(b, self.b)
        self.assertMatrixEqual(q, self.qmatrix)

    def test_nonphysical_or_nonfinite_frame_inputs_are_rejected(self):
        for beta in (-1.0, 1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                candidate.cyclic_candidate(beta)

    def test_fixed_radius_photon_input_is_not_a_positive_root_branch(self):
        with self.assertRaisesRegex(ValueError, "positive-root chamber"):
            candidate.cyclic_candidate(0)

    def test_output_isometry_preserves_gram_without_fixing_native_matrix(self):
        w = np.array([[0, 1j, 0], [1, 0, 0], [0, 0, -1]], dtype=complex)
        changed = w @ self.b
        self.assertMatrixEqual(changed.conj().T @ changed, self.qmatrix)
        self.assertGreater(np.linalg.norm(changed-self.b), 0.1)

    def test_normalization_removes_mu_b_redundancy_not_a_physical_scale(self):
        mu = 7.0
        v = mu*self.b
        self.assertAlmostEqual(np.linalg.norm(v, ord="fro"), mu)
        self.assertMatrixEqual((3*mu)*(self.b/3), v)

    def test_two_cyclic_harmonics_obey_closed_triole_bound(self):
        omega = np.exp(2j*math.pi/3)
        for b0, b1 in ((1, 1), (0.3+0.2j, -0.7j), (0, 2j), (2, -1)):
            values = np.array([b0+b1*omega**k for k in range(3)])
            closed = np.array([omega**k*values[k] for k in range(3)])
            self.assertAlmostEqual(abs(np.sum(closed)), 0)
            self.assertLessEqual(candidate.koide_diagnostic(abs(values)**2), 0.5+1e-12)

    def test_two_harmonic_bound_can_be_tight(self):
        values = 1-np.exp(2j*math.pi*np.arange(3)/3)
        self.assertAlmostEqual(candidate.koide_diagnostic(abs(values)**2), 0.5)

    def test_positive_gap_correction_increases_smaller_mass_ratios(self):
        leading = self.q/self.q[-1]
        for mu, gap in ((0.1, 5), (1, 5), (7, 5), (10, 0.5)):
            masses = candidate.light_masses(self.q, mu, gap)
            self.assertTrue(np.all(masses[:2]/masses[-1] > leading[:2]))
            exact_ratios = leading*(np.sqrt(gap**2+4*mu**2*self.q[-1])+gap)
            exact_ratios /= np.sqrt(gap**2+4*mu**2*self.q)+gap
            self.assertMatrixEqual(masses/masses[-1], exact_ratios)

    def test_ratio_error_cannot_be_fixed_by_positive_flat_gap_scales(self):
        benchmark = candidate.HISTORICAL_MASSES_MEV[1]/candidate.HISTORICAL_MASSES_MEV[2]
        self.assertGreater(self.q[1]/self.q[-1], benchmark)
        for eta in np.logspace(-16, 5, 50):
            masses = candidate.light_masses(self.q, eta, 1)
            self.assertGreater(masses[1]/masses[-1], benchmark)

    def test_simultaneous_physical_scale_change_preserves_ratios_and_weights(self):
        masses = candidate.light_masses(self.q, 0.7, 5)
        weights = masses/(5+2*masses)
        for scale in (1e-12, 7.0, 1e12):
            changed = candidate.light_masses(self.q, scale*0.7, scale*5)
            self.assertMatrixEqual(changed/scale, masses)
            self.assertMatrixEqual(changed/(scale*5+2*changed), weights)

    def test_small_eta_recovers_leading_ratios_without_planck_cancellation(self):
        gap = candidate.PLANCK_GEV
        mu = 1/math.sqrt(2*math.sqrt(2)*candidate.FERMI_GEV_MINUS_2)
        masses = candidate.light_masses(self.q, mu, gap)
        self.assertTrue(np.all(masses > 0))
        self.assertMatrixEqual(masses/(mu**2/gap), self.q)
        naive = (np.sqrt(gap**2+4*mu**2*self.q)-gap)/2
        self.assertMatrixEqual(naive, np.zeros(3))

    def test_explicit_six_dimensional_block_realizes_candidate_not_native_clock(self):
        p = np.diag([1.0]*3+[0.0]*3)
        s = np.eye(6)[:, :3]
        r = np.block([[np.zeros((3, 3)), self.b.conj().T], [self.b, np.zeros((3, 3))]])
        transition = (np.eye(6)-p) @ r @ s
        self.assertMatrixEqual(transition.conj().T @ transition, self.qmatrix)
        mu, gap = 0.7, 5.0
        omega = mu*r+gap*(np.eye(6)-p)
        spectrum = np.linalg.eigvalsh(omega)
        masses = candidate.light_masses(self.q, mu, gap)
        self.assertMatrixEqual(np.sort(-spectrum[:3]), masses)

    def test_scale_report_keeps_assumptions_calibrations_and_predictions_distinct(self):
        report = candidate.evaluate()
        self.assertIn("not native identification", report["status"])
        self.assertTrue(report["historical_comparison_only"]["no_positive_flat_gap_scale_fit_for_fixed_shape"])
        self.assertGreater(len(report["assumptions"]), 5)
        self.assertIn("one_mass_calibrations_not_predictions", report)
        self.assertIn("illustrative_not_derived_scale_choices", report)

    def test_planck_gap_electroweak_reference_has_micro_ev_scale_not_charged_leptons(self):
        report = candidate.evaluate()
        values = report["illustrative_not_derived_scale_choices"]["planck_gap_electroweak_mixing"]
        masses_ev = 1e9*np.array(values["mass_magnitudes_GeV"])
        np.testing.assert_allclose(masses_ev, [5.8751353e-10, 1.4097729e-7, 2.3412189e-6], rtol=1e-7)
        self.assertLess(masses_ev[-1], 3e-6)

    def test_one_tau_calibration_reproduces_only_the_chosen_mass(self):
        report = candidate.evaluate()
        tau_gev = candidate.HISTORICAL_MASSES_MEV[-1]/1000
        for scenario in report["one_mass_calibrations_not_predictions"].values():
            self.assertAlmostEqual(scenario["mass_magnitudes_GeV"][-1], tau_gev)
            self.assertGreater(scenario["ratios_to_largest"][1],
                               report["historical_comparison_only"]["ratios_to_largest"][1])

    def test_reference_frame_units_do_not_mix_matter_hbar_with_photon_length(self):
        gamma = (1+0.5493**2)/(1-0.5493**2)
        hbar_f, g_f, length_f = gamma**-1, gamma**-2, gamma**-1.5
        reference_mass = math.sqrt(hbar_f/g_f)
        self.assertAlmostEqual(reference_mass, gamma**0.5)
        self.assertAlmostEqual(hbar_f/length_f, reference_mass)
        self.assertAlmostEqual((1/length_f)/reference_mass, gamma)

    def test_invalid_gap_scale_or_spectrum_is_rejected(self):
        for q, mu, gap in (([-1, 2, 3], 1, 2), ([], 1, 2), ([[1, 2]], 1, 2),
                           ([1, math.inf], 1, 2), ([1], -1, 2), ([1], 1, 0),
                           ([1], math.nan, 2), ([1], 1, math.inf)):
            with self.assertRaises(ValueError):
                candidate.light_masses(q, mu, gap)

    def test_zero_coupling_or_zero_eigenvalue_stays_zero(self):
        self.assertMatrixEqual(candidate.light_masses(self.q, 0, 2), np.zeros(3))
        self.assertMatrixEqual(candidate.light_masses([0, 0, 0], 2, 2), np.zeros(3))

    def test_zero_or_invalid_koide_diagnostic_is_not_silently_activated(self):
        for masses in ([0, 0, 0], [-1, 2, 3], [1, math.inf, 3], [1, 2]):
            with self.assertRaises(ValueError):
                candidate.koide_diagnostic(masses)

    def test_recorded_candidate_preserves_evaluated_values_and_scope(self):
        recorded = json.loads((ROOT / "analysis/Coupling_Scale_Candidate.json").read_text(encoding="utf-8"))
        self.assertIn("not native identification", recorded["status"])
        self.assertMatrixEqual(recorded["B_real"], self.b.real)
        self.assertMatrixEqual(recorded["B_imag"], self.b.imag)
        self.assertMatrixEqual(recorded["q_eigenvalues_ascending"], self.q)

    def test_matrix_spectrum_exactly_matches_the_written_root_formula(self):
        analytic = (1+math.sqrt(2)*np.cos(self.theta+2*math.pi*np.arange(3)/3))/math.sqrt(6)
        self.assertMatrixEqual(np.linalg.eigvalsh(self.b), analytic)
        self.assertMatrixEqual(self.q, analytic**2)

    def test_historical_inverse_fourier_diagnosis_recovers_phase_and_radius(self):
        d = candidate.matrix_diagnosis()
        self.assertAlmostEqual(d["benchmark_phase_radians"], 2.3166242553943306)
        self.assertAlmostEqual(d["benchmark_radius"], 0.7071005784723055)
        observed = candidate.HISTORICAL_MASSES_MEV/candidate.HISTORICAL_MASSES_MEV[-1]
        self.assertMatrixEqual(d["both_benchmark_reconstructed_ratios"], observed)
        self.assertIn("not a derived phase law", d["status"])

    def test_phase_diagnosis_removes_most_shape_error_radius_alone_does_not(self):
        d = candidate.matrix_diagnosis()
        observed = candidate.HISTORICAL_MASSES_MEV/candidate.HISTORICAL_MASSES_MEV[-1]
        phase_error = np.array(d["phase_only_corrected_ratios"])/observed-1
        radius_error = np.array(d["radius_only_corrected_ratios"])/observed-1
        self.assertTrue(np.all(abs(phase_error) < 0.0005))
        self.assertGreater(abs(radius_error[0]), 0.12)
        self.assertGreater(abs(radius_error[1]), 0.01)

    def test_phase_and_radius_log_sensitivities_match_finite_differences(self):
        d = candidate.matrix_diagnosis()
        radius, step = 1/math.sqrt(2), 1e-6

        def log_ratios(r, theta):
            b = candidate.normalized_cyclic_root(r, theta)
            values = np.linalg.eigvalsh(b.conj().T @ b)
            return np.log(values/values[-1])

        phase_fd = (log_ratios(radius, self.theta+step)-log_ratios(radius, self.theta-step))/(2*step)
        radius_fd = (log_ratios(radius+step, self.theta)-log_ratios(radius-step, self.theta))/(2*step)
        np.testing.assert_allclose(phase_fd, d["log_ratio_derivative_theta"], atol=2e-6, rtol=2e-7)
        np.testing.assert_allclose(radius_fd, d["log_ratio_derivative_radius"], atol=2e-6, rtol=2e-7)

    def test_beta_sensitivity_has_small_root_amplification_and_opposite_ratio_signs(self):
        d = candidate.matrix_diagnosis()
        derivatives = d["log_ratio_derivative_beta"]
        self.assertGreater(derivatives[0], 90)
        self.assertLess(derivatives[1], -8)
        step = 1e-6
        ratios = []
        for beta in (0.5493-step, 0.5493+step):
            q = np.linalg.eigvalsh(candidate.cyclic_candidate(beta)[2])
            ratios.append(np.log(q/q[-1]))
        np.testing.assert_allclose((ratios[1]-ratios[0])/(2*step), derivatives,
                                   atol=2e-6, rtol=2e-7)

    def test_four_decimal_rounding_cannot_explain_the_middle_ratio(self):
        observed = candidate.HISTORICAL_MASSES_MEV[1]/candidate.HISTORICAL_MASSES_MEV[-1]
        values = []
        for beta in np.linspace(0.54925, 0.54935, 41):
            q = np.linalg.eigvalsh(candidate.cyclic_candidate(float(beta))[2])
            values.append(q[1]/q[-1])
        self.assertTrue(np.all(np.diff(values) < 0))
        self.assertGreater(min(values), observed)
        d = candidate.matrix_diagnosis()
        self.assertGreater(d["required_shift_in_rounding_halfsteps"], 30)

    def test_exact_string_expression_does_not_remove_the_discrepancy(self):
        d = candidate.matrix_diagnosis()["source_ratio_recomputed_not_exact_native_input"]
        self.assertAlmostEqual(d["beta"], 0.54934824835987)
        observed = candidate.HISTORICAL_MASSES_MEV[1]/candidate.HISTORICAL_MASSES_MEV[-1]
        self.assertGreater(d["ratios"][1], observed)
        self.assertGreater(d["gamma_BI_needed_for_benchmark_phase"], d["quoted_gamma_BI"])

    def test_display_rounding_and_cyclic_sign_conventions_do_not_fix_spectrum(self):
        d = candidate.matrix_diagnosis()
        self.assertLess(max(abs(np.array(d["six_decimal_matrix_relative_ratio_errors"]))), 0.001)
        for theta in (-self.theta, self.theta+2*math.pi/3, self.theta+4*math.pi/3):
            b = candidate.normalized_cyclic_root(1/math.sqrt(2), theta)
            self.assertMatrixEqual(np.linalg.eigvalsh(b.conj().T @ b), self.q)

    def test_independent_si_energy_conversion_agrees_with_codata_planck_reference(self):
        d = candidate.planck_diagnosis()
        si = d["si_inputs"]
        energy = d["si_planck_mass_kg"]*si["c_m_per_s"]**2/si["J_per_GeV"]
        self.assertAlmostEqual(energy/d["si_planck_energy_GeV"], 1)
        self.assertLess(abs(energy/candidate.PLANCK_GEV-1), 2e-7)
        self.assertAlmostEqual(d["si_planck_length_m"]/1.6162550244237053e-35, 1)

    def test_planck_mass_and_length_have_consistent_inverse_energy_units(self):
        d = candidate.planck_diagnosis()
        si = d["si_inputs"]
        product = d["si_planck_energy_GeV"]*si["J_per_GeV"]*d["si_planck_length_m"]
        self.assertAlmostEqual(product/(si["hbar_Js"]*si["c_m_per_s"]), 1)
        mu = 1/math.sqrt(2*math.sqrt(2)*candidate.FERMI_GEV_MINUS_2)
        from_si = candidate.light_masses(self.q, mu, d["si_planck_energy_GeV"])*1e9
        from_reference = candidate.light_masses(self.q, mu, candidate.PLANCK_GEV)*1e9
        np.testing.assert_allclose(from_si/from_reference, np.ones(3), rtol=2e-7)

    def test_reduced_planck_choice_changes_only_an_order_one_factor(self):
        d = candidate.planck_diagnosis()
        reduced = np.array(d["reduced_planck_gap_mass_magnitudes_eV"])
        mu = 1/math.sqrt(2*math.sqrt(2)*candidate.FERMI_GEV_MINUS_2)
        ordinary = candidate.light_masses(self.q, mu, candidate.PLANCK_GEV)*1e9
        self.assertMatrixEqual(reduced/ordinary, np.full(3, math.sqrt(8*math.pi)))
        self.assertLess(reduced[-1], 2e-5)
        self.assertGreater(d["reference_mass_shortfall_factor_vs_quoted_tau"], 7e14)

    def test_conditional_frame_factors_cannot_supply_fourteen_orders(self):
        d = candidate.planck_diagnosis()["conditional_paper_frame_factors"]
        self.assertAlmostEqual(d["consistent_planck_mass_photon_over_matter"], math.sqrt(d["gamma_L"]))
        self.assertLess(d["mixed_hbar_wrong_planck_mass_photon_over_matter"], 3)
        self.assertTrue(d["not_a_standard_Lorentz_transformation_of_constants"])

    def test_calibrated_gap_length_is_not_the_fundamental_planck_length(self):
        d = candidate.planck_diagnosis()
        calibration = d["tau_calibrations_not_predictions"]
        ratio = calibration["gap_inverse_energy_length_m"]/d["si_planck_length_m"]
        self.assertAlmostEqual(ratio/calibration["gap_length_over_fundamental_planck_length"], 1)
        self.assertGreater(ratio, 7e14)
        self.assertLess(calibration["gap_inverse_energy_length_m"], 1.3e-20)

    def test_nonflat_planck_gap_fit_is_possible_but_explicitly_calibrated(self):
        d = candidate.planck_diagnosis()["nonflat_planck_gap_full_mass_fit_not_prediction"]
        self.assertMatrixEqual(d["fitted_mass_magnitudes_GeV"], candidate.HISTORICAL_MASSES_MEV/1000)
        np.testing.assert_allclose(d["gaps_over_tau_gap"], [0.8725858312, 1.0126466798, 1], rtol=1e-9)
        self.assertGreater(min(d["gaps_over_tau_gap"]), 0.8)
        self.assertTrue(np.all(np.array(d["complementary_weights"]) > 0))
        self.assertLess(max(d["complementary_weights"]), 2e-19)

    def test_nonflat_singular_basis_witness_matches_exact_finite_block_spectrum(self):
        target = candidate.HISTORICAL_MASSES_MEV/candidate.HISTORICAL_MASSES_MEV[-1]
        mu = math.sqrt(target[-1]*(50+target[-1])/self.q[-1])
        gaps = mu**2*self.q/target-target
        _, f = np.linalg.eigh(self.b)
        h = f @ np.diag(gaps) @ f.conj().T
        omega = np.block([[np.zeros((3, 3)), mu*self.b.conj().T], [mu*self.b, h]])
        spectrum = np.linalg.eigvalsh(omega)
        self.assertMatrixEqual(np.sort(-spectrum[:3]), target)
        self.assertMatrixEqual(np.sort(spectrum[3:]), np.sort(gaps+target))

    def test_nonflat_gap_alignment_is_additional_physical_data(self):
        target = candidate.HISTORICAL_MASSES_MEV/candidate.HISTORICAL_MASSES_MEV[-1]
        mu = math.sqrt(51/self.q[-1])
        gaps = mu**2*self.q/target-target
        omega = np.block([[np.zeros((3, 3)), mu*self.b.conj().T], [mu*self.b, np.diag(gaps)]])
        masses = np.sort(-np.linalg.eigvalsh(omega)[:3])
        self.assertGreater(np.max(abs(masses-target)), 1e-4)

    def test_direct_block_eigenvalue_bound_holds_for_complex_couplings(self):
        a = np.diag([0.2, 0.7, 1.2])
        v = np.array([[0.1, 0.1j, 0], [0.2, 0.05, 0.1j], [0, 0.1, 0.1]])
        h = np.diag([4.0, 6.0, 8.0])
        omega = np.block([[a, v.conj().T], [v, h]])
        spectrum = np.linalg.eigvalsh(omega)
        bound = np.linalg.norm(v, ord=2)**2/(4-2)
        for value in spectrum[:3]:
            self.assertLess(abs(value), 2)
            self.assertLessEqual(np.min(abs(np.diag(a)-value)), bound)

    def test_planck_sector_may_be_small_correction_instead_of_whole_mass_source(self):
        d = candidate.planck_diagnosis()
        bound = d["direct_mass_block_scenario"]["light_eigenvalue_distance_to_spectrum_A_bound_eV"]
        self.assertAlmostEqual(bound/2.3412189258049486e-6, 1)
        self.assertTrue(d["direct_mass_block_scenario"]["native_A_not_evaluated"])
        self.assertIn("additional test assumptions", d["scope"])

    def test_recorded_diagnosis_preserves_the_nonprediction_boundaries(self):
        recorded = json.loads((ROOT / "analysis/Coupling_Scale_Candidate.json").read_text(encoding="utf-8"))
        self.assertIn("not a derived phase law", recorded["posthoc_matrix_diagnosis_not_prediction"]["status"])
        self.assertIn("not paper-derived identities", recorded["planck_assumption_diagnosis"]["scope"])
