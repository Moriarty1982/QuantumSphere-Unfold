"""Register and export the existing local penalty identity and its original proof."""

import argparse
import hashlib
from pathlib import Path
import json

from qam.store.registry import register
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export


def run(database, destination):
    repo = Path(__file__).resolve().parents[2]
    path = repo / 'sources/research/parts/native-operator-link.tex'
    text = path.read_text(encoding='utf-8-sig')
    start = text.index('Write $M=')
    end = text.index(r'\end{proposition}', start)
    statement = text[start:end].strip()
    proof_start = text.index(r'\begin{proof}', end)
    proof_end = text.index(r'\end{proof}', proof_start) + len(r'\end{proof}')
    proof_text = text[proof_start:proof_end]
    provenance = {'path': path.relative_to(repo).as_posix(),
                  'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                  'revision': 'registered-current-source-bytes',
                  'locator': 'v480:native-penalty-identity'}
    assumptions = ['Declared positive-metric bounded or finite realization with orthogonal P and common domains']

    def store(key, kind, payload):
        return register(database, repo, {'object_id': key, 'kind': kind, 'frame': 'native-penalty-local',
                        'status': 'conditional', 'payload': payload, 'source': provenance})['version_hash']

    package = store('native-penalty-proof-package', 'latex-resource', {
        'title': 'Proof environment', 'package': 'amsthm', 'assumptions': []})
    claim = store('native-penalty-identity-statement', 'claim', {
        'title': 'The two minimal penalty terms coincide', 'latex': statement,
        'assumptions': assumptions, 'dependencies': []})
    proof = store('native-penalty-identity-proof', 'proof', {
        'title': 'Original block-matrix proof', 'latex': proof_text,
        'assumptions': assumptions, 'dependencies': [claim, package]})
    transition_path = repo / 'qam/store/penalty_transition.tex'
    register(database, repo, {
        'object_id': 'native-penalty-editorial-transition', 'kind': 'transition',
        'frame': 'native-penalty-local', 'status': 'conditional',
        'source': {'path': transition_path.relative_to(repo).as_posix(),
                   'sha256': hashlib.sha256(transition_path.read_bytes()).hexdigest(),
                   'revision': 'registered-current-source-bytes', 'locator': 'whole file'},
        'payload': {'title': 'Scope of the following proof',
                    'latex': transition_path.read_text(encoding='utf-8').strip(),
                    'assumptions': ['Native physical identification remains open'],
                    'dependencies': [claim], 'placement': {'after': claim, 'before': proof}},
    })
    snapshot = create_snapshot(database, 'native-penalty-original-latex')['snapshot_hash']
    return export(database, snapshot, [proof], destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.db, args.out)))
