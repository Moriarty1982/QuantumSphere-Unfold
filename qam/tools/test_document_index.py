import sqlite3
from contextlib import closing
from pathlib import Path
import tempfile
import unittest

from qam.tools.document_index import ENTRYPOINTS, build_index, occurrences


class DocumentIndexTests(unittest.TestCase):
    def test_comments_verbatim_and_literal_command_variants(self):
        tex = br"""% \begin{verbatim}
\label{real}
\verb|%\ref{verbatim}|
\begin{verbatim}
\ref{hidden}
\end{verbatim}
\hyperref[real]{text} \href{https://example.org/a#b}{source}
\cite[see][p. 4]{one,two} \ref*{real}
"""
        self.assertEqual([(line, command, kind, target)
                          for _, line, _, command, kind, target in occurrences(tex)], [
            (2, 'label', 'label', 'real'),
            (7, 'hyperref', 'label', 'real'),
            (7, 'href', 'external', 'https://example.org/a#b'),
            (8, 'cite', 'citation', 'one'),
            (8, 'cite', 'citation', 'two'),
            (8, 'ref*', 'label', 'real'),
        ])

    def test_full_and_historical_references_are_resolved_separately(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            full, historical = (repo / ENTRYPOINTS[name] for name in ('full', 'historical'))
            full.parent.mkdir(parents=True)
            full.write_bytes(br'\label{same}\ref{same}\ref{history-only}')
            historical.write_bytes(br'\input{historical/part}\ref{same}\includegraphics{missing.pdf}')
            part = historical.parent / 'historical/part.tex'
            part.parent.mkdir()
            part.write_bytes(br'\label{same}\label{history-only}\begin{lemma}Claim.\end{lemma}')
            physics = repo / 'paper.tex'
            physics.write_bytes(br'\cite{entry}\bibitem{entry} Entry')
            database = repo / 'store.sqlite3'
            with closing(sqlite3.connect(database)) as db, db:
                db.execute('CREATE TABLE qstore_sentinel (value TEXT)')
                db.execute("INSERT INTO qstore_sentinel VALUES ('preserve')")
            report = build_index(repo, database, physics)
            self.assertEqual(report, build_index(repo, database, physics))
            with closing(sqlite3.connect(database)) as db:
                ref = "SELECT status, target_source FROM document_links WHERE document=? AND target=?"
                self.assertEqual(db.execute(ref, ('full', 'history-only')).fetchone(), ('unresolved', None))
                self.assertEqual(db.execute(ref, ('historical', 'same')).fetchone(),
                                 ('resolved', 'sources/historical/part.tex'))
                self.assertEqual(db.execute(ref, ('historical', 'missing.pdf')).fetchone(), ('unresolved', None))
                self.assertEqual(db.execute(ref, ('physics', 'entry')).fetchone(),
                                 ('resolved', 'editions/physics/paper.tex'))
                self.assertEqual(db.execute("SELECT content FROM document_sources WHERE source='sources/historical/part.tex'").fetchone(),
                                 (part.read_bytes(),))
                self.assertEqual(db.execute("SELECT COUNT(*) FROM manuscript_inventory WHERE kind='lemma'").fetchone(),
                                 (1,))
                self.assertEqual(db.execute("SELECT value FROM qstore_sentinel").fetchone(), ('preserve',))


if __name__ == '__main__':
    unittest.main()
