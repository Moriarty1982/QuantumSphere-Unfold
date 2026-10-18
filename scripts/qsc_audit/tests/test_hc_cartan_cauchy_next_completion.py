"""Finite next-order compatibility with unchanged tangential data."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "next_cauchy_test", ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class NextCauchyCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, cls.jets, _, cls.saved = model.source.neighborhood.load_data()
        reduction = model.source.normal.build_reduction(cls.prepared, cls.point)
        cls.changed = model.source.normal.remaining.normal_point(cls.point, reduction["sources"] @ np.array(cls.report["source_values"]))
        cls.c = np.array(cls.report["starting_coordinates"])
        cls.h = np.array(cls.report["starting_highest"])
        cls.lc = model.joint.third.lc_cubic(cls.prepared, cls.changed)
        cls.base = model.evaluate_fields(cls.prepared, cls.changed, cls.c, cls.h, cls.lc)
        cls.high = model.highest_matrix(cls.prepared)
        cls.mask = sum(model.highest_mask().values(), [])
        cls.older = [i for i in sum(model.source.allowed_cauchy_coordinates().values(), []) if i >= 240]

    def fields(self, coordinates, highest):
        return model.evaluate_fields(self.prepared, self.changed, coordinates, highest, self.lc)

    def test_current_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_exact_highest_mask_and_counts(self):
        self.assertEqual({k: len(v) for k, v in model.highest_mask().items()}, {"e4": 160, "l3": 160, "p4": 480})
        self.assertEqual(self.mask, list(range(160))+list(range(560, 720))+list(range(880, 1360)))

    def test_highest_mask_preserves_surface_traces_and_coframe_velocity(self):
        vector = np.zeros(1720)
        vector[self.mask] = np.random.default_rng(2125).normal(size=800)
        diagnostic = model.joint.third.diagnostic
        x = np.array([0., .02, -.03, .04])
        e4 = vector[:560].reshape(35, 4, 4)
        l3 = vector[560:880].reshape(20, 4, 4)
        p4 = vector[880:].reshape(35, 24)
        for values, order in ((e4, 4), (l3, 3), (p4, 4)):
            np.testing.assert_array_equal(diagnostic.homogeneous_jet(values, order, x), np.zeros(values.shape[1:]))
        np.testing.assert_array_equal(diagnostic.homogeneous_jet(e4, 4, x, derivative=(0,)), np.zeros((4, 4)))

    def test_psi4_is_realified_per_quartet(self):
        principal = model.source.spatial.constraint_principal_map(self.prepared["data"]["psi"])
        p4 = np.zeros((35, 24))
        p4[7, 19] = 1
        actual = model.joint.third.diagnostic.principal_image(principal, p4)
        np.testing.assert_allclose(self.high[-320:, 880:] @ p4.reshape(-1), actual.reshape(-1), atol=1e-12)

    def test_actual_highest_response_preserves_all_old_rows(self):
        delta = np.random.default_rng(8458).normal(size=1720)*.01
        actual = self.fields(self.c, self.h+delta)["vector"]-self.base["vector"]
        expected = np.concatenate((np.zeros(394), self.high @ delta))
        np.testing.assert_allclose(actual, expected, atol=2e-8, rtol=1e-9)
        np.testing.assert_array_equal(actual[:394], np.zeros(394))

    def test_frozen_384_lift_still_fails_the_extra_scalar_rows(self):
        self.assertLess(np.linalg.norm(self.base["old"][:384]), 1e-8)
        self.assertGreater(np.linalg.norm(self.base["old"][384:]), .4)
        self.assertGreater(np.linalg.norm(self.base["vector"]), 90)

    def test_both_highest_gates_retain_the_old_obstruction(self):
        for name, allowed, rank in (("unrestricted_highest", list(range(1720)), 363),
                                    ("tangential_highest_fixed", self.mask, 240)):
            solved = model.solve_affine(self.high[:, allowed], self.base["vector"][394:])
            self.assertEqual(solved["rank"], rank)
            h = self.h.copy()
            h[allowed] += solved["solution"]
            actual = self.fields(self.c, h)
            np.testing.assert_allclose(actual["old"], self.base["old"], atol=1e-12)
            self.assertGreater(np.linalg.norm(actual["vector"]), 20)
            self.assertAlmostEqual(np.linalg.norm(actual["vector"]),
                                   self.report["highest_only_controls"][name]["all_1114_norm"], places=7)

    def test_reprepared_witness_retains_all_prescribed_entries(self):
        c, h = np.array(self.report["fitted_coordinates"]), np.array(self.report["fitted_highest"])
        fixed = np.setdiff1d(np.arange(1200), self.older)
        high_fixed = np.setdiff1d(np.arange(1720), self.mask)
        self.assertEqual(len(self.older), 368)
        np.testing.assert_array_equal(c[fixed], self.c[fixed])
        np.testing.assert_array_equal(h[high_fixed], self.h[high_fixed])
        actual = self.fields(c, h)
        self.assertAlmostEqual(np.linalg.norm(actual["vector"]), self.report["reprepared"]["all_1114_norm"], places=7)
        self.assertGreater(np.linalg.norm(actual["vector"]), 30)

    def test_affinity_with_fixed_psi2_and_simultaneous_older_highest_changes(self):
        rng = np.random.default_rng(9498)
        dc, dh = np.zeros(1200), np.zeros(1720)
        dc[self.older], dh[self.mask] = rng.normal(size=368)*.003, rng.normal(size=800)*.003
        f0 = self.base["vector"]
        older = self.fields(self.c+dc, self.h)["vector"]
        high = self.fields(self.c, self.h+dh)["vector"]
        both = self.fields(self.c+dc, self.h+dh)["vector"]
        twice = self.fields(self.c+2*dc, self.h)["vector"]
        np.testing.assert_allclose(both, older+high-f0, atol=2e-8, rtol=1e-9)
        np.testing.assert_allclose(twice, 2*older-f0, atol=2e-8, rtol=1e-9)

    def test_point_normal_equations_are_not_the_failing_higher_conditions(self):
        self.assertLess(np.linalg.norm(model.source.normal.normal_equations(self.prepared, self.changed)), 1e-10)

    def test_old_first_solution_is_recomputed_without_discarding_rows(self):
        c, h = np.array(self.report["old_first_coordinates"]), np.array(self.report["old_first_highest"])
        actual = self.fields(c, h)
        self.assertAlmostEqual(np.linalg.norm(actual["vector"]), self.report["old_first"]["all_1114_norm"], places=7)
        self.assertAlmostEqual(np.linalg.norm(actual["old"]), self.report["old_first"]["old_394_norm"], places=7)
        self.assertLess(np.linalg.norm(actual["old"]), 1e-8)
        self.assertGreater(np.linalg.norm(actual["vector"]), 30)
        np.testing.assert_array_equal(c[:240], self.c[:240])

    def test_original_saved_1114_completion_is_not_invalidated(self):
        h = np.concatenate((self.saved["connection_coordinates"], np.asarray(self.saved["fourth_spinor_real"]).reshape(-1)))
        lc = model.joint.third.lc_cubic(self.prepared, self.point)
        original = model.evaluate_fields(self.prepared, self.point, np.asarray(self.saved["jet_coordinates"]), h, lc)
        self.assertLess(np.linalg.norm(original["vector"]), 1e-8)

    def test_scope_excludes_all_earlier_psi2_repreparation_and_regional_claims(self):
        self.assertTrue(self.report["not_full_earlier_normal_jet_repreparation"])
        self.assertTrue(self.report["not_general_nonexistence_or_regional_evolution"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_invalid_highest_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            self.fields(self.c, np.zeros(1719))


if __name__ == "__main__":
    unittest.main()
