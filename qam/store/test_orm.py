"""Regression checks for SQLAlchemy transaction and migration compatibility."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from qam.store.orm import store_session


class StoreOrmTests(unittest.TestCase):
    def test_commit_rollback_and_database_guards(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'store.sqlite3'
            with store_session(path) as (session, models):
                session.add(models.qstore_objects(object_id='definition-one', object_type='definition'))
                session.add(models.qstore_versions(
                    version_hash='test-version', object_id='definition-one',
                    payload_json='{}', status='declared', frame='unspecified'))
            with store_session(path) as (session, models):
                self.assertEqual(session.get(models.qstore_objects, 'definition-one').object_type, 'definition')
            with self.assertRaises(RuntimeError):
                with store_session(path) as (session, models):
                    session.add(models.qstore_objects(object_id='rollback', object_type='seed'))
                    session.flush()
                    raise RuntimeError('abort transaction')
            with store_session(path) as (session, models):
                self.assertIsNone(session.get(models.qstore_objects, 'rollback'))
                self.assertEqual(session.scalar(select(func.count()).select_from(models.qstore_ledger)), 6)
            with self.assertRaises(IntegrityError):
                with store_session(path) as (session, models):
                    session.add(models.qstore_objects(object_id='bad-type', object_type='missing'))
            with self.assertRaises(IntegrityError):
                with store_session(path) as (session, models):
                    session.get(models.qstore_versions, 'test-version').status = 'reviewed'
            with self.assertRaises(IntegrityError):
                with store_session(path) as (session, models):
                    session.delete(session.get(models.qstore_ledger, 1))


if __name__ == '__main__':
    unittest.main()
