# Vorab-Notiz H136: Macht eine Rückwirkung über den HC-Winkel κ ≈ 1,2 zu einem selbststabilisierenden Punkt?

**Stand:** 2026-11-25, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (K-a steht vorab fest, K-c ist
überschlagen, K-b ist offen).
Anlass: Autor, 25.11.2026, 11:45 UTC: „ja, mach das und merge und pushe vorher“ auf den Vorschlag aus H135, die Rückwirkung über den HC-Winkel zu rechnen.
Skripte **k305** (Python numpy/sympy/scipy) und **k305b** (Wolfram Language, unabhängig). Qiskit nicht vorgesehen (keine Schaltung, keine Messung).
Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug). Kein Guard wird berührt.

## Vorwissen geprüft
- **k295** (#302): mit U(1) links und rechts sind A₁ = N(ψ₁) und B = N(χ) getrennt invariant. **k297** (#303): HC als Potential η(B − μ²A₁)², tan θ = μ = 0,3018,
  θ₀ = 16,79°. **k299** (#306): unter SU(2) links ist der Winkel θ Eichung; invariant ist nur das Stromverhältnis einer drehenden Lösung.
- **H133/k302** (#308): mit der fortgesetzten Eichwirkung sind nur A = A₁ + B und C invariant. **k303** (#309): κ* = 1,2039, Treffer κ = 1/cos 2θ₀ = 1,2004.
- **H135/k304** (#309): Tiefe des Vakuums bei fester Skala F = B·exp(−2A/B), monoton wachsend in κ; kein fester Punkt im Fluss.
- **k293/k294** (#298): Zusatzterme bevorzugen den Anhang nicht. Suche im Repo nach einer Schleifen-Rückwirkung auf den HC-Winkel (25.11.): keine Fundstelle.

## Aufbau
- Felder: ψ₁ (2 reell, A₁), χ (2 reell, B), b (4 reell, C = N(b)). Auf der HC-Richtung A₁ = v²cos²θ, B = v²sin²θ.
- **Stufe 1 (Eichlesart):** Invarianten vom Grad 2 und 4 in (ψ₁, χ) unter SU(2) links mal U(1) rechts. Gibt es eine, die von θ abhängt?
- **Stufe 2 (Modell U, nur U(1) links und rechts):** Der Anhang koppelt verschieden, V_c = (κ₁A₁ + κ₂B)·C, also κ_eff(θ) = κ₁cos²θ + κ₂sin²θ und
  m_S² = 2κ_eff·v². Setzung: Top koppelt nur an ψ₁, m_t(θ) = m_t·cos θ/cos θ₀. W und Z unabhängig von θ.
  Mit HC-Strafe η: Verschiebung von θ durch die Schleife des Anhangs in führender Ordnung.
- **Stufe 3 (Schleifen allein, η = 0):** Tiefe F(θ) = B(θ)·exp(−2A(θ)/B(θ)) wie in H135. Zwei Bedingungen, F stationär bei θ₀ und κ_eff(θ₀) = κ*,
  legen (κ₁, κ₂) fest. Dann zweite Ableitung von F nach θ (Maximum = stabil) und die Steigung dκ_eff/dθ bei θ₀.

## Hypothese H136
Über den HC-Winkel entsteht eine Rückwirkung, die κ = 1/cos 2θ ≈ 1,2 zu einem selbststabilisierenden Punkt macht.

## Entscheidungskriterien
- **K-a (Eichlesart):** Es gibt unter SU(2) links mal U(1) rechts eine Invariante bis Grad 4, die von θ abhängt: bestätigt. Sonst widerlegt (keine
  Rückwirkung über einen ruhenden Winkel möglich).
- **K-b (Modell U, Schleifen allein):** Es gibt (κ₁, κ₂), beide zwischen 0 und π, mit F stationär bei θ₀, κ_eff(θ₀) = κ* und F dort ein Maximum in θ:
  bestätigt (der Winkel kann sich selbst halten). Lösung nur als Minimum oder Sattel, oder außerhalb des Bereichs: widerlegt.
- **K-c (Regel):** Die Steigung dκ_eff/dθ der Lösung aus K-b bei θ₀ stimmt mit der Steigung der Regel, d(1/cos 2θ)/dθ = 2·sin 2θ₀/cos² 2θ₀, auf ±20 %
  überein: bestätigt. Sonst widerlegt.
- **Gesamturteil:** bestätigt, wenn K-b und K-c bestätigt sind. K-b bestätigt und K-c widerlegt: „trägt teilweise“ (der Winkel hält sich selbst, aber
  nicht nach der Regel). Sonst widerlegt.

## Vorab offengelegt (kein Teil der Vorhersage)
- Zu K-a: k302 hat für die fortgesetzte Eichwirkung nur A und C gefunden, k299 nennt θ Eichung. K-a ist damit vorab entschieden.
- Zu K-c, im Kopf: Wächst θ, sinkt die Top-Masse und B steigt. Damit F bei θ₀ stationär ist, muss κ_eff mit θ fallen (κ₂ < κ₁). Die Regel 1/cos 2θ steigt
  mit θ (Steigung etwa +1,6). Ich erwarte also das falsche Vorzeichen.
- Zu K-b weiß ich nicht, ob die stationäre Stelle ein Maximum ist und ob κ₁, κ₂ im Bereich liegen.
- Die erzwungene Gleichung κ_eff(θ₀) = κ* prüft den Zahlentreffer nicht; sie setzt ihn ein. Geprüft werden nur Stabilität und Steigung.

## Vorhersage
- K-a: **widerlegt** (nicht blind). K-b: **offen**, Vermutung widerlegt. K-c: **widerlegt** (falsches Vorzeichen).
- Gesamt: **widerlegt.**

## Grenzen (vorab)
Eine Schleife. Modell U verträgt sich nicht mit der geeichten SU(2) (deshalb Stufe 1). Die Top-Kopplung nur an ψ₁ ist eine Setzung; ohne sie hängt F nur
über κ_eff an θ und hat wegen H135 kein inneres Extremum. g, g′, y_t laufen nicht mit. Massen und v aus dem Gedächtnis wie in k300. θ₀ ist eingesetzt (OP1).
