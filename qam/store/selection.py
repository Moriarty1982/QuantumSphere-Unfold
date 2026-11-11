"""Resolve a version-pinned argument selection exclusively from a stored snapshot."""

import json

from qam.store.registry import digest
from qam.store.snapshots import read_snapshot


def select_versions(path, snapshot_hash, roots):
    if not isinstance(roots, list) or not roots or any(not isinstance(key, str) for key in roots):
        raise ValueError('roots must be a nonempty list of version hashes')
    snapshot = read_snapshot(path, snapshot_hash)
    tables = snapshot['tables']
    versions = {row['version_hash']: row for row in tables['qstore_versions']}
    objects = {row['object_id']: row for row in tables['qstore_objects']}
    reviews = tables['qstore_reviews']

    def effective(kind, key, original):
        rows = [row for row in reviews if row[kind + '_hash'] == key]
        previous = {row['previous_hash'] for row in rows}
        heads = [row for row in rows if row['review_hash'] not in previous]
        if len(heads) > 1:
            raise ValueError('Conflicting review heads in snapshot')
        return heads[0]['status'] if heads else original

    dependencies = {}
    for relation in tables['qstore_relations']:
        status = effective('relation', relation['relation_hash'], relation['status'])
        if relation['relation_type'] in {'interpreted-by', 'requires'}:
            dependencies.setdefault(relation['source_version'], []).append((relation, status))
    ordered = []
    active = set()
    visited = set()
    findings = []

    def visit(key):
        if key not in versions:
            raise ValueError(f'Version absent from selected snapshot: {key}')
        if key in active:
            raise ValueError(f'Cyclic prerequisite at {key}')
        if key in visited:
            return
        active.add(key)
        for relation, status in sorted(dependencies.get(key, []), key=lambda item: item[0]['relation_hash']):
            if status in {'declared', 'reviewed'}:
                visit(relation['target_version'])
                if versions[key]['frame'] != versions[relation['target_version']]['frame']:
                    findings.append({'kind': 'frame-bridge-required', 'relation': relation['relation_hash']})
                if status == 'declared':
                    findings.append({'kind': 'declared-dependency', 'relation': relation['relation_hash']})
            elif status == 'proposed':
                findings.append({'kind': 'proposed-dependency', 'relation': relation['relation_hash'],
                                 'target': relation['target_version']})
        active.remove(key)
        visited.add(key)
        ordered.append(key)

    for root in dict.fromkeys(roots):
        visit(root)
    # Editorial endpoints select context but are not mathematical prerequisites.
    while True:
        added = False
        for key in list(ordered):
            row = versions[key]
            if objects[row['object_id']]['object_type'] == 'transition':
                placement = json.loads(row['payload_json']).get('placement')
                if placement:
                    for endpoint in placement.values():
                        if endpoint not in visited:
                            visit(endpoint)
                            added = True
        candidates = {}
        for key, row in versions.items():
            if objects[row['object_id']]['object_type'] != 'transition' or row['status'] == 'withdrawn':
                continue
            placement = json.loads(row['payload_json']).get('placement')
            if placement and set(placement.values()) <= visited:
                candidates.setdefault(row['object_id'], []).append(key)
        for identity, keys in sorted(candidates.items()):
            chosen = [key for key in keys if key in visited]
            if len(chosen) > 1 or (not chosen and len(keys) > 1):
                raise ValueError(f'Ambiguous transition versions for {identity}; select one exact version')
            key = chosen[0] if chosen else keys[0]
            if key not in visited:
                visit(key)
                added = True
        if not added:
            break
    predecessors = {key: set() for key in ordered}
    for key in ordered:
        for relation, status in dependencies.get(key, []):
            if status in {'declared', 'reviewed'}:
                predecessors[key].add(relation['target_version'])
        row = versions[key]
        if objects[row['object_id']]['object_type'] == 'transition':
            placement = json.loads(row['payload_json']).get('placement')
            if placement:
                predecessors[key].add(placement['after'])
                predecessors[placement['before']].add(key)
    pending = list(ordered)
    ordered = []
    emitted = set()
    while pending:
        key = next((key for key in pending if predecessors[key] <= emitted), None)
        if key is None:
            raise ValueError('Cyclic prerequisite or editorial placement constraints')
        pending.remove(key)
        ordered.append(key)
        emitted.add(key)
    selected = []
    for key in ordered:
        row = versions[key]
        payload = json.loads(row['payload_json'])
        selected.append({'version_hash': key, 'object_id': row['object_id'],
                         'kind': objects[row['object_id']]['object_type'],
                         'frame': row['frame'], 'status': row['status'], 'payload': payload})
        if row['status'] != 'reviewed':
            findings.append({'kind': 'object-status', 'version': key, 'status': row['status']})
        if row['frame'] == 'unspecified':
            findings.append({'kind': 'unspecified-frame', 'version': key})
        for assumption in payload.get('assumptions', []):
            findings.append({'kind': 'assumption', 'version': key, 'text': assumption})
    for guard in tables['qstore_guards']:
        if guard['subject_version'] in visited or guard['target_version'] in visited:
            status = effective('guard', guard['guard_hash'], guard['status'])
            if status != 'satisfied':
                findings.append({'kind': 'guard', 'hash': guard['guard_hash'],
                                 'status': status, 'subject': guard['subject_version'],
                                 'target': guard['target_version'], 'payload': json.loads(guard['payload_json'])})
    check_ids = {row['receipt_hash'] for row in tables['qstore_check_inputs'] if row['version_hash'] in visited}
    checks = []
    for row in tables['qstore_checks']:
        if row['receipt_hash'] in check_ids:
            receipt = json.loads(row['receipt_json'])
            if digest(receipt) != row['receipt_hash']:
                raise ValueError('Invalid check receipt in snapshot')
            checks.append({'receipt_hash': row['receipt_hash'], 'result': row['result'],
                           'all_matrix_inputs_selected': set(receipt['request'].values()) <= visited})
    result = {'format': 'qstore-selection-v1', 'snapshot_hash': snapshot_hash,
              'roots': list(dict.fromkeys(roots)), 'objects': selected,
              'relations': [{**row, 'effective_status': effective('relation', row['relation_hash'], row['status'])}
                            for row in tables['qstore_relations']
                            if row['source_version'] in visited and row['target_version'] in visited],
              'findings': findings, 'related_checks': checks,
              'scope': 'Dependency inventory; publication and LaTeX readiness are not certified'}
    return {'selection_hash': digest(result), **result}
