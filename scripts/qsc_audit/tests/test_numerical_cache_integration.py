"""Cache invalidation, payload integrity, and current Cartan integration."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_cache_integration", ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)
cache_module = model.cache


class CacheIntegrationTests(unittest.TestCase):
    def setUp(self):
        test_root = ROOT / "build/cache-tests"
        test_root.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=test_root)
        self.addCleanup(self.directory.cleanup)
        self.cache = cache_module.MatrixCache(Path(self.directory.name) / "cache")
        self.patch = patch.object(cache_module, "CACHE", self.cache)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def test_svd_reused_for_different_rhs_but_current_rank_tolerance_retained(self):
        matrix = np.diag([2., 1e-6, 0.])
        original = np.linalg.svd
        with patch.object(np.linalg, "svd", wraps=original) as spy:
            first = model.solve_affine(matrix, np.array([1., 2., 3.]))
            second = model.solve_affine(matrix, np.array([4., 5., 6.]))
            self.assertEqual(spy.call_count, 1)
        self.assertEqual(first["rank"], 2)
        self.assertEqual(second["rank"], 2)
        self.assertFalse(np.array_equal(first["solution"], second["solution"]))
        np.testing.assert_allclose(second["remainder"], [0., 0., 6.])

    def test_changed_svd_mode_and_matrix_recompute(self):
        matrix = np.ones((3, 2))
        original = np.linalg.svd
        with patch.object(np.linalg, "svd", wraps=original) as spy:
            cache_module.svd(matrix)
            full = cache_module.svd(matrix, full_matrices=True)
            cache_module.svd(2*matrix)
            self.assertEqual(spy.call_count, 3)
        self.assertEqual(full[0].shape, (3, 3))

    def test_current_highest_cache_uses_actual_prepared_data_and_provenance(self):
        prepared = {"value": np.ones(2)}
        with patch.object(model, "_highest_matrix", return_value=np.eye(2)) as build:
            model.highest_matrix(prepared)
            model.highest_matrix(prepared)
            prepared["value"][0] = 2
            model.highest_matrix(prepared)
            with patch.object(model, "input_fingerprints", return_value={"changed": "source"}):
                model.highest_matrix(prepared)
            self.assertEqual(build.call_count, 3)

    def test_canonical_dict_order_and_strided_arrays_share_entry(self):
        matrix = np.arange(12.).reshape(3, 4)
        a = {"x": matrix, "meta": [1, "v1"]}
        b = {"meta": [1, "v1"], "x": np.asfortranarray(matrix)}
        self.cache.get_or_compute("layout", a, lambda: {"matrix": matrix})
        with patch.object(self.cache, "_write", side_effect=AssertionError("unexpected write")):
            result = self.cache.get_or_compute("layout", b, lambda: self.fail("unexpected build"))
        np.testing.assert_array_equal(result["matrix"], matrix)

    def test_mutation_during_builder_is_not_published(self):
        inputs = {"a": np.ones(2)}
        def build():
            inputs["a"][0] = 2
            return {"matrix": np.ones(2)}
        with self.assertRaisesRegex(ValueError, "changed during"):
            self.cache.get_or_compute("mutation", inputs, build)
        self.assertFalse(list(self.cache.root.rglob("*.npz")))

    def test_numpy_scalar_and_zero_dimensional_array_are_distinct_inputs(self):
        cache = cache_module.MatrixCache(self.cache.root, fingerprint=lambda _: "b"*64)
        cache.get_or_compute("scalar-kind", np.float64(1), lambda: {"id": np.array(1)})
        result = cache.get_or_compute("scalar-kind", np.array(1.), lambda: {"id": np.array(2)})
        np.testing.assert_array_equal(result["id"], np.array(2))
        self.assertEqual(cache.stats["misses"], 2)

    def test_numeric_payload_checksum_detects_tampering(self):
        self.cache.get_or_compute("integrity", {}, lambda: {"matrix": np.eye(2)})
        path = next(self.cache.root.rglob("*.npz"))
        with np.load(path, allow_pickle=False) as archive:
            values = {key: archive[key].copy() for key in archive.files}
        values["output_0"][0, 0] = 7
        np.savez_compressed(path, **values)
        fresh = cache_module.MatrixCache(self.cache.root)
        result = fresh.get_or_compute("integrity", {}, lambda: {"matrix": 2*np.eye(2)})
        np.testing.assert_array_equal(result["matrix"], 2*np.eye(2))
        self.assertEqual(fresh.stats["corrupt"], 1)

    def test_permission_failure_does_not_prevent_computation(self):
        with patch.object(self.cache, "_write", side_effect=PermissionError("read only")):
            result = self.cache.get_or_compute("read-only", {}, lambda: {"matrix": np.eye(2)})
        np.testing.assert_array_equal(result["matrix"], np.eye(2))
        self.assertEqual(self.cache.stats["write_errors"], 1)

    def test_global_disable_skips_reuse_and_persistence(self):
        with patch.dict("os.environ", {"QSC_MATRIX_CACHE": "0"}):
            with patch.object(np.linalg, "svd", wraps=np.linalg.svd) as build:
                cache_module.svd(np.eye(2))
                cache_module.svd(np.eye(2))
                self.assertEqual(build.call_count, 2)
        self.assertFalse(self.cache.root.exists())

    def test_memory_eviction_keeps_disk_entries(self):
        cache = cache_module.MatrixCache(self.cache.root, memory_limit_bytes=1500)
        for i in range(4):
            cache.get_or_compute("bounded", i, lambda: {"matrix": np.ones(100)*i})
        self.assertLessEqual(cache.memory_bytes, 1500)
        result = cache.get_or_compute("bounded", 0, lambda: self.fail("disk entry missing"))
        np.testing.assert_array_equal(result["matrix"], np.zeros(100))
        self.assertGreater(cache.stats["disk_hits"], 0)


if __name__ == "__main__":
    unittest.main()
