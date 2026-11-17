# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 17.11.2026 (Claude Opus 5.5)

### Öffentlich: v5.2.0
- **v5.2.0**, veröffentlicht am 17.11.2026, Version-DOI **10.5281/zenodo.24294648**, Record https://zenodo.org/records/24294648;
  Concept-DOI 10.5281/zenodo.19210728; Vorgänger v5.1.0 (10.5281/zenodo.24237112). Vollausgabe 1457 Seiten, Physik-Paper 30.
- Paketquellstand 8fb6e9378f6e6789697c60d3ba8b748cc2b56de6, **Tag `v5.2.0`**, GitHub-Release gesetzt (latest).
- Läufe: Reservierung 43978639426, Paarbau 43978954178, Upload 43981330807 (Vorschau-Prüfung scheitert wie bei v5.1.0,
  weil das Werkzeug die Vorschau nicht setzt; der Autor setzt sie auf Zenodo).
- Nach der Veröffentlichung geprüft: 8 Dateien MD5-gleich mit dem Paket, PDFs gleich dem Paarbau, Vorschau = Vollausgabe,
  Version v5.2.0, isNewVersionOf v5.1.0. Release-Notiz `release/v5.2.0/README.md`.
- Inhalt: Runden v4.10.0-r15 bis r28; im Physik-Paper Abschnitt 5.8 „Where the missing number comes from“ und ein Satz im Ausblick.

### GitHub
- `main` nach **PR #174** (Runde v4.10.0-r29), davor **PR #173** (OP1 Rückwärtssuche, beide Lesarten der Registerbreite), davor **PR #172** (OP1 eine Zahl in sechs Gestalten, Paar (M, M̄)), davor **PR #171** (OP1 Dimensionsleiter, Spannung zu P), davor **PR #170** (OP1 Moran-Lesart), davor **PR #169** (Sichtung verworfener Ideen, TOE-Vergleich, H6 Kriterium C), davor **PR #168** (OP1 Auslesefrequenz von M), davor **PR #167** (012b296, OP1 Querungen oder Flusslinien), **PR #166** (9a07c7b, Release v5.2.0), …
  Zweige gelöscht. Keine offenen PRs. CI nach #166 grün.
- Issues #17, #10 (OP1), #131 (OP3) nachgezogen.

