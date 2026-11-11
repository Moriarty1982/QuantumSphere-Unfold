import copy
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select

from qam.store.orm import store_session
from qam.store.registry import register, register_link, register_guard, register_review, latest_review


class RegistryTests(unittest.TestCase):
    def test_versions_sources_seed_and_atomic_rejection(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'definition.tex'
            source.write_text('Example definition', encoding='utf-8')
            db = root / 'store.sqlite3'
            request = {
                'object_id': 'example-definition', 'kind': 'definition',
                'frame': 'comparison', 'status': 'conditional',
                'payload': {'title': 'Example', 'body': 'x is real', 'scope': 'test', 'assumptions': []},
                'source': {'path': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                           'revision': 'test-fixture', 'locator': 'line 1'},
            }
            definition = register(db, root, request)['version_hash']
            self.assertEqual(register(db, root, request)['version_hash'], definition)
            seed = copy.deepcopy(request)
            seed.update(object_id='example-seed', kind='seed')
            seed['payload'] = {'title': 'Initial value', 'value': '1/2', 'value_type': 'rational',
                               'origin': 'declared test input', 'assumptions': [], 'definition_version': definition}
            seed_hash = register(db, root, seed)['version_hash']
            guard = {'subject': seed_hash, 'target': definition, 'title': 'Missing native bridge',
                     'obligation': 'Derive this seed from the native definition', 'source': request['source']}
            guard_hash = register_guard(db, root, guard)['guard_hash']
            self.assertEqual(register_guard(db, root, guard)['guard_hash'], guard_hash)
            with store_session(db) as (session, models):
                row = session.get(models.qstore_guards, guard_hash)
                self.assertEqual(row.status, 'open')
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_guards)), 1)
            with self.assertRaises(ValueError):
                register_guard(db, root, {**guard, 'target': 'missing'})
            with self.assertRaises(ValueError):
                register_guard(db, root, {**guard, 'status': 'satisfied'})
            review = {'kind': 'guard', 'subject': guard_hash, 'previous': None,
                      'status': 'satisfied', 'reviewer': 'test reviewer',
                      'reason': 'Fixture assessment', 'evidence': request['source']}
            review_hash = register_review(db, root, review)['review_hash']
            self.assertEqual(register_review(db, root, review)['review_hash'], review_hash)
            with self.assertRaises(ValueError):
                register_review(db, root, {**review, 'reason': 'stale competing assessment'})
            register_review(db, root, {**review, 'previous': review_hash,
                                      'status': 'open', 'reason': 'Reopened in fixture'})
            with store_session(db) as (session, models):
                self.assertEqual(latest_review(session, models, 'guard', guard_hash).status, 'open')
                self.assertEqual(session.get(models.qstore_guards, guard_hash).status, 'open')
            with store_session(db) as (session, models):
                before = session.scalar(select(func.count()).select_from(models.qstore_ledger))
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_relations)), 1)
            bad = copy.deepcopy(seed)
            bad['object_id'] = 'bad-seed'
            bad['payload']['definition_version'] = 'missing'
            with self.assertRaises(ValueError):
                register(db, root, bad)
            with store_session(db) as (session, models):
                self.assertIsNone(session.get(models.qstore_objects, 'bad-seed'))
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_ledger)), before)
            changed = copy.deepcopy(request)
            changed['payload']['body'] = 'x is positive'
            self.assertNotEqual(register(db, root, changed)['version_hash'], definition)
            stale = copy.deepcopy(request)
            stale['source']['sha256'] = '0' * 64
            with self.assertRaises(ValueError):
                register(db, root, stale)
            with self.assertRaises(ValueError):
                register_link(db, {'source': seed_hash, 'target': definition,
                    'kind': 'requires', 'status': 'reviewed', 'description': 'unsupported promotion'})


if __name__ == '__main__':
    unittest.main()
