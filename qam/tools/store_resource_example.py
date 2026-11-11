"""Export existing manuscript macro and bibliography resources in a small example."""

import argparse
import hashlib
import json
from pathlib import Path

from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export


def run(database, destination):
    repo = Path(__file__).resolve().parents[2]

    def store(key, kind, path, locator, payload):
        return register(database, repo, {
            'object_id': key, 'kind': kind, 'frame': 'resource-export-comparison', 'status': 'conditional',
            'payload': payload, 'source': {'path': path.relative_to(repo).as_posix(),
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                'revision': 'registered-current-source-bytes', 'locator': locator}})['version_hash']

    preamble = repo / 'sources/research/parts/working-preamble.tex'
    macro = next(line for line in preamble.read_text(encoding='utf-8-sig').splitlines()
                 if line.startswith(r'\newcommand{\workingversion}'))
    macro_hash = store('example-workingversion-macro', 'latex-resource', preamble, 'workingversion', {
        'title': 'Working version macro', 'resource_type': 'macro', 'name': 'workingversion',
        'latex': macro, 'assumptions': [], 'dependencies': []})
    bibliography = repo / 'sources/research/parts/v470/28_bibliography.tex'
    text = bibliography.read_text(encoding='utf-8-sig')
    start = text.index(r'\bibitem{Edwards1974}')
    entry = text[start:text.index(r'\bibitem{', start + 1)].strip()
    entry_hash = store('example-edwards-bibliography', 'latex-resource', bibliography, 'Edwards1974', {
        'title': 'Edwards bibliography entry', 'resource_type': 'bibliography', 'key': 'Edwards1974',
        'latex': entry, 'assumptions': [], 'dependencies': []})
    source = repo / 'qam/store/resource_example.tex'
    block = store('example-resource-excerpt', 'explanation', source, 'whole file', {
        'title': 'Versioned macro and literature export', 'latex': source.read_text(encoding='utf-8').strip(),
        'assumptions': ['This excerpt is a document-assembly example'],
        'dependencies': [macro_hash, entry_hash]})
    snapshot = create_snapshot(database, 'macro-literature-example')['snapshot_hash']
    return export(database, snapshot, [block], destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.db, args.out)))
