# v5: Unterschiede zwischen lokalen und GitHub-Läufen

11.11.2026, Codex. Fortsetzung nach Main-Merge edf1a1c. Keine Änderung
mathematischer Quellen, Reviewhashes, Guards oder wissenschaftlicher Aussagen.

## Beobachtete Fehler

- Gemeinsamer PDF-Build, Run 43020334604: Git meldete im Container
  `detected dubious ownership`, bevor die Dokumentzusammenstellung begann.
  Das Fehlerpaket wurde korrekt erhalten; kein vollständiger Buildstatus.
- QAM-Stapelsuite, Run 43020334599: vier Windows-Fehler beim exakten
  Quellhashvergleich der Koide-/HC-Selbstprüfungen. Der parallele Linux-Job
  wurde abgebrochen und liefert keinen Erfolgsnachweis. Der Windows-Checkout
  hatte die reinen LF-Quellen umgewandelt.
- Wiki-Synchronisation, QAM-TeX und eigenständiger Lean-Lauf waren erfolgreich.

## Begrenzte Reparatur

`.gitattributes` schreibt ausschließlich für die beiden bereits an feste
Bytehashes gebundenen Quellen `koide-and-kernel.tex` und
`hc-mass-identification.tex` LF vor. Ihre Git-Objekte und lokalen Dateien
stimmen schon vor der Änderung mit den festgehaltenen SHA256 überein.
Die Prüffunktionen werden nicht normalisiert oder gelockert. Inhaltliche
oder sonstige Byteänderungen blockieren die Selbstprüfungen weiterhin.

Die Git-Metadatenabfragen des gemeinsamen Builders verwenden je Aufruf
`git -c safe.directory=<genau dieses Checkout>`. Das verändert keine globale
Konfiguration und vertraut weder allen Verzeichnissen noch fremden Pfaden.
Ein Regressionstest prüft den genauen begrenzten Aufruf.

Die Pfadfilter der plattformübergreifenden QAM-Prüfung berücksichtigen nun
auch `.gitattributes`, damit spätere Änderungen dieser Checkout-Vorgabe
erneut beide Plattformen prüfen.

## Lokale Validierung

Ein frischer temporärer Git-Bestand mit `core.autocrlf=true` wurde mit
den unveränderten geprüften Quellbytes und den neuen Attributen angelegt.
Beide daraus ausgecheckten Quellen bleiben bytegleich zur Vorlage.
Die vier Tests des Dokumentbuilders bestehen. Die vollständige Store-Suite
wird ebenfalls ausgeführt; GitHub-Läufe auf dem Reparaturbranch prüfen
zusätzlich den tatsächlichen Container und beide Betriebssysteme.

Die 58 Satzüberläufe der Langfassung sind hiervon getrennt und bleiben
offen. Diese Reparatur selbst führt weder einen Main-Merge noch eine
Zenodo- oder DOI-Aktion aus.
