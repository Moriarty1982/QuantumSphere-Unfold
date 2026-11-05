# Ergebnis H83: Keine der drei Regeln reproduziert die Gewichte aus r19; G wächst in allen mit γ¹

Vorab-Notiz `Vorab_Notiz_H83_Gravitation_zweite_Lesart.md`, Commit `36ec8e7` (nicht blind). Skript `k198_gravitation_zweite_lesart.py`, Ausgabe `k198_out.json`.

## Rechnung
- **R2 aus g ↦ −g berechnet (sympy, allgemeine diagonale Metrik in t, z):** R[−g] = −R[g], √|g| unverändert, also Einstein–Cartan mit Phase −1 (über das Vierbein ebenso: (i)⁴·(−i)² = −1). Skalar-Kinetik −1, Yang–Mills +1 (zwei inverse Metriken), Potential +1, **Weyl-Kinetik −i** (det e ↦ det e, ein inverses Vierbein ↦ −i).

| Regel | Gewicht EC | Gewicht YM | Weyl | α-Exponent | G-Exponent | reell |
|---|---|---|---|---|---|---|
| R1 (H82) | a − b | a − b | a − b | 1 | 1 | ja |
| R2 (g ↦ −g) | a − b | a + b | a − i·b | 0 | 1 | nein |
| R3 (Metrik c·g) | c | 1 | – | 0 | 1 | ja |

r19 verlangt α 1 und G 2.

## H83 widerlegt (wie erwartet)
Keine Regel trifft beide Gewichte. **Robust ist:** G wächst in jeder Regel mit γ¹, nie mit γ². Der Treffer bei α aus H82 hängt an R1. Die aus den Grundsätzen hergeleitete Regel R2 lässt α unverändert, weil Yang–Mills zwei inverse Metriken hat und das Vorzeichen behält.

## Spannung, für den Autor
Aus g ↦ −g folgt für Spinoren die Phase −i, nicht das Minus, das H79 über F3 gesetzt hat. Unter R2 wird die reduzierte Wirkung der Fermionen komplex: Realteil a, Imaginärteil −b. Das ist genau die Lage der komplexen Lesart K aus r81 (Re S und Im S getrennt stationär). Ob die holomorphe Festlegung (H79) und R2 zusammenpassen, ist offen.

## Zur Lesart des Autors („gemessen wird immer beides“)
In der reduzierten Theorie sind alle gemessenen Konstanten Mischwerte aus M und T; insofern stimmt die Lesart. Eine Vereinheitlichung folgt daraus nicht von selbst: Die Faktoren lassen sich in umdefinierte Parameter aufnehmen, und die einzige Stelle, an der die Struktur Gewichte vorgibt (r19), wird für die Gravitation nicht getroffen. Die Gewichte von r19 stammen aus einer anderen Operation (Umrechnung M ↔ P); eine Abweichung schließt die zweite Lesart nicht aus.
