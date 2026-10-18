"""Uniform Cartan bounds, exact Hessians, and quartic norm countercontrols."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "joint_cartan_regularity", ROOT / "analysis/HC_Cartan_Joint_Cartan_Regularity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class JointCartanRegularityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, cls.extras, cls.joint_report = model.load_data()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Joint_Cartan_Regularity.json").read_text(encoding="utf-8"))
        cls.data = model.coefficient_norms(cls.prepared, cls.point, cls.jets, cls.extras)

    def test_saved_inputs_and_report_are_current(self):
        self.assertEqual(self.report["input_sha256_LF_normalized"], model.input_fingerprints())
        self.assertEqual(self.report["coefficient_norms"], self.data)
        self.assertEqual(self.report["regular_neighborhood"], model.select_radius(self.data))
        self.assertTrue(self.report["finite_float_not_interval_certified"])
        self.assertTrue(self.report["not_full_PDE_existence"])

    def test_full_symmetric_norm_counts_multiplicities(self):
        values = np.zeros((35, 4, 4))
        indices = tuple(model.itertools.combinations_with_replacement(range(4), 4))
        values[indices.index((0, 1, 2, 3)), 0, 0] = 1
        full = model.expand_symmetric(values, 4)
        self.assertAlmostEqual(np.linalg.norm(full), np.sqrt(24))
        self.assertGreater(self.data["coframe_fourth"], self.data["coframe_fourth_unique_unweighted"])

    def test_nonzero_base_margin_and_uniform_ball_including_large_distances(self):
        self.assertAlmostEqual(self.data["minimum_base_hessian_singular_value"], 1.)
        rng = np.random.default_rng(97114)
        for d in (0., .01, .2, .7, .95):
            estimate = model.uniform_bound(self.data, d)
            self.assertGreater(estimate["hessian_singular_value_lower_bound"], 0)
            for _ in range(3):
                delta = rng.normal(size=(4, 4))
                delta *= d/np.linalg.norm(delta, 2)
                e = np.eye(4)+delta
                h = model.exact_hessian(self.prepared, e)
                np.testing.assert_allclose(h, model.congruence_hessian(self.prepared, e), atol=2e-12)
                self.assertGreaterEqual(np.linalg.svd(h, compute_uv=False)[-1]+1e-12,
                                        estimate["hessian_singular_value_lower_bound"])
                self.assertLessEqual(np.linalg.norm(h-self.prepared["hessian"], 2),
                                     estimate["hessian_change_bound"]+1e-12)

    def test_quartic_fields_and_original_polarization_obey_uniform_estimate(self):
        estimate = self.report["regular_neighborhood"]
        for sample in self.report["sample_checks_not_the_proof"]:
            self.assertLessEqual(sample["coframe_change"], estimate["coframe_change_bound"]+1e-14)
            self.assertLessEqual(sample["hessian_change"], estimate["hessian_change_bound"]+1e-12)
            self.assertGreaterEqual(sample["hessian_minimum_singular_value"], estimate["hessian_singular_value_lower_bound"])
            self.assertLessEqual(sample["hessian_inverse_norm"], estimate["hessian_inverse_norm_upper_bound"])
            self.assertLess(sample["polarized_hessian_error"], 1e-12)
            self.assertLess(sample["congruence_error"], 1e-12)
        direction = np.array([.7, -.2, .4, .5])
        direction /= np.linalg.norm(direction)
        f = model.fields(self.prepared, self.point, self.jets, self.extras, estimate["radius"]*direction)
        np.testing.assert_allclose(f["hessian"], model.cartan.contorsion_hessian(f["coframe"]), atol=1e-12)
        self.assertLess(np.linalg.norm(f["Cartan"]), 1e-12)
        self.assertGreater(np.linalg.norm(self.extras["p4"]), 0)
        self.assertGreater(np.linalg.norm(self.extras["l3"]), 0)

    def test_norm_scaling_worsens_bound_and_can_force_smaller_radius(self):
        controls = self.report["norm_scaling_countercontrols"]
        distances = [v["same_radius_bound"]["coframe_change_bound"] for v in controls]
        self.assertTrue(all(b > a for a, b in zip(distances, distances[1:])))
        self.assertLess(controls[-1]["reselected_bound"]["radius"], controls[0]["reselected_bound"]["radius"])
        extras = dict(self.extras, e4=4096*self.extras["e4"])
        scaled = model.coefficient_norms(self.prepared, self.point, self.jets, extras)
        self.assertAlmostEqual(scaled["coframe_fourth"]/self.data["coframe_fourth"], 4096)
        r = model.select_radius(scaled)["radius"]
        x = r*np.array([.5, -.5, .5, .5])
        f = model.fields(self.prepared, self.point, self.jets, extras, x)
        self.assertLessEqual(np.linalg.norm(f["coframe"]-np.eye(4), 2), model.bound(scaled, r)["coframe_change_bound"])
        zero = dict(self.data, coframe_second=0., coframe_third=0., coframe_fourth=0.)
        pure = dict(zero, coframe_fourth=24.)
        self.assertEqual(model.bound(pure, .25)["coframe_change_bound"], .25**4)
        self.assertEqual(model.bound(dict(pure, coframe_fourth=16*24.), .125)["coframe_change_bound"], .25**4)

    def test_shared_parent_radius_has_cartan_margin(self):
        parent = json.loads((ROOT / "analysis/HC_Cartan_Joint_Neighborhood.json").read_text(encoding="utf-8"))
        radius = parent["regular_neighborhood"]["radius"]
        estimate = model.bound(self.data, radius)
        self.assertEqual(estimate, self.report["at_joint_temporal_neighborhood_radius"])
        self.assertAlmostEqual(estimate["coframe_change_bound"], parent["regular_neighborhood"]["coframe_change_bound"], places=20)
        self.assertGreater(estimate["hessian_singular_value_lower_bound"], .9999999)

    def test_independent_fields_match_parent_full_symmetric_fields(self):
        spec = importlib.util.spec_from_file_location(
            "joint_cartan_parent_check", ROOT / "analysis/HC_Cartan_Joint_Neighborhood.py")
        parent = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(parent)
        p, q, j, extras, _ = parent.load_data()
        x = np.array([.7, -.2, .4, .5])*.001
        expected = parent.fields(p, q, j, extras, x)
        actual = model.fields(self.prepared, self.point, self.jets, self.extras, x)
        for name in ("coframe", "psi", "psi_first", "multiplier", "omega"):
            np.testing.assert_allclose(actual[name], expected[name], atol=2e-12, rtol=2e-12)

    def test_invalid_domains_and_zero_hessian_margin_are_rejected(self):
        for d in (-1, 1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                model.uniform_bound(self.data, d)
        with self.assertRaises(ValueError):
            model.uniform_bound(dict(self.data, minimum_base_hessian_singular_value=0), .01)
        with self.assertRaises(ValueError):
            model.bound(self.data, -1)
        self.assertFalse(model.bound(self.data, 1)["resolved"])


if __name__ == "__main__":
    unittest.main()
