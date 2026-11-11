import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from qam.tools.build_v5_documents import finalize_package, log_findings, verify_export


class DocumentBuildTests(unittest.TestCase):
    def test_missing_or_failed_document_never_completes_pair(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'physics.pdf').write_bytes(b'%PDF-physics')
            physics = {'technical_check_passed': True, 'package_pdf': 'physics.pdf'}
            self.assertFalse(finalize_package(root, {'documents': {'physics': physics}}))
            full = {'technical_check_passed': True, 'package_pdf': 'full.pdf'}
            self.assertFalse(finalize_package(root, {'documents': {'physics': physics, 'full': full}}))
            (root / 'full.pdf').write_bytes(b'%PDF-full')
            self.assertFalse(finalize_package(root, {'documents': {'physics': physics,
                'full': {**full, 'technical_check_passed': False}}}))
            self.assertTrue(finalize_package(root, {'documents': {'physics': physics, 'full': full}}))
            result = json.loads((root / 'build-manifest.json').read_text(encoding='utf-8'))
            self.assertFalse(result['publication_ready'])
            self.assertFalse(finalize_package(root, {'error': 'source changed',
                'documents': {'physics': physics, 'full': full}}))

    def test_export_hash_and_path_integrity(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'paper.tex').write_text('original', encoding='utf-8')
            manifest = {'files': {'paper.tex': hashlib.sha256(b'original').hexdigest()},
                        'entrypoint_export': 'paper.tex'}
            (root / 'assembly.json').write_text(json.dumps(manifest), encoding='utf-8')
            verify_export(root)
            (root / 'paper.tex').write_text('changed', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'changed'):
                verify_export(root)
            manifest['files'] = {'../outside.tex': 'anything'}
            (root / 'assembly.json').write_text(json.dumps(manifest), encoding='utf-8')
            with self.assertRaises(ValueError):
                verify_export(root)

    def test_log_diagnostics_preserve_layout_findings(self):
        findings = log_findings("LaTeX Warning: Reference `missing' on page 3 undefined.\n"
            "LaTeX Warning: There were multiply-defined labels.\n"
            "Label(s) may have changed. Rerun to get cross-references right.\n"
            "Overfull \\hbox (2pt too wide)")
        self.assertEqual(findings, {'undefined_references': 1, 'multiply_defined_labels': 1,
                                   'rerun_requests': 1, 'overfull_boxes': 1})
