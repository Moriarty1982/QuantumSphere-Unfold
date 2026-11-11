# Typografische Korrektur der v5-Langfassung

11.11.2026, Codex. Auftrag: nach der CI-Reparatur die breiten Formelboxen
und langen Protokollbezeichnungen bearbeiten. Rein redaktioneller Satz;
keine neue Forschungsrunde, Hypothese, Rechnung oder Beweisfreigabe.

## Änderungen

Vier Dateien unter `sources/research/parts/v470/`:

- `07_qam_infrastructure.tex`: eine slashgetrennte Bezeichnung erhält
  Umbruchmöglichkeiten mit der vorhandenen URL-Satzfunktion und gleicher Schrift.
- `26_inherited_technical_appendices.tex`: lange Protokollpfade können
  an Schrägstrichen umbrechen. Wortlaut und Reihenfolge bleiben erhalten.
- `34_mm_hc_and_c5_development.tex`: breite Status-, Entscheidungs-,
  Summen- und Bedingungsboxen werden mehrzeilig gesetzt. Fünf Tabellen
  einschließlich der r17-Vergleichstabelle bekommen passende Absatzspalten;
  eine weitere Tabelle gehört zur folgenden Datei. Der Abschluss von r54
  bleibt zusammen, damit seine letzte Notiz keine einzelne Restseite bildet.
- `36_frame_typed_endpoint.tex`: die r83-Statustabelle verwendet umbrechende
  Textspalten und unveränderte mathematische Ausdrücke in den Zellen.

Die historischen Rundeninhalte, Statuswerte und Einschränkungen bleiben
erhalten. Insbesondere werden alte Angaben wie ,,PDF not built`` nicht
nachträglich durch den heutigen Buildstatus ersetzt. Es gibt keine
mathematische oder physikalische Korrektur und keine neue OP-Bewertung.

## Inhaltserhaltung und Nachvollziehbarkeit

Das einmalige Skript `v5_layout_reflow_2026_11_11.py` erwartet exakt den
Quellstand des vorigen Satzinventars und bricht bei anderen Ausgangsbytes
ab. Es ist ein Nachweis des Eingriffs, kein Teil des regulären Builds.
Vor dem Schreiben vergleicht es eine auf die verwendeten Satzbefehle
beschränkte Inhaltsprojektion aller vier Dateien. Dabei werden nur die
neu verwendeten Layoutumgebungen, Spaltenformate, mathematischen
Modusgrenzen, Textcontainer, Abstände, Zeilenumbrüche und Größenbefehle
für vorhandene Klammern ausgeblendet. Die übrigen Zeichenfolgen und
Gruppierungen stimmen überein. Das ist eine gezielte Kontrollrechnung
für diesen Satzwechsel, kein allgemeiner semantischer TeX-Beweis.

Nach dem letzten Eingriff wurde der Vergleich nochmals gegen die
Git-Ausgangsquellen ausgeführt. Wortlaut, Zahlen, Formelsymbole,
Reihenfolge, Bedingungen, Labels und Guards sind unverändert. Die zwei
fest an Reviewhashes gebundenen Koide-/HC-Beweisquellen wurden nicht
bearbeitet und stimmen weiterhin bytegenau mit ihren Sollhashes überein.
Prüfdaten und Vorher-/Nachherhashes:
`v5_layout_reflow_validation_2026_11_11.json`.

## Lokaler Endstand

Gemeinsamer Build: `build/v5-layout-final-v2/`.

- Langfassung: 1402 Seiten; vorher lokal 1397 Seiten.
- Physikpaper: weiterhin 27 Seiten, sein LaTeX-Text ist bytegleich zur
  zuvor vollständig visuell geprüften Lesefassung.
- Beide: keine Overfull-Boxen, offenen Verweise, doppelten Labels oder
  verbleibenden Rerun-Meldungen. Vorher hatte die Langfassung 58 Meldungen.
- Der gemeinsame Snapshot wurde mit den neuen Quellhashes registriert.
  Alle Paketprüfsummen wurden nach dem Build kontrolliert.
- 33 Storetests erfolgreich; die drei Editionstests sind nach der
  letzten rein typografischen Seitenbindung zusätzlich nochmals bestanden.

## Sichtprüfung und Korrekturlesen

`v5_layout_visual_check_2026_11_11.py` grenzt die verwendeten Umbruchstellen
über benachbarte Labels und deren tatsächliche PDF-Seiten ein. Für den
letzten Abschnitt wird erforderlichenfalls das erste Label des nächsten
Eingabeteils verwendet. Das Prüfpaket deckt 60 Satzstellen auf 56 Seiten ab.
Alle 56 Seiten wurden in Kontaktbögen kontrolliert; sechs Beispiele mit
Tabellen, Statusboxen und Abschlussumbruch zusätzlich in voller Größe.
Nach der letzten Seitenbindung änderten sich nur die gerenderten Seiten
1046 und 1047; beide wurden erneut geprüft. Die Seitenzahlen sind an den
PDF-Hash in `v5_layout_visual_coverage_2026_11_11.json` gebunden.

Dies ist keine vollständige visuelle oder fachliche Begutachtung aller
1402 Seiten. Selbstkorrekturlesen umfasst die geänderten Satzstellen und
ihren Anschluss. Es gibt keine mathematischen Symbol- oder
Aussagenänderungen; geändert sind Zeilenführung, Text-/Mathe-Satzhüllen,
Spalten und Größenbefehle vorhandener Klammern.

Die Containerprüfung wird auf dem Layout-Branch zusätzlich ausgeführt.
`publication_ready=false` und die offenen Argumentprüfungen bleiben
unverändert. Die deutsche persönliche Lesefassung bleibt inhaltlich gleich.
