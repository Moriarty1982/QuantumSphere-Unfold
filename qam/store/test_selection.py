from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.registry import register_link
from qam.store.selection import select_versions
from qam.store.snapshots import create_snapshot
from qam.tools.store_example import run


class SelectionTests(unittest.TestCase):
    def test_dependencies_snapshot_isolation_and_cycles(self):
        with TemporaryDirectory() as folder:
            db = Path(folder) / 'store.sqlite3'
            example = run(db)
            first = create_snapshot(db, 'selection-test')['snapshot_hash']
            roots = [example['seeds']['projector'], example['seeds']['commuting-transport']]
            selected = select_versions(db, first, roots)
            self.assertEqual(len(selected['objects']), 3)
            self.assertEqual(selected['objects'][0]['kind'], 'definition')
            self.assertTrue(any(item['kind'] == 'assumption' for item in selected['findings']))
            applicable = [item for item in selected['related_checks'] if item['all_matrix_inputs_selected']]
            self.assertEqual([item['result'] for item in applicable], ['passed'])
            register_link(db, {'source': example['definition'], 'target': roots[0],
                'kind': 'requires', 'status': 'declared', 'description': 'Deliberate test cycle'})
            self.assertEqual(select_versions(db, first, roots), selected)
            second = create_snapshot(db, 'cycle')['snapshot_hash']
            with self.assertRaisesRegex(ValueError, 'Cyclic'):
                select_versions(db, second, roots)
            with self.assertRaisesRegex(ValueError, 'absent'):
                select_versions(db, first, ['missing'])


if __name__ == '__main__':
    unittest.main()
