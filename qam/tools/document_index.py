"""Index complete TeX sources and their literal navigation commands by document."""
import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from contextlib import closing
import hashlib
import json
from pathlib import Path
import re
import sqlite3

from qam.tools.manuscript_inventory import ENTRYPOINTS, balanced, collect, store_inventory
COMMAND = re.compile(r'\\([A-Za-z@]+|[^\n])\*?')
NON_LITERAL = re.compile(
    r'(?P<comment>%[^\r\n]*)'
    r'|(?P<verbatim>\\begin\{(verbatim\*?|Verbatim|lstlisting|minted)\}.*?\\end\{\3\}'
    r'|\\verb\*?([^a-zA-Z\s])(?:(?!\4)[^\n])*\4)'
    r'|\\[^\n]', re.S
)
LABELS = {'label': 'label', 'hypertarget': 'anchor', 'bibitem': 'citation'}
REFERENCES = {
    'ref', 'eqref', 'autoref', 'pageref', 'nameref', 'cref', 'Cref', 'vref',
    'Vref', 'hyperref', 'cpageref', 'Cpageref', 'crefrange', 'Crefrange',
    'labelcref', 'labelcpageref',
}
CITATIONS = {'cite', 'citep', 'citet', 'citealp', 'citeauthor', 'citeyear',
             'parencite', 'textcite', 'autocite', 'footcite', 'nocite'}
FILES = {'input', 'include', 'includegraphics', 'safegraphic', 'bibliography',
         'addbibresource', 'externaldocument', 'lstinputlisting', 'inputminted'}
EXTERNAL = {'href', 'url', 'nolinkurl', 'hyperlink', 'doi'}


def blank(match):
    return re.sub(r'[^\r\n]', ' ', match.group()) if match.lastgroup else match.group()


def arguments(clean, offset, opening, limit):
    values = []
    for _ in range(limit):
        while offset < len(clean) and clean[offset].isspace():
            offset += 1
        if offset >= len(clean) or clean[offset] != opening:
            break
        if opening == '{':
            end = balanced(clean, offset)
        else:
            match = re.match(r'\[(?:\\.|[^\]\\{}]|\{[^{}]*\})*\]', clean[offset:])
            end = offset + match.end() if match else None
        if end is None:
            break
        values.append(clean[offset + 1:end - 1].strip())
        offset = end
    return values, offset


def occurrences(raw):
    clean = NON_LITERAL.sub(blank, raw.decode('utf-8-sig'))
    breaks = [m.start() for m in re.finditer('\n', clean)]
    for match in COMMAND.finditer(clean):
        command = match[1]
        if command not in LABELS and command not in REFERENCES | CITATIONS | FILES | EXTERNAL:
            continue
        optional, end = arguments(clean, match.end(), '[', 2)
        groups, _ = arguments(clean, end, '{', 2 if command.endswith('range') or command == 'inputminted' else 1)
        if command == 'hyperref' and optional:
            pairs = [('label', optional[0])]
        elif command == 'hyperref':
            pairs = [('external', groups[0])] if groups else []
        elif not groups and command in {'input', 'include'}:
            bare = re.match(r'\s*([^\s\\{}%]+)', clean[end:])
            pairs = [('file', bare[1])] if bare else []
        elif not groups:
            continue
        elif command in LABELS:
            pairs = [(LABELS[command], groups[0])]
        elif command == 'hyperlink':
            pairs = [('anchor', groups[0])]
        elif command in EXTERNAL:
            pairs = [('external', groups[0])]
        else:
            kind = 'label' if command in REFERENCES else 'citation' if command in CITATIONS else 'file'
            selected = groups[-1:] if command == 'inputminted' else groups
            pairs = [(kind, value.strip()) for group in selected for value in group.split(',')]
        for number, (kind, target) in enumerate(pairs):
            yield (match.start(), bisect_right(breaks, match.start()) + 1, number,
                   match.group()[1:], kind, target)


def file_target(repo, base, source, command, target):
    suffixes = {
        'input': ('.tex',), 'include': ('.tex',), 'externaldocument': ('.aux',),
        'includegraphics': ('.pdf', '.png', '.jpg', '.jpeg', '.eps'),
        'safegraphic': ('.pdf', '.png', '.jpg', '.jpeg', '.eps'),
        'bibliography': ('.bib',), 'addbibresource': ('.bib',),
    }
    name = Path(target)
    names = (name,) if name.suffix else (name, *(Path(target + ext) for ext in suffixes.get(command, ())))
    for folder in (base, source.parent):
        for candidate in names:
            resolved = (folder / candidate).resolve()
            if resolved.is_relative_to(repo) and resolved.is_file():
                return resolved.relative_to(repo).as_posix()
    return None


