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
`1db88536ab67af7a1087fb999f63ef46ccfb9a0f8d22335c8969cf51a306c1d8`
und an die genauen normalisierten UTF-8-Quellinhalte. Englische Quelle:
`build/qam-v5-expanded-final/physics/paper.tex` aus dem Editionslauf.

Erzeugung in einem neuen Zielordner:

```powershell
python -m qam.tools.build_v5_german_reader --source build/qam-v5-expanded-final/physics/paper.tex --out build/qam-v5-physics-de-final
pdflatex -interaction=batchmode -halt-on-error -no-shell-escape -output-directory=build/qam-v5-physics-de-final build/qam-v5-physics-de-final/paper.tex
pdflatex -interaction=batchmode -halt-on-error -no-shell-escape -output-directory=build/qam-v5-physics-de-final build/qam-v5-physics-de-final/paper.tex
```

`translation.json` enthält Quellbindung, Übersetzungsdateihashes und
Ausgabehash. Deutsche Silbentrennung und deutsche Bezeichnungen für
Zusammenfassung, Literatur und Beweis kommen über Babel. Die Fassung ist
eine persönliche Leseübersetzung der Datenbankausgabe, noch kein eigenes
registriertes Sprachprofil der Editionsdatenbank und kein Release.
