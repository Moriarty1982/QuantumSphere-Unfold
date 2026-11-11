import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy.exc import IntegrityError

from qam.store.orm import store_session
from qam.store.papers import save_paper, read_paper, export_paper
from qam.store.snapshots import create_snapshot
from qam.tools.store_example import run


class PaperTests(unittest.TestCase):
    def test_pinned_revisions_exports_and_predecessors(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            example = run(db)
            snapshot = create_snapshot(db, 'paper-test')['snapshot_hash']
            request = {'paper_id': 'matrix-note', 'title': 'Matrix comparison',
                       'snapshot_hash': snapshot, 'profile': 'research-draft', 'previous': None,
                       'roots': [example['seeds']['projector'], example['seeds']['commuting-transport']]}
            first = save_paper(db, request)['paper_hash']
            self.assertEqual(save_paper(db, request)['paper_hash'], first)
            frozen = read_paper(db, first)
            export_paper(db, first, root / 'first')
            revised = save_paper(db, {**request, 'title': 'Revised title', 'previous': first})['paper_hash']
            self.assertNotEqual(first, revised)
            self.assertEqual(read_paper(db, first), frozen)
            export_paper(db, first, root / 'repeat')
            self.assertEqual((root / 'first/paper.tex').read_bytes(), (root / 'repeat/paper.tex').read_bytes())
            self.assertEqual((root / 'first/manifest.json').read_bytes(), (root / 'repeat/manifest.json').read_bytes())
            manifest = json.loads((root / 'first/manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(manifest['paper']['paper_hash'], first)
            self.assertIn('Matrix comparison', (root / 'first/paper.tex').read_text(encoding='utf-8'))
            with self.assertRaisesRegex(ValueError, 'stale'):
                save_paper(db, {**request, 'title': 'Competing title', 'previous': first})
            with self.assertRaises(ValueError):
                save_paper(db, {**request, 'profile': 'publication-ready'})
            with self.assertRaises(IntegrityError):
                with store_session(db) as (session, models):
                    session.delete(session.get(models.qstore_papers, first))


if __name__ == '__main__':
    unittest.main()
