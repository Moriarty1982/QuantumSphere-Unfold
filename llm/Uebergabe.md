# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 15.11.2026 (Claude Opus)
- **Öffentlich:** **v5.1.0**, veröffentlicht am 15.11.2026, Version-DOI 10.5281/zenodo.24237112,
  Record https://zenodo.org/records/24237112; Vorgänger v5.0.0 (10.5281/zenodo.24152615). Vollausgabe 1412 Seiten,
  Physik-Paper 29 Seiten. Paketquellstand dfdb413, Tag `v5.1.0`, GitHub-Release gesetzt. Nach der Veröffentlichung
  geprüft: acht Dateien prüfsummengleich mit dem Paket, Vorschau = Vollausgabe. Release-Notiz `release/v5.1.0/README.md`.
- **GitHub:** `main` nach PR #135 (e0be304, Runde r16 mit r16.1–r16.9), davor #134 (f32ae5c, k220 „ein Objekt“ übernommen), davor #133 (37ac7da, OP3: C⊗O, Helizitätsachse, invariante Kugel, Feldvorzeichen), davor #132
  (b6ed1a5, Runde r15, Dauerauftrag Issues), #130 (eeb6083,
  Berichtigung zu CT-004), #129 (c9bfb19, OP1 mit I1, CT-004) und #128
  (14feb02, Release v5.1.0). **Keine offenen PRs.** Gemergt am 14./15.11.: #124–#128
  (OP3-Rückwärtssuche, Dauerauftrag Versionsverwaltung, Abbildung C⊗S → C⊗H⊗O, bewachter Kern, Release), davor #108–#123.
  Gemergte Zweige sind gelöscht. Nicht geprüft: die Läufe nach dem Merge von #128 (Wiki-Sync, Zwei-PDF).
- **Letzte Runde:** v4.10.0-r16 (Statusvermerke zu Helizitätsachse, invariantem Dublett, Frame-Vorzeichen, Hurwitz-
  Ausschluss, k220, r16.7: höchstens drei nicht orthogonale Frame-Eigenzustände = Oktant, kein Zyklus nötig; r16.8: dritte Invariante w;
  r16.9: Zeitzyklus, Gewichte = normierte √m, Koide = Autokorrelation 1/√2), gemergt
  über PR #135 (e0be304); davor r15 (PR #132), r14 (in v5.1.0). Kandidat 1421 Seiten.
- **Hypothesen:** zuletzt vergeben H104 (k226, widerlegt). Frei: **H105, k227**.
  - H100 offen: nächster NuFIT-Fit nach 6.1, Frist 31.12.2027 (`notes/research/predictions/k222_test_h100.py`).
  - H102 offen: m_τ = 1777,134 MeV gegen die erste PDG-Ausgabe nach dem 13.11.2026 (`k224_test_h102.py m_tau sigma`).
    Gegenwind schon heute +2,3σ. Eingefroren; eine neue Herleitung wäre eine neue Hypothese.
- **Platzhalter:** CT-001 partially_constrained, CT-002, CT-003 und CT-004 placeholder; keiner strukturell abgeglichen.
  CT-004 (15.11.): Zählregel je Frame als Stringendpunkte (OP1 mit I1), vier Guards; H15, H46 und H96 auf Autorenauftrag verknüpft
  (erben je vier Guards). Berichtigung: Guard 1 („T = String-Sektor“) hat keine Stütze im Bestand (v4.8.0-r03 F11:
  γ_string nur dem Namen nach Stringkopplung; T11 ordnet nach J-Parität); als Spannung eingetragen (Hash c8dffe0d…).
- **Daten 15.11.:** PDG weiter Ausgabe 2026 (vor dem 13.11.), kein NuFIT nach 6.1 gefunden; H100 und H102 offen.
- **OP1 mit I1 (15.11., Erkundung, `notes/research/op1_i1_string_endpoints_2026_11_15/`):** T zählt Endpunkte einzelner
  offener Strings (Chan–Paton, j = ½), M Kanten des Spin-Netzwerks. Die Kramers-Regel ist ausgeschlossen (β = 0,337).
  Kein blinder Test. Gemergt über PR #129 (c9bfb19).
- **Daueraufträge:** gemergte Zweige löschen (14.11.); interne Nummern selbst vergeben und Buchführungs-Commits ohne
  Rückfrage auf `main` pushen (15.11., `AGENTS.md`). Neu (15.11.): **Issues nachziehen** — Register #17 und berührte OP-Issues
  nach jeder inhaltlichen Änderung ohne Rückfrage aktualisieren (`AGENTS.md`). Am 15.11. nachgezogen: #17 (Basis v5.1.0),
  Sammelnachträge #10–#12, Stand-Vermerke #13–#16, **neues OP3-Issue #131**. Inhalt nur über PR, Zenodo nur mit Freigabe.
- **Zenodo-Hinweis:** Das Upload-Hilfsskript setzt die Vorschau nicht selbst; der Autor setzt sie im Entwurf von Hand.
  Dabei kann die Veröffentlichung mit ausgelöst werden (so bei v5.1.0).

