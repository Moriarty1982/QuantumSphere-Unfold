"""Small, explicit numerical scopes without global cache or solver patching."""
import ast
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import inspect
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "analysis" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dependencies = load_module("di_test_dependencies", "Numerical_Dependencies.py")
model = load_module("di_test_cauchy", "HC_Cartan_Cauchy_Next_Completion.py")


class RecordingBackend:
    def __init__(self, version="1", name="test-svd"):
        self.metadata = {"backend": name, "version": version}
        self.calls = []

    @property
    def identity(self):
        return dict(self.metadata)

    def svd(self, matrix, *, full_matrices=False):
        self.calls.append((np.array(matrix, copy=True), full_matrices))
        return np.linalg.svd(matrix, full_matrices=full_matrices)


class FixedDiagonalBackend(RecordingBackend):
    """An analytic fake: the affine test never invokes NumPy's SVD."""

    def svd(self, matrix, *, full_matrices=False):
        np.testing.assert_array_equal(matrix, np.diag([4., 2.]))
        self.calls.append((np.array(matrix, copy=True), full_matrices))
        return np.eye(2), np.array([4., 2.]), np.eye(2)


class NumericalDependencyInjectionTests(unittest.TestCase):
    def setUp(self):
        self.environment = dict(os.environ)
        self.global_cache = model.cache.CACHE
        self.addCleanup(self.assert_ambient_state_unchanged)
        test_root = ROOT / "build/cache-tests"
        test_root.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix="dependency-injection-", dir=test_root)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def assert_ambient_state_unchanged(self):
        self.assertEqual(dict(os.environ), self.environment)
        self.assertIs(model.cache.CACHE, self.global_cache)

    def services(self, name="cache", *, enabled=True, backend=None):
        cache = model.cache.MatrixCache(self.root / name, enabled=enabled)
        return model.create_container(matrix_cache=cache, svd_backend=backend).services()

    def test_dynamic_imports_do_not_require_sys_modules_registration(self):
        self.assertNotIn(dependencies.__name__, sys.modules)
        self.assertNotIn(model.__name__, sys.modules)
        self.assertNotIn(model.dependencies.__name__, sys.modules)
        services = dependencies.NumericalContainer(
            lambda: model.cache.MatrixCache(self.root / "unregistered")
        ).services()
        self.assertIsInstance(services, dependencies.NumericalServices)
        np.testing.assert_allclose(services.svd(np.eye(2))[1], [1., 1.])

    def test_factories_are_lazy_and_singletons_within_one_container(self):
        cache = model.cache.MatrixCache(self.root / "lazy")
        backend = RecordingBackend()
        cache_factory = Mock(return_value=cache)
        backend_factory = Mock(return_value=backend)
        container = dependencies.NumericalContainer(cache_factory, backend_factory)
        cache_factory.assert_not_called()
        backend_factory.assert_not_called()
        services = container.services()
        for _ in range(5):
            self.assertIs(container.services(), services)
        self.assertIs(services.matrix_cache, cache)
        self.assertIs(services.backend, backend)
        cache_factory.assert_called_once_with()
        backend_factory.assert_called_once_with()

    def test_concurrent_resolution_constructs_each_dependency_once(self):
        workers = 8
        start = threading.Barrier(workers)
        entered = threading.Event()
        release = threading.Event()
        counts = {"cache": 0, "backend": 0}
        lock = threading.Lock()

        def cache_factory():
            with lock:
                counts["cache"] += 1
            entered.set()
            if not release.wait(timeout=10):
                raise AssertionError("cache factory was not released")
            return model.cache.MatrixCache(self.root / "concurrent")

        def backend_factory():
            with lock:
                counts["backend"] += 1
            return RecordingBackend()

        container = dependencies.NumericalContainer(cache_factory, backend_factory)

        def resolve():
            start.wait(timeout=10)
            return container.services()

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(resolve) for _ in range(workers)]
            try:
                self.assertTrue(entered.wait(timeout=10))
            finally:
                release.set()
            resolved = [future.result(timeout=10) for future in futures]
        self.assertEqual(counts, {"cache": 1, "backend": 1})
        self.assertTrue(all(item is resolved[0] for item in resolved))
        self.assertIs(container.services(), resolved[0])

    def test_separate_containers_own_independent_dependencies_and_entries(self):
        def make_container(name):
            return dependencies.NumericalContainer(
                lambda: model.cache.MatrixCache(self.root / name), RecordingBackend)

        first = make_container("first").services()
        second = make_container("second").services()
        self.assertIsNot(first, second)
        self.assertIsNot(first.matrix_cache, second.matrix_cache)
        self.assertIsNot(first.backend, second.backend)
        first.svd(np.eye(2))
        first.svd(np.eye(2))
        second.svd(np.eye(2))
        self.assertEqual(len(first.backend.calls), 1)
        self.assertEqual(len(second.backend.calls), 1)
        self.assertTrue(list((self.root / "first").rglob("*.npz")))
        self.assertTrue(list((self.root / "second").rglob("*.npz")))

    def test_cached_forwards_operation_inputs_and_builder_to_injected_cache(self):
        expected = {"matrix": np.eye(2)}
        cache = Mock()
        cache.get_or_compute.return_value = expected
        services = model.create_container(matrix_cache=cache).services()
        inputs = {"x": np.array([1., 2.])}
        builder = Mock(return_value=expected)
        self.assertIs(services.cached("di.forward/v1", inputs, builder), expected)
        cache.get_or_compute.assert_called_once_with("di.forward/v1", inputs, builder)
        builder.assert_not_called()

    def test_default_backend_has_versioned_canonical_identity_and_valid_svd(self):
        backend = dependencies.NumPySVDBackend()
        identity = backend.identity
        self.assertIsInstance(identity, dict)
        self.assertTrue(identity["backend"])
        self.assertEqual(identity["version"], np.__version__)
        self.assertEqual(identity, dependencies.NumPySVDBackend().identity)
        services = dependencies.NumericalContainer(
            lambda: model.cache.MatrixCache(self.root / "default")
        ).services()
        self.assertIsInstance(services.backend, dependencies.NumPySVDBackend)
        matrix = np.array([[3., 0., 0.], [0., 2., 0.]])
        u, singular, vh = services.svd(matrix)
        np.testing.assert_allclose((u * singular) @ vh, matrix)
        self.assertEqual(vh.shape, (2, 3))
        self.assertTrue(list(services.matrix_cache.root.rglob("*.npz")))

    def test_fake_backend_receives_matrix_and_full_matrices_and_reuses_results(self):
        backend = RecordingBackend()
        services = self.services(backend=backend)
        matrix = np.array([[3., 0., 0.], [0., 2., 0.]])
        for full in (False, True):
            for _ in range(2):
                u, singular, vh = services.svd(matrix.copy(), full_matrices=full)
                np.testing.assert_allclose((u[:, :2] * singular) @ vh[:2], matrix)
                self.assertEqual(vh.shape, (3 if full else 2, 3))
        self.assertEqual(len(backend.calls), 2)
        self.assertEqual([full for _, full in backend.calls], [False, True])
        for received, _ in backend.calls:
            np.testing.assert_array_equal(received, matrix)

    def test_backend_identity_isolates_entries_and_equal_identity_reuses_disk(self):
        root = self.root / "shared"
        matrix = np.diag([4., 2.])
        for name, version, expected_calls in (
            ("fake-a", "1", 1), ("fake-a", "2", 1),
            ("fake-b", "1", 1), ("fake-a", "1", 0),
        ):
            with self.subTest(name=name, version=version, expected_calls=expected_calls):
                backend = RecordingBackend(version=version, name=name)
                services = model.create_container(
                    cache_root=root, cache_enabled=True, svd_backend=backend).services()
                np.testing.assert_allclose(services.svd(matrix)[1], [4., 2.])
                self.assertEqual(len(backend.calls), expected_calls)
                if not expected_calls:
                    self.assertGreater(services.matrix_cache.stats["disk_hits"], 0)

    def test_invalid_backend_identity_is_rejected_before_backend_call(self):
        for index, identity in enumerate((
            None, "unversioned", {}, {"backend": "fake"}, {"version": "1"},
            {"backend": "", "version": "1"}, {"backend": None, "version": "1"},
            {"backend": "fake", "version": ""},
            {"backend": "fake", "version": None},
            {"backend": "fake", "version": "1", "setting": float("nan")},
            {"backend": "fake", "version": "1", "setting": float("inf")},
            {"backend": "fake", "version": "1", "setting": object()},
        )):
            with self.subTest(identity=identity):
                backend = Mock()
                backend.identity = identity
                services = self.services(str(index), enabled=False, backend=backend)
                with self.assertRaises((ValueError, TypeError)):
                    services.svd(np.eye(2))
                backend.svd.assert_not_called()
                self.assertFalse(services.matrix_cache.root.exists())

    def test_create_container_rejects_injected_cache_with_construction_options(self):
        cache = model.cache.MatrixCache(self.root / "injected")
        for options in (
            {"cache_root": self.root / "conflicting"},
            {"cache_enabled": True}, {"cache_enabled": False},
            {"cache_root": self.root / "conflicting", "cache_enabled": False},
        ):
            with self.subTest(options=options):
                with self.assertRaises(ValueError):
                    model.create_container(matrix_cache=cache, **options)
        self.assertFalse(cache.root.exists())
        self.assertFalse((self.root / "conflicting").exists())

    def test_explicit_services_ignore_environment_cache_flag(self):
        for enabled, flag in ((True, "0"), (False, "1")):
            with self.subTest(enabled=enabled, flag=flag):
                backend = FixedDiagonalBackend()
                services = self.services(str(enabled), enabled=enabled, backend=backend)
                with patch.dict(os.environ, {"QSC_MATRIX_CACHE": flag}):
                    environment = dict(os.environ)
                    poison = Mock()
                    poison.get_or_compute.side_effect = AssertionError("global cache used")
                    with patch.object(model.cache, "CACHE", poison):
                        for _ in range(2):
                            solved = model.solve_affine(
                                np.diag([4., 2.]), np.array([8., -6.]), services=services)
                            np.testing.assert_allclose(solved["solution"], [-2., 3.])
                        self.assertIs(model.cache.CACHE, poison)
                        poison.get_or_compute.assert_not_called()
                    self.assertEqual(dict(os.environ), environment)
                self.assertEqual(len(backend.calls), 1 if enabled else 2)
                self.assertEqual(services.matrix_cache.root.exists(), enabled)

    def test_explicitly_disabled_cache_recomputes_without_creating_disk_root(self):
        backend = FixedDiagonalBackend()
        root = self.root / "disabled" / "never-created"
        container = model.create_container(
            cache_root=root, cache_enabled=False, svd_backend=backend)
        services = container.services()
        self.assertFalse(services.matrix_cache.enabled)
        self.assertFalse(root.exists())
        for _ in range(2):
            result = model.solve_affine(np.diag([4., 2.]), np.array([8., -6.]),
                                        services=services)
            np.testing.assert_allclose(result["solution"], [-2., 3.])
        self.assertEqual(len(backend.calls), 2)
        self.assertFalse(root.parent.exists())

    def test_solve_affine_uses_injected_analytic_fake_without_patching(self):
        backend = FixedDiagonalBackend()
        services = self.services(backend=backend)
        matrix = np.diag([4., 2.])
        base = np.array([8., -6.])
        result = model.solve_affine(matrix, base, services=services)
        self.assertEqual(result["rank"], 2)
        np.testing.assert_allclose(result["solution"], [-2., 3.])
        np.testing.assert_allclose(result["inverse"], np.diag([.25, .5]))
        np.testing.assert_allclose(result["remainder"], [0., 0.], atol=1e-12)
        np.testing.assert_array_equal(result["singular"], [4., 2.])
        second = model.solve_affine(matrix, np.array([4., 4.]), services=services)
        np.testing.assert_allclose(second["solution"], [-1., -2.])
        self.assertEqual(len(backend.calls), 1)
        np.testing.assert_array_equal(matrix, np.diag([4., 2.]))
        np.testing.assert_array_equal(base, [8., -6.])

    def test_poisoned_global_cache_does_not_affect_injected_solvers(self):
        backend = RecordingBackend()
        services = self.services(backend=backend)
        poison = Mock()
        poison.get_or_compute.side_effect = AssertionError("global cache used")
        poison.root = self.root / "poison"
        matrix = np.zeros((model.OLD_EQUATION_COUNT + 1, 2))
        matrix[0, 0] = 2.
        matrix[-1] = [1., 4.]
        base = np.zeros(matrix.shape[0])
        base[0], base[-1] = 6., 11.
        assembled = model.AffineSystem(matrix, base, (240,), (880,))
        with patch.object(model.cache, "CACHE", poison):
            direct = model.solve_affine(np.diag([4., 2.]), np.array([8., -6.]),
                                        services=services)
            ordered = model.preserve_old_first(assembled, services=services)
            self.assertIs(model.cache.CACHE, poison)
        np.testing.assert_allclose(direct["solution"], [-2., 3.])
        np.testing.assert_allclose(ordered["solution"], [-3., -2.])
        np.testing.assert_allclose(base + matrix @ ordered["solution"], 0., atol=1e-12)
        self.assertEqual(ordered["old_rank"], 1)
        self.assertEqual(len(backend.calls), 3)
        poison.get_or_compute.assert_not_called()
        self.assertFalse(poison.root.exists())

    def test_poisoned_global_cache_does_not_affect_injected_matrix_paths(self):
        highest_matrix = np.array([[2., 0.], [0., 3.]])
        assembled = model.AffineSystem(np.eye(2), np.array([1., 2.]), (240,), (880,))
        payloads = {"Cartan.highest-matrix/v1": {"matrix": highest_matrix},
                    "Cartan.reprepare-matrix/v1": assembled.to_arrays()}
        injected_cache = Mock()
        injected_cache.get_or_compute.side_effect = lambda operation, inputs, builder: payloads[operation]
        services = model.create_container(matrix_cache=injected_cache).services()
        poison = Mock()
        poison.get_or_compute.side_effect = AssertionError("global cache used")
        prepared = {"di_fixture": np.array([1.])}
        with patch.object(model.cache, "CACHE", poison):
            actual_highest = model.highest_matrix(prepared, services=services)
            actual_system = model.reprepare_matrix(
                prepared, {}, np.zeros(1200), np.zeros(1720), {}, highest_matrix,
                services=services)
            self.assertIs(model.cache.CACHE, poison)
        np.testing.assert_array_equal(actual_highest, highest_matrix)
        np.testing.assert_array_equal(actual_system.matrix, assembled.matrix)
        np.testing.assert_array_equal(actual_system.base, assembled.base)
        self.assertEqual(actual_system.older, (240,))
        self.assertEqual(actual_system.highest, (880,))
        self.assertEqual(injected_cache.get_or_compute.call_count, 2)
        for call in injected_cache.get_or_compute.call_args_list:
            self.assertIs(call.args[1]["prepared"], prepared)
            self.assertTrue(callable(call.args[2]))
        poison.get_or_compute.assert_not_called()

    def test_explicit_composition_and_execution_leave_environment_unchanged(self):
        for enabled in (True, False):
            with self.subTest(enabled=enabled):
                backend = FixedDiagonalBackend()
                services = model.create_container(
                    cache_root=self.root / str(enabled), cache_enabled=enabled,
                    svd_backend=backend).services()
                self.assertEqual(services.matrix_cache.enabled, enabled)
                model.solve_affine(np.diag([4., 2.]), np.ones(2), services=services)
                self.assertEqual(dict(os.environ), self.environment)
                self.assertIs(model.cache.CACHE, self.global_cache)

    def test_evaluate_forwards_services_to_every_numerical_entry_point(self):
        # Inspect orchestration because executing evaluate builds the full witness.
        tree = ast.parse(inspect.getsource(model.evaluate))
        expected = {"highest_matrix", "solve_affine", "reprepare_matrix", "preserve_old_first"}
        seen = set()
        for call in ast.walk(tree):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id in expected:
                    seen.add(call.func.id)
                    keywords = {item.arg: item.value for item in call.keywords}
                    self.assertIn("services", keywords, call.func.id)
                    self.assertIsInstance(keywords["services"], ast.Name)
                    self.assertEqual(keywords["services"].id, "services")
        self.assertEqual(seen, expected)

    def test_main_constructs_one_container_and_passes_its_resolved_services(self):
        tree = ast.parse(inspect.getsource(model.main))
        calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
        factories = [call for call in calls if isinstance(call.func, ast.Name)
                     and call.func.id == "create_container"]
        resolutions = [call for call in calls if isinstance(call.func, ast.Attribute)
                       and call.func.attr == "services"]
        evaluations = [call for call in calls if isinstance(call.func, ast.Name)
                       and call.func.id == "evaluate"]
        self.assertEqual(len(factories), 1)
        self.assertEqual(len(resolutions), 1)
        self.assertEqual(len(evaluations), 1)
        assignments = {node.targets[0].id: node.value for node in ast.walk(tree)
                       if isinstance(node, ast.Assign) and len(node.targets) == 1
                       and isinstance(node.targets[0], ast.Name)}
        container_name = next(name for name, value in assignments.items() if value is factories[0])
        services_name = next(name for name, value in assignments.items() if value is resolutions[0])
        self.assertIsInstance(resolutions[0].func.value, ast.Name)
        self.assertEqual(resolutions[0].func.value.id, container_name)
        forwarded = {item.arg: item.value for item in evaluations[0].keywords}
        self.assertIn("services", forwarded)
        self.assertIsInstance(forwarded["services"], ast.Name)
        self.assertEqual(forwarded["services"].id, services_name)


if __name__ == "__main__":
    unittest.main()
