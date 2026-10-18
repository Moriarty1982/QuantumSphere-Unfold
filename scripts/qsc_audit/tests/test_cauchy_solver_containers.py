"""Typed finite-system containers and shared rank/inverse behavior."""
from dataclasses import FrozenInstanceError
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "solver_containers", ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class SolverContainerTests(unittest.TestCase):
    def setUp(self):
        test_root = ROOT / "build/cache-tests"
        test_root.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=test_root)
        self.addCleanup(directory.cleanup)
        cache = model.cache.MatrixCache(Path(directory.name))
        patcher = patch.object(model.cache, "CACHE", cache)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_affine_arrays_round_trip(self):
        system = model.AffineSystem(np.eye(3), np.ones(3), (240, 400), (880,))
        restored = model.AffineSystem.from_arrays(system.to_arrays())
        np.testing.assert_array_equal(restored.matrix, system.matrix)
        self.assertEqual(restored.older, system.older)
        self.assertEqual(restored.highest, system.highest)
        self.assertEqual(restored.older_count, 2)

    def test_coordinate_ownership_and_nonmutation(self):
        system = model.AffineSystem(np.eye(3), np.zeros(3), (240, 400), (880,))
        coordinates, highest = np.zeros(1200), np.zeros(1720)
        changed, new_highest = system.apply(coordinates, highest, np.array([1., 2., 3.]))
        np.testing.assert_array_equal(changed[[240, 400]], [1., 2.])
        self.assertEqual(new_highest[880], 3.)
        self.assertEqual(np.count_nonzero(changed), 2)
        self.assertEqual(np.count_nonzero(new_highest), 1)
        self.assertFalse(np.any(coordinates))
        self.assertFalse(np.any(highest))

    def test_bad_shapes_and_coordinate_masks_are_rejected(self):
        for matrix, base, older, highest in (
            (np.eye(2), np.zeros(3), (240,), (880,)),
            (np.eye(2), np.zeros(2), (240,), ()),
            (np.eye(2), np.zeros(2), (240, 240), ()),
            (np.eye(2), np.zeros(2), (-1,), (880,)),
            (np.eye(2), np.zeros(2), (1200,), (880,)),
            (np.eye(2), np.zeros(2), (240,), (1720,)),
            (np.eye(2), np.zeros(2), (True,), (880,)),
            (np.eye(2), np.zeros(2), (240.5,), (880,)),
            (np.full((2, 2), np.nan), np.zeros(2), (240,), (880,)),
        ):
            with self.subTest(older=older, highest=highest):
                with self.assertRaises(ValueError):
                    model.AffineSystem(matrix, base, older, highest)

    def test_bad_increment_is_rejected_before_modification(self):
        system = model.AffineSystem(np.eye(2), np.zeros(2), (240,), (880,))
        with self.assertRaises(ValueError):
            system.apply(np.zeros(1200), np.zeros(1720), np.ones(3))

    def test_container_field_bindings_are_frozen(self):
        system = model.AffineSystem(np.eye(2), np.zeros(2), (240,), (880,))
        with self.assertRaises(FrozenInstanceError):
            system.older = (400,)

    def test_reduction_owns_its_matrix_and_reuses_decomposition(self):
        matrix = np.diag([2., 1e-6, 0.])
        reduction = model.SVDReduction.from_matrix(matrix)
        matrix[:] = 0
        self.assertFalse(reduction.matrix.flags.writeable)
        result = reduction.solve(np.array([1., 2., 3.]))
        self.assertEqual(result["rank"], 2)
        np.testing.assert_allclose(result["remainder"], [0, 0, 3])

    def test_wide_kernel_is_complete_when_requested(self):
        matrix = np.array([[1., 0., 0.], [0., 0., 0.]])
        economy = model.SVDReduction.from_matrix(matrix)
        with self.assertRaisesRegex(ValueError, "full right basis"):
            _ = economy.kernel
        reduction = model.SVDReduction.from_matrix(matrix, retain_kernel=True)
        self.assertEqual(reduction.kernel.shape, (3, 2))
        np.testing.assert_allclose(matrix @ reduction.kernel, 0, atol=1e-12)

    def test_zero_rank_report_does_not_invent_retained_singular_value(self):
        result = model.solve_affine(np.zeros((3, 2)), np.ones(3))
        self.assertEqual(result["rank"], 0)
        self.assertIsNone(model.solve_report(result)["smallest_retained_singular"])
        np.testing.assert_array_equal(result["solution"], np.zeros(2))
        np.testing.assert_array_equal(result["remainder"], np.ones(3))

    def test_empty_reduction_is_rejected(self):
        with self.assertRaises(ValueError):
            model.SVDReduction.from_matrix(np.zeros((0, 3)))


if __name__ == "__main__":
    unittest.main()
