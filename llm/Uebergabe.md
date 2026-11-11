# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex). Diese Datei wird je Arbeitsblock überschrieben.

- Branch codex/v5-release-prep; Basis vor der Übersetzung b5f032e.
- Main/Basis bleibt PR94 / 3a68669b0b12766c256ae6eeed1f52ae0693acc4.
- Letzter Autorenauftrag: vollständige deutsche Lesefassung des ausgearbeiteten Physikpapers.
- Sieben neue Module qam/editions/v5_expanded_*.tex, jeweils als Erklärung registriert und quellengehasht.
- Umfang: 27 Seiten, davon 24 Argumentation, eine Literaturseite und zwei Seiten Originalbeweise.
- PDF: build/qam-v5-expanded-final/physics/paper.pdf; LaTeX, assembly.json und audit.md im selben Ordner.
- Einleitung: Observable Äquivalenz, Kriterien der Darstellung, Selektion und Auslesung.
- Träger: Biquaternionen, zwei Konjugationen, Pauli-/Lorentz-Realisierung, HC-Grading und Realifizierung.
- Methode: QAM/MML/MMA erklärt; komplette elektromagnetische Gram-/Lorentz-Intervallherleitung.
- Ein gespeicherter MMA-Beleg per Hash geprüft und unter qam/editions/evidence/gram_interval_receipt.json gesichert.
- Ergebnis [121/162,961/1202]; Prämissen bedingt, closure_proved und mathematical_relations_proved bleiben false.
- Teilchen: bedingte CAR-Zählung 1,3,3,1; Generationenseeds, Rang, Slot/Spektrum, relative Mischungsbasis.
- Massen: Defektnorm, positive Penalty, freie unitäre Dilatation, Schur-Komplement und endliche Lücke, zyklische Wurzeln, Positivität, Überlagerung.
- Geometrie: versteckter Lift, Gedächtnis, kanonische Partner, Wirkungsreduktion, Koframe, endliche Quellenkompatibilität, bedingte Constraint-Fortpflanzung.
- Zeta: arithmetischer Partner bei sigma > 1, Eigenzustandssperre, reguläres positives Spektralpaket, Unschärfe und offene native Selektion.
- Originalbeweise und Runden unverändert; Rohimporte erhalten keinen neuen Beweisstatus. OPs bleiben offen.
- Prüfbericht: notes/research/v5_expanded_physics_editorial_review_2026_11_11.md; Quellenkarte, Grenzen und Korrekturleseumfang.
- Physikhash: 1db88536ab67af7a1087fb999f63ef46ccfb9a0f8d22335c8969cf51a306c1d8.
- Vollhash: 7dac95aad8d2d2db2e36090a24d298d975f06c24f88a1b0035f9139faa3bc0df.
- Snapshot: fda9214d02e556594f39696505729fd64e8624055237ecf880d6bafe89d646b4.
- Zweimal pdflatex ohne Shell-Escape, finales Log ohne Overfull/undefined/Rerun/mehrfache Labels; alle 27 Seiten visuell geprüft.
- 29 Storetests erfolgreich, anschließend drei Editionstests erneut erfolgreich. Unveränderte Eingaben bleiben idempotent.
- Reproduktion: python -m qam.tools.configure_v5_editions --out build/v5-editions-new (neuer Zielordner).
- Langfassung weiterhin 61 Quellstationen / 2468 Aussagen mit vollständigem gehashtem Quellbaum.
- Entwicklung 5.0.0-draft; öffentliche Baseline 4.11.0 / DOI 10.5281/zenodo.24108818.
- Kein Main-Merge, neuer Release, DOI oder Zenodo-Upload in diesem Block.
- Deutsche persönliche Lesefassung: build/qam-v5-physics-de-final/paper.pdf, 29 Seiten einschließlich Beweisanhang.
- Übersetzungsquellen qam/editions/de/ und Werkzeug qam.tools.build_v5_german_reader; 640 mathematische Fragmente erhalten, nur Tabellenbeschriftung lokalisiert.
- Deutsche Fassung zweimal gesetzt, alle 29 Seiten visuell geprüft; keine Overfull/undefined/Rerun/mehrfachen Labels. Wiederholbarkeit und Zurückweisung geänderter Vorlage geprüft.
- Kein neues Datenbank-Sprachprofil; englische Edition bleibt Quelle. Bericht notes/research/v5_german_reader_2026_11_11.md.
- Nächster Schritt: Autor liest die deutsche Fassung; fachliche Schlussprüfung und gemeinsamen Zwei-PDF-Releasejob fortsetzen.
- Branchlöschung weiterhin durch automatische Freigabeprüfung blockiert; Liste notes/research/v5_0_0_branch_cleanup_review.md, keine neue Freigabe.
- .codex/environments/ nicht aufnehmen. Frühere H-/k-Nummern hier nicht neu vergeben.
