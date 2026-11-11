import copy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.integrity import inspect_snapshot
from qam.store.snapshots import create_snapshot, read_snapshot
from qam.tools.store_example import run


class IntegrityTests(unittest.TestCase):
    def test_internal_corruption_and_dangling_links(self):
        with TemporaryDirectory() as folder:
            db = Path(folder) / 'store.sqlite3'
            run(db)
            key = create_snapshot(db, 'integrity')['snapshot_hash']
            original = read_snapshot(db, key)
            self.assertEqual(inspect_snapshot(original)['result'], 'passed')
            altered = copy.deepcopy(original)
            altered['tables']['qstore_versions'][0]['payload_json'] = '{}'
            self.assertEqual(inspect_snapshot(altered)['result'], 'blocked')
            altered = copy.deepcopy(original)
            altered['tables']['qstore_relations'][0]['target_version'] = 'missing'
            issues = inspect_snapshot(altered)['issues']
            self.assertTrue(any(item['kind'] == 'dangling-reference' for item in issues))
            altered = copy.deepcopy(original)
            altered['tables']['qstore_checks'][0]['result'] = 'blocked'
            self.assertTrue(any(item['kind'] == 'receipt-header-mismatch' for item in inspect_snapshot(altered)['issues']))
            altered = copy.deepcopy(original)
            altered['tables']['qstore_check_inputs'].pop()
            self.assertTrue(any(item['kind'] == 'receipt-input-links-mismatch' for item in inspect_snapshot(altered)['issues']))


if __name__ == '__main__':
    unittest.main()
