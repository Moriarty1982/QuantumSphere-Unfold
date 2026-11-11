"""Apply the source-pinned Koide self-review and emit its argument view and draft."""

import argparse
import json
from pathlib import Path

from qam.store.argument_view import markdown
from qam.store.koide_review import apply_review
from qam.store.latex_export import export
from qam.store.selection import select_versions


def run(database, destination):
    repo = Path(__file__).resolve().parents[2]
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    review = apply_review(database, repo)
    review['export'] = export(database, review['snapshot_hash'], review['roots'], destination / 'paper')
    graph_roots = review['roots'] + [pair['imported'] for pair in review['pairs']]
    selection = select_versions(database, review['snapshot_hash'], graph_roots)
    (destination / 'argument.md').write_text(markdown(selection), encoding='utf-8')
    (destination / 'review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2), encoding='utf-8')
    return review


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.db, args.out), ensure_ascii=False))
