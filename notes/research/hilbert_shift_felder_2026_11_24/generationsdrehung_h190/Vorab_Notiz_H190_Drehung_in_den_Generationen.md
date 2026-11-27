# Vorab-Notiz H190: Gibt ein Vakuum, das sich in den Generationen dreht, den Farbschwingungen die Quarkmassen?

**Stand:** 27.11.2026, vor der Rechnung. Anlass: Autor, 27.11.2026, Entscheidungskarte nach H189: „Drehung in den Generationen“. Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H190, k393 (geprüft: frei).

## Vorwissen geprüft
- H128 (`../kollaps_h128/`): Der(H₃) enthält g₂ ⊕ su(3); der Stabilisator von U in F₄ ist SU(3)_Farbe × SU(3), die zweite SU(3) wirkt auf die drei
  Plätze (Generationen) und vertauscht mit der Farbe.
- H184 bis H187: Frequenzquadrate der Farbschwingungen je Paar (i, j) aus dem Potential, Funktionsmenge R (neun Funktionen), Koeffizienten frei.
- H189 (`../bewegtes_vakuum_h189/`): Die Drehung mit u = i verschiebt alle Frequenzen gleich; K₁ bis K₄ ändern die Ruhefrequenzen nie. Dort als
  nicht gerechnet vermerkt: Drehungen in den Generationen.
- k253: Grundbahn exp(uωt)ψ₀; hier tritt an die Stelle von u ein Erzeuger der Symmetrie, der das Vakuum bewegt.
- Nicht gefunden: Schwingungen um ein in den Generationen drehendes Vakuum.

## Suchrichtung (rückwärts)
Ziel: drei stark verschiedene Frequenzen je Ladung. Notwendig: ein Mechanismus, der die Paare verschieden behandelt und eine kleine Frequenz
erzeugen kann, ohne dass das Potential sie schon enthält. Eine Drehung in der Ebene zweier Generationen koppelt zwei der drei Farbschwingungen
gyroskopisch; eine der gekoppelten Frequenzen geht gegen null, wenn die Drehrate an die Krümmung heranreicht. Das wird zuerst hergeleitet
(H190a), dann gegen die Daten geprüft (H190b, c).

## Setzungen dieser Notiz
- Feld, Vakuumwert W₀ (reelle Zirkulante, K = ⅔, δ = 2/9, Eingabe), Farbe, Ladung wie H185 bis H189.
- **Bewegung:** W(t) = exp(ωt·D_T)W₀ mit D_T(W) = TW − WT, T antihermitesch, spurfrei, Einträge in ℂ_U, in der Eigenbasis von W₀ die Drehung in
  der Ebene der Eigenrichtungen p, q (drei Ebenen). Vorausgesetzt ist ein Potential, das unter der SU(3) der Plätze invariant ist (sonst ist
  die Drehung keine Lösung); Existenz und Stabilität des drehenden Vakuums werden nicht geprüft.
- Krümmungen der drei Farbschwingungen: h = s·A·f mit f ∈ R (neun Funktionen), s = ±1, A > 0 je Sektor frei. Drehrate ω frei. Damit je Sektor
  ein freier Parameter w = ω²/A für zwei Massenverhältnisse.
- Lesarten Ω² ↔ √m, m, m² wie H187. Die drei Frequenzquadrate werden der Größe nach den Generationen zugeordnet (die Drehung mischt die Paare,
  eine Zuordnung A/B gibt es nicht mehr). Daten bei M_Z aus k376.

## Hypothesen und Kriterien
- **H190a (nicht blind, vor der Notiz hergeleitet):** D_T ist eine Derivation von H₃(𝕆), vertauscht mit Farbe und Ladung, lässt die
  Farbschwingung zum Paar (p, q) fest und dreht die zwei anderen ineinander (D_T² = −1 darauf). Die Frequenzquadrate sind dann h_c (ungekoppelt) und
  Ω²_± = ½(h_a + h_b) + ω² ± √(¼(h_a − h_b)² + 2ω²(h_a + h_b)), mit Ω²_+·Ω²_− = (h_a − ω²)(h_b − ω²), für beide Ladungen gleich.
  Kriterium: numerisch im vollen Modell bestätigt (Abweichung < 10⁻⁸): **bestätigt**; sonst **widerlegt** (dann wird mit der numerisch gefundenen
  Kopplung weitergerechnet und das berichtet).
- **H190b (Ausgang offen):** Je Sektor gibt es f ∈ R, Vorzeichen s, Ebene (p, q) und w ≥ 0 mit reellen positiven Frequenzquadraten, sodass beide
  Verhältnisse X₁/X₃, X₂/X₃ innerhalb von 3σ liegen, für beide Sektoren bei derselben Lesart. Zufallskontrolle mit 2000 erfundenen Datensätzen
  wie H187. Kriterium: Treffer und Zufallsquote < 5 %: **bestätigt** (als Kandidat für einen eigenen Vorab-Test); Treffer bei Quote ≥ 5 %:
  **ohne Urteil**; kein Treffer: **widerlegt**.
- **H190c (Ausgang offen, schärfer):** dieselbe Funktion f, dasselbe Vorzeichen, dieselbe Ebene und dieselbe Lesart für Up und Down; nur w je
  Sektor frei (zwei Vorhersagen). Kriterium wie H190b.
- **Bericht:** bester Abstand je Sektor und Lesart, Zahl der Vergleiche, Zufallsquoten, bei Treffern w und der Abstand zur Schwelle w = h.

## Werkzeugwahl
Python (numpy, scipy): D_T im vollen Modell ℂ ⊗ H₃(𝕆), Eigenwertproblem zweiter Ordnung, Suche über w auf einem dichten Raster (auch dicht an
den Schwellen w = h_a, h_b), bester Abstand mit Nachverfeinerung. Wolfram Language: Formel für Ω²_± und das Produkt exakt. Qiskit nicht geeignet.

## Grenzen (vorab)
Nur Drehungen in einer Eigenebene mit fester Rate; allgemeine T (Mischungen der Ebenen) und zwei Drehraten nicht gerechnet. Kein Nachweis, dass
das drehende Vakuum Lösung der Feldgleichung ist. K₁ bis K₄ ändern die Ruhefrequenzen nicht (H189a) und werden nicht mitgeführt. Massen bei M_Z
ohne Laufen. Kein Vorzeichen gesetzt (s wird durchprobiert). OP3, OP4 bleiben offen.
