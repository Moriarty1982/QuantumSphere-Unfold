"""Algebraic and supplied finite-model checks, not native activation proofs."""
from fractions import Fraction
import importlib.util
from itertools import product
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "kernel_fragment_audit", ROOT / "scripts/qsc_audit/kernel_fragment_audit.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def relation(*classes):
    return {(a, b) for group in classes for a in group for b in group}


def koide(roots):
    return sum(x*x for x in roots) / sum(roots)**2


class KoideProofTests(unittest.TestCase):
    def test_exact_symmetric_orthogonal_decomposition(self):
        for roots in ((1, 2, 3), (0, 0, 5), (2, 2, 2), (1, 3, 7)):
            x = tuple(map(Fraction, roots))
            mean = sum(x)/3
            defect = sum((v-mean)**2 for v in x)
            self.assertEqual(koide(x), Fraction(1, 3) + defect/(9*mean*mean))
            self.assertEqual(sum(v-mean for v in x), 0)

    def test_cyclic_conservation_does_not_select_two_thirds(self):
        roots = tuple(map(Fraction, (1, 2, 3)))
        for k in range(3):
            rotated = roots[k:] + roots[:k]
            self.assertEqual(sum(rotated), 6)
            self.assertEqual(sum(x*x for x in rotated), 14)
            self.assertEqual(koide(rotated), Fraction(7, 18))
            self.assertNotEqual(koide(rotated), Fraction(2, 3))

    def test_degenerate_positive_roots_have_one_third(self):
        self.assertEqual(koide((Fraction(2),)*3), Fraction(1, 3))

    def test_radius_identity_on_positive_chambers(self):
        checked = 0
        for radius, theta in product((0, 0.5, 1, math.sqrt(2), 1.9), (0, 0.4, 2.1, 2.3)):
            roots = [1 + radius*math.cos(theta+2*math.pi*k/3) for k in range(3)]
            if min(roots) >= 0:
                self.assertAlmostEqual(koide(roots), 1/3 + radius**2/6, places=13)
                checked += 1
        self.assertGreater(checked, 10)

    def test_koide_radius_does_not_fix_phase_or_scale(self):
        patterns = []
        for theta in (2.1, 2.2, 2.3):
            roots = [1+math.sqrt(2)*math.cos(theta+2*math.pi*k/3) for k in range(3)]
            self.assertGreater(min(roots), 0)
            self.assertAlmostEqual(koide(roots), 2/3, places=13)
            self.assertAlmostEqual(koide([7*x for x in roots]), 2/3, places=13)
            patterns.append(roots)
        self.assertNotEqual(patterns[0], patterns[1])

    def test_negative_signed_roots_do_not_give_physical_koide_identity(self):
        signed = [1+math.sqrt(2)*math.cos(math.pi+2*math.pi*k/3) for k in range(3)]
        self.assertLess(signed[0], 0)
        self.assertAlmostEqual(koide(signed), 2/3, places=13)
        self.assertGreater(abs(koide([abs(x) for x in signed])-2/3), 0.2)

    def test_beta_zero_at_fixed_radius_is_not_mass_degeneracy(self):
        theta = math.pi - math.sqrt(2)*math.asin(0)
        masses = [(1+math.sqrt(2)*math.cos(theta+2*math.pi*k/3))**2 for k in range(3)]
        self.assertAlmostEqual(masses[0], 3-2*math.sqrt(2), places=13)
        self.assertAlmostEqual(masses[1], 1.5+math.sqrt(2), places=13)
        self.assertAlmostEqual(masses[1], masses[2], places=13)
        self.assertGreater(masses[1]-masses[0], 2)

    def test_circulant_linear_maps_keep_symmetric_input(self):
        for a, b, c in product(range(3), repeat=3):
            matrix = ((a, b, c), (c, a, b), (b, c, a))
            image = [sum(3*entry for entry in row) for row in matrix]
            self.assertEqual(image, [3*(a+b+c)]*3)

    def test_fixed_paper_input_diagnostics_are_reproduced(self):
        masses = (0.51100, 105.658, 1776.86)
        roots = [math.sqrt(m) for m in masses]
        amplitude = sum(roots)/3
        theta_obs = math.atan2(-sum(x*math.sin(2*math.pi*k/3) for k, x in enumerate(roots)),
                              sum(x*math.cos(2*math.pi*k/3) for k, x in enumerate(roots)))
        theta = math.pi-math.sqrt(2)*math.asin(0.5493)
        predicted = [(amplitude*(1+math.sqrt(2)*math.cos(theta+2*math.pi*k/3)))**2 for k in range(3)]
        self.assertAlmostEqual(math.degrees(theta_obs), 132.7327925517321, places=10)
        self.assertAlmostEqual(math.degrees(theta), 132.87981366307108, places=10)
        self.assertAlmostEqual(koide(roots), 0.6666608187172461, places=13)
        self.assertAlmostEqual(100*(predicted[0]/masses[0]-1), -12.799515006340755, places=8)

    def test_hc_shaped_projection_has_the_derived_correlation_formula(self):
        e = [1/math.sqrt(3)]*3
        v = [-2/math.sqrt(6), 1/math.sqrt(6), 1/math.sqrt(6)]
        for h in (0, 0.2, 0.5, 0.9):
            c, s = math.sqrt((1-h)/2), math.sqrt((1+h)/2)
            n = [c*a+s*b for a, b in zip(e, v)]
            dot = sum(a*b for a, b in zip(e, n))
            projected = [a-dot*b for a, b in zip(e, n)]
            je = [a-2*dot*b for a, b in zip(e, n)]
            self.assertGreater(min(projected), 0)
            self.assertAlmostEqual(sum(a*b for a, b in zip(e, je)), h, places=13)
            self.assertAlmostEqual(koide(projected), 2/(3*(1+h)), places=13)

    def test_identity_involution_is_hc_shaped_but_not_koide(self):
        e = [1/math.sqrt(3)]*3
        self.assertAlmostEqual(koide(e), 1/3, places=13)
        self.assertNotAlmostEqual(koide(e), 2/3, places=10)


