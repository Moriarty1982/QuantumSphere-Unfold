"""Bounded second-constitutive principal image and metric compatibility checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "second_constitutive_symmetry_test", ROOT / "analysis/HC_Cartan_Second_Constitutive_Symmetry.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class SecondConstitutiveSymmetryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, _ = model.neighborhood.load_data()
        cls.principal = model.spatial.constraint_principal_map(cls.prepared["data"]["psi"])
        cls.matrix = model.principal_matrix(cls.principal)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Second_Constitutive_Symmetry.json")
                                .read_text(encoding="utf-8"))

    def test_source_fingerprints_and_saved_rank(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["map_rank"], 80)
        np.testing.assert_allclose(self.report["principal"], self.principal, atol=1e-12)

    def test_principal_rank_and_global_real_imaginary_order(self):
        self.assertEqual(self.principal.shape, (4, 24))
        self.assertEqual(np.linalg.matrix_rank(self.principal, tol=1e-10), 4)
        self.assertEqual(self.matrix.shape, (160, 480))
        singular = np.linalg.svd(self.matrix, compute_uv=False)
        self.assertGreater(singular[79], 1e-3)
        self.assertLess(singular[80], 1e-10)
        x = np.random.default_rng(11).normal(size=480)
        tensor = model.prolong.unpack_third(x, True)
        expected = np.array([[self.principal @ model.prior.realify(tensor[r, s, mu])
                              for mu in range(4)] for r, s in model.PAIRS]).transpose(0, 2, 1)
        np.testing.assert_allclose(self.matrix @ x, expected.reshape(160), atol=1e-12)

    def test_full_metric_projection_equals_explicit_tensor_symmetrization(self):
        x = np.random.default_rng(12).normal(size=160)
        tensor = model.unpack_second(x)
        # First two indices are already symmetric: three distinct placements suffice.
        sym = (tensor+tensor.transpose(0, 3, 2, 1)+tensor.transpose(3, 1, 2, 0))/3
        image, defect, _ = model.project(x)
        np.testing.assert_allclose(image, model.pack_second(sym), atol=1e-14)
        np.testing.assert_allclose(model.project(image)[0], image, atol=1e-14)
        weights = np.repeat(model.PAIR_WEIGHTS, 16)
        self.assertAlmostEqual(np.dot(weights*x, x), np.linalg.norm(tensor)**2, places=11)
        self.assertLess(abs(np.dot(weights*image, defect)), 1e-12)
        self.assertLess(np.linalg.norm(model.compatibility(image)), 1e-12)

    def test_projector_is_weighted_self_adjoint_and_has_rank_80(self):
        p = np.column_stack([model.project(v)[0] for v in np.eye(160)])
        w = np.repeat(model.PAIR_WEIGHTS, 16)
        np.testing.assert_allclose(w[:, None]*p, p.T*w[None, :], atol=1e-14)
        self.assertEqual(np.linalg.matrix_rank(p, tol=1e-10), 80)
        np.testing.assert_allclose(p @ self.matrix, self.matrix, atol=1e-12)
        c = np.column_stack([model.compatibility(v) for v in np.eye(160)])
        self.assertEqual(c.shape, (80, 160))
        self.assertEqual(np.linalg.matrix_rank(c, tol=1e-10), 80)
        np.testing.assert_allclose(c @ self.matrix, 0, atol=1e-12)

    def test_negative_control_distinguishes_full_and_unique_metrics(self):
        source = np.zeros((10, 4, 4))
        source[model.PAIRS.index((0, 0)), 0, 1] = 1
        source = source.reshape(160)
        full, defect, _ = model.project(source)
        unique, _, _ = model.project(source, "unique")
        self.assertAlmostEqual(full.reshape(10, 4, 4)[0, 0, 1], 1/3)
        self.assertAlmostEqual(unique.reshape(10, 4, 4)[0, 0, 1], 1/2)
        self.assertAlmostEqual(np.linalg.norm(model.unpack_second(defect))**2, 2/3)
        self.assertGreater(np.linalg.norm(model.compatibility(source)), .9)
        lifted = model.minimum_norm_lift(self.principal, source)
        np.testing.assert_allclose(self.matrix @ lifted, full, atol=1e-12)
        self.assertGreater(np.linalg.norm(self.matrix @ lifted-source), .7)
        control = self.report["negative_control"]
        self.assertLess(control["direct_regular_defect_error"], 1e-9)
        self.assertAlmostEqual(control["direct_regular_residual_full_norm"], np.sqrt(2/3), places=9)

    def test_direct_regular_equations_and_projected_cancellation(self):
        before = {k: v.copy() for k, v in self.jets.items()}
        rows, starting = model.direct_checks(self.prepared, self.point, self.jets, self.principal)
        for row in rows:
            self.assertLess(row["principal_error"], 1e-9)
            self.assertEqual(row["connection_second_error"], 0.)
            self.assertEqual(row["other_equations_error"], 0.)
        self.assertLess(starting["projected_cancellation_error"], 1e-9)
        self.assertAlmostEqual(starting["remaining_full_norm"], starting["uncancellable_full_norm"], places=9)
        for k, v in before.items():
            np.testing.assert_array_equal(self.jets[k], v)

    def test_compatible_targets_have_symmetric_lifts(self):
        x = np.random.default_rng(14).normal(size=160)
        image, _, _ = model.project(x)
        lifted = model.minimum_norm_lift(self.principal, image)
        np.testing.assert_allclose(self.matrix @ lifted, image, atol=1e-12)
        tensor = model.prolong.unpack_third(lifted, True)
        np.testing.assert_array_equal(tensor, tensor.swapaxes(0, 2))
        np.testing.assert_array_equal(tensor, tensor.swapaxes(0, 1))

    def test_invalid_inputs_and_nonsurjective_lift(self):
        for bad in (np.zeros(159), np.full(160, np.nan), np.zeros(160, complex)):
            with self.assertRaises(ValueError):
                model.project(bad)
        with self.assertRaises(ValueError):
            model.project(np.zeros(160), "other")
        with self.assertRaises(ValueError):
            model.minimum_norm_lift(np.zeros((4, 24)), np.zeros(160))


if __name__ == "__main__":
    unittest.main()
