"""Phase 2 of the counterterm registry: LaTeX registry appendix and guard notes (fixture CT-000-TEST only)."""

import json
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.store.counterterms import check_residual, register_scheme, register_transition
from qam.store.latex_export import (ENTRY_MARK, NOTE_MARK, counterterm_export_issues, export_selection, render)
from qam.store.registry import register_link
from qam.store.selection import select_versions
from qam.store.snapshots import create_snapshot
from qam.store import test_counterterms as phase1

# Valid LaTeX text so that the exported draft compiles (the Phase 1 fixture text uses bare underscores).
CLAIM = 'Dummy statement S0 uses the placeholder delta0.'
FOLLOWER = 'Dummy statement S1 requires S0.'
CORE = 'Dummy core statement C0 has no compensation term.'


class CountertermExportTests(unittest.TestCase):
    def setUp(self):
        # Reuse the Phase 1 fixture helpers (temporary store, source file, CT-000-TEST payload).
        self.base = phase1.CountertermRegistryTests('test_schema_v7_and_upgrade_from_v6')
        self.base.setUp()
        self.db, self.root = self.base.db, self.base.root
        lines = [CLAIM, FOLLOWER, CORE, 'Mock structure function F0.']
        self.base.source.write_text(chr(10).join(lines), encoding='utf-8')

    def tearDown(self):
        self.base.tearDown()

    def build(self):
        scheme = register_scheme(self.db, self.root, self.base.scheme_request())['version_hash']
        claim = self.base.statement('S_0', CLAIM)
        follower = self.base.statement('S_1', FOLLOWER, [claim])
        core = self.base.statement('C_0', CORE)
        register_link(self.db, {'source': claim, 'target': scheme, 'kind': 'depends-on-counterterm',
                                'status': 'declared', 'description': 'S_0 uses delta_0'})
        register_link(self.db, {'source': follower, 'target': claim, 'kind': 'requires',
                                'status': 'declared', 'description': 'S_1 requires S_0'})
        return scheme, claim, follower, core

    def selection(self, roots, name):
        snapshot = create_snapshot(self.db, name)['snapshot_hash']
        return select_versions(self.db, snapshot, roots)

    def test_appendix_notes_and_hard_audit(self):
        scheme, claim, follower, core = self.build()
        selection = self.selection([follower, core], 'export-1')
        self.assertEqual([item['scheme'] for item in selection['counterterms']], [scheme])
        state = selection['counterterms'][0]
        self.assertEqual((state['status'], state['inherits_guards']), ('placeholder', True))
        self.assertEqual(sorted(guard['title'] for guard in state['open_guards']),
                         ['GUARD-CT000-NO-DERIVATION', 'GUARD-LOCAL-READOUT-ONLY'])
        tex = render(selection)
        # Notes on S_0 and on S_1 (transitive through requires), none on the core statement C_0.
        self.assertIn(NOTE_MARK + claim, tex)
        self.assertIn(NOTE_MARK + follower, tex)
        self.assertNotIn(NOTE_MARK + core, tex)
        self.assertIn(ENTRY_MARK + scheme, tex)
        self.assertIn('Counterterm and compensation registry', tex)
        self.assertIn('GUARD-CT000-NO-DERIVATION', tex)
        self.assertIn('Comparisons with these data are not blind', tex)
        # The scheme is not rendered as a body section.
        self.assertNotIn(r'\section{CT-000-TEST', tex)
        self.assertEqual(counterterm_export_issues(selection, tex), [])
        stripped = tex.replace(NOTE_MARK + follower, '')
        self.assertEqual([item['kind'] for item in counterterm_export_issues(selection, stripped)],
                         ['counterterm-note-missing'])
        stripped = tex.replace(ENTRY_MARK + scheme, '')
        self.assertEqual([item['kind'] for item in counterterm_export_issues(selection, stripped)],
                         ['counterterm-entry-missing'])
        result = export_selection(selection, self.root / 'out')
        written = (Path(result['directory']) / 'paper.tex').read_text(encoding='utf-8')
        self.assertEqual(written, tex)
        if shutil.which('pdflatex'):
            run = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-no-shell-escape',
                                  'paper.tex'], cwd=result['directory'], capture_output=True, text=True, timeout=180)
            self.assertEqual(run.returncode, 0, run.stdout[-2000:])

    def test_structurally_matched_entry_and_stable_hash_without_counterterms(self):
        scheme, claim, follower, core = self.build()
        plain = self.selection([core], 'export-plain')
        self.assertNotIn('counterterms', plain)
        close = self.base.structure('F_0', ['21/200', '1/2'])
        receipt = check_residual(self.db, {'scheme': scheme, 'replacement': close})
        step = self.base.transition(scheme, None, 'partially_constrained')
        self.base.transition(scheme, step['transition_hash'], 'structurally_matched', close, receipt['receipt_hash'])
        selection = self.selection([claim], 'export-2')
        state = selection['counterterms'][0]
        self.assertEqual((state['status'], state['inherits_guards'], state['replacement']),
                         ('structurally_matched', False, close))
        tex = render(selection)
        self.assertIn('structurally matched, see the registry appendix', tex)
        self.assertIn('Matching identity F\\_struct = delta\\_eff + Delta', tex)
        self.assertNotIn('Open guard GUARD-CT000-NO-DERIVATION', tex)
        self.assertEqual(counterterm_export_issues(selection, tex), [])
        self.assertEqual(json.loads(json.dumps(selection))['counterterms'][0]['transitions'], state['transitions'])


if __name__ == '__main__':
    unittest.main()
