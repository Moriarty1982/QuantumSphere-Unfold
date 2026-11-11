import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export
from qam.store.orm import store_session
from sqlalchemy import func, select


class LatexBlockTests(unittest.TestCase):
    def test_source_bound_blocks_packages_and_atomic_dependencies(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'blocks.tex'
            source.write_text(r'\[P^2=P\]' + '\n' + r'\begin{proof}Direct multiplication.\end{proof}'
                              + '\nWe now examine this identity in the declared comparison.', encoding='utf-8')
            db = root / 'store.sqlite3'
            provenance = {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                          'revision': 'fixture', 'locator': 'whole file'}

            def request(key, kind, payload):
                return {'object_id': key, 'kind': kind, 'frame': 'comparison', 'status': 'conditional',
                        'payload': payload, 'source': provenance}

            package = register(db, root, request('package', 'latex-resource', {
                'title': 'Proof environment', 'package': 'amsthm', 'assumptions': []}))['version_hash']
            claim = register(db, root, request('claim', 'claim', {'title': 'Claim', 'latex': r'\[P^2=P\]',
                             'assumptions': [], 'dependencies': []}))['version_hash']
            proof_request = request('proof', 'proof', {'title': 'Proof',
                'latex': r'\begin{proof}Direct multiplication.\end{proof}',
                'assumptions': [], 'dependencies': [claim, package]})
            proof = register(db, root, proof_request)['version_hash']
            transition = register(db, root, request('transition', 'transition', {
                'title': 'Connecting text', 'latex': 'We now examine this identity in the declared comparison.',
                'assumptions': ['The native physical bridge remains open'],
                'dependencies': [claim]}))['version_hash']
            snapshot = create_snapshot(db, 'blocks')['snapshot_hash']
            export(db, snapshot, [transition, proof], root / 'export')
            tex = (root / 'export/paper.tex').read_text(encoding='utf-8')
            self.assertIn(r'\usepackage{amsthm}', tex)
            self.assertIn(proof_request['payload']['latex'], tex)
            self.assertIn('The native physical bridge remains open', tex)
            self.assertIn('We now examine this identity', tex)
            self.assertLess(tex.index(r'\[P^2=P\]'), tex.index(r'\begin{proof}'))
            with self.assertRaises(ValueError):
                register(db, root, request('invented', 'claim', {'title': 'Missing', 'latex': 'Not in source',
                    'assumptions': [], 'dependencies': []}))
            with self.assertRaises(ValueError):
                register(db, root, request('missing-dependency', 'proof', {
                    **proof_request['payload'], 'dependencies': ['missing']}))
            with store_session(db) as (session, models):
                self.assertIsNone(session.get(models.qstore_objects, 'missing-dependency'))
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_objects)), 4)

    def test_automatic_placement_version_choice_and_cycles(self):
        from qam.store.selection import select_versions

        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'blocks.tex'
            source.write_text('First statement.\nSecond statement.\nConnecting text.\nRevised connection.', encoding='utf-8')
            db = root / 'store.sqlite3'
            provenance = {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                          'revision': 'fixture', 'locator': 'whole file'}

            def store(key, kind, latex, **extra):
                return register(db, root, {'object_id': key, 'kind': kind, 'frame': 'comparison',
                    'status': 'conditional', 'source': provenance,
                    'payload': {'title': key, 'latex': latex, 'assumptions': [], 'dependencies': [], **extra}})['version_hash']

            first = store('first', 'claim', 'First statement.')
            second = store('second', 'claim', 'Second statement.')
            transition = store('bridge', 'transition', 'Connecting text.', placement={'after': first, 'before': second})
            snapshot = create_snapshot(db, 'placement')['snapshot_hash']
            result = select_versions(db, snapshot, [second, first])
            self.assertEqual([row['version_hash'] for row in result['objects']], [first, transition, second])
            revised = store('bridge', 'transition', 'Revised connection.', placement={'after': first, 'before': second})
            changed = create_snapshot(db, 'revised-placement')['snapshot_hash']
            with self.assertRaisesRegex(ValueError, 'Ambiguous'):
                select_versions(db, changed, [first, second])
            selected = select_versions(db, changed, [revised])
            self.assertEqual([row['version_hash'] for row in selected['objects']], [first, revised, second])
            self.assertEqual(select_versions(db, snapshot, [second, first]), result)
            from qam.store.registry import register_link
            register_link(db, {'source': first, 'target': second, 'kind': 'requires',
                               'status': 'declared', 'description': 'Conflicts with editorial placement'})
            cyclic = create_snapshot(db, 'cycle')['snapshot_hash']
            with self.assertRaisesRegex(ValueError, 'Cyclic'):
                select_versions(db, cyclic, [revised])


if __name__ == '__main__':
    unittest.main()
