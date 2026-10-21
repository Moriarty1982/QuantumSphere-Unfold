# Erkundungsprotokoll: Weinberg-Winkel und Tachyon-Kegel

Angelegt am 2026-10-21 nach dem Ergebnis von H14 (`llm/Ergebnis_H14_Kegelwinkel_Weinberg.md`). Skript
`llm/k44_erkundung_weinberg.py`.

## Regeln

1. **Kein Test.** Nichts in diesem Protokoll zählt als Bestätigung. Ein Test braucht eine eigene Vorab-Notiz mit einer
   Größe, die vor ihrer Festlegung unbekannt ist.
2. **Jede Variante wird eingetragen**, mit Ergebnis, auch Fehlschläge und Einfälle, die beim Rechnen auftauchen. Die
   Zahl der Einträge ist die Zahl der Versuche und geht in jede spätere Bewertung ein.
3. **Eingaben werden nicht nachträglich angepasst**, um einen Treffer zu erzeugen. Eine Variante ändert genau eine Sache
   und sagt, welche.
4. **Physik vor Zahl.** Eine Variante braucht eine physikalische Begründung, bevor sie gerechnet wird. Ist sie beim
   Rechnen aufgefallen, wird sie als „aufgefallen“ markiert.
5. **Ziel** ist eine Erklärung, die etwas Neues vorhersagt, nicht eine, die die Abweichung wegerklärt.

## Ausgangslage

Vorhersage aus ϑ_c = 2θ_W: sin²θ_W = (1 − β_sym)/2 = 0,22533 (β_sym = 0,54935). On-shell aus den Massen: 0,22321 ±
0,00026, MS-bar: 0,23122. Die Lücke zum On-shell-Wert beträgt +0,00212. Das entspricht einer um 110 MeV kleineren
W-Masse oder einer Änderung von Δρ um −0,00275.

Daten: PDG 2024 mit Update 2025 (Summary Tables; Review „Electroweak Model and Constraints on New Physics“, Stand
15. April 2026), abgerufen 2026-10-21. Δρ_t = 0,00934 · (m_t/172,61 GeV)² nach Gl. (10.16) dort. Die Varianten E2–E5 sind
Abschätzungen in führender Ordnung, mit einer Genauigkeit von etwa 10⁻³ in sin²θ_W.

## Einträge

| Nr. | Variante | Begründung | Ergebnis | Bewertung |
|---|---|---|---|---|
| E1 | β_sym durch den Tribonacci-Wert β_T = 0,54369 ersetzen | r01.3: γ_L liegt 1,37 % über 𝕋 (Gitterkorrektur) | Vorhersage 0,22816; Abstand zu on-shell +0,00495 statt +0,00212 | **Fehlschlag**: verschiebt in die falsche Richtung |
| E2 | On-shell-Winkel ohne den Top-Beitrag Δρ_t | Der Kegel käme aus der Feldstruktur, die von schweren Teilchen nichts weiß | On-shell ohne Top: 0,23039; Abstand −0,00506 | **Fehlschlag**: Das Herausrechnen schiebt den Messwert über die Vorhersage hinaus, nahe an MS-bar |
| E3 | Baumgraphen-Winkel aus (α, G_F, m_Z) | Wert ganz ohne Schleifen, mit α(0) bzw. α̂(M_Z) | 0,21215 bzw. 0,23361; Abstand +0,01318 bzw. −0,00829 | **Fehlschlag**: Die Wahl von α allein spannt 0,02 auf; kein Wert liegt nahe |
| E4 | Bruchteil von Δρ_t, der die Vorhersage genau trifft (*aufgefallen* beim Rechnen von E2) | keine | 70,5 % von Δρ_t, also ein Top-Beitrag wie bei m_t,eff = 145 GeV | **Kein Befund**: Die Zahl hat keine Bedeutung, weder m_W, m_Z noch m_H. Nur als Versuch gezählt |
| E5 | Neutrinos als fehlender Betrag (Vorschlag des Autors) | Neutrinos stecken in denselben Schleifen wie das Top-Quark; das Dokument behandelt Neutrinomassen eigens | siehe unten | **Fehlschlag** für alle bekannten Neutrinos; offen nur für neue Physik |

