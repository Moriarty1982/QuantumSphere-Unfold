"""Content-addressed inventory snapshots with embedded store rows and provenance."""

import json

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest, require_text
from qam.store.integrity import inspect_snapshot


TABLES = (
    'qstore_schema', 'qstore_object_types', 'qstore_objects', 'qstore_versions',
    'qstore_sources', 'qstore_relations', 'qstore_guards', 'qstore_reviews',
    'qstore_checks', 'qstore_check_inputs',
)


def create_snapshot(path, label):
    require_text(label, 'label')
    with store_session(path) as (session, models):
        tables = {}
        for name in TABLES:
            table = getattr(models, name).__table__
            tables[name] = sorted((dict(row) for row in session.execute(select(table)).mappings()), key=canonical)
        ledger_table = models.qstore_ledger.__table__
        # Snapshot bookkeeping is excluded to make an unchanged checkpoint repeatable.
        ledger = [dict(row) for row in session.execute(select(ledger_table).where(
            ledger_table.c.event_type != 'SNAPSHOT').order_by(ledger_table.c.event_id)).mappings()]
        payload = {'format': 'qstore-snapshot-v1', 'label': label, 'tables': tables,
                   'ledger': ledger, 'ledger_hash': digest(ledger),
                   'status': 'inventory-checkpoint',
                   'scope': 'Store namespace only; no guard discharge or mathematical certification'}
        report = inspect_snapshot(payload)
        if report['result'] != 'passed':
            raise ValueError('Store integrity check failed: ' + canonical(report['issues']))
        key = digest(payload)
        if session.get(models.qstore_snapshots, key) is None:
            session.add(models.qstore_snapshots(snapshot_hash=key, label=label, payload_json=canonical(payload)))
            session.add(models.qstore_ledger(event_type='SNAPSHOT', payload_json=canonical({'snapshot_hash': key})))
        return {'snapshot_hash': key, 'label': label, 'status': payload['status'],
                'counts': {name: len(rows) for name, rows in tables.items()}, 'ledger_hash': payload['ledger_hash']}


def read_snapshot(path, key):
    with store_session(path) as (session, models):
        row = session.get(models.qstore_snapshots, key)
        if row is None:
            raise ValueError('Unknown snapshot')
        payload = json.loads(row.payload_json)
        if digest(payload) != key or digest(payload['ledger']) != payload['ledger_hash']:
            raise ValueError('Snapshot integrity check failed')
        report = inspect_snapshot(payload)
        if report['result'] != 'passed':
            raise ValueError('Store integrity check failed: ' + canonical(report['issues']))
        return {'snapshot_hash': key, **payload}
