from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from qam.store.argument_view import markdown
from qam.store.selection import select_versions
from qam.tools.store_koide_branch import run


class ArgumentViewTests(unittest.TestCase):
    def test_graph_retains_declared_edges_and_guards(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            result = run(db, root / 'export')
            selection = select_versions(db, result['snapshot_hash'], result['roots'])
            view = markdown(selection)
            self.assertIn('flowchart TD', view)
            self.assertIn('requires - declared', view)
            self.assertIn('Native mass-root mechanism remains open', view)
            self.assertEqual(view.count('style g'), 2)
            manifest = json.loads((root / 'export/manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(selection, manifest['selection'])
            self.assertEqual(view, markdown(selection))


if __name__ == '__main__':
    unittest.main()
