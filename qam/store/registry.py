"""Validated registration of source-backed definitions, seeds and links."""

import hashlib
import json
from pathlib import Path

from sqlalchemy import select

from qam.store.orm import store_session


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode('utf-8')).hexdigest()


def require_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{name} must be nonempty text')


def source_record(repo, source):
    if not isinstance(source, dict) or set(source) != {'path', 'sha256', 'revision', 'locator'}:
        raise ValueError('Source requires path, sha256, revision and locator')
    for name, value in source.items():
        require_text(value, f'source.{name}')
    root = Path(repo).resolve()
    relative = Path(source['path'])
    if relative.is_absolute():
        raise ValueError('Source path must be repository-relative')
    path = (root / relative).resolve()
    path.relative_to(root)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if source['sha256'] != actual:
        raise ValueError('Source SHA256 does not match current file bytes')
    return {**source, 'path': path.relative_to(root).as_posix()}


def link(session, models, source, target, kind, status, description):
    if kind not in {'interpreted-by', 'requires', 'explains', 'proves', 'contains', 'belongs-to', 'supersedes', 'same-source-as'}:
        raise ValueError('Unknown relation type')
    if status not in {'proposed', 'declared'}:
        raise ValueError('Registration permits proposed or declared links')
    require_text(description, 'description')
    left = session.get(models.qstore_versions, source)
    right = session.get(models.qstore_versions, target)
    if left is None or right is None:
        raise ValueError('Both endpoints must be registered versions')
    if kind == 'interpreted-by':
        obj = session.get(models.qstore_objects, right.object_id)
        if obj.object_type != 'definition' or left.frame != right.frame:
            raise ValueError('Interpretation requires a definition in the same declared frame')
    payload = {'description': description}
    identity = {'source': source, 'target': target, 'kind': kind, 'status': status, 'payload': payload}
    key = digest(identity)
    if session.get(models.qstore_relations, key) is None:
        session.add(models.qstore_relations(relation_hash=key, source_version=source,
                    target_version=target, relation_type=kind, status=status, payload_json=canonical(payload)))
        session.add(models.qstore_ledger(event_type='LINK', payload_json=canonical({'relation_hash': key})))
    return key