## Inhaltlicher Stand nach r14 (OP3)
- **Gebogene Achsen (exakt):** Drei Zustände mit Überlappung ½ geben immer K = 2/3; det G = (√2 cos φ − 1)/2. Der
  flache Oktant (φ = π/4) ist der Grenzfall mit einer Masse null; die geladenen Leptonen liegen bei φ = 2/3.
- **Bewachter Kern (Lesart):** Die Biegung π/4 − φ lässt sich als flussfreie Kappe im Generationsdreieck lesen
  (v470/05, X = S³ ∖ B_ε(K)). Daraus folgen das Vorzeichen (Lage), genau ein Kern (Topologie: n − 1 freie Holonomien)
  und der Gegenpol für den verdrängten Fluss (Umkehrwalze nach r02: antilinear, fixpunktfrei, auf Spin ½ antipodal).
  Kerngröße und Abfluss-Anteil sind entartet; Ω = γ_M gilt nur mit vollständiger Ablage außerhalb.
- **Offen ist eine einzige Größe:** die Kerngröße γ_M. Gelesen als Flächenquant des Beobachter-Frames fällt sie mit
  **OP1** zusammen: Warum zählt der Materie-Frame alle Spins (γ_M) und der Tachyon-Frame nur den Boden (γ_T)?
- **Generationen:** Die zwei Generationen von CT-003 sitzen, über Farbe und Ladung verglichen, am Platz des Spins.
  Ein Drei-Generationen-Träger mit neutralem Levi-Civita-Tripel fehlt weiterhin (r13.6, r14.3–r14.4).
- **Notizen:** `notes/research/op3_action_balance_search_2026_11_14/`, `op3_cs_dixon_map_2026_11_15/`,
  `op3_guarded_core_flux_2026_11_15/`, Runde `notes/research/v4_10_0_r14/`.

- **Schatten (15.11., Erkundung, `notes/research/op3_horizon_shadow_2026_11_15/`, Idee des Autors):** Der Kern als
  Schatten eines Horizonts auf dem Himmel des Beobachters. Er ist die gesuchte Abbildung und von selbst flussfrei,
  mit Anker im Paper (`rem:hc-shadow-vs-core`). Die Größe bleibt offen: Synge braucht r ≈ 9 r_s, der Sektor gibt γ/2.
  Spin 1 behebt den Faktor 2 nicht; das Spin-1-Dreieck mit Überlappung ½ ist aber schon von selbst gebogen (0,6790).
  Frame M folgt aus der Invarianz der Massen (Lesart).

- **Spin-1-Dreieck (15.11., Erkundung, `notes/research/op3_spin1_triangle_2026_11_15/`):** Drei kohärente Spin-1-Zustände
  mit Überlappung ½ geben Koide 2/3, Rang 3 und Zyklus in einer su(2); Phase 0,6790, Rest bis zu den Leptonen 0,0124.
  Die Bezugsrichtung (38,68°) ist nicht nativ (143 Kandidaten, kein Treffer) und folgt aus der Überlappung ½ selbst.
  Koide = drei Zustände auf halbem Fubini–Study-Weg zwischen gleich und orthogonal. Den Rest nicht ohne Vorab-Notiz deuten.

- **Koide als Komplementarität (15.11., Erkundung, `notes/research/op3_koide_complementarity_2026_11_15/`):** Der Oktant ist
  je ein Zustand der drei gegenseitig unverzerrten Basen eines Qubits. Ein vollständiger Satz in Dimension d gibt
  N = d + 1 Zustände mit K = 2/N; nur d = 2 gibt drei Zustände und K = 2/3. Zwei Prinzipien gesetzt (ein Zustand je Basis,
  vollständiger Satz); Biegung bleibt beim Kern, Neutralität bei CT-003. Kandidat für das Physik-Paper.

- **r38 neu gelesen (15.11., Erkundung, `notes/research/op3_frame_map_generations_2026_11_15/`, Auftrag des Autors):** r38
  ordnet Frames den Triality-Slots zu, ohne C-Faktor. r51 legt die Frame-Abbildungen in den C-Faktor; Punkt 6 von r38
  (M ↔ T = Chiralitätswechsel) widerspricht r51.1(a) und ist nicht berichtigt. Lesart „eine Generation je
  Frame-Abbildung“ (T, J_B, R): unverzerrt, K = 2/3, Phase ±π/4; R erhält, Konjugation kehrt das Vorzeichen.
  **Runde v4.10.0-r15 geschrieben** (Berichtigung zu r38 und Statusvermerke r15.2–r15.5 zu Schatten, Spin-1-Dreieck,
  Komplementarität und Generationen je Frame-Abbildung), Notizen `notes/research/v4_10_0_r15/`. Zuletzt vergebene Runde: r15.