### Forschung
- **Letzte Runde:** v4.10.0-r29 (Zählregel von M als eine Zahl, r29.1–r29.7, drei Rücknahmen; PR #174; Kandidat 1461 Seiten, Linter 0).
  Davor r28 (in v5.2.0), r27 (PR #156). Runden r29 ff. sind nicht veröffentlicht (öffentlich: v5.2.0 bis r28).
- **Hypothesen:** zuletzt vergeben **H111** (k233, widerlegt). Frei: **H112, k234**.
- **Inhaltlicher Stand:** Die Phase ist im Träger starr (H106–H111 widerlegt); der bewachte Kern (φ = π/4 − γ_M/2) entgeht
  dem über die Verbindung, seine Größe kommt nur aus der Zählregel von M (Gewicht 2, gewählt). H102 (m_τ = 1777,134 MeV,
  +2,3σ) prüft Kernlesart, U(1)-Zählung und Spektrum √(j(j+1)) gemeinsam; entschieden mit der nächsten PDG-Ausgabe.
  Register-Entropie erklärt P (2j+1) und R, nicht M; Regel von M = reine Stränge mit unbekanntem Port.
- **Flusslinien (17.11., PR #167, `notes/research/op1_flux_lines_2026_11_17/`, Erkundung):** Am isolierten Horizont φ₀ = 0
  (Eder–Sahlmann 1801.00747): keine Strahlung quert, Punktierungen sind Flusslinien. Reelle Felder (EM und Weyl, auch Typ D)
  liegen auf der χ-Kugel bei P; Breite von M und Ports nur mit Frequenz ω > 0. (S1′) als Querung passt nicht zum isolierten
  Horizont. Kein blinder H112 auf dieser Linie (Autor: „Erkundung statt Test“).
- **Auslesefrequenz (17.11., PR #168, `notes/research/op1_readout_frequency_2026_11_17/`, Erkundung):** Quasinormal-Quant 4 ln 3
  (Dreyer) = kleinster Schritt der Gewicht-2-Regel nur bei linearem Spektrum (γ = ln 3/π). Spektrumfrei: ω_M/ω_T = γ_L; QNM-Auslesung
  von M ⇔ γ_L = log₂ 3 (Ω_M 0,226, widerspricht H98). Datenpaarung ⇒ ω_M = 1,2925·T_H; Quellensuche mit vorab festgelegter Liste
  (9fce085, 16 Kandidaten): 0 Treffer, nächster 2η (4,4 %). Suchrichtung Frequenz für Schwarzschild ausgeschöpft.
- **Sichtung und TOE-Vergleich (17.11., PR #169):** `notes/research/review_discarded_ideas_2026_11_17/` (35 widerlegte Tests gegen zehn berichtigte
  Annahmen; H13, H73 nachgerechnet weiter widerlegt; H61–H63 offen statt verneint; P2 als Frequenzbedingung neu fassbar; Kandidat H6 C geprüft
  und zurückgenommen, `op4_h6_criterion_c_2026_11_17/`: Vorzeichen-Symmetrie = Kleinsche Gruppe im Torus von Stab(e₇), nur Parallele A₄/S₄).
  `toe_comparison_2026_11_17/`: Bruchstellen anderer TOEs; Lesart: Breite zwischen reell (Äquator) und selbstdual (Pol), M bei b = 1/γ_L.
  Quellen teils Vorwissen, vor Verwendung im Paper prüfen.
- **Moran-Lesart (17.11., PR #170, `notes/research/op1_moran_geometry_2026_11_17/`, Erkundung, nicht blind):** Zählgleichung in T-Einheiten =
  Moran-Gleichung Σ g r^D = 1, r_j = 2^{−a(j)/a(½)}; Frame-Faktoren = Hausdorff-Dimensionen (T 1, M 1,8647 = γ_L, P 2,1515; linear M = log₂ 3).
  M-Fraktal liegt in der Ebene (explizite Anordnung), P nicht (Σ r² = 1,199). 2 = größte ganze Kopienzahl je SU(2)-Skala in der Ebene (3: D 2,27).
  Nachträgliches Prinzip: reichstes selbstähnliches Gebilde mit ganzer Kopienzahl auf der Fläche → M, γ_L, b_M ohne freien Parameter.
  Offen: ein blinder Test (Dimension 1,8647 an anderer Stelle messbar?).
- **Dimensionsleiter und Spannung zu P (17.11., PR #171, Nachträge in derselben Notiz):** Im Regelraum von H98 reichste Regel in ℝ¹ = T, ℝ² = M,
  ℝ³ = P (T ⊆ M ⊆ P als 1 ⊂ 2 ⊂ 3). Aus der Moran-Lesart allein kein blinder Test. Spannung zu P aufgelöst: Registerzählung passt erst ab
  b > b_c ≈ 0,25–0,35 auf eine Fläche; Kette Flächenauslesung ⇒ b > b_c ⇒ Frequenz ⇒ nicht statisch; statischer Horizont liest wie P.
  Offene Kernfrage OP1: woher die Frequenz der Auslesung M kommt.
- **Eine Zahl (17.11., PR #172, `notes/research/op1_one_number_2026_11_17/`):** γ_L = γ_M/γ_T = D_M = ω_M/ω_T = cosh 2η = 1/b_M.
  Beobachterpaar aus r11.5(b) geprüft: (M, M̄), nicht (M, T) (Boost erhält s; T = J_B-Bild, Tachyonseite, iπ/2). Boost-Lesart der Frequenz
  zurückgenommen; γ_L = Lorentz-Faktor (M, M̄) = u(M)/u(R). Frequenz von M weiter offen.
- **Rückwärtssuche und zwei Lesarten (17.11., PR #173, `notes/research/op1_backward_search_2026_11_17/`, `op1_two_readings_2026_11_17/`):**
  Registerbreite b: (B) Beobachtergröße φ = sech 2η gibt alle Definitionen wieder (R E∥B φ = 1, P 0, M/T 0,5363, Vorzeichen Re s); (H) Helizitäts-
  breite widerspricht R. Frequenzkette (Flusslinien, Auslesefrequenz, Spannung zu P) als nur unter (H) gültig vermerkt; Moran-Lesart unberührt.
  **OP1 jetzt:** warum bewegt sich der Beobachter M mit β_sym = 0,5494 relativ zum Ruheframe des Feldes (T6, H48)? 9 Horizontgeschwindigkeiten
  (Liste 4677bc1): 0 Treffer, nächste 1/√3 (5,1 %). Ungeprüft für (H): Kerr/Superradianz.
- **Möglicher nächster Schritt:** OP1 steht wieder bei „warum Gewicht 2 im Spektrum √(j(j+1))“; ungeprüft: geladene/rotierende
  Horizonte, Graukörper. Ggf. OP1 ruhen lassen (Autorentscheidung). Test nur mit Vorab-Notiz (H112). Nächste Version erst mit
  genug Stoff für beide Ausgaben.
- OP1–OP5, C5, C6/T2 offen. Notizen unter `notes/research/op1_*_2026_11_1[67]/`, `op3_*_2026_11_16/`, `v4_10_0_r28/`.
