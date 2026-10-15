"""The length audit checks source preservation, not mathematical correctness."""
import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "reading_length_audit.py"
SPEC = importlib.util.spec_from_file_location("reading_length_audit", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def record(labels=None, blocks=None):
    return {"labels": labels or {}, "protected_environments_and_displays": blocks or {}, "pages": {}}


class ReadingLengthAuditTests(unittest.TestCase):
    def test_comment_removal_preserves_escaped_percent(self):
        self.assertEqual(audit.uncomment("a% comment\nb\\%c"), "a\nb\\%c")

    def test_whitespace_changes_do_not_change_protected_hashes(self):
        left = r"\begin{theorem} x=1 \end{theorem}"
        right = "\\begin{theorem}\n x=1\n\\end{theorem}"
        self.assertEqual(audit.environment_hashes(left), audit.environment_hashes(right))

    def test_changed_hypothesis_is_not_hidden_by_preserved_label(self):
        left = audit.environment_hashes(r"\begin{theorem}\label{t}Assume A.\end{theorem}")
        right = audit.environment_hashes(r"\begin{theorem}\label{t}Assume B.\end{theorem}")
        result = audit.compare(record({"t": 1}, left), record({"t": 1}, right))
        self.assertFalse(result["missing_labels"])
        self.assertTrue(result["missing_protected_content"])

    def test_standalone_display_is_protected(self):
        self.assertNotEqual(audit.environment_hashes(r"\[x=1\]"), audit.environment_hashes(r"\[x=2\]"))

    def test_nested_environment_mismatch_is_rejected(self):
        with self.assertRaises(ValueError):
            audit.environment_hashes(r"\begin{theorem}\begin{align}x=1\end{theorem}")

    def test_new_duplicate_label_is_rejected(self):
        result = audit.compare(record({"t": 1}), record({"t": 2}))
        self.assertEqual(result["new_duplicate_labels"], {"t": 2})

    def test_preserved_existing_duplicate_is_not_new(self):
        result = audit.compare(record({"t": 2}), record({"t": 2}))
        self.assertFalse(result["new_duplicate_labels"])

    def test_deleted_repeated_block_is_detected(self):
        result = audit.compare(record(blocks={"proof:hash": 2}), record(blocks={"proof:hash": 1}))
        self.assertEqual(result["missing_protected_content"], {"proof:hash": 1})
