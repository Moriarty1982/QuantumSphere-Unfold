"""Immutable named paper revisions with a frozen, snapshot-backed selection."""

import hashlib
import json
from pathlib import Path

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest, require_text
from qam.store.selection import select_versions
from qam.store.scrub import scrub
from qam.store.snapshots import read_snapshot
from qam.store.latex_export import export_selection


def save_paper(database, request):
    fields = {'paper_id', 'title', 'snapshot_hash', 'roots', 'profile', 'previous'}
    if not isinstance(request, dict) or set(request) != fields:
        raise ValueError(f'Paper requires exactly {sorted(fields)}')
    for name in ('paper_id', 'title', 'snapshot_hash'):
        require_text(request[name], name)
    if request['profile'] != 'research-draft':
        raise ValueError('Only the research-draft profile is implemented')
    if request['previous'] is not None:
        require_text(request['previous'], 'previous')
    selection = select_versions(database, request['snapshot_hash'], request['roots'])
    check = scrub(selection)
    if check['result'] != 'passed':
        raise ValueError('Paper selection fails technical checks: ' + canonical(check['issues']))
    payload = {'format': 'qstore-paper-v1', **request, 'selection': selection,
               'selection_code_sha256': hashlib.sha256(Path(__file__).with_name('selection.py').read_bytes()).hexdigest()}
    key = digest(payload)
    with store_session(database) as (session, models):
        if session.get(models.qstore_papers, key) is not None:
            return {'paper_hash': key, 'paper_id': request['paper_id'], 'profile': request['profile']}
        rows = list(session.scalars(select(models.qstore_papers).where(
            models.qstore_papers.paper_id == request['paper_id'])))
        previous = {row.previous_hash for row in rows}
        heads = [row.paper_hash for row in rows if row.paper_hash not in previous]
        expected = heads[0] if len(heads) == 1 else None
        if len(heads) > 1 or request['previous'] != expected:
            raise ValueError('Paper predecessor is stale or belongs to another paper')
        session.add(models.qstore_papers(paper_hash=key, paper_id=request['paper_id'],
                    snapshot_hash=request['snapshot_hash'], previous_hash=expected, payload_json=canonical(payload)))
        session.add(models.qstore_ledger(event_type='PAPER', payload_json=canonical({'paper_hash': key})))
    return {'paper_hash': key, 'paper_id': request['paper_id'], 'profile': request['profile']}


def read_paper(database, key):
    with store_session(database) as (session, models):
        row = session.get(models.qstore_papers, key)
        if row is None:
            raise ValueError('Unknown paper version')
        payload = json.loads(row.payload_json)
        if digest(payload) != key or (row.paper_id, row.snapshot_hash, row.previous_hash) != (
                payload['paper_id'], payload['snapshot_hash'], payload['previous']):
            raise ValueError('Paper version integrity check failed')
    read_snapshot(database, payload['snapshot_hash'])
    selection = payload['selection']
    content = {name: value for name, value in selection.items() if name != 'selection_hash'}
    if digest(content) != selection['selection_hash']:
        raise ValueError('Frozen paper selection hash mismatch')
    return {'paper_hash': key, **payload}


def export_paper(database, key, destination):
    paper = read_paper(database, key)
    return export_selection(paper['selection'], destination,
        paper={'paper_hash': key, 'paper_id': paper['paper_id'], 'title': paper['title'], 'profile': paper['profile']})
