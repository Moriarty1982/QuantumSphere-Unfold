from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select
from qam.store.hc_koide_bridge import apply_review
from qam.store.hc_identification_review import apply_review as review_hc
from qam.store.koide_review import apply_review as review_koide, SOURCE as KOIDE_SOURCE
from qam.store.manuscript_import import import_manuscript
from qam.store.orm import store_session
from qam.store.scrub import scrub
from qam.store.selection import select_versions
from qam.tools.store_koide_branch import run as store_koide
from qam.store.hc_identification_review import SOURCE as HC_SOURCE


class BridgeTests(unittest.TestCase):
    def test_transitive_proofs_open_guards_and_idempotence(self):
        repo = Path(__file__).resolve().parents[2]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            import_manuscript(db, repo)
            store_koide(db, root / 'koide')
            review_koide(db, repo)
            review_hc(db, repo)
            result = apply_review(db, repo)
            selected = select_versions(db, result['snapshot_hash'], result['roots'])
            self.assertTrue(set(result['prerequisites']).issubset(
                {v['version_hash'] for v in selected['objects']}))
            self.assertEqual(scrub(selected)['result'], 'passed')
            self.assertEqual(sum(f['kind'] == 'frame-bridge-required' for f in selected['findings']), 1)
            guard_keys = {f['hash'] for f in selected['findings'] if f['kind'] == 'guard'}
            self.assertTrue(set(result['guards']).issubset(guard_keys))
            with store_session(db) as (session, models):
                before = session.scalar(select(func.count()).select_from(models.qstore_ledger))
            self.assertEqual(apply_review(db, repo), result)
            with store_session(db) as (session, models):
                self.assertEqual(before, session.scalar(select(func.count()).select_from(models.qstore_ledger)))

    def test_both_source_pins_fail_before_database_creation(self):
        repo = Path(__file__).resolve().parents[2]
        for changed in (HC_SOURCE, KOIDE_SOURCE):
            with self.subTest(source=changed), TemporaryDirectory() as folder:
                root = Path(folder)
                for name in (HC_SOURCE, KOIDE_SOURCE):
                    target = root / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes((repo / name).read_bytes())
                (root / changed).write_text('changed', encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'Source changed'):
                    apply_review(root / 'store.sqlite3', root)
                self.assertFalse((root / 'store.sqlite3').exists())
