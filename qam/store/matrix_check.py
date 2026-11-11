"""Exact, bounded checks of registered rational matrix seeds, not native physics."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest, latest_review


CHECKER = 'rational-projector-commutator-v1'
MAX_DIMENSION = 32


def matrix(value):
    if not isinstance(value, list) or not 1 <= len(value) <= MAX_DIMENSION:
        raise ValueError('Matrix requires 1 to 32 rows')
    size = len(value)
    result = []
    for row in value:
        if not isinstance(row, list) or len(row) != size:
            raise ValueError('Matrix must be square and rectangular')
        parsed = []
        for entry in row:
            if type(entry) is int:
                entry = str(entry)
            if not isinstance(entry, str) or len(entry) > 256 or not re.fullmatch(r'[+-]?\d+(?:/[1-9]\d*)?', entry):
                raise ValueError('Entries must be integers or exact rational strings')
            parsed.append(Fraction(entry))
        result.append(parsed)
    return result


def multiply(left, right):
    return [[sum(a * b for a, b in zip(row, column)) for column in zip(*right)] for row in left]


def residual(left, right):
    return [[str(a - b) for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


def load_version(session, models, key, snapshots):
    row = session.get(models.qstore_versions, key)
    if row is None:
        raise ValueError('Input version is not registered')
    obj = session.get(models.qstore_objects, row.object_id)
    payload = json.loads(row.payload_json)
    identity = {'format': 'qstore-version-v1', 'object_id': row.object_id,
                'kind': obj.object_type, 'frame': row.frame, 'status': row.status, 'payload': payload}
    if digest(identity) != key:
        raise ValueError('Input version hash is invalid')
    snapshots[key] = identity
    if row.status == 'withdrawn' or row.frame == 'unspecified':
        raise ValueError('Input needs an explicit frame and nonwithdrawn status')
    return identity


def load_seed(session, models, key, snapshots):
    seed = load_version(session, models, key, snapshots)
    if seed['kind'] != 'seed' or seed['payload']['value_type'] != 'rational-matrix':
        raise ValueError('Expected a rational-matrix seed')
    definition = load_version(session, models, seed['payload']['definition_version'], snapshots)
    if definition['kind'] != 'definition' or definition['frame'] != seed['frame']:
        raise ValueError('Seed definition or frame does not match')
    return seed, matrix(seed['payload']['value'])


def verify(path, request):
    if not isinstance(request, dict) or set(request) not in ({'projector'}, {'projector', 'transport'}):
        raise ValueError('Request requires projector and optional transport version hashes')
    if any(not isinstance(value, str) or not value for value in request.values()):
        raise ValueError('Version hashes must be nonempty strings')
    snapshots = {}
    checks = {}
    result = 'blocked'
    error = None
    with store_session(path) as (session, models):
        try:
            seed, projector = load_seed(session, models, request['projector'], snapshots)
            checks['projector_residual'] = residual(multiply(projector, projector), projector)
            if 'transport' in request:
                other, transport = load_seed(session, models, request['transport'], snapshots)
                if seed['frame'] != other['frame'] or len(projector) != len(transport):
                    raise ValueError('Transport frame and dimension must match projector')
                checks['commutator_residual'] = residual(multiply(transport, projector), multiply(projector, transport))
            result = 'passed' if all(value == '0' for rows in checks.values() for row in rows for value in row) else 'failed'
        except (ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
            error = str(exc)
        guards = [{'version': key, 'assumptions': item['payload'].get('assumptions', [])}
                  for key, item in sorted(snapshots.items()) if item['payload'].get('assumptions')]
        for guard in session.scalars(select(models.qstore_guards).order_by(models.qstore_guards.guard_hash)):
            if guard.subject_version not in snapshots and guard.target_version not in snapshots:
                continue
            review = latest_review(session, models, 'guard', guard.guard_hash)
            status = review.status if review else guard.status
            if status != 'satisfied':
                guards.append({'guard_hash': guard.guard_hash, 'status': status,
                               'review_hash': review.review_hash if review else None,
                               'payload': json.loads(guard.payload_json)})
        sources = {}
        for key in sorted(snapshots):
            rows = session.scalars(select(models.qstore_sources).where(
                models.qstore_sources.version_hash == key).order_by(models.qstore_sources.source_id))
            sources[key] = [{'path': row.source_path, 'sha256': row.source_hash,
                             'revision': row.source_revision, 'locator': row.locator} for row in rows]
        receipt = {'format': 'qstore-check-v1', 'checker': CHECKER,
                   'checker_hash': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   'registry_hash': hashlib.sha256(Path(__file__).with_name('registry.py').read_bytes()).hexdigest(),
                   'python': sys.version, 'request': request, 'inputs': snapshots, 'sources': sources,
                   'result': result, 'residuals': checks, 'error': error, 'guards': guards,
                   'assertion_tested': 'P squared equals P; optionally MP equals PM over rational matrices',
                   'scope': 'Concrete registered entries only; native interpretation and LaTeX binding require separate review'}
        key = digest(receipt)
        if session.get(models.qstore_checks, key) is None:
            session.add(models.qstore_checks(receipt_hash=key, checker=CHECKER,
                        checker_hash=receipt['checker_hash'], result=result, receipt_json=canonical(receipt)))
            session.flush()
            for version in snapshots:
                session.add(models.qstore_check_inputs(receipt_hash=key, version_hash=version))
            session.add(models.qstore_ledger(event_type='VERIFY', payload_json=canonical({'receipt_hash': key})))
    return {'receipt_hash': key, **receipt}


def read_receipt(path, key):
    with store_session(path) as (session, models):
        row = session.get(models.qstore_checks, key)
        if row is None:
            raise ValueError('Unknown verification receipt')
        receipt = json.loads(row.receipt_json)
        if digest(receipt) != key:
            raise ValueError('Verification receipt hash mismatch')
        return {'receipt_hash': key, **receipt}
