"""Bulk registration of the literal active manuscript inventory as unreviewed objects."""

from collections import Counter
from bisect import bisect_right
import hashlib
from pathlib import Path
import re
import json

from sqlalchemy import insert, select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest
from qam.tools.manuscript_inventory import collect, mask_comments


THEMES = {
    'qam': ('QAM, Sprache und Speicher', ('qam', 'kernel', 'computational', 'machine')),
    'mass': ('Massen, Generationen und Mischung', ('koide', 'mass', 'generation', 'mixing', 'flavour')),
    'op': ('OP1–OP5 und Schließungsfragen', ('op1', 'op2', 'op3', 'op4', 'op5', 'op~', 'closure', 'solve', 'endpoint')),
    'geometry': ('Geometrie und Transport', ('teich', 'hopf', 'geometry', 'geometric', 'transport', 'shell')),
    'gravity': ('Gravitation und Kosmologie', ('gravity', 'gravit', 'einstein', 'cosmolog', 'vacuum', 'horizon')),
    'algebra': ('Algebra, Operatoren und Symmetrien', ('algebra', 'operator', 'projector', 'compensator', 'spectral')),
    'dynamics': ('Dynamik und Feldgleichungen', ('action', 'dynamics', 'field', 'cartan', 'dirac', 'yang')),
    'readout': ('Physikalische Auslesungen und Frames', ('readout', 'physical', 'frame', 'observer')),
    'review': ('Übergreifend oder noch zuzuordnen', ()),
}


def proposed_theme(source, title, heading=''):
    # Organizational heuristic only; no semantic claim or proof dependency.
    for text in ((title + ' ' + heading).lower(), Path(source).stem.lower()):
        match = next((key for key, (_, words) in THEMES.items() if any(word in text for word in words)), None)
        if match:
            return match
    return 'review'


