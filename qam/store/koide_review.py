"""Apply the explicit, source-pinned Koide self-review to registered branch versions."""

import hashlib
import json
from pathlib import Path
import re

from sqlalchemy import select

from qam.store.orm import store_session
from qam.store.registry import register, register_link, register_guard, register_review, latest_review
from qam.store.snapshots import create_snapshot


SOURCE = 'sources/research/parts/koide-and-kernel.tex'
AUDITED_SHA256 = '63fe03eb53ec883292ac09935f65fc04bb4a9f6e7a32870743471cdc294336c7'
LABELS = ('koide-equal-norm', 'koide-hc-mixing', 'koide-radius-phase', 'koide-equivariant-obstruction')


def apply_review(database, repo):
    repo = Path(repo).resolve()
    if hashlib.sha256((repo / SOURCE).read_bytes()).hexdigest() != AUDITED_SHA256:
        raise ValueError('Source changed; the recorded self-review must be revisited')
    report = repo / 'notes/research/koide_store_branch_review_2026_11_11.md'
    evidence = {'path': report.relative_to(repo).as_posix(),
                'sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
                'revision': 'codex-self-review-2026-11-11', 'locator': 'four claim cards and proof obligations'}

    def find(object_id):
        with store_session(database) as (session, models):
            rows = list(session.scalars(select(models.qstore_versions).where(models.qstore_versions.object_id == object_id)))
            valid = []
            for row in rows:
                sources = list(session.scalars(select(models.qstore_sources).where(models.qstore_sources.version_hash == row.version_hash)))
                if any(item.source_path == SOURCE and item.source_hash == AUDITED_SHA256 for item in sources):
                    valid.append((row.version_hash, json.loads(row.payload_json)))
            if len(valid) != 1:
                raise ValueError(f'Expected one source-pinned version of {object_id}')
            return valid[0]

    def assess(kind, subject, status, reason):
        with store_session(database) as (session, models):
            previous = latest_review(session, models, kind, subject)
            if previous:
                payload = json.loads(previous.payload_json)
                if previous.status == status and payload['reason'] == reason and payload['evidence'] == evidence:
                    return previous.review_hash
            previous_hash = previous.review_hash if previous else None
        return register_review(database, repo, {'kind': kind, 'subject': subject, 'previous': previous_hash,
            'status': status, 'reviewer': 'Codex self-review 2026-11-11', 'reason': reason, 'evidence': evidence})['review_hash']

    def reviewed_link(source, target, kind, reason):
        key = register_link(database, {'source': source, 'target': target, 'kind': kind,
                                     'status': 'declared', 'description': reason})['relation_hash']
        assess('relation', key, 'reviewed', reason)
        return key

    # Complete every documentary check before writing the reviewed associations.
    pairs = []
    for label in LABELS:
        imported, raw = find('manuscript:' + SOURCE + ':label:v480:' + label)
        curated, statement = find('koide-branch-' + label)
        proof, proof_payload = find('koide-branch-' + label + '-proof')
        normalized = raw['latex'].replace('\r\n', '\n').strip()
        header = re.match(r'\\begin\{proposition\}(?:\[[^\]]*\])?\s*', normalized)
        if not header or not normalized.endswith(r'\end{proposition}'):
            raise ValueError('Unsupported imported proposition wrapper')
        body = normalized[header.end():-len(r'\end{proposition}')].strip()
        if body != statement['latex'].replace('\r\n', '\n').strip():
            raise ValueError('Imported and curated proposition contents differ')
        source_text = (repo / SOURCE).read_text(encoding='utf-8-sig')
        if proof_payload['latex'].replace('\r\n', '\n') not in source_text:
            raise ValueError('Curated proof no longer matches its source')
        pairs.append({'label': label, 'imported': imported, 'claim': curated, 'proof': proof})

    definitions = {}
    descriptions = {
        'principal-roots': ('Principal-root comparison domain',
            'A nonzero triple of real nonnegative principal mass roots. A is its positive arithmetic mean; u is the constant triple with entry A; d is x-u.'),
        'hc-representation': ('Declared real HC representation',
            'On Euclidean real three-space, e is the normalized symmetric vector, J_m is an orthogonal involution and C_m=(I+J_m)/2. The output alpha C_m e is assumed nonzero and componentwise nonnegative with alpha positive.'),
        'cyclic-linear': ('Cyclic linear comparison domain',
            'P cyclically permutes three real coordinates. T is a real linear map commuting with P. Its input lies on the line of constant triples.'),
    }
    for key, (title, body) in descriptions.items():
        definitions[key] = register(database, repo, {'object_id': 'koide-reviewed-definition-' + key,
            'kind': 'definition', 'frame': 'koide-principal-root-comparison', 'status': 'declared',
            'source': evidence, 'payload': {'title': title, 'body': body,
                'scope': 'Explicit local mathematical interpretation of the source-pinned claim cards', 'assumptions': []}})['version_hash']
    roots = [find('koide-branch-root-setup')[0]]
    associations = []
    import_guards = []
    for index, pair in enumerate(pairs):
        associations.append(reviewed_link(pair['imported'], pair['claim'], 'same-source-as',
            'Exact source-content match after removing the proposition wrapper; curated abstract frame is a separate declared interpretation'))
        reviewed_link(pair['proof'], pair['claim'], 'proves',
            'Self-reviewed original proof establishes this exact statement under its explicit mathematical hypotheses')
        domain_keys = ['cyclic-linear'] if index == 3 else ['principal-roots']
        if index == 1:
            domain_keys.append('hc-representation')
        for key in domain_keys:
            reviewed_link(pair['claim'], definitions[key], 'interpreted-by',
                'Source-pinned claim card uses this explicit abstract domain; native physical interpretation remains open')
        with store_session(database) as (session, models):
            old_guards = [row.guard_hash for row in session.scalars(select(models.qstore_guards).where(
                models.qstore_guards.subject_version == pair['imported']))]
        import_guards.extend(old_guards)
        roots += [pair['claim'], pair['proof'], find('koide-branch-' + pair['label'] + '-discussion')[0]]
    # K4 is self-contained on real linear three-space; principal-root positivity is unnecessary.
    setup = roots[0]
    with store_session(database) as (session, models):
        redundant = [row.relation_hash for row in session.scalars(select(models.qstore_relations).where(
            models.qstore_relations.source_version == pairs[3]['claim'],
            models.qstore_relations.target_version == setup,
            models.qstore_relations.relation_type == 'requires'))]
    for key in redundant:
        assess('relation', key, 'rejected', 'K4 needs only the real cyclic-linear domain, not principal-root positivity')
    mathematical_nodes = {pair[role] for pair in pairs for role in ('claim', 'proof')}
    with store_session(database) as (session, models):
        prerequisite_keys = [row.relation_hash for row in session.scalars(select(models.qstore_relations))
            if row.relation_type == 'requires' and row.source_version in mathematical_nodes
            and row.relation_hash not in redundant]
    for key in prerequisite_keys:
        assess('relation', key, 'reviewed',
            'Self-review confirms this local mathematical or proof-environment dependency under the source-pinned claim card; native physical identification is separate')
    obligations = [
        ('Native principal-root readout', pairs[1]['claim'], 'Derive a native three-generation principal-root readout with positivity, nonzero output and a common generation basis.'),
        ('Independent equal-norm selection', pairs[0]['claim'], 'Derive equal symmetric and orthogonal norms, or the HC condition h=0, independently of the target masses.'),
        ('Physical phase and mass scale', pairs[2]['claim'], 'Determine the admissible phase and mass scale from native dynamics; Koide radius alone leaves both free.'),
        ('Native hierarchy mechanism', pairs[3]['claim'], 'Identify an independently specified asymmetric source or coupling that evades the cyclic-equivariant linear obstruction.'),
    ]
    guards = [register_guard(database, repo, {'subject': subject, 'target': None,
              'title': title, 'obligation': text, 'source': evidence})['guard_hash']
              for title, subject, text in obligations]
    for key in import_guards:
        assess('guard', key, 'satisfied',
            'Source, hypotheses, original proof and technical resources mapped to the curated abstract version. '
            'The raw import metadata stays unspecified; native obligations are separately open. Standalone raw export was not approved.')
    snapshot = create_snapshot(database, 'koide-source-and-proof-self-review')['snapshot_hash']
    return {'snapshot_hash': snapshot, 'roots': roots, 'pairs': pairs, 'definitions': definitions,
            'source_associations': associations, 'native_guards': guards,
            'review_kind': 'source-pinned Codex self-review; no formal proof-assistant certificate'}
