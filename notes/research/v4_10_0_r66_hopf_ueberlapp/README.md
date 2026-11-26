# v4.10.0-r66: β_sym als Überlapp des Hopf-Zustands mit dem Gegenpol (26.11.2026)

Auftrag des Autors vom 26.11.2026: die Abbildung aus H164 als Companion-Runde. Die Runde rechnet nichts Neues. Sie hält H164 (k355) und den Teil K-e von H161
(k352) fest. Text: `rounds/v4100_r66_round.tex`, angehängt an `sources/research/parts/v4100-post-release-layers.tex`.

| Eintrag | Inhalt | Test, Skript | Prüfung |
|---|---|---|---|
| r66.1 | Überlapp zweier Lichtrichtungen = Geschwindigkeit des Systems, in dem sie gegenüberliegen | H161 K-e (bestätigt, nicht blind), k352 | Qiskit, sympy, Wolfram exakt |
| r66.2 | β_sym = \|⟨K₁\|S⟩\|; Boost mit β_sym, Rapidität ε der Maske, γ_L als relativer Faktor | H164 K-a, K-b (bestätigt, nicht blind), k355 | sympy und Wolfram exakt |
| r66.3 | Mischung der zwei Auslesen ist nicht der Materie-Zustand | H164 K-c (widerlegt, wie vorhergesagt) | exakt |
| r66.4 | θ_H → 2α mit cos 2α = 1/γ_L; Besetzungen (1, β²)/(1+β²) | H164 K-d (Wortlaut widerlegt, Kern bestätigt) | Wolfram: Differenzen exakt null |
| r66.5 | Hopf-Wert und Tetraeder (vier gleichberechtigte Auslesen) | Erkundung | — |

Präzisierungen (ohne ältere Runden umzuschreiben): Statusvermerk zu `thm:bsym-hopf` (r61) um die Abbildung ergänzt; r27 (2α ist das Bild des Hopf-Winkels);
v4.9.0-r24.3 (Bloch-Länge sech 2ε).

Gesetzt und benannt: Lesart C (Hopf-Sphäre als Himmelskugel von Lichtrichtungen), der Gegenpol als zweite Auslese, das Dephasieren.
Unverändert: β_sym ist Eingabe, OP1 offen. Guards: Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1), β₄ = 1/256. OP1–OP5, C5, C6/T2 offen.

Skripte und Ausgaben: `notes/research/beta_sym_ueberlapp_h164/`, `notes/research/gedankenexperiment_proben_2026_11_26/`.
Nicht in dieser Runde: Test H165 (`notes/research/op1_herkunft_beta_sym_h165/`); er steht nur als Notiz.
