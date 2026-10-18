"""Higher elimination versus source fixing with prescribed finite tangential jets."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "normal_source_compatibility_test", ROOT / "analysis/HC_Cartan_Normal_Source_Compatibility.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class NormalSourceCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, cls.starting = model.neighborhood.load_data()
        cls.reduction = model.normal.build_reduction(cls.prepared, cls.point)
        cls.system = model.assemble(cls.prepared, cls.point, cls.jets, cls.reduction)
        cls.full = model.elimination(cls.system["matrix"], cls.system["source"], cls.system["base"])
        cls.blocks = model.allowed_cauchy_coordinates()
        cls.allowed = sum(cls.blocks.values(), [])
        cls.fixed = np.setdiff1d(np.arange(1200), cls.allowed)
        cls.cauchy = model.elimination(cls.system["matrix"][:, cls.allowed], cls.system["source"], cls.system["base"])
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Normal_Source_Compatibility.json").read_text(encoding="utf-8"))

    def test_current_fingerprints_and_singular_gap(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.system["matrix"].shape, (384, 1200))
        self.assertEqual(self.full["rank"], 332)
        self.assertGreater(self.full["singular"][331], .001)
        self.assertLess(self.full["singular"][332], 1e-8)

    def test_frozen_response_rank_six_is_not_the_eliminated_gate_rank(self):
        self.assertEqual(np.linalg.matrix_rank(self.system["source"], tol=1e-8), 6)
        self.assertEqual(self.full["gate_rank"], 0)
        self.assertLess(np.linalg.norm(self.full["gate"]), 1e-8)
        self.assertLess(np.linalg.norm(self.system["matrix"] @ self.full["source_lift"]+self.system["source"]), 1e-8)

    def test_joint_finite_affinity_with_simultaneous_normal_and_higher_changes(self):
        rng = np.random.default_rng(8393)
        q, z = rng.normal(size=6)*.003, rng.normal(size=1200)*.003
        p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, z)
        actual = model.regular.equations(self.prepared, p, higher)["vector"]
        expected = self.system["base"]+self.system["source"] @ q+self.system["matrix"] @ z
        np.testing.assert_allclose(actual, expected, atol=2e-9)

    def test_arbitrary_six_source_values_have_full_higher_lifts_at_this_order(self):
        rng = np.random.default_rng(5192)
        for _ in range(3):
            q = rng.normal(size=6)*.01
            z = self.full["base_lift"]+self.full["source_lift"] @ q
            p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, z)
            result = model.regular.equations(self.prepared, p, higher)
            self.assertLess(np.linalg.norm(model.normal.normal_equations(self.prepared, p)), 1e-10)
            self.assertLess(np.linalg.norm(result["vector"]), 1e-8)
            self.assertLess(np.linalg.norm(result["constraint_second"]), 1e-8)

    def test_minimum_lift_and_higher_kernel_freedom(self):
        q = np.array([.01, -.005, .003, .002, .004, -.001])
        z = self.full["base_lift"]+self.full["source_lift"] @ q
        np.testing.assert_allclose(self.full["inverse"] @ self.system["matrix"] @ z, z, atol=1e-9)
        seed = np.random.default_rng(6573).normal(size=1200)*.001
        kernel = seed-self.full["inverse"] @ (self.system["matrix"] @ seed)
        self.assertGreater(np.linalg.norm(kernel), .01)
        self.assertLess(np.linalg.norm(self.system["matrix"] @ kernel), 1e-8)
        p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, z+kernel)
        self.assertLess(np.linalg.norm(model.regular.equations(self.prepared, p, higher)["vector"]), 1e-8)

    def test_fixing_psi2_produces_a_real_rank_six_compatibility_gate(self):
        restricted = model.elimination(self.system["matrix"][:, 240:], self.system["source"], self.system["base"])
        self.assertEqual(restricted["rank"], 177)
        self.assertEqual(restricted["gate_rank"], 6)
        q = np.array([.01, -.005, .003, .002, .004, -.001])
        z = np.zeros(1200)
        z[240:] = restricted["base_lift"]+restricted["source_lift"] @ q
        p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, z)
        actual = model.regular.equations(self.prepared, p, higher)["vector"]
        projected = restricted["base_gate"]+restricted["gate"] @ q
        self.assertGreater(np.linalg.norm(actual), .005)
        self.assertAlmostEqual(np.linalg.norm(actual), np.linalg.norm(projected), places=8)

    def test_mask_sizes_and_global_real_imaginary_packing(self):
        self.assertEqual({key: len(value) for key, value in self.blocks.items()},
                         {"psi2": 96, "lambda2": 64, "e3": 64, "psi3": 240})
        self.assertEqual(len(set(self.allowed)), 464)
        self.assertEqual(len(self.fixed), 736)
        expected = list(range(48))+list(range(120, 168))+list(range(240, 304))
        expected += list(range(400, 464))+list(range(720, 840))+list(range(960, 1080))
        self.assertEqual(self.allowed, expected)

    def test_mask_freezes_tangential_derivatives_of_E_Et_psi_and_lambda(self):
        z = np.zeros(1200)
        z[self.allowed] = np.random.default_rng(9751).normal(size=464)
        delta = model.regular.unpack(z)
        for i in range(1, 4):
            for j in range(1, 4):
                np.testing.assert_array_equal(delta["p2"][i, j], np.zeros((3, 4)))
                np.testing.assert_array_equal(delta["l2"][i, j], np.zeros((4, 4)))
                np.testing.assert_array_equal(delta["e3"][0, i, j], np.zeros((4, 4)))
                for k in range(1, 4):
                    np.testing.assert_array_equal(delta["e3"][i, j, k], np.zeros((4, 4)))
                    np.testing.assert_array_equal(delta["p3"][i, j, k], np.zeros((3, 4)))

    def test_fixed_tangential_jet_has_injective_source_gate(self):
        self.assertEqual(self.cauchy["rank"], 200)
        self.assertEqual(self.cauchy["gate_rank"], 6)
        self.assertGreater(self.cauchy["gate_singular"][-1], .13)
        q = model.prescribed_source_law(self.system, self.cauchy, self.allowed, np.zeros(736))["source"]
        self.assertLess(np.linalg.norm(q), 1e-8)

    def test_compatible_changed_prescribed_data_recover_nonzero_sources(self):
        rng = np.random.default_rng(6522)
        for _ in range(3):
            q = rng.normal(size=6)*.01
            known_z = self.full["base_lift"]+self.full["source_lift"] @ q
            result = model.prescribed_source_law(self.system, self.cauchy, self.allowed, known_z[self.fixed])
            np.testing.assert_allclose(result["source"], q, atol=1e-8)
            np.testing.assert_array_equal(result["higher_increment"][self.fixed], known_z[self.fixed])
            p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], result["source"], result["higher_increment"])
            self.assertLess(np.linalg.norm(model.normal.normal_equations(self.prepared, p)), 1e-10)
            self.assertLess(np.linalg.norm(model.regular.equations(self.prepared, p, higher)["vector"]), 1e-8)

    def test_incompatible_prescribed_data_are_not_silently_projected(self):
        data = np.random.default_rng(7154).normal(size=736)*.01
        with self.assertRaisesRegex(ValueError, "compatibility"):
            model.prescribed_source_law(self.system, self.cauchy, self.allowed, data)

    def test_prescribed_data_compatibility_rank_is_not_a_physical_mode_count(self):
        projected = self.cauchy["left_null"].T @ self.system["matrix"][:, self.fixed]
        law = -np.linalg.pinv(self.cauchy["gate"], rcond=1e-10) @ projected
        remainder = projected+self.cauchy["gate"] @ law
        self.assertEqual(law.shape, (6, 736))
        self.assertEqual(np.linalg.matrix_rank(remainder, tol=1e-8), 126)

    def test_later_1114_completion_is_not_silently_claimed_preserved(self):
        q = np.asarray(self.report["example_source_values"])
        z = np.asarray(self.report["example_higher_increment"])
        p, higher = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, z)
        self.assertLess(np.linalg.norm(model.regular.equations(self.prepared, p, higher)["vector"]), 1e-8)
        later = model.later_residual(self.prepared, p, z, self.starting)
        self.assertGreater(np.linalg.norm(later["vector"]), 90.)
        self.assertGreater(np.linalg.norm(later["old"]), .4)

    def test_no_change_to_lower_state_spatial_point_jets_or_couplings(self):
        q = np.asarray(self.report["example_source_values"])
        p, _ = model.changed_fields(self.point, self.jets, self.reduction["sources"], q, np.zeros(1200))
        np.testing.assert_array_equal(p["psi_first"], self.point["psi_first"])
        np.testing.assert_array_equal(p["multiplier"], self.point["multiplier"])
        np.testing.assert_array_equal(p["multiplier_first"][1:], self.point["multiplier_first"][1:])
        np.testing.assert_array_equal(p["coframe_second"][1:], self.point["coframe_second"][1:])

    def test_invalid_shapes_and_noninjective_source_law_are_rejected(self):
        with self.assertRaises(ValueError):
            model.changed_fields(self.point, self.jets, self.reduction["sources"], np.zeros(5), np.zeros(1200))
        with self.assertRaises(ValueError):
            model.prescribed_source_law(self.system, self.cauchy, self.allowed, np.zeros(735))
        with self.assertRaises(ValueError):
            model.prescribed_source_law(self.system, self.full, list(range(1200)), np.zeros(0))

    def test_scope_remains_finite_order_and_not_gauge_or_regional_evolution(self):
        self.assertTrue(self.report["not_free_regional_functions_or_gauge_classification"])
        self.assertTrue(self.report["not_preservation_of_all_1114_equations"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
