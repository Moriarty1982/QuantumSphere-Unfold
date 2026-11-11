"""Register and self-review the five source-pinned abstract HC propositions."""

import hashlib
from pathlib import Path
import re
from sqlalchemy import select
from qam.store.orm import store_session

from qam.store.registry import register, register_guard
from qam.store.review_support import SourceReview
from qam.store.snapshots import create_snapshot

SOURCE = 'sources/research/parts/hc-mass-identification.tex'
AUDITED_SHA256 = '4a2cecf409f75355ea3c49e8191993a4cb4019d8c997eb0a64e4674a62301f4c'
LABELS = ('hc-mass-descent', 'hc-mass-odd-obstruction', 'hc-mass-equivariant-obstruction',
          'hc-mass-triole-bound', 'hc-mass-fit-freedom')


def apply_review(database, repo):
    repo = Path(repo).resolve()
    path = repo / SOURCE
    if hashlib.sha256(path.read_bytes()).hexdigest() != AUDITED_SHA256:
        raise ValueError('Source changed; the recorded self-review must be revisited')
    text = path.read_text(encoding='utf-8-sig')
    report = repo / 'notes/research/hc_identification_store_review_2026_11_11.md'
    evidence = {'path': report.relative_to(repo).as_posix(),
                'sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
                'revision': 'codex-self-review-2026-11-11', 'locator': 'H1 through H5 and native obligations'}
    source = {'path': SOURCE, 'sha256': AUDITED_SHA256,
              'revision': 'registered-current-source-bytes', 'locator': 'five HC identification propositions'}
    review = SourceReview(database, repo, SOURCE, AUDITED_SHA256, evidence)
    # Validate all raw imports before introducing any curated versions.
    extracted = []
    for label in LABELS:
        imported, raw = review.find('manuscript:' + SOURCE + ':label:v480:' + label)
        at = text.index(r'\label{v480:' + label + '}')
        start = text.rfind(r'\begin{proposition}', 0, at)
        end = text.index(r'\end{proposition}', at)
        header = re.match(r'\\begin\{proposition\}(?:\[[^\]]*\])?\s*', text[start:])
        body = text[start + header.end():end].strip()
        normalized = raw['latex'].replace('\r\n', '\n').strip()
        if normalized != text[start:end + len(r'\end{proposition}')].strip():
            raise ValueError('Imported HC proposition differs from audited source')
        pstart = text.index(r'\begin{proof}', end)
        pend = text.index(r'\end{proof}', pstart) + len(r'\end{proof}')
        extracted.append((label, imported, body, text[pstart:pend]))
    frame = 'hc-root-real-hilbert-comparison'
    packages = [register(database, repo, {'object_id': 'hc-reviewed-package-' + name,
        'kind': 'latex-resource', 'frame': frame, 'status': 'declared', 'source': source,
        'payload': {'title': name, 'package': name, 'assumptions': []}})['version_hash']
        for name in ('amsthm', 'amssymb')]
    domains = (
        'Real Hilbert H, orthogonal involution J, C=(I+J)/2; bounded coisometry B to Euclidean real three-space with J-invariant kernel.',
        'Real HC involution and its even projector. The descended-route clause additionally assumes H1 and a seed whose image is the normalized symmetric vector e.',
        'An admitted set stable under U; a map F equivariant for U and cyclic coordinate permutation P. The tested input is fixed by U. No linearity of F is assumed.',
        'Three vectors in any normed space sum to zero and are not all zero. Masses are their squared norms times one common positive coupling.',
        'Nonzero nonnegative real root triple x and normalized symmetric e=(1,1,1)/sqrt(3). The projector and involution are constructed from this prescribed x.',
    )
    definitions, pairs, roots = [], [], []
    for index, (label, imported, body, proof_text) in enumerate(extracted):
        definition = register(database, repo, {'object_id': 'hc-reviewed-domain-' + label,
            'kind': 'definition', 'frame': frame, 'status': 'declared', 'source': evidence,
            'payload': {'title': 'Local domain: ' + label, 'body': domains[index],
                        'scope': 'Abstract mathematical comparison; no native physical identification', 'assumptions': []}})['version_hash']
        definitions.append(definition)
        def block(suffix, kind, latex, dependencies):
            return register(database, repo, {'object_id': 'hc-reviewed-' + label + suffix,
                'kind': kind, 'frame': frame, 'status': 'conditional', 'source': source,
                'payload': {'title': label + suffix, 'latex': latex, 'dependencies': dependencies,
                            'assumptions': []}})['version_hash']
        claim = block('', 'claim', body, [pairs[0]['claim']] if index == 1 else [])
        proof = block('-proof', 'proof', proof_text, [claim] + packages)
        review.reviewed_link(imported, claim, 'same-source-as',
            'Exact source-content match; curated abstract domain is separately declared and raw metadata remains unspecified')
        review.reviewed_link(claim, definition, 'interpreted-by', domains[index])
        review.reviewed_link(proof, claim, 'proves',
            'Source-pinned self-review establishes the statement under its explicit hypotheses; no native mass law follows')
        pairs.append({'label': label, 'imported': imported, 'claim': claim, 'proof': proof})
        roots += [claim, proof]
    with store_session(database) as (session, models):
        prerequisites = [row.relation_hash for row in session.scalars(select(models.qstore_relations))
                         if row.source_version in roots and row.relation_type == 'requires']
    for key in prerequisites:
        review.assess('relation', key, 'reviewed',
                      'Self-reviewed mathematical or proof-environment prerequisite; physical identification remains open')
    obligations = (
        ('Native scalar and HC interpretation', 0, 'Construct the native real or complex carrier and distinguish linear orthogonal HC from antiunitary operations.'),
        ('Native mass-root descent', 0, 'Supply B, its domain, coisometry, invariant kernel, independent seed and physical principal-root readout with positivity.'),
        ('Native generation coupling', 3, 'Derive the residual coupling and generation states with their domains if the residual route is used.'),
        ('Independent selection, phase and scale', 4, 'Derive norm selection, phase and mass scale without fitting the operator to prescribed masses.'),
    )
    guards = [register_guard(database, repo, {'subject': pairs[index]['claim'], 'target': None,
              'title': title, 'obligation': obligation, 'source': evidence})['guard_hash']
              for title, index, obligation in obligations]
    return {'snapshot_hash': create_snapshot(database, 'hc-identification-self-review')['snapshot_hash'],
            'roots': roots, 'pairs': pairs, 'definitions': definitions, 'native_guards': guards,
            'review_kind': 'source-pinned Codex self-review; no formal or native-physics certificate'}
