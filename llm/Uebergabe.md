# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex).

- Branch `codex/v5-release-prep`; bisheriger Commit 1c09a9a, neue Einrichtung folgt in diesem Block.
- Main/Basis: PR94, 3a68669b0b12766c256ae6eeed1f52ae0693acc4.
- Autorenauftrag „mach das“: besprochene Lang- und Physikzusammenstellung in der Datenbank einrichten. Themenfolge damit als Forschungsprofil beauftragt.
- Store-Schema jetzt v6: qstore_editions, qstore_edition_sections, qstore_edition_members; immutable Revisionen und Vorgängerkontrolle.
- Dokumentversion bleibt 5.0.0-draft, öffentliche Baseline 4.11.0/10.5281/zenodo.24108818.
- Reproduktion: `python -m qam.tools.configure_v5_editions --out build/v5-editions-new` (Ziel muss neu sein).
- CLI: edition-save/read/export in qam.tools.store_db. API in qam/store/editions.py.
- Physikprofil qsc-v5-physics: sieben Abschnitte, Einführungstexte aus qam/editions/v5_sections.tex, QAM/MML/MMA-Projektorbeispiel mit exakten Matrixbelegen, kuratierte Koide/HC-Beweise und fünf benannte Prüfkandidaten.
- Physikhash: e7415c4c26cd24ad2ec6ef38fba83b0bc9d3b5010f8a89e065a838fe87da46c8.
- Vollprofil qsc-v5-full: 61 Quellstationen in Input-Reihenfolge, 2468 Aussagen, kompletter source-pinned LaTeX-Quellbaum inkl. Abbildung/Metadaten.
- Vollhash: 56436bd576d5b776881dc01ee3a94a47a3995cba7e3aeec3700542e2c53f4419.
- Snapshot: b0233f94b2bbf2658eabdb82ef55b21f6d1d7e5b362f5eb07e578ea881aac201.
- Ausgaben: build/qam-v5-editions-ordered/, Physik-PDF unter physics/paper.pdf (9 Seiten).
- PDF zweimal gebaut, keine Overfull/undefinierten Verweise/Zitate/Rerun-Meldungen, alle neun Seiten visuell geprüft.
- Letzter Codeexport auch build/qam-v5-editions-verified-physics; LaTeX bytegleich mit gebautem PDF-Quelltext.
- Validierung: ganze Store-Suite 29 Tests bestanden; nach Format-/Reihenfolgeanpassungen drei Editionstests erneut bestanden, abschließend einzelner Mitgliedschaft/Guard/CAS-Test erfolgreich.
- qam-batch-CI erweitert um SQLAlchemy-Installation und Store-/Editionstests auf Linux und Windows.
- Vollbackup: build/qam-v5-editions-backup, 28 Tabellen. Backupprüfung und Wiederherstellung nach build/qam-v5-editions-restore.sqlite3 erfolgreich; Physikexport bytegleich.
- Editionstabellen und EDITION-Events außerhalb des Inventarcheckpointumfangs, aber im Vollbackup. Wiederholte Konfiguration erzeugt keine unnötigen Revisionen.
- Beide Exporte bleiben Forschungsentwürfe. Rohimporte werden nicht als bewiesene Physik exportiert, Guards bleiben offen. Kein vollständig verifizierter Gesamtargumentationsbaum.
- Nächster Schritt: fünf Kandidaten fachlich kartieren; dann gemeinsamen automatischen Zwei-PDF-Releasejob und Veröffentlichungspaket fertigstellen. Langfassung bislang als vollständiger Quellbaum exportiert, kein neuer Lang-PDF-Build dieses Blocks.
- Kein neuer Zenodo-Entwurf/DOI/Upload/Publish und kein neuer Main-Merge.
- Branchlöschung weiterhin durch automatische Freigabeprüfung blockiert; genaue Liste in notes/research/v5_0_0_branch_cleanup_review.md. Nicht ohne ausdrückliche Listenfreigabe erneut versuchen.
- `.codex/environments/` unberührt außerhalb des Commits.
