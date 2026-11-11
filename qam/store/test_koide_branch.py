import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.tools.store_koide_branch import run


class KoideBranchTests(unittest.TestCase):
    def test_source_branch_and_open_native_obligations(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            result = run(root / 'store.sqlite3', root / 'export')
            manifest = json.loads((root / 'export/manifest.json').read_text(encoding='utf-8'))
            selection = manifest['selection']
            self.assertEqual(selection['snapshot_hash'], result['snapshot_hash'])
            self.assertEqual(sum(row['kind'] == 'claim' for row in selection['objects']), 4)
            self.assertEqual(sum(row['kind'] == 'proof' for row in selection['objects']), 4)
            self.assertEqual(sum(row['kind'] == 'guard' for row in selection['findings']), 2)
            self.assertEqual(manifest['technical_check']['result'], 'passed')
            tex = (root / 'export/paper.tex').read_text(encoding='utf-8')
            self.assertIn('historical-input comparison', tex)
            self.assertIn('independently of fitted masses', tex)


if __name__ == '__main__':
    unittest.main()
