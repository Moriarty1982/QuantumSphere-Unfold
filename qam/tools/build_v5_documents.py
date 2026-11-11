"""Build both pinned v5 document editions as one auditable draft package."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from qam.tools.configure_v5_editions import configure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_export(root):
    root = Path(root).resolve()
    manifest = json.loads((root / 'assembly.json').read_text(encoding='utf-8'))
    for name, expected in manifest['files'].items():
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file() or digest(path) != expected:
            raise ValueError('Export file missing or changed: ' + name)
    entry = (root / manifest['entrypoint_export']).resolve()
    if not entry.is_relative_to(root) or not entry.is_file():
        raise ValueError('Invalid exported entrypoint')
    return manifest, entry


def log_findings(text):
    return {
        'undefined_references': len(re.findall(r'(?:Reference|Citation)\s+[^\n]*?undefined|There were undefined (?:references|citations)', text)),
        'multiply_defined_labels': len(re.findall(r'multiply[- ]defined|multiply defined', text)),
        'rerun_requests': len(re.findall(r'Rerun to get|Please rerun|Rerun to get /PageLabels', text)),
        'overfull_boxes': len(re.findall(r'Overfull \\[hv]box', text)),
    }


def compile_document(entry, output):
    output.mkdir(parents=True, exist_ok=False)
    command = ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
               '-halt-on-error', '-file-line-error', '-output-directory=' + str(output), entry.name]
    previous = None
    with (output / 'compiler-output.txt').open('wb') as stream:
        for passes in range(1, 7):
            result = subprocess.run(command, cwd=entry.parent, stdout=stream,
                                    stderr=subprocess.STDOUT, timeout=7200, check=False)
            if result.returncode:
                break
            state = {p.name: digest(p) for p in output.iterdir() if p.suffix in {'.aux', '.toc', '.out'}}
            if passes >= 2 and state == previous:
                break
            previous = state
    pdf = output / (entry.stem + '.pdf')
    log = output / (entry.stem + '.log')
    findings = log_findings(log.read_text(encoding='utf-8', errors='replace')) if log.exists() else None
    valid_pdf = pdf.is_file() and pdf.stat().st_size > 5 and pdf.read_bytes().startswith(b'%PDF-')
    passed = result.returncode == 0 and valid_pdf and findings is not None and not any(
        findings[k] for k in ('undefined_references', 'multiply_defined_labels', 'rerun_requests'))
    return {'returncode': result.returncode, 'passes': passes, 'pdf_present': valid_pdf,
            'technical_check_passed': passed, 'findings': findings}, pdf


def finalize_package(output, result):
    """Never identify one successful document as a complete two-document build."""
    output = Path(output)
    documents = result.get('documents', {})
    result['build_complete'] = (not result.get('error') and set(documents) == {'full', 'physics'} and
        all(d.get('technical_check_passed') and (output / d.get('package_pdf', '')).is_file()
            for d in documents.values()))
    result['publication_ready'] = False
    result['status'] = 'draft-built' if result['build_complete'] else 'draft-build-failed'
    result['scope'] = 'Technical document build only; unresolved scientific guards and argument reviews remain open.'
    (output / 'build-manifest.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    lines = ['# Quantum Sphaera: paired document draft', '',
             'This package is an unpublished development draft, not a release or proof certificate.', '',
             'Build status: ' + result['status'],
             'Both PDFs technically complete: ' + str(result['build_complete']),
             'Publication ready: False', '',
             'The full Companion preserves its complete source tree. The physics paper is a selected narrative edition.',
             'See build-manifest.json and editions/*/assembly.json for exact snapshots, source hashes, findings and open review state.',
             'Overfull boxes are counted as layout findings; they still require editorial assessment.',
             'No DOI reservation, upload or publication is performed by this builder.', '']
    (output / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    paths = sorted(p for p in output.rglob('*') if p.is_file() and p.name != 'SHA256SUMS.txt')
    (output / 'SHA256SUMS.txt').write_text(''.join(digest(p) + '  ' + p.relative_to(output).as_posix() + '\n' for p in paths), encoding='utf-8')
    return result['build_complete']


def build(output):
    repo = Path(__file__).resolve().parents[2]
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {'format': 'qsc-dual-document-build-v1', 'version': '5.0.0-draft', 'documents': {}}
    try:
        result['git_commit'] = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
        result['tracked_changes'] = bool(subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=repo, text=True).strip())
        result['builder_sha256'] = digest(Path(__file__))
        result['editions_builder_sha256'] = digest(repo / 'qam/tools/configure_v5_editions.py')
        provenance = output / 'provenance'
        provenance.mkdir()
        for relative in ('qam/tools/build_v5_documents.py', 'qam/tools/configure_v5_editions.py',
                         'qam/store/physics_paper.py', 'qam/store/requirements.txt'):
            shutil.copyfile(repo / relative, provenance / Path(relative).name)
        editions = configure(output / 'qam.sqlite3', output / 'editions')
        result['snapshot_hash'] = editions['snapshot_hash']
        manifests = {name: verify_export(output / 'editions' / name) for name in ('full', 'physics')}
        full, physics = [manifests[n][0] for n in ('full', 'physics')]
        if full['snapshot_hash'] != physics['snapshot_hash'] or full['source_files'] != physics['source_files']:
            raise ValueError('The two editions do not share one source state')
        result['source_files'] = full['source_files']
        for name in ('full', 'physics'):
            manifest, entry = manifests[name]
            print('Compiling ' + name + ' edition', flush=True)
            report, pdf = compile_document(entry, output / 'compile' / name)
            verify_export(output / 'editions' / name)
            report.update({'edition_hash': manifest['edition_hash'],
                           'incomplete_argument_review': manifest['incomplete_argument_review'],
                           'assembly_sha256': digest(output / 'editions' / name / 'assembly.json')})
            if report['pdf_present']:
                filename = 'Quantum_Sphaera_Companion_v5_0_0_draft_' + name + '.pdf'
                shutil.copyfile(pdf, output / filename)
                report.update({'package_pdf': filename, 'pdf_sha256': digest(output / filename)})
            result['documents'][name] = report
        # Detect source changes during a long compilation, not only before it.
        for name, expected in result['source_files'].items():
            if digest(repo / name) != expected:
                raise ValueError('Repository source changed during compilation: ' + name)
        if digest(Path(__file__)) != result['builder_sha256'] or digest(repo / 'qam/tools/configure_v5_editions.py') != result['editions_builder_sha256']:
            raise ValueError('Build implementation changed during compilation')
    except Exception as error:
        result['error'] = type(error).__name__ + ': ' + str(error)
        # Even two existing PDFs cannot override a failed source or provenance check.
        for report in result['documents'].values():
            report['technical_check_passed'] = False
    complete = finalize_package(output, result)
    print(json.dumps({'status': result['status'], 'build_complete': complete, 'output': str(output)}), flush=True)
    return 0 if complete else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='New directory for the complete draft package')
    args = parser.parse_args()
    sys.exit(build(args.out))