### E5 im Einzelnen

- **Richtung.** Nötig ist *weniger* Δρ als im Standardmodell, um 0,00275. Ein Dublett mit Massenaufspaltung liefert
  immer Δρ ≥ 0. Zusätzliche Teilchen dieser Art verschieben also in die falsche Richtung, wie das Top-Quark selbst.
- **Leichte Neutrinos.** Im Dublett mit dem Elektron tragen sie Δρ ≈ 3 · 10⁻¹⁴ bei. Nötig wäre 3 · 10⁻³, also elf
  Größenordnungen mehr. Ihre Masse ist zu klein, um irgendetwas zu bewirken.
- **Gemessene Massen.** Der On-shell-Winkel ist aus gemessenen Massen gebildet. Neutrinos können eine Messung nicht
  ändern. Sie könnten nur Teil einer Korrektur zwischen einem „strukturellen“ und dem gemessenen Winkel sein, wie in E2.
- **Was übrig bleibt.** Ein *negativer* Beitrag bräuchte neue Physik. Genannt werden in der Literatur etwa schwere
  Majorana-Teilchen oder Neutrinomischungen außerhalb der Unitarität. Das ist hier nicht nachgeprüft. Die Größe wäre
  erheblich, gleichwertig mit 110 MeV in m_W. Vor jeder weiteren Verfolgung müssten die bestehenden Schranken für solche
  Effekte geprüft werden.

### Berichtigung zu E5 (2026-10-21, beim Rechnen von E6)

Der Punkt „Richtung“ oben ist falsch gerahmt und bleibt zur Nachvollziehbarkeit stehen. Richtig ist: Die Vorhersage
entspricht dem On-shell-Wert, aus dem ein **in der Natur vorhandener** Beitrag Δρ_X = +0,00275 herausgerechnet ist.
Positive Beiträge, also Dubletts, haben damit die *richtige* Richtung, genau wie das Top-Quark in E2. Das Problem ist
die Größe. Für leichte Neutrinos ist sie elf Größenordnungen zu klein, für neue Teilchen ist sie durch E7 begrenzt. Die
Bewertung „Fehlschlag“ bleibt, die Begründung lautet jetzt so.

| Nr. | Variante | Begründung | Ergebnis | Bewertung |
|---|---|---|---|---|
| E6 | Kombinationen von Beiträgen weglassen (Vorschlag des Autors) | Der strukturelle Winkel könnte der Winkel ohne einen Teil der Schleifen sein | Nur zwei Stücke sind groß: Top 0,00934 und Rest (Higgs, bosonisch, höhere Ordnung) 0,00108. Leichte Dubletts liegen bei ≤ 5 · 10⁻⁷. Die vier Teilmengen ergeben 0,22321 / 0,22404 / 0,23039 / 0,23122, das Ziel ist 0,22533 | **Fehlschlag**: Keine Teilmenge trifft. Am nächsten kommt „Rest weglassen“ mit −0,00129. Leichte Teilchen können nichts beitragen |
| E7 | Gemischter Zustand oder dunkler Sektor (Z–Z′-Mischung, dunkles Photon, Dunkle Materie mit Z-Kopplung; Vorschlag des Autors) | Eine Beimischung eines dunklen Zustands zu Z oder Photon verschiebt die Massen | Größenschranke unabhängig vom Mechanismus: Ein neuer Beitrag Δρ = 0,00275 höbe m_W um 155 MeV gegen die SM-Vorhersage. Gemessen minus SM-Fit: +10 ± 14 MeV, also 2σ-Raum Δρ_neu ∈ [−0,0003; 0,0007]. Unsichtbare Z-Breite N_ν = 2,9963 ± 0,0074 | **Fehlschlag**: Jeder reale Effekt in den Massen darf höchstens etwa ein Viertel der Lücke ausmachen |

