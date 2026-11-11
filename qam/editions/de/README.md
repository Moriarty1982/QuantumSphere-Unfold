# Deutsche persönliche Lesefassung

Vollständige Übersetzung der erweiterten englischen Physikfassung vom
11.11.2026, einschließlich der neun Propositionen und Beweise im Anhang.
Die ursprünglichen Literaturtitel und maschinenlesbaren Kennungen bleiben
erhalten. Voraussetzungen, Einschränkungen und offene Nachweispflichten
werden mitübersetzt. Keine neue wissenschaftliche Aussage oder Freigabe.

Die Vorlagen enthalten nummerierte Platzhalter für sämtliche mathematischen
Fragmente. Beim Zusammenstellen werden diese aus der englischen Quelle
unverändert eingesetzt. Fehlende oder doppelte Fragmente, geänderte
Quellmodule oder eine andere englische Ausgabe brechen den Vorgang ab.
Ein Multimengenvergleich prüft zusätzlich alle 640 mathematischen Fragmente
des Gesamtdokuments. Anschließend wird nur die Tabellenbeschriftung
`multiplicity` in `Vielfachheit` übersetzt. Formeln, Zahlen, Voraussetzungen
in Formeln und Zitationskennungen ändern sich dadurch nicht.

`sources.json` bindet die Übersetzung an die englische Edition
`af90ae83e7a9ba9756bc8f1a995fd4f353ed98868d8d5afb110cb79a3385a186`
und an die genauen normalisierten UTF-8-Quellinhalte. Englische Quelle:
`build/v5-precision-paired-verified/editions/physics/paper.tex` aus dem Editionslauf.

Erzeugung in einem neuen Zielordner:

```powershell
python -m qam.tools.build_v5_german_reader --source build/v5-precision-paired-verified/editions/physics/paper.tex --out build/qam-v5-physics-de-precision
pdflatex -interaction=batchmode -halt-on-error -no-shell-escape -output-directory=build/qam-v5-physics-de-precision build/qam-v5-physics-de-precision/paper.tex
pdflatex -interaction=batchmode -halt-on-error -no-shell-escape -output-directory=build/qam-v5-physics-de-precision build/qam-v5-physics-de-precision/paper.tex
```

`translation.json` enthält Quellbindung, Übersetzungsdateihashes und
Ausgabehash. Deutsche Silbentrennung und deutsche Bezeichnungen für
Zusammenfassung, Literatur und Beweis kommen über Babel. Die Fassung ist
eine persönliche Leseübersetzung der Datenbankausgabe, noch kein eigenes
registriertes Sprachprofil der Editionsdatenbank und kein Release.

Nachtrag 11.11.2026: Nichtnullige Auslesen und reelle Kopplungsskala aus dem
Review wurden in beiden Sprachen präzisiert; alle 640 mathematischen
Fragmente bleiben erhalten. sources.json nennt auch die vorherige Edition.
Die aktuelle lokale geprüfte Ausgabe liegt unter build/v5-precision-de-final/.
