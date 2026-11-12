"""Reader-facing physics paper; machine provenance remains in the audit export."""
import json
from qam.store.latex_export import escape
from qam.store.latex_resources import resource_groups


def render_paper(edition, snapshot):
    presentation = edition['presentation']
    date_lines = 'Working paper ' + escape(presentation['version']) + r'\\\small ' + escape(presentation.get('date', '11 November 2026')) + '; not peer reviewed'
    if 'version_doi' in presentation:
        date_lines += r'\\\small Version DOI: ' + escape(presentation['version_doi'])
        date_lines += r'\\\small Concept DOI: ' + escape(presentation['concept_doi'])
    versions = {v['version_hash']: v for v in snapshot['tables']['qstore_versions']}
    abstract = json.loads(versions[presentation['abstract']]['payload_json'])['latex']
    objects = {}
    for state in edition['sections_state']:
        if state['selection']:
            if state['technical_check']['result'] != 'passed':
                raise ValueError('Reader paper requires technically valid selected sections')
            objects.update({o['version_hash']: o for o in state['selection']['objects']})
    packages, macros, bibliography = resource_groups(list(objects.values()))
    lines = [r'\documentclass[11pt,a4paper]{article}', r'\usepackage[T1]{fontenc}',
             r'\usepackage[utf8]{inputenc}', r'\usepackage[margin=27mm]{geometry}',
             r'\setlength{\emergencystretch}{2em}']
    lines += [r'\usepackage{' + p + '}' for p in sorted(packages | {'amsmath', 'amssymb', 'amsthm'})]
    lines += [m['payload']['latex'] for m in macros]
    lines += [r'\newtheorem{proposition}{Proposition}[section]',
              r'\title{' + escape(edition['title']) + '}',
              r'\author{' + escape(presentation['author']) + r'\\\small Independent Researcher, Bochum, Germany}',
              r'\date{' + date_lines + '}',
              r'\begin{document}', r'\maketitle', r'\begin{abstract}', abstract, r'\end{abstract}']
    for section in edition['sections']:
        lines.append(r'\section{\raggedright ' + escape(section['title']) + '}')
        for member in section['members']:
            if member['use'] != 'prose' or member['version'] == presentation['abstract']:
                continue
            payload = json.loads(versions[member['version']]['payload_json'])
            lines.append(payload['latex'])
    if bibliography:
        lines += [r'\begin{thebibliography}{99}']
        lines += [entry['payload']['latex'] for entry in bibliography]
        lines.append(r'\end{thebibliography}')
    evidence = [o for section, state in zip(edition['sections'], edition['sections_state'])
                if section['key'] == 'masses' and state['selection']
                for o in state['selection']['objects']
                if o['kind'] in {'claim', 'proof'} or o['object_id'] == 'koide-branch-root-setup']
    if evidence:
        lines += [r'\clearpage', r'\appendix', r'\section{Supporting mass-readout arguments}',
                  'For completeness, the original mathematical arguments for the conditional mass-readout statements are reproduced below. '
                  'Their hypotheses refer to the comparison domains stated in the text; they do not identify a native physical readout.']
        seen = set()
        for obj in evidence:
            if obj['version_hash'] in seen:
                continue
            seen.add(obj['version_hash'])
            payload = obj['payload']
            if obj['kind'] == 'claim':
                title = payload['title'].replace('hc-mass-', '').replace('-', ' ')
                lines += [r'\begin{proposition}[' + escape(title) + ']', payload['latex'], r'\end{proposition}']
            else:
                lines.append(payload['latex'])
    lines += [r'\end{document}', '']
    return '\n'.join(lines)


def audit_markdown(edition, snapshot):
    versions = {v['version_hash']: v for v in snapshot['tables']['qstore_versions']}
    lines = ['# Editorial and evidence audit', '',
             'The reader paper is a narrative synthesis. This report retains the selected objects, pending candidates and all selection findings.',
             'A prose summary does not independently certify an imported source theorem.', '']
    for section, state in zip(edition['sections'], edition['sections_state']):
        lines += ['## ' + section['title'], '']
        for member in section['members']:
            row = versions[member['version']]
            lines.append('- ' + member['use'] + ': `' + row['object_id'] + '` / `' + member['version'] + '`')
        if state['selection']:
            lines += ['', '### Findings', '']
            lines.extend('- `' + json.dumps(f, ensure_ascii=False) + '`' for f in state['selection']['findings'])
            lines += ['', '### Finite check receipts', '']
            lines.extend('- `' + json.dumps(c, ensure_ascii=False) + '`' for c in state['selection']['related_checks'])
        lines.append('')
    return '\n'.join(lines)
