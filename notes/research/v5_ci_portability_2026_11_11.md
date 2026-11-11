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
Die vier Tests des Dokumentbuilders und alle 33 lokalen Storetests bestehen.
Auf dem Codecommit `6e524f5c01037bcbdfa29263d18776bc88211341` sind auch die
GitHub-Prüfungen erfolgreich: QAM Windows und Linux (Run 43067075940),
Lean (43067076106), TeX (43067076143) sowie der vollständige gemeinsame
PDF-Build im Container (43067072925). PR: #95.

Das erfolgreiche Artefakt `qsc-v5-paired-documents-2` wurde heruntergeladen.
Sein Manifest bestätigt beide vollständigen Dokumente und weiterhin
`publication_ready=false` sowie `incomplete_argument_review=true`.
Alle 111 verzeichneten SHA256 wurden nach dem Download geprüft.
Der Container liefert 1396 Seiten Langfassung und 27 Seiten Physikpaper,
45 Satzüberläufe im Langtext und keinen im Physikpaper. Die abweichenden
Seiten- und Satzmeldungszahlen gegenüber lokalem MiKTeX sind keine
Quellkorrektur: Der lokale Lauf hatte 1397 Seiten und 58 Meldungen.

Die 58 Satzüberläufe der Langfassung sind hiervon getrennt und bleiben
offen. Diese Reparatur selbst führt weder einen Main-Merge noch eine
Zenodo- oder DOI-Aktion aus.
