# Wolfram-Prüfung des Preprints 0.1.0

20. November 2026. [Veröffentlichte Fassung](https://doi.org/10.5281/zenodo.24405553). Das öffentliche Zenodo-PDF und das lokale PDF sind bytegleich. SHA-256 99aec02ead80b924fdb93182227307eeb8e4a2f3636f16ff6604a45507dc01dc. Gezielte Wiederholungsprüfung mit bekannten Zielausdrücken.

| Bereich | Befund |
| --- | --- |
| HC, Feld, Träger und lineare Geometrie | 19 von 19 exakten Prüfgruppen. Projektionen modulo J² = I, Lichtfeldbeispiel, Feldinvariante, Dublett-Gram-Matrix, Biquaternionennorm, Nullspinor, Übergangsmatrix, lokale Eichregel und lineare Geometrie stimmen. |
| Dixon-Vergleich | Exakte Generatorrechnung. Nach der Lorentz- und Farbreduktion geben 24 Kandidatenfreiheitsgrade und Rang 18 die komplexe Kommutantendimension sechs. Die sechs Hyperladungsprojektoren zerlegen die Identität. Der antilineare Anteil hat Dimension null. |
| Koide | 29 von 29 exakten Prüfungen. Spektrum, Spur, Umphasierung, Phase, Positivitätsrand, Mittelung und Flat-Gap-Vergleich stimmen. Am Rand abs(φ) = π/4 hat die Gram-Matrix genau Rang zwei. |
| OP5 | 32 von 32 exakten Prüfungen mit Nullresiduen. Darunter Erhaltung des linearen mechanischen Tensors, Wellenfaktor, Achsen- und Bündelkoeffizient, Piola-Entwicklung und Kalibrieralgebra. |

## Reichweite und Präzisierung

Die HC- und Feldidentitäten wurden mit generischen Eingabekomponenten geprüft. Für die Positivität des Feld-Grams folgt die Schranke aus der Gram-Determinante. Die Nullspinor-Inversen sind mit der Nullbedingung kompatibel. Für ein nichtverschwindendes Nullfeld ist mindestens eines der Spinorquadrate von null verschieden. Die Wahl seiner Quadratwurzel fixiert das gemeinsame Vorzeichenpaar.

Die Normmultiplikativität in Abschnitt 2.1 gilt auf der vollen Biquaternionenalgebra. Die Familie mit rein imaginärem Skalarteil ist unter der Multiplikation im Allgemeinen nicht abgeschlossen. Bereits das Quadrat einer imaginären Quaternion-Einheit hat reellen Skalarteil. Die Formel stimmt. Der Definitionsbereich ließe sich im Artikel deutlicher benennen.

Die Prüfungen zu Rechtsinverser, Eichregel, Coframe und endlicher Quellenreduktion erfassen konkrete exakte Testfamilien. Die allgemeinen Schlüsse beruhen auf Produktregel, Determinantenmultiplikativität und Projektionseigenschaften der Pseudoinversen. Für die Cartan-Fortpflanzung wurde die Symmetrie des angegebenen Hauptsymbols unter dem Symmetrisierer kontrolliert. Die Existenz gemeinsamer Felder auf einem offenen Gebiet bleibt offen.

Der OP5-Residual prüft die Wahl der Quelle und ihrer Antwort unter den angegebenen Gleichungen. Retardierte Eindeutigkeit, native Higgs–OP5-Kopplung, vollständige Materialbilanz und physikalische Auslese bleiben Voraussetzungen. Ein Datenvergleich für Leptonenmassen oder H96 war kein Bestandteil dieses Laufs.

Der erste Kernlauf meldete beim Rang-eins-Beispiel eine Abweichung durch die Vorzeichenkonvention des eingebauten charakteristischen Polynoms. Die explizite Determinante det(λ I − Q) korrigiert das Prüfskript. Eigenwerte und beide Koide-Werte waren bereits im ersten Lauf korrekt. Eingabe und tatsächliche Ausgabe sind auch für den ersten Lauf abgelegt.

## Reproduktion

Ausgeführt wurden die WL-Dateien im Wolfram Language Evaluator mit Wolfram 15.0.1 für Linux. Lokal lassen sie sich mit wolframscript -file DATEI.wl auswerten. Ein abschließendes Out[1]=Null stammt in einzelnen Läufen von der letzten Print-Anweisung. Klassische Algebra, Tensor- und Differentialrechnung bestimmten die Werkzeugwahl. Qiskit wurde erwogen. Ein Quantenschaltkreis war für diese Aussagen nicht definiert.

- [Kernskript](core/article_core.wl) · [Ausgabe](core/article_core.txt)
- [Dixon-Skript](dixon/dixon.wl) · [Ausgabe](dixon/dixon.txt) · [Methode](dixon/README.md)
- [Koide-Skript](koide/koide.wl) · [Ausgabe](koide/koide.txt) · [Methode](koide/README.md)
- [OP5-Skript](op5/op5.wl) · [Ausgabe](op5/op5-output.txt) · [Methode](op5/README.md)
