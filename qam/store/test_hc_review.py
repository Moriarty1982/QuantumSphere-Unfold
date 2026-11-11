from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from qam.store.hc_identification_review import apply_review, SOURCE
from qam.store.manuscript_import import import_manuscript
from qam.store.selection import select_versions
from qam.store.scrub import scrub


class HCReviewTests(unittest.TestCase):
    def test_source_matching_idempotence_and_open_physical_guards(self):
        repo = Path(__file__).resolve().parents[2]
        with TemporaryDirectory() as folder:
            db = Path(folder) / 'store.sqlite3'
            import_manuscript(db, repo)
            result = apply_review(db, repo)
            self.assertEqual(result, apply_review(db, repo))
            selection = select_versions(db, result['snapshot_hash'], result['roots'])
            self.assertEqual(len(result['pairs']), 5)
            self.assertEqual(len(result['native_guards']), 4)
            self.assertEqual(sum(row['relation_type'] == 'proves' and row['effective_status'] == 'reviewed'
                                 for row in selection['relations']), 5)
            self.assertFalse(any(row['kind'] == 'declared-dependency' for row in selection['findings']))
            self.assertEqual(scrub(selection)['result'], 'passed')

    def test_changed_source_blocks_review_before_creating_database(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / SOURCE
            source.parent.mkdir(parents=True)
            source.write_text('changed', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Source changed'):
                apply_review(root / 'store.sqlite3', root)
            self.assertFalse((root / 'store.sqlite3').exists())
