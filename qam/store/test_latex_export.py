import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.latex_export import export, escape
from qam.store.snapshots import create_snapshot
from qam.tools.store_example import run


class LatexExportTests(unittest.TestCase):
    def test_manifest_reproducibility_and_no_overwrite(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            db = root / 'store.sqlite3'
            example = run(db)
            snapshot = create_snapshot(db, 'export-test')['snapshot_hash']
            roots = [example['seeds']['projector'], example['seeds']['commuting-transport']]
            first = export(db, snapshot, roots, root / 'first')
            second = export(db, snapshot, roots, root / 'second')
            self.assertEqual(first['manifest_hash'], second['manifest_hash'])
            tex = (root / 'first/paper.tex').read_bytes()
            manifest = json.loads((root / 'first/manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(hashlib.sha256(tex).hexdigest(), manifest['files']['paper.tex'])
            self.assertIn(b'No identification with a native physical transport', tex)
            self.assertIn(b'passed', tex)
            self.assertNotIn(b'failed', tex)
            self.assertIn(r'\textbackslash{}input\{secret\}', escape(r'\input{secret}'))
            with self.assertRaises(FileExistsError):
                export(db, snapshot, roots, root / 'first')


if __name__ == '__main__':
    unittest.main()
