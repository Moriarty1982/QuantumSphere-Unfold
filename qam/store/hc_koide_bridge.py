"""Record the conditional HC-to-Koide interface without equating native frames."""

import hashlib
from pathlib import Path

from qam.store.hc_identification_review import SOURCE, AUDITED_SHA256
from qam.store.koide_review import SOURCE as KOIDE_SOURCE, AUDITED_SHA256 as KOIDE_SHA256
from qam.store.registry import register, register_guard
from qam.store.review_support import SourceReview
from qam.store.snapshots import create_snapshot


def apply_review(database, repo):
    repo = Path(repo).resolve()
    for source, expected in ((SOURCE, AUDITED_SHA256), (KOIDE_SOURCE, KOIDE_SHA256)):
        if hashlib.sha256((repo / source).read_bytes()).hexdigest() != expected:
            raise ValueError('Source changed; bridge self-review must be revisited')
    report = repo / 'notes/research/hc_koide_bridge_review_2026_11_11.md'
    evidence = {'path': report.relative_to(repo).as_posix(),
                'sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
                'revision': 'codex-self-review-2026-11-11', 'locator': 'conditional implication and frame obligations'}
    hc = SourceReview(database, repo, SOURCE, AUDITED_SHA256, evidence)
    koide = SourceReview(database, repo, KOIDE_SOURCE, KOIDE_SHA256, evidence)
    # Exact version lookup rejects missing or ambiguous prerequisites before registration.
    descent = hc.find('hc-reviewed-hc-mass-descent-proof')[0]
    mixing = koide.find('koide-branch-koide-hc-mixing-proof')[0]
    text = (repo / SOURCE).read_text(encoding='utf-8-sig')
    start = text.index('If an independently supplied seed')
    end = text.index(r'\subsection{Obstructions', start)
    source = {'path': SOURCE, 'sha256': AUDITED_SHA256,
              'revision': 'registered-current-source-bytes', 'locator': 'paragraph after v480:hc-mass-descent'}
    bridge = register(database, repo, {'object_id': 'hc-koide-conditional-interface',
        'kind': 'explanation', 'frame': 'hc-root-real-hilbert-comparison',
        'status': 'conditional', 'source': source,
        'payload': {'title': 'Conditional HC descent to the Koide root law',
                    'latex': text[start:end].strip(), 'dependencies': [],
                    'assumptions': [
                        'The Euclidean root space uses the same ordered generation basis as the Koide comparison space.',
                        'An independent seed, positive nonzero principal-root law and independent orthogonality condition must be supplied.']}})['version_hash']
    relations = [hc.reviewed_link(bridge, prerequisite, 'requires', reason)
        for prerequisite, reason in (
            (descent, 'BC=C_m B follows under the real coisometric descent hypotheses.'),
            (mixing, 'Conditional application in the same Euclidean ordered root space: x=alpha C_m e; the explicit bridge assumptions are required.'))]
    obligations = (
        ('Native bridge realization', 'Supply native B, invariant kernel, metric control, independent seed and principal-root law on an admitted state set.'),
        ('Independent HC orthogonality', 'Derive <B*e,JB*e>=0 independently of the target masses; descent alone allows K=1/3.'),
        ('Machine-checkable frame bridge', 'Represent and verify the typed Euclidean root-space identification in the store before suppressing frame-bridge-required.'),
    )
    guards = [register_guard(database, repo, {'subject': bridge, 'target': mixing,
              'title': title, 'obligation': obligation, 'source': evidence})['guard_hash']
              for title, obligation in obligations]
    return {'snapshot_hash': create_snapshot(database, 'hc-koide-conditional-bridge')['snapshot_hash'],
            'roots': [bridge], 'bridge': bridge, 'prerequisites': [descent, mixing],
            'relations': relations, 'guards': guards,
            'review_kind': 'conditional mathematical self-review; native bridge and machine frame typing remain open'}
