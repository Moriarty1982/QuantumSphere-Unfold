"""Full metric versus cross-readout covariance, nonlinear invariants and rank gates."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "gauge_invariant_geometry_readouts", ROOT / "analysis/HC_Gauge_Invariant_Geometry_Readouts.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCGaugeInvariantGeometryReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.spectral.field_data()
        cls.jet = model.covariant_jet(cls.data)
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=1e-9):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=4e-8)

    def maximal_unitary(self):
        result = np.zeros((6, 6), complex)
        for p, sigma, angle in zip(model.spectral.modal_projectors(), model.spectral.intertwiners.PAULI, (0.2, -0.4, 0.3)):
            block = np.cos(angle)*np.eye(2)+1j*np.sin(angle)*sigma
            result += p @ np.kron(block, np.eye(3))
        self.assertClose(result.conj().T @ result, np.eye(6))
        return result

    def test_native_metric_uses_whole_triad_while_cross_readout_is_separate(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        self.assertIn("closed triadic probe field", text)
        self.assertIn("maximal rank", text)
        self.assertIn(r"\bar\Psi_\triangle \,\Gamma^a", text)
        self.assertTrue(self.report["native_source_distinction"]["full_metric_alone_does_not_force_common_internal_gauge_factor"])

    def test_covariant_jet_includes_same_levi_civita_spin_transport_as_dirac_check(self):
        d = self.data
        reference = model.dirac.dirac_data(d["psi"], d["psi_first"]+d["connection"] @ d["psi"], d["mass_operator"],
            gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])
        self.assertClose(self.jet, reference["covariant"])
        self.assertLess(np.linalg.norm(reference["residual"]), 1e-12)

    def test_full_complex_pairing_is_invariant_under_maximal_internal_gauge(self):
        g = self.maximal_unitary()
        before = model.pairing(self.data["psi"], self.jet)
        after = model.pairing(g @ self.data["psi"], g @ self.jet)
        self.assertClose(before, after)

    def test_full_metric_is_invariant_without_requiring_fixed_channel_projectors(self):
        g = self.maximal_unitary()
        before = model.geometry(self.data["psi"], self.jet)
        after = model.geometry(g @ self.data["psi"], g @ self.jet)
        self.assertClose(before["metric"], after["metric"])
        cross = model.spectral.cross_readout_operator()
        self.assertGreater(np.linalg.norm(g.conj().T @ cross @ g-cross), 0.4)

    def test_on_shell_full_real_coframe_has_analytic_rank_one_form(self):
        y = self.data["state"]
        mass, _ = model.spectral.modal_basis()
        target = np.zeros((4, 4))
        target[0, 3] = 2*np.sum(mass*y[:, 0]*y[:, 1])
        actual = model.geometry(self.data["psi"], self.jet)
        self.assertClose(actual["coframe"], target)
        self.assertEqual(actual["coframe_rank_at_1e_minus_10"], 1)

    def test_current_gradient_identity_is_independently_checked(self):
        step = 1e-5
        point = self.data["point"]
        densities = []
        for sign in (1, -1):
            d = model.spectral.field_data(point+sign*step*np.array([0, 0, 0, 1]))
            densities.append(np.trace(d["current"][0]).real)
        derivative = (densities[0]-densities[1])/(2*step)
        self.assertClose(model.geometry(self.data["psi"], self.jet)["coframe"][0, 3], derivative/2)

    def test_rank_one_persists_at_other_radii_and_angular_points(self):
        for point, radius in (([-0.3, 2.4, 1.2, -0.01], 1.6), ([0.2, 0.5, -0.4, 0.01], 0.8)):
            d = model.spectral.field_data(point, radius=radius)
            result = model.geometry(d["psi"], model.covariant_jet(d))
            self.assertEqual(result["coframe_rank_at_1e_minus_10"], 1)

    def test_prescribed_product_metric_is_not_induced_by_this_same_probe(self):
        result = model.geometry(self.data["psi"], self.jet)
        self.assertEqual(np.sum(abs(result["metric_eigenvalues"]) > 1e-10), 1)
        self.assertEqual(np.linalg.matrix_rank(self.data["bundle"]["metric"]), 4)
        self.assertGreater(np.linalg.norm(result["metric"]-self.data["bundle"]["metric"]), 1)

    def test_imaginary_pairing_is_not_silently_adopted_as_native_coframe(self):
        imaginary = model.pairing(self.data["psi"], self.jet).imag
        self.assertEqual(np.sum(np.linalg.svd(imaginary, compute_uv=False) > 1e-10), 2)
        self.assertClose(model.geometry(self.data["psi"], self.jet)["coframe"], model.pairing(self.data["psi"], self.jet).real)

    def test_full_rank_cross_metric_control_is_genuinely_nondegenerate(self):
        psi, derivative = model.full_rank_cross_control()
        result = model.geometry(psi, derivative, model.spectral.cross_readout_operator())
        self.assertClose(result["coframe"], np.eye(4))
        self.assertClose(result["metric"], model.ETA)
        self.assertEqual(result["coframe_rank_at_1e_minus_10"], 4)

    def test_squaring_bare_cross_coframe_does_not_automatically_make_metric_invariant(self):
        psi, derivative = model.full_rank_cross_control()
        cross, g = model.spectral.cross_readout_operator(), model.gauge_unitary()
        before = model.geometry(psi, derivative, cross)
        after = model.geometry(g @ psi, g @ derivative, cross)
        self.assertEqual(after["coframe_rank_at_1e_minus_10"], 4)
        self.assertGreater(np.linalg.norm(after["metric"]-before["metric"]), 0.12)
        self.assertClose(g @ self.data["mass_operator"], self.data["mass_operator"] @ g)

    def test_transporting_cross_selector_restores_cross_metric(self):
        psi, derivative = model.full_rank_cross_control()
        cross, g = model.spectral.cross_readout_operator(), model.gauge_unitary()
        before = model.geometry(psi, derivative, cross)
        after = model.geometry(g @ psi, g @ derivative, g @ cross @ g.conj().T)
        self.assertClose(after["coframe"], before["coframe"])
        self.assertClose(after["metric"], before["metric"])

    def test_invariant_fixed_selector_dimensions_are_nine_vs_three(self):
        algebras = model.fixed_selector_algebras()
        self.assertEqual(algebras["common"]["dimension"], 9)
        self.assertEqual(algebras["spectral"]["dimension"], 3)

    def test_every_maximal_invariant_fixed_bilinear_selector_is_spectral_diagonal(self):
        projectors = model.spectral.modal_projectors()
        for selector in model.fixed_selector_algebras()["spectral"]["basis"]:
            reconstructed = sum(np.trace(p @ selector).real*p/2 for p in projectors)
            self.assertClose(selector, reconstructed)

    def test_pair_tensors_are_invariant_under_nonabelian_spectral_rotations(self):
        g = self.maximal_unitary()
        current = self.data["current"]
        self.assertClose(model.pair_tensors(g @ current @ g.conj().T), model.pair_tensors(current))

    def test_loop_tensor_is_invariant_under_nonabelian_spectral_rotations(self):
        g = self.maximal_unitary()
        current = self.data["current"]
        self.assertClose(model.loop_tensor(g @ current @ g.conj().T), model.loop_tensor(current))

    def test_time_pair_components_are_hilbert_schmidt_norm_squares(self):
        current = self.data["current"]
        tensors = model.pair_tensors(current)
        for a, p in enumerate(model.spectral.modal_projectors()):
            for b, q in enumerate(model.spectral.modal_projectors()):
                self.assertClose(tensors[a, b, 0, 0], np.vdot(p @ current[0] @ q, p @ current[0] @ q).real)
                self.assertGreaterEqual(tensors[a, b, 0, 0].real, -1e-14)

    def test_pair_conjugation_and_index_exchange_identities(self):
        pair = model.pair_tensors(model.complex_loop_control())
        self.assertClose(pair.conj(), pair.swapaxes(2, 3))
        self.assertClose(pair, pair.swapaxes(0, 1).swapaxes(2, 3))
        self.assertClose(pair.real, pair.real.swapaxes(2, 3))

    def test_current_tensor_time_components_are_not_lorentz_scalars(self):
        boost = np.eye(4)
        boost[0, 0] = boost[3, 3] = np.cosh(0.3)
        boost[0, 3] = boost[3, 0] = np.sinh(0.3)
        current = self.data["current"]
        transformed = np.einsum("mn,nij->mij", boost, current)
        pair = model.pair_tensors(current)
        target = np.einsum("ma,nb,rsab->rsmn", boost, boost, pair)
        self.assertClose(model.pair_tensors(transformed), target)
        self.assertGreater(np.linalg.norm(target[:, :, 0, 0]-pair[:, :, 0, 0]), 0.002)

    def test_current_loop_is_a_three_tensor_not_an_observer_independent_time_scalar(self):
        change = np.eye(4)
        change[0, 0], change[0, 3] = np.cosh(0.3), np.sinh(0.3)
        change[3, 0], change[3, 3] = np.sinh(0.3), np.cosh(0.3)
        current = self.data["current"]
        transformed = np.einsum("mn,nij->mij", change, current)
        target = np.einsum("ma,nb,pc,abc->mnp", change, change, change, model.loop_tensor(current))
        self.assertClose(model.loop_tensor(transformed), target)

    def test_complex_loop_control_has_nonzero_invariant_cyclic_phase(self):
        current = model.complex_loop_control()
        loop = model.loop_tensor(current)[0, 0, 0]
        self.assertClose(loop, 0.25-0.25j)
        self.assertClose(np.angle(loop), -np.pi/4)
        g = self.maximal_unitary()
        self.assertClose(model.loop_tensor(g @ current @ g.conj().T)[0, 0, 0], loop)

    def test_on_shell_real_polarization_has_no_nontrivial_time_loop_phase(self):
        loop = model.loop_tensor(self.data["current"])[0, 0, 0]
        self.assertGreater(loop.real, 0.00012)
        self.assertLess(abs(loop.imag), 1e-14)

    def test_spectral_block_deletion_control_removes_cross_products_not_a_quantum_claim(self):
        current = model.spectral.spectral_projection(model.complex_loop_control())
        pairs = model.pair_tensors(current)
        for a in range(3):
            for b in range(3):
                if a != b:
                    self.assertClose(pairs[a, b], 0)
        self.assertClose(model.loop_tensor(current), 0)

    def test_nonlinear_readouts_have_different_probe_scaling_from_the_coframe(self):
        amplitude = 1.7
        current = self.data["current"]
        self.assertClose(model.pair_tensors(amplitude**2*current), amplitude**4*model.pair_tensors(current))
        self.assertClose(model.loop_tensor(amplitude**2*current), amplitude**6*model.loop_tensor(current))
        self.assertClose(model.pairing(amplitude*self.data["psi"], amplitude*self.jet),
                         amplitude**2*model.pairing(self.data["psi"], self.jet))

    def test_quadratic_current_tensors_do_not_fill_missing_angular_directions(self):
        pair = model.pair_tensors(self.data["current"])
        self.assertClose(pair[:, :, 1:3], 0)
        self.assertClose(pair[:, :, :, 1:3], 0)
        for a in range(3):
            for b in range(3):
                self.assertLessEqual(np.sum(np.linalg.svd(pair[a, b], compute_uv=False) > 1e-10), 2)

    def test_invalid_jets_selectors_and_current_shapes(self):
        with self.assertRaises(ValueError):
            model.pairing(np.zeros((6, 3)), np.zeros((4, 6, 3)))
        with self.assertRaises(ValueError):
            model.pairing(self.data["psi"], self.jet[:3])
        with self.assertRaises(ValueError):
            model.pairing(self.data["psi"], self.jet, np.eye(3))
        for function in (model.pair_tensors, model.loop_tensor):
            with self.assertRaises(ValueError):
                function(np.zeros((4, 3, 3)))

    def test_saved_report_reproduces_without_native_or_quantum_promotion(self):
        saved = json.loads((ROOT / "analysis/HC_Gauge_Invariant_Geometry_Readouts.json").read_text(encoding="utf-8"))

        def compare(actual, expected):
            if isinstance(expected, float):
                self.assertClose(actual, expected)
            elif isinstance(expected, dict):
                self.assertEqual(actual.keys(), expected.keys())
                for key, value in expected.items():
                    compare(actual[key], value)
            elif isinstance(expected, list):
                self.assertEqual(len(actual), len(expected))
                for a, b in zip(actual, expected):
                    compare(a, b)
            else:
                self.assertEqual(actual, expected)

        compare(self.report, saved)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["candidate_matrix_readouts"]["quartic_sextic_classical_products_not_native_metric_replacements_or_quantum_observables"])
        self.assertIn("NOT induced product geometry", self.report["status"])


if __name__ == "__main__":
    unittest.main()
