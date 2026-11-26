# Ergebnis H166: Das Ziel ist nicht „2/9 und ⅔“ zugleich; exakt 2/9 kann kein polynomiales Potential geben; die Maske mit festem ε erzeugt die Phase aus keinem nativen Winkel

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H166_Phase_der_Nebendiagonale.md` (Commit c0e9142; a, b, c nicht blind, d blind). Skripte `k359_test_h166.py`
(`k359_out.txt`), `k359b_gegenprobe.wl` (`k359b_out.txt`, Wolfram). Status: H166a, b, c bestätigt (nicht blind); H166d bestätigt (kein Treffer).**

Anlass: Autor, 26.11.2026: Punkt 1 der offenen Stränge, „Was legt die Phase der Nebendiagonale in der Albert-Algebra fest?“ (offen seit H158).
Werkzeuge: Python (mpmath mit 30 Stellen, sympy, numpy/scipy); Wolfram unabhängig (FindRoot mit 40 Stellen, symbolische Reste, Eigenwerte). Die Ausgaben
stimmen überein (δ* auf 13 Stellen, 442,02σ, Tabelle d auf 7 Stellen). Qiskit nicht eingesetzt (keine Schaltung). Wolfram meldete nur die Warnung
`Symbol::undefined2` zu den im Skript selbst definierten Symbolen, keinen Rechenfehler.

## Kontrollen
ε = 0 gibt (K′, δ′) = (⅔, δ₀) auf 3·10⁻¹⁶. Maskenplatz, δ₀ → −δ₀ und δ₀ → δ₀ + 2π/3 ändern das Spektrum um höchstens 3·10⁻¹⁵. Form S ändert es um 10⁻¹⁶.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H166a | Aus m_μ/m_e allein: mit K = ⅔ ist δ* = 0,2222220470731 ± 4·10⁻¹⁰ (2/9 − 1,751·10⁻⁷); mit δ = 2/9 ist K = ⅔ − 1,421·10⁻⁷; beide exakt geben m_μ/m_e = 206,770316 gegen 206,7682827(46), Abstand 442σ (relativ 9,8·10⁻⁶) | > 5σ; Python = Wolfram | **bestätigt** (nicht blind) |
| H166b | dV/dδ = sin δ · (−12q x² − 4x + 3q) für cos 2δ + q cos 3δ, sin δ · (−q − 4x) für cos 2δ + q cos δ, x = cos δ; cos(2/9), tan(2/9) nicht algebraisch (sympy, Wolfram) | symbolisch; Satz | **bestätigt** (nicht blind) |
| H166c | S = exp(i(2π/3)L_n); W = (a + 2s) − 3s·L_n² − √3 v·L_n; w₁₂w₂₃w₃₁ − b³ = 0 nach Umeichung; tan δ = √3(√m_μ − √m_e)/(2√m_τ − √m_μ − √m_e): Rest 0 | Nullreste | **bestätigt** (nicht blind) |
| H166d | vorwärts 0 von 24 Treffern (nächster: Abstand 0,077); rückwärts 0 Treffer, keine Lösung hat K₀ = ⅔ (K₀ zwischen 0,446 und 7,9) | kein Treffer vorhergesagt | **bestätigt** |

## Lesart
- **Zielwert (a).** m_μ/m_e ist auf 2·10⁻⁸ gemessen und braucht m_τ nicht. Damit ist die Lage scharf: „K = ⅔ exakt“ und „δ = 2/9 exakt“ schließen sich
  auf Polmassen gegenseitig aus (442σ). Es bleibt eine Kurve. Unter dem Postulat J (K = ⅔) ist das Ziel δ* = 0,2222220471, nicht 2/9; der Unterschied ist
  relativ 7,9·10⁻⁷.
- **Die Daten trennen die Lesarten nicht.** K = ⅔ verlangt m_τ = 1776,9690 MeV, δ = 2/9 verlangt 1776,9665, der Selbstbezug 3δ = K 1776,9671 (alle +0,4σ).
  Nur H102 (3δ = π/4 − γ_M/2) liegt mit 1777,134 MeV abseits (+2,3σ, wie bekannt). Eine τ-Masse auf 1 keV wäre nötig, um ⅔ und 2/9 zu trennen.
- **Ob 2/9 exakt ist, lässt sich so nicht entscheiden.** Der Abstand 7,9·10⁻⁷ liegt zwischen (α/π)² = 5,4·10⁻⁶ und (α/π)³ = 1,3·10⁻⁸. Schon die Frage,
  für welche Massendefinition die Beziehung gilt, verschiebt mehr (H154: Laufen an gemeinsamer Skala ändert K um 1,2·10⁻³). 2/9 ist auf Polmassen eine
  auffällig gute Näherung, mehr gibt die Messung nicht her.
- **Notwendige Bedingung (b).** Beweis: Für ein Polynom V in (a, s, v) mit algebraischen Koeffizienten ist ein isolierter stationärer Punkt eine
  isolierte Lösung eines polynomialen Gleichungssystems über den algebraischen Zahlen; seine Koordinaten sind algebraisch (die Lösungsmenge ist über dem
  algebraischen Abschluss definiert, isolierte Punkte liegen in ihm). Dann ist tan δ = v/s algebraisch. Nach Lindemann–Weierstraß ist tan t für
  algebraisches t ≠ 0 transzendent, also δ ≠ 2/9. Dasselbe gilt für δ* nur dann nicht, wenn tan δ* algebraisch ist; das ist offen.
  Folge: Alle bisherigen Wege (H11, H16, H149, H152, H155, H157, H158) konnten 2/9 nur annähern. Exakt 2/9 verlangt eine transzendente Zahl im
  Koeffizientenverhältnis oder einen Mechanismus, in dem der Winkel linear entsteht (Fluss, Holonomie, Drehung um den Winkel selbst).
- **Was die Phase ist (c).** W ist eine Funktion des Zyklus-Erzeugers: W = a + 2r cos(Θ + δ) mit Θ = (2π/3)L_n. δ verschiebt den Zykluswinkel. In
  Spin-1-Sprache: W = c₀ + D·L_n² + B·L_n. Der Quadrupol D ist der Spin-2-Teil, der Dipol B der Spin-1-Teil, tan δ = −√3 B/D. B ist ungerade unter der
  Konjugation σ. Das τ ist der Zustand m = 0 (der symmetrische Fourier-Vektor), Elektron und Myon sind m = ∓1; δ misst ihre Aufspaltung relativ zum
  Abstand des τ. Eichinvariant ist nur Φ = 3δ, der Fluss durch das Platzdreieck (schon in `op3_selection_principle_2026_11_13.md`).
- **Maske (d).** Mit festem ε₀ = artanh β_sym = 0,6175296 erzeugt weder Form K noch die lineare Form aus einem der sechs nativen Winkel das
  Lepton-Spektrum, und rückwärts gehört zum Lepton-Spektrum kein unmaskiertes Paar mit K₀ = ⅔. Nur Form S (Ähnlichkeit) lässt K = ⅔ stehen, und dort ist
  δ in jedem Frame gleich. Die Übertragung in den Materie-Frame verschiebt das Ziel also nicht.

## Nachträglich (nicht in der Vorab-Notiz)
- K′ hängt in beiden Formen nicht von δ₀ ab (Spuren von DCD und (DCD)² sehen die Phase nicht). In Form K gilt geschlossen
  K′ = 2(1 + 2cosh 6ε + sinh 6ε)/(3cosh 3ε + sinh 3ε)², bei ε₀ also 0,7440. Die Vorwärtsprüfung über sechs Winkel war damit in K schon nach einem
  Winkel entschieden; das hätte vorab auffallen können.
- In 19 der 24 Vorwärtsfälle hat das maskierte Spektrum einen negativen Eigenwert; die Zuordnung zu (K′, δ′) ist dort nur formal.

## Bilanz der Setzungen (AGENTS, nach H155, H157, H158)
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H155 | Skala; tauschsymmetrische Terme | K = ⅔ am Baumgraph | δ: ein Koeffizient (Fit R*) |
| H156/H157 | Postulat J | nur gerade Ordnungen; N(W) verboten | δ am Rand bis Ordnung 10; innen ab Ordnung 12 mit Fit |
| H158 | Träger H₃(𝕆), σ als Symmetrie, Λ = v | Brannen-Form exakt; cos 2δ ab Ordnung 4 | v/s, als Verhältnis β/α |
| H166 | nichts Neues | Ziel δ* unter J; Ausschluss algebraischer Wege für exakt 2/9; Maske scheidet aus | eine reelle Zahl: Dipol B gegen Quadrupol D, σ-ungerade, entlang der Zyklusachse |

Geprüft: Das Ziel „2/9“ ist selbst eine gesetzte Eingabe (Brannens Zahl); unter J ist δ* die Messgröße. Die Frage entsteht nicht nur in einer gewählten
Zerlegung: Φ = 3δ ist eichinvariant und legt das Spektrum fest.

## Was eine Herleitung liefern müsste
1. einen σ-ungeraden, P-invarianten Term entlang der Zyklusachse (einen Drehsinn im Familienraum);
2. seine Größe relativ zum Quadrupol auf 2·10⁻⁹ (so genau ist δ* bekannt);
3. Invarianz unter dem Frame-Wechsel in Form S;
4. falls 2/9 exakt gemeint ist: keine rein algebraische Bestimmung.
Nativ σ-ungerade ist im Projekt die Chiralität (r45/H30: sie bricht die Spiegelung ρ, die Stärke ist nicht festgelegt). Ob die Feldgleichung daraus eine
Größe macht, ist die Frage des zweiten Strangs; sie braucht eine eigene Vorab-Notiz.

## Grenzen
- Nur der Zirkulantensektor; Polmassen ohne Strahlungskorrekturen; m_μ/m_e aus CODATA 2022, m_τ = 1776,93 ± 0,09 MeV wie H146.
- Teil b gilt für isolierte stationäre Punkte polynomialer Potentiale mit algebraischen Koeffizienten; Schleifenpotentiale mit Logarithmen fallen nicht darunter.
- Teil d prüft nur die Maske aus r47/r57 mit W = diag(0, 0, −3), Auslesung A und sechs Winkel.
- OP3 und OP4 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H166, k359. Nächste frei: H167, k362 (k360, k361 sind vergeben).