### E8 und E9: Ableitung aus der Struktur (Skript `llm/k45_struktur_weinberg.py`)

**E8, Umformung von H14 (Mathematik, kein Versuch im Sinn der Zählung).** cos 2θ = tanh η ist gleichwertig mit
- tan θ = e^{−η},
- sin²θ = 1/(1 + e^{2η}),
- ϑ_c = 2θ = Π(η), wobei Π der Parallelitätswinkel nach Lobatschewski ist (cos Π(x) = tanh x).

In der Sprache von r05.1(d) heißt das: Die Portgewichtung e^{tσ_x} bei t = η hat das Gewichtsverhältnis
e^{2η} = cot²θ = (g/g′)². **H14 ist also eine Aussage über ein Kopplungsverhältnis**, g/g′ = e^η, den Doppler-Faktor aus
r01, Weg (C). Ein Massenverhältnis ist es nicht. Kopplungsverhältnisse laufen mit der Skala. Im MS-bar-Schema hat sin²θ_W
sein Minimum bei μ = M_W, etwa 0,231 (PDG Abb. 10.1). Darüber steigt es (Ein-Schleife: 0,235 bei 200 GeV, 0,243 bei
1 TeV), darunter ebenfalls. **Kein Skalenwert erreicht 0,22533.** Die Struktur verweist damit auf das Schema, in dem der
Abstand *größer* ist. Die Nähe zum On-shell-Wert wird von ihr nicht gestützt.

| Nr. | Variante | Begründung | Ergebnis | Bewertung |
|---|---|---|---|---|
| E8 | H14 als Kopplungsverhältnis g/g′ = e^η bei laufender Skala | Strukturelle Lesart über die Portgewichtung (r05.1d) | MS-bar-Minimum ≈ 0,231 > 0,22533 auf jeder Skala | **Fehlschlag** der Skalenrettung |
| E9 | cot θ_W (on-shell) gegen die drei Dokumentkonstanten 1/β_sym, e^η, γ_L (*aufgefallen* beim Rechnen von E8) | r01.3: γ_L (Weg A) und e^η (Weg C) fallen am Tribonacci-Punkt zusammen | cot θ_W = m_W/√(m_Z² − m_W²) = 1,86550 ± 0,00140. γ_L = 1,86444: z = −0,8. e^η: z = −8,1. 1/β_sym: z = −32 | **Auffällig, kein Beleg** (siehe unten) |

### E9 im Einzelnen

- **Form.** cot θ_W = γ_L, also g/g′ = cosh 2η, der Materie–Tachyon-Lorentzfaktor. H14 war g/g′ = e^η. Nach r01.3 sind
  beide am Tribonacci-Punkt gleich. Sie unterscheiden sich nur um die 0,55 % zwischen Weg (A) und Weg (C). Die On-shell-Daten
  liegen bei (A).
- **Gleichwertige Vorhersage.** m_W = m_Z γ_L/√(1 + γ_L²) = 80,3590 GeV mit γ_BI = 0,2375 und 80,3614 GeV mit
  γ_BI = 0,237532. Gemessen: 80,3692 ± 0,0133. Die SM-Vorhersage aus dem Fit ist 80,359 ± 0,006. **Die Beziehung fällt
  derzeit mit der SM-Vorhersage zusammen** und lässt sich von ihr erst bei einer Genauigkeit von wenigen MeV trennen.
  Dafür müsste außerdem die Ziffernfolge von γ_BI festgelegt sein, denn die vierte Stelle verschiebt m_W um 2,4 MeV. Mit
  γ_BI = 0,274 (andere Zählweise der Literatur) ergäbe sich 82,7 GeV, ausgeschlossen.
