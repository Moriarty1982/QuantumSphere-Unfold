"""One-off typographic reflow of the frozen pre-edit v5 layout inventory."""
import hashlib
import json
from pathlib import Path
import re


def group_end(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] in '{}' and (i == 0 or text[i - 1] != '\\'):
            depth += 1 if text[i] == '{' else -1
            if depth == 0:
                return i + 1
    raise ValueError('Unbalanced argument')


def unwrap(text, command):
    pattern = re.compile(re.escape(command) + r'\s*\{')
    while match := pattern.search(text):
        start = match.end() - 1
        end = group_end(text, start)
        text = text[:match.start()] + text[start + 1:end - 1] + text[end:]
    return text


def content_projection(text):
    """Remove only the layout syntax used here; retain remaining group structure."""
    text = re.sub(r'\{\\urlstyle\{same\}\\nolinkurl\{([^{}]*)\}\}', r'\1', text)
    text = re.sub(r'\\(?:qquad|quad|allowbreak|left|right|bigl|bigr)\b', '', text)
    for command in (r'\text', r'\hbox'):
        text = unwrap(text, command)
    pattern = re.compile(r'\\begin\{(?:array|tabular)\}')
    while match := pattern.search(text):
        start = match.end()
        while text[start].isspace():
            start += 1
        end = group_end(text, start)
        text = text[:match.start()] + text[end:]
    text = re.sub(r'\\(?:begin|end)\{(?:gathered|center|samepage)\}|\\end\{(?:array|tabular)\}', '', text)
    text = re.sub(r'\\(?:qquad|quad|allowbreak|left|right|bigl|bigr)\b', '', text)
    text = re.sub(r'\\[\[\]()]+|\\\\|(?<!\\)\$|&', '', text)
    return re.sub(r'\s+', '', text)


def cell(text):
    # Text cells wrap as prose. Mathematical parts retain their original tokens.
    pattern = re.compile(r'\\text\s*\{')
    parts = []
    position = 0
    for match in pattern.finditer(text):
        if match.start() < position:
            continue
        end = group_end(text, match.end() - 1)
        if text[position:match.start()].strip():
            parts.append(r'\(' + text[position:match.start()].strip() + r'\)')
        parts.append(text[match.end():end - 1])
        position = end
    if text[position:].strip():
        parts.append(r'\(' + text[position:].strip() + r'\)')
    return ' '.join(parts)


def table(block, widths):
    match = re.search(r'\\begin\{array\}\{[^{}]+\}(.*?)\\end\{array\}', block, re.S)
    body = match[1]
    rows = body.split(r'\\')
    output = [r'\begin{center}', r'\begin{tabular}{@{}' + ''.join(
        r'>{\raggedright\arraybackslash}p{' + str(w) + r'\linewidth}' for w in widths) + '@{}}']
    for i, row in enumerate(rows):
        rule = r'\hline' in row
        row = row.replace(r'\hline', '').strip()
        if rule:
            output.append(r'\hline')
        cells = row.split('&')
        if len(cells) != len(widths):
            raise ValueError('Unexpected table width')
        output.append(' & '.join(cell(c.strip()) for c in cells) + r'\\')
    output += [r'\end{tabular}', r'\end{center}']
    return '\n'.join(output)


def display(block):
    if r'\boxed{' not in block:
        return block.replace(r'\[', '\\[\n\\begin{gathered}').replace(r'\]', '\\end{gathered}\n\\]').replace(r'\qquad', r'\\')
    start = block.index(r'\boxed{') + len(r'\boxed')
    end = group_end(block, start)
    body = block[start + 1:end - 1]
    body = body.replace(r'\left', r'\bigl').replace(r'\right', r'\bigr')
    body = re.sub(r'\\q(?:quad|uad)\b', r'\\\\', body)
    body = re.sub(r',\s*\n', lambda _: ',' + r'\\' + '\n', body)
    body = re.sub(r'^([+]|\\wedge)\s*$', r'\\\\\1', body, flags=re.M)
    body = body.replace(r'\text{ is a monitor', '\\\\\n\\text{ is a monitor')
    body = re.sub(r'(?:\\\\\s*){2,}', lambda _: r'\\' + '\n', body)
    return block[:start + 1] + '\n\\begin{gathered}\n' + body.strip() + '\n\\end{gathered}\n' + block[end - 1:]


