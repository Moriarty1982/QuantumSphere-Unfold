# H205 / k415 — Drehwinkel-Richtung: ist die θ₁₃-Korrektur geometrisch erzwungen?

**Verdikt: K1 — exakt und strukturell erzwungen** (kein Zufall). Die k373-Beobachtung ist bestätigt und begründet.

Vom Autor gewählte Weggabel (Karte „Drehwinkel-Richtung prüfen", 27.11. 12:38 UTC), nachdem der Quark-Massenstrang ruht und „erstmal die winkel" dran sind.

- **v₀ = (1,0,1)/√2** ist Eigenvektor der neutralen Form N̂ für **jedes** b, c (Eigenwert 1+c) → feste Spalte, unabhängig vom Baumwert δ_ν.
- Die A-ungeraden antisymmetrischen (Ladungs-)Generatoren K₁, K₂ haben Achsen a₁ = (0,1,0), a₂ = (−1,0,1)/√2, beide **exakt ⊥ v₀**, Rang 2 → **span{a₁,a₂} = Ebene senkrecht zu v₀** (die Rotationen, die v₀ kippen = θ₁₃ öffnen).
- (K₁+K₂)/√2 **halbiert** die beiden übrigen Baum-Richtungen u₊=(0,1,0), u₋=(1,0,−1)/√2 **exakt** (45°).
- **Folge:** Die **Richtungsklasse** der θ₁₃-Korrektur im Ladungssektor ist hergeleitet. Frei bleiben: Winkel in der Ebene, Stärke, Vorzeichen. **Aber** (H175): die Daten verlangen den Ladungssektor nicht (erlaubter Raum 5-dim) — strukturelle, keine Datenauszeichnung. **Teilweise nicht blind** (≈45° aus k373 bekannt; neu: Exaktheit + Strukturgrund).

**Werkzeuge:** numpy (k415), Wolfram Language exakt (k415b) — einig.

**Dateien:** `Vorab_H205_Drehwinkel_Richtung.md`, `k415_test_h205.py` (+ `k415_out.txt`), `k415b_kontrolle.wl` (+ `k415b_out.txt`), `Ergebnis_H205_Drehwinkel_Richtung.md`.
