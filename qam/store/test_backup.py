from contextlib import closing
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

from qam.store.backup import create_backup, check_backup, restore_backup
from qam.store.papers import save_paper, read_paper, export_paper
from qam.store.snapshots import create_snapshot
from qam.tools.store_example import run


class BackupTests(unittest.TestCase):
    def test_full_database_restore_and_identical_export(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            example = run(db)
            snapshot = create_snapshot(db, 'backup-test')['snapshot_hash']
            paper = save_paper(db, {'paper_id': 'backup-note', 'title': 'Backup comparison',
                'snapshot_hash': snapshot, 'roots': [example['seeds']['projector']],
                'profile': 'research-draft', 'previous': None})['paper_hash']
            export_paper(db, paper, root / 'before')
            with closing(sqlite3.connect(db)) as live:
                live.execute('PRAGMA journal_mode=WAL')
                live.execute('CREATE TABLE legacy_receipts(value TEXT)')
                live.execute("INSERT INTO legacy_receipts VALUES ('kept from WAL')")
                live.commit()
                create_backup(db, root / 'backup')
            manifest = check_backup(root / 'backup')
            self.assertEqual(manifest['table_rows']['legacy_receipts'], 1)
            restored = root / 'restored.sqlite3'
            restore_backup(root / 'backup', restored)
            self.assertEqual(read_paper(restored, paper), read_paper(db, paper))
            export_paper(restored, paper, root / 'after')
            self.assertEqual((root / 'before/paper.tex').read_bytes(), (root / 'after/paper.tex').read_bytes())
            self.assertEqual((root / 'before/manifest.json').read_bytes(), (root / 'after/manifest.json').read_bytes())
            with closing(sqlite3.connect(restored)) as connection:
                self.assertEqual(connection.execute('SELECT value FROM legacy_receipts').fetchone()[0], 'kept from WAL')
            with self.assertRaises(FileExistsError):
                restore_backup(root / 'backup', restored)
            with self.assertRaises(FileExistsError):
                create_backup(db, root / 'backup')
            backup_file = root / 'backup/qam.sqlite3'
            backup_file.write_bytes(backup_file.read_bytes() + b'corruption')
            with self.assertRaises(ValueError):
                restore_backup(root / 'backup', root / 'invalid.sqlite3')
            self.assertFalse((root / 'invalid.sqlite3').exists())


if __name__ == '__main__':
    unittest.main()
