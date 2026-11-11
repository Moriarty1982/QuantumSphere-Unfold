"""Reproducibly register the agreed v5 full and physics document assemblies."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import register
from qam.store.manuscript_import import import_manuscript
from qam.store.koide_review import apply_review as koide_review
from qam.store.hc_identification_review import apply_review as hc_review
from qam.store.hc_koide_bridge import apply_review as bridge_review
from qam.store.editions import save_edition, read_edition, export_edition
from qam.store.snapshots import create_snapshot
from qam.tools.store_koide_branch import run as store_koide
from qam.tools.store_example import run as matrix_example


TITLES = [('question', 'Physical question and scope'), ('core', 'Carrier, HC and frames'),
          ('method', 'Reading QAM, MML and MMA'), ('particles', 'Particles and generations'),
          ('masses', 'Masses as a readout test'), ('geometry', 'Dynamics and geometry'),
          ('limits', 'Limits and open physical identifications')]


def configure(database, destination):
    repo = Path(__file__).resolve().parents[2]
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    inventory = import_manuscript(database, repo)
    store_koide(database, destination / 'koide-registration')
    koide = koide_review(database, repo)
    hc = hc_review(database, repo)
    bridge = bridge_review(database, repo)
    matrices = matrix_example(database)
    source_path = 'qam/editions/v5_sections.tex'
    text = (repo / source_path).read_text(encoding='utf-8')
    source = {'path': source_path, 'sha256': hashlib.sha256((repo / source_path).read_bytes()).hexdigest(),
              'revision': 'v5-edition-editorial-v1', 'locator': 'section markers'}
    blocks = dict(re.findall(r'% section:(\w+)\n(.*?)(?=% section:|\Z)', text, re.S))
    sections = []
    for key, title in TITLES:
        note = register(database, repo, {'object_id': 'v5-edition-intro-' + key, 'kind': 'explanation',
            'frame': 'editorial-physics-scope', 'status': 'declared', 'source': source,
            'payload': {'title': title + ': introduction', 'latex': blocks[key].strip(),
                        'assumptions': [], 'dependencies': []}})['version_hash']
        sections.append({'key': key, 'title': title, 'members': [{'version': note, 'use': 'prose'}]})
    by_key = {s['key']: s for s in sections}
    def add(key, versions, use):
        by_key[key]['members'] += [{'version': v, 'use': use} for v in dict.fromkeys(versions)]
    add('method', list(matrices['seeds'].values()), 'argument')
    add('masses', koide['roots'] + hc['roots'] + bridge['roots'], 'argument')
    # Use exact source-pinned raw versions, never a latest-row heuristic.
    raw_files = {}
    with store_session(database) as (session, models):
        rows = list(session.scalars(select(models.qstore_versions)))
        source_rows = list(session.scalars(select(models.qstore_sources)))
        for version in rows:
            payload = json.loads(version.payload_json)
            if not payload.get('inventory'):
                continue
            matching = [s for s in source_rows if s.version_hash == version.version_hash
                        and inventory['source_hashes'].get(s.source_path) == s.source_hash]
            if matching:
                raw_files.setdefault(matching[0].source_path, []).append((version.version_hash, payload))
    wanted = {'core': ['def:biquaternion'], 'particles': ['thm:SM', 'thm:three-generations'],
              'geometry': ['v480:hc-projected-autonomy', 'v490:normal-inverse']}
    for key, labels in wanted.items():
        for label in labels:
            matches = [v for values in raw_files.values() for v, p in values if p['inventory'].get('label') == label]
            if len(matches) != 1:
                raise ValueError('Expected one current statement for ' + label)
            add(key, matches, 'candidate')
    # Pin both the full source tree and the exact editorial/evidence sources.
    source_files = {p.relative_to(repo).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (repo / 'sources/research').rglob('*')
                    if p.is_file() and p.suffix.lower() in {'.tex', '.bib', '.sty', '.pdf', '.png', '.jpg'}}
    source_files[source_path] = source['sha256']
    for path in ('qam/store/matrix_example.json', 'notes/research/koide_store_branch_review_2026_11_11.md',
                 'notes/research/hc_identification_store_review_2026_11_11.md', 'notes/research/hc_koide_bridge_review_2026_11_11.md'):
        source_files[path] = hashlib.sha256((repo / path).read_bytes()).hexdigest()
    snapshot = create_snapshot(database, 'v5-dual-document-assemblies')['snapshot_hash']
    # Importer source order follows the manuscript's literal input traversal.
    # Include files without theorem environments too (preamble, opening, etc.).
    full_sections = [{'key': 'source-' + str(i), 'title': path,
        'members': [{'version': v, 'use': 'candidate'} for v, p in raw_files.get(path, [])]}
        for i, path in enumerate(inventory['source_hashes'])]
    def save(edition_id, title, mode, outline, entrypoint):
        request = {'edition_id': edition_id, 'title': title, 'mode': mode, 'snapshot_hash': snapshot,
                   'sections': outline, 'source_files': source_files, 'entrypoint': entrypoint, 'previous': None}
        with store_session(database) as (session, models):
            rows = list(session.scalars(select(models.qstore_editions).where(models.qstore_editions.edition_id == edition_id)))
            previous = {r.previous_hash for r in rows}
            heads = [r for r in rows if r.edition_hash not in previous]
            if len(heads) > 1:
                raise ValueError('Conflicting edition heads')
            if heads:
                old = json.loads(heads[0].payload_json)
                request['previous'] = old['previous'] if all(old[k] == v for k, v in request.items() if k != 'previous') else heads[0].edition_hash
        return save_edition(database, repo, request)['edition_hash']
    physics = save('qsc-v5-physics', 'Quantum Sphaera Companion v5.0.0-draft: Physics edition', 'selected-arguments', sections, None)
    full = save('qsc-v5-full', 'Quantum Sphaera Companion v5.0.0-draft: Full edition', 'manuscript-source', full_sections,
                'sources/research/v480-companion.tex')
    exports = {name: export_edition(database, repo, key, destination / name) for name, key in [('physics', physics), ('full', full)]}
    result = {'snapshot_hash': snapshot, 'physics': physics, 'full': full, 'exports': exports,
              'physics_sections': len(sections), 'full_statements': sum(len(s['members']) for s in full_sections)}
    (destination / 'editions.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    for name, key in [('physics', physics), ('full', full)]:
        edition = read_edition(database, key)
        lines = ['# ' + edition['title'], '', '| Section | Members | Pending candidates |', '|---|---:|---:|']
        for section in edition['sections']:
            lines.append('| ' + section['title'] + ' | ' + str(len(section['members'])) + ' | ' +
                         str(sum(m['use'] == 'candidate' for m in section['members'])) + ' |')
        (destination / (name + '-outline.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = configure(args.db, args.out)
    print(json.dumps({k: v for k, v in result.items() if k != 'exports'}))
