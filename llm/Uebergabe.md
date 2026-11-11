# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex).

- Branch codex/v5-release-prep; letzter Commit vor diesem Block 8edd317.
- Main/Basis bleibt PR94 / 3a68669b0b12766c256ae6eeed1f52ae0693acc4.
- Autorenkritik: Physikfassung liest sich wie Datenbankbericht. Redaktionell zu wissenschaftlichem Artikel überarbeitet.
- Neue Textquellen: qam/editions/v5_physics_article.tex und v5_physics_references.tex.
- Neuer Renderer qam/store/physics_paper.py; technische Auditdarstellung weiterhin für alte Editionen verfügbar.
- Editionsformat v2 ergänzt optionale presentation mit style=physics-paper, Autor, Version, registrierter Abstractversion. Schema unverändert v6.
- Sieben Abschnitte: Einleitung, Träger, Methode, Teilchen/Generationen, Massenauslesung, Dynamik/Geometrie, Diskussion.
- Abstract, wissenschaftliche Prosa, nummerierte Gleichungen, vier Literaturangaben; Koide-/HC-Originalbeweise in Anhang A.
- Keine Versionshashes, Frame-Statuslisten oder einzelnen Checkresultate im Haupttext. Diese stehen vollständig in audit.md und assembly.json.
- Wissenschaftliche Voraussetzungen/Grenzen bleiben im Haupttext; Rohimporte erhalten keinen neuen Beweisstatus.
- Physikhash: c384db1ca558247d592fae55c32c15c4733f194ca0a6760975c2700bf0714c05.
- Vollhash: ceead7e916aa05d0b112d7a85342b44ddb03b6092a2bb741c9ab8ab1044b2133.
- Snapshot: b2a85f3128c8cad6a122a15cb82df4da1aae5254038c23e2c51b5c05e8f1cd5e.
- PDF: build/qam-v5-physics-narrative/physics/paper.pdf. Fünf Seiten Haupttext inkl. Literatur + zwei Seiten Beweisanhang.
- Zweimal mit pdflatex gebaut, keine Overfull/undefinierten Zitate/Verweise/Rerun-Meldungen. Alle sieben Seiten visuell geprüft.
- Ganze Store-Suite: 29 Tests erfolgreich, inkl. neuer Tests für Abstract/Autor, getrennte Auditdaten und Erhaltung offener Kandidaten.
- Reproduktion: python -m qam.tools.configure_v5_editions --out build/v5-editions-new (neuer Zielordner).
- CLI edition-read/save/export in qam.tools.store_db; Datenbank build/qam.sqlite3, weiterhin 2468 Aussagen/61 Langquellstationen.
- Entwicklung 5.0.0-draft; öffentliche Baseline 4.11.0 / DOI 10.5281/zenodo.24108818.
- Kein neuer Release, DOI, Zenodo-Upload oder Main-Merge. Redaktionelle Fassung noch kein publikationsfertig geprüftes Gesamtpaper.
- Nächster Schritt: Autor soll die neue Lesefassung beurteilen; dann fachliche Lücken der ausgewählten Teilchen-/Geometrieaussagen vervollständigen und gemeinsamen Zwei-PDF-Releasejob fertigstellen.
- Alte Editionsrevisionen und Vorläufertexte bleiben unverändert abrufbar, alte Quellhashes nicht überschreiben.
- Branchlöschung weiterhin durch automatische Freigabeprüfung blockiert; Liste in notes/research/v5_0_0_branch_cleanup_review.md. Keine neue Freigabe erhalten.
- .codex/environments/ außerhalb des Commits belassen. OPs und native Identifikationen bleiben offen.