def build_index(repo, database, physics=None):
    repo = Path(repo).resolve()
    documents = {}
    inventory = []
    for name, entry in ENTRYPOINTS.items():
        nodes = collect(repo, entry)
        inventory.extend(nodes)
        documents[name] = (repo / entry, {row[3]: repo / row[3] for row in nodes if row[2] == 'file'})
    if physics is not None:
        physics = Path(physics).resolve()
        documents['physics'] = (physics, {'editions/physics/paper.tex': physics})
    sources, targets, links = [], [], []
    summary = {}
    for document, (entry, paths) in documents.items():
        definitions = defaultdict(list)
        discovered = []
        hashes = {}
        for name, path in sorted(paths.items()):
            raw = path.read_bytes()
            sha = hashlib.sha256(raw).hexdigest()
            hashes[name] = sha
            sources.append((document, name, sha, raw))
            for offset, line, index, command, kind, target in occurrences(raw):
                if command.rstrip('*') in LABELS:
                    definitions[(kind, target)].append((name, line))
                    targets.append((document, name, offset, line, kind, target))
                else:
                    discovered.append((name, path, offset, line, index, command, kind, target))
        counts = Counter()
        for name, path, offset, line, index, command, kind, target in discovered:
            destination, destination_line = None, None
            if not target or '#' in target and kind != 'external':
                status = 'dynamic'
            elif kind == 'external':
                status = 'literal'
            elif kind == 'file':
                destination = file_target(repo, entry.parent, path, command.rstrip('*'), target)
                status = 'resolved' if destination else 'unresolved'
            elif target == '*' and kind == 'citation':
                status = 'all'
            else:
                matches = definitions[(kind, target)]
                status = 'resolved' if len(matches) == 1 else 'ambiguous' if matches else 'unresolved'
                if len(matches) == 1:
                    destination, destination_line = matches[0]
            counts[status] += 1
            links.append((document, name, offset, line, index, command, kind, target, status,
                          destination, destination_line))
        summary[document] = {'source_files': hashes, 'targets': sum(map(len, definitions.values())),
                             'references': dict(sorted(counts.items()))}
    database = Path(database)
    database.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(database)) as db, db:
        db.execute('''CREATE TABLE IF NOT EXISTS document_sources (
            document TEXT, source TEXT, sha256 TEXT, content BLOB,
            PRIMARY KEY (document, source))''')
        db.execute('''CREATE TABLE IF NOT EXISTS document_targets (
            document TEXT, source TEXT, offset INTEGER, line INTEGER, kind TEXT, target TEXT,
            PRIMARY KEY (document, source, offset))''')
        db.execute('''CREATE TABLE IF NOT EXISTS document_links (
            document TEXT, source TEXT, offset INTEGER, line INTEGER, occurrence INTEGER,
            command TEXT, kind TEXT, target TEXT, status TEXT, target_source TEXT, target_line INTEGER,
            PRIMARY KEY (document, source, offset, occurrence))''')
        db.execute('CREATE INDEX IF NOT EXISTS document_links_lookup ON document_links(document, kind, target)')
        db.execute('CREATE INDEX IF NOT EXISTS document_targets_lookup ON document_targets(document, kind, target)')
        store_inventory(db, inventory)
        db.execute('DELETE FROM document_links')
        db.execute('DELETE FROM document_targets')
        db.execute('DELETE FROM document_sources')
        db.executemany('INSERT INTO document_sources VALUES (?,?,?,?)', sources)
        db.executemany('INSERT INTO document_targets VALUES (?,?,?,?,?,?)', targets)
        db.executemany('INSERT INTO document_links VALUES (?,?,?,?,?,?,?,?,?,?,?)', links)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('build/qam.sqlite3'))
    parser.add_argument('--physics', type=Path, help='Exact generated physics LaTeX entrypoint')
    args = parser.parse_args()
    print(json.dumps(build_index(Path(__file__).resolve().parents[2], args.db, args.physics),
                     indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
