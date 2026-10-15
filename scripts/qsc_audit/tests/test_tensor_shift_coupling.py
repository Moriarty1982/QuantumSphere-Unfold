"""Tensor covariance is distinct from an added physical comparison metric."""
from pathlib import Path
import importlib.util
import json
import math
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "tensor_candidate", ROOT / "analysis/Coupling_Scale_Candidate.py")
candidate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(candidate)


class TensorShiftCouplingTests(unittest.TestCase):
    def setUp(self):
        _, self.b, self.q = candidate.cyclic_candidate()
        self.eye = np.eye(3)
        self.k = np.array([[2, 0.1j, 0], [-0.1j, 1, 0.2], [0, 0.2, 3]])
        self.h = np.array([[1, 0.2, 0], [0.2, 2, 0.1j], [0, -0.1j, 1.5]])

    def assertClose(self, actual, expected):
        np.testing.assert_allclose(actual, expected, rtol=2e-10, atol=2e-12)

    def test_identity_metrics_recover_previous_candidate(self):
        coupling, gram, q = candidate.tensor_coupling(self.b, self.eye, self.eye)
        self.assertClose(coupling, self.b)
        self.assertClose(gram, self.q)
        self.assertClose(q, np.linalg.eigvalsh(self.q))

    def test_positive_metric_roots_and_inverses(self):
        root = candidate.positive_metric_root(self.k)
        inverse = candidate.positive_metric_root(self.k, inverse=True)
        self.assertClose(root @ root, self.k)
        self.assertClose(root @ inverse, self.eye)

    def test_invalid_metrics_rejected(self):
        for metric in ([], np.zeros((0, 0)), [1, 2], np.ones((2, 3)),
                       [[1, 1], [0, 1]], np.diag([1, 0]),
                       np.diag([1, -1]), np.diag([1, np.nan]),
                       np.diag([1, np.inf])):
            with self.subTest(metric=metric), self.assertRaises(ValueError):
                candidate.positive_metric_root(metric)

    def test_mismatched_spaces_rejected(self):
        with self.assertRaises(ValueError):
            candidate.tensor_coupling(self.b, self.eye, np.eye(4))
        with self.assertRaises(ValueError):
            candidate.tensor_coupling(self.b, np.eye(2), self.eye)
        with self.assertRaises(ValueError):
            candidate.tensor_coupling([np.nan], self.eye, self.eye)

    def test_rectangular_map_is_supported(self):
        b = np.array([[1, 0], [0, 2], [1j, 1]])
        coupling, gram, q = candidate.tensor_coupling(b, np.eye(2), self.h)
        self.assertEqual(coupling.shape, (3, 2))
        self.assertClose(gram, b.conj().T @ self.h @ b)
        self.assertGreater(q[0], 0)

    def test_generalized_eigenvectors_satisfy_tensor_equation(self):
        _, gram, _ = candidate.tensor_coupling(self.b, self.k, self.h)
        q, vectors = np.linalg.eigh(gram)
        x = candidate.positive_metric_root(self.k, inverse=True) @ vectors
        self.assertClose(self.b.conj().T @ self.h @ self.b @ x, (self.k @ x)*q)
        self.assertClose(x.conj().T @ self.k @ x, self.eye)

    def test_nonunitary_charts_preserve_generalized_spectrum(self):
        a = np.array([[2, 0.2j, 0], [0, 0.7, 0], [0, 0, 1.1]])
        d = np.array([[1, 0, 0.1], [0, 1.3, 0], [0, 0.2j, 0.8]])
        transformed = np.linalg.solve(d, self.b @ a)
        _, _, expected = candidate.tensor_coupling(self.b, self.k, self.h)
        _, _, actual = candidate.tensor_coupling(
            transformed, a.conj().T @ self.k @ a, d.conj().T @ self.h @ d)
        self.assertClose(actual, expected)

    def test_identity_metric_reuse_can_create_spurious_shift(self):
        result = candidate.tensor_shift_diagnosis()["nonunitary_chart_test_not_native_frame"]
        self.assertLess(result["max_absolute_eigenvalue_difference"], 2e-12)
        self.assertGreater(np.max(np.abs(np.array(result["incorrect_identity_metric_ratios"])
                                        - result["correct_covariant_ratios"])), 0.001)

    def test_common_phase_cancels_with_nontrivial_metrics(self):
        _, gram, _ = candidate.tensor_coupling(self.b, self.k, self.h)
        _, phased, _ = candidate.tensor_coupling(np.exp(0.7j)*self.b, self.k, self.h)
        self.assertClose(gram, phased)

    def test_comparison_metric_changes_spectrum_when_not_coordinate_transport(self):
        _, _, weighted = candidate.tensor_coupling(self.b, self.eye, self.h)
        self.assertFalse(np.allclose(weighted, np.linalg.eigvalsh(self.q)))

    def test_weighted_self_adjoint_block_has_expected_exact_spectrum(self):
        mu, gap = 0.6, 2.0
        bsharp = np.linalg.solve(self.k, self.b.conj().T @ self.h)
        omega = np.block([[np.zeros((3, 3)), mu*bsharp], [mu*self.b, gap*self.eye]])
        metric = np.block([[self.k, np.zeros((3, 3))], [np.zeros((3, 3)), self.h]])
        root = candidate.positive_metric_root(metric)
        canonical = root @ omega @ candidate.positive_metric_root(metric, inverse=True)
        self.assertClose(canonical, canonical.conj().T)
        _, _, q = candidate.tensor_coupling(self.b, self.k, self.h)
        light = candidate.light_masses(q, mu, gap)
        self.assertClose(np.linalg.eigvalsh(canonical), np.sort(np.r_[-light, gap+light]))

    def test_minmax_metric_bounds_hold_mode_by_mode(self):
        _, _, q = candidate.tensor_coupling(self.b, self.k, self.h)
        baseline = np.linalg.eigvalsh(self.q)
        h = np.linalg.eigvalsh(self.h)
        k = np.linalg.eigvalsh(self.k)
        self.assertTrue(np.all(q >= baseline*h[0]/k[-1]-1e-12))
        self.assertTrue(np.all(q <= baseline*h[-1]/k[0]+1e-12))

    def test_historical_metric_witness_is_fit_not_prediction(self):
        fit = candidate.tensor_shift_diagnosis()["posthoc_output_metric_fit_not_prediction"]
        self.assertClose(fit["fitted_leading_ratios"],
                         candidate.HISTORICAL_MASSES_MEV/candidate.HISTORICAL_MASSES_MEV[-1])
        self.assertClose(fit["output_eigenweights_ascending_B_modes"],
                         [1.146019066893, 0.987511261324, 1])
        self.assertTrue(fit["exact_flat_gap_correction_still_applies"])

    def test_scalar_output_metric_rescales_only_coupling_normalization(self):
        _, _, q = candidate.tensor_coupling(self.b, self.eye, 7*self.eye)
        self.assertClose(q, 7*np.linalg.eigvalsh(self.q))
        self.assertClose(candidate.light_masses(q, 0.2, 2),
                         candidate.light_masses(np.linalg.eigvalsh(self.q), math.sqrt(7)*0.2, 2))

    def test_planck_scale_cannot_be_repaired_by_modest_absolute_weights(self):
        result = candidate.tensor_shift_diagnosis()["planck_metric_bound"]
        self.assertGreater(result["required_h_max_over_k_min_at_least"], 7e14)
        self.assertAlmostEqual(result["equivalent_canonical_coupling_norm_enhancement"]**2
                               / result["required_h_max_over_k_min_at_least"], 1)
        self.assertLess(result["fitted_shape_metric_max_weight"], 1.15)

    def test_tensor_identity_extension_preserves_compressed_gram(self):
        result = candidate.tensor_shift_diagnosis()["identity_tensor_extension"]
        self.assertLess(result["max_absolute_compressed_gram_difference"], 2e-12)
        self.assertTrue(result["requires_new_interaction_for_new_effect"])

    def test_tag_shift_reconstructs_masks_not_numeric_matrix_payload(self):
        result = candidate.tensor_shift_diagnosis()["source_shift_is_tag_only"]
        self.assertEqual(result["packed_mask_before"], 37)
        self.assertEqual(result["packed_mask_after"], 74)
        self.assertNotEqual(result["packed_mask_after"], result["packed_mask_before"]+1)
        self.assertFalse(result["numeric_payload_changed"])

    def test_saved_report_matches_evaluation(self):
        report = json.loads((ROOT / "analysis/Coupling_Scale_Candidate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["tensor_shift_diagnosis"], candidate.tensor_shift_diagnosis())
