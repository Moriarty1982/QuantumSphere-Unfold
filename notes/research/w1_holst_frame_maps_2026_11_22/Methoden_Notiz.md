# Methoden-Notiz: W1 mit Holst-Term und die Frame-Abbildungen (Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind** (die Zielgrößen γ_M = 0,237533, γ_T = 0,127384, γ_L = 1,864700 sind bekannt). Keine
H-Nummer. Auftrag des Autors: „Ja, Holst-Erkundung“, nach dem Vorschlag, eine Feldgleichung zu erzeugen. Damit öffnet der Autor die
am 6.11.2026 eingefrorene Dynamik-Linie W1/W2 für diese eine Erkundung (`../v4_10_0_w1/Bestandsaufnahme_Wirkungsansaetze.md`).

## Frage
W1 (r81–r86, v4.10.0-r01) ist Einstein–Cartan mit S_grav = −(1/2κ)∫ e R(ω), Dixon-Ablage und Higgs; die Feldgleichungen sind hergeleitet,
aber sie liefern weder eine Skala noch β_sym. Der Holst-Term ergänzt die Wirkung um (1/(κγ))∫ e e R ohne Hodge-Stern; sein Koeffizient
γ ist der Barbero-Immirzi-Parameter, also die Zählgröße hinter OP1. Nach r10.3 ist die Zuordnung der Zählregeln gleichwertig mit einem
frame-abhängigen γ (γ_M/γ_T = γ_L), und nach r30.1 kann das nur von einer nicht-unitären Frame-Abbildung kommen. Gefragt ist:
**Welche Frame-Abbildung ändert γ in der Wirkung W1 + Holst, und auf welchen Wert?**

## Vorwissen geprüft
- `../v4_10_0_w1/Bestandsaufnahme_Wirkungsansaetze.md`: Anforderungen W1–W8, Entscheidungen 1–5, Einfrieren am 6.11.
- `../v4_10_0_r01/README.md`: W1 nichtlinear, Vorzeichen −(1/2κ); Vier-Fermion-Term +(3/16)κ j·j.
- r10.3 (`sources/research/parts/v4100-post-release-layers.tex`): Zuordnung ⇔ frame-abhängiges γ; „die Dualitätsdrehung allein kann
  ein Flächenquant nicht ändern, weil sie alles Geometrische festhält“. Gemeint ist dort die Dualität des Maxwell-Feldes.
- `../op1_area_quantum_boost_2026_11_18/`: unitäre Boosts erhalten das Flächenspektrum (Rovelli–Speziale).
- `../op3_flux_two_thirds_2026_11_13.md`: γ als topologischer Winkel (Holst, Nieh-Yan) nur erwähnt, nicht gerechnet.
- Holst-Term in W1 im Repo nicht gerechnet (Suche nach „Holst“, „Immirzi“).

## Aufbau
Wolfram Language, exakt, Skript `holst_duality.wl`, Ausgabe `run/holst_duality.txt`.
1. Bivektor-Algebra in Minkowski (Signatur +,−,−,−): Hodge-Stern ⋆ auf Bivektoren, ⋆² = −1, selbstduale und antiselbstduale Anteile.
2. Lagrange-Dichte L = A ⟨⋆Σ, R⟩ + B ⟨Σ, R⟩ mit A = −1/(2κ) (W1) und B/A = 1/γ (Holst). Zerlegung in die ±-Anteile mit Koeffizienten
   c± = A(1/γ ∓ i) bzw. der tatsächlich berechneten Form.
3. Wirkung auf (A, B), also auf γ und κ:
   - (L) reelle Lorentz-Transformationen und komplexe Boosts (Rapidität η + iπ/2, wie T in Konvention F) auf Σ und R zugleich;
   - (D1) Dualitätsdrehung R ↦ cos θ R + sin θ ⋆R nur auf der Krümmung;
   - (D2) dieselbe Drehung auf Σ und R zugleich.
4. Gesetz für γ′ und für das Flächenquant a ∝ κγ unter (D1) und (D2), allgemein in θ.

## Vorab festgelegte Auswertung
- Für die im Bestand natürliche Drehung J_B (Dualität um θ = π/2, r16.4) und für die Liste
  θ ∈ {π/4, π/2, iπ/2, η, 2η} mit η = artanh β_sym = 0,617529 werden γ′ = γ_M ↦ ? und a′/a unter (D1) und (D2) berechnet.
- Verglichen wird mit γ_T und mit dem Faktor 1/γ_L (relative Abweichung, Schranke 0,5 %). Bei 5 Winkeln × 2 Gesetzen × 2 Größen
  = 20 Vergleichen ist ein zufälliger Treffer nicht ausgeschlossen; ein Treffer gilt nur als Hinweis und braucht einen eigenen Test.
- Zusätzlich wird der Winkel θ*, der γ_M exakt auf γ_T abbildet, für (D1) und (D2) angegeben, ohne ihn mit weiteren Konstanten zu
  vergleichen.

## Was daraus folgt (vorab)
- Zeigt (L) Invarianz und (D1)/(D2) eine Verschiebung, ist die Dualität auf der Krümmung die einzige Stelle in W1 + Holst, an der ein
  frame-abhängiges γ entstehen kann. Ob J_B auf die Krümmung fortgesetzt wird, ist dann eine Setzung, die benannt wird.
- Kein Ergebnis dieser Erkundung schließt OP1; ein Treffer wäre nicht blind.
