# Vorab-Notiz H5: Mischwinkel der erhaltenen Spalte aus der Hopf-Struktur

Festgelegt am 2026-10-20, **vor** dem Datenvergleich. Baut auf K16 (H4) und K16.4 auf.

## Zuordnung (M)

Die erhaltene Spalte w = cos a · c₂ − sin a · e^{ib} · c₁ mit c₁ = (2,−1,−1)/√6, c₂ = (1,1,1)/√3 ist ein Punkt
(cos a, sin a e^{ib}) ∈ S³ ⊂ ℂ². Die Hopf-Abbildung S³ → S² = ℂP¹ bildet ihn auf den Punkt mit Polwinkel
θ = 2a und Azimut b ab. TM2 ist der Nordpol (θ = 0), TM1 der Südpol (θ = 180°), die 1:1-Überlagerung der
Äquator (Clifford-Torus, θ = 90°).

## Hypothese (V)

**H5:** Der Polwinkel der erhaltenen Spalte ist ein Hopf-Winkel des Companion (Kernkarte Abschnitt 3):
θ ∈ {θ_H = 66,64° (Frame-Offset, aus β_sym), θ_sym = 70,53° (symmetrischer ℤ/3-Fall, β = 1/√3)}.
Der Äquator θ = 90° ist durch K16.4 bereits ausgeschlossen und wird nicht erneut gezählt. Ebenso werden die
supplementären Winkel 180° − θ (Spiegelung Nord/Süd) mitgeprüft, da die Zuordnung der Pole nicht festliegt.

Varianten für den Azimut b:
- **(i) kanonisch:** b ∈ {0°, 90°, 180°, 270°}.
- **(ii) frei:** b wird angepasst; dann ist θ₁₂ Eingabe und nur δ_CP bleibt Test.

Die erhaltene Spalte darf ν₁ oder ν₂ sein. Variante (i) umfasst damit 4 Polwinkel × 4 Azimute × 2 Zuordnungen
= 32 Kombinationen.

## Offenlegung vor der Festlegung

Bekannt vor dieser Notiz (K16.4): Mit b = 0 verlangen die Daten a = 90,6° (θ = 181,2°) oder a = 2,0°
(θ = 4,0°), also fast genau die Pole. Bei b = 0 liegt keiner der Kandidaten dort. Kopfrechnung: Für a = 33,3° und
freies b überstreicht |U_e|² von w den Bereich 0,001–0,866, enthält also die Zielwerte; Variante (ii) wird
daher θ₁₂ sicher treffen. Nicht gerechnet: Fits, δ_CP-Vorhersagen, χ²-Werte.

## Daten (verbindlich)

NuFIT 6.0 (arXiv:2410.05380), IC24 + SK, normale Ordnung, wie in H4 (asymmetrische Fehler, Gauß-Näherung).

## Verfahren (verbindlich)

- Mischungsmatrix: Spalte w (als ν₁ oder ν₂); die beiden anderen Spalten sind eine unitäre Drehung (Winkel ϑ,
  Phase φ) im Orthogonalraum von w, aufgespannt von der Restkombination in span(c₁, c₂) und c₃ = (0,1,−1)/√2.
  Spalten nach ν₁, ν₂, ν₃ ordnen; Winkel und δ_CP über |U_e3|², |U_e2|², |U_μ3|² und die Jarlskog-Invariante.
- Anpassung von ϑ, φ (und in Variante (ii) von b); χ² über sin²θ₁₂, sin²θ₁₃, sin²θ₂₃, δ_CP.
- Freiheitsgrade: Variante (i) 2, Variante (ii) 1.

## Entscheidungskriterium (verbindlich)

- Variante (i): Eine Kombination gilt als verträglich bei χ²_min < 5,99 (2 FG, 95 %). Wegen 32 Versuchen zählt
  ein Treffer als Beleg erst bei χ²_min < 0,1 · 5,99 im Sinne eines strengen Versuchsfaktors; sonst nur als
  verträglich vermerkt. Keine Kombination verträglich: Variante (i) **widerlegt**.
- Variante (ii): verträglich bei χ²_min < 3,84 (1 FG). Die δ_CP-Vorhersage wird festgeschrieben.
- Vergleich mit TM1 (χ² = 4,43 bei 2 FG) wird angegeben, aber nicht als Entscheidung gewertet.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
