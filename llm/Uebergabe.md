# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 16.11.2026 (Claude Fable, dann Claude Opus 5.5)
- **Öffentlich:** **v5.1.0**, veröffentlicht am 15.11.2026, Version-DOI 10.5281/zenodo.24237112,
  Record https://zenodo.org/records/24237112; Vorgänger v5.0.0 (10.5281/zenodo.24152615). Vollausgabe 1412 Seiten,
  Physik-Paper 29 Seiten. Paketquellstand dfdb413, Tag `v5.1.0`, GitHub-Release gesetzt. Nach der Veröffentlichung
  geprüft: acht Dateien prüfsummengleich mit dem Paket, Vorschau = Vollausgabe. Release-Notiz `release/v5.1.0/README.md`.
- **GitHub:** `main` nach PR #156 (f0bb768, Runde r27, Berichtigung), davor PR #155 (69863d8, Runde r26, Verdopplungsregel), davor PR #154 (942508b, Runde r25, Dixon-Kopien), davor PR #153 (17f20aa, Vorab-Notiz H105), davor PR #152 (ad665b4, Runde r24, OP1), davor PR #151 (Frame-Abschnitte im Aussagenspeicher), davor PR #150 (fdde521, Runden-Absätze im Aussagenspeicher), davor PR #149 (f495e5a, Runde r23, Kaskade), davor PR #148 (a141650, Runde r22, Kollapszustand typisiert), davor PR #147 (c0f3011, Runde r21, C5 neu gestellt), davor PR #146 (d9d4b5c, Runde r20, C5), davor PR #145 (81a6ccb, Neuheitsprüfungen Kern und Koide), davor #144 (982c476, Runde r19), davor #143 (80af436, C5 (α) in der r10-Lesart), davor #142 (cdb45bf, C5 Nullaugenblick), davor #141 (144d4ff, Runde r18), davor #140 (c66a5ab, OP4 Zeitzyklus und Spin(8)-Zentrum), davor #139 (86d80c8, Suche nach blindem Test, H2 nachgerechnet), davor #138 (68e1075, Runde r17), davor #137 (a835c46, OP1 Brücke: Barbero-Dublett, Penrose-Stränge), davor #136 (45f518d, OP3 Uhr-Abgleich und Treue-Lesart, OP1 Irreduzibilität), davor #135 (e0be304, Runde r16 mit r16.1–r16.9), davor #134 (f32ae5c, k220 „ein Objekt“ übernommen), davor #133 (37ac7da, OP3: C⊗O, Helizitätsachse, invariante Kugel, Feldvorzeichen), davor #132
  (b6ed1a5, Runde r15, Dauerauftrag Issues), #130 (eeb6083,
  Berichtigung zu CT-004), #129 (c9bfb19, OP1 mit I1, CT-004) und #128
  (14feb02, Release v5.1.0). **Offen: PR #157** (Zweig `research/h106-singlet-residual`: H106 und H107 widerlegt; wartet auf Freigabe). **Offen: PR #158** (Zweig `tools/hs-partition`: Hilfskonstruktion `tools/hs_partition.py`,
  Idee des Autors; Selbsttest reproduziert r25/H106; wartet auf Freigabe). Gemergt am 14./15.11.: #124–#128
  (OP3-Rückwärtssuche, Dauerauftrag Versionsverwaltung, Abbildung C⊗S → C⊗H⊗O, bewachter Kern, Release), davor #108–#123.
  Gemergte Zweige sind gelöscht (16.11.: drei lokale Altzweige). Die Läufe nach dem Merge von #146 waren erfolgreich.
