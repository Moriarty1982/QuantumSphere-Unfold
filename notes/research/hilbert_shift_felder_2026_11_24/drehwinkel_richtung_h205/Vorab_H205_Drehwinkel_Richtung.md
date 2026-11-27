# Vorab-Notiz H205 (k415): Ist die Richtung der θ₁₃-Korrektur geometrisch erzwungen?

**Datum:** 2026-11-27. **Strang:** Lepton-Mischung (Strang 3), freier Drehwinkel. **Auslöser:** Autor, 27.11., „erstmal die winkel" (Mischungsstrang jetzt, Quarkmassen ruhen). Karte „Wie weiter bei den Mischungswinkeln?", Option „Drehwinkel-Richtung prüfen". Einordnung: `wiki/Gesamtbild.md` T8/T13, OP4.

## Frage
H173 zeigte: am Baumwert δ_ν = π/6 ist die Lepton-Mischung **exakt** tribimaximal (TM1: θ₂₃ = 45°, |sin δ_CP| = 1, sin²θ₁₂ = ⅓, θ₁₃ = 0). θ₁₃ ≠ 0 entsteht erst durch einen symmetriebrechenden Zusatzterm. H175 fand: der erlaubte Raum dieser Terme ist 5-dimensional, die Daten zeichnen **keine** Richtung aus. Im Nachtrag k373 wurde aber **beobachtet** (nicht geprüft): die Achsenvektoren der beiden A-ungeraden (Ladungsrichtungs-)Generatoren K₁ = i(E₁₃−E₃₁), K₂ = i(−E₁₂+E₂₁+E₂₃−E₃₂)/√2 spannen die Ebene senkrecht zur festen Baum-Spalte v₀ = (1,0,1)/√2 auf, und (K₁+K₂)/√2 liegt mittig (45°) zwischen den beiden übrigen Neutrino-Baum-Richtungen.

**H205:** Sind diese beiden Aussagen **exakte** Identitäten, von der Konstruktion der A-ungeraden Generatoren und der TM1-Struktur **erzwungen** (dann wäre die θ₁₃-Korrektur-Richtung hergeleitet, nur Stärke und Vorzeichen blieben frei), oder gelten sie nur näherungsweise / bei zufällig passenden Zahlen?

## Was gerechnet wird (k415)
Maschinerie aus k371 (DIRS, N̂). Exakt (Wolfram) und numerisch (numpy):
1. **Baum-Richtungen:** Eigenvektoren von N̂(π/6, 1); identifiziere die feste Spalte v₀ und die beiden übrigen Richtungen u₊, u₋.
2. **Achsenvektoren** a₁, a₂ der reell-antisymmetrischen Teile von K₁, K₂ (Dualvektor: A_ij = ε_ijk a_k).
3. **Test (a) Orthogonalität:** a₁·v₀ = 0 und a₂·v₀ = 0 (liegen die Achsen in der Ebene ⊥ v₀)? Exakte Reste.
4. **Test (b) Halbierung:** Winkel von (a₁+a₂)/√2 (bzw. (a₁−a₂)/√2) zu u₊ und zu u₋ — gleich (45°-Bisektion)? Exakt.
5. **Strukturgrund:** Ist der 2-dim Raum der A-ungeraden antisymmetrischen Generatoren genau der Raum der Rotationsgeneratoren mit Achse ⊥ v₀? (d. h. erzwingt die ℤ₂-Symmetrie A aus k262, dass die θ₁₃-Korrektur um eine Achse ⊥ v₀ dreht?) — Projektionen/Rang.
6. **Allgemeinheit:** Hängt (a) vom Baumwert δ_ν ab, oder gilt es für die feste Spalte unabhängig von δ_ν? (v₀ ist δ_ν-abhängig; a₁,a₂ fest.)

## Entscheidungskriterien (vorab)
- **K1 (Richtung hergeleitet):** Test (a) exakt (Reste ≤ 10⁻¹²) **und** der Strukturgrund (5) trägt: die A-ungeraden antisymmetrischen Generatoren sind genau die Rotationen mit Achse ⊥ v₀ (Rang 2, exakt). Dann ist die θ₁₃-Korrektur **auf die Ebene ⊥ v₀ festgelegt** (Richtung bis auf einen Winkel in dieser Ebene hergeleitet). Die 45°-Bisektion (b) zusätzlich exakt ⇒ auch die konkrete Richtung (K₁+K₂)/√2 ist ausgezeichnet.
- **K2 (Zufall / frei):** Test (a) oder der Strukturgrund (5) nicht exakt (nur näherungsweise, oder von einer Zahlwahl abhängig). Dann ist die Richtung nicht erzwungen; die Korrektur bleibt frei (wie die Quark-Kopplungen nach H202/H204).

## Erwartung (ehrlich)
Offen. Teil (a)/(5) ist plausibel erzwungen (die A-Symmetrie ist eine echte Struktur aus k262), Teil (b) eher eine Eigenschaft der speziellen Kombination. **Nicht blind** ist, **dass** die Zahlen ≈45°/⊥ sind (aus k373 bekannt); **blind geprüft** wird, ob es **exakte, strukturell erzwungene** Identitäten sind und was sie am Freiheitsgrad-Zählstand ändern (Richtung hergeleitet vs. frei). Selbst bei K1 bleiben Stärke tan x, Vorzeichen und die H168-Spannung (Neutrino- vs. Lepton-Versatz) offen; die Daten verlangen die Richtung nach H175 ohnehin nicht — K1 wäre eine **strukturelle** Auszeichnung, keine Datenauszeichnung.

## Vorwissen geprüft
- `mischung_h173/` (H173): TM1 am Baum exakt; θ₁₃ aus Versatz; eine Zahl trifft R und θ₁₃ nicht zugleich.
- `mischung_h175/` (H175, k371–k373): 8 ℤ₃-brechende Terme, 2 Gruppen; erlaubter Raum 5-dim; Ladungsrichtung möglich, nicht nötig; k373-Beobachtung (⊥, 45°) ungeprüft.
- `mischung_h174/` (H174): nötiger Term halb imaginär-antisymmetrisch.
- k262/k262b (Träger, ℤ₃, A-ungerade), H158 (Ein-Feld-Form), H99 (Brannen-Spektrum), H168 (gemeinsamer Versatz δ_ν = π/6).

## Werkzeuge
numpy (Konstruktion, Eigenvektoren, Projektionen) und **Wolfram Language** exakt (Achsenvektoren, Orthogonalität, Bisektionswinkel, Rang des A-ungeraden Generatorraums). Qiskit nicht einschlägig.
