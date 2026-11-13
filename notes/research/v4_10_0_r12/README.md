# v4.10.0-r12: Statusvermerke zu geerbten Koide- und Generationsaussagen

13. November 2026. Autorenauftrag: „erst die Fäden“ (Faden „Statusvermerke in einer neuen Runde“ aus der Übergabe).
Runde als Datei `rounds/v4100_r12_round.tex`, angehängt an `sources/research/parts/v4100-post-release-layers.tex`.
Kein neuer Test, keine neue H-Nummer; Guards unverändert.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r12.1 | Teil 17 nennt den Koide-Block „strukturell geschlossen“ und OP3 kein Hauptproblem mehr: überholt, OP3 offen | Status zu thm:koide-triolic, v4.8.0-r11 (H1), v4.11-Abschnitt, v5-Stringfrage |
| r12.2 | Bemerkung „The 2/3 factor is everywhere“: Liste von Zufällen, kein Ergebnis (Ω_Λ ≈ 0,685; K = 2/3 als ρ² = 1/2) | `op3_gram_eigen_readout_2026_11_13.md` |
| r12.3 | rem:koide-mass-discrepancy: Zuschreibung an β_sym hinfällig (Phasenformel mit 300–400σ ausgeschlossen, r09) | Status zu thm:koide-triolic |
| r12.4 | r33-Labels μ_i nicht Q_em-invariant; kein Träger gibt Zahl drei und Massen; Rand des Koide-Bogens = Oktanten-Tripel (exakt), kein neutraler nativer Träger | `op3_generation_carrier_review_2026_11_13.md`, `op3_eta_form_search_2026_11_13.md`, `op3_hopf_octant_2026_11_13.md`, `op3_neutral_su2_octant_2026_11_13.md`, `op3_sedenion_reference_2026_11_13.md` |
| r12.5 | H99 (+1,31σ / +1,80σ, verträglich, nicht blind); H100 vorab (drei Werte für R); Erkundungen zur Phase π/4 | `predictions/`, `op3_neutrino_phase_candidates_2026_11_13.md`, `op3_eta_form_search_2026_11_13.md` |

Prüfung: Guard-Linter auf die neue Runde (ab Zeile 1502 der Schichtdatei) 0 Treffer; Kandidaten-Build siehe PR.
Die lokale Monolith-Fassung und das Bündel aus der Anleitung entfallen: Der lokale Ordner ist seit dem 12.11. ein
Klon des Repos (`main`), die Historie ist dieselbe.
