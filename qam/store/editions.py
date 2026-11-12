"""Immutable ordered document assemblies, separate from mathematical dependencies."""
import hashlib
import json
from pathlib import Path
from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import canonical, digest, require_text
from qam.store.snapshots import read_snapshot
from qam.store.selection import select_versions
from qam.store.scrub import scrub
from qam.store.latex_export import render, escape


def safe_path(repo, name):
    root = Path(repo).resolve()
    path = (root / name).resolve()
    if Path(name).is_absolute() or not path.is_relative_to(root):
        raise ValueError('Edition source must be repository-relative')
    return path


def save_edition(database, repo, request):
    fields = {'edition_id', 'title', 'mode', 'snapshot_hash', 'sections', 'source_files', 'entrypoint', 'previous'}
    if set(request) not in (fields, fields | {'presentation'}) or request['mode'] not in {'selected-arguments', 'manuscript-source'}:
        raise ValueError('Invalid edition contract')
    for name in ('edition_id', 'title', 'snapshot_hash'):
        require_text(request[name], name)
    snapshot = read_snapshot(database, request['snapshot_hash'])
    versions = {v['version_hash']: v for v in snapshot['tables']['qstore_versions']}
    if 'presentation' in request:
        presentation = request['presentation']
        required_presentation = {'style', 'author', 'version', 'abstract'}
        release_fields = {'date', 'version_doi', 'concept_doi'}
        if request['mode'] != 'selected-arguments' or set(presentation) not in (required_presentation, required_presentation | release_fields):
            raise ValueError('Invalid reader presentation')
        if presentation['style'] != 'physics-paper' or presentation['abstract'] not in versions:
            raise ValueError('Reader abstract must be source-pinned in the snapshot')
        abstract_payload = json.loads(versions[presentation['abstract']]['payload_json'])
        if not isinstance(abstract_payload.get('latex'), str):
            raise ValueError('Reader abstract must be a LaTeX text block')
        for field in ('author', 'version'):
            require_text(presentation[field], field)
        for field in release_fields & presentation.keys():
            require_text(presentation[field], field)
    if not request['sections']:
        raise ValueError('Edition requires sections')
    keys = set()
    selections = []
    for section in request['sections']:
        if set(section) != {'key', 'title', 'members'} or section['key'] in keys:
            raise ValueError('Invalid or duplicate edition section')
        require_text(section['key'], 'section key')
        require_text(section['title'], 'section title')
        keys.add(section['key'])
        roots = []
        candidates = []
        for member in section['members']:
            if set(member) != {'version', 'use'} or member['use'] not in {'prose', 'argument', 'candidate'}:
                raise ValueError('Invalid edition membership')
            if member['version'] not in versions:
                raise ValueError('Edition member absent from snapshot')
            payload = json.loads(versions[member['version']]['payload_json'])
            if 'presentation' in request and member['use'] == 'prose' and not isinstance(payload.get('latex'), str):
                raise ValueError('Reader prose must be a LaTeX text block')
            if member['use'] != 'candidate' and (payload.get('inventory') or versions[member['version']]['status'] == 'imported-unreviewed'):
                raise ValueError('Raw inventory members must remain candidates')
            (candidates if member['use'] == 'candidate' else roots).append(member['version'])
        if request['mode'] == 'selected-arguments' and roots:
            selected = select_versions(database, request['snapshot_hash'], roots)
            report = scrub(selected)
        else:
            selected, report = None, None
        selections.append({'selection': selected, 'technical_check': report, 'candidates': candidates})
    if 'presentation' in request and not any(m['version'] == request['presentation']['abstract'] and m['use'] == 'prose'
            for s in request['sections'] for m in s['members']):
        raise ValueError('Reader abstract must be a registered prose member')
    if not isinstance(request['source_files'], dict):
        raise ValueError('source_files must be a path/hash mapping')
    for name, expected in request['source_files'].items():
        if hashlib.sha256(safe_path(repo, name).read_bytes()).hexdigest() != expected:
            raise ValueError('Edition source changed: ' + name)
    if request['mode'] == 'manuscript-source' and request['entrypoint'] not in request['source_files']:
        raise ValueError('Full edition entrypoint must be source-pinned')
    if request['mode'] == 'selected-arguments' and request['entrypoint'] is not None:
        raise ValueError('Selected edition has no manuscript entrypoint')
    payload = {'format': 'qstore-edition-v2' if 'presentation' in request else 'qstore-edition-v1', **request, 'sections_state': selections,
               'status': 'research-draft', 'selector_sha256': hashlib.sha256(Path(__file__).with_name('selection.py').read_bytes()).hexdigest()}
    key = digest(payload)
    with store_session(database) as (session, models):
        if session.get(models.qstore_editions, key):
            return {'edition_hash': key, 'edition_id': request['edition_id']}
        rows = list(session.scalars(select(models.qstore_editions).where(models.qstore_editions.edition_id == request['edition_id'])))
        predecessors = {r.previous_hash for r in rows}
        heads = [r.edition_hash for r in rows if r.edition_hash not in predecessors]
        expected = heads[0] if len(heads) == 1 else None
        if len(heads) > 1 or request['previous'] != expected:
            raise ValueError('Edition predecessor is stale or belongs to another edition')
        session.add(models.qstore_editions(edition_hash=key, edition_id=request['edition_id'], snapshot_hash=request['snapshot_hash'],
                    previous_hash=expected, payload_json=canonical(payload)))
        session.flush()
        for index, section in enumerate(request['sections']):
            session.add(models.qstore_edition_sections(edition_hash=key, ordinal=index, section_key=section['key'], title=section['title']))
            session.flush()
            for position, member in enumerate(section['members']):
                session.add(models.qstore_edition_members(edition_hash=key, section_ordinal=index, ordinal=position,
                            version_hash=member['version'], usage=member['use']))
        session.add(models.qstore_ledger(event_type='EDITION', payload_json=canonical({'edition_hash': key})))
    return {'edition_hash': key, 'edition_id': request['edition_id']}


