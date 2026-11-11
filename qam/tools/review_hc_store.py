"""Export the source-pinned HC identification self-review."""
import argparse
import json
from pathlib import Path
from qam.store.hc_identification_review import apply_review
from qam.store.argument_view import markdown
from qam.store.selection import select_versions
from qam.store.latex_export import export


def run(database, destination):
    repo = Path(__file__).resolve().parents[2]
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    result = apply_review(database, repo)
    result['export'] = export(database, result['snapshot_hash'], result['roots'], destination / 'paper')
    selection = select_versions(database, result['snapshot_hash'], result['roots'] + [p['imported'] for p in result['pairs']])
    (destination / 'argument.md').write_text(markdown(selection), encoding='utf-8')
    (destination / 'review.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    return {'snapshot_hash': result['snapshot_hash'], 'claims': len(result['pairs']), 'native_guards': len(result['native_guards'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.db, args.out)))
