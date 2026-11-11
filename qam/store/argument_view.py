"""Readable graph projection of a fixed store selection with explicit evidence status."""

import html
from collections import Counter


def mermaid_label(text):
    return html.escape(str(text).replace('\n', ' '), quote=True).replace('`', '&#96;')


def markdown(selection):
    objects = selection['objects']
    names = {row['version_hash']: f'n{index}' for index, row in enumerate(objects)}
    lines = ['# Argumentansicht', '',
             'Snapshot `' + selection['snapshot_hash'] + '`', '',
             'Auswahl `' + selection['selection_hash'] + '`', '',
             'Bei requires und interpreted-by laufen Pfeile von Voraussetzungen zu ihrer Verwendung. '
             'Andere Relationen folgen ihrer gespeicherten Richtung. Gepunktete Kanten '
             'bezeichnen deklarierte oder vorgeschlagene Beziehungen. Eine Review-Markierung '
             'verweist auf eine protokollierte Beurteilung. Mathematische Guards bleiben separat sichtbar.', '',
             '```mermaid', 'flowchart TD']
    for row in objects:
        label = row['payload']['title'] + ' / ' + row['kind'] + ' / ' + row['status']
        lines.append(f'  {names[row["version_hash"]]}["{mermaid_label(label)}"]')
    for relation in selection['relations']:
        status = relation['effective_status']
        if status == 'rejected':
            continue
        source = names[relation['source_version']]
        target = names[relation['target_version']]
        label = mermaid_label(relation['relation_type'] + ' - ' + status)
        arrow = '-->' if status == 'reviewed' else '-.->'
        if relation['relation_type'] in {'requires', 'interpreted-by'}:
            source, target = target, source
        lines.append(f'  {source} {arrow}|"{label}"| {target}')
    for row in objects:
        placement = row['payload'].get('placement') if row['kind'] == 'transition' else None
        if placement:
            node = names[row['version_hash']]
            lines.append(f'  {names[placement["after"]]} -.->|"editorial"| {node}')
            lines.append(f'  {node} -.->|"editorial"| {names[placement["before"]]}')
    guards = [row for row in selection['findings'] if row['kind'] == 'guard']
    for index, guard in enumerate(guards):
        label = guard['payload']['title'] + ' / ' + guard['status']
        lines.append(f'  g{index}["{mermaid_label(label)}"]')
        for endpoint in dict.fromkeys([guard['subject'], guard['target']]):
            if endpoint in names:
                lines.append(f'  g{index} -.->|"guard obligation"| {names[endpoint]}')
        lines.append(f'  style g{index} fill:#fff0d0,stroke:#a65b00')
    lines += ['```', '', '## Registrierte Bausteine', '',
              '| Nr. | Typ | Titel | Status | Versionshash |',
              '|---|---|---|---|---|']
    for index, row in enumerate(objects, 1):
        title = html.escape(row['payload']['title']).replace('|', '&#124;').replace('\n', ' ')
        lines.append(f'| {index} | {row["kind"]} | {title} | {row["status"]} | `{row["version_hash"]}` |')
    lines += ['', '## Offene Anschlussstellen', '']
    if guards:
        for guard in guards:
            obligation = guard['payload']['obligation'].replace('\n', ' ')
            lines += ['- ' + obligation + ' (`' + guard['hash'] + '`, ' + guard['status'] + ').']
    else:
        lines.append('In dieser Auswahl sind keine offenen Guard-Einträge erfasst. Weitere Annahmen stehen im Auswahlmanifest.')
    counts = Counter(row['effective_status'] for row in selection['relations'])
    lines += ['', 'Beziehungsstatus ' + ', '.join(f'{key}={value}' for key, value in sorted(counts.items())) + '.',
              '', 'Der Graph zeigt die registrierten Beziehungen dieser Auswahl. '
              'Vollständigkeit der fachlichen Abhängigkeiten und allgemeine Beweisgültigkeit sind gesondert zu prüfen.', '']
    return '\n'.join(lines)
