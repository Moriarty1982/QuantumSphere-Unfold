"""Check literal include/label routing for the whole-paper reading route.

This checks document structure, not TeX semantics or mathematical validity.
The compiler remains the authority for processing the full document.
"""

from collections import Counter
from pathlib import Path
import re
import unittest


SOURCES = Path(__file__).resolve().parents[3] / "sources"
INFRASTRUCTURE = "parts/01_qam_mml_mma_pre_v4_infrastructure"
INFRASTRUCTURE_MODULES = (
    "01_working_orientation_and_public_shape",
    "02_store_array_and_pre_v4_readouts",
    "03_two_sided_tensor_masks_and_freeze",
    "04_qam_predicates_transport_shell",
    "05_qam_tensor_admissibility_translation",
)
DETAILS = SOURCES / "parts/09_structural_tools_appendices/06_core_proof_details.tex"


def active_files(path, ancestors=()):
    """Follow the project's literal, line-start input declarations."""
    if path in ancestors:
        raise AssertionError(f"Cyclic TeX input: {path}")
    result = [path]
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"(?m)^[ \t]*\\input\{([^{}\n]+)\}", text):
        child = SOURCES / target
        if not child.suffix:
            child = child.with_suffix(".tex")
        result.extend(active_files(child, (*ancestors, path)))
    return result


class ReadingRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = active_files(SOURCES / "active-core.tex")
        cls.text = "\n".join(path.read_text(encoding="utf-8") for path in cls.files)
        cls.labels = Counter(re.findall(r"\\label\{([^{}]+)\}", cls.text))

    def test_infrastructure_is_loaded_once_after_appendix_boundary(self):
        counts = Counter(self.files)
        appendix_boundary = SOURCES / "parts/09_structural_tools_appendices.tex"
        boundary = self.files.index(appendix_boundary)
        self.assertIn("\\appendix", appendix_boundary.read_text(encoding="utf-8"))
        for name in INFRASTRUCTURE_MODULES:
            path = SOURCES / INFRASTRUCTURE / f"{name}.tex"
            self.assertEqual(counts[path], 1)
            self.assertGreater(self.files.index(path), boundary)
        compact = (SOURCES / f"{INFRASTRUCTURE}.tex").read_text(encoding="utf-8")
        self.assertNotIn("\\input{", compact)

    def test_new_appendix_targets_resolve_uniquely(self):
        targets = (
            "sec:compact-qam-interface", "app:core-proof-details",
            "app:hc-spectral-proof", "app:hc-spectral-counterexamples",
            "app:fixed-exponent-proof", "app:inverse-exponent-check",
            "app:verification-ledger", "app:qam-runtime-details",
            "rem:op5-reading-contract",
            "app:historical-tool-memory", "app:legacy-synthesis",
            "app:local-crystal-protocol", "app:hc-transport-protocols",
            "app:status-genealogy", "app:phase-iv-unfolding",
            "app:local-op-entry", "app:op-transport-unfolding",
            "app:split-refold-memory", "app:computational-protocols",
        )
        for target in targets:
            self.assertEqual(self.labels[target], 1, target)
            references = self.text.count(f"\\ref{{{target}}}")+self.text.count(f"\\hyperref[{target}]")
            self.assertGreater(references, 0, target)

    def test_original_definition_and_theorem_labels_are_preserved_once(self):
        for target in (
            "def:qam-store-state", "def:mml-store-instructions", "def:mma-store-transition",
            "lem:diagonal-traversal-scalar-action", "thm:hc-spectral-projector",
            "thm:self-consistent-gL", "eq:SC1", "eq:SC2", "prop:exponent-5", "rem:exact-sc",
        ):
            self.assertEqual(self.labels[target], 1, target)

    def test_main_spectral_hypotheses_are_not_moved_out_of_sight(self):
        source = (SOURCES / "parts/04_closure_projection_and_structural_core.tex").read_text(encoding="utf-8")
        statement = source.split("\\label{thm:hc-spectral-projector}", 1)[1].split("\\end{theorem}", 1)[0]
        for required in ("bounded", "orthogonal", "commuting", "single-eigenvalue", "\\ker(C)"):
            self.assertIn(required, statement)
        self.assertIn("\\ref{app:hc-spectral-proof}", source)
        self.assertIn("\\ref{app:hc-spectral-counterexamples}", source)

    def test_main_ansatz_and_identity_remain_explicit(self):
        source = (SOURCES / "parts/07_open_questions_and_op_transport/02_op1_op2_tribonacci_teichmueller.tex").read_text(encoding="utf-8")
        statement = source.split("\\label{thm:self-consistent-gL}", 1)[1].split("\\end{theorem}", 1)[0]
        for required in ("model ansatz", "exponent $5$", "27/20", "\\label{eq:SC1}", "\\label{eq:SC2}"):
            self.assertIn(required, statement)
        identity = source.split("\\label{rem:exact-sc}", 1)[1].split("\\end{remark}", 1)[0]
        self.assertIn("imposes no new constraint", identity)
        self.assertIn("=A(g,\\beta)", identity)

    def test_appendix_has_full_arguments_and_executed_check_paths(self):
        source = DETAILS.read_text(encoding="utf-8")
        self.assertIn("Proof of Theorem~\\ref{thm:hc-spectral-projector}", source)
        self.assertIn("Proof of Theorem~\\ref{thm:self-consistent-gL}", source)
        self.assertIn("(t+3)", source)
        self.assertIn("(I-C)x", source)
        self.assertIn("test_spectral_and_exponent_contracts.py", source)
        self.assertIn("analysis/OP5_Relay_C5_Check.py", source)
        self.assertNotIn("\\mathrm{GRCite}", source)

    def test_every_active_file_is_included_exactly_once(self):
        self.assertEqual(len(self.files), len(set(self.files)))

    def test_single_appendix_switch_precedes_relocated_support(self):
        self.assertEqual(self.text.count("\\appendix"), 1)
        boundary = self.files.index(SOURCES / "parts/09_structural_tools_appendices.tex")
        for path in self.files:
            if ("reading_details" in path.parts
                    or path.parent.name == "08_computational_and_pre_op_foundation"
                    or path.name == "06_hs_split_refold_xor_register_memory.tex"):
                self.assertGreater(self.files.index(path), boundary)

    def test_main_transport_keeps_conditional_statement(self):
        source = (SOURCES / "parts/07_open_questions_and_op_transport/03_inflow_and_op_transport_architecture.tex").read_text(encoding="utf-8")
        statement = source.split("\\label{thm:compressed-op-branch-shell}", 1)[1].split("\\end{theorem}", 1)[0]
        for required in ("HC-confined", "two-pass", "class-admissible", "linear"):
            self.assertIn(required, statement)
        self.assertIn("not an unconditional", source)

    def test_core_physics_and_master_model_remain_in_main_text(self):
        boundary = self.files.index(SOURCES / "parts/09_structural_tools_appendices.tex")
        for name in ("03_core_sphaera_and_physics_baseline", "06_master_equation_matter_mm_hc"):
            self.assertLess(self.files.index(SOURCES / f"parts/{name}.tex"), boundary)


if __name__ == "__main__":
    unittest.main()
