"""Register the bounded Koide-condition subsection as a source-backed argument branch."""

import argparse
import hashlib
import json
from pathlib import Path

from qam.store.registry import register, register_guard
from qam.store.snapshots import create_snapshot
from qam.store.latex_export import export


def run(database, destination):
    repo = Path(__file__).resolve().parents[2]
    path = repo / 'sources/research/parts/koide-and-kernel.tex'
    text = path.read_text(encoding='utf-8-sig')
    provenance = {'path': path.relative_to(repo).as_posix(),
                  'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                  'revision': 'registered-current-source-bytes', 'locator': 'v480:koide-condition'}
    frame = 'koide-principal-root-comparison'

    def store(key, kind, title, latex, dependencies, assumptions):
        return register(database, repo, {'object_id': key, 'kind': kind, 'frame': frame,
            'status': 'conditional', 'source': provenance,
            'payload': {'title': title, 'latex': latex.strip(), 'dependencies': dependencies,
                        'assumptions': assumptions}})['version_hash']

    package = register(database, repo, {'object_id': 'koide-branch-proof-package',
        'kind': 'latex-resource', 'frame': frame, 'status': 'declared', 'source': provenance,
        'payload': {'title': 'Proof environment', 'package': 'amsthm', 'assumptions': []}})['version_hash']
    first = text.index('Let $x_i=')
    begin = text.index(r'\begin{proposition}', first)
    setup = store('koide-branch-root-setup', 'explanation', 'Principal roots and orthogonal decomposition',
                  text[first:begin], [], ['Nonnegative principal roots with nonzero root vector'])
    roots = [setup]
    proofs = []
    for label in ('koide-equal-norm', 'koide-hc-mixing', 'koide-radius-phase', 'koide-equivariant-obstruction'):
        label_at = text.index(r'\label{v480:' + label + '}')
        start = text.rfind(r'\begin{proposition}', 0, label_at)
        body_start = text.index('\n', start) + 1
        end = text.index(r'\end{proposition}', label_at)
        title = text[start:text.index('\n', start)].split('[', 1)[1].rsplit(']', 1)[0]
        claim = store('koide-branch-' + label, 'claim', title, text[body_start:end], [setup], [])
        proof_start = text.index(r'\begin{proof}', end)
        proof_end = text.index(r'\end{proof}', proof_start) + len(r'\end{proof}')
        dependencies = [claim, package]
        if label == 'koide-radius-phase':
            dependencies.append(proofs[0])
        proof = store('koide-branch-' + label + '-proof', 'proof', 'Proof of ' + title,
                      text[proof_start:proof_end], dependencies, [])
        proofs.append(proof)
        roots += [claim, proof]
        next_block = text.index(r'\begin{proposition}', proof_end) if label != 'koide-equivariant-obstruction' else text.index(r'\subsection', proof_end)
        commentary = text[proof_end:next_block].strip()
        if commentary:
            note = store('koide-branch-' + label + '-discussion', 'explanation',
                         'Scope and limitations of ' + title, commentary, [proof],
                         ['Quoted numerical comparisons retain their historical-input status']
                         if label == 'koide-equivariant-obstruction' else [])
            roots.append(note)
        if label in {'koide-equal-norm', 'koide-hc-mixing'}:
            register_guard(database, repo, {'subject': claim, 'target': setup,
                'title': 'Native mass-root mechanism remains open',
                'obligation': 'Derive the native principal-root representation and the required equal-norm or HC orthogonality condition independently of fitted masses.',
                'source': provenance})
    snapshot = create_snapshot(database, 'koide-condition-argument-branch')['snapshot_hash']
    result = export(database, snapshot, roots, destination)
    return {**result, 'roots': roots, 'snapshot_hash': snapshot}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.db, args.out)))
