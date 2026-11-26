# v4.10.0-r68: Nachrechnung der von β_sym abhängigen Zahlen beim Bezugswert (26.11.2026)

Erkundung k358 als Runde, damit der Companion die maßgebliche Fassung ist (Artikel und Preprint nennen die Nachrechnung). Kein Test, keine
Vorab-Notiz, kein neuer Messwert. Text: `rounds/v4100_r68_round.tex`, angehängt an `sources/research/parts/v4100-post-release-layers.tex`.

| Eintrag | Inhalt | Skript | Prüfung |
|---|---|---|---|
| r68.1 | Empfindlichkeiten d ln X/d ln β; stark reagieren nur Hopf-Lücke (−20,7) und γ_L⁵ (6,64) | k358 | mpmath; Wolfram symbolisch (k358d) |
| r68.2 | Abstände zu den Messwerten des Bestands; kein Urteil kippt; m_W schärfste Stelle (2σ: 0,54907 ≤ β ≤ 0,54978) | k358 | mpmath, Wolfram |
| r68.3 | H102 hängt an γ_M allein; d m_τ/d γ_M = 2396 MeV; registriert mit dem Wert der Zählregel (+2,27σ) | k358 mit k224 | numpy/scipy |
| r68.4 | Maskenscans: H46 Trefferzahl 120 → 168 (Rasterwirkung), Fenster unverändert; H134 Urteile unverändert | k358b, k358c | unveränderter Code von k105, k263 |

Guards: Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1), β₄ = 1/256. OP1–OP5, C5, C6/T2 offen.
Notiz, Skripte und Ausgaben: `notes/research/op1_herkunft_beta_sym_h165/`. Vergeben: r68. Nächste freie Runde: r69.