def register(path, repo, request):
    if not isinstance(request, dict) or set(request) != {'object_id', 'kind', 'frame', 'status', 'payload', 'source'}:
        raise ValueError('Registration requires object_id, kind, frame, status, payload and source')
    for name in ('object_id', 'kind', 'frame', 'status'):
        require_text(request[name], name)
    kind = request['kind']
    text_kinds = {'claim', 'proof', 'explanation', 'transition'}
    if kind not in {'definition', 'seed', 'latex-resource'} | text_kinds:
        raise ValueError('Unsupported object type')
    if request['status'] not in {'imported-unreviewed', 'declared', 'conditional'}:
        raise ValueError('Registration does not grant review or withdrawal status')
    payload = request['payload']
    if kind == 'definition':
        fields = {'title', 'body', 'scope', 'assumptions'}
    elif kind == 'seed':
        fields = {'title', 'value', 'value_type', 'origin', 'assumptions', 'definition_version'}
    elif kind == 'latex-resource':
        if isinstance(payload, dict) and 'resource_type' in payload:
            symbol = 'name' if payload['resource_type'] == 'macro' else 'key'
            fields = {'title', 'resource_type', symbol, 'latex', 'assumptions', 'dependencies'}
        else:
            fields = {'title', 'package', 'assumptions'}
    else:
        fields = {'title', 'latex', 'assumptions', 'dependencies'}
    if kind == 'transition' and isinstance(payload, dict) and 'placement' in payload:
        fields = fields | {'placement'}
    if not isinstance(payload, dict) or set(payload) != fields:
        raise ValueError(f'{kind} payload requires exactly {sorted(fields)}')
    for name in fields - {'assumptions', 'value', 'dependencies', 'placement'}:
        require_text(payload[name], name)
    if not isinstance(payload['assumptions'], list):
        raise ValueError('assumptions must be a list of explicit statements')
    for item in payload['assumptions']:
        require_text(item, 'assumption')
    if kind == 'seed' and payload['value'] is None:
        raise ValueError('Seed value must be explicit')
    has_dependencies = kind in text_kinds or (kind == 'latex-resource' and 'resource_type' in payload)
    if has_dependencies:
        if not isinstance(payload['dependencies'], list):
            raise ValueError('dependencies must be a list of exact version hashes')
        for key in payload['dependencies']:
            require_text(key, 'dependency')
    if kind == 'transition' and 'placement' in payload:
        placement = payload['placement']
        if not isinstance(placement, dict) or set(placement) != {'after', 'before'}:
            raise ValueError('placement requires after and before version hashes')
        for key in placement.values():
            require_text(key, 'placement endpoint')
        if placement['after'] == placement['before']:
            raise ValueError('Transition endpoints must differ')
    if kind == 'latex-resource':
        if 'resource_type' in payload:
            from qam.store.latex_resources import validate_resource

            validate_resource(payload)
        elif payload['package'] not in {'amsthm', 'amssymb', 'array'}:
            raise ValueError('Supported package resources: amsthm, amssymb, array')
    source = source_record(repo, request['source'])
    if has_dependencies:
        original = (Path(repo) / source['path']).read_text(encoding='utf-8-sig')
        if payload['latex'].replace('\r\n', '\n') not in original:
            raise ValueError('LaTeX block must occur verbatim in the declared source')
    identity = {key: request[key] for key in ('object_id', 'kind', 'frame', 'status', 'payload')}
    version = digest({'format': 'qstore-version-v1', **identity})
    with store_session(path) as (session, models):
        obj = session.get(models.qstore_objects, request['object_id'])
        if obj is not None and obj.object_type != kind:
            raise ValueError('Stable object identity cannot change type')
        if obj is None:
            session.add(models.qstore_objects(object_id=request['object_id'], object_type=kind))
            session.flush()
        if session.get(models.qstore_versions, version) is None:
            session.add(models.qstore_versions(version_hash=version, object_id=request['object_id'],
                        payload_json=canonical(payload), status=request['status'], frame=request['frame']))
            session.flush()
            session.add(models.qstore_ledger(event_type='STORE', payload_json=canonical({'version_hash': version})))
        query = select(models.qstore_sources).filter_by(version_hash=version,
            source_path=source['path'], source_hash=source['sha256'],
            source_revision=source['revision'], locator=source['locator'])
        if session.scalar(query) is None:
            session.add(models.qstore_sources(version_hash=version, source_path=source['path'],
                        source_hash=source['sha256'], source_revision=source['revision'], locator=source['locator']))
            session.add(models.qstore_ledger(event_type='SOURCE', payload_json=canonical({'version_hash': version, **source})))
        if kind == 'seed':
            link(session, models, version, payload['definition_version'], 'interpreted-by',
                 'declared', 'Seed interpretation supplied by the registering author')
        if has_dependencies:
            for dependency in dict.fromkeys(payload['dependencies']):
                target = session.get(models.qstore_versions, dependency)
                if target is None or target.frame != request['frame']:
                    raise ValueError('Block dependencies require registered versions in the same frame')
                link(session, models, version, dependency, 'requires', 'declared',
                     'Declared prerequisite of a source-backed LaTeX block')
        if kind == 'transition' and 'placement' in payload:
            for endpoint in payload['placement'].values():
                target = session.get(models.qstore_versions, endpoint)
                if target is None or target.frame != request['frame']:
                    raise ValueError('Placement endpoints require registered versions in the same frame')
    return {'version_hash': version, 'status': request['status']}


def register_link(path, request):
    if not isinstance(request, dict) or set(request) != {'source', 'target', 'kind', 'status', 'description'}:
        raise ValueError('Link requires source, target, kind, status and description')
    for key, value in request.items():
        require_text(value, key)
    with store_session(path) as (session, models):
        key = link(session, models, **request)
    return {'relation_hash': key, 'status': request['status']}