- **Nachtrag zu r15.5 (15.11., gemergt über PR #133):** Auf C⊗O ist R skalar, T und J_B haben
  dieselben Eigenstrahlen, und diese tragen keine bestimmte Ladung (⟨Q⟩ = ½). Die Lesart „Generation je Frame-Abbildung“
  gilt nur auf der komplexifizierten Ebene z, also auf einem gesetzten Qubit; sie fällt auf r15.4 zurück. Gehört in die
  Runde r16 (r16.1).

- **Helizitätsachse (15.11., Erkundung, `notes/research/op3_helicity_axis_2026_11_15/`):** Auf dem Dublett (E, B) mit der
  Helizität als σy (r05.2) wirken R, T, J_B wie auf die Chiralität in r51; σy-Pole = Ports. Koide-Phase braucht Helizität
  (Σ b_y² = 1 je Oktant; Scheibe gibt Phase 0 oder π). Grenze: b_y nicht boost-invariant, kein Frame für drei Zustände.
  Nachtrag: Auf der Kugel der Invarianten χ = (√s₊, √s₋), s± = (E ± iB)², gibt es ein boost-invariantes Oktant
  (Materie, Photonseite, selbstdual); Zweigwahl der Wurzel = R. Überlappung ½ bleibt gesetzt.
  Nachtrag: R, T, J_B erhalten je eines der drei Feldvorzeichen (Re s, Im s, Helizität); Pole = Eigenzustände; Überlappung ½
  folgt bedingt aus „je Frame-Abbildung ein Eigenzustand“. Kein Dreierzyklus aus linearen Feldabbildungen (nur diagonal/
  vertauschend auf χ). Kandidat Hurwitz-Einheiten auf N (r13.2, CT-003) geprüft und ausgeschlossen: R skalar auf N,
  T bildet N auf N̄ ab (r16.5, PR #135). Prinzip „je Frame-Abbildung ein Auslesezustand“ bleibt gesetzt.
  Festgehalten in Runde r16.

- **k220 übernommen (15.11.):** Die Erkundung „ein Objekt“ vom 7.11. (Bahnen von SO(3,ℂ) × Dualität; M und T eine Bahn,
  P Fixpunkt) lag nur auf dem lokalen Zweig `claude/quantenphysik-paper-herleitung-e723a3`; jetzt unter
  `notes/research/k220_ein_objekt_2026_11_07/` (PR #134). Lokale Altzweige danach gelöscht (Autorenauftrag).

- **Dritte Invariante (15.11., Erkundung, `notes/research/op3_third_invariant_2026_11_15/`):** w = F₊·F̄₋ ist die
  dritte komplexe Lorentz-Invariante (6 reelle); s(t) = ¼[s₊e^{−2iωt} + 2w + s̄₋e^{2iωt}]. S = [[s₊, w], [w, s̄₋]] ist Spin 1;
  Rang 1 = χ (Oktant flach), Rang 2 gibt Platz für die Biegung, Größe σ₂/σ₁ frei. **H105 bewusst nicht vergeben** (keine
  wahlfreie Konstruktion). Zuletzt vergeben weiterhin H104; frei H105, k227.
- **Zeitzyklus (15.11., Rückwärtssuche, `notes/research/op3_time_cycle_2026_11_15/`):** Verschiebung um ⅓ der Periode
  von s(t) = nativer Dreierzyklus auf S, gibt Brannen-Form. Nötige Gewichte p₀ = 0,793, p₊ = 0,193, p₋ = 0,013 (Kontrolle
  1 : 206,77 : 3477,5); kein nativer Wert (24 Kandidaten, 0,5 %, Erwartung 0,44); Rang 2, weit vom Oktanten r16.7.
  Nachtrag (Zweig `research/op3-clock-check`): Koide = Kohärenzfunktional der Photon-Uhr-Sonde (r90), aber keine
  Fensterschwelle bei ½ und Drift 120° ≫ 26,57°; Uhr legt Σp² = 2/3 nicht fest. Noch in keiner Runde.
  Dazu Lesart: Treue ½ als maximale Unsicherheit „dasselbe Objekt?“ (ein Bit); kein Test. OP3 ruht; weiter mit OP1.

## Nächster Schritt (Autorentscheidung)
- **(a) OP1 aus dem Bild des Kerns angehen:** Warum zählt T nur den Boden? Vorher Vorwissen (r08–r10, H98, H104,
  `Erkundung_Zaehlregel_Prinzip.md`) und Suchrichtung prüfen. Zu beachten: Eine Kramers-Regel (nur halbzahlige Spins,
  Θ² = −1) liegt im Regelraum von H98; dort trifft nur das gewählte Paar alle drei Fenster. Auslöser I1-3 der
  zurückgestellten Ideen ist bei jeder OP1-Arbeit berührt und dem Autor zu nennen.
- **(b) Daten:** H100 und H102 auswerten, sobald NuFIT oder PDG eine neue Ausgabe haben.
- **(c) Ruhen:** OP3 ist bis auf die Kerngröße ausgeschöpft; ohne neue Struktur keine weiteren Varianten.

## Pflichten in jeder Sitzung
`AGENTS.md`, `wiki/Gesamtbild.md`, die einschlägige Anleitung unter `notes/anleitungen/`, die Auslöser in
`notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md`. Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen.
Merges nur nach Freigabe. Wiki im selben PR. `.codex/environments/` bleibt unversioniert.
