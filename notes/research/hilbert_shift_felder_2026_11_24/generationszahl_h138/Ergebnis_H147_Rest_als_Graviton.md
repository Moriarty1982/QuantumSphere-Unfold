# Ergebnis H147: Die HS(0)-Linie ist ein masseloser, neutraler Skalar, kein Spin-2-Graviton; Spin 2 bietet die Algebra nur antisymmetrisch

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H147_Rest_als_Graviton.md` (Commit 61e5ff3; großteils nicht blind). Skripte `k330_rest_graviton.py`
(`k330_out.txt`), `k330b_spin2_und_mischwinkel.py` (`k330b_out.txt`, berichtigte Auswertung des Ableitungskanals und nachträgliche Erkundung
zum Mischwinkel), `k330c_gegenprobe.wl` (`k330c_out.txt`, Wolfram exakt). Status: H147a, b, c, d bestätigt (c nach Berichtigung einer
Auswertung, siehe unten). Lesart B (Hauptuntergruppe in G₂) nur darstellungstheoretisch, nicht numerisch gebaut.**

Anlass: Autor: „unser neuer quasi HS(0) dürfte doch verschwindend klein sein, könnte das unser gesuchtes Austauschteilchen zur Gravitation
sein?“, „ist die Tensorstruktur nicht schon durch den Raum, in dem es erzeugt wird, automatisch gegeben?“ und „es könnte sein, dass es beide
Zustände und Mischwinkel davon annehmen kann, dann wäre es mal Higgs, mal skalare Gravitation und manchmal was dazwischen“.
Werkzeuge: Python (numpy), Wolfram exakt; Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H147a | Linie c in allen 54 Generationsauswahlen exakter Nullvektor der Gram-Matrix (≤ 10⁻¹⁵); Ladung und Farbe wirken nur auf y | vorab, nicht blind | **bestätigt** |
| H147b | Lesart A (SO(3) ⊂ SU(3)_Farbe, alle 8 total reellen Koordinaten-Tripel): ℂ𝕆 = 2 × Spin 0 ⊕ 2 × Spin 1 (Wolfram exakt); Rest-Generation c ⊗ ℂ𝕆 ebenso; die Linie c selbst Spin 0; Lesart B: 1 ⊕ 7 = Spin 0 ⊕ Spin 3 | kein Spin 2 | **bestätigt** |
| H147c | Sym²(𝕆) äußeres Produkt: Spins 0, 1, 2 (Spin-2-Dimension 15); symmetrisches Algebrenprodukt auf dem Spin-2-Teil: Norm ≤ 7·10⁻¹⁵ (null); Ableitungen D_{x,y} spannen g₂ (Rang 14), ihr su(3)-Teil enthält Spin 2 voll (Rang 5; su(3) = Spin 1 ⊕ Spin 2, Wolfram exakt) | alle drei | **bestätigt** |
| H147d | c ∘ c auf dem Träger exakt gleichgewichtet (Spreizung ≤ 5·10⁻¹⁵), Träger stets 4 Kopien; c selbst mit Vorzeichen (−1, −1, 1, 1) | vorab | **bestätigt** |

**Berichtigung (offengelegt):** Der erste Lauf (k330) projizierte den su(3)-Anteil der Ableitungen mit einem nicht spektralen Projektor und
meldete Rang 3–5 je Tripel. Das war ein Fehler der Auswertung; k330b rechnet in der Eigenbasis der Casimir-Matrix und findet in allen 8 Fällen
Rang 5. Die Algebra-Aussage war vorab festgelegt und ändert sich nicht.

## Mischwinkel zwischen zwei Skalaren (Erkundung, nachträglich, nicht blind)
Im Rest gibt es zwei skalare Richtungen: c ⊗ e₀ (die reelle Einheit, HS(0)) und c ⊗ e₇ (die Ladungsachse). Ergebnisse (k330b):
- Die Ladungsdrehung exp(iφQ) dreht e₀ in e₇ um den Winkel φ/2 (bis auf eine Gesamtphase), also gibt es eine stetige Familie
  cos θ · e₀ + sin θ · e₇. Unter der Ladungssymmetrie ist θ **frei**.
- Kein Automorphismus mischt die beiden (alle Ableitungen fixieren e₀). Die Algebra unterscheidet die Enden: e₀² = +e₀ (Einheit, s = 0, im
  Sinn von H144 lichtartig), e₇² = −e₀ (s = 1).
- Lesart des Autors: Ein Ende Dilaton-artig (die reelle Einheit), das andere an der Ladungsachse, dazwischen ein freier Winkel. Das hat dieselbe
  Gestalt wie die offene Frage nach dem freien Drehwinkel der Mischung (H131/H134): Die Symmetrie lässt den Winkel frei, festlegen müsste ihn
  ein Potential bzw. die Feldgleichung. Ob das Ende an e₇ ein Higgs ist, ist nicht gezeigt (kein SU(2)-Dublett, keine Hyperladung hier).
- Literatur (aus dem Gedächtnis, in dieser Sitzung nicht nachgeschlagen): Higgs-Dilaton-Mischung bei Goldberger, Grinstein und Skiba (2008) und
  in der Higgs-Dilaton-Kosmologie (Shaposhnikov, Zenhäusern 2009; García-Bellido u. a. 2011). Dort legt das Potential den Winkel fest.

## Lesart
- **Antwort:** Die HS(0)-Linie hat zwei Merkmale eines Austauschteilchens der Gravitation: Sie ist neutral und (in der Gram-Auslesung) masselos.
  Sie ist aber ein **Skalar** (Spin 0) unter jeder Drehgruppe, die hier wirkt, also eher eine skalare Gravitation bzw. ein Dilaton als das
  Spin-2-Graviton.
- **Zur Teilfrage „Tensor aus dem Raum“:** Ja, der Raum, in dem die Linie lebt, bringt eine Tensorstruktur mit, aber nur auf zwei Wegen:
  im äußeren Tensorprodukt zweier Zustände (das gibt Spin 2 für jedes Vektorfeld, ist also nicht eigen) und im Ableitungskanal D_{x,y}, der den
  Spin-2-Teil von su(3) (die symmetrischen spurfreien 3×3-Matrizen) voll erreicht, aber antisymmetrisch in den beiden Zuständen ist. Das
  Produkt der Algebra selbst löscht den Spin-2-Teil. Zwei Rest-Zustände koppeln dabei gleich stark an alle vier Kopien (c ∘ c = (1, 1, 1, 1)).
- **Was offen bleibt:** welche SO(3) der Ortsraum ist (gesetzt), eine symmetrische Spin-2-Kopplung (bräuchte die Metrik als zusätzliche Regel,
  wie in W1/W2), Kopplungsstärke, Newton-Konstante, Λ. Ein masseloser Skalar mit gleicher Kopplung an alle Generationen wäre durch
  Tests der fünften Kraft stark eingeschränkt; das ist hier nicht gerechnet. OP5 offen; kein Guard berührt.
- Vergeben: H147, k330. Nächste frei: H148, k331.
