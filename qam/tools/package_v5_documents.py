"""Package an authenticated English paired-document package without publishing it."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sqlite3
import zipfile


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root, name):
    relative = PurePosixPath(name)
    if relative.is_absolute() or '..' in relative.parts or '\\' in name or ':' in name:
        raise ValueError('Unsafe package path: ' + name)
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Missing or escaped package path: ' + name)
    return path


def package(bundle, output, expected_commit):
    bundle = Path(bundle).resolve()
    output = Path(output).resolve()
    if output.exists() or output.is_relative_to(bundle) or bundle.is_relative_to(output):
        raise ValueError('Use a new output directory outside the input bundle')
    manifest = json.loads((bundle / 'build-manifest.json').read_text(encoding='utf-8'))
    if manifest.get('git_commit') != expected_commit or manifest.get('tracked_changes'):
        raise ValueError('Bundle is not the requested clean source revision')
    if not manifest.get('build_complete') or set(manifest.get('documents', {})) != {'full', 'physics'}:
        raise ValueError('Incomplete paired build')
    release = manifest.get('release', {})
    if release.get('version') != '5.0.0' or release.get('version_doi') != '10.5281/zenodo.24152615':
        raise ValueError('Unexpected release identity')
    verified = {}
    for line in (bundle / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        if name in verified or sha(contained(bundle, name)) != digest:
            raise ValueError('Checksum mismatch or duplicate: ' + name)
        verified[name] = digest
    actual = {p.relative_to(bundle).as_posix() for p in bundle.rglob('*')
              if p.is_file() and p.relative_to(bundle).as_posix() != 'SHA256SUMS.txt'}
    if set(verified) != actual:
        raise ValueError('Bundle checksum manifest does not cover exactly its files')
    for name in ('full', 'physics'):
        doc = manifest['documents'][name]
        if doc.get('package_pdf') != 'Quantum_Sphaera_Companion_v5_0_0_' + name + '.pdf':
            raise ValueError('Unexpected English document filename: ' + name)
        if not doc.get('technical_check_passed') or any(doc.get('findings', {}).values()):
            raise ValueError('Document has unresolved technical findings: ' + name)
        pdf = contained(bundle, doc['package_pdf'])
        if sha(pdf) != doc['pdf_sha256'] or not pdf.read_bytes().startswith(b'%PDF-'):
            raise ValueError('Invalid document PDF: ' + name)
        assembly_path = contained(bundle, 'editions/' + name + '/assembly.json')
        if sha(assembly_path) != doc['assembly_sha256']:
            raise ValueError('Assembly identity mismatch')
        assembly = json.loads(assembly_path.read_text(encoding='utf-8'))
        if assembly['edition_hash'] != doc['edition_hash'] or assembly['snapshot_hash'] != manifest['snapshot_hash']:
            raise ValueError('Edition snapshot mismatch')
        # Independently check the exported source bindings, not only the outer archive.
        from qam.tools.build_v5_documents import verify_export
        verify_export(bundle / 'editions' / name)
    database = contained(bundle, 'qam.sqlite3')
    with sqlite3.connect(database.as_uri() + '?mode=ro', uri=True) as db:
        if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('Database integrity check failed')
        for doc in manifest['documents'].values():
            row = db.execute('SELECT snapshot_hash FROM qstore_editions WHERE edition_hash = ?',
                             (doc['edition_hash'],)).fetchone()
            if row != (manifest['snapshot_hash'],):
                raise ValueError('Database does not contain the documented edition snapshot')
    selected = {}
    for name in sorted(verified):
        # No German reader templates, narrative notes, logs or copied review reports.
        if name in {'editions/physics/paper.tex', 'editions/physics/assembly.json',
                    'editions/full/assembly.json', 'build-manifest.json'}:
            selected[name] = contained(bundle, name)
        elif name.startswith('editions/full/source/') and not name.endswith('.md'):
            selected[name] = contained(bundle, name)
        elif name.startswith('provenance/') and Path(name).suffix in {'.py', '.txt'}:
            selected[name] = contained(bundle, name)
    if any('/de/' in name or name.endswith('.tex.in') for name in selected):
        raise ValueError('Translation material entered the source selection')
    output.mkdir(parents=True)
    for doc in manifest['documents'].values():
        shutil.copyfile(bundle / doc['package_pdf'], output / doc['package_pdf'])
    shutil.copyfile(database, output / 'qam.sqlite3')
    shutil.copyfile(bundle / 'build-manifest.json', output / 'build-manifest.json')
    archive = output / 'Quantum_Sphaera_v5_0_0_english_sources.zip'
    archive_readme = """# English document sources

This is an source-bound v5.0.0 package; publication status is recorded on Zenodo.
Compile the full edition from editions/full/source/sources/research/
with pdflatex -no-shell-escape v480-companion.tex until references settle.
Compile the physics edition from editions/physics/ with the same command
using paper.tex. The exported entrypoints require an installed LaTeX system.

Assembly records retain the original source hashes and open review state.
German narrative review notes are deliberately omitted; their historical
source identities may remain in the manifests. For their originals and
complete database regeneration code, consult the exact repository commit
in build-manifest.json. This archive supports compilation of the exported
documents; its selected provenance scripts are not a complete standalone
installation of the database application. The separate qam.sqlite3 file
preserves the machine-readable source snapshot and assertion records.
There is no German reader edition or translation template in this archive.
"""
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in [('README.md', archive_readme.encode('utf-8'))] + [
                (name, path.read_bytes()) for name, path in sorted(selected.items())]:
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise ValueError('Archive CRC check failed')
        for name, path in selected.items():
            if hashlib.sha256(z.read(name)).hexdigest() != sha(path):
                raise ValueError('Archived source mismatch: ' + name)
    report = {'format': 'qsc-english-payload-v1', 'source_commit': expected_commit,
              'snapshot_hash': manifest['snapshot_hash'], 'documents': manifest['documents'],
              'input_checksums_verified': len(verified), 'source_archive_entries': len(selected) + 1,
              'excluded_narrative_reports': sorted(n for n in verified if n.endswith('.md')),
              'german_reader_included': False, 'publication_ready': False,
              'doi_reserved': True, 'version_doi': '10.5281/zenodo.24152615', 'uploaded': False,
              'database_integrity': 'ok'}
    (output / 'package-manifest.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    (output / 'README.md').write_text(
        '# Quantum Sphaera: English paired-document package\n\n'
        'Two English PDFs, compilable exported sources and the machine-readable database.\n'
        'No German reader edition or German narrative reports are supplied.\n'
        'Reserved version DOI: 10.5281/zenodo.24152615. Package creation does not publish it.\n'
        'The full Companion is the proposed preview. Source and snapshot identities, technical\n'
        'checks and remaining argument-review flags are in the two manifests.\n'
        'Database records and hashes do not prove physical interpretation.\n'
        'Use the existing v4.11.0 public citation until a new version is actually published.\n', encoding='utf-8')
    files = sorted(p for p in output.iterdir() if p.is_file())
    (output / 'SHA256SUMS.txt').write_text(''.join(sha(p) + '  ' + p.name + '\n' for p in files), encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--expected-commit', required=True)
    args = parser.parse_args()
    result = package(args.bundle, args.out, args.expected_commit)
    print(json.dumps({k: result[k] for k in ('source_commit', 'input_checksums_verified',
          'source_archive_entries', 'german_reader_included', 'publication_ready')}))