- **Warum kein Beleg.**
  - Die Beziehung ist nachträglich gefunden.
  - Die drei Dokumentkonstanten 1,820 / 1,854 / 1,864 liegen im selben Bereich wie cot θ_W über die Schemata
    (1,823 bis 1,866). Irgendeine Paarung ist dadurch fast erwartbar.
  - Geschätzt liegt die Wahrscheinlichkeit, dass der On-shell-Wert innerhalb von 1σ an einer der drei Konstanten liegt,
    bei etwa 3 · 2 · 0,0014 / 0,05 ≈ 0,17.
- **Was es wert ist.** Es ist der erste Kandidat dieses Protokolls, der eine echte, künftige Messung betrifft. Ein Test
  bräuchte eine Vorab-Notiz mit festgelegtem γ_BI, festgelegter Fehlerrechnung und einer künftigen m_W-Kombination, deren
  Genauigkeit die SM-Vorhersage von der Beziehung trennt.

### E10: H15 zusammen mit der Drift von β_sym (Folgerung, kein gezählter Versuch; Skript `llm/k47_drift_weinberg.py`)

`prop:H0-tension` lässt β_sym driften, von 0,527 zur Zeit der Hintergrundstrahlung (z = 1100) auf 0,5493 heute,
mit etwa 1,6 · 10⁻¹² pro Jahr. Hält H15 (cot θ_W = γ_L), dann driftet auch der Weinberg-Winkel.

**(a) Frame-Umrechnung.** H15 vergleicht m_W/m_Z. Haben W und Z dieselbe k-Zahl, kürzt sich der Faktor γ^{−k}. Der
On-shell-Winkel ist dann in jedem Frame gleich. Die k-Gleichheit ist naheliegend, steht aber nicht in der Quelle.

**(b) Für den Test von H15 bedeutungslos.** Heute beträgt die Drift etwa 7 · 10⁻⁸ MeV pro Jahr in m_W.

**(c) Welche Lesart?** Zur Wahl stehen zwei:
- **symmetrisch:** γ_L = cosh 2η(t), z = 1100: γ_L = 1,7690;
- **nur der Materie-Frame driftet** (r18, „angeboten, nicht übernommen“): γ_L = cosh(η₊(t) + η_s), z = 1100: 1,8157.

Für die symmetrische Lesart sprechen drei Punkte:
1. **`thm:spring`.** Das Photon ist Gleichgewichtspunkt nur für z_T = −z_M. Bei kleiner Auslenkung gilt x_γ = x_M/3
   und x_T = −x_γ. Relativ zum mitgeführten Photon liegen Materie und Tachyon damit wieder symmetrisch, beide bei
   β + 2δ/3. Die Dynamik der Quelle erhält also die Symmetrie um das Photon.
2. **Neutrale Photonachse (r01, Autorangabe).** Driftet nur der Materie-Frame, wandert die Mitte, und das Photon ist
   nicht mehr der neutrale Mittelpunkt.
3. **Lesart B.** Der Tachyon ist das Dualitätsbild z_T = iz_M mit gleichem |s|. Er folgt der Materie, statt fest zu
   bleiben (r19.1, r20.1).

Der H0-Faktor entscheidet **nicht**. Symmetrisch trifft er 1,083 mit dem Exponenten 1,52, nur Materie mit dem Exponenten
3,03. Der Exponent steht nicht in der Quelle (r18).

**Ergebnis (c):** Die symmetrische Lesart ist die mit der Quelle verträgliche. Die andere stützt sich nur auf die nicht
übernommene Lesart aus r18.

**(d) Folgerung.** Mit H15, Drift und symmetrischer Lesart war zur Zeit der Hintergrundstrahlung sin²θ_W = 0,2422 und
m_W/m_Z = 0,8705. Heute sind es 0,2234 und 0,8812, also etwa 8 % mehr in sin²θ_W. Ist die Drift linear in der Zeit,
gilt derselbe Wert praktisch auch zur Zeit der Elementsynthese.

