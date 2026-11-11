from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import unittest

from qam.store.scrub import scrub
from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export


def selection(texts):
    return {'selection_hash': 'fixture', 'objects': [
        {'kind': 'claim', 'version_hash': f'v{index}', 'payload': {'latex': text}}
        for index, text in enumerate(texts)]}


class ScrubTests(unittest.TestCase):
    def test_literal_references_and_comments(self):
        report = scrub(selection([r'\label{eq:one}\eqref{eq:one}']))
        self.assertEqual(report['result'], 'passed')
        report = scrub(selection([r'\label{x}', r'\label{x}\ref{missing}\cite{absent}']))
        self.assertEqual({item['kind'] for item in report['issues']},
                         {'duplicate-label', 'missing-label', 'missing-citation'})
        report = scrub(selection(['% \\ref{missing}\nText.', r'\% escaped \ref{qv-v0}']))
        self.assertEqual(report['result'], 'passed')
        report = scrub(selection([r'\ref{\generated}\input{external}']))
        self.assertEqual(report['result'], 'blocked')
        report = scrub(selection([r'\label{qv-v0}']))
        self.assertEqual(report['issues'][0]['kind'], 'duplicate-label')

    def test_export_stops_before_creating_output(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'missing.tex'
            source.write_text(r'\cite{missing}', encoding='utf-8')
            db = root / 'store.sqlite3'
            key = register(db, root, {'object_id': 'bad-reference', 'kind': 'claim',
                'frame': 'comparison', 'status': 'conditional',
                'payload': {'title': 'Missing citation', 'latex': source.read_text(),
                            'assumptions': [], 'dependencies': []},
                'source': {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                           'revision': 'test', 'locator': 'whole file'}})['version_hash']
            snapshot = create_snapshot(db, 'missing-reference')['snapshot_hash']
            with self.assertRaisesRegex(ValueError, 'missing-citation'):
                export(db, snapshot, [key], root / 'output')
            self.assertFalse((root / 'output').exists())

    def test_commands_packages_and_recursive_macros(self):
        report = scrub(selection([r'\UndefinedMacro']))
        self.assertTrue(any(item['kind'] == 'unresolved-command' for item in report['issues']))
        report = scrub(selection([r'\begin{proof}Text.\end{proof}']))
        self.assertTrue(any(item['kind'] == 'unsupported-environment' for item in report['issues']))
        report = scrub(selection([r'\mathbb{R}']))
        self.assertEqual(report['result'], 'blocked')
        selected = selection([r'\mathbb{R}'])
        selected['objects'].append({'kind': 'latex-resource', 'version_hash': 'package',
                                   'payload': {'package': 'amssymb'}})
        self.assertEqual(scrub(selected)['result'], 'passed')
        recursive = selection([r'\Loop'])
        recursive['objects'].append({'kind': 'latex-resource', 'version_hash': 'loop',
            'payload': {'resource_type': 'macro', 'name': 'Loop', 'latex': r'\newcommand{\Loop}{\Loop}'}})
        self.assertTrue(any(item['kind'] == 'recursive-macro' for item in scrub(recursive)['issues']))
        clash = selection([])
        clash['objects'].append({'kind': 'latex-resource', 'version_hash': 'frac',
            'payload': {'resource_type': 'macro', 'name': 'frac', 'latex': r'\newcommand{\frac}{x}'}})
        self.assertTrue(any(item['kind'] == 'macro-name-conflict' for item in scrub(clash)['issues']))


if __name__ == '__main__':
    unittest.main()
