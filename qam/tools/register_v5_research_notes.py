"""Register selected research notes and open obligations in the draft store."""
import hashlib
import json

from qam.store.registry import register, register_guard

CATALOGUE = 'qam/editions/v5_research_notes.json'


def register_research_notes(database, repo):
    catalogue = (repo / CATALOGUE).read_bytes()
    entries = json.loads(catalogue)
    if len({entry['id'] for entry in entries}) != len(entries):
        raise ValueError('Research note IDs must be unique')
    sources = {CATALOGUE: hashlib.sha256(catalogue).hexdigest()}
    requests = []
    for entry in entries:
        path = entry['path']
        note = (repo / path).resolve()
        note.relative_to(repo.resolve())
        raw = note.read_bytes()
        excerpt = entry['excerpt']
        contents = raw.decode('utf-8-sig').replace('\r\n', '\n')
        if contents.count(excerpt) != 1:
            raise ValueError('Expected one verbatim research excerpt in ' + path)
        sources[path] = hashlib.sha256(raw).hexdigest()
        requests.append((entry, {'path': path, 'sha256': sources[path],
                                 'revision': 'v5-research-note-import-v1',
                                 'locator': 'verbatim excerpt listed in ' + CATALOGUE}))
    records = {}
    for entry, source in requests:
        version = register(database, repo, {
            'object_id': entry['id'], 'kind': 'claim', 'frame': 'unspecified',
            'status': 'imported-unreviewed', 'source': source,
            'payload': {'title': entry['title'], 'latex': entry['excerpt'],
                        'assumptions': entry['assumptions'], 'dependencies': []},
        })['version_hash']
        guard = register_guard(database, repo, {
            'subject': version, 'target': None, 'title': entry['guard'],
            'obligation': entry['obligation'], 'source': source,
        })
        records[entry['id']] = {'version_hash': version, 'open_guard': guard['guard_hash']}
    return records, sources
