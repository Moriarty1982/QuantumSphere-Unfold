"""Bounded static checks of literal LaTeX references in a pinned selection."""

import re

from qam.store.latex_resources import resource_groups
from qam.store.registry import digest


REFERENCES = {'ref', 'eqref', 'pageref', 'autoref', 'cref', 'Cref'}
CITATIONS = {'cite', 'citep', 'citet', 'nocite'}

# Deliberately bounded contract for article + the exporter's fixed amsmath preamble.
CORE_COMMANDS = set('''begin end newcommand label ref eqref pageref cite nocite
frac dfrac tfrac sqrt binom dbinom tbinom left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr mathrm mathcal mathbf mathit mathsf
mathtt mathnormal boldsymbol text textrm textbf textit textsf texttt emph rm
operatorname DeclareMathOperator overline underline bar hat widehat tilde widetilde
vec dot ddot ddots dots cdots ldots vdots phantom hphantom vphantom
sum prod int iint iiint oint lim sup inf max min log ln exp sin cos tan sinh cosh
ker dim det rank gcd hom mod bmod pmod partial nabla infty arcsin arccos arctan
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
le leq ge geq ne neq equiv sim simeq approx cong subset subseteq superset supset supseteq
in notin ni cup cap setminus emptyset forall exists neg land lor implies iff
to mapsto rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow
cdot times otimes oplus circ bullet ast star pm mp div perp parallel mid
langle rangle lvert rvert lVert rVert vert Vert quad qquad hspace vspace
nonumber notag tag displaystyle textstyle scriptstyle scriptscriptstyle
section subsection paragraph item par noindent smallskip medskip bigskip
small footnotesize normalsize large Large textsuperscript textsuperscript
newblock bibitem footnote centering hline cline multicolumn hfill vfill
underbrace overbrace underset overset substack stackrel not limits nolimits
endinput'''.split())
PACKAGE_COMMANDS = {
    'amssymb': {'mathbb', 'mathfrak', 'leqslant', 'geqslant', 'varnothing', 'nexists', 'square', 'blacksquare'},
    'amsthm': {'qed', 'qedhere'},
    'array': {'extrarowheight'},
}
CORE_ENVIRONMENTS = {'equation', 'equation*', 'align', 'align*', 'aligned', 'gather', 'gather*',
                     'gathered', 'split', 'multline', 'multline*', 'cases', 'matrix', 'pmatrix',
                     'bmatrix', 'Bmatrix', 'vmatrix', 'Vmatrix', 'smallmatrix', 'array',
                     'tabular', 'itemize', 'enumerate', 'description', 'quote', 'center'}


def commands(text):
    """Scan control words, skipping comments and escaped control symbols."""
    index = 0
    while index < len(text):
        if text[index] == '%':
            end = text.find('\n', index)
            index = len(text) if end < 0 else end + 1
        elif text[index] == '\\':
            match = re.match(r'\\([A-Za-z@]+)', text[index:])
            if match:
                end = index + match.end()
                yield match.group(1), end
                index = end
            else:
                index += 2
        else:
            index += 1


def scrub(selection):
    issues = []
    labels = {}
    citations = []
    references = []
    try:
        packages, macros, bibliography = resource_groups(selection['objects'])
    except ValueError as exc:
        result = {'format': 'qstore-scrub-v1', 'result': 'blocked',
                  'issues': [{'kind': 'resource-conflict', 'message': str(exc)}],
                  'selection_hash': selection['selection_hash']}
        return {'report_hash': digest(result), **result}
    bibkeys = {item['payload']['key'] for item in bibliography}
    known = CORE_COMMANDS | REFERENCES | CITATIONS
    for package in packages:
        known |= PACKAGE_COMMANDS.get(package, set())
    # Names from optional reference packages require resources not yet supported.
    known -= {'citep', 'citet', 'autoref', 'cref', 'Cref', 'rank', 'url'}
    macro_names = {item['payload']['name'] for item in macros}
    for name in sorted(macro_names & known):
        issues.append({'kind': 'macro-name-conflict', 'command': name})
    known |= macro_names
    environments = CORE_ENVIRONMENTS | ({'proof'} if 'amsthm' in packages else set())
    macro_graph = {}
    for macro in macros:
        name = macro['payload']['name']
        # Skip the declared name itself, which follows newcommand in the scanner.
        calls = list(commands(macro['payload']['latex']))[2:]
        macro_graph[name] = {command for command, _ in calls if command in macro_names}
    active_macros = set()
    visited_macros = set()

    def visit_macro(name):
        if name in active_macros:
            issues.append({'kind': 'recursive-macro', 'command': name})
            return
        if name in visited_macros:
            return
        active_macros.add(name)
        for target in sorted(macro_graph[name]):
            visit_macro(target)
        active_macros.remove(name)
        visited_macros.add(name)

    for name in sorted(macro_graph):
        visit_macro(name)
    for obj in selection['objects']:
        key = obj['version_hash']
        if obj['kind'] != 'latex-resource':
            labels['qv-' + key] = key
    for obj in selection['objects']:
        key = obj['version_hash']
        text = obj['payload'].get('latex', '')
        for name, end in commands(text):
            if name not in known:
                issues.append({'kind': 'unresolved-command', 'command': name, 'version': key})
            if name in {'begin', 'end'}:
                environment = re.match(r'\s*\{([^{}]*)\}', text[end:])
                if environment is None or environment.group(1) not in environments:
                    issues.append({'kind': 'unsupported-environment', 'version': key,
                                   'environment': environment.group(1) if environment else None})
            if name in {'input', 'include', 'includegraphics', 'bibliography', 'addbibresource', 'verb', 'catcode'}:
                issues.append({'kind': 'unsupported-external-or-dynamic-tex', 'command': name, 'version': key})
            if name == 'begin' and re.match(r'\s*\{(?:verbatim|Verbatim|lstlisting|minted)\}', text[end:]):
                issues.append({'kind': 'unsupported-verbatim-environment', 'version': key})
            if name not in REFERENCES | CITATIONS | {'label'}:
                continue
            match = re.match(r'\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^{}]*)\}', text[end:])
            if match is None:
                issues.append({'kind': 'unsupported-reference-syntax', 'command': name, 'version': key})
                continue
            argument = match.group(1).strip()
            targets = argument.split(',') if name in CITATIONS | {'cref', 'Cref'} else [argument]
            for target in targets:
                target = target.strip()
                if name == 'nocite' and target == '*':
                    continue
                if not re.fullmatch(r'[A-Za-z0-9:._-]+', target):
                    issues.append({'kind': 'nonliteral-reference', 'command': name, 'version': key})
                elif name == 'label':
                    if target in labels:
                        issues.append({'kind': 'duplicate-label', 'label': target, 'version': key})
                    else:
                        labels[target] = key
                elif name in CITATIONS:
                    citations.append((target, key))
                else:
                    references.append((target, key))
    for target, key in citations:
        if target not in bibkeys:
            issues.append({'kind': 'missing-citation', 'target': target, 'version': key})
    for target, key in references:
        if target not in labels:
            issues.append({'kind': 'missing-label', 'target': target, 'version': key})
    result = {'format': 'qstore-scrub-v1', 'selection_hash': selection['selection_hash'],
              'result': 'blocked' if issues else 'passed', 'issues': issues,
              'counts': {'labels': len(labels), 'references': len(references), 'citations': len(citations)},
              'scope': 'Literal references, declared macros, a bounded command/environment catalogue and '
                       'direct macro recursion; general TeX expansion and mathematical validity require separate checks'}
    return {'report_hash': digest(result), **result}
