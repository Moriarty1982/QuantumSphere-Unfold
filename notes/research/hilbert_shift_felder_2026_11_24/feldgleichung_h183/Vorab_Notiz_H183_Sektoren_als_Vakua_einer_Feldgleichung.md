# Vorab-Notiz H183: Sind die Sektoren gleichzeitig stabile Lösungen einer einzigen Feldgleichung, und welche Vorzeichen erzwingt das?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026 („mergen und dann schau dir die feldgleichung an“), nach H182. Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung) mit den Eingaben aus Strang 3. Vergeben: H183, k386 (geprüft: frei).

## Vorwissen geprüft
- k290 (`../feldgleichung/README.md`): rekursive Lagrangedichte L_{n+1} = L_n + Δ_n; auf HS(3) kinetischer Term, Potential, K₁ bis K₃; Vorzeichen frei.
  Dort hat das Potential nur die Invarianten N(ψ) und Re ψ (ohne ausgezeichnete Einheit U).
- k291 bis k305, H129, H132, H133, H135, H136 (`../feldgleichung/`): Skala nicht aus dem Ansatz; κ für den Anhang frei; mehrere Mechanismen widerlegt.
- H167 bis H171 (`../delta_h167/` bis `../delta_h171/`): Skala als Setzung; δ-Terme; nicht Gegenstand hier.
- H178, k378, H182 (`../farbe_h178/`, `../farbanteil_k378/`, `../ladung_h182/`): Mit U = e₇ und J hat das Potential mehr Invarianten; alle bis Grad 4 sind
  gezählt (7 + 33 auf ℂ ⊗ 𝕆). Dort wurde je Sektor ein Feld mit vorgegebener Art (farblos, Ladung ⅓, Ladung ⅔) betrachtet und nur der Winkel θ variiert.
  **Nicht geprüft** ist dort, ob diese Felder stationäre und stabile Lösungen in **allen** Feldrichtungen sind, also Lösungen einer Feldgleichung.
- H178: „κ < 0 (Leptonen im Minimum) ist das offene Vorzeichen 2a − b aus H149, als Konsistenzbedingung benutzt, nicht hergeleitet.“
- Autor, 25.11.2026: Offene Vorzeichen sollen aus der finalen Feldgleichung folgen, nicht gesetzt werden.
- Nicht gefunden: eine Stabilitätsrechnung (zweite Variation) für die Sektorfelder im vollen Feldraum.

## Suchrichtung (rückwärts)
Ziel: eine Feldgleichung, deren statische homogene Lösungen die gemessenen Konfigurationen sind. Notwendige Bedingungen: (1) jede Konfiguration ist
stationär in allen 16 Feldrichtungen; (2) die zweite Variation ist dort nicht negativ, Nullrichtungen nur entlang der Symmetrie. Diese Bedingungen sind
linear in den Koeffizienten des Potentials und werden direkt gelöst, statt Potentiale zu raten.

## Setzungen dieser Notiz
- Ein Feld Ψ ∈ ℂ ⊗ 𝕆, L = ½⟨∂Ψ, ∂Ψ⟩ − V(Ψ), mit fester Norm Ψ†Ψ = 1 (**Skala als Setzung**, Autor 26.11.2026). Statische homogene Lösungen sind die
  stationären Punkte von V auf der Kugel; kleine Schwingungen haben die Frequenzquadrate der zweiten Variation auf dem Tangentialraum.
- V: allgemeines reelles Polynom bis Grad 4, invariant unter SU(3)_c, Oktonion-Konjugation und J (komplex-linear), wie in H182 („volle Fassung“,
  40 Koeffizienten). „Phasenfassung“: zusätzlich invariant unter der gemeinsamen Phase von ℂ.
- Konfigurationen: L = (1 + U)/√2 (θ = 45°); D = cos θ_d·1 + sin θ_d·n_{1/3}; Up = cos θ_u·1 + sin θ_u·n_{2/3}; θ_d = 48,114°, θ_u = 52,207° (M_Z).
- Ableitungen und K-Terme (k290) tragen zu statischen homogenen Lösungen nicht bei und bleiben außen vor.

## Hypothesen und Kriterien
- **H183a (Ausgang offen):** Es gibt Koeffizienten, für die L, D und Up zugleich stationär und stabil sind (kleinster Eigenwert der zweiten Variation
  außerhalb der Symmetrierichtungen > 0). Kriterium: konvexes Programm (größter erreichbarer kleinster Eigenwert bei normierten Koeffizienten). Volle
  Fassung lösbar: **bestätigt** (die Sektoren können Lösungen einer Feldgleichung sein). Nicht lösbar: **widerlegt** (ein Feld reicht nicht; die
  Sektoren brauchen getrennte Felder). Die Phasenfassung wird getrennt berichtet.
- **H183b (Ausgang offen):** Im lösbaren Bereich sind Vorzeichen erzwungen. Geprüft werden vorab benannte Größen: (1) der Koeffizient des Terms, der in
  der farblosen Ebene 45° gegen 0° trennt (in H178: κ); (2) der ladungsungerade Koeffizient im Farbblock (in H182: C); (3) die Krümmung des
  Leptonzustands in Richtung Farbe. Kriterium je Größe: Maximum und Minimum über den lösbaren Bereich haben dasselbe Vorzeichen: **erzwungen**; sonst
  **frei**. Kein Urteil über die Hypothese als Ganzes; die Liste wird berichtet.
- **H183c (Zählung):** Zahl der Koeffizienten, die nach den Stationaritätsbedingungen frei bleiben. Bericht, kein Kriterium.
- **Bericht:** die Frequenzquadrate der kleinen Schwingungen um L, D, Up an einem Punkt im Inneren des lösbaren Bereichs (nur als Beispiel, nicht als
  Vorhersage); Zahl der Nullrichtungen gegen die Erwartung aus der Symmetrie (D, Up: SU(3) → SU(2), fünf; L: keine).

## Werkzeugwahl
Python (numpy, scipy; cvxpy falls vorhanden, sonst eigenes Verfahren für das konvexe Programm): Invarianten wie in k385, Gradient und zweite Variation
exakt aus den Polynomen. Wolfram Language als unabhängige exakte Kontrolle an einer Unterfamilie mit expliziten Invarianten. Qiskit nicht geeignet
(keine Schaltung). Ausgaben werden neben den Skripten abgelegt.

## Grenzen (vorab)
Grad ≤ 4, feste Norm, nur statische homogene Lösungen, Winkel bei M_Z, δ und die Generationenstruktur nicht behandelt. Lokale Stabilität, nicht globale.
Kein Vorzeichen wird gesetzt. OP3 und OP4 bleiben offen.