def main():
    repo = Path(__file__).resolve().parents[2]
    inventory = json.loads((repo / 'notes/research/v5_layout_inventory_2026_11_11.json').read_text())
    originals = {}
    for path, expected in inventory['source_sha256'].items():
        raw = (repo / path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError('Source changed since inventory: ' + path)
        originals[path] = (raw, raw.decode('utf-8').replace('\r\n', '\n'))
    blocks = []
    for finding in inventory['findings']:
        if finding['kind'] != 'display-or-box':
            continue
        path = finding['source_hint']
        text = originals[path][1]
        lines = text.splitlines(keepends=True)
        end = finding['tex_line_start'] - 1
        start = next(i for i in range(end, -1, -1) if lines[i].strip() == r'\[')
        close = next(i for i in range(end, len(lines)) if lines[i].strip() == r'\]')
        blocks.append((path, ''.join(lines[start:close + 1]).rstrip('\n')))
    widths = {1: [.19, .04, .065, .075, .04, .09, .30],
              2: [.22, .11, .28, .27], 18: [.08, .39, .21, .22],
              40: [.08, .33, .14, .34], 43: [.29, .30, .32]}
    changed = {p: text for p, (_, text) in originals.items()}
    for index, (path, block) in enumerate(blocks):
        replacement = table(block, widths[index]) if index in widths else display(block)
        if content_projection(block) != content_projection(replacement):
            raise ValueError('Content changed in display ' + str(index))
        if block not in changed[path]:
            continue  # Repeated identical guard boxes were already replaced together.
        changed[path] = changed[path].replace(block, replacement)
    p = 'sources/research/parts/v470/34_mm_hc_and_c5_development.tex'
    anchor = '\\begin{tabular}{c|c|c|c}\n\\toprule\nedge & r16 status'
    replacement = r'\begin{tabular}{@{}>{\raggedright\arraybackslash}p{.14\linewidth}>{\raggedright\arraybackslash}p{.25\linewidth}>{\raggedright\arraybackslash}p{.25\linewidth}>{\raggedright\arraybackslash}p{.25\linewidth}@{}}' + '\n\\toprule\nedge & r16 status'
    if changed[p].count(anchor) != 1:
        raise ValueError('Expected one r17 table')
    changed[p] = changed[p].replace(anchor, replacement)
    changed[p] = changed[p].replace(r'\subsection{r54 Decision}', '\\begin{samepage}\n\\subsection{r54 Decision}')
    tail = '\\text{v4.7.0-r55: local theoremlet-to-lemma packaging and guard-stable lemma registry.}\n}\n\\]'
    if changed[p].count(tail) != 1:
        raise ValueError('Expected one final r54 handoff')
    changed[p] = changed[p].replace(tail, tail + '\n\\end{samepage}')
    tokens_by_path = {}
    for finding in inventory['findings']:
        path = finding['source_hint']
        if finding['kind'] != 'paragraph' or path == p:
            continue
        original_lines = originals[path][1].splitlines()
        excerpt = '\n'.join(original_lines[finding['tex_line_start'] - 1:finding['tex_line_end']])
        tokens_by_path.setdefault(path, set()).update(re.findall(r'(?:ask/respond/|address/object/)[a-zA-Z/-]+', excerpt))
    for path, tokens in tokens_by_path.items():
        pattern = '(?:' + '|'.join(re.escape(t) for t in sorted(tokens, key=len, reverse=True)) + r')(?![a-zA-Z/-])'
        changed[path] = re.sub(pattern, lambda m: r'{\urlstyle{same}\nolinkurl{' + m[0] + '}}', changed[path])
    reports = []
    for path, text in changed.items():
        if content_projection(originals[path][1]) != content_projection(text):
            raise ValueError('Content changed in ' + path)
    for path, text in changed.items():
        raw, old = originals[path]
        output = text.replace('\n', '\r\n') if b'\r\n' in raw else text
        (repo / path).write_bytes(output.encode('utf-8'))
        reports.append({'path': path, 'before_sha256': hashlib.sha256(raw).hexdigest(),
                        'after_sha256': hashlib.sha256(output.encode()).hexdigest(),
                        'content_projection_unchanged': True})
    (repo / 'tmp/v5-layout-content-check.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    print('Reflowed four source files; content projection unchanged.')


if __name__ == '__main__':
    main()
