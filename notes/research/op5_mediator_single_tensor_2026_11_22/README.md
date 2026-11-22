# Der Skalar als Komponente eines einzigen Tensorfelds: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Ein einziges symmetrisches Tensorfeld H_ab auf dem Unterraum (t, x, y) senkrecht zur Achse, mit einer Masse und
einer Geschwindigkeit, gibt den Vermittlerterm des Vergleichsmodells exakt, wenn es an die identisch erhaltene Kombination
J_ab = ∂_a∂_bη − η_ab□_∥η koppelt (die Unterraum-Fassung der Verbesserung S^{μν} aus r32.0) und die Zeit-Quer-Komponenten H_0i nicht koppeln.
Gewicht und Entartung des Skalars aus r38 sind damit hergeleitet. Die Zeit-Zeit-Komponente koppelt dabei an Δ_⊥η, nicht an ∂_t²η, und der
Quertensor-Vertex ist nicht der des Strings. **Nach dem vorab festgelegten Raster: trägt teilweise** (w = 0 ist eine Strukturwahl).

Auftrag des Autors: „skalar als zeit-zeit-komponente herleiten“. Verfahren vorab: `Methoden_Notiz.md` (Commit 538b11d6). Skript
`single_tensor.wl`, Ausgabe `run/single_tensor.txt`, Wolfram exakt, Stabilität zusätzlich auf dem Raster von r38. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) Austausch | N(c, w) = (3c² − 2c + 1)(x² + a_⊥²) + (4c − 6c² + 2w)a_⊥x. Gleich λN_m genau für w = (3c+1)(c−1)/2, λ = 3(3c² − 2c + 1)/2. |
| w = 1 | nur c = (1 ± √10)/3, λ = 6: keine ausgezeichneten Werte. |
| w = 0 | c = 1 oder c = −⅓, λ = 3, also g′² = g_m²/3. |
| (2) Erhaltung | p^aJ_ab = 0 genau für c = 1. Mit c = 1 verlangt der Abgleich w = 0. |
| (3) Vertizes bei c = 1 | H_00: −a_⊥ (also Δ_⊥η); H_ij: −k_ik_j − (x − a_⊥)δ_ij. Zerlegung anders als r38: (H_00, Spur) trägt a_⊥²/2 − ⅔a_⊥x + ⅔x², der spurfreie Teil a_⊥²/6 (r38: a_⊥²/3 − ⅔a_⊥x + ⅔x² und a_⊥²/3). Gleiche Summe, keine Drehung im Feldraum. Stringvertex k_ik_j − (x/2)δ_ij weicht ab. |
| (4) Stabilität | Kinetische Mischung nur über die Spur; geisterfrei für g_m² < 3; statischer Zähler ⅔g_m²a_⊥² wie im Modell, also g_m² ≤ 3r_m; Raster wie r38 (8/5 instabil bei r_m = ½). |

## Lesart
- Der Skalar braucht kein eigenes Gewicht und keine eigene Masse mehr: Ein Feld mit einer Masse liefert beides, und die Kopplung an die
  erhaltene Kombination J_ab ist ausgezeichnet. J_ab ist die Fassung der Verbesserung S^{μν} = p^μp^ν − η^{μν}d aus r32.0 auf dem Unterraum
  senkrecht zur Achse; so schließt sich der Kreis zur Herkunft der Form des Vergleichsoperators.
- Gewählt bleibt, dass H_0i nicht koppeln (w = 0). In einer Fierz–Pauli-artigen Dynamik wären die Zeitkomponenten Hilfsfelder ohne eigenen Pol;
  das ist Lesart, nicht gerechnet.
- Spannung zu r37/r38: Der Quertensor des Einzelfelds koppelt mit −k_ik_j − (x − a_⊥)δ_ij, der String mit k_ik_j − (x/2)δ_ij. Beide Zerlegungen
  geben dasselbe N_m, aber nicht mit denselben Komponenten. Entweder trägt der String nur einen Teil, oder das Einzelfeld ist nicht seine
  Feldfassung; offen.
- OP5 und H96 bleiben offen.
