import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError

from qam.store.editions import save_edition, read_edition, export_edition
from qam.store.orm import store_session
from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.tools.store_example import run
from qam.tools.configure_v5_editions import configure


class EditionTests(unittest.TestCase):
    def test_ordered_membership_revisions_guards_and_immutable_index(self):
        repo = Path(__file__).resolve().parents[2]
        source = 'qam/store/matrix_example.json'
        source_hash = hashlib.sha256((repo / source).read_bytes()).hexdigest()
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            example = run(db)
            candidate = register(db, repo, {'object_id': 'unreviewed-candidate', 'kind': 'definition',
                'frame': 'unspecified', 'status': 'imported-unreviewed',
                'source': {'path': source, 'sha256': source_hash, 'revision': 'test', 'locator': 'candidate'},
                'payload': {'title': 'Candidate only', 'body': 'RAW-CANDIDATE-BODY', 'scope': 'pending', 'assumptions': []}})['version_hash']
            snapshot = create_snapshot(db, 'edition-test')['snapshot_hash']
            request = {'edition_id': 'test-physics', 'title': 'Physics test', 'mode': 'selected-arguments',
                'snapshot_hash': snapshot, 'previous': None, 'entrypoint': None, 'source_files': {source: source_hash},
                'sections': [{'key': 'method', 'title': 'Method', 'members': [
                    {'version': example['seeds']['projector'], 'use': 'argument'},
                    {'version': example['seeds']['commuting-transport'], 'use': 'argument'}]},
                    {'key': 'future', 'title': 'Future', 'members': [{'version': candidate, 'use': 'candidate'}]}]}
            key = save_edition(db, repo, request)['edition_hash']
            self.assertEqual(save_edition(db, repo, request)['edition_hash'], key)
            self.assertEqual(create_snapshot(db, 'edition-test')['snapshot_hash'], snapshot)
            export_edition(db, repo, key, root / 'export')
            tex = (root / 'export/paper.tex').read_text(encoding='utf-8')
            self.assertIn('pending review', tex)
            self.assertNotIn('RAW-CANDIDATE-BODY', tex)
            self.assertLess(tex.index(r'\section{Method}'), tex.index(r'\section{Future}'))
            self.assertIn('passed', tex)
            revised = save_edition(db, repo, {**request, 'title': 'Revised', 'previous': key})['edition_hash']
            self.assertNotEqual(revised, key)
            self.assertEqual(read_edition(db, key)['title'], 'Physics test')
            with self.assertRaisesRegex(ValueError, 'stale'):
                save_edition(db, repo, {**request, 'title': 'Stale revision'})
            with self.assertRaises(IntegrityError):
                with store_session(db) as (session, models):
                    session.get(models.qstore_edition_sections, (key, 0)).title = 'Changed'
            bad = {**request, 'edition_id': 'unsafe', 'sections': [{'key': 'raw', 'title': 'Raw',
                'members': [{'version': candidate, 'use': 'argument'}]}]}
            with self.assertRaisesRegex(ValueError, 'candidates'):
                save_edition(db, repo, bad)

    def test_full_source_export_and_freshness_preflight(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            repo = root / 'repo'
            repo.mkdir()
            (repo / 'paper.tex').write_text(r'\documentclass{article}\begin{document}test\end{document}', encoding='utf-8')
            source_hash = hashlib.sha256((repo / 'paper.tex').read_bytes()).hexdigest()
            db = root / 'store.sqlite3'
            snapshot = create_snapshot(db, 'empty-source')['snapshot_hash']
            request = {'edition_id': 'full', 'title': 'Full', 'mode': 'manuscript-source', 'snapshot_hash': snapshot,
                'previous': None, 'entrypoint': 'paper.tex', 'source_files': {'paper.tex': source_hash},
                'sections': [{'key': 'all', 'title': 'Whole source', 'members': []}]}
            key = save_edition(db, repo, request)['edition_hash']
            export_edition(db, repo, key, root / 'export')
            self.assertEqual((root / 'export/source/paper.tex').read_bytes(), (repo / 'paper.tex').read_bytes())
            (repo / 'paper.tex').write_text('changed', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'source changed'):
                export_edition(db, repo, key, root / 'blocked')
            self.assertFalse((root / 'blocked').exists())

    def test_actual_two_editions_and_repeat_without_new_versions(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            first = configure(db, root / 'first')
            with store_session(db) as (session, models):
                count = session.scalar(select(func.count()).select_from(models.qstore_editions))
            second = configure(db, root / 'second')
            self.assertEqual((first['physics'], first['full']), (second['physics'], second['full']))
            self.assertEqual(first['physics_sections'], 7)
            self.assertEqual(first['full_statements'], 2468)
            self.assertEqual(len(read_edition(db, first['full'])['sections']), 61)
            with store_session(db) as (session, models):
                self.assertEqual(count, session.scalar(select(func.count()).select_from(models.qstore_editions)))
            manifest = json.loads((root / 'first/physics/assembly.json').read_text(encoding='utf-8'))
            self.assertTrue(manifest['incomplete_argument_review'])
            self.assertTrue(all(s['technical_check']['result'] == 'passed' for s in manifest['sections_state']))
            self.assertEqual((root / 'first/physics/paper.tex').read_bytes(), (root / 'second/physics/paper.tex').read_bytes())
