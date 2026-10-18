"""Independent adversarial checks for the persistent numerical matrix cache."""

from concurrent.futures import ThreadPoolExecutor
import importlib.util
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "numerical_matrix_cache_under_test",
    ROOT / "analysis" / "Numerical_Matrix_Cache.py",
)
cache_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cache_module
SPEC.loader.exec_module(cache_module)
MatrixCache = cache_module.MatrixCache


def constant_digest(canonical_bytes):
    if not isinstance(canonical_bytes, bytes):
        raise AssertionError("fingerprint must receive canonical bytes")
    return "a" * 64


def unexpected_builder():
    raise AssertionError("a cached result should not invoke the builder")


class NumericalMatrixCacheTests(unittest.TestCase):
    def setUp(self):
        test_root = ROOT / "build/cache-tests"
        test_root.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=test_root)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name) / "matrix-cache"

    def cache(self, **kwargs):
        return MatrixCache(self.root, **kwargs)

    def assertPayload(self, actual, expected):
        self.assertIsInstance(actual, dict)
        self.assertEqual(set(actual), set(expected))
        for key, array in expected.items():
            self.assertIsInstance(actual[key], np.ndarray)
            self.assertEqual(actual[key].dtype, array.dtype)
            self.assertEqual(actual[key].shape, array.shape)
            np.testing.assert_array_equal(actual[key], array)
            self.assertEqual(actual[key].tobytes(), array.tobytes())

    def test_memory_hit_and_statistics(self):
        cache = self.cache()
        for key in ("hits", "disk_hits", "misses", "corrupt"):
            self.assertEqual(cache.stats[key], 0)
        expected = {"matrix": np.arange(6, dtype=np.float64).reshape(2, 3)}
        self.assertPayload(cache.get_or_compute("matrix", {"n": 3}, lambda: expected), expected)
        self.assertEqual(cache.stats["misses"], 1)
        self.assertPayload(cache.get_or_compute("matrix", {"n": 3}, unexpected_builder), expected)
        self.assertEqual(cache.stats["hits"], 1)
        self.assertEqual(cache.stats["misses"], 1)
        self.assertEqual(cache.stats["disk_hits"], 0)

    def test_copies_isolate_builder_results_and_every_return(self):
        cache = self.cache()
        source = {"matrix": np.arange(4, dtype=np.float64).reshape(2, 2)}
        expected = {key: value.copy() for key, value in source.items()}
        first = cache.get_or_compute("copy", {}, lambda: source)
        self.assertFalse(np.shares_memory(first["matrix"], source["matrix"]))
        source["matrix"][:] = -99
        first["matrix"][:] = 88
        first["extra"] = np.ones(1)
        second = cache.get_or_compute("copy", {}, unexpected_builder)
        self.assertPayload(second, expected)
        second["matrix"][:] = 77
        second.clear()
        self.assertPayload(cache.get_or_compute("copy", {}, unexpected_builder), expected)
        fresh = self.cache()
        disk = fresh.get_or_compute("copy", {}, unexpected_builder)
        self.assertPayload(disk, expected)
        disk["matrix"][:] = 66
        self.assertPayload(fresh.get_or_compute("copy", {}, unexpected_builder), expected)
        self.assertPayload(self.cache().get_or_compute("copy", {}, unexpected_builder), expected)

    def test_new_instance_reuses_disk_with_no_memory_budget(self):
        expected = {
            "complex": np.array([[1 + 2j, -3j]], dtype=np.complex128),
            "integer": np.array([2, 7], dtype=np.int16),
            "scalar": np.array(-0.0),
            "empty": np.empty((0, 3), dtype=np.float32),
        }
        self.cache(memory_limit_bytes=0).get_or_compute("persist", [1, "x"], lambda: expected)
        fresh = self.cache(memory_limit_bytes=0)
        self.assertPayload(fresh.get_or_compute("persist", [1, "x"], unexpected_builder), expected)
        self.assertEqual(fresh.stats["disk_hits"], 1)
        self.assertEqual(fresh.stats["misses"], 0)
        self.assertTrue(list(self.root.rglob("*.npz")))

    def test_forced_collisions_preserve_exact_structured_identity(self):
        values = [
            None, False, True, 0, 1, 0.0, -0.0, 1.0, 1 + 0j,
            complex(-0.0, 0.0), complex(0.0, -0.0), "1", b"1",
            [], (), [1], (1,), {"x": 1}, {"y": 1},
            np.int32(1), np.int64(1), np.float32(1), np.float64(1),
            np.array(7, dtype=np.int64), np.array([1], dtype=np.int64),
            np.array([[1]], dtype=np.int64), np.array([1], dtype=np.int32),
            np.array([1], dtype=np.float64), np.array([2], dtype=np.float64),
            np.array([0.0]), np.array([-0.0]),
            {"matrix": np.eye(2), "metadata": {"version": 1, "units": "m"}},
            {"matrix": np.eye(2), "metadata": {"version": 2, "units": "m"}},
            {"matrix": np.eye(2), "metadata": {"version": 1, "units": "s"}},
        ]
        cache = self.cache(fingerprint=constant_digest)
        for index, value in enumerate(values):
            with self.subTest(index=index, value=repr(value)):
                expected = {"id": np.array([index], dtype=np.int64)}
                self.assertPayload(cache.get_or_compute("collision", value, lambda: expected), expected)
        self.assertEqual(cache.stats["misses"], len(values))
        for index in reversed(range(len(values))):
            expected = {"id": np.array([index], dtype=np.int64)}
            with self.subTest(reload=index):
                self.assertPayload(cache.get_or_compute("collision", values[index], unexpected_builder), expected)
                fresh = self.cache(fingerprint=constant_digest, memory_limit_bytes=0)
                self.assertPayload(fresh.get_or_compute("collision", values[index], unexpected_builder), expected)

    def test_operation_and_namespace_changes_invalidate_even_on_collision(self):
        cases = [
            ("eigensystem", {"namespace": "v1", "matrix": np.eye(2)}),
            ("inverse", {"namespace": "v1", "matrix": np.eye(2)}),
            ("eigensystem", {"namespace": "v2", "matrix": np.eye(2)}),
            ("eigensystem", {"namespace": "v1", "matrix": 2 * np.eye(2)}),
        ]
        for index, (operation, inputs) in enumerate(cases):
            expected = {"id": np.array([index])}
            cache = self.cache(fingerprint=constant_digest)
            self.assertPayload(cache.get_or_compute(operation, inputs, lambda: expected), expected)
            self.assertEqual(cache.stats["misses"], 1)
        for index, (operation, inputs) in enumerate(cases):
            self.assertPayload(
                self.cache(fingerprint=constant_digest).get_or_compute(operation, inputs, unexpected_builder),
                {"id": np.array([index])},
            )

    def test_mutated_inputs_are_reidentified(self):
        inputs = {"matrix": np.eye(2), "metadata": ["v1"]}
        cache = self.cache(fingerprint=constant_digest)
        cache.get_or_compute("mutable", inputs, lambda: {"id": np.array([1])})
        inputs["matrix"][0, 0] = 3
        inputs["metadata"][0] = "v2"
        self.assertPayload(cache.get_or_compute("mutable", inputs, lambda: {"id": np.array([2])}),
                           {"id": np.array([2])})
        original = {"matrix": np.eye(2), "metadata": ["v1"]}
        self.assertPayload(cache.get_or_compute("mutable", original, unexpected_builder), {"id": np.array([1])})

    def test_corrupt_entry_is_skipped_without_losing_colliding_sibling(self):
        cache = self.cache(fingerprint=constant_digest)
        cache.get_or_compute("corrupt", {"id": 1}, lambda: {"id": np.array([1])})
        first_files = set(self.root.rglob("*.npz"))
        self.assertTrue(first_files)
        cache.get_or_compute("corrupt", {"id": 2}, lambda: {"id": np.array([2])})
        self.assertTrue(set(self.root.rglob("*.npz")) - first_files)
        for path in first_files:
            path.write_bytes(b"PK\x03\x04truncated archive")
        fresh = self.cache(fingerprint=constant_digest)
        self.assertPayload(fresh.get_or_compute("corrupt", {"id": 2}, unexpected_builder), {"id": np.array([2])})
        self.assertPayload(fresh.get_or_compute("corrupt", {"id": 1}, lambda: {"id": np.array([1])}),
                           {"id": np.array([1])})
        self.assertGreaterEqual(fresh.stats["corrupt"], 1)
        self.assertPayload(self.cache(fingerprint=constant_digest).get_or_compute(
            "corrupt", {"id": 1}, unexpected_builder), {"id": np.array([1])})

    def test_numpy_disk_load_explicitly_disables_pickle(self):
        expected = {"matrix": np.eye(2)}
        self.cache().get_or_compute("pickle", {}, lambda: expected)
        real_load = np.load

        def guarded_load(*args, **kwargs):
            self.assertIs(kwargs.get("allow_pickle"), False)
            return real_load(*args, **kwargs)

        with patch.object(np, "load", side_effect=guarded_load) as spy:
            self.assertPayload(self.cache().get_or_compute("pickle", {}, unexpected_builder), expected)
            self.assertGreater(spy.call_count, 0)

    def test_object_archive_is_rejected_and_rebuilt(self):
        expected = {"matrix": np.eye(2)}
        self.cache().get_or_compute("hostile", {}, lambda: expected)
        entries = list(self.root.rglob("*.npz"))
        self.assertTrue(entries)
        for path in entries:
            np.savez(path, matrix=np.array([{"not": "numeric"}], dtype=object))
        fresh = self.cache()
        self.assertPayload(fresh.get_or_compute("hostile", {}, lambda: expected), expected)
        self.assertGreaterEqual(fresh.stats["corrupt"], 1)

    def test_disabled_cache_never_persists_or_reads_existing_entries(self):
        enabled = self.cache()
        enabled.get_or_compute("disabled", {}, lambda: {"id": np.array([1])})
        snapshot = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        disabled = self.cache(enabled=False)
        for index in (2, 3):
            self.assertPayload(disabled.get_or_compute("disabled", {}, lambda: {"id": np.array([index])}),
                               {"id": np.array([index])})
        self.assertEqual(snapshot, {p.relative_to(self.root): p.read_bytes()
                                    for p in self.root.rglob("*") if p.is_file()})
        absent = self.root.parent / "disabled-only"
        MatrixCache(absent, enabled=False).get_or_compute("unused", {}, lambda: {"a": np.ones(2)})
        self.assertFalse(any(p.is_file() for p in absent.rglob("*")))

    def test_unsupported_and_nonfinite_inputs_never_invoke_builder(self):
        bad_values = [
            object(), {1, 2}, np.array([object()], dtype=object), np.array(["text"]),
            float("nan"), float("inf"), float("-inf"), complex(1, float("nan")),
            np.float32("inf"), np.array([1, np.nan]), np.array([complex(1, float("inf"))]),
            {"nested": [np.array([np.inf])]},
        ]
        for index, inputs in enumerate(bad_values):
            with self.subTest(index=index):
                with self.assertRaises((TypeError, ValueError)):
                    self.cache().get_or_compute("invalid", inputs, unexpected_builder)

    def test_invalid_builder_results_are_not_cached(self):
        bad_results = [
            None, np.ones(2), {"a": np.array([object()], dtype=object)},
            {"a": np.array(["text"])}, {"a": np.array([np.nan])},
            {"a": np.array([np.inf])}, {"a": np.array([complex(1, float("nan"))])},
            {1: np.ones(2)},
        ]
        for index, result in enumerate(bad_results):
            with self.subTest(index=index):
                cache = self.cache()
                with self.assertRaises((TypeError, ValueError)):
                    cache.get_or_compute("invalid-result", index, lambda: result)
                expected = {"ok": np.array([index])}
                self.assertPayload(cache.get_or_compute("invalid-result", index, lambda: expected), expected)
                self.assertPayload(self.cache().get_or_compute("invalid-result", index, unexpected_builder), expected)

    def test_builder_exception_does_not_publish_an_entry(self):
        def broken():
            raise RuntimeError("builder failed deliberately")

        with self.assertRaisesRegex(RuntimeError, "deliberately"):
            self.cache().get_or_compute("exception", {}, broken)
        self.assertFalse(list(self.root.rglob("*.npz")))
        expected = {"ok": np.ones(2)}
        self.assertPayload(self.cache().get_or_compute("exception", {}, lambda: expected), expected)

    def test_threads_publish_complete_entries_under_forced_collisions(self):
        workers = 8
        start = threading.Barrier(workers)
        shared = self.cache(fingerprint=constant_digest, memory_limit_bytes=0)

        def task(index):
            # Repeated identities exercise racing writers; distinct ones share a bucket.
            identity = index % 3
            expected = {"matrix": np.full((48, 32), identity, dtype=np.float64),
                        "check": np.arange(17, dtype=np.int32)}
            cache = shared if index % 2 else self.cache(fingerprint=constant_digest, memory_limit_bytes=0)
            start.wait(timeout=10)
            for _ in range(4):
                actual = cache.get_or_compute("threaded", {"id": identity}, lambda: expected)
                self.assertPayload(actual, expected)
                actual["matrix"][:] = -99

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(task, index) for index in range(workers)]
            for future in futures:
                future.result(timeout=30)
        for identity in range(3):
            expected = {"matrix": np.full((48, 32), identity, dtype=np.float64),
                        "check": np.arange(17, dtype=np.int32)}
            fresh = self.cache(fingerprint=constant_digest, memory_limit_bytes=0)
            self.assertPayload(fresh.get_or_compute("threaded", {"id": identity}, unexpected_builder), expected)
            self.assertEqual(fresh.stats["corrupt"], 0)


if __name__ == "__main__":
    unittest.main()
