"""Register and verify the explicitly declared, source-backed matrix comparison."""

import argparse
import hashlib
import json
from pathlib import Path

from qam.store.registry import register
from qam.store.matrix_check import verify, read_receipt


def run(database):
    repo = Path(__file__).resolve().parents[2]
    source_path = repo / 'qam/store/matrix_example.json'
    raw = source_path.read_bytes()
    example = json.loads(raw)
    source = {'path': source_path.relative_to(repo).as_posix(),
              'sha256': hashlib.sha256(raw).hexdigest(),
              'revision': 'content-addressed-comparison-v1', 'locator': '/definition'}
    definition_request = {
        'object_id': 'store-example-matrix-definition', 'kind': 'definition',
        'frame': example['frame'], 'status': 'conditional',
        'payload': example['definition'], 'source': source,
    }
    definition = register(database, repo, definition_request)['version_hash']
    seeds = {}
    for name, value in example['seeds'].items():
        request = {
            'object_id': 'store-example-' + name, 'kind': 'seed',
            'frame': example['frame'], 'status': 'conditional',
            'payload': {'title': name, 'value': value, 'value_type': 'rational-matrix',
                        'origin': 'Explicit finite comparison in matrix_example.json',
                        'assumptions': [], 'definition_version': definition},
            'source': {**source, 'locator': '/seeds/' + name},
        }
        seeds[name] = register(database, repo, request)['version_hash']
    reports = {}
    for name in ('commuting-transport', 'noncommuting-transport'):
        result = verify(database, {'projector': seeds['projector'], 'transport': seeds[name]})
        saved = read_receipt(database, result['receipt_hash'])
        if saved != result:
            raise ValueError('Stored receipt does not match the executed check')
        reports[name] = {'receipt_hash': result['receipt_hash'], 'result': result['result'],
                         'residuals': result['residuals'], 'guards': result['guards']}
    return {'definition': definition, 'seeds': seeds, 'checks': reports}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    args = parser.parse_args()
    print(json.dumps(run(args.db), ensure_ascii=False, indent=2))
