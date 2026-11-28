# Vorab H235 (k450): Bricht eine Casimir-Verdrehungsenergie mit Sektorgewichten den Sektortausch und legt φ = x fest?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Erkundung k449 (inneres und äußeres Feld, Casimir-Spalt) und Marcs Wahl
„Ja, Verdrehungs-Casimir“ (Karte, „weiter“ 15:45). Der φ-Strang ruht formal (Marc 15:41). Dieser Test ist der eine Zusatzversuch, den Marc mit der
k449-Karte freigegeben hat.

## Vorwissen geprüft
- **H225 (k439):** Das Baum-Modell ist V_Im = −cos2(δ−π/4−φ) + q cos3δ, V_Re = cos2(δ−φ) + q cos3δ mit q = −0,0852. Der Sektortausch
  V_Re(−δ; π/4−φ) = V_Im(δ; φ) ist exakt. Jedes symmetrische Potential legt φ auf π/8 oder 7π/24. Ungleiche Gewichte w in führender Ordnung
  reichen nicht (φ* bleibt über π/12).
- **H226 (k440):** Ein Konjugationsterm nur im Im-Sektor gibt ein lokales Minimum bei x, aber x_ν liegt 212σ daneben. Dort hing der Zusatzterm
  von δ ab und verschob die Versätze.
- **H232 (k446):** Mit symmetrischem P gilt an jedem stationären φ: φ = Mittelwert der Sektor-Versätze. x ist nur lokal stationär.
- **H213/H214:** Der gemeinsame Versatz ist verträglich: x_ν − x liegt bei 1,78σ.
- **k449:** Verdrehungsenergie E(α) ∝ ∓S(α), S(α) = Σcos(nα)/n⁴ = π⁴/90 − π²α²/12 + πα³/12 − α⁴/48. Bei Fermionen (Vorzeichen +) liegt das
  Minimum bei α = π. Die Zählgewichte sind die Zahl der reellen Freiheitsgrade.
- Zurückgestellte Ideen I1–I6: Keine trifft diesen Ansatz direkt.

## Modell (gesetzt)
E(φ; κ) = e_Im(φ) + e_Re(φ) + κ·[w_I·S(α_I) + w_R·S(α_R)]
- e_s(φ) ist das Minimum des Baum-Potentials über δ (H225, q = −0,0852, r = 0).
- Die Verdrehungswinkel sind α_R = 2φ und α_I = π/2 − 2φ. Der Faktor 2 kommt von cos2. Die Zuordnung ist so gewählt, dass der Sektortausch
  φ ↔ π/4−φ die beiden Winkel genau vertauscht. Bei gleichen Gewichten bleibt der Tausch also erhalten.
- **Gewichte (Hauptfall):** w_I = 2 für den geladenen Sektor (c = 1, komplexes Feld, Dirac), w_R = 1 für den neutralen Sektor (c = 0, reelles Feld,
  Majorana-Lesart). Das sind Zählzahlen, keine angepassten Werte.
- **Vorzeichen:** Leptonen sind Fermionen, daher steht +κ·S mit κ > 0.
- κ ist die einzige freie Größe, die Gesamtstärke der Schleife relativ zum Baum.

## Satz vor der Rechnung (nicht blind)
Der Zusatzterm hängt nur von φ ab, nicht von δ. Die Versätze o_Im(φ) und o_Re(φ) sind deshalb reine Baumfunktionen.
- Wer verlangt, dass o_Im(φ*) = x, legt damit φ* fest, unabhängig von κ, Gewichten und Vorzeichen.
- Daraus folgt x_ν,pred = o_Re(φ*) für jeden Term, der nur von φ abhängt.
- Weil H213 schon zeigte, dass der gemeinsame Versatz bis auf 1,78σ verträglich ist, ist ein Ausgang nahe −1,8σ zu erwarten. Teil A ist damit nur
  teilweise blind.

## Kriterien
- **A (teilweise blind):** x_ν,pred = o_Re(φ_x) mit o_Im(φ_x) = x. Bestanden, wenn |x_ν,pred − 0,04336| ≤ 2·0,00213.
- **B (blind):** Es gibt ein κ* > 0 (Fermionen-Vorzeichen), bei dem φ_x ein stationärer Punkt von E ist. Dieses κ* wird aus dE/dφ = 0 bei φ_x bestimmt.
  - **B1:** κ* > 0, und φ_x ist dort ein lokales Minimum.
  - **B2:** Zusätzlich ist φ_x das globale Minimum von E auf [0, 2π/3).
- **Urteil:**
  - **trägt:** A und B2.
  - **trägt teilweise:** A und B1, aber nicht B2.
  - **widerlegt:** A verfehlt, oder kein κ* > 0 macht φ_x zu einem lokalen Minimum.
- Ein „trägt“ hieße nur, dass φ durch eine gesetzte Schleifenstärke κ ersetzt ist. Das ist keine Herleitung von φ, denn κ bleibt frei. Ob κ* einer
  natürlichen Zahl entspricht (etwa 1/(16π²) oder α relativ zu |q|), wird nur berichtet und nicht gewertet.

## Nur Bericht (nicht gewertet)
- Gewichte (w_I, w_R) = (1, 0): Nur der geladene Sektor koppelt an die Phase.
- Gewichte (2, 2): Dirac-Neutrinos. Hier bleibt die Symmetrie erhalten, erwartet sind π/8 oder 7π/24 (nicht blind).
- Bosonen-Vorzeichen (κ < 0).
- Lage des globalen Minimums als Funktion von κ.

## Werkzeuge
Python k450 (Hauptrechnung, Minimierung in δ wie k446) und Wolfram k450b (unabhängig, FindMinimum über δ, dE/dφ und κ*). Qiskit ist nicht einschlägig.
