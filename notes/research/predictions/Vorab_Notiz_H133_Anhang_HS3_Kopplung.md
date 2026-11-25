# Vorab-Notiz H133: Legt der Turm die Kopplung des HS(3)-Anhangs so fest, dass die fehlenden Bosonen herauskommen?

**Stand:** 2026-11-25, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 25.11.2026, 11:24 UTC: „mach das“ auf den Vorschlag aus k300, den Anhang von HS(3) anzukoppeln. Skripte **k302** (Python sympy/numpy/scipy)
und **k302b** (Wolfram Language, unabhängig). Qiskit nicht vorgesehen (keine Schaltung, keine Messung). Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug).
Kein Guard wird berührt.

## Vorwissen geprüft
- **k300** (#307): Schleifen-Skala m_s² = [Σ_Bosonen n·m⁴ − Σ_Fermionen n·m⁴]/(8π²v²). Mit W, Z und Top fehlt eine Bosonen-Summe von 8,52·10¹⁰ GeV⁴,
  das sind 1/2/4/8 reelle Felder bei 540/454/382/321 GeV. Eine Bedingung, keine Vorhersage.
- **k295** (#302): im Anhang ℂ → ℍ sind nur B, AB, B² zulässig. **H129/k296** (#302): eine Schleife, Fluss 16π²·dr/dt = −4λr(r − 2)², feste Punkte r = 0 und
  r = 2 (voller Norm-Punkt, dort ist der Anhang masselos).
- **k297** (#303): HC als Potential η(B − μ²A)², flache Richtung; quadratische Strafe ist Setzung. **k299** (#306): SU(2) links, U(1) rechts auf ℍ.
- **k253** (README des Ordners `hilbert_shift_felder_2026_11_24`): Der(𝕆) = g₂ (14), Stabilisator einer Einheit su(3) (8), Linksmultiplikationen erzeugen so(8).
- **k270/k271, r43** (`rueckwaerts/README.md`): im Turm trägt HS(3) die Farbe (SU(3), eine feste Einheit u), die schwache SU(2) sitzt auf ℍ.
- Suche unter `notes/research`, `wiki`, `analysis` nach „2HDM“, „zwei Dubletts“, „Landau-Pol“, „inert“ (25.11.): keine Fundstelle zu einem zweiten skalaren
  Vierer-Block oder zu einem Pol der Kopplungen.

## Aufbau
- ψ = a + b·ℓ ∈ 𝕆 mit a, b ∈ ℍ (Cayley–Dickson, Konvention im Skript festgehalten). A = N(a), C = N(b). Vakuum in der Vorstufe: a = v, b = 0.
- **Lesart S-a (Fortsetzung der Eichwirkung aus k299):** Linksmultiplikation mit den Einheiten i, j, k von ℍ und Rechtsmultiplikation mit i, beide als
  8×8-Matrizen auf 𝕆. Erzeugte Lie-Algebra, ihre Dimension, ihre invarianten Polynome vom Grad 2 und 4.
- **Lesart S-b (Symmetrie aus k253):** g₂ (Derivationen von 𝕆). **Lesart S-c:** su(3) als Stabilisator von u = i in g₂. Jeweils dieselbe Zählung.
- Je Lesart: Zahl der gemischten Terme (Portal-Kopplungen), Entartung der neuen Felder, nötige Masse aus n·m⁴ = 8,52·10¹⁰ GeV⁴, nötige Kopplung.
- **Fluss mit einer Schleife** (nur Skalare) für V = λ_A·A² + κ·A·C + λ_C·C² mit Blockgrößen (N, M) = (4, 4), (2, 6), (1, 7), aus 16π²·dV/dt = ½·Sp[(V″)²].
  Feste Verhältnisse und der Ort, an dem die Kopplungen 4π überschreiten, bei Start μ = v mit λ_A = 0 (skalenfrei), λ_C = 0 und dem nötigen κ.

## Hypothese H133
Der Turm legt die Kopplung des HS(3)-Anhangs an die Vorstufe so fest, dass die neuen Felder die fehlende Summe 8,52·10¹⁰ GeV⁴ liefern.

## Entscheidungskriterien
- **K-a (Form):** In Lesart S-a gibt es genau einen gemischten Term bis Grad 4, und die vier neuen Felder sind entartet: bestätigt. Zwei oder mehr gemischte
  Terme (Aufspaltung, mehrere freie Zahlen): widerlegt.
- **K-b (Wert):** Mindestens eine der vorab genannten Regeln legt κ ohne freie Zahl fest, und die Summe liegt innerhalb von ±20 % des Ziels: bestätigt.
  Regeln: R1 volle Norm (V hängt nur an A + C), R2 HC-Strafe η(C − μ²A)² mit μ = β_sym², R3 festes Verhältnis des Ein-Schleifen-Flusses.
  Legt keine Regel den Wert fest oder liegt jeder festgelegte Wert außerhalb: widerlegt.
- **K-c (Tragfähigkeit):** Ort des Pols im Fluss mit dem nötigen κ (Lesart S-a). Über 10¹⁶ GeV: bestätigt. Zwischen 10 TeV und 10¹⁶ GeV: „trägt teilweise“
  (nur als Beschreibung bis dorthin). Unter 10 TeV: widerlegt.
- **Gesamturteil:** bestätigt nur, wenn K-a und K-b bestätigt sind. K-a bestätigt und K-b widerlegt: „nicht bestätigt, Form festgelegt, Wert frei“.

## Vorab offengelegt (kein Teil der Vorhersage)
Beim Aufschreiben von Hand überlegt, ungeprüft:
- In 𝕆 ist p(a + bℓ) = pa + (bp)ℓ und (a + bℓ)q = aq + (b·q̄)ℓ. Auf b wirken also beide als Rechtsmultiplikation und vertauschen nicht. Die erzeugte Algebra
  sollte su(2) (auf a) ⊕ u(1) (auf a) ⊕ su(2) (auf b) sein, Dimension 7. Dann sind N(a) und N(b) die einzigen Invarianten: ein gemischter Term A·C, vier
  entartete Felder. Die Linksmultiplikation bildet auf 𝕆 keine SU(2) mehr (Nicht-Assoziativität).
- R1 gibt masselose neue Felder (Summe null), das ist aus H129 bekannt. R2 lässt η frei. Für R3 erwarte ich wie in H129 nur die Punkte κ = 0 und volle Norm.
- Nötige Kopplung in S-a: m² = 2κv², also κ ≈ 1,2. Das habe ich überschlagen. Den Pol habe ich nicht gerechnet; Schätzung im Kopf 10⁵ bis 10⁷ GeV.
- S-b sollte 7 entartete Felder geben (332 GeV), S-c 6 (345 GeV, ein farbiges Triplett). Ungeprüft.

## Vorhersage
- K-a: **bestätigt** (nicht blind, siehe oben).
- K-b: **widerlegt** (keine Regel legt den Wert fest; R3 ist vor der Rechnung offen).
- K-c: **trägt teilweise** (offen, Schätzung).
- Gesamt: **nicht bestätigt, Form festgelegt, Wert frei.**

## Grenzen (vorab)
Eine Schleife, im Fluss nur Skalare (ohne Eichfelder und Top). Massen und v aus dem Gedächtnis wie in k300. Start des Flusses bei μ = v ist eine
Vereinfachung. Welche der drei Lesarten der Turm meint, ist offen. Schranken aus Beschleuniger-Suchen werden nicht gerechnet.
