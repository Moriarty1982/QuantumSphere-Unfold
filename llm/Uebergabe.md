# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 18.11.2026 (Claude Opus 5.5)

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
- `main` nach **PR #184** (Einheitenliste), davor **PR #183** (J_B-Kandidat), davor **PR #182** (T-Regel), davor **PR #181** (U2 unter (B)), davor **PR #180** (OP1 gemeinsame Prämisse), davor **PR #179** (Zufallsabschätzung), davor **PR #178** (I5 zurückgestellt), davor **PR #177** (H112 vorab), davor **PR #176** (OP4-Vorschau), davor **PR #175** (OP4-Bestandsaufnahme), davor **PR #174** (Runde v4.10.0-r29), davor **PR #173** (OP1 Rückwärtssuche, beide Lesarten der Registerbreite), davor **PR #172** (OP1 eine Zahl in sechs Gestalten, Paar (M, M̄)), davor **PR #171** (OP1 Dimensionsleiter, Spannung zu P), davor **PR #170** (OP1 Moran-Lesart), davor **PR #169** (Sichtung verworfener Ideen, TOE-Vergleich, H6 Kriterium C), davor **PR #168** (OP1 Auslesefrequenz von M), davor **PR #167** (012b296, OP1 Querungen oder Flusslinien), **PR #166** (9a07c7b, Release v5.2.0), …
  Zweige gelöscht. CI nach #166 grün.
- **PR #177 gemergt** (Squash 9b369c5; Vorab-Commit 42bebf0 per ours-Merge 2b6a1b1 von main erreichbar). Zweig gelöscht.
- **PR #178 gemergt** (5afb5d0, Merge-Commit): I5 Außenwirkung in `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md`. Zweig gelöscht. #17 nachgezogen.
- **PR #179 gemergt** (9407d90, Merge-Commit; Methode 8557ed7 erreichbar): Zufallsabschätzung. Zweig gelöscht. Keine offenen PRs.
  Issues #17, #10 nachgezogen.
- **PR #181 gemergt** (U2 unter (B), Methode 4ee7618 erreichbar). Zweig gelöscht. Keine offenen PRs. #17, #10 nachgezogen. **Befund:** graduell; Boost mit η_M entlang der Normalen bevorzugt |k, ±k⟩ (P 0,74–0,82 gegen 0,49–0,73), wählt sie nicht.
- **PR #182 gemergt** (T-Regel). Zweig gelöscht. Keine offenen PRs. #17, #10 nachgezogen.
- **PR #183 gemergt** (J_B-Kandidat). Zweig gelöscht. Keine offenen PRs. #17, #10 nachgezogen. **Befund:** entfällt; J_B² = −1 wählt Kramers (unter (A), schon 15.11.), jedes j oder j = 1, 3, 5 (als Dualität), nie allein j = ½.
- **PR #184 gemergt** (Einheitenliste, Liste c64caff erreichbar). Zweig gelöscht. Keine offenen PRs. #17, #10 nachgezogen. **Befund:** 0 von 47 Einheiten im Fenster [γ_T; γ_P/2), erwartet 0,94; Kandidat 2 entfällt, T-Regel ohne datenfreien Grund.
- **Offen: PR #185** (Zweig `research/op1-flaechenquant-boost`): Flächenquant unter Boosts, Literatur Rovelli–Speziale (gr-qc/0205108).
  Wartet auf „PR 185 mergen“; danach #17, #10 nachziehen. **Befund:** Unitäre Boosts erhalten das Flächenspektrum; das frame-abhängige Flächenquant
  aus r10 braucht eine nicht-unitäre Frame-Abbildung (einzige Kandidatin J_B mit iπ/2) oder γ_T als Mittelwert (zirkulär).
  **Nächster Schritt (Vorschlag):** prüfen, ob J_B (imaginäre Rapidität iπ/2) auf dem Flächenoperator nicht-unitär wirkt und das Spektrum skaliert;
  sonst OP1 ruhen lassen.
  **Befund:** fünf Gründe für j = ½ in T, keiner datenfrei tragfähig; Dimensionsleiter gilt nur für Einheit γ₀ ∈ [1; 1,0757) · γ_T, für T also im Kreis.
  Ungeprüfte Kandidaten: J_B wählt Dubletts mit J_B² = −1; unabhängige Einheit im Fenster (vorab festgelegte Liste).
  U2 folgt aus (B) allein nicht; scharf erst in der masselosen Grenze.
