# Ergebnis H94 bestätigt: Am Urknall-Übergang wechselt die Norm der Bosonen von +1 nach −1, mit genau einer Nullstelle und dazwischen ohne Normerhaltung; Fermionen haben exakt −1

Vorab-Notiz `Vorab_Notiz_H94_Norm_Bosonen_Fermionen.md`, Commit `99f1cce` (teilweise nicht blind). Code `k210_norm_uebergang.py`, Ausgabe `k210_out.json`. Ein Lauf. Gültigkeit erfüllt: holomorphe Wronski-Determinante konstant auf 1·10⁻¹¹.

## Ergebnisse (tanh, Δ = 2, N = a(|C|² − |D|²)/b)
| kΔ | 0,01 | 0,1 | 0,2 | 0,3 | 0,5 | 0,7 | 1 | 2 | 6 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| N₊ | +1,024 | +1,168 | +1,175 | +1,043 | +0,560 | +0,073 | −0,380 | −0,729 | −0,901 | −0,969 |
| N₋ | +0,974 | +0,681 | +0,260 | −0,197 | −0,989 | −1,446 | −1,629 | −1,368 | −1,110 | −1,032 |

- **H94a bestätigt:** N(0,01) = 1,024 bzw. 0,974, N(20) = −0,969 bzw. −1,032 (Kriterium jeweils ±0,05).
- **H94b bestätigt:** genau ein Vorzeichenwechsel je Drehsinn. Die Nullstelle liegt bei **k*Δ = 0,7361** (Drehsinn +) bzw. **0,2569** (Drehsinn −).
- **H94c bestätigt:** An 10 (+) bzw. 5 (−) Gitterpunkten gilt 0,1 < |N| < 0,9.
- **H94d bestätigt:** Fermionen haben N_F = −1 auf allen Gitterpunkten und für beide Helizitäten, Abweichung 6·10⁻¹².

## Nachträglich (nicht vorregistriert)
- Die Norm der Bosonen ist nicht nur im Übergangsbereich verkleinert, sie wird auch **verstärkt**: N₊ erreicht +1,18 bei kΔ ≈ 0,2, N₋ erreicht −1,63 bei kΔ ≈ 1. Der Übergang ist für Bosonen in beide Richtungen nicht normerhaltend. Die Drehsinne verhalten sich dabei deutlich verschieden: Drehsinn − kippt früher und überschießt stärker.
- Das Mittel beider Drehsinne ist an den Rändern ±1 (0,999 bzw. −1,000), dazwischen nicht (etwa −0,94 bei kΔ = 0,9, −1,07 bei 1,5). Es gibt also keine einfache Mittelungsregel, die die Erhaltung wiederherstellt.
- Die Annäherung an −1 bei kurzen Wellen ist langsam, wie 1/(kΔ) (Asymmetrie der |D±| aus H86).

## Lesart
- **Fermionen** gehen unitär durch den Urknall. Die gewichtete Ladung kehrt exakt ihr Vorzeichen, für jede Wellenzahl, jedes Profil und jede Masse: reine CPT-Zuordnung, keine Erzeugung.
- **Bosonen** gehen nur in den beiden Grenzfällen normerhaltend hindurch. Lange Wellen (kΔ → 0) behalten die Norm (Bogoliubov mit n = 0,404 je Mode im Bild des scharfen Sprungs), kurze Wellen (kΔ ≫ 1) bekommen die CPT-Zuordnung wie die Fermionen. Für kΔ ~ 0,1–3 ist der glatte komplexe Übergang keine Bogoliubov-Transformation: Die Norm wird kleiner, wird verstärkt oder geht durch 0. Eine Mode mit k*Δ hat danach die Norm 0.
- **Folge der Asymmetrie:** Die Teilchenzahl der Bosonen ist am Urknall nur für Wellenlängen weit über bzw. weit unter Δ definiert. Bei k ~ 1/Δ ist die zweite Lesart unter G2 mit komplexem Übergang für Bosonen nicht unitär. Für Fermionen gibt es dieses Problem nicht. Das ist eine strukturelle Folge, keine Beobachtungsgröße. Eine solche bräuchte Δ und die Zuordnung der Bosonen-Arten zu den Frames (Photon-Gewichte a = b ergäben C₀ = 1, D₀ = 0 und keinen Übergang).
- **Korrektur zu `Erkundung_Fermionen_Urknall.md` (Befund 1, Folge):** „Bosonen mit Materie-Gewichten werden erzeugt (n = 0,404 je Mode)“ gilt nur im Bild des reellen scharfen Sprungs. Beim glatten komplexen Übergang ist die Bosonen-Zahl im Bereich kΔ ~ 1 nicht definiert, darunter wie oben, darüber CPT. Die Aussagen zu den Fermionen bleiben.

## Folge für die nächsten Schritte
- Die Nicht-Unitarität der Bosonen bei k ~ 1/Δ ist ein Konsistenzproblem der zweiten Lesart unter G2 mit holomorpher Fortsetzung. Mögliche Auswege: (i) ein reeller Übergang mit Nulldurchgang statt der komplexen Umrundung (dann aber singulär bei w = 0); (ii) Bosonen in der P-Gewichtung, ohne Übergang; (iii) die Norm der zweiten Lesart anders definieren (holomorphes Skalarprodukt statt |·|²); (iv) annehmen, dass Δ unter der kleinsten physikalischen Wellenlänge liegt, also Δ ≲ Planck-Länge. Dann ist für alle beobachtbaren Moden kΔ ≪ 1, sie gehen normerhaltend durch, und der problematische Bereich liegt jenseits der Planck-Skala. Das ist eine Entscheidung des Autors.
