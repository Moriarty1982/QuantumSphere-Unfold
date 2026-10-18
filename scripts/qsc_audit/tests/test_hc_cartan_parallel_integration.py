"""Cross-check parallel results against the same preserved lower data and inputs."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
ANALYSIS = ROOT / "analysis"
SPEC = importlib.util.spec_from_file_location("cartan_parallel_neighborhood", ANALYSIS / "HC_Cartan_Regular_Neighborhood.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)
SCALAR_SPEC = importlib.util.spec_from_file_location("cartan_parallel_scalar", ANALYSIS / "HC_Cartan_Next_Scalar_Compatibility.py")
scalar = importlib.util.module_from_spec(SCALAR_SPEC)
SCALAR_SPEC.loader.exec_module(scalar)


class HCCartanParallelIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.original = model.load_data()
        cls.scalar_report = json.loads((ANALYSIS / "HC_Cartan_Next_Scalar_Compatibility.json").read_text(encoding="utf-8"))
        cls.multiplier_report = json.loads((ANALYSIS / "HC_Cartan_Remaining_Multiplier.json").read_text(encoding="utf-8"))
        cls.saved = json.loads((ANALYSIS / "HC_Cartan_Parallel_Neighborhood.json").read_text(encoding="utf-8"))
        cls.result = model.completed_scalar_neighborhood(cls.prepared, cls.point, cls.scalar_report)
        cls.completed = model.gravity.unpack(np.array(cls.scalar_report["joint_394_system"]["jet_coordinates"]))

    def test_two_independent_workers_use_the_same_saved_inputs(self):
        for name in ("HC_Cartan_Regular_Gravity.json", "HC_Cartan_Spatial_Propagation.json"):
            actual = hashlib.sha256((ANALYSIS / name).read_bytes()).hexdigest()
            self.assertEqual(self.scalar_report["input_sha256"][name], actual)
            self.assertEqual(self.multiplier_report["input_sha256"][name], actual)

    def test_every_retained_lower_field_and_coupling_was_checked(self):
        self.assertTrue(self.result["retained_lower_point_and_couplings_verified"])
        self.assertTrue(self.scalar_report["joint_394_system"]["lower_point_unchanged"])

    def test_changed_lower_data_or_mass_cannot_be_silently_combined(self):
        for key in ("psi_first_real", "M_real"):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.scalar_report)
                array = np.array(changed["fixed_lower_point_and_couplings"][key])
                array.flat[0] += .1
                changed["fixed_lower_point_and_couplings"][key] = array.tolist()
                with self.assertRaises(ValueError):
                    model.completed_scalar_neighborhood(self.prepared, self.point, changed)

    def test_all_394_equations_reproduce_without_another_fit(self):
        value = model.gravity.equations(self.prepared, self.point, self.completed)["vector"]
        hessian = scalar.scalar_jet(self.prepared, self.point, self.completed)["hessian"]
        full = np.concatenate((value, np.array([hessian[p] for p in model.gravity.prior.PAIR2])))
        self.assertEqual(full.shape, (394,))
        self.assertLess(np.linalg.norm(full), 1e-8)

    def test_radius_is_recomputed_from_changed_higher_coefficients(self):
        old = model.coefficients(self.prepared, self.point, self.original)
        new = model.coefficients(self.prepared, self.point, self.completed)
        self.assertGreater(abs(new["spinor_second"]-old["spinor_second"]), 1)
        self.assertEqual(new, self.result["coefficient_norms"])
        self.assertEqual(model.select_radius(new), self.result["regular_neighborhood"])

    def test_new_estimate_covers_sampled_weights_and_constraint_blocks(self):
        bound = self.result["regular_neighborhood"]
        self.assertTrue(bound["resolved"])
        for sample in self.result["sample_checks_not_the_proof"]:
            self.assertGreaterEqual(sample["probe_minimum_eigenvalue"], bound["probe_eigenvalue_lower_bound"])
            self.assertGreaterEqual(sample["constraint_minimum_singular_value"], bound["constraint_singular_value_lower_bound"])
            self.assertLessEqual(sample["constraint_block_change"], bound["constraint_block_change_bound"])

    def test_retained_point_curvature_does_not_change_with_reprepared_higher_jets(self):
        old = model.gravity.equations(self.prepared, self.point, self.original)["curvature"]
        new = model.gravity.equations(self.prepared, self.point, self.completed)["curvature"]
        np.testing.assert_array_equal(old, new)
        self.assertFalse(self.multiplier_report["main_TeX_or_PDF_changed"])

    def test_saved_cross_result_and_its_scope_are_reproducible(self):
        actual = hashlib.sha256((ANALYSIS / "HC_Cartan_Next_Scalar_Compatibility.json").read_bytes()).hexdigest()
        self.assertEqual(actual, self.saved["next_scalar_input_sha256"])
        self.assertEqual(self.saved["completed_scalar_jet"]["regular_neighborhood"], self.result["regular_neighborhood"])
        self.assertTrue(self.saved["not_full_normal_rank_control"])
        self.assertTrue(self.saved["not_Cauchy_existence_or_physical_scale"])
        self.assertFalse(self.saved["main_TeX_changed"])


if __name__ == "__main__":
    unittest.main()
