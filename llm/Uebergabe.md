# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex). Wird pro Arbeitsblock überschrieben.

- Branch codex/v5-release-prep; Basis vor diesem Block 01ca2a8.
- Main bleibt PR94 / 3a68669b0b12766c256ae6eeed1f52ae0693acc4; öffentliche Baseline v4.11.0.
- Entwicklung v5.0.0-draft, keine eigene DOI oder Veröffentlichung.
- Folgeauftrag weiter: gemeinsamen Zwei-Dokument-Build eingerichtet und lokal vollständig geprüft.
- Werkzeug: python -m qam.tools.build_v5_documents --out NEUER_ORDNER.
- Workflow .github/workflows/qsc-v5-dual-documents.yml: manuell oder passende Änderungen auf main; GitHub-Ausführung noch nicht geprüft.
- Ausgabe build/v5-paired-documents-final/: Lang-PDF 1397 Seiten, englisches Physikpaper 27 Seiten.
- Langfassung drei Satzläufe, Physik zwei; beide ohne offene Verweise, doppelte Labels oder Rerun-Meldungen.
- 58 Overfull-Boxen im Langtext, keine im Physikpaper. Diese sind nicht bereinigt und bleiben redaktionell offen.
- Physik-LaTeX bytegleich zur vollständig visuell geprüften Vorfassung; Langfassung nur Titel, Leseführung und Schluss visuell geprüft.
- Paket: PDFs, frische Datenbank, Quellbaum, Auswahl-/Auditmanifeste, Compilerprotokolle, Builderquellen, README und SHA256SUMS.
- Alle verzeichneten Prüfsummen nach dem Lauf geprüft.
- build_complete=true bedeutet technische Paar-Vollständigkeit. publication_ready bleibt false; beide incomplete_argument_review bleiben true.
- Keine neue mathematische Beweisfreigabe, native Identifikation oder OP-Schließung.
- 32 Storetests erfolgreich; neue Fehlerfallprüfungen verhindern vollständigen Status bei fehlendem/fehlgeschlagenem Dokument oder geänderter Quelle.
- Compiler verwendet pdflatex direkt ohne Shell-Escape, bis zu sechs Läufe. latexmk scheiterte lokal an fehlendem Perl.
- Bericht notes/research/v5_dual_document_build_2026_11_11.md enthält genaue Buildidentitäten.
- Snapshot: 168977e6c8ec955214fc5463769eb2ae709d0815dc6cee38d3d1e05245cb0f67.
- full-Edition: 07b52fadd6c9e325a04b06f0d391f921bbb073c15292851c97d5cd42cf3c53f2.
- physics-Edition: 740eef6f937c78046d492df36fb4760527b00cb010075bd123aa0e31bb093380.
- Redaktionelle englische Physiktexte qam/editions/v5_expanded_*.tex; Originalbeweise und Runden unverändert.
- Deutsche persönliche Lesefassung: build/qam-v5-physics-de-final/paper.pdf, 29 Seiten, alle visuell geprüft.
- Deutsche Quellen qam/editions/de/, Builder qam.tools.build_v5_german_reader; 640 mathematische Fragmente erhalten.
- Deutsche Fassung ist kein Datenbank-Sprachprofil; ihre englische Vorlage bleibt 1db88536ab67af7a1087fb999f63ef46ccfb9a0f8d22335c8969cf51a306c1d8.
- Der gespeicherte MMA-Intervallbeleg bleibt bedingt, closure_proved und mathematical_relations_proved false.
- Nächster Schritt: 58 Satzüberläufe im Langtext nach Fundstelle/Art erfassen und korrigieren; danach fachliche Schlussprüfung und Workflow-Prüfung.
- Kein Main-Merge, Tag, DOI, Zenodo-Entwurf, Upload oder Release in diesem Block.
- Branchlöschung bleibt durch automatische Freigabeprüfung blockiert; Liste notes/research/v5_0_0_branch_cleanup_review.md, keine neue Freigabe.
- .codex/environments/ nicht aufnehmen. Keine H-/k-Nummer vergeben.
