# Gemeinsamer v5-Dokumentbuild

11.11.2026, Codex. Fortsetzung der Veröffentlichungsvorbereitung.

Werkzeug: `python -m qam.tools.build_v5_documents --out NEUER_ORDNER`.
Workflow: `.github/workflows/qsc-v5-dual-documents.yml`.
Beide englischen Ausgaben entstehen aus einem eigenen gemeinsamen Bestand.
Die deutsche persönliche Lesefassung bleibt separat.

## Lokal geprüft

- Vollständiger Lauf: `build/v5-paired-documents-final/`.
- Langfassung: 1397 Seiten, drei Satzläufe, 58 Overfull-Boxen.
- Physikpaper: 27 Seiten, zwei Satzläufe, keine Overfull-Boxen.
- Beide ohne offene Verweise, doppelte Labels oder verbleibende Rerun-Meldungen.
- Physik-LaTeX bytegleich zur bereits vollständig visuell geprüften Ausgabe.
- Langfassung nur stichprobenartig visuell geprüft: Titel, Leseführung und Schluss.
  Das ist keine vollständige visuelle oder fachliche Freigabe der 1397 Seiten.
- Alle im SHA256-Manifest verzeichneten Dateien nach dem Lauf überprüft.
- 32 Storetests erfolgreich, einschließlich drei neuer Tests für Paar-Vollständigkeit,
  Quellenintegrität und Erhaltung der Compilerbefunde.
- Erster lokaler Versuch scheiterte am fehlenden Perl für latexmk. Der gemeinsame
  Ablauf verwendet nun pdflatex direkt, ohne Shell-Escape und mit maximal sechs
  Durchläufen bis zur Stabilisierung der Hilfsdateien. Keine Installation von Perl.
- Der GitHub-Workflow ist eingerichtet, wurde hier aber noch nicht ausgeführt.

## Aussage des Status

`build_complete=true` bedeutet: Beide PDFs vorhanden, Compiler- und
Quellen-/Verweisprüfungen bestanden. Satzüberläufe werden als getrennte
Layoutbefunde erhalten. `publication_ready=false` bleibt ausdrücklich gesetzt.
Die Auswahlen tragen weiterhin `incomplete_argument_review=true`.
Keine wissenschaftlichen Guards werden geschlossen, keine neuen Messdaten
oder Beweise erzeugt und keine DOI-/Zenodo-Aktionen ausgeführt.

Fehlende Ausgabe, Compilerfehler, ungültiger Exporthash oder während des
Baus geänderte Quellen führen zum Fehlerstatus. Auch fehlgeschlagene Läufe
schreiben ein Manifest und behalten vorhandene Diagnoseprotokolle.

Das Paket enthält beide PDFs, Editions-/Auditdaten, Datenbank, Langquellbaum,
Compilerprotokolle, Erzeugungsskripte, README und SHA256SUMS. Es ist ein
technisches Entwurfspaket, kein zur Veröffentlichung freigegebenes Release.

## Eingefrorene Identitäten

Snapshot: `168977e6c8ec955214fc5463769eb2ae709d0815dc6cee38d3d1e05245cb0f67`.

full: `07b52fadd6c9e325a04b06f0d391f921bbb073c15292851c97d5cd42cf3c53f2`.

physics: `740eef6f937c78046d492df36fb4760527b00cb010075bd123aa0e31bb093380`.

Nächster Schritt: Die 58 Satzüberläufe im Langtext nach Quelle und Art erfassen und redaktionell bearbeiten; danach fachliche Schlussprüfung und Workflow-Prüfung.
