"""Generate a bounded LaTeX draft and provenance manifest from a pinned selection."""

import hashlib
import json
from collections import Counter
from pathlib import Path

from qam.store.matrix_check import matrix
from qam.store.registry import canonical, digest
from qam.store.selection import select_versions
from qam.store.latex_resources import resource_groups
from qam.store.scrub import scrub


def escape(text):
    replacements = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}',
                    '$': r'\$', '&': r'\&', '#': r'\#', '%': r'\%',
                    '_': r'\_', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(replacements.get(char, char) for char in str(text)).replace('\n', ' ')


def matrix_tex(value):
    rows = matrix(value)
    def number(item):
        if item.denominator == 1:
            return str(item.numerator)
        return rf'\frac{{{item.numerator}}}{{{item.denominator}}}'
    return r'\begin{pmatrix}' + r'\\'.join(' & '.join(number(item) for item in row) for row in rows) + r'\end{pmatrix}'


def render(selection, title='QAM registered comparison draft'):
    titles = {obj['version_hash']: obj['payload']['title'] for obj in selection['objects']}
    lines = [r'\documentclass[10pt,a4paper]{article}', r'\usepackage[T1]{fontenc}',
             r'\usepackage[utf8]{inputenc}', r'\usepackage{amsmath}',
             r'\usepackage[margin=25mm]{geometry}', r'\setlength{\emergencystretch}{1em}']
    packages, macros, references = resource_groups(selection['objects'])
    for package in sorted(packages):
        lines.append(r'\usepackage{' + package + '}')
    for macro in macros:
        lines.append(macro['payload']['latex'])
    lines += [r'\begin{document}',
             r'\section*{' + escape(title) + '}',
             'Snapshot ' + selection['snapshot_hash'][:16] + r'.\par',
             'Selection ' + selection['selection_hash'][:16] + r'.\par',
             'This draft displays registered argument blocks with their declared assumptions. '
             'Native physical interpretation requires separate review.']
    for obj in selection['objects']:
        payload = obj['payload']
        if obj['kind'] == 'latex-resource':
            continue
        lines += [r'\section{' + escape(payload['title']) + '}',
                  r'\label{qv-' + obj['version_hash'] + '}',
                  escape(obj['kind'] + ' / ' + obj['status'] + ' / frame ' + obj['frame']) + r'.\par']
        if obj['kind'] == 'definition':
            lines += [escape(payload['body']) + r'\par', 'Scope. ' + escape(payload['scope']) + r'\par']
        elif obj['kind'] == 'seed' and payload['value_type'] == 'rational-matrix':
            lines += [r'\[' + matrix_tex(payload['value']) + r'\]',
                      'Origin. ' + escape(payload['origin']) + r'\par']
        elif obj['kind'] in {'claim', 'proof', 'explanation', 'transition'}:
            lines.append(payload['latex'])
        else:
            raise ValueError('Unsupported export object')
    lines.append(r'\section*{Open prerequisites and review notes}')
    if selection['findings']:
        lines.append(r'\begin{itemize}\setlength{\itemsep}{0pt}')
        notes = []
        status_counts = Counter()
        for finding in selection['findings']:
            # Long hashes live in the manifest, keeping the visible draft readable.
            kind = finding['kind']
            if kind == 'object-status':
                status_counts[finding['status']] += 1
                continue
            elif kind == 'assumption':
                text = titles[finding['version']] + ': ' + finding['text']
            elif kind == 'declared-dependency':
                text = 'A selected dependency is declared and awaits independent review.'
            elif kind == 'proposed-dependency':
                text = 'A proposed dependency remains unresolved.'
            elif kind == 'frame-bridge-required':
                text = 'A dependency requires an explicit bridge between frames.'
            elif kind == 'unspecified-frame':
                text = titles[finding['version']] + ': frame unspecified'
            else:
                text = finding.get('payload', {}).get('obligation', kind)
                if 'status' in finding:
                    text += ' (' + finding['status'] + ')'
            notes.append(text)
        for text, count in Counter(notes).items():
            suffix = ' (' + str(count) + ' recorded instances)' if count > 1 else ''
            lines.append(r'\item ' + escape(text + suffix))
        for status, count in sorted(status_counts.items()):
            lines.append(r'\item ' + escape(str(count) + ' selected objects carry status ' + status + '.'))
        lines.append(r'\end{itemize}')
    else:
        lines.append('No selection findings recorded. Publication readiness requires separate review.')
    lines.append(r'\section*{Automatic checks}')
    applicable = [row for row in selection['related_checks'] if row['all_matrix_inputs_selected']]
    if applicable:
        lines.append(r'\begin{itemize}')
        for check in applicable:
            lines.append(r'\item ' + escape(check['result']) + ' --- receipt ' + check['receipt_hash'][:16] + '.')
        lines.append(r'\end{itemize}')
        lines.append('The checks concern the registered rational matrix equations only. '
                     'Full input hashes and selection findings are recorded in the manifest.')
    else:
        lines.append('No matrix check with all matrix inputs in this selection is recorded.')
    if references:
        lines.append(r'\begin{thebibliography}{' + str(len(references)) + '}')
        lines.extend(reference['payload']['latex'] for reference in references)
        lines.append(r'\end{thebibliography}')
    lines += [r'\end{document}', '']
    return '\n'.join(lines)


def export(path, snapshot_hash, roots, destination):
    selection = select_versions(path, snapshot_hash, roots)
    return export_selection(selection, destination)


def export_selection(selection, destination, paper=None):
    report = scrub(selection)
    if report['result'] != 'passed':
        raise ValueError('Technical export check blocked: ' + canonical(report['issues']))
    tex = render(selection, paper['title']).encode('utf-8') if paper else render(selection).encode('utf-8')
    manifest = {'format': 'qstore-latex-export-v1', 'selection': selection,
                'generator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'selection_code_sha256': hashlib.sha256(Path(__file__).with_name('selection.py').read_bytes()).hexdigest(),
                'resource_code_sha256': hashlib.sha256(Path(__file__).with_name('latex_resources.py').read_bytes()).hexdigest(),
                'scrub_code_sha256': hashlib.sha256(Path(__file__).with_name('scrub.py').read_bytes()).hexdigest(),
                'technical_check': report,
                'files': {'paper.tex': hashlib.sha256(tex).hexdigest()},
                'text_mode': 'escaped text; rational matrices; source-backed verbatim LaTeX blocks',
                'status': 'research-draft'}
    if paper:
        manifest['paper'] = paper
    manifest_hash = digest(manifest)
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=False)
    # Publish the manifest last; a partial output without it is incomplete.
    (destination / 'paper.tex').write_bytes(tex)
    (destination / 'manifest.json').write_text(canonical(manifest) + '\n', encoding='utf-8')
    return {'directory': str(destination), 'manifest_hash': manifest_hash,
            'selection_hash': selection['selection_hash'], 'status': 'research-draft'}
