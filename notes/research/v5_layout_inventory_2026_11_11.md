# Satzbefunde vor der redaktionellen Korrektur

11.11.2026, Codex. Bestandsaufnahme, noch keine Quellkorrektur.

Die vollständigen Meldungen mit Breite, TeX-Zeilenbereich, Logzeile und
Kontext stehen in zwei JSON-Dateien neben dieser Notiz:
`v5_layout_inventory_2026_11_11.json` für den lokalen MiKTeX-Build und
`v5_layout_inventory_ci_2026_11_11.json` für GitHub-Run 43067072925.
Loghash, Snapshot und die jeweiligen Quellhashes sind mitgespeichert.

| Hinweis auf Quelldatei unter sources/research/parts/v470/ | Lokal | Container |
|---|---:|---:|
| 07_qam_infrastructure.tex | 1 | 0 |
| 26_inherited_technical_appendices.tex | 12 | 0 |
| 34_mm_hc_and_c5_development.tex | 44 | 44 |
| 36_frame_typed_endpoint.tex | 1 | 1 |
| Gesamt | 58 | 45 |

Lokal betreffen 14 Meldungen Absätze und 44 Formeln oder Boxen; im
Container betrifft eine Meldung einen Absatz und 44 Formeln oder Boxen.
Die größte gemeldete Breitenüberschreitung beträgt in beiden Läufen
400,3517 pt. Die geringere Meldungszahl im Container bedeutet nicht,
dass 13 Stellen bereits korrigiert wurden. Die lokalen Quellen wurden
nicht geändert.

Die Quelldateihinweise stammen aus dem zuletzt geöffneten parts/*.tex
im jeweiligen Compilerprotokoll. Das ist kein vollständiger TeX-Parser:
Vor einer Änderung muss jeder Hinweis mit den angegebenen Quellzeilen
und der gerenderten Seite abgeglichen werden. Stichproben bestätigen
lange slashgetrennte Protokollbezeichnungen und sehr breite eingerahmte
Status-/Entscheidungslisten. Eine allgemeine mathematische Korrektur
folgt aus keiner dieser Meldungen.

Die lokalen Quellbytes wurden gegen das lokale Buildmanifest geprüft.
Die CI-Quellbytes wurden gegen den exportierten Quellbaum des
heruntergeladenen Artefakts und dessen Manifest geprüft. Der als UTF-8
mit vereinheitlichten Zeilenenden gelesene Text der betroffenen Quellen
stimmt zwischen beiden Umgebungen überein; rohe Hashes anderer als der
zwei explizit LF-gebundenen Quellen können wegen Checkout-Zeilenenden
abweichen.

Nächster Schritt: zuerst die in beiden Umgebungen verbleibenden langen
Formelboxen und Protokollbezeichnungen prüfen und rein typografisch
umbrechen. Voraussetzungen, logische Aussagen, Formeln und archivierte
Statuswerte müssen erhalten bleiben. Danach beide Satzumgebungen neu
prüfen; die Datenbankeditionen müssen die geänderten Quellhashes neu
registrieren. Die bereits fest gehashten Koide-/HC-Beweisquellen sind
von dieser Bestandsaufnahme nicht betroffen.
