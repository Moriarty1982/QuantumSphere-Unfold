from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select

from qam.store.koide_review import apply_review, SOURCE
from qam.store.manuscript_import import import_manuscript
from qam.store.orm import store_session
from qam.store.registry import latest_review
from qam.store.selection import select_versions
from qam.tools.store_koide_branch import run


class KoideReviewTests(unittest.TestCase):
    def test_documentary_matching_proof_reviews_and_remaining_guards(self):
        repo = Path(__file__).resolve().parents[2]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            run(db, root / 'initial')
            import_manuscript(db, repo)
            result = apply_review(db, repo)
            self.assertEqual(len(result['pairs']), 4)
            self.assertEqual(len(result['definitions']), 3)
            self.assertEqual(len(result['native_guards']), 4)
            selected = select_versions(db, result['snapshot_hash'], result['roots'])
            proof_edges = [row for row in selected['relations'] if row['relation_type'] == 'proves']
            self.assertEqual(len(proof_edges), 4)
            self.assertTrue(all(row['effective_status'] == 'reviewed' for row in proof_edges))
            self.assertEqual(sum(row['kind'] == 'guard' for row in selected['findings']), 6)
            with store_session(db) as (session, models):
                before = session.scalar(select(func.count()).select_from(models.qstore_ledger))
                for pair in result['pairs']:
                    guards = list(session.scalars(select(models.qstore_guards).where(
                        models.qstore_guards.subject_version == pair['imported'])))
                    self.assertTrue(guards)
                    for guard in guards:
                        self.assertEqual(latest_review(session, models, 'guard', guard.guard_hash).status, 'satisfied')
            self.assertEqual(apply_review(db, repo), result)
            with store_session(db) as (session, models):
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_ledger)), before)

    def test_changed_source_prevents_applying_review(self):
        with TemporaryDirectory() as folder:
            repo = Path(folder)
            source = repo / SOURCE
            source.parent.mkdir(parents=True)
            source.write_text('Changed source', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Source changed'):
                apply_review(repo / 'store.sqlite3', repo)
            self.assertFalse((repo / 'store.sqlite3').exists())


if __name__ == '__main__':
    unittest.main()