- **PR #180 gemergt** (OP1 gemeinsame Prämisse, `notes/research/op1_common_premise_2026_11_18/`). Zweig gelöscht. Keine offenen PRs. #17, #10 nachgezogen.
- **Befund 18.11. (gemeinsame Prämisse):** keine einzelne gemeinsame Prämisse; Kern U2 für M (drei Wege, Zustände |j, ±j⟩), „alle Spins“ nur gesetzt, T-Regel mit fünf
  Gründen. **Nächster Schritt (Vorschlag):** U2 unter (B) erledigt (graduell). T-Regel erledigt (PR #182 gemergt). J_B-Kandidat entfällt (PR #183 gemergt). Einheitenliste ohne Treffer (PR #184 gemergt). Beide T-Kandidaten erledigt; Vorschlag: OP1 ruhen lassen bis H9/H15/H96/H102/H112 entschieden.
  Issues #17, #10, #11 nachgezogen.
- Issues #17, #10 (OP1), #131 (OP3) nachgezogen.

### Forschung
- **Letzte Runde:** v4.10.0-r29 (Zählregel von M als eine Zahl, r29.1–r29.7, drei Rücknahmen; PR #174; Kandidat 1461 Seiten, Linter 0).
  Davor r28 (in v5.2.0), r27 (PR #156). Runden r29 ff. sind nicht veröffentlicht (öffentlich: v5.2.0 bis r28).
- **Hypothesen:** zuletzt vergeben **H112** (k234, offen, vorab 42bebf0, PR #177 gemergt). Frei: **H113, k240** (k235 Zufallsabschätzung, k236 U2-Boost, k237 Leiter-Einheit, k238 J_B-Quadrat, k239 Einheitenliste).
- **Zufallsabschätzung (18.11., PR #179 gemergt, Erkundung, nicht blind):** Dreifachtreffer von DL/ABCK (sin²θ₁₂, cot θ_W, Ω_m) unter festem Katalog
  (16 Ziele, 8 Formen, 2σ) **mit Zufall verträglich**: über 36 Paare 0,64–0,81 gleich gute erwartet; nur bei datenfrei feststehendem Paar ≈ 2 %.
  Teil A: Σp = 1,31 gegen 4 Treffer, P(4/4) = 0,004 als Untergrenze. Nachträglich: Ziele um 0,30 zu 73 % gekoppelt.
  Folge: Gewicht hängt an datenfreier Begründung der Zuordnung (OP1) und an vorab festgelegten Vorhersagen.
- **H112 (17.11., Vorab-Notiz `notes/research/predictions/Vorab_Notiz_H112_Ueberbestimmung_beta.md`):** sin²θ₁₂ cos²θ₁₃ (Prüfdaten H9) = Ω_m
  (Prüfdaten H96), ohne den Wert 0,30185; |z| ≥ 3 widerlegt, Frist 31.12.2029. Schwacher Test (widerlegt erst ab |Δβ²| ≳ 0,022), offen benannt.
  Vorschau (kein Test): alle vier Paarungen verträglich. Auswertung: `python k234_test_h112.py S12 S12+ S12- S13 OM OM+ OM-`, sobald beide Daten da sind.
- **Offene Vorschläge an den Autor (17.11., noch nicht entschieden):**
  1. ~~**H112 Überbestimmungstest:**~~ erledigt (Vorab-Notiz, PR #177 gemergt); offen bleiben 2 und 3. vorab festlegen, dass β aus der nächsten JUNO-Messung von θ₁₂ (β² = sin²θ₁₂ cos²θ₁₃) und β aus dem
     nächsten Ω_m (Euclid/DESI DR3, β² = Ω_M) innerhalb der gemeinsamen Fehler übereinstimmen; prüft „eine Zahl“ ohne den exakten Wert der
     Zählregel. Heutiger Stand (kein Test): NuFIT 6.1 0,5494, JUNO 2026 0,5448, DESI DR2 0,5454, Planck 0,5615 (±0,006–0,008).
  2. ~~**Außenwirkung:**~~ vom Autor zurückgestellt (17.11.), als I5 mit markiertem Material und Auslösern (PR #178 gemergt); Vorschlag 3 erledigt (PR #179). Keine offenen Vorschläge mehr. Neuheit prüfen (Moran-Lesart der Zählgleichung; Koide-Phase als Oktant minus γ_M/2, Brannen beachten), dann
     2–3 kurze englische Notizen mit Standardbegriffen und je einem Test.
  3. **Zufallsabschätzung:** Zahl der Auswahlmöglichkeiten hinter den Treffern zählen und die Zufallswahrscheinlichkeit abschätzen.
- **OP4 (17.11., PR #175, `notes/research/op4_status_audit_2026_11_17/`):** Bestandsaufnahme gegen Datenstand (NuFIT v6.1 = neueste, Daten
  Nov. 2025; JUNO zuletzt 29.09.2026, sin²θ₁₂ = 0,3036 ± 0,0064). Offen und wartend: H9 (JUNO σ ≤ 0,004), H42/H46 (nächste globale Auswertung),
  H100 (NuFIT nach 6.1, Frist 31.12.2027). H9 und H46 hängen an β_sym/η (OP1-Zahl). Issue #11: drei von vier Kriterien erfüllt, Herleitung fehlt.
  Nächster Schritt bei neuen Daten: Prüfungen nach den festen Kriterien auswerten.
  Vorschau (PR #176, kein Test): mit NuFIT 6.1 läge H42 bestätigt, H46 unentschieden, H9 0,00σ (JUNO 2026 +0,81σ), TM1 +2,28σ gegen JUNO 2026.
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
