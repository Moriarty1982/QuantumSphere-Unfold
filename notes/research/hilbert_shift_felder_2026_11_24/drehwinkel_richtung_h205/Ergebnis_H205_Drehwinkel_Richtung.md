# Ergebnis H205 (k415): Die θ₁₃-Korrekturrichtung ist strukturell erzwungen — exakt, kein Zufall (K1)

**Datum:** 2026-11-27. **Werkzeuge:** numpy (Konstruktion, Eigenvektoren, Projektionen), **Wolfram Language** exakt (Achsenvektoren, Orthogonalität, Eigenvektor-Identität, Bisektion, Rang). Beide einig.
**Vorab:** `Vorab_H205_Drehwinkel_Richtung.md` (vor der Rechnung committet). **Teilweise nicht blind** (siehe unten).

## Frage
Ist die in k373 **beobachtete** (nicht geprüfte) Geometrie der θ₁₃-Korrektur — Achsen der A-ungeraden (Ladungs-)Generatoren K₁, K₂ senkrecht zur festen Baum-Spalte v₀ = (1,0,1)/√2, und (K₁+K₂)/√2 als 45°-Halbierende der beiden übrigen Baum-Richtungen — **exakt und strukturell erzwungen**, oder Zufall?

## Befund: K1 — exakt und strukturell erzwungen

Drei exakte Identitäten (Wolfram, Reste = 0; numpy ≤ 2·10⁻¹⁷):

1. **Feste Spalte, baumunabhängig.** v₀ = (1,0,1)/√2 ist Eigenvektor der neutralen Form N̂ = [[1,b,c],[b,1,−b],[c,−b,1]] für **jedes** b, c (Eigenwert 1+c; die mittlere Zeile gibt b·1 − b·1 = 0). v₀ ist damit die feste Spalte **unabhängig vom Baumwert δ_ν**, nicht nur bei δ_ν = π/6.

2. **Achsen ⊥ v₀, spannen die Ebene.** Die Achsenvektoren der A-ungeraden antisymmetrischen Generatoren sind a₁ = axis(K₁) = (0,1,0) und a₂ = axis(K₂) = (−1,0,1)/√2. Beide exakt orthogonal zu v₀ (a₁·v₀ = a₂·v₀ = 0), orthogonal zueinander (a₁·a₂ = 0), Rang 2. **span{a₁, a₂} = Ebene senkrecht zu v₀** (v₀ liegt nicht darin, Rang{a₁,a₂,v₀} = 3). Die A-ungeraden antisymmetrischen Generatoren sind also genau die Rotationen mit Achse ⊥ v₀ — die v₀ kippen und damit θ₁₃ öffnen.

3. **Exakte 45°-Halbierung.** a₁ und a₂ **sind** (bis auf Norm/Vorzeichen) selbst die beiden übrigen Baum-Richtungen u₊ = (0,1,0), u₋ = (1,0,−1)/√2. Daher halbiert (a₁+a₂)/√2 sie exakt: gleiche Projektionen ((a₁+a₂)/√2·u₊ = +1/√2, ·u₋ = −1/√2), also 45°/45°. (Die numpy-Winkelprüfung meldete eine Scheinabweichung von 1,8·10⁻⁶° — reines arccos-Runden nahe 45°; Wolfram zeigt die exakte Gleichheit.)

**Strukturgrund:** Die ℤ₂-Symmetrie A aus k262 zeichnet die Ebene senkrecht zu v₀ aus; jede A-ungerade antisymmetrische (Ladungs-)Korrektur dreht um eine Achse in dieser Ebene. Die k373-Beobachtung ist damit **keine zufällige Zahlenkoinzidenz**, sondern eine exakte Folge der Konstruktion.

## Was das heißt (ehrliche Einordnung)
- **Hergeleitet:** die **Richtungsklasse** der θ₁₃-Korrektur im Ladungssektor — sie liegt in der Ebene senkrecht zur festen Spalte v₀, und die symmetrische Kombination (K₁+K₂)/√2 ist in dieser Ebene durch die 45°-Halbierung ausgezeichnet.
- **Weiter frei:** der Winkel **innerhalb** der Ebene (welche Mischung aus K₁, K₂), die **Stärke** (tan x) und das **Vorzeichen**. Die H168-Spannung (Neutrino- vs. Lepton-Versatz, 5,7σ in H176) bleibt offen.
- **Kein Datensieg:** Nach H175 verlangen die Daten den Ladungssektor **nicht** (der erlaubte Term-Raum ist 5-dimensional, und die θ₁₂-bewegenden symmetrischen Terme sind ebenso zugelassen). H205 ist eine **strukturelle** Auszeichnung der Ladungsrichtung, keine Datenauszeichnung: die Geometrie macht die Ladungsrichtung zur natürlichen θ₁₃-Richtung, zwingt die Natur aber nicht, nur sie zu nehmen.

## Ehrlichkeit (teilweise nicht blind)
**Nicht blind:** *dass* die Zahlen ≈ 45°/orthogonal sind, war aus der k373-Beobachtung bekannt. **Blind/neu geprüft:** dass es sich um **exakte** Identitäten handelt, der **Strukturgrund** (v₀ Eigenvektor für alle δ_ν; A-ungerade antisymmetrische Generatoren = Rotationen mit Achse ⊥ v₀), und die ehrliche Folge für den Freiheitsgrad-Zählstand (Richtungsklasse hergeleitet, Stärke/Winkel-in-Ebene/Vorzeichen frei, Daten verlangen die Richtung nicht).

## Stand Mischungswinkel (Strang 3)
- **Hergeleitet:** TM1-Baum bei δ_ν = π/6 (H173, exakt); feste Spalte v₀ baumunabhängig und die θ₁₃-Richtungsklasse im Ladungssektor (H205, exakt).
- **Gesetzt/frei:** Ein-Feld-Form (H158), Brannen-Spektrum (H99), Versatz x / Stärke, Winkel in der Ebene, Vorzeichen; die gemeinsame-Versatz-Annahme H168 steht mit H176 in Spannung. OP3/OP4 bleiben offen.

## Dateien
- `Vorab_H205_Drehwinkel_Richtung.md` — Vorab-Notiz (vor der Rechnung).
- `k415_test_h205.py`, `k415_out.txt` — numpy-Rechnung und Ausgabe.
- `k415b_kontrolle.wl`, `k415b_out.txt` — Wolfram-Gegenkontrolle (exakt).
