# v4.10.0-r74: Der Wert des Lepton-Winkels φ bleibt offen; φ trägt den Versatz, q nur das Vorzeichen; der φ-Strang ruht

Festhalte-Runde ohne neue Rechnung, auf Entscheidung des Autors vom 28.11.2026 (Vorbereitung des Releases v5.6.0). Sie hält die Tests H228–H236
(k442–k448, k450, k451) und die Erkundung k449 fest. Autorentscheidung 28.11.2026, 15:41: φ = 0,0395773 bleibt offen (gemessene Eingabe), der
φ-Strang ruht; H235 war der eine Zusatzversuch nach k449, H236 klärt die Buchführung. Die Tests H173–H212 stehen weiterhin in keiner Runde.

| Theoremlet | Test | Inhalt | Urteil |
|---|---|---|---|
| r74.1 | H228 (k442) | φ weder Grenzwert einer Schleife (111 110 Wörter, kein Treffer) noch natürlicher Zwischenstand des Flusses (t_x/τ = 0,1321, keine Uhr) | widerlegt |
| r74.2 | H229 (k443) | J bei Ordnung 6 gelockert (λN²): Zweig aus Stabilität, Minima nur π/12, π/6, π/8; Lockerung nicht übernommen, Vorzeichen bleibt Setzung | widerlegt (für φ) |
| r74.3 | H230 (k444) | Symmetriepunkt π/8 aus R nach M übertragen: kein Frame-Bild trifft x; Schritt abgehakt | widerlegt |
| r74.4 | H231 (k445) | Expansion als Uhr: μ* = 0,9721 rollt heute, Drift von m_e 2,7·10⁻¹⁰/Jahr gegen Atomuhren | widerlegt |
| r74.5 | H232 (k446) | an jedem Gleichgewicht o_Im + o_Re = 2φ (exakt); symmetrischer Term macht x nur lokal minimal | widerlegt |
| r74.6 | H233 (k447) | 8 Stellungen mit Halbierung bis 8 Bit: φ 392σ neben jedem Gitterpunkt | widerlegt |
| r74.7 | H234 (k448) | keine gemeinsame Feinstufe (ε = φ: 36σ; freies ε: p = 0,74) | widerlegt |
| r74.8 | k449 | inneres/äußeres Feld, Casimir-Spalt: HS(−1), HS(0), HS(1) als Lesart; −7/8; stetige Phase gesetzt | Erkundung, nicht blind |
| r74.9 | H235 (k450) | Casimir-Verdrehung 2:1 bricht den Tausch, x_ν,pred +9,2σ, x nur lokal | widerlegt |
| r74.10 | H236 (k451) | φ trägt den Versatz, q → 0⁻ (2σ: q ∈ [−0,029; 0]); kein Urteil H221–H235 kippt; H227 unverändert | trägt |
| r74.D | — | Autorentscheidung 28.11., 15:41: φ offen, Strang ruht | Entscheidung |

Bilanz: Die offene Wahl sitzt seit r73.4 im Wert von φ und hat sich nicht bewegt. Hergeleitet: φ = Mittelwert der Sektor-Versätze an jedem
Gleichgewicht (H232), φ-abhängige Brecher ändern die Neutrino-Vorhersage nicht (H235). Gesetzt: Zweigvorzeichen (r73.6; H229 würde es durch eine
Regeländerung ersetzen, nicht übernommen), K = ⅔, Brannen-Form, H99, Skalen μ_e, μ_ν; q nur als Vorzeichen (H236). Die Doppelzählung q/φ entstand
in einer gewählten Zerlegung und ist mit H236 aufgelöst. Weggabel „Gleichgewichtswert oder Anfangsbedingung“ dem Autor vorgelegt; er lässt φ offen.

Namen nach r69 (Ruheframe R, Materie-Frame M, Dual-Frame T, Lichtpunkt P; Re-/Im-Sektor).
Rundentext: `rounds/v4100_r74_round.tex` (wörtlich angehängt an `sources/research/parts/v4100-post-release-layers.tex`).
Werkzeuge: keine neue Rechnung; die zitierten Tests je mit Python und Wolfram-Gegenprobe, Qiskit nicht einschlägig.
Guard-Prüfung `tools/qs.py guards`: 0 Kandidaten. Guards unverändert.
