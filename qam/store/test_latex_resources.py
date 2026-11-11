import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export
from qam.store.latex_resources import validate_resource


class LatexResourceTests(unittest.TestCase):
    def test_resource_export_and_conflicts(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'resources.tex'
            macro = r'\newcommand{\QamHalf}{\frac{1}{2}}'
            revised = r'\newcommand{\QamHalf}{0.5}'
            citation = r'\bibitem{comparison}Declared comparison source.'
            statement = r'The value is $\QamHalf$; see \cite{comparison}.'
            source.write_text('\n'.join([macro, revised, citation, statement]), encoding='utf-8')
            provenance = {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                          'revision': 'fixture', 'locator': 'whole file'}
            db = root / 'store.sqlite3'

            def store(key, kind, payload):
                return register(db, root, {'object_id': key, 'kind': kind, 'frame': 'comparison',
                    'status': 'conditional', 'source': provenance, 'payload': payload})['version_hash']

            macro_payload = {'title': 'Half', 'resource_type': 'macro', 'name': 'QamHalf',
                             'latex': macro, 'assumptions': [], 'dependencies': []}
            macro_hash = store('half', 'latex-resource', macro_payload)
            citation_hash = store('citation', 'latex-resource', {
                'title': 'Reference', 'resource_type': 'bibliography', 'key': 'comparison',
                'latex': citation, 'assumptions': [], 'dependencies': []})
            claim = store('claim', 'claim', {'title': 'Value', 'latex': statement,
                'assumptions': [], 'dependencies': [macro_hash, citation_hash]})
            snapshot = create_snapshot(db, 'resources')['snapshot_hash']
            export(db, snapshot, [claim], root / 'export')
            tex = (root / 'export/paper.tex').read_text(encoding='utf-8')
            self.assertLess(tex.index(macro), tex.index(r'\begin{document}'))
            self.assertIn(citation, tex)
            self.assertEqual(tex.count(macro), 1)
            alternative = store('half', 'latex-resource', {**macro_payload, 'latex': revised})
            changed = create_snapshot(db, 'conflict')['snapshot_hash']
            with self.assertRaisesRegex(ValueError, 'Conflicting'):
                export(db, changed, [claim, alternative], root / 'bad')
            self.assertFalse((root / 'bad').exists())
            with self.assertRaises(ValueError):
                validate_resource({**macro_payload, 'latex': macro + '\n' + revised})
            with self.assertRaises(ValueError):
                validate_resource({**macro_payload, 'latex': r'\newcommand{\Other}{x}'})


if __name__ == '__main__':
    unittest.main()