**(e) Schranken (Literaturrecherche 2026-10-21).**
- Eine veröffentlichte Schranke speziell für eine zeitliche Änderung von sin²θ_W wurde **nicht gefunden**.
- Yang und Rafelski (arXiv:2603.02652, „Weinberg Angle, Neutron Abundance in BBN, and Lifetime“) untersuchen die
  Empfindlichkeit von Neutronenanteil und Neutronenlebensdauer auf s²_W. Sie halten α und v fest und geben ausdrücklich
  keine Schranke an.
- Für die Higgs-VEV finden Burns, Keus, Sher und Tait (arXiv:2403.09325) mit ⁴He −0,014 ≤ δv/v ≤ 0,026 und mit
  Deuterium −0,005 ≤ δv/v ≤ −0,001. Ältere Werte stammen von Yoo und Scherrer (astro-ph/0211545).
- Für α gilt aus BBN Δα/α = (−7 ± 9) · 10⁻³.

**Eigene Abschätzung**, nicht veröffentlicht, nur führende Ordnung: Bei festem α und v hängt G_F nur über den
Schleifenterm 3c²/(32π² s²) von θ_W ab (Yang/Rafelski, Gl. 8). Die Änderung von cot²θ_W von 3,48 auf 3,13 gibt
ΔG_F/G_F ≈ +0,33 %, gleichwertig mit δv/v ≈ −0,16 %. Das liegt innerhalb der ⁴He-Schranke. Neutrale Ströme (g_V^e) wirken
auf die Neutrino-Entkopplung nur schwach. **Eine Drift von 8 % in sin²θ_W bei festem α und v ist nach dieser
Abschätzung kosmologisch nicht ausgeschlossen, aber auch nicht prüfbar.** Hält man statt α und v andere Größen fest,
ändert sich das. H15 legt nicht fest, welche Größen konstant bleiben.

### E11: Was bleibt laut Dokument bei der Drift fest? (Prüfung der Quelle; Skript `llm/k48_feste_groessen.py`)

**Was die Quelle sagt.**
- Definition des Frame-Insertion-Counts: X^(photon) = γ_L^{−k} X^(matter).
- `thm:k-values`: k(α⁻¹) = 1, k(m_e) = 1, k(ħ) = 1, k(G_N) = 2, k(c) = 0, k(γ_BI) = 0 („frame-invariant by
  construction“).
- Korollar „α-drift as a frame effect“: „The hardware value α^(photon) is strictly constant“, und
  α^(matter)(t) = γ_L^(local)(t) · α^(photon).
- `prop:saturation` (1) schreibt die Neutrinomasse ebenso als γ_L(t)⁴ mal Photon-Frame-Wert.

**Fest bleiben** damit die Werte im Photon-Frame und alle Größen mit k = 0 (c, γ_BI). **Es driften** die
Materie-Frame-Werte mit γ_L^(local)(t)^k. Die Quelle unterscheidet dabei selbst zwei Faktoren: das strukturelle
γ_L = γ_BI/γ_string, fest, weil beide Eingaben k = 0 haben bzw. feste Zahlen sind, und den lokalen Faktor
γ_L^(local)(t), der driften kann. Das ist die Trennung aus r18.

**Folge für H15 und E10.**
- H15 ist mit dem strukturellen γ_L = γ_BI/γ_string festgelegt, und der ist fest. **H15 sagt deshalb keine Drift von
  θ_W voraus.**
- Unabhängig davon ist m_W/m_Z ein Verhältnis von Massen mit gleichem k. Im k-Gesetz kürzt es sich und driftet nicht.
- Die Folgerung E10 (d), sin²θ_W = 0,242 bei z = 1100, gilt deshalb nur, wenn man H15 statt mit dem strukturellen mit
  dem lokalen Faktor liest. Nach den Regeln der Quelle ist das nicht die naheliegende Lesart. **E10 (d) wird damit auf
  diese Zusatzannahme eingeschränkt.**

