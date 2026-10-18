import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.qsc_audit import metadata_hygiene_audit as audit


class UndefinedMarkerTests(unittest.TestCase):
    def errors(self, text, suffix=".md"):
        path = audit.ROOT / ("notes" + suffix)
        with patch.object(Path, "read_text", return_value=text):
            return [f for f in audit.scan_file(path, None) if f.severity == "error"]

    def test_zero_count_summary_is_not_an_unresolved_reference(self):
        self.assertEqual(self.errors("- Visible `??` / `[?]`: 0 / 0 according to r93 audit\n"), [])

    def test_nonzero_count_still_blocks(self):
        self.assertTrue(self.errors("- Visible `??` / `[?]`: 1 / 0 according to r93 audit\n"))

    def test_real_reference_on_next_line_retains_line_number(self):
        findings = self.errors("- Visible `??` / `[?]`: 0 / 0 according to r93 audit\nSee Theorem ??\n")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].line, 2)

    def test_inline_and_trailing_markers_still_block(self):
        self.assertTrue(self.errors("See `??` for the result.\n"))
        self.assertTrue(self.errors("- Visible `??` / `[?]`: 0 / 0; see Section ??\n"))

    def test_tex_is_not_exempted(self):
        self.assertTrue(self.errors("- Visible `??` / `[?]`: 0 / 0\n", ".tex"))

    def test_generated_audits_are_not_scanned(self):
        self.assertFalse(audit.is_scannable(Path("audits/v4.8.0/report.md")))


if __name__ == "__main__":
    unittest.main()
