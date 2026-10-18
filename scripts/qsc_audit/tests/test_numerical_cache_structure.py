"""Focused regression checks for cache refactoring boundaries."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]


def load_cache():
    spec = importlib.util.spec_from_file_location(
        "unregistered_numerical_cache", ROOT / "analysis/Numerical_Matrix_Cache.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NumericalCacheStructureTests(unittest.TestCase):
    def setUp(self):
        test_root = ROOT / "build/cache-tests"
        test_root.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=test_root)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.module = load_cache()

    def test_dynamic_import_without_sys_modules_registration(self):
        self.assertNotIn(self.module.__name__, sys.modules)
        cache = self.module.MatrixCache(self.root)
        cache.get_or_compute("import", {}, lambda: {"value": np.array([3])})
        result = cache.get_or_compute("import", {}, lambda: self.fail("cache miss"))
        np.testing.assert_array_equal(result["value"], [3])
        self.assertGreater(cache.memory_bytes, 0)

    def test_concurrent_misses_counted_and_builders_run_outside_lock(self):
        workers = 8
        for enabled in (True, False):
            with self.subTest(enabled=enabled):
                cache = self.module.MatrixCache(self.root / str(enabled), enabled=enabled)
                barrier = threading.Barrier(workers)

                def task(index):
                    def build():
                        barrier.wait(timeout=10)
                        return {"value": np.array([index])}
                    return cache.get_or_compute("parallel", index, build)

                with ThreadPoolExecutor(max_workers=workers) as executor:
                    results = list(executor.map(task, range(workers)))
                for index, result in enumerate(results):
                    np.testing.assert_array_equal(result["value"], [index])
                self.assertEqual(cache.stats, {
                    "hits": 0, "disk_hits": 0, "misses": workers,
                    "corrupt": 0, "write_errors": 0,
                })

    def test_typed_canonical_packet_matches_schema_one_bytes(self):
        descriptor, arrays = self.module._encode("typed/v1", {
            "z": np.array([1, -2], dtype="<i2"),
            "a": (None, True, 7, -0.0, b"x"),
        })
        expected = ('[1,"typed/v1",["dict",[["a",["tuple",[["none"],'
                    '["bool",true],["int","7"],["float","-0x0.0p+0"],'
                    '["bytes","78"]]]],["z",["array","input_0","<i2",[2]]]]]]')
        self.assertEqual(descriptor, expected)
        pieces = (expected.encode("ascii"), b"\x01\x00\xfe\xff")
        packet = b"".join(len(piece).to_bytes(8, "big") + piece for piece in pieces)
        self.assertEqual(self.module._packet(descriptor, arrays), packet)

    def test_schema_one_archive_compatibility(self):
        descriptor = '[1,"legacy",["none"]]'
        output = np.array([2., 3.], dtype="<f8")
        metadata = {
            "schema": 1, "descriptor": descriptor, "inputs": {},
            "outputs": {"value": {
                "dtype": "<f8", "shape": [2],
                "sha256": hashlib.sha256(output.tobytes()).hexdigest(),
            }},
        }
        packet = len(descriptor).to_bytes(8, "big") + descriptor.encode("ascii")
        bucket = self.root / hashlib.sha256(packet).hexdigest()
        bucket.mkdir()
        np.savez_compressed(bucket / "legacy.npz", output_0=output,
                            metadata=np.frombuffer(json.dumps(metadata).encode("ascii"),
                                                   dtype=np.uint8))
        cache = self.module.MatrixCache(self.root)
        result = cache.get_or_compute("legacy", None, lambda: self.fail("legacy miss"))
        np.testing.assert_array_equal(result["value"], output)
        self.assertEqual(cache.stats["disk_hits"], 1)

        cache.get_or_compute("new", None, lambda: {"value": output})
        new_path = next(path for path in self.root.rglob("*.npz") if path.parent != bucket)
        with np.load(new_path, allow_pickle=False) as archive:
            self.assertEqual(set(archive.files), {"metadata", "output_0"})
            self.assertEqual(archive["metadata"].dtype, np.dtype("uint8"))
            written = json.loads(archive["metadata"].tobytes().decode("ascii"))
            self.assertEqual(written, dict(metadata, descriptor='[1,"new",["none"]]'))


if __name__ == "__main__":
    unittest.main()
