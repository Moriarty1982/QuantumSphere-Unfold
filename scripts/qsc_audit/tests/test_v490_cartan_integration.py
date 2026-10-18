"""Main-text inclusion and claim boundaries of the v4.9 research candidate."""
from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "sources/research"


class CartanMainIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (WORK / "v480-companion.tex").read_text(encoding="utf-8")
        cls.raw = (WORK / "parts/cartan-normal-source.tex").read_text(encoding="utf-8")
        cls.text = " ".join(cls.raw.split())

    def test_main_inclusion_is_unique_and_precedes_inherited_claims(self):
        token = r"\input{parts/cartan-normal-source}"
        self.assertEqual(self.entry.count(token), 1)
        self.assertLess(self.entry.index("parts/hc-dynamics-and-geometry"), self.entry.index(token))
        self.assertLess(self.entry.index(token), self.entry.index("parts/v470/10_sphaera_and_physics"))

    def test_working_version_does_not_relabel_public_release(self):
        preamble = (WORK / "parts/working-preamble.tex").read_text(encoding="utf-8")
        self.assertIn(r"\newcommand{\workingversion}{4.9.0-draft}", preamble)
        self.assertNotIn(r"\renewcommand{\docversion}", preamble)
        self.assertIn('version: "v4.8.0"', (ROOT / "CITATION.cff").read_text(encoding="utf-8"))

    def test_three_conditional_propositions_have_proofs(self):
        self.assertEqual(self.raw.count(r"\begin{proposition}"), 3)
        self.assertEqual(self.raw.count(r"\begin{proof}"), 3)
        for label in ("subsidiary", "normal-inverse", "source-law-theorem"):
            self.assertIn(r"\label{v490:"+label+"}", self.raw)
        self.assertNotIn("GRCite", self.raw)

    def test_comparison_action_keeps_fields_and_sources(self):
        for token in ("commuting", "multiplier density", "weight one",
                      "not an identification", "independent coframe",
                      "compatible", "not generally the Levi--Civita curvature"):
            self.assertIn(token, self.text)
        self.assertIn(r"0.6&0&4\\0&0.6&0.7\\4&0.7&0.6", self.raw)
        self.assertIn(r"-F^a{}_{\mu}\delta\lambda_a{}^\mu", self.raw)

    def test_source_law_requires_compatibility_and_keeps_higher_kernel(self):
        for token in (r"(I-JJ^+)b(d)=0", r"k\in\ker A_f", "464", "736",
                      "not silently", "not an added law", "at least two"):
            self.assertIn(token, self.text)

    def test_saved_numerical_evidence_matches_gate_and_mask(self):
        report = json.loads((ROOT / "analysis/HC_Cartan_Normal_Source_Compatibility.json")
                            .read_text(encoding="utf-8"))
        self.assertEqual(report["higher_rank"], 332)
        self.assertEqual(report["remaining_source_gate_rank"], 0)
        fixed = report["frozen_block_controls"]["tangential_Cauchy_jet_fixed"]
        self.assertEqual(fixed["higher_rank"], 200)
        self.assertEqual(fixed["gate_rank"], 6)
        self.assertEqual(fixed["allowed_higher_coordinates"], 464)
        self.assertIn("98.96", self.text)
        self.assertGreater(report["later_frozen_highest_control"]["all_1114_norm"], 90)

    def test_regional_and_native_limits_are_explicit(self):
        for token in ("open region", "no incoming", "does not propagate",
                      "not a nonexistence proof", "derivatives",
                      "No regional existence", "OP5 closure", "physical scale"):
            self.assertIn(token, self.text)

    def test_reading_route_and_acceptance_gates_reference_new_section(self):
        for name in ("working-orientation.tex", "current-v4-synthesis.tex", "v480-integration.tex"):
            source = (WORK / "parts" / name).read_text(encoding="utf-8")
            self.assertIn("v490:cartan-source", source)


if __name__ == "__main__":
    unittest.main()
