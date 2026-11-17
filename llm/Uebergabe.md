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
- `main` nach **PR #168** (OP1 Auslesefrequenz von M), davor **PR #167** (012b296, OP1 Querungen oder Flusslinien), **PR #166** (9a07c7b, Release v5.2.0), …
  Zweige gelöscht. Keine offenen PRs. CI nach #166 grün.
- Issues #17, #10 (OP1), #131 (OP3) nachgezogen.

### Forschung
- **Letzte Runde:** v4.10.0-r28 (Stand Restbiegung und Zählregel, r28.1–r28.7). Davor r27 (PR #156).
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
- **Möglicher nächster Schritt:** OP1 steht wieder bei „warum Gewicht 2 im Spektrum √(j(j+1))“; ungeprüft: geladene/rotierende
  Horizonte, Graukörper. Ggf. OP1 ruhen lassen (Autorentscheidung). Test nur mit Vorab-Notiz (H112). Nächste Version erst mit
  genug Stoff für beide Ausgaben.
- OP1–OP5, C5, C6/T2 offen. Notizen unter `notes/research/op1_*_2026_11_1[67]/`, `op3_*_2026_11_16/`, `v4_10_0_r28/`.
