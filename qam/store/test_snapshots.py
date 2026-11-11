import json
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import unittest

from sqlalchemy.exc import IntegrityError

from qam.store.orm import store_session
from qam.store.snapshots import create_snapshot, read_snapshot
from qam.tools.store_example import run


class SnapshotTests(unittest.TestCase):
    def test_repeatability_history_and_cli(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / 'store.sqlite3'
            run(path)
            first = create_snapshot(path, 'comparison')
            self.assertEqual(first['counts']['qstore_versions'], 4)
            self.assertEqual(first['counts']['qstore_checks'], 2)
            self.assertEqual(create_snapshot(path, 'comparison'), first)
            saved = read_snapshot(path, first['snapshot_hash'])
            with store_session(path) as (session, models):
                session.add(models.qstore_objects(object_id='later-object', object_type='topic'))
                session.add(models.qstore_ledger(event_type='test-change', payload_json='{}'))
            second = create_snapshot(path, 'comparison')
            self.assertNotEqual(first['snapshot_hash'], second['snapshot_hash'])
            self.assertEqual(read_snapshot(path, first['snapshot_hash']), saved)
            command = [sys.executable, '-m', 'qam.tools.store_db', 'snapshot-read',
                       '--db', str(path), '--hash', first['snapshot_hash']]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout), saved)
            with self.assertRaises(IntegrityError):
                with store_session(path) as (session, models):
                    session.delete(session.get(models.qstore_snapshots, first['snapshot_hash']))


if __name__ == '__main__':
    unittest.main()
