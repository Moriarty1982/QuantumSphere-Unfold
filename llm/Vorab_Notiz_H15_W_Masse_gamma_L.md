# Vorab-Notiz H15: Weinberg-Winkel aus γ_L, Vorhersage der W-Masse

Festgelegt am 2026-10-21, **vor** dem Vergleich mit künftigen Messungen und vor der Berechnung von γ_BI auf mehr als vier
Stellen. Bezug: Erkundungsprotokoll `llm/Erkundungsprotokoll_Weinberg_Kegel.md`, Eintrag E9; v4.9.0-r01.3 (Wege A/C);
v4.9.0-r05.1 (Portgewichtung).

## Hypothese (V)

**H15:** Das Verhältnis der elektroschwachen Kopplungen in der On-shell-Definition ist der Materie–Tachyon-Faktor:

    cot θ_W = m_W / √(m_Z² − m_W²) = γ_L = γ_BI / γ_string,

gleichwertig m_W = m_Z · γ_L / √(1 + γ_L²).

## Eingaben (verbindlich)

- **γ_string** = ln 2/(π√3), exakt.
- **γ_BI**: die positive Lösung der Zählgleichung von Meissner bzw. Domagała–Lewandowski,
  Σ_{j = 1/2, 1, 3/2, …} 2 · exp(−2π γ √(j(j+1))) = 1, numerisch auf 10⁻¹² gelöst. Begründung: Das Dokument nennt
  γ_BI ≈ 0,2375 und führt es in r03 auf genau diese Zählung zurück (gr-qc/0407051, gr-qc/0407052). Die Gleichung legt die
  Ziffern fest, ohne dass eine gerundete Angabe gewählt werden muss.
- **m_Z** = 91,1880 ± 0,0020 GeV (PDG 2025). Wird m_Z in der Vergleichsquelle neu angegeben, gilt der neue Wert.
- **Unsicherheit der Vorhersage:** allein aus σ(m_Z), σ_pred = cos θ_W · σ(m_Z) in führender Ordnung. γ_BI und γ_string
  gelten als exakt.

## Vergleichsdaten (verbindlich)

**Die erste Weltmittelung oder Kombination von m_W, die nach dem 2026-10-21 veröffentlicht wird**, von der PDG (Summary
Tables) oder von einer offiziellen Kombinationsgruppe der LHC- und Tevatron-Experimente. Gibt es beides, gilt die zuerst
erschienene. Einzelmessungen zählen nicht.

Ausdrücklich **kein Test** sind die bereits bekannten Werte: PDG 2025 80,3692 ± 0,0133 GeV, die Einzelmessungen von ATLAS,
CMS, LHCb, CDF und D0, und die SM-Fit-Vorhersage 80,359 ± 0,006 GeV.

## Offenlegung (vor dem Festschreiben bekannt)

1. **Nachträglich gefunden.** Die Beziehung fiel beim Rechnen von E8 auf. Sie liegt 0,8σ am bekannten On-shell-Wert. Die
   Nähe ist der Grund für diese Notiz und zählt nicht als Ergebnis.
2. **Ungefähre Vorhersage bekannt.** Mit γ_BI = 0,2375 ergibt sich 80,3590 GeV, mit dem aus dem Gedächtnis bekannten
   Meissner-Wert 0,237532 etwa 80,3614 GeV. Die genaue Zahl folgt aus der Gleichung oben.
3. **Fällt mit dem Standardmodell zusammen.** Die SM-Vorhersage (80,359 ± 0,006 GeV) liegt nur wenige MeV entfernt. Ein
   Vergleich kann H15 widerlegen. Er kann H15 aber erst dann gegenüber dem SM auszeichnen, wenn die Messunsicherheit
   unter etwa 1 MeV liegt.
4. **Look-elsewhere.** Die drei Dokumentkonstanten 1/β_sym, e^η und γ_L liegen im Bereich, den cot θ_W über die Schemata
   abdeckt. Die Wahrscheinlichkeit eines 1σ-Treffers einer der drei am On-shell-Wert ist etwa 0,17. Im Protokoll sind
   8 Versuche gezählt.
5. **Keine Herleitung.** Lesart B enthält kein SU(2) × U(1). Die Gleichsetzung des Gewichtsverhältnisses der
   Portgewichtung mit (g/g′)² ist formal (r05.1, r06.4).

## Verfahren (verbindlich)

Skript `llm/k46_test_h15.py`:
1. γ_BI aus der Zählgleichung (Summe bis zur Konvergenz < 10⁻¹⁵), γ_L, m_W,pred, σ_pred. **Sofort nach dem Commit dieser
   Notiz** rechnen und das Ergebnis als festgelegte Vorhersage eintragen, ohne Vergleich.
2. Sobald die Vergleichsdaten vorliegen: z = (m_W,meas − m_W,pred)/√(σ_meas² + σ_pred²). Daneben wird die SM-Vorhersage
   der Vergleichsquelle berichtet und der Abstand m_W,pred − m_W,SM in Einheiten von σ_meas.

## Entscheidungskriterium (verbindlich)

- |z| ≥ 3: **widerlegt**.
- 2 ≤ |z| < 3: **Spannung**.
- |z| < 2: **verträglich**. Ist zugleich |m_W,pred − m_W,SM| < 2σ_meas, lautet der Zusatz „nicht vom SM unterscheidbar“.
  Dann zählt das Ergebnis nicht als Stütze für H15.
- **Gestützt** ist H15 nur, wenn |z| < 2 gilt und die Messung die SM-Vorhersage mit mindestens 3σ ausschließt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
