# Fundstellen: Was der Companion an Dynamik für die Λ-Auslesung (Ω_Λ : Ω_M = (1 − β²) : β²) enthält

**6. November 2026. Status: Quellensuche, keine Rechnung.** Autor (6.11.): „Was ist mit der fehlenden Dynamik? … such mal weiter.“ Durchsucht wurde der Monolith (Kaskade, Markov, Hubble, Friedmann, Skalenfaktor) sowie die Runden v4.8.0-r03, r17 und v4.9.0-r27–r31.

## Gefunden
1. **v4.9.0-r31 (Markov-Kaskade).** Die einzige Stelle, an der das Verhältnis aus einer Dynamik kommt statt gesetzt zu werden.
   - Geschlossen endet die Kette im Photon (S²).
   - Mit Rückweg S² → S⁸ (Rate r) ist die stationäre Verteilung eindeutig: (p₂, p₄, p₈) = (1, β²r, r)/(1 + r + β²r).
   - Die Flussanteile aus S⁸ sind β² (nach S⁴) und 1 − β² (nach S²), **für jede Rate**.
   - Als Rückweg schlägt r29 die Paarerzeugung aus dem Vakuum vor.
   - **Es fehlt:** eine physikalische Zeit für einen Schritt, die Rate r und die Brücke von Flussanteilen zu Energiedichten in der Friedmann-Gleichung.
2. **v4.8.0-r17 (Epoche).** Eine feste Verzweigung kann nicht zu allen Epochen den kosmologischen Anteilen entsprechen. Notierte Auswege:
   - (a) nur heute; das ist seit 6.11. gewählt;
   - (b) β läuft rückwärts;
   - (c) eine andere, zeitabhängige Funktion der Kaskadenwahrscheinlichkeiten.

   Für (c) heißt es dort: „braucht eine zeitabhängige Brücke, die die Quelle nicht liefert“.
3. **Kern, frühe Fassung (Z. ~6928):** Der Skalenfaktor wird mit der Eigenzeit identifiziert, H mit der „Aktivierungsrate der Riemann-Nullstellen“, n_H ~ 10⁶². Das hing an der Riemann-Arbeit und ist seit v4.8.0-r04 keine Beweisquelle mehr. **Die einzige Verbindung des Kerns zur kosmischen Zeit ist damit weggefallen.**
4. **`prop:inflow-cascade`:** Die Zufluss-Lesart (Information fließt S⁸ → S², „Widerstand als Masse“ = Anteil β² durch S⁴) wird ausdrücklich als „intuitive Umformulierung“ ohne neue Mathematik geführt.
5. **v4.8.0-r03 F11:** γ_L ist das Verhältnis der korrigierten zur überholten Bestimmung desselben LQG-Parameters. Der Companion liest es als Lorentzfaktor; eine Herleitung aus der Struktur gibt es nicht.

## Folge
- Die Dynamik, die die Λ-Auslesung bräuchte, wäre eine **zeitliche Brücke** zwischen der Kaskade (diskrete Schritte, stationäre Flüsse) und der kosmischen Expansion. Der Companion hatte sie nur über die Riemann-Nullstellen, und diese Verbindung ist zurückgezogen.
- Der nächstliegende Kandidat ist die r31-Kaskade mit einer Regel, die Schritte an die kosmische Zeit koppelt und Flüsse an Energiedichten. Dafür müsste der Autor zwei Dinge festlegen, bevor gerechnet wird:
  - **Zeit:** Was ist ein Kaskadenschritt in kosmischer Zeit, z. B. 1/H oder eine feste Zeit?
  - **Dichte:** Wie wird ein Fluss zu einer Energiedichte, und wie verdünnt sich, was in S⁴ bzw. S² landet?

  Danach ergäbe sich eine Funktion Ω_M(z), die mehr wäre als die Zahl in H96.
- Ohne diese Brücke bleibt die Λ-Auslesung eine Aussage über eine Epoche (H96).
