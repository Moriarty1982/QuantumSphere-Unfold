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


ACTIVE_EDGES = {'requires', 'interpreted-by', 'depends-on-counterterm'}
NOTE_MARK = '% qstore-counterterm-note '
ENTRY_MARK = '% qstore-counterterm-entry '


def counterterm_dependencies(selection):
    """Map each selected statement to the counterterm states it reaches through declared or reviewed edges."""
    states = {item['scheme']: item for item in selection.get('counterterms', [])}
    if not states:
        return {}
    forward = {}
    for row in selection['relations']:
        if row['relation_type'] in ACTIVE_EDGES and row['effective_status'] in {'declared', 'reviewed'}:
            forward.setdefault(row['source_version'], set()).add(row['target_version'])
    result = {}
    for obj in selection['objects']:
        if obj['kind'] == 'counterterm-scheme':
            continue
        seen, pending, reached = {obj['version_hash']}, [obj['version_hash']], set()
        while pending:
            for target in forward.get(pending.pop(), set()):
                if target in states:
                    reached.add(target)
                if target not in seen:
                    seen.add(target)
                    pending.append(target)
        if reached:
            result[obj['version_hash']] = sorted(reached)
    return result


def counterterm_note(version, schemes, selection):
    """Inline guard annotation for a statement that depends on registered counterterms."""
    states = {item['scheme']: item for item in selection['counterterms']}
    lines = [NOTE_MARK + version, r'\par\noindent\textit{Effective scope.} '
             'This statement depends on registered compensation terms. It is local, effective and '
             r'readout-dependent, not a parameter-free derivation.\par']
    lines.append(r'\begin{itemize}\setlength{\itemsep}{0pt}')
    for scheme in schemes:
        state = states[scheme]
        text = state['object_id'] + ' (status ' + state['status'] + ')'
        if state['inherits_guards']:
            titles = [guard['title'] for guard in state['open_guards']]
            text += '; inherited open guards: ' + (', '.join(titles) if titles else 'none recorded')
        else:
            text += '; structurally matched, see the registry appendix'
        if state['status'] == 'deprecated':
            text += '; deprecated dependency'
        lines.append(r'\item ' + escape(text))
    lines.append(r'\end{itemize}')
    return lines


def parameter_text(name, spec):
    if spec['role'] == 'discrete_choice':
        return f"{name}: discrete choice {spec['value']} from {len(spec['options'])} options ({'; '.join(spec['options'])})"
    bounds = spec.get('bounds')
    return f"{name}: {spec['role']}, value {spec['value']}, bounds [{bounds[0]}, {bounds[1]}]"


def counterterm_appendix(selection):
    """Counterterm and compensation registry: one entry per selected scheme, with status and open guards."""
    payloads = {obj['version_hash']: obj['payload'] for obj in selection['objects']
                if obj['kind'] == 'counterterm-scheme'}
    lines = [r'\section*{Counterterm and compensation registry}',
             'Every compensation term used by a statement in this draft is listed here. Entries are local and '
             'effective bookkeeping, not derivations. Statements depending on an entry that is not structurally '
             r'matched inherit its open guards.\par',
             r'\begin{tabular}{lll}', r'Entry & Status & Open guards\\ \hline']
    for state in selection['counterterms']:
        lines.append(escape(state['object_id']) + ' & ' + escape(state['status']) + ' & '
                     + str(len(state['open_guards'])) + r'\\')
    lines.append(r'\end{tabular}')
    for state in selection['counterterms']:
        payload = payloads[state['scheme']]
        function = payload['compensation_function']
        domain = payload['validity_domain']
        lines += [ENTRY_MARK + state['scheme'],
                  r'\subsection*{' + escape(state['object_id'] + ': ' + payload['title']) + '}',
                  r'\begin{itemize}\setlength{\itemsep}{0pt}',
                  r'\item ' + escape('Version ' + state['scheme'][:16] + ', status ' + state['status']
                                     + ', transitions ' + str(len(state['transitions'])) + '.'),
                  r'\item ' + escape('Target sector: ' + payload['target_sector'] + '.'),
                  r'\item ' + escape('Basis (' + payload['operator_basis']['kind'] + ', frame '
                                     + payload['operator_basis']['frame'] + '): '
                                     + payload['operator_basis']['expression'] + '.'),
                  r'\item ' + escape('Functional form: ' + function['symbolic'] + '.')]
        for name, spec in sorted(function['parameters'].items()):
            lines.append(r'\item ' + escape('Parameter ' + parameter_text(name, spec) + '.'))
        lines.append(r'\item ' + escape('Validity domain: ' + domain['variable'] + ' in [' + domain['interval'][0]
                                        + ', ' + domain['interval'][1] + ']; ' + domain['description'] + '.'))
        fit = payload.get('fitted_on')
        if fit:
            data = ', '.join(item['label'] + ' (' + item['source'] + ' ' + item['version'] + ')' for item in fit['data'])
            text = 'Fitted on: ' + data
            if fit.get('scan'):
                scan = fit['scan']
                text += f"; scan with {scan['trials']} trials, {scan['hits']} hit(s), chance expectation {scan['chance_expectation']}"
            lines.append(r'\item ' + escape(text + '. Comparisons with these data are not blind.'))
        for tension in payload.get('known_tensions', []):
            lines.append(r'\item ' + escape('Known tension: ' + tension['description'] + ' (delta '
                                            + tension['delta'] + ').'))
        if state['status'] == 'structurally_matched':
            lines.append(r'\item ' + escape('Matching identity F_struct = delta_eff + Delta with replacement '
                                            + str(state['replacement'])[:16] + ' and residual receipt '
                                            + str(state['receipt'])[:16] + '. The phenomenological '
                                            'parameterization stays in the version history.'))
        if state['inherits_guards']:
            for guard in state['open_guards']:
                lines.append(r'\item ' + escape('Open guard ' + guard['title'] + ': ' + guard['obligation']
                                                + ' (' + guard['status'] + ').'))
        lines.append(r'\item ' + escape('Scope: ' + payload['scope'] + '.'))
        lines.append(r'\end{itemize}')
    return lines


def counterterm_export_issues(selection, tex):
    """Hard audit: every dependent statement carries its guard note and every scheme its registry entry."""
    issues = []
    for version in counterterm_dependencies(selection):
        if NOTE_MARK + version not in tex:
            issues.append({'kind': 'counterterm-note-missing', 'version': version})
    for state in selection.get('counterterms', []):
        if ENTRY_MARK + state['scheme'] not in tex:
            issues.append({'kind': 'counterterm-entry-missing', 'scheme': state['scheme']})
    return issues


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
    dependent = counterterm_dependencies(selection)
    for obj in selection['objects']:
        payload = obj['payload']
        if obj['kind'] in {'latex-resource', 'counterterm-scheme'}:
            # Counterterm schemes appear only in the registry appendix, never as core text.
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
        if dependent.get(obj['version_hash']):
            lines += counterterm_note(obj['version_hash'], dependent[obj['version_hash']], selection)
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
    if selection.get('counterterms'):
        lines += counterterm_appendix(selection)
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
    text = render(selection, paper['title']) if paper else render(selection)
    issues = counterterm_export_issues(selection, text)
    if issues:
        raise ValueError('Counterterm export check blocked: ' + canonical(issues))
    tex = text.encode('utf-8')
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
