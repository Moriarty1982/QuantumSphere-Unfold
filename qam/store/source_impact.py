"""Report source-byte drift and downstream dependencies without changing prior evidence."""

import hashlib
import json
from pathlib import Path

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import digest
from qam.store.snapshots import read_snapshot


def impact(snapshot, roots):
    tables = snapshot['tables']
    versions = {row['version_hash']: row for row in tables['qstore_versions']}
    if any(key not in versions for key in roots):
        raise ValueError('Impact roots must be versions present in the snapshot')
    reviews = tables['qstore_reviews']
    previous = {row['previous_hash'] for row in reviews}
    relation_status = {row['relation_hash']: row['status'] for row in reviews
                       if row['relation_hash'] is not None and row['review_hash'] not in previous}
    downstream = {}
    for row in tables['qstore_relations']:
        status = relation_status.get(row['relation_hash'], row['status'])
        if row['relation_type'] in {'requires', 'interpreted-by'} and status in {'declared', 'reviewed'}:
            downstream.setdefault(row['target_version'], set()).add(row['source_version'])
    for key, row in versions.items():
        payload = json.loads(row['payload_json'])
        for endpoint in payload.get('placement', {}).values():
            downstream.setdefault(endpoint, set()).add(key)
    affected = set(roots)
    pending = list(roots)
    while pending:
        for key in downstream.get(pending.pop(), set()) - affected:
            affected.add(key)
            pending.append(key)
    receipts = sorted({row['receipt_hash'] for row in tables['qstore_check_inputs']
                       if row['version_hash'] in affected})
    guards = sorted(row['guard_hash'] for row in tables['qstore_guards']
                    if row['subject_version'] in affected or row['target_version'] in affected)
    return {'roots': sorted(set(roots)), 'affected_versions': sorted(affected),
            'dependent_versions': sorted(affected - set(roots)),
            'affected_receipts': receipts, 'affected_guards': guards,
            'scope': 'Declared/reviewed prerequisite edges and editorial endpoints in this snapshot; '
                     'affected means review candidate, not a failed or revoked historical result'}


def containing_snapshots(database, affected):
    affected = set(affected)
    result = []
    with store_session(database) as (session, models):
        rows = [(row.snapshot_hash, row.payload_json) for row in session.scalars(
            select(models.qstore_snapshots).order_by(models.qstore_snapshots.snapshot_hash))]
    for key, text in rows:
        payload = json.loads(text)
        if digest(payload) != key:
            raise ValueError('Stored snapshot hash mismatch during impact lookup')
        matches = affected & {row['version_hash'] for row in payload['tables']['qstore_versions']}
        if matches:
            result.append({'snapshot_hash': key, 'label': payload['label'], 'contained_versions': sorted(matches)})
    return result


def impact_report(database, snapshot_hash, roots):
    if not isinstance(roots, list) or any(not isinstance(key, str) for key in roots):
        raise ValueError('roots must be a list of version hashes')
    result = impact(read_snapshot(database, snapshot_hash), roots)
    result.update(format='qstore-impact-v1', snapshot_hash=snapshot_hash)
    result['containing_snapshots'] = containing_snapshots(database, result['affected_versions'])
    return {'report_hash': digest(result), **result}


def freshness_report(database, snapshot_hash, repo):
    snapshot = read_snapshot(database, snapshot_hash)
    root = Path(repo).resolve()
    observations = []
    changed = set()
    tables = snapshot['tables']

    def observe(source, owner_type, owner):
        try:
            relative = Path(source['path'])
            if relative.is_absolute():
                raise ValueError('Absolute registered source path')
            path = (root / relative).resolve()
            path.relative_to(root)
        except ValueError:
            status, actual = 'invalid-path', None
        else:
            try:
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                status = 'matches' if actual == source['sha256'] else 'bytes-changed'
            except FileNotFoundError:
                status, actual = 'missing', None
            except OSError:
                status, actual = 'unreadable', None
        observations.append({'owner_type': owner_type, 'owner': owner, 'path': source['path'],
                             'recorded_sha256': source['sha256'], 'actual_sha256': actual, 'status': status})
        return status != 'matches'

    for source in tables['qstore_sources']:
        if observe({'path': source['source_path'], 'sha256': source['source_hash']}, 'version', source['version_hash']):
            changed.add(source['version_hash'])
    evidence_changes = []
    evidence_versions = set()
    guard_rows = {row['guard_hash']: row for row in tables['qstore_guards']}
    relation_rows = {row['relation_hash']: row for row in tables['qstore_relations']}

    def evidence_endpoints(row, kind):
        names = ('subject_version', 'target_version') if kind == 'guard' else ('source_version', 'target_version')
        evidence_versions.update(row[name] for name in names if row[name] is not None)

    for row in tables['qstore_guards']:
        payload = json.loads(row['payload_json'])
        if observe(payload['source'], 'guard', row['guard_hash']):
            evidence_changes.append({'kind': 'guard-source-changed', 'hash': row['guard_hash']})
            evidence_endpoints(row, 'guard')
    for row in tables['qstore_reviews']:
        payload = json.loads(row['payload_json'])
        if observe(payload['evidence'], 'review', row['review_hash']):
            evidence_changes.append({'kind': 'review-evidence-changed', 'hash': row['review_hash'],
                                     'guard_hash': row['guard_hash'], 'relation_hash': row['relation_hash']})
            if row['guard_hash'] is not None:
                evidence_endpoints(guard_rows[row['guard_hash']], 'guard')
            else:
                evidence_endpoints(relation_rows[row['relation_hash']], 'relation')
    dependencies = impact(snapshot, sorted(changed))
    evidence_dependencies = impact(snapshot, sorted(evidence_versions))
    result = {'format': 'qstore-freshness-v1', 'snapshot_hash': snapshot_hash,
              'result': 'review-needed' if changed or evidence_changes else 'matches',
              'sources': observations, 'evidence_changes': evidence_changes, 'impact': dependencies,
              'evidence_impact': evidence_dependencies,
              'containing_snapshots': containing_snapshots(database,
                  set(dependencies['affected_versions']) | set(evidence_dependencies['affected_versions'])),
              'scope': 'Exact source bytes compared with current files; semantic changes and historical correctness require review'}
    return {'report_hash': digest(result), **result}
