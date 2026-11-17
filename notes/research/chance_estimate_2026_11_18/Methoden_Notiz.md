# Zufallsabschätzung der Treffer von γ_L: Verfahren (vor der Rechnung festgelegt)

**Stand:** 18. November 2026, vor jeder Rechnung committet. **Erkundung, nicht blind:** Die Treffer selbst sind bekannt (Ω_M, |U_e2|², cot θ_W,
Φ_e); unbekannt ist, wie selten sie unter einer festen Zählung der Auswahlmöglichkeiten sind. Keine H-Nummer, kein Test der Theorie.
Auftrag des Autors vom 17./18.11.2026: „Ja, Zufallsabschätzung“ (offener Vorschlag 3 der Übergabe: Zahl der Auswahlmöglichkeiten hinter den
Treffern zählen und die Zufallswahrscheinlichkeit abschätzen). Skript `k235_chance_estimate.py`, Ausgabe `run/k235_stdout.txt`.

## Vorwissen geprüft
Einzelabschätzungen gibt es schon, eine zusammenführende nicht:
- H15 (`../v4_9_0_r01_r16/llm/Vorab_Notiz_H15_W_Masse_gamma_L.md`, Offenlegung 4): cot θ_W = γ_L; drei Dokumentkonstanten (1/β, e^η, γ_L),
  1σ-Treffer zufällig mit p ≈ 0,17; im Erkundungsprotokoll 8 Versuche.
- H102 (`../predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`): Φ_e = π/4 − γ_M/2 aus einem Scan mit 154 Versuchen, ein Treffer, 0,34 erwartet.
- H9 (`../v4_8_0_r03_r12/llm/Vorab_Notiz_H9_Solarwinkel_beta_sym.md`, Offenlegung 1): nachträglich, „rund zehn vergleichbare Konstanten“.
- Λ-Kreuzungen (`../v4_10_0_r70/llm/Erkundung_Lambda_Kreuzungen.md`): 26 Lesarten für Ω_M, Trefferbereich 0,049 der Einheitsstrecke, 1,3 Zufallstreffer
  erwartet; Ω_M = β² stand schon vorher im Korpus (`thm:dark-energy`).
- H98 (`../predictions/Ergebnis_H98_Zaehlregel_Sonderstellung.md`): 36 Zählregel-Paare, γ_L zwischen 1,006 und 3,51; nur DL/ABCK trifft Leptonfenster,
  m_W und Ω_M; Schätzung „wenige Prozent“ für einen zufälligen Dreifachtreffer. Die drei Fenster waren nach den bekannten Treffern gewählt.
- Kernkarte K11.2, K51 (`../v4_10_0_r26_r31/llm/Kernkarte_Quantum_Sphaera_v1.md`): frühere Look-elsewhere-Werte 11 % und 2 % je Beziehung für andere
  Formeln; hier nicht verwendet, weil sie nicht an γ_L hängen.
- `../review_discarded_ideas_2026_11_17/`: 35 widerlegte Tests; sie gehen in Teil A nur als Hinweis ein (nicht gezählte Suchen).

## Teil A: Buchführung der belegten Auswahl
Je Treffer i: belegte Zahl der Versuche N_i und Trefferanteil w_i, p_i = 1 − (1 − w_i)^{N_i} (bzw. der belegte Wert). Feste Liste:
| i | Treffer | p_i | Herkunft |
|---|---|---|---|
| 1 | Ω_M = β² | 1 − 0,951^26 | Λ-Kreuzungen |
| 2 | \|U_e2\|² = β² | 1 − (1 − w)^10, w = 2σ-Breite (1σ beidseitig) von \|U_e2\|² aus NuFIT 6.1 auf der Einheitsstrecke | H9 |
| 3 | cot θ_W = γ_L | 0,17 | H15 |
| 4 | Φ_e = π/4 − γ_M/2 | 1 − e^{−0,34} | H102 |

Berichtet werden Σ p_i (erwartete Zufallstreffer bei diesen Suchen), das naive Produkt Π p_i und die Wahrscheinlichkeit für vier von vier
(Poisson-Binomial). Vorab gesagt: Das Produkt ist eine **Untergrenze** der Zufallswahrscheinlichkeit, weil (a) nicht gezählte Suchen fehlen,
(b) Treffer 1 und 2 dieselbe Zahl gegen zwei Messgrößen um 0,30 prüfen (Ω_m ≈ |U_e2|² ist eine Zahlengleichheit der Natur) und (c) die Treffer erst
nach dem Sehen als Treffer ausgewählt wurden.

## Teil B: Gegenprobe mit einem breiten, festen Zielkatalog
Statt der drei nachträglich gewählten Fenster von H98 ein vorab festgelegter Katalog dimensionsloser Messgrößen; dieselbe Zählung für jedes Paar.
- **Formen F (8):** β, β², 1/β, γ_L, 1/γ_L, e^η, e^{−η}, η, mit β = √((γ_L − 1)/(γ_L + 1)), η = artanh β.
- **Ziele K (16), Treffer bei |Form − Ziel| ≤ 2σ:**
  - Neutrinos (NuFIT 6.1, NO; Werte im Repo): sin²θ₁₂ 0,3088 (+0,0067/−0,0066), sin²θ₂₃ 0,470 (+0,017/−0,014), sin²θ₁₃ 0,02248 ± 0,00056,
    Δm²₂₁/Δm²₃₁ 0,03002 ± 0,00046.
  - Elektroschwach: cot θ_W (on-shell) aus m_W 80,3692 ± 0,0133, m_Z 91,1880 (Repo); sin²θ_W (MS-bar, M_Z) 0,23129 ± 0,00004.
  - Massenverhältnisse: m_H/m_Z 1,3730 ± 0,0012; m_t/m_W 2,1472 ± 0,0037; m_μ/m_τ 0,059464 ± 0,000004.
  - Starke Kopplung, CKM: α_s(M_Z) 0,1180 ± 0,0009; |V_us| 0,2243 ± 0,0008; |V_cb| 0,0408 ± 0,0014; |V_ub| 0,00382 ± 0,00020.
  - Kosmologie: Ω_m (DESI DR2 BAO) 0,2975 ± 0,0086 (Repo); n_s 0,9649 ± 0,0042; Ω_b h² 0,02237 ± 0,00015.
  - Werte ohne Repo-Fundstelle aus Vorwissen (PDG 2024, Planck 2018), für eine Abschätzung ausreichend, vor Verwendung im Paper prüfen.
- **Ensembles für γ_L:** (a) die 36 Paare aus k218 (Regelraum S von H98); (b) γ_L gleichverteilt auf [1,006; 3,51]; (c) log-gleichverteilt auf
  demselben Bereich; (b) und (c) mit 200 000 Ziehungen, Startwert 235.
- **Berichtet:** Trefferzahl n_obs von DL/ABCK und welche Ziele; Verteilung der Trefferzahlen über die 36 Paare und der Rang von DL/ABCK;
  P(n ≥ n_obs) in (b) und (c); 36 · P als erwartete Zahl gleich guter Paare.
- **Lesart, vorab festgelegt:** Ist 36 · P(n ≥ n_obs) in (b) und (c) unter 0,05, heißt der Befund „seltener als Zufall unter dieser Zählung“;
  liegt es über 0,3, „mit Zufall verträglich“; dazwischen „unentschieden“. Das ist keine Aussage über die Physik, nur über die Zählung.
  Ziele, Formen, Schranken und Ensembles werden nach dem Commit nicht geändert; Zusatzrechnungen werden als nachträglich markiert.
