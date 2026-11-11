"""Index manuscript statements as unreviewed inventory, separate from QAM evidence."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3


def mask_comments(text):
    """Mask comments without changing offsets or line numbers."""
    chars = list(text)
    index = 0
    while index < len(text):
        if text[index] == '\\':
            index += 2
        elif text[index] == '%':
            end = text.find('\n', index)
            end = len(text) if end < 0 else end
            chars[index:end] = [' '] * (end - index)
            index = end
        else:
            index += 1
    return ''.join(chars)


def collect(repo):
    repo = Path(repo).resolve()
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
        clean = mask_comments(text)
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
            depth = 1
            end = None
            for closing in re.finditer(r'\\(begin|end)\{' + re.escape(kind) + r'\}', clean[match.end():]):
                depth += 1 if closing.group(1) == 'begin' else -1
                if depth == 0:
                    end = match.end() + closing.end()
                    break
            if end is None:
                raise ValueError(f'Unclosed {kind} at {relative}:{line}')
            statement = text[match.start():end]
            claim_key = f'{relative}:{line}:{kind}'
            add(claim_key, key, kind, relative, line, statement, digest)

    visit(entry, None)
    return nodes


def build(repo, database):
    nodes = collect(repo)
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
    files = sum(row[2] == 'file' for row in nodes)
    print(json.dumps({'database': str(database), 'files': files,
                      'statements': len(nodes) - files,
                      'status': 'imported-unreviewed', 'logical_edges': 0}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    args = parser.parse_args()
    build(Path(__file__).resolve().parents[2], args.db)
