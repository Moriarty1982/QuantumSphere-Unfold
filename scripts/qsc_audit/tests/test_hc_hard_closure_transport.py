"""Normal master transport, compatible connections and hard-closure curvature freedom."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "hard_transport", ROOT / "analysis/HC_Hard_Closure_Transport.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCHardClosureTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.texture()
        cls.report = model.evaluate()
        cls.point = np.array([0.0, 0.2, -0.1, 0.0])

    def setUp(self):
        self.rng = np.random.default_rng(391)

    def assertClose(self, actual, expected, rtol=3e-8, atol=2e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def normal(self, data=None, omega=None, connection=None):
        d = self.data if data is None else data
        return model.normal_operator(d["P"], d["P_first"],
                                     d["connection"] if connection is None else connection,
                                     0.6*np.eye(2) if omega is None else omega)

    def reduced(self, data=None, connection=None, first=None):
        d = self.data if data is None else data
        return model.reduce_frame(d["frame"], d["frame_first"], d["frame_second"],
                                  d["connection"] if connection is None else connection,
                                  d["connection_first"] if first is None else first, 0.6*np.eye(2))

    def test_spin_basis_has_the_required_five_independent_components(self):
        basis = np.concatenate([np.eye(4)[None], model.GAMMA])
        gram = np.einsum("aij,bij->ab", basis.conj(), basis)
        self.assertClose(gram, 4*np.eye(5))

    def test_normal_operator_norm_identity(self):
        raw = self.rng.normal(size=(4, 2, 2))+1j*self.rng.normal(size=(4, 2, 2))
        omega = self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))
        d = self.normal(connection=raw, omega=omega)
        self.assertClose(d["norm_squared"], d["coefficient_norm_squared"])

    def test_M_commutation_alone_does_not_preserve_full_transport(self):
        p, m = np.diag([1.0, 0.0]), np.diag([0.4, 1.3])
        b = np.zeros((4, 2, 2), complex)
        b[1] = 1j*model.PAULI[0]
        self.assertClose(model.commutator(m, p), 0)
        d = model.normal_operator(p, np.zeros_like(b), b, m)
        self.assertGreater(d["norm_squared"], 0)

    def test_separate_triadic_resonance_leakage_is_not_removed_by_M_closure(self):
        p = np.diag([1.0, 0.0])
        b = np.zeros((4, 2, 2), complex)
        d = model.normal_operator(p, b, b, model.PAULI[0])
        self.assertClose(d["transport_leakage"], 0)
        self.assertGreater(np.linalg.norm(d["resonance_leakage"]), 0)

    def test_one_sided_nonunitary_invariance_is_not_full_covariant_constancy(self):
        p = np.diag([1.0, 0.0])
        b = np.zeros((4, 2, 2), complex)
        b[1, 0, 1] = 1
        d = model.normal_operator(p, np.zeros_like(b), b, np.eye(2))
        self.assertClose(d["operator"], 0)
        self.assertGreater(np.linalg.norm(d["covariant_projector_first"]), 0)

    def test_moving_P_without_its_connection_leaks(self):
        d = self.normal(connection=np.zeros((4, 2, 2)))
        self.assertGreater(np.linalg.norm(d["operator"]), 0.8)

    def test_canonical_connection_cancels_the_off_sector_master_operator(self):
        self.assertClose(self.normal()["operator"], 0)

    def test_general_compatible_unitary_connection_has_arbitrary_diagonal_data(self):
        p, dp = self.data["P"], self.data["P_first"]
        diagonal = np.array([1j*x*p+1j*y*(np.eye(2)-p)
                             for x, y in self.rng.normal(size=(4, 2))])
        b = model.compatible_connection(p, dp, diagonal)
        self.assertClose(dp+model.commutator(b, p), 0)
        self.assertClose(b, -b.conj().swapaxes(-1, -2))

    def test_invalid_off_block_compatible_addition_is_rejected(self):
        p, dp = np.diag([1.0, 0.0]), np.zeros((4, 2, 2))
        c = np.zeros((4, 2, 2), complex)
        c[1] = 1j*model.PAULI[0]
        with self.assertRaises(ValueError):
            model.compatible_connection(p, dp, c)

    def test_projector_and_frame_are_independently_consistent(self):
        d = self.data
        self.assertClose(d["P"] @ d["P"], d["P"])
        self.assertClose(d["U"].conj().T @ d["U"], np.eye(2))
        self.assertClose(d["frame"] @ d["frame"].conj().T, d["P"])
        self.assertClose(d["P_first"], d["frame_first"] @ d["frame"].conj().T
                         +d["frame"] @ d["frame_first"].conj().swapaxes(-1, -2))

    def test_texture_first_and_second_jets_match_finite_differences(self):
        step = 1e-5
        for mu, e in enumerate(np.eye(4)):
            plus, minus = model.texture(self.point+step*e), model.texture(self.point-step*e)
            self.assertClose((plus["P"]-minus["P"])/(2*step), self.data["P_first"][mu])
            self.assertClose((plus["P_first"]-minus["P_first"])/(2*step), self.data["P_second"][mu])
            self.assertClose((plus["U_first"]-minus["U_first"])/(2*step), self.data["U_second"][mu])

    def test_full_connection_derivative_includes_the_closure_load(self):
        step = 1e-5
        for mu, e in enumerate(np.eye(4)):
            numerical = (model.texture(self.point+step*e)["connection"]
                         -model.texture(self.point-step*e)["connection"])/(2*step)
            self.assertClose(numerical, self.data["connection_first"][mu])

    def test_same_projector_supports_flat_and_nonflat_non_gauge_equivalent_choices(self):
        a, b = self.data, model.texture(mix=1)
        self.assertClose(a["P"], b["P"])
        self.assertGreater(np.linalg.norm(a["curvature"]), 0.2)
        self.assertLess(np.linalg.norm(b["curvature"]), 1e-12)

    def test_every_interpolated_connection_preserves_P(self):
        for mix in (-0.3, 0, 0.4, 1, 1.7):
            self.assertClose(self.normal(model.texture(mix=mix))["covariant_projector_first"], 0)

    def test_exact_curvature_formula_for_the_whole_family(self):
        for mix in (-0.3, 0, 0.4, 1, 1.7):
            d = model.texture(mix=mix)
            self.assertClose(d["curvature"], d["expected_curvature"])

    def test_native_constant_null_load_does_not_change_this_compatible_curvature(self):
        for eta in (-2, 0, 0.7, 3):
            d = model.texture(eta=eta)
            self.assertClose(d["curvature"], self.data["curvature"])
            self.assertClose(self.normal(d)["operator"], 0)

    def test_hard_minimal_HC_is_exactly_zero_for_the_degenerate_M_example(self):
        for x in (-0.3, 0.2, 0.7):
            p = model.texture([0, x, 0.1, 0])["P"]
            h = model.hessian.phase.minimal_native_closure(1.3*np.eye(2), p)
            self.assertClose(h, 0)

    def test_printed_closure_current_vanishes_for_M_scalar(self):
        derivative = np.trace(1.3*self.data["P_first"], axis1=-2, axis2=-1)
        self.assertClose(derivative, 0)

    def test_actual_source_free_connection_equation_by_finite_differences(self):
        for mix in (0, 0.4, 1):
            self.assertLess(np.linalg.norm(model.yang_mills_check(mix=mix)), 1e-8)

    def test_reduced_probe_connection_and_curvature_have_the_expected_Berry_form(self):
        for mix in (0, 0.4, 1):
            d = model.texture(mix=mix)
            reduced = self.reduced(d)
            self.assertClose(reduced["connection"][:, 0, 0], d["reduced_expected"])
            self.assertClose(reduced["curvature"][1, 2, 0, 0], 1j*d["constant_flux"])

    def test_curvature_compression_matches_the_direct_reduced_connection(self):
        d = self.data
        compressed = model.compressed_curvature(d["P"], d["P_first"], d["connection"], d["curvature"])
        reduced = d["frame"].conj().T @ compressed @ d["frame"]
        self.assertClose(reduced, self.reduced()["curvature"])

    def test_naive_compression_has_an_extrinsic_term_even_when_full_F_is_zero(self):
        d = self.data
        b, db, f = np.zeros((4, 2, 2)), np.zeros((4, 4, 2, 2)), np.zeros((4, 4, 2, 2))
        compressed = model.compressed_curvature(d["P"], d["P_first"], b, f)
        self.assertGreater(np.linalg.norm(compressed), 0.1)
        self.assertClose(d["frame"].conj().T @ compressed @ d["frame"],
                         self.reduced(connection=b, first=db)["curvature"])

    def test_constant_P_compression_removes_off_block_connection_contributions_correctly(self):
        p = np.diag([1.0, 0.0])
        b = np.zeros((4, 2, 2), complex)
        b[1], b[2] = 1j*model.PAULI[0], 1j*model.PAULI[1]
        f = model.checks.connection_curvature(b, np.zeros((4, 4, 2, 2)))
        self.assertGreater(np.linalg.norm(p @ f @ p), 0)
        self.assertClose(model.compressed_curvature(p, np.zeros_like(b), b, f), 0)

    def test_lifted_master_residual_identity_for_arbitrary_probe_jets(self):
        chi = self.rng.normal(size=(1, 4))+1j*self.rng.normal(size=(1, 4))
        derivative = self.rng.normal(size=(4, 1, 4))+1j*self.rng.normal(size=(4, 1, 4))
        for mix in (0, 0.4, 1):
            self.assertClose(model.lifted_residual(model.texture(mix=mix), chi, derivative)["lift_error"], 0)

    def test_unmodified_master_normal_component_matches_the_obstruction_on_a_closed_jet(self):
        p = self.data["P"]
        raw = self.rng.normal(size=(4, 2, 2))+1j*self.rng.normal(size=(4, 2, 2))
        psi = p @ (self.rng.normal(size=(2, 4))+1j*self.rng.normal(size=(2, 4)))
        derivative = self.data["P_first"] @ psi
        residual = model.dirac.dirac_data(psi, derivative+raw @ psi, 0.6*np.eye(2))["residual"]
        normal = self.normal(connection=raw)
        expected = (normal["operator"] @ psi.reshape(-1)).reshape(2, 4)
        self.assertClose((np.eye(2)-p) @ residual, expected)

    def test_full_spatial_transport_holonomy_converges_to_the_reduced_phase(self):
        errors = [item["error"] for item in self.report["spatial_holonomy"]]
        self.assertGreater(errors[0]/errors[1], 3.99)
        self.assertGreater(errors[1]/errors[2], 3.99)
        self.assertLess(errors[-1], 4e-8)

    def test_flat_contractible_loop_has_trivial_holonomy(self):
        result = model.loop_transport(mix=1, steps=64)
        self.assertLess(abs(result["phase"]-1), 3e-6)

    def test_noninteger_interpolation_has_the_appropriately_scaled_loop_phase(self):
        result = model.loop_transport(mix=0.4, steps=64)
        self.assertLess(result["error"], 3e-7)
        self.assertClose(result["transport"].conj().T @ result["transport"], np.eye(2))

    def test_canonical_projector_energy_starts_at_fourth_order(self):
        d = self.report["canonical_projector_energy_near_constant_P"]
        energies = d["energy"]
        self.assertGreater(energies[0]/energies[1], 15.99)
        self.assertGreater(energies[1]/energies[2], 15.99)
        self.assertEqual(model.quartic_energy(0), 0)

    def test_same_HC_and_projector_do_not_determine_the_curvature_energy(self):
        energies = [np.vdot(model.texture(mix=x)["curvature"], model.texture(mix=x)["curvature"]).real/4
                    for x in (0, 0.5, 1)]
        self.assertClose(energies[1], energies[0]/4)
        self.assertLess(energies[2], 1e-25)

    def test_invalid_texture_and_transport_parameters(self):
        with self.assertRaises(ValueError):
            model.texture([0, -10, 0, 0])
        with self.assertRaises(ValueError):
            model.loop_transport(steps=1)
        with self.assertRaises(ValueError):
            model.yang_mills_check(step=0)

    def test_invalid_projector_derivatives_are_rejected(self):
        p = np.diag([1.0, 0.0])
        first = np.repeat(np.eye(2)[None], 4, axis=0)
        with self.assertRaises(ValueError):
            model.normal_operator(p, first, np.zeros((4, 2, 2)), np.eye(2))

    def test_no_metric_or_vacuum_cancellation_is_claimed(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT a native metric/Einstein solution or vacuum cancellation", self.report["status"])
        self.assertTrue(self.report["local_source_free_family"]["not_a_full_gravitational_or_global_finite_energy_solution"])
        self.assertTrue(self.report["reduced_probe"]["this_is_an_operator_lift_identity_not_an_on_shell_backreacting_probe_solution"])

    def test_native_limit_anchors_exist(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        for label in ("thm:closed-master-system", "prop:yang-mills-limit"):
            self.assertIn("\\label{"+label+"}", text)

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Hard_Closure_Transport.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
