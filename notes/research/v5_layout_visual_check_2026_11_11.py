"""Render the reflow regions with bounding neighbour-label pages for visual QA.

Requires pypdf, Pillow and pdftoppm; no source changes or scientific checks.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

from pypdf import PdfReader, PdfWriter
from PIL import Image, ImageDraw


def main(bundle, output):
    repo = Path(__file__).resolve().parents[2]
    bundle = Path(bundle)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    aux = (bundle / 'compile/full/v480-companion.aux').read_text(encoding='utf-8')
    labels = {m[1]: int(m[2]) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{.*?\}\{(\d+)\}', aux)}
    records = []
    for name in ('07_qam_infrastructure.tex', '26_inherited_technical_appendices.tex',
                 '34_mm_hc_and_c5_development.tex', '36_frame_typed_endpoint.tex'):
        path = Path('sources/research/parts/v470') / name
        text = (repo / path).read_text(encoding='utf-8')
        positions = list(re.finditer(r'\\label\{([^}]+)\}', text))
        markers = list(re.finditer(r'\\begin\{gathered\}|\\begin\{tabular\}\{@\{\}>|\{\\urlstyle\{same\}\\nolinkurl', text))
        for marker in markers:
            before = [m for m in positions if m.start() < marker.start() and m[1] in labels]
            after = [m for m in positions if m.start() > marker.start() and m[1] in labels]
            if not before:
                raise ValueError('Cannot bound visual region at ' + path.as_posix())
            if after:
                following = after[0][1]
            else:
                # The final decision box has no later label in its own input file.
                # Bound it by the next input's label in auxiliary-file order.
                local_labels = {m[1] for m in positions}
                order = list(labels)
                following = next(k for k in order[order.index(before[-1][1]) + 1:] if k not in local_labels)
            records.append({'path': path.as_posix(), 'line': text[:marker.start()].count('\n') + 1,
                            'before': before[-1][1], 'after': following,
                            'pages': [labels[before[-1][1]], labels[following]]})
    pages = sorted({p for r in records for p in range(r['pages'][0], r['pages'][1] + 1)})
    pdf = bundle / 'Quantum_Sphaera_Companion_v5_0_0_draft_full.pdf'
    reader = PdfReader(pdf)
    writer = PdfWriter()
    for n in pages:
        writer.add_page(reader.pages[n - 1])
    with (output / 'changed-regions.pdf').open('wb') as stream:
        writer.write(stream)
    subprocess.run(['pdftoppm', '-scale-to', '1100', '-png', str(output / 'changed-regions.pdf'),
                    str(output / 'page')], check=True, capture_output=True)
    images = sorted(output.glob('page-*.png'))
    for k in range(0, len(images), 6):
        canvas = Image.new('RGB', (1500, 1460), '#ddd')
        draw = ImageDraw.Draw(canvas)
        for j, path in enumerate(images[k:k + 6]):
            img = Image.open(path)
            img.thumbnail((490, 700))
            x, y = (j % 3) * 500, (j // 3) * 730
            draw.text((x + 10, y + 7), 'Original page ' + str(pages[k + j]), fill='black')
            canvas.paste(img, (x + (500 - img.width) // 2, y + 25))
        canvas.save(output / ('contact-' + str(k // 6 + 1).zfill(2) + '.png'))
    result = {'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pages': pages,
              'records': records, 'page_count': len(reader.pages),
              'scope': 'Changed regions and their bounding neighbour-label pages, not a whole-manuscript review.'}
    (output / 'coverage.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({'regions': len(records), 'rendered_pages': len(pages), 'total_pages': len(reader.pages)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    main(args.bundle, args.out)