def register_guard(path, repo, request):
    """Record an open obligation; closing it requires a future evidence review API."""
    fields = {'subject', 'target', 'title', 'obligation', 'source'}
    if not isinstance(request, dict) or set(request) != fields:
        raise ValueError(f'Guard requires exactly {sorted(fields)}')
    for name in ('subject', 'title', 'obligation'):
        require_text(request[name], name)
    if request['target'] is not None:
        require_text(request['target'], 'target')
    source = source_record(repo, request['source'])
    payload = {'title': request['title'], 'obligation': request['obligation'], 'source': source}
    key = digest({'format': 'qstore-guard-v1', 'subject': request['subject'],
                  'target': request['target'], 'status': 'open', 'payload': payload})
    with store_session(path) as (session, models):
        for endpoint in (request['subject'], request['target']):
            if endpoint is not None and session.get(models.qstore_versions, endpoint) is None:
                raise ValueError('Guard endpoints must be registered versions')
        if session.get(models.qstore_guards, key) is None:
            session.add(models.qstore_guards(
                guard_hash=key, subject_version=request['subject'],
                target_version=request['target'], status='open', payload_json=canonical(payload)))
            session.add(models.qstore_ledger(event_type='GUARD', payload_json=canonical({'guard_hash': key})))
    return {'guard_hash': key, 'status': 'open'}


def latest_review(session, models, kind, key):
    column = models.qstore_reviews.guard_hash if kind == 'guard' else models.qstore_reviews.relation_hash
    rows = list(session.scalars(select(models.qstore_reviews).where(column == key)))
    predecessors = {row.previous_hash for row in rows}
    heads = [row for row in rows if row.review_hash not in predecessors]
    if len(heads) > 1:
        raise ValueError('Review history has conflicting heads')
    return heads[0] if heads else None


def register_review(path, repo, request):
    fields = {'kind', 'subject', 'previous', 'status', 'reviewer', 'reason', 'evidence'}
    if not isinstance(request, dict) or set(request) != fields:
        raise ValueError(f'Review requires exactly {sorted(fields)}')
    kind = request['kind']
    allowed = {'guard': {'open', 'satisfied', 'failed'},
               'relation': {'proposed', 'declared', 'reviewed', 'rejected'}}
    if kind not in allowed or request['status'] not in allowed[kind]:
        raise ValueError('Invalid review kind or status')
    for name in ('subject', 'reviewer', 'reason'):
        require_text(request[name], name)
    if request['previous'] is not None:
        require_text(request['previous'], 'previous')
    evidence = source_record(repo, request['evidence'])
    payload = {'reviewer': request['reviewer'], 'reason': request['reason'], 'evidence': evidence,
               'assessment': 'declared-human-or-agent-review'}
    identity = {name: request[name] for name in ('kind', 'subject', 'previous', 'status')}
    key = digest({'format': 'qstore-review-v1', **identity, 'payload': payload})
    with store_session(path) as (session, models):
        table = models.qstore_guards if kind == 'guard' else models.qstore_relations
        if session.get(table, request['subject']) is None:
            raise ValueError('Review subject is not registered')
        if session.get(models.qstore_reviews, key) is not None:
            return {'review_hash': key, 'status': request['status']}
        previous = latest_review(session, models, kind, request['subject'])
        expected = previous.review_hash if previous else None
        if request['previous'] != expected:
            raise ValueError('Stale review predecessor; read the current review head')
        session.add(models.qstore_reviews(
            review_hash=key, guard_hash=request['subject'] if kind == 'guard' else None,
            relation_hash=request['subject'] if kind == 'relation' else None,
            previous_hash=expected, status=request['status'], payload_json=canonical(payload)))
        session.add(models.qstore_ledger(event_type='REVIEW', payload_json=canonical({'review_hash': key})))
    return {'review_hash': key, 'status': request['status']}
