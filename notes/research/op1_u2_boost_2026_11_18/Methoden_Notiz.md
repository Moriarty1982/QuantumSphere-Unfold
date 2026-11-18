# OP1: Liest ein geboosteter Beobachter an einer Punktierung nur Extremzustände? (Verfahren, vor der Rechnung festgelegt)

**Stand:** 18. November 2026, vor der Rechnung committet. **Erkundung, nicht blind:** Dass die Extremzustände am wenigsten gestört werden, folgt
analytisch aus dem Faktor √((j+1)² − m²) der Boost-Matrixelemente (unten). Offen ist nur, ob die Trennung **scharf** ist. Keine H-Nummer.
Auftrag des Autors: „U2 unter (B) prüfen“ (Angriffspunkt aus `../op1_common_premise_2026_11_18/`).

## Vorwissen geprüft
- `../op1_common_premise_2026_11_18/`: U2 („M liest nur |j, ±j⟩“) ist der gemeinsame Kern dreier Wege für das Gewicht 2.
- `../op1_two_readings_2026_11_17/`: Lesart (B), M ist gegen R mit η = artanh β_sym geboostet (φ = sech 2η).
- Wiki Forschungsstand, Nachtrag Literatur (EPRL arXiv:0711.0146, Bianchi arXiv:1204.5122): Boosts mischen in γ-einfachen Darstellungen die Spins
  (K = γL nur schwach); Bianchis Quanten-Rindler-Horizont hat Facetten |j, +j⟩ längs der Normalen.
- `../op1_s1_check_2026_11_16/`: U2 über masselose Helizität (S1′); `../v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md`: U2 über Robertson-Sättigung.
- `../v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md`: Über erstes Gesetz und Unruh zählen M und T gleich.

## Aufbau
- Punktierung als SL(2,ℂ)-Hauptreihe (k, ρ), Basis |j, m⟩, j ≥ k, Spin der Punktierung j = k (EPRL: Rand im niedrigsten Block).
- Boost entlang der Horizontnormalen (Achse 3), Naimark-Form: K₃|j,m⟩ = α_j √(j²−m²)|j−1,m⟩ + kρ m/(j(j+1)) |j,m⟩ − α_{j+1} √((j+1)²−m²)|j+1,m⟩,
  α_j = (i/j) √((j²−k²)(j²+ρ²)/(4j²−1)). K₃ erhält m; die Leckage aus dem Block j = k geht nur nach oben.
- γ = γ_M = 0,237533 (DL); ρ = γ(k+1) (exakte Simplizität im Block j = k) und ρ = γk (EPRL) als zweite Einstellung.
- Rapidität η_M = artanh 0,549412 = 0,6173; zum Vergleich η = 0,2 und 1,5. k = ½ … 3, alle m.
- Größen: Dispersion D_m = ⟨(K₃ − γL₃)²⟩ im Zustand |k, m⟩; Verbleib P_m(η) = |⟨k,m| e^{−iηK₃} |k,m⟩|² (Abschneiden bei j ≤ k + 60, Konvergenz
  mit k + 120 geprüft).
- Transversale Boosts: Die Summe der Leckage über die drei Komponenten ist nach Wigner–Eckart von m unabhängig (Vektoroperator); nur die
  Normalkomponente kann Extremzustände auszeichnen. Wird nicht gerechnet, nur festgehalten.

## Lesart, vorab festgelegt
- **Scharf:** bei η_M für alle k gilt P_{±k} ≥ 0,9 und P_m ≤ 0,5 für |m| < k. Dann löst der Beobachter M praktisch nur Extremzustände auf; U2 folgt
  aus (B) plus Boost entlang der Normalen.
- **Graduell:** Extremzustände haben das größte P, aber die Schranken werden verfehlt. Dann zeichnet (B) die Extremzustände nur aus, wählt sie nicht;
  U2 bräuchte eine zusätzliche Auswahlregel.
- **Gegen U2:** Ein Zustand mit |m| < k hat ein größeres P als die Extremzustände.
Skript `k236_u2_boost.py`, Ausgabe `run/k236_stdout.txt`. Schranken und Einstellungen werden nach dem Commit nicht geändert.
