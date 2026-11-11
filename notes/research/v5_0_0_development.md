# Version 5.0.0: Datenbankgestützte Dokumentarchitektur

Start: 11. November 2026. Status: **5.0.0-draft**, unveröffentlicht.
Öffentliche Baseline bleibt v4.11.0, Version-DOI 10.5281/zenodo.24108818.
Der Entwurf hat keine eigene Version-DOI.

Der Hauptversionssprung kennzeichnet die neue Organisation des Dokuments:
registrierte Aussagen und Definitionen, unveränderliche Inhaltsversionen,
explizite Abhängigkeiten und Guards, versionierte Auswahlen und LaTeX-Exporte.
Er kennzeichnet weder eine Lösung der offenen Physikfragen noch eine
vollständige automatische Verifikation des Papers.

## Vorhandene Grundlage

- SQLite/SQLAlchemy-Store mit Migrationen, Quellenhashes und append-only Ledger.
- Gesamtinventar: 2468 Aussageumgebungen aus 61 Quelldateien; Rohimporte
  behalten ungeprüfte Interpretation und offene Prüfpflichten.
- Kuratierte Koide-/HC-Zweige mit Originalbeweisen und Selbstprüfungen.
- Bedingte HC–Koide-Verbindung mit offenen nativen und Frame-Pflichten.
- Auswahlexporte, statische LaTeX-Prüfung, Snapshots und portable DB-Sicherung.

## Noch nötig

- Weitere Aussagen und ihre tatsächlichen Beweisabhängigkeiten prüfen.
- Typisierte Frame-Abbildungen erfassen und prüfen.
- Überleitungstexte und Ressourcen für weitere Paper-Auswahlen registrieren.
- Quellenfrische nach Änderungen am Manuskript prüfen und bewusst neue
  Inventargenerationen erzeugen; keine alten Hashes überschreiben.
- Die eingerichteten 5.0-Ausgabeprofile fachlich vervollständigen und den
  gemeinsamen Zwei-PDF-Releasejob einrichten. Der Physikentwurf ist gebaut;
  die Langfassung exportiert vorerst den vollständigen Quellbaum.

`sources/research/v480-companion.tex` bleibt der historische Einstiegspfad.
`working-preamble.tex` setzt die aktuelle Entwicklungsversion. Historische
docversion-Werte und freigegebene Dateien unter release/ bleiben erhalten.
CITATION.cff beschreibt weiterhin die publizierte Baseline. Die vorläufige
5.0-Kennzeichnung bezeichnet die Dokumentarchitektur und ist keine
Neuvergabe mathematischer Aussageversionen. Das davon unabhängig versionierte
Store-Schema wurde auf v6 erweitert, um geordnete Dokumenteditionen abzulegen.

Kein Push, Tag, Merge, Zenodo-Upload oder Release durch diese Umstellung.
