# Erster Feldansatz für den gerichteten OP5-Vermittler: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Ein Tensorfeld X_ij quer zur Achse und ein Skalar S, beide an η gekoppelt, geben Feldgleichungen, deren Austausch
den Vermittlerterm des Vergleichsmodells exakt reproduziert, mit eindeutigen Kopplungen g² = ⅔g_m², κ = ½, g_s² = ⅓g_m², sofern Tensor und
Skalar gleiche Masse und Geschwindigkeit haben. Der Ansatz ist geisterfrei und für die Modellwerte stabil; die statische Energie verlangt
g_m² ≤ 3r_m. Der String aus r37 legt κ = ½ genau fest, liefert aber den Skalar nicht. **Nach dem vorab festgelegten Raster: trägt teilweise.**

Auftrag des Autors: „wäre eine feldgleichung bzw. ein erster ansatz davon nicht erstmal sinnvoll?“, „ja, anlegen und rechnen“. Verfahren vorab:
`Methoden_Notiz.md` (Commit 6bad83cb). Skript `mediator_field_equation.wl`, Ausgabe `run/mediator_field_equation.txt`, Wolfram exakt (Stabilität
zusätzlich numerisch auf einem Raster). Keine H-Nummer.

## Feldgleichungen (Ruhesystem u, Achse n = e_z, i, j ∈ {x, y})
- (∂_t² − r_mΔ + m²) X_ij = g (∂_i∂_j − κδ_ij∂_t²) η
- (∂_t² − r_sΔ + m_s²) S = g_s ∂_t² η
- 2(∂_t² − Δ + m_H²) η = 𝒥_h + g (∂_i∂_jX_ij − κ∂_t²X_ii) + g_s ∂_t²S

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) Austausch | effektiver η-Operator 2(m_H² + q − x) − g²TrV²/d_m − g_s²x²/d_s mit TrV² = a_⊥² − 2κa_⊥x + 2κ²x² |
| (2) Abgleich | Für d_s = d_m gilt g²TrV² + g_s²x² = g_m²N_m identisch genau für g² = ⅔g_m², κ = ½, g_s² = ⅓g_m² (eindeutig bis auf Vorzeichen). Ohne Skalar fehlt −⅓g_m²x². Für d_s ≠ d_m entstehen zwei Pole statt einem. |
| (3a) geisterfrei | Kinetische Matrix positiv definit genau für g²κ² < 1 und g_s² + 2g²κ² < 2; mit den Abgleichwerten g_m² < 3. |
| (3b) statisch | Statische Energie positiv für alle **k** genau für g² ≤ 2r_m, also g_m² ≤ 3r_m. Für r_m = ½: g_m² ≤ 3/2. |
| (3c) Dispersion | Raster mit r_m = ½: alle Lösungen reell und positiv für g_m² = 3/100, 1, 7/5; für 8/5 instabil bei großem a_⊥ (kleinste Wurzel −1,31), wie (3b) verlangt. |
| (4) String | r37 entspricht κ = ½, g_s = 0: TrV² = ½(2a_⊥² − 2a_⊥x + x²). Es fehlt der Skalar mit g_s²/g² = ½. |

## Lesart
- Der Vermittler hat jetzt Feldgleichungen statt eines gesetzten Operators. Die Zahlen ⅔ und −⅔ in N_m sind keine freien Wahlen mehr: Sie folgen
  aus einem Tensor quer zur Achse mit der Spurkopplung κ = ½, und genau diesen Wert liefert der gespannte String.
- Neu ist eine Rolle für r_m: Für den führenden Kontrast war r_m entbehrlich (r35.2), für die Stabilität nicht. Die Kopplung ist durch
  g_m² ≤ 3r_m begrenzt; ein Medium mit r_m → 0 könnte diesen Vermittler nicht stabil tragen.
- Offen: der Skalar S (Gewicht ½ relativ zum Tensor) und seine Entartung mit dem Tensor (d_s = d_m). Die Entartung legt nahe, S als weitere
  Komponente desselben Feldes zu lesen (etwa die Zeit-Zeit-Komponente eines Tensors auf dem Unterraum senkrecht zur Achse); das ist Lesart.
  Ebenso offen: ein Feld X_ij(x) setzt viele gleich ausgerichtete Strings voraus, deren Kopplung r_m festlegen würde.
- OP5 und H96 bleiben offen.