def read_edition(database, key):
    with store_session(database) as (session, models):
        row = session.get(models.qstore_editions, key)
        if row is None:
            raise ValueError('Unknown edition')
        payload = json.loads(row.payload_json)
        if digest(payload) != key or (row.edition_id, row.snapshot_hash, row.previous_hash) != (
                payload['edition_id'], payload['snapshot_hash'], payload['previous']):
            raise ValueError('Edition integrity check failed')
        sections = list(session.scalars(select(models.qstore_edition_sections).where(
            models.qstore_edition_sections.edition_hash == key).order_by(models.qstore_edition_sections.ordinal)))
        members = list(session.scalars(select(models.qstore_edition_members).where(
            models.qstore_edition_members.edition_hash == key).order_by(models.qstore_edition_members.section_ordinal, models.qstore_edition_members.ordinal)))
        expected_sections = [(i, s['key'], s['title']) for i, s in enumerate(payload['sections'])]
        expected_members = [(i, j, m['version'], m['use']) for i, s in enumerate(payload['sections']) for j, m in enumerate(s['members'])]
        if [(s.ordinal, s.section_key, s.title) for s in sections] != expected_sections or [
                (m.section_ordinal, m.ordinal, m.version_hash, m.usage) for m in members] != expected_members:
            raise ValueError('Edition relational index mismatch')
    read_snapshot(database, payload['snapshot_hash'])
    return {'edition_hash': key, **payload}


