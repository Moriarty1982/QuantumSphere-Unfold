"""First primary prolongation and conditional six-source identification."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "first_source_gate_test", ROOT / "analysis/HC_Cartan_First_Compatibility_Source_Gate.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ExtractionTests(unittest.TestCase):
    def test_packing_against_explicit_symmetric_tensor(self):
        rng = np.random.default_rng(191019)
        c1, r1, f1 = rng.normal(size=(4, 4, 4)), rng.normal(size=(4, 24)), rng.normal(size=(4, 4, 4))
        c2 = np.zeros((4, 4, 4, 4))
        unique = rng.normal(size=(10, 4, 4))
        for pair, value in zip(model.source.prior.PAIR2, unique):
            c2[pair[0], pair[1]] = value
            c2[pair[1], pair[0]] = value
        packed = np.concatenate((c1.ravel(), r1[:, :12].ravel(), r1[:, 12:].ravel(), f1.ravel(), unique.ravel()))
        expected = np.concatenate([np.concatenate((c1[r].ravel(), r1[r], f1[r].ravel(),
            np.array([c2[r, 0, :, i]-c2[r, i, :, 0] for i in (1, 2, 3)]).ravel())) for r in range(4)])
        np.testing.assert_allclose(model.extraction_matrix() @ packed, expected, atol=1e-14)

    def test_tall_matrix_retains_extra_left_directions(self):
        matrix = np.vstack((np.eye(2), np.zeros((3, 2))))
        response = np.eye(5)[:, 2:]
        result = model.eliminate(matrix, response)
        self.assertEqual(result["left_null"].shape, (5, 3))
        self.assertEqual(result["gate_rank"], 3)
        np.testing.assert_allclose(result["left_null"].T @ matrix, 0, atol=1e-14)


class SourceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_First_Compatibility_Source_Gate.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_full_spatial_gate_but_no_time_only_gate(self):
        self.assertEqual(self.report["source_gate_rank"], 6)
        self.assertEqual(self.report["time_only_gate_rank"], 0)
        self.assertGreater(min(self.report["source_gate_singular_values"]), .13)

    def test_prolongation_dimensions_and_cancellation(self):
        self.assertEqual((self.report["equations"], self.report["normal_higher_coordinates"]), (272, 224))
        self.assertEqual((self.report["higher_rank"], self.report["left_nullity"]), (160, 112))
        self.assertLess(self.report["psi3_response_norm"], 1e-10)

    def test_candidate_source_recovery_and_direct_affinity(self):
        for key in ("candidate_residual_norm", "source_recovery_error", "projected_compatibility_norm"):
            self.assertLess(self.report[key], 1e-8)
        self.assertLess(max(self.report["direct_affinity_errors"]), 1e-8)

    def test_against_actual_general_equation_derivatives(self):
        spec = importlib.util.spec_from_file_location(
            "first_gate_general", ROOT / "analysis/HC_Cartan_General_Normal_Chart.py")
        general = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(general)
        prepared, point, jets, _, full, _ = general.domain.load_data()
        expected = model.extraction_matrix() @ model.source.regular.equations(prepared, point, jets)["vector"]
        rows = []
        step = 1e-7
        for direction in np.eye(4):
            plus = general.domain.temporal.fields(prepared, point, jets, full, step*direction)
            minus = general.domain.temporal.fields(prepared, point, jets, full, -step*direction)
            rows.append((general.equations(prepared, plus)["vector"]-general.equations(prepared, minus)["vector"])/(2*step))
        np.testing.assert_allclose(np.concatenate(rows), expected, atol=2e-5, rtol=1e-6)


if __name__ == "__main__":
    unittest.main()
