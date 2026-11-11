# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex). Wird pro Arbeitsblock überschrieben.

- Aktueller Branch codex/v5-layout-fixes, Layout-Codecommit 875a6ad; Basis codex/v5-ci-portability bei 5bc39f8.
- Main bleibt edf1a1c, öffentliche Paper-Baseline v4.11.0; Entwicklung 5.0.0-draft.
- PR #95 (CI-Reparatur) offen und zuletzt vollständig grün; kein neuer Merge freigegeben oder ausgeführt.
- PR #96 (Layout) offen gegen codex/v5-ci-portability: https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/96.
- Layout korrigiert vier Dateien unter sources/research/parts/v470/: 07, 26, 34, 36.
- Lange Protokollpfade umbrechen; breite Boxen mehrzeilig; sechs Tabellen mit Absatzspalten; r54-Abschluss zusammengehalten.
- Historischer Wortlaut, mathematische Symbole, Bedingungen, Labels und Guards erhalten; keine wissenschaftliche Neubewertung.
- Koide-/HC-Reviewquellen weiterhin bytegleich zu ihren festen Sollhashes.
- Lokaler Gesamtbuild build/v5-layout-final-v2/: 1402 Seiten Langfassung, 27 Seiten Physikpaper.
- Beide ohne Overfull-Boxen, offene Verweise, doppelte Labels oder Rerun-Meldungen; vorher lokal 58 Überläufe.
- Physik-LaTeX bytegleich zur vorher vollständig visuell geprüften Ausgabe. Deutsche Lesefassung bleibt unverändert (29 Seiten).
- Neue Quellhashes im gemeinsamen Snapshot registriert; alle Paketprüfsummen nach dem Build kontrolliert.
- 33 Storetests erfolgreich; drei Editionstests nach letztem Satznachzug nochmals erfolgreich.
- Sichtprüfung: 60 Satzstellen über Nachbarlabels eingegrenzt, 56 Prüfseiten in Kontaktbögen, sechs Beispiele groß geprüft.
- Letzte Seitenbindung änderte nur die gerenderten Seiten 1046/1047; beide erneut geprüft. Keine Gesamtsichtung aller 1402 Seiten.
- Prüfbericht notes/research/v5_layout_reflow_2026_11_11.md; Inhaltsdaten v5_layout_reflow_validation_2026_11_11.json.
- Visueller Umfang v5_layout_visual_coverage_2026_11_11.json; QA-PDF/Bilder tmp/v5-layout-qa-final-v2/.
- Einmalskript v5_layout_reflow_2026_11_11.py erwartet exakt die Inventar-Ausgangsbytes; kein Bestandteil des regulären Builds.
- Hilfsskript v5_layout_visual_check_2026_11_11.py nutzt pypdf, Pillow und pdftoppm (gebündelte Laufzeit verfügbar).
- GitHub-Containerprüfung des Layout-Codecommits: Run 43078619869; aktuelle Ergebnisse über GitHub abrufen.
- Plattform-, Lean- und TeX-Prüfungen laufen am PR #96; aktuelle Ergebnisse dort abrufen.
- Lokaler Snapshot: 74a9596b8370c849870e816102181cb3f4aec0802944dd66a1a427029fe223b9.
- full-Edition: 8b1b4b5d803651660d91f95d9eb04af3afbabb007eeb94756b8478f1c77cadb9.
- physics-Edition: 6fdaedf173b3c8ba2f5cbe0bee3711e56cc3405fbe254518e292d3e7e84a162c.
- publication_ready bleibt false und beide incomplete_argument_review bleiben true. Kein Release, Tag, DOI oder Zenodo-Schritt.
- Nächster Schritt: Abschlussstatus von PR #96/Containerprüfung prüfen; PR #95 und danach #96 nur nach Autorenfreigabe mergen.
- Danach fachliche Schlussprüfung und konkrete Zwei-Dokument-Veröffentlichungsunterlagen vorbereiten.
- .codex/environments/ nicht aufnehmen; alte Branchlöschung weiterhin nicht freigegeben.
- Keine H-/k-Nummer vergeben; die historischen Satzinventare mit 58 lokal /45 im früheren Containerlauf bleiben als Vorzustand erhalten.
