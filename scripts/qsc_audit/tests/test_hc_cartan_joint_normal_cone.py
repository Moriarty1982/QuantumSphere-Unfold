"""Tilt normalization, direct real principal law and uniform subblock bounds."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_joint_normal_cone", ROOT / "analysis/HC_Cartan_Joint_Normal_Cone.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class JointNormalConeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, cls.extras, _ = model.neighborhood.load_data()
        cls.data = model.neighborhood.coefficient_norms(cls.prepared, cls.point, cls.jets, cls.extras)
        cls.ball = model.neighborhood.select_radius(cls.data)
        cls.cone = model.cone_bound(cls.prepared, cls.point, cls.jets, cls.extras, cls.data, cls.ball)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Joint_Normal_Cone.json").read_text(encoding="utf-8"))
        cls.psi = cls.prepared["data"]["psi"]
        cls.e = np.eye(4)
        cls.lam = cls.point["multiplier"]

    def test_current_fingerprints_match_saved_cone(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_temporal_normal_reproduces_the_original_schur_block(self):
        actual = model.schur_block(self.e, self.psi, self.lam, [1, 0, 0, 0])
        old = model.neighborhood.rank_model.probe_constraint_block(self.e, self.psi, self.lam)
        np.testing.assert_allclose(actual["block"], old["block"], atol=1e-14)

    def test_direct_real_law_has_the_half_divergence_principal_term(self):
        rng = np.random.default_rng(2814)
        n = np.array([1., .02, -.01, .03])
        u = rng.normal(size=12)+1j*rng.normal(size=12)
        a = rng.normal(size=4)
        p = self.psi.reshape(12)
        divergence = np.einsum("a,aij->ij", a, model.prolong.Q_WEIGHTS)
        weights = model.cartan.kinetic_weights(self.e, self.lam)
        exact = model.neighborhood.third.scalar.odd.real_law.real_operator(
            p, n[:, None]*u, weights, np.zeros((4, 12, 12), complex),
            np.zeros((12, 12), complex), divergence)["symmetric"]
        principal = 1j*np.einsum("m,mij,j->i", n, weights, u)+.5j*divergence @ p
        np.testing.assert_allclose(exact, principal, atol=1e-12)
        matrix = model.partial_matrix(self.e, self.psi, self.lam, n)
        readout = np.array([np.vdot(p, w @ u).imag for w in model.prolong.Q_WEIGHTS])
        np.testing.assert_allclose(matrix @ np.r_[model.prior.realify(u), a],
                                   np.r_[model.prior.realify(exact), readout], atol=1e-12)

    def test_schur_reduction_matches_the_actual_real_matrix(self):
        n = np.array([1., .01, .03, -.02])
        matrix = model.partial_matrix(self.e, self.psi, self.lam, n)
        schur = -matrix[24:, :24] @ np.linalg.solve(matrix[:24, :24], matrix[:24, 24:])
        np.testing.assert_allclose(schur, model.schur_block(self.e, self.psi, self.lam, n)["block"], atol=1e-12)

    def test_covector_rescaling_requires_normalized_constraint_rows(self):
        n = np.array([1., .01, -.02, .03])
        first = model.schur_block(self.e, self.psi, self.lam, n)
        scaled = model.schur_block(self.e, self.psi, self.lam, 2*n)
        np.testing.assert_allclose(scaled["block"], first["block"]/2, atol=1e-12)
        # Raw temporal constitutive rows acquire n0; normalized X.F rows do not.
        matrix = model.partial_matrix(self.e, self.psi, self.lam, 2*n)
        raw_schur = -2*matrix[24:, :24] @ np.linalg.solve(matrix[:24, :24], matrix[:24, 24:])
        np.testing.assert_allclose(raw_schur, first["block"], atol=1e-12)
        self.assertGreater(np.linalg.norm(raw_schur-scaled["block"]), 1e-3)

    def test_nonpositive_probe_normals_are_not_accepted(self):
        with self.assertRaises(ValueError):
            model.schur_block(self.e, self.psi, self.lam, [-1, 0, 0, 0])

    def test_uniform_tilt_retains_at_least_half_temporal_margins(self):
        self.assertGreater(self.cone["tilt_radius"], 0)
        self.assertGreaterEqual(self.cone["probe_eigenvalue_lower_bound"], self.ball["probe_eigenvalue_lower_bound"]/2)
        self.assertGreaterEqual(self.cone["constraint_singular_value_lower_bound"], self.ball["constraint_singular_value_lower_bound"]/2)
        self.assertLess(self.cone["normal_metric_quadratic_upper_bound"], 0)

    def test_sampled_blocks_and_inverse_norms_obey_uniform_estimates(self):
        samples = model.sample_checks(self.prepared, self.point, self.jets, self.extras, self.cone)
        for sample in samples:
            self.assertGreaterEqual(sample["probe_minimum_eigenvalue"], self.cone["probe_eigenvalue_lower_bound"]-1e-12)
            self.assertGreaterEqual(sample["constraint_minimum_singular_value"], self.cone["constraint_singular_value_lower_bound"]-1e-12)
            self.assertLessEqual(sample["normal_metric_quadratic"], self.cone["normal_metric_quadratic_upper_bound"]+1e-12)
            self.assertLessEqual(sample["partial_28_inverse_norm"], self.cone["partial_28_inverse_norm_upper_bound"]+1e-9)

    def test_spatial_multiplier_changes_are_included_not_just_temporal_columns(self):
        changed = dict(self.jets, l2=self.jets["l2"].copy())
        changed["l2"][..., 1:] *= 10
        estimate = model.cone_bound(self.prepared, self.point, changed, self.extras, self.data, self.ball)
        self.assertGreater(estimate["spatial_weight_operator_bound"], self.cone["spatial_weight_operator_bound"])
        self.assertLess(estimate["tilt_radius"], self.cone["tilt_radius"])

    def test_partial_block_does_not_replace_the_full_normal_symbol(self):
        self.assertTrue(self.report["not_full_gravitational_normal_symbol"])
        self.assertTrue(self.report["not_hyperbolicity_or_Cauchy_existence"])
        self.assertTrue(self.report["no_physical_angle_or_length_calibration"])
        self.assertTrue(self.report["not_interval_certified"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
