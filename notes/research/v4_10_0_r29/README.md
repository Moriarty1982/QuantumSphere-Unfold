# v4.10.0-r29: Die Zählregel von M als eine Zahl (Stand nach dem 17.11.)

17. November 2026. Auftrag des Autors: „Runde r29 schreiben“. Die Runde bringt die Arbeiten aus PR #167–#173 in den Companion. Sie steht als Datei
`rounds/v4100_r29_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Keine neue Rechnung, keine H-Nummer, kein
Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r29.1 | isolierter Horizont φ₀ = 0, Punktierungen sind Flusslinien; reelle Felder (EM, Weyl Typ D) auf dem χ-Äquator; (S1′) als Querung passt nicht | `op1_flux_lines_2026_11_17/` |
| r29.2 | ω_T = ln 2 · T_H, ω_M = γ_L ln 2 · T_H; Quasinormal-Quant 4 ln 3 = Schritt der Gewicht-2-Regel nur bei linearem Spektrum; Quasinormal-Auslesung ⇔ γ_L = log₂ 3; 16 Frequenzen, kein Treffer | `op1_readout_frequency_2026_11_17/` |
| r29.3 | Zählgleichung = Moran-Gleichung; D_T 1, D_M 1,8647, D_P 2,1515; M in der Ebene, P nicht; w = 2 größte ganze Kopienzahl; Dimensionsleiter T/M/P = ℝ¹/ℝ²/ℝ³ | `op1_moran_geometry_2026_11_17/` |
| r29.4 | eine Zahl in sechs Gestalten; Paar aus r11.5(b) ist (M, M̄), nicht (M, T) | `op1_one_number_2026_11_17/` |
| r29.5 | Registerbreite: Beobachterlesart φ = sech 2η widerspruchsfrei, Helizitätslesart widerspricht R; Frequenzkette bedingt; 9 Geschwindigkeiten, kein Treffer | `op1_backward_search_2026_11_17/`, `op1_two_readings_2026_11_17/` |
| r29.6 | Sichtung verworfener Ideen; H13, H73 weiter widerlegt; H61–H63 offen; H6 Kriterium C trägt nicht | `review_discarded_ideas_2026_11_17/`, `op4_h6_criterion_c_2026_11_17/` |
| r29.7 | Vergleich mit anderen Vereinheitlichungsversuchen (Lesart) | `toe_comparison_2026_11_17/` |
| Rücknahmen | H6-Grund aus den Frame-Abbildungen; Boost-Lesart der Frequenz; Frequenzbedingung als Aussage über das M-Register | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3981`): 0 Kandidaten in den Zeilen 3981–4133.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX): 1461 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r29 im Inhaltsverzeichnis, Text ab Seite 1455.

OP1–OP5, C5, C6/T2 offen.
