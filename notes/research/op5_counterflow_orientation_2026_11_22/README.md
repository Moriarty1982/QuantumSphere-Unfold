# Gleiche Gewichte beider Zeitorientierungen aus dem Gegenstrom des OP5-Keims: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Am OP5-Keim ist der Gegenstrom-Block 2 bis auf 8·10⁻⁴ das lokale Zeitumkehrbild von Block 0, und die
Dichten beider Laufrichtungen sind bis auf 6·10⁻⁴ bis 8·10⁻⁴ gleich (p = 0,5003 bzw. 0,5004). Liest man die Enden des Vermittleraustauschs
in den Strömen der Blöcke aus, folgt die Entkopplung der H_0i also fast genau, mit |w| < 10⁻³. Die Fierz-Größen unterscheiden aber
Zeitumkehr und Spiegelung x ↦ −x nicht; die Zeitumkehr ist die Lesart, die N_m gibt. **Nach dem vorab festgelegten Raster: trägt teilweise.**

Auftrag des Autors: „weiter“ nach r40. Verfahren vorab: `Methoden_Notiz.md` (Commit 10e483e1, Rückwärtssuche). Nicht blind: Die
Dichten waren aus k168 auf zwei Stellen bekannt. Skripte `counterflow_weights.py` (Python, mpmath 40 Stellen, Keimordner als Argument) und
`reflection_average.wl` (Wolfram, exakt); Ausgaben in `run/`. Keine H-Nummer.

## Ergebnis
| Frage | Befund |
|---|---|
| (1) Zeitumkehrbild | Block 2 gegen T(Block 0): größte Abweichung der normierten Fierz-Größen 7,9·10⁻⁴; gegen T(Block 1): 4,5·10⁻³ (Block 1 weicht selbst um 3,7·10⁻³ von Block 0 ab). Spiegelung x ↦ −x gibt dieselben Abweichungen: Bei J entlang x und K entlang y fallen beide Bilder bis auf 2,5·10⁻⁴ zusammen. |
| (2) Gewichte | φ²: 5,96893 + 0,42636 gegen 6,38448, p = 0,500423, w = 8,5·10⁻⁴. J⁰ = ψ†ψ: p = 0,500299, w = 6,0·10⁻⁴. Größte relative Abweichung des Zählers von N_m ist \|w\| (bei x = a). |
| (3) Zeitumkehr oder Spiegelung | Mittel mit Zeitumkehr: genau 3N_m. Mittel mit Spiegelung: 3N_m − a(a − 2x + a cos 2φ)sin²φ, also N_m nur für k entlang des Gegenstroms; Winkelmittel 7a²/4 − ax + 2x², nicht ∝ N_m. |
| nachträglich | Gesamtstrom der drei Blöcke J^a = (15,97; 0,0015; 0,0008; 0,0005): Nettogeschwindigkeit 9·10⁻⁵. Gleiche Gewichte bei gleicher Geschwindigkeit heißen: Der Keim ruht im Bezugssystem seines Gesamtstroms. |

## Lesart
- Kandidat (a) der Rückwärtssuche liefert fast genau die gesuchte Gleichgewichtung. Der Keim enthält einen Strom und sein lokales
  Zeitumkehrbild (Geschwindigkeit und Spin umgekehrt) mit nahezu gleicher Dichte; die Restabweichung |w| < 10⁻³ ist so klein wie die
  Abweichung der Blöcke 0 und 1 voneinander.
- Nachträglich, nicht vorab festgelegt: Die Gleichgewichtung entspricht einem verschwindenden Nettostrom. Das Ruhesystem der Rechnungen
  r36–r40 wäre dann das Ruhesystem des Keimstroms (Eckart-artig); so würde der Rahmen, den der Vermittler braucht, auch die Gleichgewichtung
  liefern. Das ist eine Lesart.
- Offen: (i) Zeitumkehr und Spiegelung sind am Keim nicht zu unterscheiden; die Zeitumkehr wird gewählt, weil nur sie N_m gibt. (ii) Dass
  die Enden des Austauschs in den Blockströmen ausgelesen werden, ist eine Lesart. (iii) Nur ein Keimpunkt.
- Kandidat (c), der String zwischen M und T unter G2, ist nicht gerechnet; vollständig umgekehrte Orientierung gäbe den Lorentz-Fall p = 0.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
