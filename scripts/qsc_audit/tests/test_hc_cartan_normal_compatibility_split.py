"""Known left identities, six remaining gates and forced projector transport."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "normal_compatibility_split_test", ROOT / "analysis/HC_Cartan_Normal_Compatibility_Split.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CompatibilityTransportTests(unittest.TestCase):
    def test_projector_transport_against_smooth_matrix_difference(self):
        rng = np.random.default_rng(1910284)
        matrix = np.linalg.qr(rng.normal(size=(84, 56)))[0]
        dmatrix = rng.normal(size=(84, 56))*.02
        target, dtarget = rng.normal(size=(2, 84))
        result = model.compatibility_transport(matrix, target, dmatrix, dtarget)
        step = 1e-6
        plus = model.projection_state(matrix+step*dmatrix, target+step*dtarget)
        minus = model.projection_state(matrix-step*dmatrix, target-step*dtarget)
        difference = (plus["residual"]-minus["residual"])/(2*step)
        np.testing.assert_allclose(result["derivative"], difference, atol=1e-7)
        np.testing.assert_allclose(result["derivative"], result["forcing"]+result["homogeneous"], atol=1e-14)

    def test_formal_forced_example_is_not_homogeneous_propagation(self):
        matrix = np.vstack((np.eye(56), np.zeros((28, 56))))
        left = np.eye(84)[56]
        initial = matrix @ np.ones(56)
        at_zero = model.compatibility_transport(matrix, initial, np.zeros_like(matrix), left)
        later = model.compatibility_transport(matrix, initial+.2*left, np.zeros_like(matrix), left)
        np.testing.assert_allclose(at_zero["residual"], np.zeros(84), atol=1e-14)
        np.testing.assert_allclose(later["residual"], .2*left, atol=1e-14)
        np.testing.assert_allclose(later["forcing"], left, atol=1e-14)
        np.testing.assert_allclose(later["homogeneous"], np.zeros(84), atol=1e-14)

    def test_singular_augmented_matrix_rejected(self):
        with self.assertRaises(ValueError):
            model.projection_state(np.zeros((84, 56)), np.zeros(84))


class NormalCompatibilitySplitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Normal_Compatibility_Split.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.general.domain.load_data()
        cls.services = model.prior.create_container().services()

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_dimensions_and_known_left_identities_at_all_samples(self):
        for sample in self.report["samples"]:
            self.assertEqual(sample["block_dimensions"], {"spatial": 12, "gravity": 4,
                "Lorentz_representative": 6, "mixed": 6})
            self.assertEqual(sample["old_rank"], 34)
            self.assertEqual(sample["full_rank"], 40)
            for key in ("selector_matrix_error", "Lorentz_matrix_error", "known_span_old_left_error", "full_left_split_error"):
                self.assertLess(sample[key], 1e-10)

    def test_Lorentz_identity_uses_unfitted_residuals_too(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["Lorentz_actual_identity_norm"], 1e-10)
            self.assertLess(sample["Lorentz_unfitted_identity_norm"], 1e-10)
        x = np.array([.3, -.2, .4, .1])/16384
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x)
        values = model.general.normal_values(fields)+np.random.default_rng(1910285).normal(size=56)*.2
        varied = model.general.with_normal_values(fields, values)
        result = model.general.equations(self.prepared, varied)["vector"]
        _, rows = model.known_rows(fields)
        self.assertGreater(np.linalg.norm(result), .01)
        np.testing.assert_allclose(rows @ result, np.zeros(6), atol=1e-10)

    def test_projector_blocks_replay_and_are_orthogonal(self):
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, np.eye(4)[1]/16384)
        matrix = model.general.normal_system(self.prepared, fields, services=self.services)["matrix"]
        split = model.split_projectors(matrix, fields)
        blocks = [split[k] for k in ("spatial", "gravity", "Lorentz_representative", "mixed")]
        for i, block in enumerate(blocks):
            np.testing.assert_allclose(block, block.T, atol=1e-12)
            np.testing.assert_allclose(block @ block, block, atol=1e-12)
            np.testing.assert_allclose(block @ matrix, np.zeros_like(matrix), atol=1e-10)
            for other in blocks[:i]:
                np.testing.assert_allclose(block @ other, np.zeros_like(block), atol=1e-12)
        np.testing.assert_allclose(sum(blocks), split["full_left"], atol=1e-12)

    def test_six_remaining_gates_cannot_be_removed_by_normal_refit(self):
        self.assertGreater(max(s["remaining_mixed_gate_norm"] for s in self.report["samples"]), 1e-8)
        self.assertLess(max(s["remaining_normal_variation_error"] for s in self.report["samples"]), 1e-10)

    def test_kinematic_constraint_identity_on_actual_field(self):
        x = np.array([.3, -.2, .4, .1])/16384
        step = 1e-7
        fields = lambda y: model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, y)
        derivative = np.array([(fields(x+step*e)["constraint"]-fields(x-step*e)["constraint"])/(2*step)
                               for e in np.eye(4)])
        mixed = model.general.equations(self.prepared, fields(x))["mixed_curl"]
        spatial_temporal_gradient = derivative[1:, :, 0]
        np.testing.assert_allclose(derivative[0, :, 1:].T, mixed+spatial_temporal_gradient, atol=1e-7)

    def test_transport_diagnostic_retains_nonzero_forcing_and_scope(self):
        diagnostic = self.report["transport_diagnostic"]
        self.assertGreater(diagnostic["minimum_augmented_singular"], .1)
        for value in diagnostic["differences"]:
            self.assertGreater(value["forcing_norm"], 1e-3)
            self.assertLess(value["transport_difference_error"], 1e-5)
        for key in ("six_Lorentz_rows_are_identities_not_independent_initial_constraints",
                    "constitutive_propagation_requires_temporal_constraint_and_all_mixed_curls",
                    "remaining_six_gate_propagation_not_closed", "projector_transport_forcing_not_shown_homogeneous",
                    "not_full_constraint_propagation_or_regional_existence"):
            self.assertTrue(self.report[key])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