- **Letzte Runde:** v4.10.0-r27 (Berichtigung zu r26, r27.2, PR #156, f0bb768). **Davor:** v4.10.0-r26 (Verdopplungsregel, PR #155, 69863d8). **Davor:** v4.10.0-r25 (Dixon-Kopien, PR #154, 942508b), v4.10.0-r24 (OP1, Querungen, PR #152, ad665b4). **Davor:** v4.10.0-r23 (Kaskade, PR #149, f495e5a), v4.10.0-r22 (Kollapszustand, PR #148, a141650), davor v4.10.0-r21 (gemergt über PR #147 als c0f3011), C5 frame-sauber neu gestellt (PR #147). Anteile C5_M + C5_T = 1,
  frame-freier Boden |s|/2u. Drei Fragen: Übergangsfrage (Verlagerung, keine Entladung), Photonpunkt-Frage (für Felder
  positiv; bleibende Null nur bei s₊ = s₋ = w = 0), Brückenfrage (offen). Berichtigung zu r20.4: gleiche Anteile sind für P
  notwendig, nicht hinreichend. Notizen `notes/research/c5_restatement_2026_11_16/`, `notes/research/v4_10_0_r21/`.
  Nachtrag vor dem Merge (r21.8–r21.10): Unter Lorentz-Gruppe, Dualität und Skala gibt es genau zwei Klassen von Feldern
  (lichtartig oder nicht), Vertreter P (φ = 0) und R (φ = 1), φ = sech 2η_R. Kollapszustand z⁻ = 0 des Hauptkorpus mit
  heutigem Wissen: zwei Rollen, Nullpunkt des Versatzes (R, kein Nullzustand) und invariantes Objekt (P, Nullzustand);
  Spannung mit r24.3 vermerkt („never fully reach z⁻ = 0“ passt zu P). Skript `two_classes.py`.
  Kandidat 1438 Seiten, Guard-Linter 0. Issues #13 und #17 nachgezogen. Zuletzt vergebene Runde: **r21**.
- **Davor:** v4.10.0-r20 (C5-Kandidat Nullaugenblick, Abgleich mit r88, Zeit gegen Kollar-Stufe, Frame-Audit r20.4),
  gemergt über PR #146 (d9d4b5c); ursprünglich als r19 geschrieben und wegen paralleler Vergabe von r19 (PR #144)
  umbenannt. Kandidat 1433 Seiten.
- **Davor:** v4.10.0-r19, gemergt über PR #144 (982c476) (Kommutant einer Generation C⁶, kein Generations-Qubit ohne Kopien; Vorliteratur Brannen 2010, Foot 1994, Golat et al. 2024). Nummer r19, weil r16–r18 schon vergeben waren. Kandidat 1430 Seiten.
- **Davor:** v4.10.0-r18 (Statusvermerke zu Suche nach blindem Test, Nachrechnung H2, Dirac-Zyklus = Zeitzyklus,
  Neutrino-ℤ₂ = Spin(8)-Zentrum), gemergt über PR #141 (144d4ff); davor r17 (PR #138), r16, r15, r14 (in v5.1.0).
  Kandidat 1427 Seiten.
- **Hypothesen:** zuletzt vergeben **H107** (k229, widerlegt, Vorab 30a4a50, erweitert 44cda89, 16.11.). Frei: **H108, k230**.
  - H107 widerlegt: verschachtelte Normierung HS(8) = HS(7) ⊕ HS(6) ⊕ HS(6) (Idee des Autors), volle Grammatik, 20 Versuche, kein Treffer
    auf 0,0002 rad; nächster N1 −0,0015. Struktur: Bei Produktzuständen |n⟩|n⟩ ist ein in seiner HS(7)-Hälfte normiertes HS(6) das Gewicht
    eines einzelnen Kopien-Qubits; die Verschachtelung trägt nur bei verschränkten Generationszuständen. Kreuzprüfung mit
    `tools/hs_partition.py` (PR #158). Nächste Wege (Autor): verschränkte Generationszustände; Renormierung (Polmassen/laufende Massen).
  - H106 (k228, Vorab abf54a0): widerlegt.
  - H106 widerlegt: Singulett der vier Dixon-Kopien schließt den Rest 0,012376 nicht (M1 Gewicht ¼ → 0,640; M2 Normalen-Paare →
    0,679). Nachträglich, nicht gedeutet: Gewicht 0,0979 träfe 2/3. Neuer Test nur mit Mechanismus, der das Gewicht vorher festlegt.
  - H105 offen (Vorab b77ba9e, k227).
  - H105 offen: Flächenschritte 4 ln 2 l_P² und Echos im Ringdown unter Setzung V1 (Querungs-Lesart r24.4); nur Analysen nach
    dem 16.11.2026, Frist 31.12.2028 (`notes/research/predictions/Vorab_Notiz_H105_Flaechenschritte_Echos.md`, `k227_test_h105.py`).
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
  Nachtrag (PR #136): Koide = Kohärenzfunktional der Photon-Uhr-Sonde (r90), aber keine
  Fensterschwelle bei ½ und Drift 120° ≫ 26,57°; Uhr legt Σp² = 2/3 nicht fest. In Runde r17.
  Dazu Lesart: Treue ½ als maximale Unsicherheit „dasselbe Objekt?“ (ein Bit); kein Test. OP3 ruht; weiter mit OP1.

- **OP1, Irreduzibilität (15.11., Erkundung, `notes/research/op1_frame_irreducibility_2026_11_15/`,
  PR #136):** Frame-Abbildungen als exp(−iπJ_k) auf Spin j wirken nur bei j = ½ irreduzibel; T = irreduzibel,
  M = invariantes Extremdublett gibt das H98-Paar (γ_L = 1,864700). Ersetzt P2; Annahme (A) Feld-Dublett → Punktierung und
  Asymmetrie M/T gesetzt; kein Test. Mögliche Alternative zu Guard 1 von CT-004 (Register unverändert).
  Nachtrag (PR #137): A_γ = c₊A₊ + c₋A₋, reelles γ auf dem Äquator; Frame-Abbildungen wirken auf γ als
  −1/γ, −γ, 1/γ, keine gibt γ_T aus γ_M. Brücke (A) weiter offen.
  Nachtrag: Penrose-Bündel geben (A), wenn ein Strang ein Quant von χ ist; bosonische Stränge → alle j (M), fermionische →
  nur j = ½ (T). Ersetzt Guards T = String und Chan–Paton von CT-004 durch (S1)–(S3); Register unverändert; kein Test.
  Nachtrag (PR #138, r17.6): R² = −1 gibt Kramers, nicht Pauli; Frame-Abbildungen sehen die Statistik
  nicht. (S2) ist reine Setzung; Begründung über R² zurückgenommen.

- **Suche nach blindem Test (15.11., `notes/research/blind_test_search_2026_11_15/`, PR #139):**
  kein Test gefunden. Neutrino-Kandidaten „Majorana: p₊ = p₋“ (R = 0) und „p₋ = 0“ (R = 0,0052) durch Daten ausgeschlossen;
  δ_CP, Majorana/Dirac, Strang-Statistik ohne Konstruktion. Daten 15.11.: kein NuFIT nach 6.1, PDG 2026 ohne neues m_τ.
  H2 nachgerechnet: Σm_ν = 0,0592 eV stabil (NuFIT 6.0/6.1, JUNO, SNO+), verträglich; Wiki-Angabe zur Ordnung berichtigt.

- **OP4, Zeitzyklus (15.11., Erkundung, `notes/research/op4_time_cycle_mixing_2026_11_15/`,
  PR #140):** Slotzyklus τ (r55) = Zeitzyklus (r16.9); Slotzustände = Auslesungen zu 0, T/3, 2T/3,
  Fourier-Moden = Massenbasis. TM2-ℤ₂ ohne Frame-Herkunft (T fixiert alle Slots, ρ gibt θ₁₃ = 0). Keine Zahl. Dazu Wiki-H2-Zeile
  um JUNO-Globalanalyse (Δχ² = 4,6 für normale Ordnung) ergänzt. H9 offen (keine JUNO-Messung mit σ ≤ 0,004 gefunden).
  Nachtrag: Neutrino-ℤ₂ = Spin(8)-Zentrum (1, −1, −1), Vektor-Slot fest → TM2; mit r57-Maske nur maskenfreie Slots als feste
  Spalte (je 388 Treffer, Maskenslot 0). Begründung für G_M, keine neue Zahl.

- **C5, Form (iii) (15.11., Erkundung, `notes/research/c5_null_instant_2026_11_15/`, PR #142):**
  Nullaugenblick: s(t) eines nicht generischen zeitharmonischen Feldes wird zu endlicher Zeit exakt 0 (Feld ≠ 0, Zustand im
  Photonpunkt, Score ½, Lorentz-invariant, periodisch). Erfüllt (β)–(δ) von r88, (α) nur unter „Obstruktion = augenblickliches s“.
  Nachtrag (PR #143): Lesart B ist augenblicklich (r05.2(a)), r10s Obstruktion = Boden |s| des augenblicklichen
  Feldes → (α) innerhalb der r10-Lesart erfüllt. Offen: periodische Null, Zuordnung zu Kollar-Stufen, nicht generische Felder.
  Nachtrag (PR #146): Zeit = Kollar-Stufe nur bei reiner Helizität, dort kein Nullaugenblick; Felder mit
  Nullaugenblick tragen beide Helizitäten → keine Folge von Kollar-Stufen (passt zu (β), Zählung als Stufe offen).
  Keine Entladung; C5 offen.

- **C5, Autorentscheidungen 16.11.:** Neufassung („C5 neu stellen“, r21) und zu (B2) die Ereignis-Lesart als Arbeitsannahme
  (r21.10; Autor: „erst die Existenz eines Augenblicks zeigen, dann eventuell verallgemeinern“). Gesetzt, nicht hergeleitet.
  Offen bleiben (B1) Lesart „Obstruktion = Boden“ (r10) und (B3) Vorliegen der Felder von Kodimension 1.
- **Hinweis des Autors (16.11.):** Die Idee des Kollapszustands stammt vom Anfang des Projekts und ist mit heutigem Wissen
  zu überprüfen; r21.9 ist ein erster Schritt (vier Hauptkorpus-Stellen). Eine Durchsicht aller z⁻-Stellen des Hauptkorpus
  (Statusvermerke nach r21.9-Tabelle) steht aus.
- **OP3, Brücke r15.5 (15.11., Erkundung, `notes/research/op3_frame_bridge_2026_11_15/`, PR #144):** Kommutant von Eich- und Lorentzgruppe auf einer Generation von C⊗H⊗O = C⁶ (je Multiplett eine Phase), kein antilinearer Anteil → kein Generations-Qubit; R zentral, T und J_B keine Symmetrien. Mit n Kopien M_n(C). Beantwortet „geladener Träger“ aus r16.7 negativ für eine Generation. Nicht blind (Schur).
- **Kurzfassung / Paper (15.11.):** Literaturprüfung: Algebra-Kern = Riemann–Silberstein-Stoff, Zustandsscheibe ≈ Symmetrie-Kugel (Golat et al. 2024), Koide-Oktant, π/4, π/12 bei Brannen 2010. Kein neues Ergebnis für ein Forschungspaper aus Kern oder Koide. Planungsdateien `paper/kernel-note/outline.md` und `paper/koide-note/novelty_check.md`, gemergt über PR #145 (81a6ccb). Literaturnotiz in `notes/research/literature_check_2026_11_15/` (PR #144).

## Nächster Schritt (Autorentscheidung)
- **C5 (B3) als r21.11 in PR #147 (16.11., Autorentscheidung):** Nullaugenblicke liegen in generischen monochromatischen
  Feldern auf Flächen im Raum, überall bei einer linear polarisierten Teilwelle; Punkte der Riemann–Silberstein-Wirbel
  (Kaiser 2003, Białynicki-Birula 2003; nachträglich gefunden). Offen: Wahl des Punktes. Notiz
  `notes/research/c5_presence_2026_11_16/`. Zweig `research/c5-b3-presence` ist in den r21-Zweig übernommen und gelöscht.
  Kandidat 1439 Seiten.
- **C5 (B1) rückwärts als r21.12 in PR #147 (16.11.):** Im ursprünglichen C5 ist der Score das Normquadrat der Obstruktion
  (`def:v470-r04-c5-lowering-score`), beide verschwinden nur gemeinsam. Am Nullaugenblick Boden 0, Score ½ → **kein C5-Zeuge**;
  Brückenfrage unter der ursprünglichen Definition negativ; **Berichtigung zu r20.2** (Boden mit Residuum gleichgesetzt);
  Form (iii) hat keinen Kandidaten mehr. C5 offen in der Übergangsfrage (nur Verlagerung, δ). Dazu Nachtrag zu (B3):
  helizitätsneutral ist die einzige von allen Frame-Abbildungen erhaltene Helizitätsstufe (nur Notiz/Wiki, nicht im Rundentext).
  Wiki: Berichtigungsvermerke an den r20-Einträgen. CI-Lauf gestartet, Ergebnis nicht geprüft.
- **Kollapszustand typisiert = Runde v4.10.0-r22 (16.11., gemergt über PR #148 als a141650, Zweig gelöscht):**
  `notes/research/collapse_state_typing_2026_11_16/`. Alle 93 z⁻-Stellen des Hauptkorpus: Gruppe 1 (Nullpunkt des Versatzes)
  = R; Gruppe 2 (invariantes Objekt) = Rolle von P am Punkt z⁻ = 0; Gruppe 3 (Horizont z⁻ → ∞, β → 1) = Ort von P; Gruppe 4
  kein Punkt; Gruppe 5 (Richtung der Kaskade) offen. Die Koordinate z⁻ läuft von R nach P wie η_R in r21.8. Der Nullzustand
  im Sinn von r21.8 liegt beim Horizont. **Berichtigung zu r21.9 Zeile 3:** „never fully reach z⁻ = 0“ ist R (bleibender
  Versatz), nicht P. Wiki im selben PR; Register #17 nachgezogen. Kandidat 1442 Seiten, Guard-Linter 0.
  Zuletzt vergebene Runde: **r22**.
- **Kaskade = Runde v4.10.0-r23 (16.11., gemergt über PR #149 als f495e5a):** `notes/research/cascade_endpoint_2026_11_16/`.
  Antwort auf r22.4: zwei Kaskaden unter einem Namen. Kompensator-Kaskade (C ∘ Π_J, Kollar, Hopf, Λ = 0) → R; Nullachsen-
  Transport (`thm:fractal` mit r06) trägt P, führt nicht hin; Dephasierung → P nur im Grenzwert; Reservoir (r28.2(c)) dazwischen,
  je nach Kopplung. Zum Nullzustand P führt keine endliche Kaskade. Kandidat 1444 Seiten, Linter 0. Zuletzt vergebene Runde: **r23**.
- **Datenbank analysiert (16.11.):** Aussagenspeicher aus `main` lokal gebaut: 2599 Objekte, fast alle `imported-unreviewed`,
  Frame `unspecified`, 2481 offene Guards; nur die Koide/HC-Zweige geprüft (63 Reviews, 1 abgelehnt). Lücke: Runden nur als je ein
  Thema → geschlossen über PR #150 (fdde521): 354 Runden-Einträge aus 134 Runden (Stand r22), v5-Editionen unverändert.
  Frame-Abschnitte eingelesen (PR #151 gemergt): 236 von 359 Runden-Einträgen (83 Runden) mit Frame `convention-f-section`,
  117 mit eigener Zeile; wörtlicher Vermerk, keine geprüfte Typisierung, Guards offen. Danach: OP1 (Rückwärtssuche, I1-3 nennen).
- **OP1, Rückwärtssuche zu (S2) = Runde v4.10.0-r24.1/r24.2 (16.11., gemergt über PR #152 als ad665b4):**
  `notes/research/op1_statistics_backward_2026_11_16/`. Kein Operator im Bestand wirkt auf den Strangtausch und wird zugleich von R
  vertauscht (Frame-Abbildungen, Port-Parität J, strangweiser Kompensator wirken strangweise). (S2) aus Frame-/Portstruktur nicht
  begründbar; weitere Varianten mit dieser Voraussetzung ausgeschlossen. Nebenbefund: strangweise Kompensation → ausgerichtete
  Bündel = Lesart für (S3). Auslöser I1-3 getroffen, I1 dem Autor als Ausweg vorgelegt (T zählt Endpunkte einzelner Strings;
  Preis Guard 1 von CT-004).
- **OP1 mit I1 = Runde v4.10.0-r24.3/r24.4 (16.11., gemergt über PR #152, `notes/research/op1_i1_crossing_2026_11_16/`):** Guard 1 „T = String-Sektor“ hat keine Stütze;
  T11 widerspricht ihm sogar (Scheiben-Ports: M liest C = String, T liest A = LQG). Ersatz: „T zählt Querungen des Horizonts, eine
  Querung = ein Strang“ (Stütze `thm:core`, r64(e), r63.3); j = ½ aus der Einzahl, (S2) entfällt. Lesart, kein Test.
  CT-004-Register unverändert. Issue #10 und #17 nachgezogen. Kandidat 1447 Seiten, Linter 0. Zuletzt vergebene Runde: **r24**.
- **Testsuche zur Querungs-Lesart (16.11., Zweig `research/op1-crossing-test-search`, nur Notiz):** Kein blinder Test.
  Folge: Flächenschritte 4 ln 2 l_P² (Bekenstein–Mukhanov, α = 4 ln 2), Echos im Ringdown nur, wenn jede Querung ein T-Quant ist
  (V1). (V1) ist eine neue Wahl, Beobachtbarkeit umstritten (arXiv:2201.03245), Wert nicht projektspezifisch; (V2) nur Hawking.
  Autor hat V1 gesetzt → H105 (siehe Hypothesen).
- **OP3, Dixon-Kopien = Runde v4.10.0-r25 (16.11., Idee des Autors, gemergt über PR #154 als 942508b):**
  `notes/research/op3_dixon_copies_2026_11_16/`. HS(7) = 2 Kopien → Kopien-Qubit (Ladung bestimmt), drei unverzerrte Zustände =
  flacher Oktant (det G = 0). HS(8) = 4 Kopien = Triplett + Singulett; Spin-1-Dreieck im Triplett gebogen; Spatprodukt der drei
  → Singulett, |det V|² = det G: vierte Kopie speichert die Biegung (neutraler Levi-Civita-Träger aus r13.6). Halbierung bestätigt,
  3 + 1 liegt quer dazu. Offen: HS(7)/HS(8) im Atlas nicht definiert; Rest 0,0124; Auswahl der drei Zustände.
  Kandidat 1450 Seiten, Linter 0; Issue #131 und #17 nachgezogen. Zuletzt vergebene Runde: **r25**.
- **Zulässigkeit HS(7)/HS(8) = Runde v4.10.0-r26 (16.11., gemergt über PR #155 als 69863d8):** Atlas definiert nur bis HS(6), empfiehlt
  vor neuer Stufe die Bildprüfung und nutzt Dixon als OP5-Routen-Code ohne Teilchenaussage. Mit der Verdopplungsregel von HS(5) als
  allgemeiner Regel (gesetzt) sind alle Kopienoperationen aus r25 leck- und schuldfrei; Schuld nur innerhalb einer Kopie. Formal
  zulässig, stützt die physikalische Lesart aber nicht. Regel als r26.1 gesetzt (Autorentscheidung). Kandidat 1452 Seiten, Linter 0;
  Issue #131 und #17 nachgezogen.
- **Berichtigung = Runde v4.10.0-r27 (16.11., gemergt über PR #156 als f0bb768):** Die Bildprüfung von HS(6) steht schon im Atlas (Schicht r59, keine offene
  Klasse); r26 hatte sie fälschlich als offen geführt. OP5 laut Atlas lokal geschlossen, offen nur an der Active-Core-Grenze. r59 rät
  von neuen Trägern ab. Dazu r27.2 (Frage des Autors): Gründe des Atlas geprüft: (a) endliche OP5-Routenprüfung gilt nur für Routen,
  (b) Vorsicht vor Algebra-Verdopplung trifft Kopien nicht, (c) Rahmen ohne Teilchenanspruch heißt nur: Rollen getrennt halten. Keiner
  verbietet HS(7)/HS(8) als Kopienträger. Kandidat 1454 Seiten, Linter 0. Zuletzt vergebene Runde: **r27**.
- **C5 ruht nach r21.12:** Form (iii) ohne Kandidat; ohne neue Struktur keine weiteren Varianten. Möglich: OP1 (a)
  oder den Kollapszustand im ganzen Hauptkorpus nach der Tabelle r21.9 typisieren (R oder P).
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
