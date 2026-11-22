# Vorab-Notiz H115: Kompensator und Nullrichtung des flachen Oktanten

22. November 2026. Nicht blind. Anlass ist die Frage des Autors, ob der Kompensator zuerst eine reelle Hälfte derselben komplexen Richtung entfernt, die im 45-Grad-Oktanten ganz verschwindet.

## Vorwissen geprüft

- [H114](Ergebnis_H114_Photon_Oktant.md): komplexer Gram-Rang 3→2, reell 6→4. Die Zuordnung des Oktanten zum Photon-Eigenpunkt ist bedingt.
- [HC-Massenauslese](../sources/research/parts/hc-mass-identification.tex) unterscheidet unitäre, antiunitäre und reell-orthogonale Lesarten. Der direkte Kompensator C=(I+J)/2 vernichtet deklarierte J-ungerade Fermioneingänge.
- [Generationskopplung](../sources/research/parts/generation-coupling.tex) konstruiert geschlossene, ungerade Vergleichszustände JS=-S. Der Closure-Projektor ist von C verschieden.
- [Flacher Oktant, r25](../notes/research/op3_dixon_copies_2026_11_16/README.md) und [Gesamtbild](../wiki/Gesamtbild.md), T2/T5/T8. Die Massenmasken und OP5-Vergleichsnotizen liefern für die hier geprüfte Richtung keine zusätzliche HC-Abbildung.

## Kriterien

- **H115a (nativer direkter Test):** Auf den drei geschlossenen ungeraden Generationsrichtungen soll der vorhandene C-Eingriff genau eine reelle Richtung der komplexen Gram-Nullgeraden entfernen und Rang fünf haben. Prüfe die Quellannahme JS=-S und als Kontrollen die reellen Ränge einer global antiunitären Involution und einer komplexlinearen Involution.
- **H115b (reeller Vergleich):** Verwende die Oktantstrahlen +x,+y,+z in C². Bestimme aus der zugehörigen Gram-Matrix eine komplexe Nullgerade L und deren unabhängige reelle Basisrichtungen n und i n. Spiegele jeweils eine dieser beiden Richtungen, lasse ihren reellen Orthogonalraum fest und setze C=(I+J)/2. Entscheidung: Beide Projektoren müssen Rang fünf haben, je eine reelle Richtung in L entfernen, und nach dem Oktant-Ausleser dieselbe Abbildung ergeben wie der Oktant-Ausleser allein. Prüfe außerdem, ob der Phasenwechsel i die beiden Projektionswahlen vertauscht. Die beiden Alternativen testen eine Auswahllücke; der Vergleich setzt keine native Fixierung ihrer Phase.

Wolfram Language prüft exakte Matrixidentitäten, Ränge und die zyklische Phase. H115b betrifft lineare Kinematik und setzt weder einen nativen Eingriff des Kompensators noch eine zeitliche Abfolge oder Stabilität voraus.
