# Vorab-Notiz H132: Bleibt auf der HC-Richtung ein masseloses Eichfeld, und hängen die Massenverhältnisse nur an β_sym?

**Stand:** 2026-11-25, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 25.11.2026, 11:06 UTC: „mach das“ auf den Vorschlag aus k297, die Eichfelder auf der HC-Richtung dazuzunehmen. Skripte **k298** (Python sympy)
und **k298b** (Wolfram Language, unabhängig). Qiskit nicht vorgesehen (keine Schaltung, keine Messung). Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug).
Kein Guard wird berührt.

## Vorwissen geprüft
- **k291** (#296), Punkt 5 und 6: geeichte U(1) bei fester Norm gibt m_A = e·f; auf ℍ mit SU(2) links und U(1) rechts und Vakuum ψ = f die Massenquadrate
  g²f²/4 (zweimal), (g² + g′²)f²/4 und 0, masselos ist g′W₃ + gB.
- **k292** (#296): Linksladung ω(a² + b²), Rechtsladung ω(a² − b²); Winkel auf der Hopf-Sphäre cos ϑ = (a² − b²)/(a² + b²).
- **k295** (#302), **H129/k296** (#302), **k297** (#303): V = η(B − μ²A)², flache Richtung B = μ²A, zwei masselose Phasen, Größenmode, Formmode m_H² = 8ημ²f².
- Suche im Repo nach einer Eichung auf einer Richtung mit beiden Anteilen (25.11.): keine Fundstelle.

## Aufbau
- ψ = ψ₁ + χ·j, Vakuum auf der HC-Richtung: ψ₀ = f(cos θ + sin θ·j), tan θ = μ = β_sym² (eingesetzt, OP1). A = f²cos²θ, B = f²sin²θ.
- **Stufe A (Eichung der Symmetrie des HC-Potentials):** U(1) links (ψ → e^{iα}ψ, Feld L, Kopplung g_L) und U(1) rechts (ψ → ψe^{iβ}, Feld R, Kopplung g_R).
  Massenmatrix aus ½·N(D ψ₀) mit Dψ = ∂ψ + g_L·L·iψ − g_R·R·ψi.
- **Stufe B (zum Vergleich, k291 Punkt 6):** SU(2) links (g) und U(1) rechts (g′) auf demselben Vakuum; dazu die Änderung von V unter einer
  infinitesimalen SU(2)-Linksdrehung, die nicht in der U(1) liegt.
- **Stufe C (ohne Kriterium):** Schleifen-Skala mit Eichfeldern nach Gildener–Weinberg, Summe m_H⁴ + 3(m₊⁴ + m₋⁴), Masse der Größenmode.

## Hypothese H132
Mit den Eichfeldern der Symmetrie des HC-Potentials bleibt auf der HC-Richtung ein masseloses Eichfeld (Licht), und das Verhältnis der Eichfeldmassen
ist eine reine Funktion von β_sym.

## Entscheidungskriterien
- **K-a (masseloses Feld):** Determinante der Massenmatrix aus Stufe A auf der HC-Richtung. Null: bestätigt. Ungleich null für μ = β_sym²: widerlegt.
- **K-b (Verhältnis):** m₋²/m₊² aus Stufe A. Hängt es nicht von g_L/g_R ab: bestätigt. Hängt es davon ab, ist aber für g_L = g_R eine reine Funktion von μ:
  „trägt teilweise“. Sonst widerlegt.
- **Gesamturteil:** bestätigt nur, wenn K-a und K-b bestätigt sind.

## Vorab offengelegt (kein Teil der Vorhersage)
Überschlag beim Aufschreiben (im Kopf, ungeprüft):
- Beide Anteile tragen beide Ladungen (ψ₁: +1 links, +1 rechts; χ: +1 links, −1 rechts). Die Massenmatrix in (L, R) sollte
  [[g_L²f², g_Lg_R(A − B)], [g_Lg_R(A − B), g_R²f²]] sein, mit Determinante 4g_L²g_R²·A·B. Sie ist null nur für A = 0 oder B = 0.
- Für g_L = g_R = g erwarte ich m_±² = g²f²(1 ± cos 2θ), also m₋²/m₊² = B/A = μ².
- Stufe B: SU(2) links wirkt transitiv auf der Sphäre, das Spektrum sollte von θ nicht abhängen (wie k291); das HC-Potential ist aber nicht SU(2)-invariant.

## Vorhersage
- K-a: **widerlegt** (kein masseloses Eichfeld, sobald beide Anteile ungleich null sind).
- K-b: **trägt teilweise** (für gleiche Kopplungen m₋/m₊ = μ = β_sym² = 0,3018; sonst hängt es am Verhältnis der Kopplungen).
- Gesamt: **H132 widerlegt**. Offen vor der Rechnung: ob der Überschlag stimmt (Vorzeichen der Ladungen, Faktoren), die allgemeine Formel für das Verhältnis,
  die Masse des leichten Felds für kleine μ, die Zahlen aus Stufe C.

## Grenzen (vorab)
Klassische Massenmatrix, eine Schleife nur in Stufe C, nur ℂ → ℍ, ohne Fermionen. Die quadratische Form des HC-Potentials ist eine Setzung (k297).
β_sym ist eingesetzt (OP1). Welche Kombination „das Licht“ ist, ist eine Lesart.
