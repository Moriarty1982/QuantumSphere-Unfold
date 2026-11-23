# v4.10.0-r56: Zeitlich geordnete Oktant-Auslese auf einer Punktierung vom Spin j (H123, Q1a) (Stand 23.11.)

23. November 2026. Faden „Auslesegesetz Q1a als H123 testen“ (Anlass: r55.6 und Übergabe, H123 für Q1a vorgemerkt); Freigabe des Autors
„Committen und rechnen“. Hypothese H123, Vorab-Notiz `llm/Vorab_Notiz_H123_Zeitliche_Oktantauslese.md` (1a4662ef), Skripte
`llm/h123_temporal_octant.wl` (Wolfram exakt, Ausgabe `llm/h123_temporal_octant.txt`) und `llm/k242_h123_qiskit_cycle_test.py` (Qiskit-Zyklustest,
Ausgabe `llm/k242_out.txt`), Ergebnis `llm/Ergebnis_H123_Zeitliche_Oktantauslese.md`. Teilweise nicht blind. Die Runde ist die Quelle für die
Ergänzungen im Physik-Paper (`v5_expanded_limits.tex`) und im deutschen Preprint (5.6, Anhang C).

| Eintrag | Inhalt |
|---|---|
| r56.1 | H123a bestätigt (exakt, nicht blind): B_τ = 2^{−3j} e^{iτεjπ/2} für j ≤ 20, alle 8 Tripel, beide τ; umgekehrte Reihenfolge und Θ_j konjugieren, zusammen bleibt B fest (r31.2 auf Spin j); Qiskit j = ½, 1, 2: Abweichung 6,6·10⁻¹⁶ |
| r56.2 | H123b widerlegt (erwartet): gleicher Betrag, aber getrennt nur für j ∉ 2ℕ; für j = 2, 4, … ist B(+j) = B(−j) = (−1)^{j/2} 2^{−3j}. H123c bestätigt: Eigenwert von R_j trennt nur halbzahlige j |
| r56.3 | H123d trägt nicht: Zählregel mit Gewicht 1 auf j ∈ 2ℕ gibt γ_M′ = 0,23412, γ_L′ = 1,83793, β′ = 0,54338, m_W′ = 80,0994 GeV (−20,3σ), Ω_M′ = 0,2953 (−0,26σ) |
| r56.4 | Lesart: Oktantvorzeichen und Gewicht 2 nicht derselbe Datensatz in dieser Form; τ weiter gesetzt; U2-Auslese bräuchte Raumwinkel mit jΩ ∉ πℤ für alle j; nachträglich: gebogenes Dreieck (≈ ⅔) erfüllt das, ist aber aus γ_M gebaut; Auslöser 3 von I1 getroffen |

Runde als Datei: `rounds/v4100_r56_round.tex`. Guard-Linter (`tools/qs.py guards`) über die neue Schicht: 0 Treffer. Kein lokaler LaTeX-Build
(keine TeX-Installation in dieser Sitzung); Build über CI.

OP1–OP5, C5, C6/T2 und Q1a offen; kein Guard berührt.