class LocalKernelProofTests(unittest.TestCase):
    def setUp(self):
        self.fragment = audit.FiniteKernelFragment(range(4), relation((0, 1), (2, 3)))

    def test_payload_projection_reconstructs_each_tagged_surface(self):
        for tag, a in product((0, 1), range(4)):
            state = self.fragment.state(tag, a)
            self.assertEqual(self.fragment.state(tag, self.fragment.project(state)), state)

    def test_normal_form_is_total_idempotent_and_exact_for_classes(self):
        fragment = self.fragment
        self.assertEqual(fragment.normal_forms, {0: 0, 1: 0, 2: 2, 3: 2})
        for a, b in product(range(4), repeat=2):
            self.assertEqual(fragment.normal_form(fragment.normal_form(a)), fragment.normal_form(a))
            self.assertEqual(fragment.normal_form(a) == fragment.normal_form(b), (a, b) in fragment.closure)

    def test_invalid_relations_are_rejected_not_completed(self):
        examples = (
            (range(2), {(0, 0), (0, 1), (1, 0)}, "reflexive"),
            (range(2), {(0, 0), (1, 1), (0, 1)}, "symmetric"),
            (range(3), {(0, 0), (1, 1), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)}, "transitive"),
        )
        for payloads, pairs, message in examples:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                audit.FiniteKernelFragment(payloads, pairs)

    def test_empty_duplicate_and_noninteger_payloads_are_rejected(self):
        for payloads in ((), (0, 0), (True, 1), (-1, 0), (0, 0.5)):
            with self.subTest(payloads=payloads), self.assertRaises(ValueError):
                audit.FiniteKernelFragment(payloads, ())

    def test_invalid_state_tags_and_payloads_are_rejected(self):
        for state in ((2, 0), (True, 0), (0, 9), (1, True), (0, 1, 2)):
            with self.subTest(state=state), self.assertRaises(ValueError):
                self.fragment.project(state)

    def test_total_readout_factors_through_the_class_minima(self):
        result = self.fragment.audit_readout({0: 7, 1: 7, 2: 11, 3: 11})
        self.assertTrue(result["exact_partial_factorization"])
        self.assertTrue(result["total_on_fragment"])
        self.assertEqual(result["factor_on_observed_classes"], {0: 7, 2: 11})

    def test_only_post_class_map_values_need_to_be_constant(self):
        raw = {a: a for a in range(4)}
        self.assertFalse(self.fragment.audit_readout(raw)["constant_on_fibres"])
        post_class_map = {a: value//2 for a, value in raw.items()}
        self.assertTrue(self.fragment.audit_readout(post_class_map)["exact_partial_factorization"])

    def test_noninvariant_aspect_cannot_be_preserved_by_normalization(self):
        aspect = {0: "left", 1: "right", 2: "other", 3: "other"}
        self.assertFalse(self.fragment.audit_readout(aspect)["constant_on_fibres"])

    def test_partial_unsaturated_domain_is_not_silently_extended(self):
        result = self.fragment.audit_readout({0: 7})
        self.assertTrue(result["constant_on_fibres"])
        self.assertEqual(result["factor_on_observed_classes"], {0: 7})
        self.assertFalse(result["domain_saturated"])
        self.assertFalse(result["exact_partial_factorization"])

    def test_saturated_partial_readout_has_exact_partial_factorization(self):
        result = self.fragment.audit_readout({0: 7, 1: 7})
        self.assertTrue(result["exact_partial_factorization"])
        self.assertFalse(result["total_on_fragment"])

    def test_empty_partial_readout_needs_no_total_extension(self):
        result = self.fragment.audit_readout({})
        self.assertTrue(result["exact_partial_factorization"])
        self.assertFalse(result["total_on_fragment"])
        self.assertEqual(result["factor_on_observed_classes"], {})

    def test_readout_conflicts_unknown_payload_and_nan_are_detected(self):
        result = self.fragment.audit_readout({0: 7, 1: 8})
        self.assertFalse(result["constant_on_fibres"])
        self.assertIsNone(result["factor_on_observed_classes"])
        for values in ({9: 0}, {0: float("nan")}):
            with self.assertRaises(ValueError):
                self.fragment.audit_readout(values)

    def test_bare_macro_identity_does_not_prove_factorization(self):
        normal_forms = {0: 0, 1: 0}
        payload = lambda state: state[1]
        for a in (0, 1):
            self.assertEqual(normal_forms[payload((0, a))], normal_forms[a])
        self.assertFalse(audit.audit_factorization(normal_forms, {0: 0, 1: 1})["constant_on_fibres"])

    def test_transport_only_preserves_the_supplied_admissible_edges(self):
        self.assertTrue(self.fragment.transport_preserved(((0, 1), (3, 2))))
        self.assertFalse(self.fragment.transport_preserved(((0, 2),)))
        with self.assertRaises(ValueError):
            self.fragment.transport_preserved(((0, 9),))

    def test_class_compression_does_not_reconstruct_distinct_payloads(self):
        state = self.fragment.state(1, 1)
        compressed = self.fragment.normal_form(self.fragment.project(state))
        self.assertNotEqual(self.fragment.state(1, compressed), state)

    def test_payload_preserving_shift_commutes_with_normalization(self):
        for a in range(4):
            before, after = self.fragment.state(0, a), self.fragment.state(1, a)
            self.assertEqual(self.fragment.project(before), self.fragment.project(after))
            self.assertEqual(self.fragment.normal_form(self.fragment.project(before)),
                             self.fragment.normal_form(self.fragment.project(after)))

    def test_projection_aggregator_passes_the_local_gate(self):
        table = {row: row[0] for row in product(range(4), repeat=2)}
        result = self.fragment.audit_aggregation(2, table)
        self.assertTrue(result["local_routed_gate"])
        self.assertTrue(result["common_class_preserved"])

    def test_normalized_weights_do_not_make_constant_aggregator_class_preserving(self):
        self.assertEqual(Fraction(1, 2)+Fraction(1, 2), 1)
        table = {row: 2 for row in product(range(4), repeat=2)}
        result = self.fragment.audit_aggregation(2, table)
        self.assertTrue(result["congruent_on_classes"])
        self.assertFalse(result["diagonal_class_preserved"])
        self.assertFalse(result["common_class_preserved"])
        self.assertFalse(result["local_routed_gate"])

    def test_noncongruent_aggregator_does_not_descend(self):
        table = {row: (0 if row[0] == 0 else 2) for row in product(range(4), repeat=2)}
        result = self.fragment.audit_aggregation(2, table)
        self.assertFalse(result["congruent_on_classes"])
        self.assertIsNone(result["quotient_operation"])

    def test_diagonal_preservation_alone_is_insufficient(self):
        table = {row: row[0] for row in product(range(4), repeat=2)}
        table[(1, 2)] = 2
        result = self.fragment.audit_aggregation(2, table)
        self.assertTrue(result["diagonal_class_preserved"])
        self.assertFalse(result["congruent_on_classes"])

    def test_total_aggregation_domain_and_code_types_are_checked(self):
        valid = {row: row[0] for row in product(range(4), repeat=2)}
        incomplete = dict(valid)
        del incomplete[(0, 0)]
        invalid_value = dict(valid)
        invalid_value[(0, 0)] = 9
        boolean_key = dict(valid)
        del boolean_key[(1, 0)]
        boolean_key[(True, 0)] = 1
        for table in (incomplete, invalid_value, boolean_key):
            with self.assertRaises(ValueError):
                self.fragment.audit_aggregation(2, table)
        with self.assertRaises(ValueError):
            self.fragment.audit_aggregation(True, valid)

    def test_exhaustive_two_code_operations_satisfy_the_proved_implication(self):
        for pairs in (relation((0,), (1,)), relation((0, 1))):
            fragment = audit.FiniteKernelFragment((0, 1), pairs)
            inputs = tuple(product((0, 1), repeat=2))
            for outputs in product((0, 1), repeat=4):
                result = fragment.audit_aggregation(2, dict(zip(inputs, outputs)))
                if result["local_routed_gate"]:
                    self.assertTrue(result["common_class_preserved"])

    def test_normalized_linear_readout_aggregation_preserves_a_common_value(self):
        weights = (Fraction(1, 3), Fraction(2, 3))
        value = Fraction(7, 5)
        self.assertEqual(sum(w*value for w in weights), value)

    def test_positive_instance_has_all_declared_local_gates(self):
        fragment = self.fragment
        for aspect in ({a: "state" for a in range(4)},
                       {a: a//2 for a in range(4)},
                       {a: ("class", a//2) for a in range(4)}):
            self.assertTrue(fragment.audit_readout(aspect)["exact_partial_factorization"])
        self.assertTrue(fragment.audit_readout({0: 7, 1: 7, 2: 11, 3: 11})["exact_partial_factorization"])
        self.assertTrue(fragment.transport_preserved(((0, 1), (1, 0), (2, 3), (3, 2))))
        table = {row: row[0] for row in product(range(4), repeat=2)}
        self.assertTrue(fragment.audit_aggregation(2, table)["local_routed_gate"])
