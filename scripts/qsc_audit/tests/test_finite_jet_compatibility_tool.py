"""Reusable compatibility tool: full null spaces, source fits and identity sources."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
TOOL = ROOT / "skills/finite-jet-compatibility/scripts/compatibility.py"
SPEC = importlib.util.spec_from_file_location("finite_jet_tool_test", TOOL)
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


class EliminationTests(unittest.TestCase):
    def test_tall_matrix_retains_all_left_directions(self):
        matrix = np.vstack((np.eye(2), np.zeros((3, 2))))
        source = np.eye(5)[:, 2:]
        system = tool.eliminate(matrix, source)
        self.assertEqual(system["left_null"].shape, (5, 3))
        self.assertEqual(system["source_rank"], 3)
        fit = tool.fit_sources(system, np.arange(5.), require_unique=True, require_compatible=True)
        np.testing.assert_allclose(fit["residual"], 0, atol=1e-14)

    def test_wide_matrix_complete_left_space_and_injected_backend(self):
        class Services:
            def __init__(self):
                self.calls = []

            def svd(self, matrix, *, full_matrices=False):
                self.calls.append(full_matrices)
                return np.linalg.svd(matrix, full_matrices=full_matrices)

        services = Services()
        matrix = np.zeros((3, 5))
        matrix[:2, :2] = np.eye(2)
        system = tool.eliminate(matrix, services=services)
        self.assertEqual(services.calls, [False])
        self.assertEqual(system["left_null"].shape, (3, 1))
        tool.eliminate(matrix.T, services=services)
        self.assertTrue(services.calls[-1])

    def test_complex_conjugate_spaces_and_recovery(self):
        rng = np.random.default_rng(20261021)
        frame = np.linalg.qr(rng.normal(size=(6, 6))+1j*rng.normal(size=(6, 6)))[0]
        matrix, source = frame[:, :3], frame[:, 3:]
        target = matrix @ np.array([1., 2j, -1.])+source @ np.array([2j, 1., 3.])
        system = tool.eliminate(matrix, source)
        fit = tool.fit_sources(system, target, require_unique=True, require_compatible=True)
        np.testing.assert_allclose(fit["sources"], -np.array([2j, 1., 3.]), atol=1e-13)
        report = tool.attribute_left_space(system, frame[:, 3:].conj().T,
                                          frame[:, 3:].conj().T @ target, target)
        self.assertLess(report["span_error"], 1e-13)
        self.assertLess(report["reconstruction_error"], 1e-13)

    def test_zero_matrix_has_full_left_space(self):
        system = tool.eliminate(np.zeros((3, 2)), np.eye(3))
        self.assertEqual(system["rank"], 0)
        self.assertEqual(system["left_null"].shape, (3, 3))
        np.testing.assert_allclose(tool.fit_sources(system, np.ones(3))["sources"], -np.ones(3))

    def test_full_row_rank_has_no_left_constraints(self):
        system = tool.eliminate(np.eye(3), np.ones((3, 2)))
        self.assertEqual(system["left_null"].shape, (3, 0))
        self.assertEqual(system["source_rank"], 0)
        self.assertFalse(tool.fit_sources(system, np.ones(3))["unique_sources"])

    def test_injective_source_does_not_hide_remaining_compatibility(self):
        system = tool.eliminate(np.eye(4)[:, :1], np.eye(4)[:, 1:2])
        fit = tool.fit_sources(system, np.eye(4)[3])
        self.assertTrue(fit["unique_sources"])
        self.assertFalse(fit["compatible"])
        self.assertAlmostEqual(fit["residual_norm"], 1.)
        with self.assertRaisesRegex(ValueError, "compatibility residual"):
            tool.fit_sources(system, np.eye(4)[3], require_compatible=True)

    def test_nonunique_source_rejected_when_required(self):
        system = tool.eliminate(np.eye(3)[:, :1], np.ones((3, 2)))
        with self.assertRaisesRegex(ValueError, "not injective"):
            tool.fit_sources(system, np.zeros(3), require_unique=True)

    def test_bad_inputs_and_tolerances(self):
        for matrix in (np.ones(3), np.array([[np.nan]]), np.zeros((0, 3)), np.array([["x"]])):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                tool.eliminate(matrix)
        with self.assertRaises(ValueError):
            tool.eliminate(np.eye(2), np.ones((3, 1)))
        for tolerance in (-1., np.inf, np.nan, 1j):
            with self.subTest(tolerance=tolerance), self.assertRaises(ValueError):
                tool.eliminate(np.eye(2), absolute=tolerance)


class AttributionTests(unittest.TestCase):
    def test_redundant_rows_and_nonzero_identity_sources(self):
        system = tool.eliminate(np.array([[1.], [0.]]))
        rows, target, rhs = np.array([[0., 1.], [0., 2.]]), np.array([2., 3.]), np.array([3., 6.])
        report = tool.attribute_left_space(system, rows, rhs, target)
        self.assertEqual(report["known_rank"], 1)
        self.assertLess(report["span_error"], 1e-14)
        self.assertLess(report["identity_error"], 1e-14)
        self.assertLess(report["reconstruction_error"], 1e-14)
        omitted = tool.attribute_left_space(system, rows, np.zeros(2), target)
        self.assertGreater(omitted["identity_error"], 6.)
        self.assertAlmostEqual(omitted["reconstruction_error"], 3.)

    def test_equal_rank_does_not_certify_equal_spaces(self):
        system = tool.eliminate(np.array([[1.], [0.]]))
        report = tool.attribute_left_space(system, np.array([[1., 0.]]), np.ones(1), np.ones(2))
        self.assertEqual(report["known_rank"], report["left_nullity"])
        self.assertGreater(report["span_error"], 1.)
        self.assertGreater(report["annihilation_error"], .9)

    def test_attribution_shape_rejected(self):
        system = tool.eliminate(np.eye(2))
        with self.assertRaises(ValueError):
            tool.attribute_left_space(system, np.ones((1, 3)), np.ones(1), np.zeros(2))


class CommandTests(unittest.TestCase):
    def test_cli_preserves_incompatible_report_and_failure_exit(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "build") as directory:
            path, output = Path(directory)/"case.npz", Path(directory)/"report.json"
            np.savez(path, matrix=np.array([[1.], [0.]]), target=np.array([0., 2.]),
                     known_rows=np.array([[0., 1.]]), known_rhs=np.array([2.]))
            status = tool.main([str(path), "--output", str(output), "--require-compatible"])
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(status, 2)
            self.assertFalse(report["compatible"])
            self.assertAlmostEqual(report["full_residual_norm"], 2.)
            self.assertLess(report["attribution"]["identity_error"], 1e-14)

    def test_cli_rejects_overwriting_input(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "build") as directory:
            path = Path(directory)/"case.npz"
            np.savez(path, matrix=np.eye(2), target=np.zeros(2))
            content = path.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                tool.main([str(path), "--output", str(path)])
            self.assertEqual(content, path.read_bytes())

    def test_cli_outputs_complex_sources(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "build") as directory:
            path = Path(directory)/"case.npz"
            np.savez(path, matrix=np.zeros((1, 1)), source=np.array([[1j]]), target=np.ones(1))
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                status = tool.main([str(path), "--require-compatible", "--require-unique-source"])
            self.assertEqual(status, 0)
            report = json.loads(stdout.getvalue())
            self.assertAlmostEqual(report["source_values"]["imag"][0], 1.)


class ScientificIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location(
            "tool_scientific_case", ROOT / "analysis/HC_Cartan_First_Compatibility_Attribution.py")
        cls.case = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.case)
        cls.loaded = cls.case.previous.first.load_system()

    def test_existing_source_values_recovered_by_generic_tool(self):
        _, _, _, _, coordinates, fitted, q, full, response, base, _ = self.loaded
        extract = self.case.previous.first.extraction_matrix()
        blocks = self.case.source.allowed_cauchy_coordinates()
        normal = np.array(blocks["psi2"]+blocks["lambda2"]+blocks["e3"])
        prescribed = np.setdiff1d(np.arange(1200), normal)
        matrix = extract @ full
        increment = np.asarray(fitted["fitted_coordinates"])-coordinates
        target = extract @ base+matrix[:, prescribed] @ increment[prescribed]
        system = tool.eliminate(matrix[:, normal], extract @ response)
        result = tool.fit_sources(system, target, require_unique=True, require_compatible=True)
        self.assertEqual(system["left_null"].shape, (272, 112))
        np.testing.assert_allclose(result["sources"], q, atol=1e-9)
        self.assertLess(result["residual_norm"], 1e-8)

    def test_existing_identity_attribution_with_generic_tool(self):
        prepared, point, jets, _, full, _ = self.case.general.domain.load_data()
        fields = self.case.general.domain.temporal.fields(prepared, point, jets, full, np.zeros(4))
        evaluated = self.case.general.equations(prepared, fields)
        extract = self.case.previous.first.extraction_matrix()
        matrix = extract @ self.loaded[7][:, :720]
        target = extract @ self.case.source.regular.equations(prepared, point, jets)["vector"]
        result = tool.attribute_left_space(tool.eliminate(matrix), self.case.known_rows(fields),
                                          self.case.known_rhs(fields, evaluated), target)
        self.assertEqual((result["known_rank"], result["left_nullity"]), (52, 52))
        self.assertLess(result["span_error"], 1e-8)
        self.assertLess(result["identity_error"], 1e-8)


if __name__ == "__main__":
    unittest.main()
