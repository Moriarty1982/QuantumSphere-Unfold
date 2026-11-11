# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex). Wird pro Arbeitsblock überschrieben.

- Branch codex/v5-release-payload ab main 802c7af; englische Quellen-/Evidenz-Payload vorbereitet.
- Main jetzt 802c7af9e672f138461ffb112b0fcd43b7b79c58; öffentliche Baseline v4.11.0, Entwicklung v5.0.0-draft ohne eigene DOI.
- Auf ausdrückliche Autorenfreigabe alle drei PRs gemergt: #95 als 4200c23, #96 als fdd9acc, #97 als 802c7af. Keine offenen PRs.
- Lokales main per Fast-forward synchronisiert; neue Paketbranch darauf angelegt.
- Sämtliche Main-CI auf 802c7af erfolgreich: paired PDF 43087358029, Lean 43087357965, TeX 43087358072, Batch 43087357942 und Wiki 43087357911.
- Containerlauf 43078619869 des alten Layoutstands 875a6ad erfolgreich: 1401/27 Seiten, alle vier Befunde null, 111 Prüfsummen geprüft.
- Fachliche Selbstprüfung der vollständigen englischen Physikfassung samt Anhang: notes/research/referee/v5-physics-2026-11-11-pass1/report.md.
- Kein tragender Fehler festgestellt; keine unabhängige Begutachtung. Archivierter Review bleibt an seinen Snapshot gebunden.
- Review-Präzisierungen jetzt in Englisch/Deutsch umgesetzt: nichtnullige Amplituden und Übergangs-Gram-Matrix, reelle Schur-Kopplungsskala.
- Alle 640 mathematischen Fragmente in derselben Reihenfolge erhalten. Originalbeweise und historische Runden unverändert.
- Nachtrag notes/research/v5_precision_followup_2026_11_11.md; Validierung und visuelle Abdeckung in den gleichnamigen JSON-Dateien.
- Neuer lokaler Gesamtbuild build/v5-precision-paired-verified/: 1402 Seiten Langfassung, 27 Seiten Physikpaper, alle vier Befunde null.
- Alle 111 Paketprüfsummen geprüft; drei Editionstests erfolgreich.
- Neue Physikedition af90ae83e7a9ba9756bc8f1a995fd4f353ed98868d8d5afb110cb79a3385a186.
- Snapshot 83a07eed57a127f216cca38bcd93c20fea05b5c04eb19555ac5de242f6874fd3; weitere Hashes im Validierungs-JSON.
- Deutsche sources.json neu gebunden; build/v5-precision-de-final/compile/paper.pdf: 29 Seiten, alle Befunde null.
- 4 englische und 13 deutsche Seiten mit geänderten Seitentexten gerendert und in Kontaktbögen geprüft; keine Gesamtsichtung der Langfassung.
- Erster eingeschränkter MiKTeX-Start scheiterte am Profilzugriff; der neue Build mit passendem Zugriff war erfolgreich.
- Entwurfsmetadaten release/zenodo/metadata_v5_0_0_draft.json; Paketplan, Changelog und Trockenlaufprotokoll unter release/v5.0.0-prep/.
- Der Metadaten-Trockenlauf bezeichnet ausdrücklich ältere PDFs; finale Dateien erneut prüfen.
- publication_ready=false und beide incomplete_argument_review=true; Guards und OPs unverändert.
- Autorenauftrag: nur englische Texte hochladen; deutsche Lesefassung und deutsche narrative Notizen aus der Payload ausgeschlossen.
- Konkreter Kandidat build/v5-english-upload-verified/: zwei EN-PDFs (1401/27 Seiten), Quellen-ZIP mit 86 Einträgen, DB und Manifeste; vollständiger Trockenlauf erfolgreich.
- Beide Dokumente aus dem Quellen-ZIP lokal erfolgreich gebaut, alle vier Befunde null; 111 Eingangshashes, DB-Integrität und Editions-/Snapshotbindung geprüft.
- Paketwerkzeug qam/tools/package_v5_documents.py; Dokumentation und exaktes Inventar release/v5.0.0-prep/ENGLISH_PAYLOAD*.
- Nächster Schritt: DOI-Reservierung und endgültige Titelseiten vorbereiten, dann finale Payload neu bauen/prüfen; aktueller Kandidat bleibt draft.
- Alle drei PRs vor dem Merge auf main umgestellt und verbleibende Diffs geprüft; alle PR-Prüfungen erfolgreich.
- Kein weiterer Merge, Release, DOI-Schritt oder Löschen alter Branches freigegeben.
- DOI-Reservierung, tatsächliches Veröffentlichungsdatum, finaler Quellenarchivbau und serverseitige Metadatenannahme bleiben offen.
- Kein Zenodo-Entwurf, Upload, Release oder Tag; CITATION.cff bleibt auf v4.11.0.
- .codex/environments/ nicht aufnehmen; alte Branchlöschung weiterhin nicht freigegeben.
- Keine H-/k-Nummer vergeben.
