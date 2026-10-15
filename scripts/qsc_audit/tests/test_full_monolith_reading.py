"""Full-origin preservation and v4.8 reading-route regression checks."""
from pathlib import Path
import importlib.util
import json
import unittest
from unittest.mock import patch
from types import SimpleNamespace


SCRIPT = Path(__file__).resolve().parents[1] / "full_monolith_reading.py"
SPEC = importlib.util.spec_from_file_location("full_monolith_reading", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class FullMonolithReadingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = audit.SOURCE.read_bytes()
        cls.manifest = json.loads(audit.MANIFEST.read_text(encoding="utf-8"))
        cls.files = []
        cls.text = audit.expand(audit.WORKING / "v480-companion.tex", cls.files)
        cls.entry = (audit.WORKING / "v480-companion.tex").read_text(encoding="utf-8")

    def test_full_origin_identity_is_pinned(self):
        self.assertEqual(audit.sha(audit.canonical(self.raw)), self.manifest["canonical_origin_sha256"])
        self.assertEqual(len(audit.canonical(self.raw)), self.manifest["canonical_origin_bytes"])

    def test_crlf_lf_checkout_conversion_is_accepted(self):
        reader = Path.read_bytes

        def lf_checkout(path):
            return audit.canonical(reader(path))

        with patch.object(Path, "read_bytes", lf_checkout):
            result = audit.check()
        self.assertTrue(result["byte_identical_reconstruction_in_current_checkout"])
        self.assertEqual(result["original_label_occurrences"], 3290)

    def test_partition_reassembles_every_original_byte(self):
        pieces = audit.partition(self.raw)
        self.assertEqual(len(pieces), 38)
        self.assertEqual(b"".join(piece[3] for piece in pieces), self.raw)
        self.assertEqual(pieces[0][1], 0)
        self.assertEqual(pieces[-1][2], len(self.raw))

    def test_full_audit_preserves_original_labels_and_fragments(self):
        result = audit.check()
        self.assertEqual(result["original_label_occurrences"], 3290)
        self.assertEqual(result["inherited_fragments"], 38)
        self.assertFalse(result["missing_labels"])
        self.assertFalse(result["new_duplicate_labels"])

    def test_every_included_file_occurs_once(self):
        self.assertEqual(len(self.files), len(set(self.files)))

    def test_inherited_fragment_tampering_is_rejected(self):
        target = audit.WORKING / "parts/v470/36_frame_typed_endpoint.tex"
        reader = Path.read_bytes

        def altered(path):
            result = reader(path)
            return result + b"X" if path == target else result

        with patch.object(Path, "read_bytes", altered):
            with self.assertRaisesRegex(ValueError, "Coverage gap|modified"):
                audit.check()

    def test_omitting_late_v4_endpoint_is_rejected(self):
        reader = Path.read_text
        target = (audit.WORKING / "parts/support-route.tex").resolve()

        def omitted(path, *args, **kwargs):
            result = reader(path, *args, **kwargs)
            return result.replace(r"\input{parts/v470/36_frame_typed_endpoint}", "") if path == target else result

        with patch.object(Path, "read_text", omitted):
            with self.assertRaisesRegex(ValueError, "Missing inherited fragment"):
                audit.check()

    def test_input_cannot_escape_the_research_tree(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            audit.expand(audit.SOURCE)

    def test_later_macro_defining_chains_keep_their_order(self):
        names = [path.stem for path in self.files]
        for left, right in zip(("29_shifted_qam", "31_op_selector_and_routes", "32_atlas_and_op_promotion", "34_mm_hc_and_c5_development"),
                               ("31_op_selector_and_routes", "32_atlas_and_op_promotion", "34_mm_hc_and_c5_development", "36_frame_typed_endpoint")):
            self.assertLess(names.index(left), names.index(right))

    def test_bibliography_is_after_all_inherited_research(self):
        names = [path.stem for path in self.files]
        self.assertGreater(names.index("28_bibliography"), names.index("36_frame_typed_endpoint"))
        self.assertLess(names.index("28_bibliography"), names.index("37_closing"))

    def test_main_contains_core_and_explicit_v4_synthesis(self):
        split = self.entry.index(r"\input{parts/v470/25_appendix_switch}")
        main = self.entry[:split]
        for fragment in ("10_sphaera_and_physics", "16_master_model", "23_physical_readouts", "current-v4-synthesis", "v480-integration"):
            self.assertIn(fragment, main)
        for fragment in ("07_qam_infrastructure", "34_mm_hc_and_c5_development"):
            self.assertNotIn(fragment, main)

    def test_premise_audit_precedes_inherited_spectral_claims(self):
        self.assertLess(self.entry.index("parts/premise-audit"), self.entry.index("parts/v470/12_structural_core"))
        for token in ("bounded self-adjoint", "nonzero orthogonal", "complement exclusion", "an identity", "empty truncated"):
            self.assertIn(token, self.text)

    def test_current_shift_not_rolled_back_to_pre_v4(self):
        current = (audit.WORKING / "parts/current-v4-synthesis.tex").read_text(encoding="utf-8")
        self.assertIn("not authorization to undo it", current)
        self.assertIn("def:v400-r05-governing-shifted-normal-form-object", current)

    def test_koide_and_local_kernel_proofs_are_visible_before_inherited_claims(self):
        self.assertLess(self.entry.index("parts/koide-and-kernel"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = (audit.WORKING / "parts/koide-and-kernel.tex").read_text(encoding="utf-8")
        for token in ("v480:koide-equal-norm", "v480:koide-hc-mixing",
                      "v480:kernel-quotient", "v480:kernel-partial-factorization",
                      "v480:kernel-routed-condition", "Explicit positive finite instance",
                      "global activation package remains unproved"):
            self.assertIn(token, source)
        self.assertNotIn(r"\newcommand{\activateZeroKernel}", source)

    def test_metric_program_keeps_units_null_and_calibration_guards(self):
        source = (audit.WORKING / "parts/v480-integration.tex").read_text(encoding="utf-8")
        for token in ("dimensionless", "unit conversion", "explicit", "calibration", "degenerate", "nondegenerate metric", "fixed norms"):
            self.assertIn(token, source)
        self.assertIn(r"g_R=\lambda_R^2 g_{\rm ref}", source)
        self.assertIn("smooth and strictly positive", source)

    def test_hc_mass_identification_keeps_native_and_ansatz_lanes_distinct(self):
        self.assertLess(self.entry.index("parts/hc-mass-identification"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = (audit.WORKING / "parts/hc-mass-identification.tex").read_text(encoding="utf-8")
        for token in ("v480:hc-mass-descent", "v480:hc-mass-odd-obstruction",
                      "v480:hc-mass-equivariant-obstruction", "v480:hc-mass-triole-bound",
                      "v480:hc-mass-fit-freedom", "real Hilbert", "additional effective ansatz",
                      "No native HC-to-lepton-root identification is established"):
            self.assertIn(token, source)
        self.assertIn("prop:spectral-to-mass-realization-map", source)
        self.assertIn("thm:three-generations", source)

    def test_working_metadata_does_not_relabel_inherited_docversion(self):
        source = (audit.WORKING / "parts/working-preamble.tex").read_text(encoding="utf-8")
        self.assertNotIn(r"\renewcommand{\docversion}", source)
        self.assertIn("Baseline v4.7.0 DOI (provenance only)", source)
        self.assertIn("unreleased", source)

    def test_generation_coupling_keeps_phase_basis_and_native_guards(self):
        self.assertLess(self.entry.index("parts/generation-coupling"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = (audit.WORKING / "parts/generation-coupling.tex").read_text(encoding="utf-8")
        for token in ("v480:generation-closed-seeds", "v480:generation-defect-gram",
                      "v480:generation-mass-spectrum", "v480:generation-cyclic-root",
                      "v480:generation-phase-chambers",
                      "v480:generation-global-phase", "v480:generation-relative-phase",
                      "v480:generation-unitary-dilation", "not an equivalent",
                      "not a recovery of the native pacer", "not yet evaluated",
                      r"\emph{not} the HC projector", "anticommutation"):
            self.assertIn(token, source)

    def test_short_contents_does_not_delete_inherited_navigation_records(self):
        source = (audit.WORKING / "parts/working-preamble.tex").read_text(encoding="utf-8")
        self.assertIn(r"\setcounter{tocdepth}{1}", source)
        self.assertEqual(self.text.count(r"\tableofcontents"), 1)
        self.assertGreaterEqual(self.text.count(r"\addcontentsline"),
                                self.raw.decode("utf-8").count(r"\addcontentsline"))

    def test_native_link_keeps_closure_spectral_and_mass_law_qualifications(self):
        self.assertLess(self.entry.index("parts/generation-coupling"),
                        self.entry.index("parts/native-operator-link"))
        self.assertLess(self.entry.index("parts/native-operator-link"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = (audit.WORKING / "parts/native-operator-link.tex").read_text(encoding="utf-8")
        source = " ".join(source.split())
        for token in ("v480:native-penalty-identity", "v480:native-closure-transfer",
                      "v480:native-isospectral-freedom", "v480:native-frame-covariance",
                      "v480:native-channel-rank", "v480:native-schur-mass",
                      "v480:native-flat-gap-mass", "not exactly $P$-closed",
                      "Hermiticity requires adjoint relations", "not supplied by the source",
                      "positive inverse root", "not an identification of a Lorentz boost"):
            self.assertIn(token, source)

    def test_aux_metric_counts_entire_document(self):
        source = "\\newlabel{boundary}{{H1}{124}{Title}{anchor}{}}\n\\gdef\\@abspage@last{1024}\n"
        with patch.object(Path, "read_text", return_value=source):
            self.assertEqual(audit.aux_pages(Path("test.aux"), "boundary"),
                             {"total": 1024, "main_and_frontmatter": 123,
                              "appendices_and_bibliography": 901})

    def test_evaluated_coupling_candidate_keeps_scale_and_fit_boundaries(self):
        self.assertLess(self.entry.index("parts/native-operator-link"),
                        self.entry.index("parts/coupling-scale-candidate"))
        self.assertLess(self.entry.index("parts/coupling-scale-candidate"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = " ".join((audit.WORKING / "parts/coupling-scale-candidate.tex").read_text(encoding="utf-8").split())
        for token in ("v480:coupling-scale-freedom", "v480:coupling-two-harmonic-bound",
                      "v480:coupling-gap-ratio-obstruction", "not predictions",
                      "not a parameter-free", "not a valid interpolation",
                      "No measured lepton mass enters", "single-frame Planck reference"):
            self.assertIn(token, source)

    def test_matrix_planck_diagnosis_keeps_fits_and_direct_block_scope_explicit(self):
        source = " ".join((audit.WORKING / "parts/coupling-scale-candidate.tex").read_text(encoding="utf-8").split())
        for token in ("v480:matrix-phase-sensitivity", "v480:planck-nonflat-fit-freedom",
                      "v480:planck-direct-block-bound", "post-hoc diagnostics",
                      "not an assigned experimental uncertainty", "not a unit correction",
                      "not a new fundamental Planck length", "an additional choice",
                      "exact fitted counterexample", "does not uniquely identify a physical cause"):
            self.assertIn(token, source)

    def test_missing_aux_boundary_is_not_guessed(self):
        with patch.object(Path, "read_text", return_value="\\gdef\\@abspage@last{1024}\n"):
            with self.assertRaisesRegex(ValueError, "Missing settled page"):
                audit.aux_pages(Path("test.aux"), "boundary")

    def test_tensor_shift_extension_keeps_covariance_and_physical_fit_distinct(self):
        self.assertLess(self.entry.index("parts/coupling-scale-candidate"),
                        self.entry.index("parts/tensor-shift-coupling"))
        self.assertLess(self.entry.index("parts/tensor-shift-coupling"),
                        self.entry.index("parts/v470/10_sphaera_and_physics"))
        source = " ".join((audit.WORKING / "parts/tensor-shift-coupling.tex").read_text(encoding="utf-8").split())
        for token in ("v480:tensor-generalized-spectrum", "v480:tensor-chart-covariance",
                      "v480:tensor-comparison-fit-freedom", "v480:tensor-metric-scale-bound",
                      "v480:tensor-identity-extension", "post-hoc metric fit",
                      "not merely metric condition numbers", "not a native metric extraction",
                      "def:v400-r01-shifted-tensor-payload-migration",
                      "def:v400-r05-governing-shifted-normal-form-object"):
            self.assertIn(token, source)

    def test_mismatched_published_baseline_cannot_be_accepted(self):
        def include(path, files):
            files.append(Path("included.tex"))
            return ""

        with patch.object(audit, "check", return_value={}), \
             patch.object(audit, "expand", side_effect=include), \
             patch.object(Path, "stat", return_value=SimpleNamespace(st_mtime=0)), \
             patch.object(Path, "read_text", return_value=""), \
             patch.object(audit, "aux_pages", side_effect=[{"total": 1013}, {"total": 1008}]):
            with self.assertRaisesRegex(ValueError, "does not match"):
                audit.measure(Path("before.aux"), Path("after.aux"), Path("never-written.json"))
