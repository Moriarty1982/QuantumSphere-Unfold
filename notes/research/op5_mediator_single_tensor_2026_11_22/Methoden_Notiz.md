# Methoden-Notiz: Der Skalar des Feldansatzes als Zeit-Zeit-Komponente eines Tensors (Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Beim Entwurf wurde von Hand skizziert, dass die erhaltene Kopplung (c = 1 unten) ohne
Zeit-Quer-Komponenten N_m ergibt. Keine H-Nummer. Auftrag des Autors: „skalar als zeit-zeit-komponente herleiten“, nach Runde v4.10.0-r38.

## Vorwissen geprüft
- r38: Tensor X_ij quer zur Achse plus Skalar S; Austausch = −g_m²N_m/d_m genau für g² = ⅔g_m², κ = ½, g_s² = ⅓g_m² und d_s = d_m. Gewicht
  und Entartung des Skalars gesetzt; Lesart: S als Zeit-Zeit-Komponente.
- r32.0: Die Form des Vergleichsoperators folgt aus der identisch transversalen Verbesserung S^{μν} = p^μp^ν − η^{μν}d (p_μS^{μν} = 0).
- r36.3: Familie positiver Polarisationssummen mit N_m; Zeit-Quer-Block β ∈ [0, ⅓].
- r37: Stringvertex ∝ k_ik_j − 2ω₁²δ_ij am Pol.

## Ansatz
Ein symmetrisches Tensorfeld H_ab auf dem Unterraum (t, x, y) senkrecht zur Achse, a, b ∈ {0, 1, 2}, mit **einer** Masse m und **einer**
Geschwindigkeit r_m für alle Komponenten und positiver kinetischer Energie jeder Komponente:
L_H = ½ Σ_ab [(∂_tH_ab)² − r_m(∇H_ab)² − m²H_ab²]. Kopplung g′ H^ab J_ab mit
J_ab = ∂_a∂_bη − c η_ab □_∥η, η_ab = diag(1, −1, −1), □_∥ = ∂_t² − ∂_x² − ∂_y²,
und einem Gewicht w ≥ 0 der Zeit-Quer-Komponenten H_0i in der Kopplung (w = 1 natürlich, w = 0 entkoppelt). H_00 ist die Zeit-Zeit-Komponente,
H_ij der Quertensor aus r38.

## Fragen und Rechnung (Wolfram, exakt; Skript `single_tensor.wl`, Ausgabe `run/single_tensor.txt`)
1. Austauschzähler N(c, w) = Σ_ab (Gewicht) V_ab² im Fourierbild; für welche (c, w) ist N ∝ N_m identisch in x und a_⊥? Proportionalität → g′².
2. Erhaltung: p^aJ_ab = 0 (mit η_ab) genau für welches c?
3. Vergleich mit r38: Vertizes von H_00 und der Spur von H_ij gegen die von S und X_ii; folgt r38 durch eine Drehung im Feldraum, oder ist die
   Zerlegung eine andere? Stimmt der Quertensor-Vertex mit dem Stringvertex aus r37 überein?
4. Stabilität: kinetische Matrix, statische Energie, Dispersion auf dem Raster von r38.

## Raster (vorab)
- **trägt:** Ein einzelnes Feld H_ab mit erhaltener Kopplung und w = 1 gibt N_m; Gewicht und Entartung des Skalars folgen.
- **trägt teilweise:** N_m folgt aus einem einzelnen Feld (Gewicht und Entartung damit hergeleitet), aber nur mit einer zusätzlichen
  Strukturwahl, etwa w = 0 oder einem nicht ausgezeichneten c.
- **trägt nicht:** Kein (c, w) mit w ≥ 0 gibt N_m.

Frames: alles im Materie-Frame M, Rahmen und Achse wie in r36–r38. OP5 bleibt in jedem Fall offen.
