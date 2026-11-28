# Vorab-Notiz H226 (k440): Welcher Term, der Im- und Re-Sektor unterscheidet, legt den Modulus φ auf den Messwert?

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11., 09:53 (Karte: „Tauschbrechenden Term suchen“).
**Werkzeuge:** Python (`k440_test_h226.py` → `k440_out.txt`), Wolfram unabhängig (`k440b_gegenprobe.wl` → `k440b_out.txt`; führende Ordnung symbolisch,
Minimierung mit FindMinimum). Qiskit nicht einschlägig.

## Ausgangslage
H225 (k439, widerlegt): Mit V_Im = −cos 2(δ − π/4 − φ) + q cos 3δ und V_Re = +cos 2(δ − φ) + q cos 3δ (q < 0 gesetzt) liegt das Minimum der gemeinsamen
Vakuumenergie E(φ) = min V_Im + min V_Re für jedes q bei φ = π/8. Grund: V_Re(−δ; π/4 − φ) = V_Im(δ; φ) exakt (Sektortausch). Messwert φ = x = 0,0395773.
Ein Term, der φ auf x legen soll, muss diesen Tausch brechen.

## Kandidatenterme (vorab, vollständig)
- **T1 Konjugationsterm nur im geladenen Sektor:** + c·α cos 2δ mit c = 1 (Im), c = 0 (Re); feste Achse, nicht mit φ gedreht. (H167: im Im-Sektor eigenständig; im
  Re-Sektor für c = 0 nicht vorhanden, H168.)
- **T2 ungleiche kubische Stärke:** q_Re = λ·q_Im, λ > 0 (gleiches Vorzeichen, damit die Zweigwahl H222 in beiden Sektoren bleibt).
- **T3 ungleiche Spin-1-Stärke:** |α′_Re| = κ·|α′_Im|, κ > 0.
- **T4 (Kontrolle, tauscherhaltend):** α cos 2δ in beiden Sektoren gleich. Erwartung: Tausch bleibt (cos 2δ gerade in δ), Minimum auf einem symmetrischen Punkt.

## Was vorab feststeht (nicht blind, führende Ordnung in α, q)
- T1: Stationarität bei φ = x verlangt α/q = 3[sin(π/4 − 3x) + cos 3x]/(2 cos 2x) ≈ 2,42 (also α < 0 bei q < 0); zweite Ableitung dort positiv. Ob es das **globale**
  Minimum ist, ist offen (der α-Term hat Periode π, die q-Terme π/3).
- T2: Stationarität bei φ = x verlangt λ = −sin(π/4 − 3x)/cos 3x ≈ −0,62 < 0, also außerhalb λ > 0. Erwartung: kein Treffer.
- T3: κ tritt in führender Ordnung nicht in die φ-Abhängigkeit (e_Re = −κ + q·|sin 3φ|). Erwartung: kein Treffer.

## Teile und Kriterien
**A (Grenzfall q → 0⁻, Verhältnis, blind für Globalität):** Für T1 bis T4 das Verhältnis (α/q, λ, κ), das φ = x zum **globalen** Minimum von E macht, exakt numerisch
bei q = −10⁻⁴. Vergleich mit einer vorab festen Liste von Rahmenzahlen: H167-Verhältnis (0,0793204/−0,0852 = −0,931), ±1, ±√2, ±1/√2, ±2, ±½, ±3, ±β_sym (0,54941),
±γ_L (1,86470), ±1/γ_L, ±γ_M (0,23753). **Übereinstimmung:** innerhalb 2 %.
**B (endliche Kopplung, Vorhersage, blind):** q/α′ = −0,0852 fest (H167). Den einen Koeffizienten des Terms so wählen, dass der geladene Sektor am globalen Modulus-Minimum
δ_Im = δ* = 0,2222220 trifft; dann ist δ_Re eine Vorhersage: x_ν,pred = π/6 − δ_Re gegen x_ν = 0,04336 ± 0,00213 (H213). **Kriterium:** innerhalb 2σ.
Natürliche Größe: |Koeffizient| ≤ 1 (bei T1 |α| ≤ 1).
**Urteil:** **trägt**, wenn ein Term B innerhalb 2σ erfüllt und sein Verhältnis aus A eine Rahmenzahl trifft; **trägt teilweise**, wenn B erfüllt ist, aber keine Rahmenzahl
getroffen wird (dann ein Parameter, angepasst an die geladenen Leptonen, Re-Sektor vorhergesagt); **widerlegt**, wenn kein Term mit natürlicher Größe φ = x zum
globalen Minimum macht. T4 zählt nicht für das Urteil (Kontrolle).

## Vorwissen geprüft
H167 (Konjugationsterm ρ* = α/α′ = 0,0793 als Fit; 42 Kandidaten ohne Treffer, H167d1), H168 (c = 0: Konjugationsterm fällt mit Spin-1-Term zusammen), H221
(Universalität gesetzt; Teil c: beide Terme universell mit kleinem α, q treffen beide Versätze als Fit), H222 (Zweigwahl), H225 (Tausch, π/8). Kein früherer Modulus-Ansatz.

## Grenzen (vorab)
Zirkulantensektor, Baumniveau, K = ⅔, H99. Jeder Kandidat führt einen Koeffizienten ein; ohne Treffer in A ist ein Erfolg in B ein Fit mit einer Vorhersage (Re-Sektor).
Herkunft des Tauschbruchs (warum gerade dieser Term) wird nicht hergeleitet.
