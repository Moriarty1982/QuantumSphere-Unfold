"""Connected intertwiners, missing readout locks and common-frame transport."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "triadic_intertwiner_classification", ROOT / "analysis/HC_Triadic_Intertwiner_Classification.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCTriadicIntertwinerClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = model.evaluate()
        cls.cases = model.reference_cases()
        cls.data = model.framed_data()

    def assertClose(self, actual, expected, atol=1e-9):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=4e-8)

    def block_diagonal(self, blocks):
        n = len(blocks[0])
        return sum(np.kron(np.diag(np.eye(len(blocks))[i]), x) for i, x in enumerate(blocks))

    def test_hermitian_basis_is_real_orthonormal_and_complete(self):
        basis = model.hermitian_basis(6)
        self.assertEqual(basis.shape, (36, 6, 6))
        self.assertClose(basis, basis.conj().swapaxes(-1, -2))
        self.assertClose(np.einsum("aij,bij->ab", basis.conj(), basis), np.eye(36))

    def test_scalar_links_with_fixed_channel_labels_force_common_four_dimensional_algebra(self):
        basis = self.cases["scalar_tree_locked"]["basis"]
        self.assertEqual(len(basis), 4)
        for x in basis:
            self.assertClose(x[:2, :2], x[2:4, 2:4])
            self.assertClose(x[:2, :2], x[4:, 4:])
            self.assertClose(x, self.block_diagonal([x[:2, :2]]*3))

    def test_resonance_alone_does_not_force_common_channel_representation(self):
        self.assertEqual(self.cases["same_resonance_without_channel_locks"]["dimension"], 12)
        omega = model.coupled_operator()
        p = model.channel_projectors()[0]
        self.assertClose(model.commutator(omega, omega), 0)
        self.assertGreater(np.linalg.norm(model.commutator(omega, p)), 7)

    def test_unequal_nonzero_scalar_gains_and_phases_preserve_common_algebra(self):
        for a, b in ((4, 0.7), (0.01, 2), (3*np.exp(0.4j), 0.8*np.exp(-0.2j))):
            self.assertEqual(model.classify(a*np.eye(2), b*np.eye(2))["dimension"], 4)

    def test_one_anisotropic_link_restricts_root_to_diagonal_generators(self):
        self.assertEqual(self.cases["one_anisotropic_link"]["dimension"], 2)
        for x in self.cases["one_anisotropic_link"]["basis"]:
            self.assertClose(x-np.diag(np.diag(x)), 0)

    def test_two_noncommuting_grams_leave_only_central_common_generator(self):
        case = self.cases["two_noncommuting_link_grams"]
        self.assertEqual(case["dimension"], 1)
        generator = case["basis"][0]
        self.assertClose(generator, np.trace(generator)*np.eye(6)/6)

    def test_scalar_cycle_phase_does_not_reduce_the_common_algebra(self):
        self.assertEqual(self.cases["scalar_cycle_phase"]["dimension"], 4)

    def test_noncentral_matrix_cycle_map_restricts_the_common_algebra(self):
        case = self.cases["matrix_cycle_phase"]
        self.assertEqual(case["dimension"], 2)
        loop = np.diag(np.exp(1j*np.array([0.3, -0.3])))
        for x in case["basis"]:
            self.assertClose(model.commutator(x[-2:, -2:], loop), 0)

    def test_scalar_cycle_phase_can_change_spectrum_without_changing_gauge_algebra(self):
        zero = model.coupled_operator(direct=0.2*np.eye(2))
        quarter = model.coupled_operator(direct=0.2j*np.eye(2))
        self.assertGreater(np.linalg.norm(np.linalg.eigvalsh(zero)-np.linalg.eigvalsh(quarter)), 0.05)
        self.assertClose(np.trace(zero @ zero @ zero-quarter @ quarter @ quarter), 2*6*4*0.7*0.2)
        self.assertEqual(model.classify(direct=0.2j*np.eye(2))["dimension"], 4)

    def test_cycle_endomorphism_is_covariant_under_different_channel_bases(self):
        first, second, direct = 4*np.eye(2), 0.7*np.eye(2), 0.2*model.PAULI[2]
        unitaries = [np.cos(a)*np.eye(2)+1j*np.sin(a)*p for a, p in zip((0.4, 0.2, -0.3), model.PAULI)]
        u1, u2, u0 = unitaries
        changed = (u1 @ first @ u0.conj().T, u2 @ second @ u0.conj().T, u1 @ direct @ u2.conj().T)
        before = model.root_obstructions(first, second, direct)[-1]
        after = model.root_obstructions(*changed)[-1]
        self.assertClose(after, u0 @ before @ u0.conj().T)
        self.assertClose(np.sort_complex(np.linalg.eigvals(after)), np.sort_complex(np.linalg.eigvals(before)))

    def test_rank_deficient_and_disconnected_channels_retain_extra_generators(self):
        self.assertEqual(self.cases["rank_deficient_first_link"]["dimension"], 3)
        self.assertEqual(self.cases["disconnected_first_channel"]["dimension"], 8)
        self.assertEqual(model.classify(np.zeros((2, 2)), np.zeros((2, 2)))["dimension"], 12)

    def test_scalar_channel_charge_is_common_but_not_numerically_fixed(self):
        case = model.classify(4*np.eye(1), 0.7*np.eye(1))
        self.assertEqual(case["dimension"], 1)
        for charge in (-3.2, 0, 1, 12):
            self.assertClose(model.commutator(charge*np.eye(3), model.coupled_operator(4*np.eye(1), 0.7*np.eye(1))), 0)

    def test_root_reduction_matches_full_block_equations(self):
        rotation = np.array([[1, -1], [1, 1]])/np.sqrt(2)
        cases = [(4*np.eye(2), 0.7*np.eye(2), None),
                 (np.diag([4, 2]), 0.7*np.eye(2), None),
                 (np.diag([4, 2]), rotation @ np.diag([0.7, 0.3]) @ rotation.T, None),
                 (4*np.eye(2), 0.7*np.eye(2), 0.2*np.diag(np.exp(1j*np.array([0.3, -0.3]))))]
        for first, second, direct in cases:
            root = model.commutant(model.root_obstructions(first, second, direct))
            full = model.classify(first, second, direct)
            self.assertEqual(root["dimension"], full["dimension"])
            for t0 in root["basis"]:
                t1 = first @ t0 @ np.linalg.inv(first)
                t2 = second @ t0 @ np.linalg.inv(second)
                generator = self.block_diagonal([t1, t2, t0])
                self.assertClose(generator, generator.conj().T)
                self.assertClose(model.commutator(generator, model.coupled_operator(first, second, direct)), 0)

    def test_unitary_links_derive_equivalent_not_identically_written_generators(self):
        u1 = np.cos(0.4)*np.eye(2)+1j*np.sin(0.4)*model.PAULI[0]
        u2 = np.cos(0.2)*np.eye(2)+1j*np.sin(0.2)*model.PAULI[2]
        omega = model.coupled_operator(4*u1, 0.7*u2)
        t0 = model.PAULI[1]
        t1, t2 = u1 @ t0 @ u1.conj().T, u2 @ t0 @ u2.conj().T
        self.assertClose(model.commutator(self.block_diagonal([t1, t2, t0]), omega), 0)
        self.assertGreater(np.linalg.norm(t1-t0), 1)
        self.assertEqual(model.classify(4*u1, 0.7*u2)["dimension"], 4)

    def test_anisotropic_similarity_is_not_automatically_a_hermitian_generator(self):
        k = np.diag([4, 2])
        image = k @ model.PAULI[0] @ np.linalg.inv(k)
        self.assertGreater(np.linalg.norm(image-image.conj().T), 2)
        self.assertGreater(np.linalg.norm(model.commutator(model.PAULI[0], k.conj().T @ k)), 10)

    def test_every_reported_basis_is_hermitian_and_solves_fixed_constraints(self):
        for case in self.cases.values():
            self.assertClose(case["basis"], case["basis"].conj().swapaxes(-1, -2))
            self.assertLess(case["max_basis_residual"], 1e-10)

    def test_common_commutant_is_closed_under_hermitian_lie_bracket(self):
        basis = self.cases["scalar_tree_locked"]["basis"]
        for a in basis:
            for b in basis:
                bracket = 1j*model.commutator(a, b)
                coefficients = np.einsum("aij,ij->a", basis.conj(), bracket).real
                self.assertClose(np.einsum("a,aij->ij", coefficients, basis), bracket)

    def test_commutant_dimension_is_invariant_under_simultaneous_basis_change(self):
        permutation = np.eye(6)[[0, 2, 4, 1, 3, 5]]
        operators = [model.coupled_operator(), *model.channel_projectors()]
        transformed = [permutation @ x @ permutation.T for x in operators]
        self.assertEqual(model.commutant(transformed)["dimension"], 4)

    def test_local_frame_and_both_derivative_orders_are_correct(self):
        point, step = self.data["base"]["point"], 1e-5
        s, ds, dds = model.local_frame_jet(point)
        self.assertClose(s.conj().T @ s, np.eye(6))
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.local_frame_jet(point+step*direction), model.local_frame_jet(point-step*direction)
            self.assertClose((plus[0]-minus[0])/(2*step), ds[mu])
            self.assertClose((plus[1]-minus[1])/(2*step), dds[mu])

    def test_framed_probe_connection_and_projector_jets(self):
        d, step = self.data, 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.framed_data(d["base"]["point"]+step*direction), model.framed_data(d["base"]["point"]-step*direction)
            for name, derivative in (("psi", "psi_first"), ("connection", "connection_first"), ("P", "P_first")):
                self.assertClose((plus[name]-minus[name])/(2*step), d[derivative][mu])

    def test_mass_spectrum_and_scalar_bilinear_are_unchanged_by_the_frame(self):
        d, base = self.data, self.data["base"]
        self.assertClose(np.linalg.eigvalsh(d["mass_operator"]), np.linalg.eigvalsh(base["mass_operator"]))
        self.assertClose(np.trace(d["mass_operator"] @ d["scalar"]), np.trace(base["mass_operator"] @ base["scalar"]))
        self.assertClose(np.trace(d["P"]), np.trace(base["P"]))

    def test_full_correct_transformed_fields_solve_the_same_declared_equations(self):
        result = model.frame_checks()
        for name, value in result.items():
            self.assertLess(np.linalg.norm(value), 2e-8, name)

    def test_shifted_channels_without_connection_term_do_not_solve_dirac(self):
        result = model.frame_checks(connection_shift=False)
        self.assertGreater(np.linalg.norm(result["Dirac"]), 0.2)
        self.assertGreater(np.linalg.norm(result["curvature_covariance"]), 0.1)

    def test_shifting_channels_but_freezing_resonance_does_not_solve_dirac(self):
        result = model.frame_checks(rotate_mass=False)
        self.assertGreater(np.linalg.norm(result["Dirac"]), 0.32)

    def test_gauge_embedding_must_be_transformed_with_the_fields(self):
        d, s = self.data, self.data["S"]
        original = np.kron(model.PAULI[1], np.eye(3))
        transported = s @ original @ s.conj().T
        self.assertClose(model.commutator(transported, d["mass_operator"]), 0)
        self.assertGreater(np.linalg.norm(model.commutator(original, d["mass_operator"])), 1)
        self.assertClose(model.framed_projection(transported, s), transported)

    def test_projection_covariance_does_not_gauge_new_channel_directions(self):
        d, s = self.data, self.data["S"]
        projected = model.framed_projection(d["scalar"], s)
        expected = s @ model.factor.gauge_projection(d["base"]["scalar"]) @ s.conj().T
        self.assertClose(projected, expected)
        self.assertGreater(np.linalg.norm(projected-d["scalar"]), 0.15)

    def test_correct_frame_at_other_curved_points(self):
        for point, radius in (([-0.3, 2.4, 1.2, -0.01], 1.6), ([0.2, 0.5, -0.4, 0.01], 0.8)):
            for name, value in model.frame_checks(point, radius=radius).items():
                self.assertLess(np.linalg.norm(value), 2e-8, name)

    def test_source_readouts_are_not_silently_promoted_to_fixed_channel_projectors(self):
        text = (ROOT / "sources/research/parts/v470/12_structural_core.tex").read_text(encoding="utf-8")
        self.assertIn("be admissible readout maps", text)
        self.assertTrue(self.report["native_audit"]["fixed_readout_locks_are_an_additional_hypothesis"])
        self.assertTrue(self.report["native_audit"]["readouts_in_source_are_general_maps_not_fixed_orthogonal_channel_projectors"])

    def test_invalid_operators_links_domains_frames_and_steps(self):
        for size in (0, 13, True):
            with self.assertRaises(ValueError):
                model.hermitian_basis(size)
        for operators in ([], [np.ones((2, 3))], [np.eye(2), np.eye(3)]):
            with self.assertRaises(ValueError):
                model.commutant(operators)
        with self.assertRaises(ValueError):
            model.coupled_operator(np.ones((2, 3)), np.eye(2))
        with self.assertRaises(ValueError):
            model.root_obstructions(np.diag([1, 0]), np.eye(2))
        with self.assertRaises(ValueError):
            model.classify(lock_channels="yes")
        with self.assertRaises(ValueError):
            model.framed_projection(np.eye(6), 2*np.eye(6))
        with self.assertRaises(ValueError):
            model.framed_data(connection_shift="yes")
        with self.assertRaises(ValueError):
            model.frame_checks(step=0)

    def test_saved_report_reproduces_and_does_not_identify_native_charges_or_frames(self):
        saved = json.loads((ROOT / "analysis/HC_Triadic_Intertwiner_Classification.json").read_text(encoding="utf-8"))

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
        self.assertTrue(self.report["local_basis_checks"]["not_independent_physical_gauge_transformations_of_the_original_fixed_embedding"])
        self.assertIn("NOT native gauge charges", self.report["status"])


if __name__ == "__main__":
    unittest.main()
