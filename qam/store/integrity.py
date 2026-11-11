"""Verify internal hashes and references of an embedded store checkpoint."""

import json

from qam.store.registry import digest


def inspect_snapshot(snapshot):
    tables = snapshot['tables']
    issues = []
    objects = {row['object_id']: row for row in tables['qstore_objects']}
    types = {row['name'] for row in tables['qstore_object_types']}
    versions = {row['version_hash']: row for row in tables['qstore_versions']}
    relations = {row['relation_hash']: row for row in tables['qstore_relations']}
    guards = {row['guard_hash']: row for row in tables['qstore_guards']}
    reviews = {row['review_hash']: row for row in tables['qstore_reviews']}
    checks = {row['receipt_hash']: row for row in tables['qstore_checks']}

    def reference(value, index, context, optional=False):
        if not (optional and value is None) and value not in index:
            issues.append({'kind': 'dangling-reference', 'context': context, 'target': value})

    def hashed(key, identity, context):
        if digest(identity) != key:
            issues.append({'kind': 'content-hash-mismatch', 'context': context, 'hash': key})

    for row in objects.values():
        reference(row['object_type'], types, row['object_id'])
    for key, row in versions.items():
        reference(row['object_id'], objects, key)
        if row['object_id'] not in objects:
            continue
        try:
            payload = json.loads(row['payload_json'])
            kind = objects[row['object_id']]['object_type']
            hashed(key, {'format': 'qstore-version-v1', 'object_id': row['object_id'], 'kind': kind,
                         'frame': row['frame'], 'status': row['status'], 'payload': payload}, key)
            if kind == 'seed':
                reference(payload['definition_version'], versions, key)
            for dependency in payload.get('dependencies', []):
                reference(dependency, versions, key)
            for endpoint in payload.get('placement', {}).values():
                reference(endpoint, versions, key)
        except (ValueError, KeyError, TypeError) as exc:
            issues.append({'kind': 'invalid-payload', 'context': key, 'message': str(exc)})
    for row in tables['qstore_sources']:
        reference(row['version_hash'], versions, 'source')
    for key, row in relations.items():
        reference(row['source_version'], versions, key)
        reference(row['target_version'], versions, key)
        hashed(key, {'source': row['source_version'], 'target': row['target_version'],
                     'kind': row['relation_type'], 'status': row['status'],
                     'payload': json.loads(row['payload_json'])}, key)
    for key, row in guards.items():
        reference(row['subject_version'], versions, key)
        reference(row['target_version'], versions, key, optional=True)
        hashed(key, {'format': 'qstore-guard-v1', 'subject': row['subject_version'],
                     'target': row['target_version'], 'status': row['status'],
                     'payload': json.loads(row['payload_json'])}, key)
    successors = {}
    roots = {}
    for key, row in reviews.items():
        kind = 'guard' if row['guard_hash'] is not None else 'relation'
        subject = row[kind + '_hash']
        reference(subject, guards if kind == 'guard' else relations, key)
        reference(row['previous_hash'], reviews, key, optional=True)
        hashed(key, {'format': 'qstore-review-v1', 'kind': kind, 'subject': subject,
                     'previous': row['previous_hash'], 'status': row['status'],
                     'payload': json.loads(row['payload_json'])}, key)
        previous = row['previous_hash']
        if previous is None:
            roots.setdefault((kind, subject), []).append(key)
        else:
            successors.setdefault(previous, []).append(key)
            parent = reviews.get(previous)
            if parent and (parent['guard_hash'], parent['relation_hash']) != (row['guard_hash'], row['relation_hash']):
                issues.append({'kind': 'review-subject-mismatch', 'context': key})
        seen = {key}
        while previous in reviews:
            if previous in seen:
                issues.append({'kind': 'review-cycle', 'context': key})
                break
            seen.add(previous)
            previous = reviews[previous]['previous_hash']
    if any(len(items) != 1 for items in roots.values()) or any(len(items) > 1 for items in successors.values()):
        issues.append({'kind': 'review-branch-conflict'})
    input_links = {}
    for row in tables['qstore_check_inputs']:
        reference(row['receipt_hash'], checks, 'check-input')
        reference(row['version_hash'], versions, 'check-input')
        input_links.setdefault(row['receipt_hash'], set()).add(row['version_hash'])
    for key, row in checks.items():
        receipt = json.loads(row['receipt_json'])
        hashed(key, receipt, key)
        if row['result'] != receipt['result'] or row['checker_hash'] != receipt['checker_hash'] or row['checker'] != receipt['checker']:
            issues.append({'kind': 'receipt-header-mismatch', 'context': key})
        if set(receipt['inputs']) != input_links.get(key, set()):
            issues.append({'kind': 'receipt-input-links-mismatch', 'context': key})
        for version, identity in receipt['inputs'].items():
            reference(version, versions, key)
            hashed(version, identity, key)
    result = {'format': 'qstore-integrity-v1', 'result': 'blocked' if issues else 'passed',
              'issues': issues, 'scope': 'Internal stored hashes and links; current filesystem and mathematical validity are separate'}
    return {'report_hash': digest(result), **result}
