"""Index manuscript statements as unreviewed inventory, separate from QAM evidence."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3


def build(repo, database):
    root = repo / 'sources/research'
    entry = root / 'v480-companion.tex'
    nodes = []
    seen = set()

    def add(key, parent, kind, source, line, text, digest):
        nodes.append((key, parent, kind, source, line, text, digest,
                      'imported-unreviewed', 'unspecified',
                      'Native interpretation and logical dependencies require review'))

    def visit(path, parent):
        path = path.resolve()
        if path in seen:
            return
        seen.add(path)
        relative = path.relative_to(repo).as_posix()
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        digest = hashlib.sha256(raw).hexdigest()
        key = 'file:' + relative
        add(key, parent, 'file', relative, 1, relative, digest)
        # Strip LaTeX comments before detecting declarations and includes.
        clean = re.sub(r'(?<!\\)%[^\n]*', '', text)
        events = re.compile(
            r'\\(?:input|include)\{([^}]+)\}|'
            r'\\begin\{(theorem|lemma|proposition|corollary|definition|assumption|axiom|conjecture)\}'
            r'(?:\[([^\]]*)\])?')
        for match in events.finditer(clean):
            line = clean.count('\n', 0, match.start()) + 1
            if match.group(1):
                name = match.group(1)
                candidates = [root / name, path.parent / name]
                candidates = [p if p.suffix else p.with_suffix('.tex') for p in candidates]
                target = next((p for p in candidates if p.is_file()), None)
                if target is None:
                    raise ValueError(f'Unresolved include {name} in {relative}:{line}')
                visit(target, key)
                continue
            kind = match.group(2)
            end = clean.find('\\end{' + kind + '}', match.end())
            if end < 0:
                raise ValueError(f'Unclosed {kind} at {relative}:{line}')
            statement = clean[match.start():end + len('\\end{' + kind + '}')]
            claim_key = f'{relative}:{line}:{kind}'
            add(claim_key, key, kind, relative, line, statement, digest)

    visit(entry, None)
    database.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database) as db:
        db.execute('''CREATE TABLE IF NOT EXISTS manuscript_inventory (
            node_id TEXT PRIMARY KEY, parent_id TEXT, kind TEXT, source TEXT,
            line INTEGER, statement TEXT, source_sha256 TEXT, status TEXT,
            frame TEXT, missing_bridge TEXT)''')
        db.execute('DELETE FROM manuscript_inventory')
        db.executemany('INSERT INTO manuscript_inventory VALUES (?,?,?,?,?,?,?,?,?,?)', nodes)
        count = db.execute('SELECT count(*) FROM manuscript_inventory').fetchone()[0]
        assert count == len(nodes)
    print(json.dumps({'database': str(database), 'files': len(seen),
                      'statements': len(nodes) - len(seen),
                      'status': 'imported-unreviewed', 'logical_edges': 0}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    args = parser.parse_args()
    build(Path(__file__).resolve().parents[2], args.db)
