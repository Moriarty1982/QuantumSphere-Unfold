# Vorab-Notiz H7: Wählt der Heisenberg-Kompensator zwischen TM1-Lift und θ₁₃ = 0-Lift?

Festgelegt am 2026-10-20, **vor** der Rechnung. Bezug: K6.1/K6.2, K18.5, K19.

## Ausgangslage

Heisenberg-Kompensator C = ½(1 + J) mit linearer Involution J (K6.1). Soll J eine Symmetrie der Algebra sein, muss
es ein Vorzeichen-Automorphismus sein: vier Einheiten negiert, eine quaternionische Linie fest (K6.2). Die
ursprüngliche J_B ist die e₁-Spiegelung, deshalb werden bevorzugt die Vorzeichen-Automorphismen betrachtet, die e₁
negieren.

## Kandidaten für J (verbindlich)

- **J-Haupt:** die Vorzeichen-Automorphismen, die e₁ negieren **und** e₇ festhalten (verträglich mit SU(3) und dem
  Kaskaden-Ende span(1, e₇)): feste Linie (2,5,7) oder (3,4,7).
- J-Neben: alle 7 nicht-trivialen Vorzeichen-Automorphismen.

## Offenlegung (vor der Rechnung)

Strukturelle Erwartung: TM1-Lift und θ₁₃ = 0-Lift über demselben Fano-Bild unterscheiden sich um ein Element σ des
Vorzeichen-Kerns (k24). Die Vorzeichen-Automorphismen bilden eine abelsche Gruppe. Daher gilt
h_TM1 J h_TM1⁻¹ = σ (h_θ J h_θ⁻¹) σ⁻¹ = h_θ J h_θ⁻¹. Kriterien, die nur von der Konjugationswirkung auf J abhängen,
können **nicht** trennen. Das wird mitgeprüft, nicht vorausgesetzt.

## Kriterien (verbindlich)

- **K1 (Haupt):** h kommutiert mit J (Restsymmetrie verträglich mit dem Kompensator; C-Bild h-invariant).
- K2: Die erhaltene Spalte von h (eindeutiger Eigenvektor auf dem Triplett) ist Eigenvektor von J.
- K3: Die erhaltene Spalte liegt im J-geraden Teil (J = +1) des Tripletts.
- K4: Das Dreier-Element g₃ kommutiert mit J (Triole verträglich mit dem Kompensator) — Vorbedingung, berichtet.

Ausgewertet für alle vier Lifts von g₃ und alle Kandidaten J. TM1/θ₁₃ = 0 jeweils relativ zum gewählten g₃.

## Bewertung (verbindlich)

- K1 trennt zugunsten TM1 für J-Haupt: „Kompensator ist modellinterner Kandidat für die Auswahl“.
- K1 trennt nicht: kein Auswahlgrund aus dem Kompensator; K2, K3 nur als Hinweise.
- Ergebnis hängt vom Lift von g₃ oder von der Wahl unter J-Haupt ab: Konventionsfrage, kein Befund.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
