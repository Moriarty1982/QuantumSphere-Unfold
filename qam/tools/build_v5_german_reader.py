"""Assemble the personal German translation, preserving all source math verbatim."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

MATH = re.compile(r'\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}|\\\[.*?\\\]|\$(?:\\.|[^$])*?\$', re.S)
TOKEN = re.compile(r'@@(\d+)@@')
KEYS = ('question', 'core', 'method', 'particles', 'masses', 'geometry', 'limits')


def protect(text):
    maths = []
    def replace(match):
        maths.append(match.group())
        return '@@' + str(len(maths) - 1) + '@@'
    return MATH.sub(replace, text), maths


def source_parts(repo, english):
    parts = {'base': (repo / 'qam/editions/v5_physics_article.tex').read_text(encoding='utf-8')}
    parts.update({key: (repo / ('qam/editions/v5_expanded_' + key + '.tex')).read_text(encoding='utf-8') for key in KEYS})
    parts['appendix'] = english[english.index(r'\clearpage' + '\n' + r'\appendix'):english.index(r'\end{document}')]
    return parts


def build(source, destination):
    repo = Path(__file__).resolve().parents[2]
    english = Path(source).read_text(encoding='utf-8')
    translations = repo / 'qam/editions/de'
    lock = json.loads((translations / 'sources.json').read_text(encoding='utf-8'))
    if hashlib.sha256(english.encode()).hexdigest() != lock['english_tex_sha256']:
        raise ValueError('English edition changed: review the translation before rebuilding')
    parts = source_parts(repo, english)
    translated = {}
    for key, original in parts.items():
        if hashlib.sha256(original.encode()).hexdigest() != lock['parts'][key]:
            raise ValueError('Translation source changed: ' + key)
        _, maths = protect(original)
        template = (translations / (key + '.tex.in')).read_text(encoding='utf-8')
        if Counter(TOKEN.findall(template)) != Counter(str(i) for i in range(len(maths))):
            raise ValueError('Missing or repeated mathematical fragment in ' + key)
        translated[key] = TOKEN.sub(lambda m: maths[int(m[1])], template)
    base = dict(re.findall(r'% section:(\w+)\n(.*?)(?=% section:|\Z)', translated['base'], re.S))
    titles = ('Einleitung', 'Ein graduierter Träger und seine Interpretation',
              'Aussagensprache und Nachvollziehbarkeit', 'Teilchen- und Generationenzuordnungen',
              'Massenauslesung und Konsistenzbedingungen', 'Projizierte Dynamik und Geometrie',
              'Diskussion und Ausblick')
    preamble = english[:english.index(r'\begin{document}')]
    preamble = re.sub(r'\\title\{[^\n]+', r'\\title{Graduierte Träger und physikalische Auslesungen: Bedingungen für die Interpretation von Massen und Geometrie}', preamble)
    preamble = preamble.replace('Independent Researcher, Bochum, Germany', 'Unabhängiger Forscher, Bochum, Deutschland')
    preamble = preamble.replace('Working paper', 'Arbeitsfassung').replace('11 November 2026; not peer reviewed', '11. November 2026; nicht begutachtet, deutsche Lesefassung')
    preamble += '\\usepackage[ngerman]{babel}\n'
    bibliography = english[english.index(r'\begin{thebibliography}'):english.index(r'\end{thebibliography}') + len(r'\end{thebibliography}')]
    body = [preamble, r'\begin{document}', r'\maketitle', r'\begin{abstract}', base['abstract'], r'\end{abstract}']
    for key, title in zip(KEYS, titles):
        body += [r'\section{\raggedright ' + title + '}', base[key], translated[key]]
    body += [bibliography, translated['appendix'], r'\end{document}', '']
    result = '\n'.join(body)
    # Protect the entire mathematical content, not just displayed equations.
    if Counter(protect(result)[1]) != Counter(protect(english)[1]):
        raise ValueError('Mathematical content differs from the English edition')
    # Translate a table caption inside math mode, leaving the algebra untouched.
    result = result.replace(r'\text{multiplicity}', r'\text{Vielfachheit}')
    result = result.replace('accessed 11 November 2026', 'abgerufen am 11. November 2026')
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    (destination / 'paper.tex').write_text(result, encoding='utf-8')
    manifest = {'language': 'de', 'purpose': 'personal reading translation',
                'english_source': lock, 'math_fragments_preserved': len(protect(english)[1]),
                'localized_math_text': {'multiplicity': 'Vielfachheit'},
                'translated_tex_sha256': hashlib.sha256(result.encode()).hexdigest(),
                'translations': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in translations.iterdir() if p.is_file()}}
    (destination / 'translation.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'output': str(destination), 'math_fragments_preserved': manifest['math_fragments_preserved']}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='Exported English physics paper.tex')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    build(args.source, args.out)
