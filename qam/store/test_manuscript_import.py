from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select

from qam.store.manuscript_import import import_manuscript, overview_from_snapshot
from qam.store.orm import store_session
from qam.store.snapshots import create_snapshot, read_snapshot
from qam.tools.manuscript_inventory import collect


class ManuscriptImportTests(unittest.TestCase):
    def test_literal_import_idempotence_and_versions(self):
        with TemporaryDirectory() as folder:
            repo = Path(folder)
            parts = repo / 'sources/research/parts'
            parts.mkdir(parents=True)
            entry = parts.parent / 'v480-companion.tex'
            entry.write_text(r'\input{parts/koide}' + '\n', encoding='utf-8')
            source = parts / 'koide.tex'
            source.write_text('% \\begin{theorem}Comment only\\end{theorem}\n'
                '\\begin{definition}[Root]\\label{def:root}\nOriginal % kept comment\n\\end{definition}\n'
                '\\begin{proposition}[Koide example]\\label{prop:example}Value one.\\end{proposition}\n', encoding='utf-8')
            db = repo / 'store.sqlite3'
            first = import_manuscript(db, repo)
            self.assertEqual(first['files'], 2)
            self.assertEqual(first['statements'], 2)
            self.assertEqual(first['topics']['mass']['count'], 2)
            snapshot = create_snapshot(db, 'first')['snapshot_hash']
            frozen = read_snapshot(db, snapshot)
            view = overview_from_snapshot(db, snapshot, first['root_version'])
            self.assertIn('2 Aussageumgebungen aus 2', view)
            self.assertIn('sources/research/parts/koide.tex', view)
            with store_session(db) as (session, models):
                before = session.scalar(select(func.count()).select_from(models.qstore_ledger))
                rows = list(session.scalars(select(models.qstore_versions)))
                self.assertTrue(any('% kept comment' in row.payload_json for row in rows))
            repeated = import_manuscript(db, repo)
            self.assertFalse(any(repeated['new_rows'].values()))
            with store_session(db) as (session, models):
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_ledger)), before)
            source.write_text(source.read_text(encoding='utf-8').replace('Value one.', 'Value two.'), encoding='utf-8')
            changed = import_manuscript(db, repo)
            self.assertNotEqual(changed['root_version'], first['root_version'])
            self.assertEqual(read_snapshot(db, snapshot), frozen)
            self.assertEqual(overview_from_snapshot(db, snapshot, first['root_version']), view)
            with store_session(db) as (session, models):
                obj = session.get(models.qstore_objects, 'manuscript:sources/research/parts/koide.tex:label:prop:example')
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_versions).where(
                    models.qstore_versions.object_id == obj.object_id)), 2)
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_guards)), 4)
            entry.write_text(r'\input{missing}', encoding='utf-8')
            with self.assertRaises(ValueError):
                import_manuscript(db, repo)

    def test_nested_environment_preserves_full_source(self):
        with TemporaryDirectory() as folder:
            repo = Path(folder)
            source = repo / 'sources/research/v480-companion.tex'
            source.parent.mkdir(parents=True)
            text = r'\begin{definition}Outer \begin{definition}Inner\end{definition} tail\end{definition}'
            source.write_text(text, encoding='utf-8')
            statements = [row for row in collect(repo) if row[2] != 'file']
            self.assertEqual(len(statements), 2)
            self.assertEqual(statements[0][5], text)


if __name__ == '__main__':
    unittest.main()
