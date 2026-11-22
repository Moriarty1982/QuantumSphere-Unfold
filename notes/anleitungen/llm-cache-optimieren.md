# LLM-Kontext im Quantum Sphaera Companion

Halte den Einstieg in [AGENTS.md](../../AGENTS.md) kurz und stabil. Verweise von dort auf Detailanleitungen. Aktuelle Arbeitsstände gehören in die [Übergabe](../../llm/Uebergabe.md) und die jeweiligen Quellen. Die [Anleitungsübersicht](README.md) zeigt, welcher Ablauf zur Aufgabe passt.

## Quellen je nach Aufgabe laden

| Aufgabe | Einstieg und gezielter nächster Abruf |
|---|---|
| Arbeit fortsetzen oder Kontext wiederherstellen | [Weitermachen](weitermachen.md). Übergabe mit Branch, Commit und Arbeitsbaum abgleichen. Den offenen Arbeitsschritt und die dafür maßgeblichen Fundstellen laden. |
| Fachfrage zum aktuellen Forschungsstand | Zuerst [Gesamtbild](../../wiki/Gesamtbild.md) lesen. Über [Forschungsstand](../../wiki/Forschungsstand.md) oder [offene Probleme](../../wiki/Offene-Probleme.md) zur konkreten Runde, Notiz oder TeX-Stelle springen. Dort auch Definitionen, Voraussetzungen, Frames, Guards und spätere Korrekturen prüfen. |
| Neue Hypothese oder Rechnung | Nach der Einordnung das Vorwissen prüfen und [Hypothese testen](hypothese-testen.md) anwenden. Bei OP5 zuerst „Bereits beantwortet“ in der [OP5-Anleitung](op5-vergleichsmodell-rechnen.md) lesen. |
| Veröffentlichung oder Dokumentdatenbank | Den verlangten Tag und die Ausgabe bestimmen. Die Baseline in [AGENTS.md](../../AGENTS.md) mit dem passenden Release-README bzw. Manifest abgleichen. Für Datenbankeinträge und Dokumentausgaben den benötigten Abschnitt der [QAM-Dokumentation](../../qam/store/README.md) lesen. Import- und Prüfstatus mitführen. |
| Gespeicherter QAM-/MMA-Beleg | Zuerst schreibgeschützt über `qsc-qam` per Hash abrufen, soweit verfügbar. Mit der Kurzansicht beginnen und die für die Frage nötigen Prämissen nachladen. Fehlt eine Beleg-ID, kann `select_qam_context` nach MMA-Kontexthash, deklariertem Frame und MMA-Status suchen. Bei unbekanntem Stapelhash Berichte zuerst listen. Den lokalen Ersatz beschreibt die [MCP-Anleitung](../../mcp/README.md). |

## Kontext schlank halten

- In großen Dateien zuerst nach Satzlabel, H-Nummer, OP oder Begriff suchen. Den Treffer mit den für ihn nötigen Definitionen und Abhängigkeiten lesen. Für ein Zitat oder eine Prüfung Ausgabe, Commit oder Tag, Abschnitt und gegebenenfalls Beleg- oder Prämissenhash festhalten. Die [Hinweise für LLMs](../../wiki/Hinweise-fuer-LLMs.md) erläutern die Quellenprüfung.
- Skripte und relevante tatsächliche Rechenausgaben im Projekt ablegen. In der Antwort Befund, Geltungsbereich und offene Guards kurz nennen und zum Ergebnis springen lassen. Belege mit demselben Hash innerhalb eines Arbeitsblocks einmal prüfen und bei Bedarf erneut abrufen.
- Vor einer Kontextverdichtung oder am Ende eines Arbeitsblocks die [Übergabe](sitzung-uebergeben.md) auf den nächsten konkreten Schritt, den Quellstand und die offenen Entscheidungen konzentrieren. Dokumentierte Herleitungen per Fundstelle mitgeben.

## Abgleich vor dem Zenodo-Release

Nach der Aktualisierung des Schemas und der Einträge diese Anleitung anhand desselben Quellstands prüfen. Die Quellenwege für Veröffentlichung, Forschung, Datenbank und QAM-Belege mit den aktuellen Verweisen und Abrufen vergleichen. Geänderte Pfade, Abschnitte oder Abfragen hier nachziehen und die Links prüfen. Die [Release-Vorbereitung](zenodo-datenbank-vorbereiten.md) legt die Reihenfolge fest.
