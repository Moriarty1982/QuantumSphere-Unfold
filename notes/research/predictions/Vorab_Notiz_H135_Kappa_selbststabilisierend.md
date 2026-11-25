# Vorab-Notiz H135: Ist die Kopplung κ ≈ 1,2 ein selbststabilisierender Punkt?

**Stand:** 2026-11-25, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (K-a steht vorab fest, K-b ist offen).
Anlass: Autor, 25.11.2026, 11:39 UTC, zum Zahlentreffer aus k303: „0.3% daneben sind nicht so schlecht […] die frage ist doch eher, ob das system bei dem
evtl. selbststabilisierend ist, dann müsste es quasi bei unendlichen möglichkeiten halt nur oft genug auftauchen um das system zu starten“.
Skripte **k304** (Python numpy/sympy/scipy) und **k304b** (Wolfram Language, unabhängig). Qiskit nicht vorgesehen (keine Schaltung, keine Messung).
Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug). Kein Guard wird berührt.

## Vorwissen geprüft
- **k300** (#307): m_s² = [Σ_B n·m⁴ − Σ_F n·m⁴]/(8π²v²). **H133/k302** (#308): ein Term κ·A·C, vier entartete Felder, m_S² = 2κv²; Fluss
  16π²·dκ/dt = 16κ(κ + 3λ_A + 3λ_C); Pol bei 1,4·10⁴ GeV. **k303** (#309, offen): κ* = 1,2039; kein fester Punkt von κ mit Eichfeldern und Top;
  Zahlentreffer κ = (γ_L + 1/γ_L)/2 = 1,2004; unter κ = 0,416 kein Minimum; Unitaritätsgrenze κ = π.
- **H129/k296** (#302): skalenfreier Fall, Schleifen erzeugen die Skala; **k297** (#303): Größenmode auf der flachen Richtung.
- Suche unter `notes/research`, `wiki`, `analysis` nach „selbststabilisierend“, „Attraktor“ im Zusammenhang mit einer Kopplung (25.11.): keine Fundstelle zu κ.

## Lesarten von „selbststabilisierend“ (vorab festgelegt)
- **L1 (Fluss):** κ ≈ 1,2 ist ein anziehender fester Punkt des Flusses der Kopplungen.
- **L2 (Vakuumtiefe):** Wäre κ selbst beweglich, liefe es dorthin, wo das Vakuum am tiefsten ist. Skalenfreies Ein-Schleifen-Potential
  V(φ) = φ⁴[A + B·ln(φ²/Λ²)] mit Massen m_i = c_i·φ: c_W² = g²/4, c_Z² = (g² + g′²)/4, c_t² = y_t²/2, c_S² = 2κ.
  B = (1/64π²)[Σ_B n·c⁴ − Σ_F n·c⁴], A = (1/64π²)[Σ n·c⁴(ln c² − k)] mit k = 3/2 (Skalare, Fermionen, mit Vorzeichen) und 5/6 (Vektoren).
  Minimum bei ln(v²/Λ²) = −1/2 − A/B, Tiefe V_min = −(B/2)·Λ⁴·exp(−1 − 2A/B). Bei fester Skala Λ ist die Tiefe F(κ) = B·exp(−2A/B) bis auf einen Faktor.
- **L3 (Häufigkeit, ohne Kriterium):** Welcher Anteil der κ zwischen 0 und der Unitaritätsgrenze π gibt überhaupt ein Vakuum, und welche m_h entstehen dabei?

## Hypothese H135
Die Kopplung κ ≈ 1,2 ist ein selbststabilisierender Punkt des Systems.

## Entscheidungskriterien
Fenster wie in H133: κ zwischen 1,077 und 1,319.
- **K-a (L1):** Es gibt einen festen Punkt mit κ im Fenster, der zu kleinen Skalen hin anzieht: bestätigt. Sonst widerlegt.
- **K-b (L2):** F(κ) hat für κ > 0,416 ein lokales Maximum im Fenster: bestätigt. Ein lokales Maximum außerhalb des Fensters: „trägt teilweise“
  (selbststabilisierend, aber bei einem anderen Wert; dann mit dem zugehörigen m_h angeben). Kein inneres Maximum (monoton): widerlegt.
- **Gesamturteil:** bestätigt, wenn K-a oder K-b bestätigt ist. „Trägt teilweise“, wenn K-b teilweise trägt. Sonst widerlegt.

## Vorab offengelegt (kein Teil der Vorhersage)
- Zu K-a: Der Ein-Schleifen-Fluss nur mit Skalaren ist homogen vom Grad 2 in den Kopplungen. Dann können nur Verhältnisse fest sein, kein Wert ungleich
  null. Mit Eichfeldern und Top hat k303 keinen festen Punkt mit κ > 0 gefunden. K-a ist damit vor der Rechnung entschieden; gerechnet wird nur noch,
  wohin κ = 1,2 tatsächlich läuft.
- Zu K-b, im Kopf überschlagen: Für großes κ wird F konstant (B ≈ κ²/4π², A ≈ B(ln 2κ − 3/2), F → e³/(16π²)). Bei κ → 0,416 geht B gegen null und A
  bleibt positiv, also F → 0. Ob es dazwischen ein Maximum gibt, weiß ich nicht.
- Zu L3: Ein Vakuum gibt es für alle κ zwischen 0,416 und π, also für etwa 87 % bei gleichverteiltem κ.

## Vorhersage
- K-a: **widerlegt** (nicht blind).
- K-b: **widerlegt** (Vermutung: F wächst monoton; offen).
- Gesamt: **widerlegt.** Offen vor der Rechnung: der Verlauf von F(κ).

## Grenzen (vorab)
Eine Schleife. In L2 werden g, g′, y_t zwischen Λ und v nicht mitgeführt. Der Vergleich der Vakuumtiefe bei fester Skala Λ ist eine Lesart; bei festem v
ist die Tiefe −m_s²v²/16 und fällt monoton mit κ. Ob κ im Turm überhaupt beweglich ist, ist nicht gezeigt. Massen und v aus dem Gedächtnis wie in k300.