**Nebenbefund 1: Die Drift aus `prop:H0-tension` verträgt sich nicht mit konstantem α.**
- Wirkt die Drift über den lokalen Faktor, wie r18 sie liest, dann driftet nach dem Korollar auch α^(matter).
- Bei 1,6 · 10⁻¹² pro Jahr in β_sym folgt |d ln α/dt| = 3,9 · 10⁻¹² pro Jahr.
- Atomuhren geben (1/α) dα/dt = 1,0(1,1) · 10⁻¹⁸ pro Jahr (Lange et al., PRL 126, 011102, 2021). Das ist ein Abstand von
  etwa 3,5 · 10⁶ σ.
- Seit z = 1100 ergäbe sich |Δα/α| ≈ 5 %, gegen Schranken im Bereich von 10⁻³ aus der Hintergrundstrahlung.
- `prop:H0-tension` kann also nicht zugleich die Hubble-Spannung über den lokalen Frame-Faktor erklären und α konstant
  lassen. Es sei denn, der Faktor, der α setzt, ist ein anderer als der, der die Hubble-Spannung erzeugt. Das sagt die
  Quelle nicht.
- Die jährliche Modulation aus P5 ist davon nicht betroffen. Ihre Amplitude ist klein, etwa 10⁻¹⁰ · δΦ/c².

**Nebenbefund 2: Das Vorzeichen für α ist uneinheitlich.**
- `thm:k-values` gibt k(α⁻¹) = 1, also α^(matter) = α^(photon)/γ_L.
- Das Korollar schreibt α^(matter) = γ_L · α^(photon).
- Für den Betrag der Drift ist das gleichgültig.

Bewertung: E11 ist eine Prüfung bestehender Aussagen der Quelle gegen bekannte Daten, keine neue Vorhersage. Sie wird
nicht als Versuch gezählt.

## Stand

11 Einträge, davon 8 gezählte Versuche, 0 Treffer im Sinne einer Erklärung, 1 Auffälligkeit (E9), 1 Folgerung (E10, durch
E11 auf eine Zusatzannahme eingeschränkt), 1 Quellenprüfung (E11). H15 sagt nach den Regeln der Quelle einen zeitlich
konstanten Weinberg-Winkel voraus. Die Drift aus `prop:H0-tension` steht in ihrer Frame-Faktor-Form gegen die Atomuhren.

Vorige Zwischenbilanz: 10 Einträge, davon 8 gezählte Versuche, 0 Treffer im Sinne einer Erklärung, 1 Auffälligkeit (E9), 1 Folgerung (E10).
Die Folgerung E10 macht H15 zusammen mit `prop:H0-tension` zu einer Aussage über eine frühere Epoche. Mit heutigen
Schranken lässt sie sich nicht prüfen, solange offen ist, welche Größen bei der Drift fest bleiben.

Frühere Zwischenbilanz: 9 Einträge, davon 8 gezählte Versuche, 0 Treffer im Sinne einer Erklärung, 1 Auffälligkeit (E9).

Frühere Zwischenbilanz: 7 Versuche, 0 Treffer. Keine Variante hat die Lücke physikalisch erklärt. Die Tribonacci-Korrektur verschiebt in die
falsche Richtung. Das Weglassen von Beiträgen trifft in keiner Kombination. E7 schließt allgemein aus, dass ein in der
Natur vorhandener Zusatzeffekt die Lücke füllt: Er wäre in der W-Masse sichtbar. Übrig bleiben zwei Möglichkeiten. Die
Lücke ist ein Unterschied zwischen einer strukturellen und der physikalischen Größe, für den eine Vorschrift fehlt, oder
die Beziehung ist ein Zufall.

## Offene Fragen

- Aus welcher Größe von Lesart B ließe sich ein Schema oder eine Skala ableiten, statt sie zu wählen?
- Lässt sich für E5 (negative Beiträge) eine Schranke aus der Literatur angeben, bevor weitergerechnet wird?
