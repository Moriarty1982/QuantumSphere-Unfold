# v4.10.0-r67: Die Zählregel als Postulat; β_sym als berechnete Zahl (26.11.2026)

Entscheidung des Autors vom 26.11.2026 (11:18 UTC): Die Zählregel wird als Postulat angenommen, im selben Sinn wie die Frame-Gleichberechtigung (r63.7):
benannt, nicht hergeleitet. Text: `rounds/v4100_r67_round.tex`, angehängt an `sources/research/parts/v4100-post-release-layers.tex`.

| Eintrag | Inhalt | Test, Skript | Prüfung |
|---|---|---|---|
| r67.P | Zählpostulat: (C1) Gewicht 2 je Spin, (C2) Fläche √(j(j+1)), (C3) T zählt nur j = ½ mit einem Bit; Zuordnung zu M und T | Postulat | — |
| r67.1 | γ_L = Wurzel von Σ 2^(1 − γ_L·c_k) = 1 = 1,8646997646; β_sym = 0,5494056410; mit j + ½ exakt 1/√3 | H165 K-a (nicht blind), k356 | mpmath und Wolfram, 39 Stellen |
| r67.2 | Bezugswert ab r67; Tabelle der r66-Zahlen beim Bezugswert; kein Urteil kippt | Erkundung k357 | mpmath |
| r67.3 | Überlapp-Schließung erzwingt den Hopf-Wert; γ_L = 1 + Σ 2β^{4j} (nachträglich) | H165 K-b (widerlegt, wie vorhergesagt), k356 | Qiskit, sympy, Wolfram symbolisch |
| r67.4 | Zahlenkandidaten ohne Identität; Kegel des Spins ½ | H165 K-c, K-d | 30 Stellen |

Was sich ändert: β_sym ist nicht mehr „Verhältnis zweier Literaturwerte“, sondern die aus dem Postulat berechnete Zahl. Was sich nicht ändert: OP1 bleibt offen,
jetzt in der Form „leite das Zählpostulat her“. Ein Postulat schließt kein offenes Problem.

Geprüft vor dem Nachziehen des Werts (k357): Unterschied 1,05·10⁻⁴ in β, 1,4·10⁻⁴ in γ_L, 7·10⁻⁴ in γ_L⁵. Die Tests mit Datenvergleich (H96, m_W aus r08/k218,
H98, H102) rechnen schon mit dem ungerundeten γ_M; das Leptonfenster [0,545; 0,570] enthält beide Werte. Ältere Runden behalten ihre gedruckten Zahlen
(append-only), ebenso Release-Stände und gespeicherte Rechenausgaben. Nachgezogen sind: der Statusvermerk zu `thm:bsym-hopf` im Haupttext und das Wiki.

Guards: Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1), β₄ = 1/256. OP1–OP5, C5, C6/T2 offen.
Skripte und Ausgaben: `notes/research/op1_herkunft_beta_sym_h165/`.