def export_edition(database, repo, key, destination):
    edition = read_edition(database, key)
    # Preflight every pinned source before creating any output.
    files = {}
    for name, expected in edition['source_files'].items():
        data = safe_path(repo, name).read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError('Edition source changed: ' + name)
        files[name] = data
    destination = Path(destination)
    if destination.exists():
        raise ValueError('Edition destination must be new')
    destination.mkdir(parents=True)
    if edition['mode'] == 'manuscript-source':
        for name, data in files.items():
            target = destination / 'source' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        entry = 'source/' + edition['entrypoint']
        incomplete = True  # Complete source, not a fully reviewed argument graph.
    elif edition.get('presentation', {}).get('style') == 'physics-paper':
        from qam.store.physics_paper import render_paper, audit_markdown
        snapshot = read_snapshot(database, edition['snapshot_hash'])
        (destination / 'paper.tex').write_text(render_paper(edition, snapshot), encoding='utf-8')
        (destination / 'audit.md').write_text(audit_markdown(edition, snapshot), encoding='utf-8')
        entry = 'paper.tex'
        incomplete = any(state['candidates'] or (state['selection'] and state['selection']['findings'])
                         for state in edition['sections_state'])
    else:
        snapshot = read_snapshot(database, edition['snapshot_hash'])
        versions = {v['version_hash']: v for v in snapshot['tables']['qstore_versions']}
        pieces, seen = [], set()
        packages, macros, references = set(), {}, {}
        from qam.store.latex_resources import resource_groups
        incomplete = False
        for section, state in zip(edition['sections'], edition['sections_state']):
            pieces.append(r'\section{' + escape(section['title']) + '}')
            selected = state['selection']
            if state['candidates']:
                incomplete = True
                pieces.append(escape(str(len(state['candidates'])) + ' source statements are registered for this section but await interpretation, proof/dependency and resource review. They are not silently exported as established results.') + r'\par')
                pieces.append(r'\begin{itemize}')
                for version in state['candidates']:
                    candidate = json.loads(versions[version]['payload_json'])
                    label = candidate.get('inventory', {}).get('label') or candidate['title']
                    pieces.append(r'\item ' + escape(label + ' / pending review / version ' + version[:12]))
                pieces.append(r'\end{itemize}')
            if selected:
                if any(f['kind'] in {'guard', 'frame-bridge-required', 'unspecified-frame',
                                    'declared-dependency', 'proposed-dependency'} for f in selected['findings']):
                    incomplete = True
                if state['technical_check']['result'] != 'passed':
                    incomplete = True
                    pieces.append('Technical export of this section is blocked. See the assembly manifest.')
                    continue
                groups = resource_groups(selected['objects'])
                packages.update(groups[0])
                for obj in groups[1]: macros[obj['version_hash']] = obj
                for obj in groups[2]: references[obj['version_hash']] = obj
                subset = {**selected, 'objects': [o for o in selected['objects'] if o['version_hash'] not in seen]}
                seen.update(o['version_hash'] for o in subset['objects'])
                rendered = render(subset)
                start = rendered.index('Native physical interpretation requires separate review.') + len('Native physical interpretation requires separate review.')
                end = rendered.index(r'\section*{Open prerequisites and review notes}')
                pieces.append(rendered[start:end].replace(r'\section{', r'\subsection{\raggedright '))
                pieces.append(r'\paragraph{Open prerequisites and review notes}')
                findings_end = rendered.find(r'\begin{thebibliography}', end)
                if findings_end < 0:
                    findings_end = rendered.index(r'\end{document}', end)
                pieces.append(rendered[end + len(r'\section*{Open prerequisites and review notes}'):findings_end].replace(
                    r'\section*{Automatic checks}', r'\paragraph{Automatic checks}'))
        # Detect resource conflicts across sections, not just within each selection.
        combined = {}
        for state in edition['sections_state']:
            if state['selection'] and state['technical_check']['result'] == 'passed':
                combined.update({o['version_hash']: o for o in state['selection']['objects']})
        resource_groups(list(combined.values()))
        preamble = [r'\documentclass[10pt,a4paper]{article}', r'\usepackage[T1]{fontenc}', r'\usepackage[utf8]{inputenc}',
                    r'\usepackage{amsmath}', r'\usepackage[margin=25mm]{geometry}', r'\setlength{\emergencystretch}{1em}']
        preamble += [r'\usepackage{' + p + '}' for p in sorted(packages)]
        preamble += [o['payload']['latex'] for o in macros.values()]
        preamble += [r'\begin{document}', r'\section*{' + escape(edition['title']) + '}',
                     'Research draft. Section assignments do not certify proofs. Unreviewed members and open guards remain visible.']
        if references:
            pieces += [r'\begin{thebibliography}{99}'] + [o['payload']['latex'] for o in references.values()] + [r'\end{thebibliography}']
        (destination / 'paper.tex').write_text('\n'.join(preamble + pieces + [r'\end{document}']), encoding='utf-8')
        entry = 'paper.tex'
    manifest = {**edition, 'entrypoint_export': entry, 'incomplete_argument_review': incomplete,
                'exporter_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'files': {p.relative_to(destination).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sorted(destination.rglob('*')) if p.is_file()}}
    (destination / 'assembly.json').write_text(canonical(manifest) + '\n', encoding='utf-8')
    return {'edition_hash': key, 'entrypoint': entry, 'incomplete_argument_review': incomplete}
