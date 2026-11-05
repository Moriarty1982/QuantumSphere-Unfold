# Wirkung W2: W1 plus Higgs-Sektor (Aufbau, 5. November 2026)

**Status: Aufbau und analytische Erkundung, ohne Kriterium.** Ausgelöst durch den nächsten Schritt der Übergabe; I4 (Auslöser 1: Arbeit am Higgs-Sektor) ist damit fällig.

## Aufbau
W2 = W1 + Higgs-Dublett Φ mit
L_H = e[ |D_μΦ|² − V(Φ) ],  V = −μ²|Φ|² + λ|Φ|⁴,
dazu Yukawa-Kopplungen über die antilinearen Konnektoren aus r44.1(b) (Kern → Bild von C_ch, Higgs-Quantenzahlen Y/2 = ±½).
- **Lesart des negativen Massenquadrats** (k185, Erkundung): Der Übergangs-Konnektor zwischen Materie und gegenläufigem Tachyonbild hat q² = −2m² sinh 2η. Das Vorzeichen −μ² ist damit eine Lesart dieses Übergangs, **keine Herleitung**. μ und λ bleiben Eingaben.
- **Offene Modellwahl:** Ist Φ ein elementares Feld (wie im Standardmodell) oder der Konnektor als zusammengesetztes Feld (Bilinear ψ_M ψ_T)? W2 nimmt vorerst das elementare Feld; die zusammengesetzte Lesart ist ein späterer Test.

## Vakuumenergie (analytisch, Erkundung)
- Im Minimum |Φ|² = μ²/(2λ) gilt V_min = −μ⁴/(4λ). Das ist ein Λ-Term der Größe ρ_vac = V_min. Mit den Higgs-Werten (μ ≈ 88 GeV, λ ≈ 0,13) ist |V_min|^{1/4} ≈ 100 GeV, rund 10⁵⁵-mal zu viel (bekanntes Λ-Problem, Vorwissen). **W2 erzeugt also einen Vakuumterm, aber den falschen.**
- **M–T-Bilanz:** Nimmt man zu jedem Feld sein Tachyonbild mit dem Vorzeichen aus F3 dazu (wie in H69), wechselt dessen gesamter Energie-Impuls-Tensor das Vorzeichen, einschließlich der Vakuumenergie. Gewichtet die Gravitation die Lesarten mit a (M) und b (T), so ist ρ_vac = (a − b)·V_min:
  - Photon-Gewichte (a = b): ρ_vac = 0 **exakt**, unabhängig von μ und λ;
  - Materie-Gewichte (a = p₊, b = p₋): ρ_vac = V_min/γ, immer noch ≈ 10⁵⁵ zu groß.
- **Literatur (Vorwissen, nicht nachgeschlagen):** Kaplan und Sundrum (2005, „A symmetry for the cosmological constant“) schlagen eine Kopie des Standardmodells mit negativer Energie vor, die über eine „Energieparität“ die Vakuumenergie aufhebt. Das ist strukturell dieselbe Idee wie die M–T-Paarung mit F3-Vorzeichen. Dort bleibt das Problem der Stabilität (Felder negativer Energie); die Kopplung beider Sektoren nur über die Gravitation soll es entschärfen.

## Lesart
- Die M–T-Paarung hebt nicht nur Strom und Energie der masselosen Fermionen auf (H69), sondern bei gleichen Gewichten auch die Higgs-Vakuumenergie, für jede Höhe. Das wäre ein **struktureller Mechanismus gegen das Λ-Problem**: Der Companion liest „Λ = 0 im Photon-Frame“ (T9) genau so.
- Der beobachtete kleine Wert müsste dann aus der **Abweichung** von gleichen Gewichten kommen. Mit den Materie-Gewichten ist die Abweichung 1/γ ≈ 0,54, viel zu groß. Für ρ_Λ ≈ (2,2 meV)⁴ bräuchte es (a − b) ≈ 10⁻⁵⁵. Das ist nicht natürlich, solange nichts die Gewichte so fein abstimmt.
- I4 (Kondensation durch Expansion) wäre die dynamische Fassung: Die Gewichte bzw. die Kondensate von M und T entwickeln sich mit der Expansion; ein winziger Rest könnte aus der Zeitverschiebung (Versatz δ, H70) entstehen. Das ist eine Frage, nicht gerechnet.

## Nächste Schritte (Vorschlag)
1. **H74 (vorab):** Ist die exakte Aufhebung der Higgs-Vakuumenergie bei Photon-Gewichten stabil gegen die Kopplung beider Sektoren über die Gravitation und über den Konnektor? Kaplan–Sundrum zeigen, wo das typisch scheitert; das wäre die Prüfung.
2. Rest-Λ aus dem Versatz: Ergibt ein mitbewegter Versatz δ ∝ a zwischen M- und T-Kondensat einen kleinen, zeitabhängigen Rest?
3. Zusammengesetzte Lesart von Φ (Konnektor-Bilinear) gegen elementares Φ.


## Nachtrag (5.11., H74)
Die exakte Aufhebung ist gegen jede direkte Kopplung der Sektoren instabil (Resonanz gleicher Spektren, Rate ε/2ω). Stabil nur bei Verstimmung |Δω²| > 2ε, dann bleibt ein Rest ≳ 2ε|V_min|/ω². Kleiner Rest-Λ verlangt extrem schwache Kopplung; Kopplung nur über die Gravitation bleibt offen. Siehe `Ergebnis_H74_Stabilitaet_MT.md`.

## Nachtrag (5.11., H75)
Nur über die Gravitation gekoppelt: keine Resonanz, kein exponentielles Wachstum bei exakter Paarung; gemeinsames Durchgehen (∝ t², Bondi) als Preis. Siehe `Ergebnis_H75_Gravitationskopplung.md`.