def import_manuscript(database, repo):
    repo = Path(repo).resolve()
    nodes = collect(repo)
    source_hashes = {row[3]: row[6] for row in nodes}
    importer_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    collector_hash = hashlib.sha256(Path(__file__).parents[1].joinpath('tools/manuscript_inventory.py').read_bytes()).hexdigest()
    generation = digest({'format': 'literal-import-v1', 'sources': source_hashes,
                         'importer_sha256': importer_hash, 'collector_sha256': collector_hash})
    headings = {}
    for source in source_hashes:
        text = mask_comments((repo / source).read_text(encoding='utf-8-sig'))
        headings[source] = [(text.count('\n', 0, match.start()) + 1, match.group(1))
                            for match in re.finditer(r'\\(?:sub)*section\*?\{([^{}\n]+)\}', text)]
    versions = {}
    objects = {}
    sources = {}
    relations = {}
    guards = {}
    counts = Counter()
    topic_counts = Counter()
    unlabelled = 0
    duplicate_labels = 0

    def add(object_id, kind, payload, source, line):
        identity = {'format': 'qstore-version-v1', 'object_id': object_id, 'kind': kind,
                    'frame': 'unspecified', 'status': 'imported-unreviewed', 'payload': payload}
        key = digest(identity)
        objects[object_id] = {'object_id': object_id, 'object_type': kind}
        versions[key] = {'version_hash': key, 'object_id': object_id, 'payload_json': canonical(payload),
                         'status': 'imported-unreviewed', 'frame': 'unspecified'}
        provenance = {'version_hash': key, 'source_path': source, 'source_hash': source_hashes[source],
                      'source_revision': 'inventory-current-source-bytes', 'locator': f'line {line}'}
        sources[tuple(provenance.values())] = provenance
        return key

    def relation(source, target, kind, status, description):
        payload = {'description': description}
        key = digest({'source': source, 'target': target, 'kind': kind, 'status': status, 'payload': payload})
        relations[key] = {'relation_hash': key, 'source_version': source, 'target_version': target,
                          'relation_type': kind, 'status': status, 'payload_json': canonical(payload)}

    entry = nodes[0][3]
    root = add('manuscript:inventory', 'topic', {'title': 'Companion statement inventory',
               'scope': 'Literal environments in the active input chain; semantic and historical status require review',
               'generation': generation}, entry, 1)
    topics = {}
    for key, (title, _) in THEMES.items():
        topics[key] = add('manuscript:theme:' + key, 'topic',
                          {'title': title, 'scope': 'Proposed organizational grouping', 'generation': generation}, entry, 1)
        relation(root, topics[key], 'contains', 'declared', 'Inventory topic container')
    files = {}
    ordinal = Counter()
    labels_seen = Counter()
    for node_id, parent_id, environment, source, line, statement, _, _, _, _ in nodes:
        if environment == 'file':
            key = add('manuscript:file:' + source, 'topic',
                      {'title': source, 'scope': 'Source document container', 'generation': generation}, source, 1)
            files[node_id] = key
            relation(files.get(parent_id, root), key, 'contains', 'declared', 'Literal document inclusion')
            continue
        counts[environment] += 1
        clean = mask_comments(statement)
        label_match = re.search(r'\\label\{([^{}]+)\}', clean)
        title_match = re.match(r'\\begin\{[^{}]+\}(?:\[([^\]]*)\])?', clean)
        title = title_match.group(1) if title_match and title_match.group(1) else f'{environment} at {source}:{line}'
        ordinal[(source, environment)] += 1
        if label_match:
            label = label_match.group(1).strip()
            labels_seen[(source, label)] += 1
            occurrence = labels_seen[(source, label)]
            object_id = 'manuscript:' + source + ':label:' + label
            if occurrence > 1:
                duplicate_labels += 1
                object_id += ':occurrence:' + str(occurrence)
        else:
            unlabelled += 1
            label = None
            object_id = f'manuscript:{source}:unlabelled:{environment}:{ordinal[(source, environment)]}'
        kind = 'definition' if environment == 'definition' else 'assumption' if environment in {'assumption', 'axiom'} else 'claim'
        metadata = {'environment': environment, 'label': label,
                    'registration': 'literal-import-v1', 'status_review': 'pending'}
        if kind == 'definition':
            payload = {'title': title, 'body': statement, 'scope': 'Imported definition; interpretation pending',
                       'assumptions': [], 'inventory': metadata}
        else:
            payload = {'title': title, 'latex': statement, 'assumptions': [], 'dependencies': [], 'inventory': metadata}
        key = add(object_id, kind, payload, source, line)
        relation(files[parent_id], key, 'contains', 'declared', 'Literal environment occurrence')
        section_index = bisect_right([item[0] for item in headings[source]], line) - 1
        heading = headings[source][section_index][1] if section_index >= 0 else ''
        theme = proposed_theme(source, title_match.group(1) if title_match and title_match.group(1) else '', heading)
        topic_counts[theme] += 1
        relation(key, topics[theme], 'belongs-to', 'proposed', 'Filename/title/section heuristic; thematic review pending')
        guard_payload = {'title': 'Imported statement awaits interpretation and dependency review',
                         'obligation': 'Determine current historical status, frame and interpretation, actual premises, proof association and LaTeX resources; assess whether a native physical bridge is required.',
                         'source': {'path': source, 'sha256': source_hashes[source],
                                    'revision': 'inventory-current-source-bytes', 'locator': f'line {line}'}}
        guard_key = digest({'format': 'qstore-guard-v1', 'subject': key, 'target': None,
                            'status': 'open', 'payload': guard_payload})
        guards[guard_key] = {'guard_hash': guard_key, 'subject_version': key, 'target_version': None,
                             'status': 'open', 'payload_json': canonical(guard_payload)}
    # Check every observed source again before committing the prepared batch.
    for source, expected in source_hashes.items():
        if hashlib.sha256((repo / source).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Source changed during inventory collection: {source}')
    new_counts = {}
    with store_session(database) as (session, models):
        def write(name, rows, keys):
            table = getattr(models, name).__table__
            existing = {tuple(row) for row in session.execute(select(*(table.c[key] for key in keys)))}
            pending = [row for row in rows if tuple(row[key] for key in keys) not in existing]
            if pending:
                session.execute(insert(table), pending)
            new_counts[name] = len(pending)

        for row in session.scalars(select(models.qstore_objects)):
            if row.object_id in objects and row.object_type != objects[row.object_id]['object_type']:
                raise ValueError('Imported identity conflicts with existing object type')
        write('qstore_objects', objects.values(), ['object_id'])
        write('qstore_versions', versions.values(), ['version_hash'])
        write('qstore_sources', sources.values(), ['version_hash', 'source_path', 'source_hash', 'source_revision', 'locator'])
        write('qstore_relations', relations.values(), ['relation_hash'])
        write('qstore_guards', guards.values(), ['guard_hash'])
        report = {'format': 'qstore-manuscript-import-v1', 'root_version': root,
                  'generation': generation, 'files': len(files), 'statements': sum(counts.values()), 'environments': dict(counts),
                  'importer_sha256': importer_hash, 'collector_sha256': collector_hash,
                  'topics': {key: {'title': THEMES[key][0], 'count': topic_counts[key]} for key in THEMES},
                  'unlabelled_statements': unlabelled, 'duplicate_labels': duplicate_labels,
                  'new_rows': new_counts, 'source_hashes': source_hashes,
                  'scope': 'Literal environments before TeX expansion, including historical/archive material; '
                           'free prose, proof association and semantic dependencies remain to be reviewed'}
        if any(new_counts.values()):
            session.add(models.qstore_ledger(event_type='MANUSCRIPT_IMPORT', payload_json=canonical(report)))
    return report


def overview(report):
    lines = ['# Gesamtinventar des Companions', '',
             f'{report["statements"]} Aussageumgebungen aus {report["files"]} eingebundenen Dateien.', '',
             'Alle Einträge sind ungeprüft importiert. Frames und fachliche Abhängigkeiten bleiben offen. '
             'Themenzuordnungen sind Vorschläge nach Dateiname, Überschrift und Abschnitt. Dokumentkanten bedeuten Zugehörigkeit.', '',
             '| Vorgeschlagener Bereich | Aussagen |', '|---|---|']
    for topic in report['topics'].values():
        lines.append(f'| {topic["title"]} | {topic["count"]} |')
    lines += ['', '## Erkannte Aussageformen', '']
    lines.extend(f'- {kind} — {count}' for kind, count in report['environments'].items())
    lines += ['', '## Offene Erfassung', '',
              '- Proof-Zuordnung, Makros, Literatur, Frames und tatsächliche Voraussetzungen.',
              '- Statuskorrekturen und Rücknahmen gegenüber historischer Satzsprache.',
              '- Aussagen im freien Fließtext und TeX-Makroexpansion.',
              f'- {report["unlabelled_statements"]} Umgebungen ohne Label verwenden eine vorläufige Positionsidentität.',
              f'- {report["duplicate_labels"]} weitere Vorkommen doppelter Labels wurden getrennt registriert.', '',
              'Die zusätzlich angelegten offenen Prüfpflichten behaupten keine Widerlegung der importierten Aussagen.', '']
    return '\n'.join(lines)


def overview_from_snapshot(database, snapshot_hash, root_version):
    """Reconstruct the organizational inventory from stored document edges."""
    from qam.store.snapshots import read_snapshot

    snapshot = read_snapshot(database, snapshot_hash)
    tables = snapshot['tables']
    versions = {row['version_hash']: row for row in tables['qstore_versions']}
    if root_version not in versions or versions[root_version]['object_id'] != 'manuscript:inventory':
        raise ValueError('Expected a registered manuscript inventory root in this snapshot')
    children = {}
    for row in tables['qstore_relations']:
        if row['relation_type'] == 'contains' and row['status'] == 'declared':
            children.setdefault(row['source_version'], []).append(row['target_version'])
    reached = set()
    pending = [root_version]
    while pending:
        key = pending.pop()
        if key not in reached:
            reached.add(key)
            pending.extend(children.get(key, []))
    payloads = {key: json.loads(versions[key]['payload_json']) for key in reached}
    statements = {key for key, payload in payloads.items() if payload.get('inventory', {}).get('registration') == 'literal-import-v1'}
    files = {key for key in reached if versions[key]['object_id'].startswith('manuscript:file:')}
    topics = {}
    theme_keys = {}
    for key in reached:
        object_id = versions[key]['object_id']
        if object_id.startswith('manuscript:theme:'):
            theme = object_id.rsplit(':', 1)[1]
            topics[theme] = {'title': payloads[key]['title'], 'count': 0}
            theme_keys[key] = theme
    for row in tables['qstore_relations']:
        if row['relation_type'] == 'belongs-to' and row['source_version'] in statements and row['target_version'] in theme_keys:
            topics[theme_keys[row['target_version']]]['count'] += 1
    counts = Counter(payloads[key]['inventory']['environment'] for key in statements)
    report = {'files': len(files), 'statements': len(statements), 'environments': dict(sorted(counts.items())),
              'topics': dict(sorted(topics.items())),
              'unlabelled_statements': sum(payloads[key]['inventory']['label'] is None for key in statements),
              'duplicate_labels': sum(':occurrence:' in versions[key]['object_id'] for key in statements)}
    text = overview(report)
    text += '\nSnapshot `' + snapshot_hash + '`\n\nRoot `' + root_version + '`\n'
    text += '\n## Quellenübersicht\n\n| Datei | Aussageumgebungen |\n|---|---|\n'
    for key in sorted(files, key=lambda item: payloads[item]['title']):
        count = sum(child in statements for child in children.get(key, []))
        text += '| ' + payloads[key]['title'].replace('|', '&#124;') + ' | ' + str(count) + ' |\n'
    return text
