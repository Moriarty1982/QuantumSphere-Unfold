# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 14.11.2026 (Claude Opus, zuletzt Claude Fable)
- **GitHub:** **PR #119 gemergt als 70da32a** (CT-003 eingetragen, Platzhalter-Bilanz), auf „PR 119 mergen“; Läufe
  danach (Wiki-Sync, Zwei-PDF) erfolgreich. Zweig gelöscht. **Offen: PR #120** (vier OP3-Erkundungen vom 14.11.,
  Zweig `claude/anthropic-skills-weitermachen-0a9117`, mergebar, keine Checks am PR). Merge nur auf „PR 120 mergen“.
  Am 14.11. außerdem gemergt: #118 (60ba894, Register Phase 2), #117 (f4a62cf, CT-002/T11), #116 (a3fe755), #115
  (990a3cc), #114 (44cdcd1), #113 (10d670e), #112 (ad7756f), #111 (c247ea3), #110 (8606691), #109 (963f557), #108
  (91cbb69). Am 13.11.: #104–#107.
- **Lokal:** `main` = `github/main` = 9b9dfda (Übergabe-Commits sind gepusht). Die Erkundung „Rechtswirkung von H_n“
  , „Majorana-Vektor auf N“, „dritte Generation als Singulett“ und „Achse auf dem τ-Dublett“ (14.11., Claude Fable) liegen auf dem Zweig
  `claude/anthropic-skills-weitermachen-0a9117` (Worktree `zealous-fermi-f46fd7`), gepusht als PR #120.
  Unversioniert: `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf` (jetzt wirklich im Hauptordner).
- **Letzte Runde:** v4.10.0-r12 (Statusvermerke) aus PR #106.
- **Zuletzt vergebene Hypothese:** H103 (vorab 45314b2, k225).
  - **H103a ist widerlegt:** Q_S wirkt auf N als 1/2 + σ_y/3 und steht senkrecht zur ψ-Achse (K = 1/2).
  - Nachtrag 14.11. (Erkundung, auf „Als Erkundung nachtragen“, `op3_rf_reference_2026_11_14.*`): Der Suchtreffer
    i R_f ist analytisch erzwungen. N ist ein Rechtsmodul über H_n; i R_e7, i R_e15, i R_e8 sind dort ein Pauli-Tripel
    mit e8 als ψ-Achse, also gilt c(i R_u) = |⟨u, e8⟩|, und jede Raumdiagonale trifft. Offen: warum die Rechtswirkung
    maßgeblich ist und was die Diagonale auszeichnet. H104 wird dafür nicht vergeben.
  - H102 ist offen: m_τ = 1777,134 MeV gegen die erste PDG-Ausgabe nach dem 13.11.2026 (`k224_test_h102.py m_tau sigma`).
  - H101 ist widerlegt. H100 ist offen; am 13.11. war NuFIT 6.1 weiterhin die neueste Version.
  - Als Nächstes ist H104 frei, das letzte k-Skript ist k225.
- **Offene Autorentscheidungen:** keine.
- **Platzhalter-Bilanz (14.11., `notes/research/counterterms/Bilanz_2026_11_14.md`):** Neu eingetragen ist CT-003, die
  Ladungsachse e8 statt e7 auf den Sedenionen (placeholder, drei Guards). Daran hängen S-N (neutrales Qubit), S-2T
  (über S-N) und S-GEN (zwei Generationen); sie erben je drei Guards. Der Elektron-Abstand π/12 − θ_e ist ΔΦ/3 und hängt
  an CT-001/CT-002, kein eigener Eintrag. Stand: drei Einträge, keiner strukturell abgeglichen. Der LaTeX-Export der
  echten Auswahl besteht die harte Prüfung (3 Einträge, 4 Vermerke), übersetzt aber nicht, weil die Aussagetexte aus
  Markdown stammen; der Anhang selbst übersetzt sauber.
- **Counterterm-Registry (14.11.):** Der Autor will damit Rapid Prototyping betreiben: Gegenterme setzen und später
  durch Herleitungen ersetzen. Phase 1 ist seit PR #114 gemergt (Schema, Validator, Weitergabe der Guards,
  Fixture CT-000-TEST). Ergänzt um die Herkunft der Fitdaten, eine Blindheitsprüfung, Δ als Prüfstein sowie diskrete
  Konventionswahlen mit Versuchszahl. Phase 2 ist seit PR #118 auf main (Exporttabelle, Guard-Vermerke, harte Exportprüfung).
  **Erster echter Platzhalter (Autorenwahl): CT-001, die Einheit bei ΔΦ = γ_M/2.** Der Entwurf liegt unter
  `notes/research/counterterms/CT-001_gamma_halbe_einheit_entwurf.md`; Eingetragen am 14.11. (`register_ct001_ct002_2026_11_14.py`, Bericht
  `register_2026_11_14_report.json`, reproduzierbar): CT-001 partially_constrained, CT-002 placeholder. H102 erbt
  sieben Guards; Blindheit gegen m_τ der PDG: not_blind, eine neue Version wird mit same_version = false
  ausgewiesen.
  Bekannte Spannung: Die r10-Konvention gibt Δ = 42,5 · γ/2.
  **Schritt 1 nach der Methode (14.11., `ct001_shrink_2026_11_14.*`):** Verlangt ist κs = 0,49982 (1σ-Band
  0,49974 bis 0,49990). ΔΦ ist ein äußerer Fluss, denn das Qubit-Tripel selbst gibt Ω/2 ≈ π/4. Als minimale
  Dirac-Phase folgt κs = 1/2 pro Steradiant. CT-001 wird `partially_constrained` (Guard: Monopol angenommen), dazu
  kommt der neue Restplatzhalter CT-002, Raumwinkel Ω_ext = γ_M. Nächste Frage: Ist γ_M im Companion als Winkel lesbar?
  **Schritt 2 (Hinweis des Autors: Kreisfläche zur Bogenlänge gegen eingeschlossenen Winkel,
  `ct001_sector_reading_2026_11_14.*`):** Der Sektor A = r²θ/2 gibt A/r² = θ/2. Liest man A_j aus r10 als Sektor mit
  Öffnungswinkel γ (r_j² = 16π a(j), unabhängig von γ), sind γ/2, das √3-fache und das 43,5-fache drei Messweisen
  desselben Sektors. Die einheitenfreie Weise (A/r², wie Ω = A/R²) gibt γ/2 für alle j. Vorschlag: CT-001
  `structurally_matched` unter dem Guard „Phase = normierte Sektorfläche“. CT-002 heißt jetzt: γ_M als
  Öffnungswinkel, warum? Offen ist auch, welche Messweise wofür gilt, denn r10.1 misst in 8πGħ.
  **Schritt 3 (`ct002_gamma_angle_2026_11_14.*`):** Der Wert von γ_M ist nativ: Die Zählregel ist in der Sektorlesart
  eine Gleichung für den Öffnungswinkel. Die Winkelbedeutung steckt im Unruh-Bild r10.1, wo der Boltzmann-Exponent die
  γK-Phase eines vollen euklidischen Umlaufs ist. Offen ist nur noch die Kopplung (CT-002 neu gefasst): Warum
  durchläuft der Lepton-Fluss genau einen Radianten bei Spingewicht ½? Die Daten geben κ = 0,99964 ± 0,00016 rad,
  also 2,3σ.
  **Schritt 4, I1 verfolgt (auf „Ja, I1 verfolgen“, `op3_i1_string_bridge_2026_11_14.*`):** Ein String zur
  Horizont-Punktierung überstreicht euklidisch einen Sektor. Bei einer Lichtquerung (Bogen = Länge, φ = 1 bzw.
  Rapidität 1) ist die normierte Weltfläche ½, also ΔΦ = γ_M/2; von vier gelisteten Dauern passt nur diese. CT-002 heißt
  jetzt „eine Informationsquerung“. Offen sind der Grund für genau eine Querung, das Ende im Frame M und die
  Stringdynamik. I1 hat in `Zurueckgestellte_Ideen.md` einen Stand-Eintrag. Nächste Frage: Gibt T11 bzw. die QAM-
  Verschiebung einen Grund für genau eine Querung?
  **Geprüft am 14.11. (`op3_ct002_t11_shift_2026_11_14.md`):** nein. T11 trägt nur die euklidische Lesart (Wick-Rotation),
  der Shift ist eine inhaltsfreie Umbenennung. Das war der vierte Ansatz an derselben Stelle; die Suche ruht, bis die
  nächste PDG-Ausgabe H102 prüft. Die Kette CT-001/CT-002 hängt an diesem Datum.
- **14.11., Hurwitz-Einheiten auf N** (`op3_hurwitz_2t_neutral_qubit_2026_11_14.*`, Erkundung, nicht blind):
  Die 24 Hurwitz-Einheiten von H_n wirken von rechts treu auf N als 2T (projektiv A4). N ist also ein natives
  2T-Dublett. Die ψ-Achse e8 ist zweizählig, die vier dreizähligen Achsen liegen unter 1/√3 dazu. Der Bezug ist ein
  Eigenzustand einer Hurwitz-Einheit der Ordnung 3 und gibt K = 2/3, π/4. ψ normalisiert 2T nicht. Die Frage zu Weg B
  war schon beantwortet (`op3_neutral_su2_octant`, Punkt 3: dort nur der A4-Vektor).
- **14.11., Generationen unter Q_*** (`op3_sedenion_generations_estar_2026_11_14.*`, Erkundung, nicht blind):
  C⊗S hat unter Q_* genau zwei vollständige Generationen. Die ψ-Sektoren sind aber keine Generationen
  (1: ν, e⁺; ω: ν, u, d̄; ω̄: e⁺, u, d̄). ψ wirkt innerhalb der Generationen als Phase und ist kein Generationsschritt.
  N ist der Raum zweier Neutrino-Flavours; der dritte fehlt (K28).
- **14.11., Rechtswirkung von H_n auf ganz C⊗S** (`op3_family_su2_right_action_2026_11_14.*`, Erkundung zu (c)):
  R_e7, R_e8, R_e15 vertauschen überall mit su(3)_c und Q_*. Quaternionen-Relationen gelten auf dem neutralen und dem
  farbigen Teil mit entgegengesetzter Orientierung, die erzeugte Lie-Algebra ist su(2)_Leptonen ⊕ su(2)_Quarks. Jede
  Teilchenart ist ein Dublett: Die zwei Generationen sind ein Dublett einer nativen neutralen Familien-su(2). ψ dreht
  Im H_n um e8 um 120°. Hurwitz-Einheit als Zyklus mit ψ-Eigenzustand als Bezug gibt den Oktanten in erster Form.
  Majorana-Bilinear = Vektor ohne Singulett. Einschränkung: Eine U(2) je Teilchenart folgt schon aus Schur; es bleiben
  zwei Generationen, das Dublett tragen alle Teilchenarten. Erbt die Guards von CT-003.
- **14.11., Majorana-Vektor auf N** (`op3_majorana_vector_n_2026_11_14.*`, Erkundung, nicht blind): Die native
  Bilinearform verschwindet auf N. Symmetrische Formen sind Vektoren m ∈ C³ in Im H_n: reelle Richtung = zwei gleiche
  Massen, Nullvektor = eine Masse. ψ-fest ist nur M₁₁ (ein massives Neutrino), Hurwitz-fest die Raumdiagonale (zwei
  gleiche). K = 2/3 nur bei freiem Mischwinkel, also Anpassung. Der Paarkanal ν^c ν^c (r82.4) ist nicht gerechnet,
  die Abbildung C⊗S ↔ C⊗H⊗O fehlt. Das war die dritte Variante mit derselben offenen Voraussetzung (dritte
  Generation); weitere Rechnungen auf N erst, wenn sie geklärt ist.
- **14.11., dritte Generation als Singulett** (`op3_third_generation_singlet_2026_11_14.*`, Erkundung, Rückwärtssuche):
  (S ⊕ O, ψ ⊕ 1) und Weg B (O³, τ) sind im farbigen Teil dieselbe Z₃-Darstellung, für u und d̄ passt 2 + 1 also. Im
  neutralen Teil steht (4, 1, 1) gegen (2, 2, 2): Die Ebene span(1, e8) ist unter ψ fest und hat in O³ kein
  Gegenstück. Die e8-Ladung lässt sich nicht τ-symmetrisch auf drei Plätze setzen (Paarstruktur). Weg B hat ein
  τ-symmetrisches 2 + 1 für alle Arten (τ = diag(ω, ω̄) auf dem Dublett der Slot-Moden), aber nur S_3: zweizählige
  Achsen bei 90°, reeller Slot-Vektor gibt K = 1/2. Komplementär: Weg A hat 2T und Bezug, aber zwei Generationen;
  Weg B drei Generationen und Zyklus, aber keinen magischen Winkel. **Benannte Lücke:** eine zweizählige Achse unter
  dem magischen Winkel auf dem τ-Dublett (S_3 → 2T).
- **14.11., Achse auf dem τ-Dublett** (`op3_tau_doublet_axis_2026_11_14.*`, Erkundung, nicht blind): Die Lücke wird
  nicht geschlossen. Monomiale Slotoperationen (τ, ρ, Vorzeichenwechsel von A_4, slotweise Trialität) geben auf dem
  Dublett nur 0° und 90°; A_4 erhält 2 + 1 gar nicht. Das gesuchte Element überlagert alle drei Slots. Grund: 2T
  braucht ein Dublett aus zwei Slots (Weg A), τ macht das Dublett zum Fourier-Paar (Weg B). **Mit dem jetzigen
  Bestand ist das Profil nicht erfüllbar.** Vierte Variante mit derselben offenen Voraussetzung: hier anhalten.
  Nicht geprüft: eine neue Struktur auf O³ (Jordan-Algebra, F_4); die Trialitätsabbildungen wurden nicht neu gerechnet.
- **Ausgelöste Zurückgestellte Ideen:** I1, Auslöser 4 (14.11.), auf Autorentscheidung verfolgt.

### Heute abend: Ladung über e8 (`notes/research/op3_sedenion_charge_2026_11_13.*`, Erkundung, nicht blind)
- Rückwärtssuche nach jeder Ladung Q auf C⊗S mit diesen Bedingungen: [Q, ψ] = 0, [Q, su(3)_c] = 0, Q̄ = 1 − Q,
  Spektrum {0, 1/3, 2/3, 1} mit 3 → 2/3. Die Bedingung Q|_O = Q8 wurde dabei aufgegeben.
- Der Kommutant hat die Dimension 10. Der farbige Teil ist eindeutig.
- Der farbneutrale Teil ist bis auf zwei Vorzeichen eindeutig: **Q_* = 1/2 − (i/2) L_e8** (oder R_e8). Die
  Ladungsachse ist also e8, die einzige ψ-feste imaginäre Richtung.
- **Ergebnis:** N = ker Q_* = span(1 + i e8, e7 − i e15) ist ein farb- und ladungsneutrales Qubit. ψ wirkt darauf
  als diag(1, ω), also mit Ordnung 3.
- **Offen:** Der Bezug unter dem magischen Winkel ist nicht nativ. Für reelle Elemente mit rationalen Koeffizienten
  ist cos θ rational. Die Diagonale gibt K = 5/9, die Hurwitz-Einheiten K = 1/2. Nötig wäre tan(θ/2) = 2 sin(π/12).
- **Preis:** Q_* lässt O nicht invariant. ε wirkt auf den Leptonen als Ladungskonjugation, die Ladung bricht S3
  also zu Z3. Weg A hat weiterhin nur zwei farbige Generationen (K28).

- **Nächster Schritt:**
  - H100 und H102 auswerten, sobald neue Daten erscheinen:
    - `python notes/research/predictions/k222_test_h100.py dm21 sig21 dm31 sig31` (Spalte mit SK, normale Ordnung,
      asymmetrische Fehler gemittelt; Frist 31.12.2027);
    - `k224_test_h102.py m_tau sigma`.
  - Inhaltlich zur Wahl:
    - **(a)** erledigt am 14.11.: Bezug = Eigenzustand einer Hurwitz-Einheit der Ordnung 3 (2T von rechts).
      Frühere Fassung: einen nativen Bezugszustand in N suchen. Stand 14.11.: H103 widerlegt; der Bezug ist auf die Wahl einer
      Richtung u ∈ Im H_n mit |⟨u, e8⟩| = 1/√3 zurückgeführt (Rechtsmodul). Offen ist, was diese Richtung auszeichnet. Gesucht ist ein Gewicht 2 sin(π/12), zum Beispiel aus einer
      Drehung um π/12 oder aus der Hurwitz-/2T-Struktur über H_n. Querbezug zum Auswahlprinzip: Der Abstand vom
      Oktanten ist dort π/12 − θ_e.
    - **(b)** erledigt am 14.11.: Ladungsinhalt richtig (zwei Generationen), ψ aber kein Generationsschritt.
      Folgefrage: ob der Qubit-Oktant als Zwei-Flavour-Phänomen trägt oder ob Weg B (Triality, drei Generationen)
      ein neutrales Qubit mit derselben Struktur hat.
    - **(c)** erledigt am 14.11.: Die Rechtswirkung von H_n ist eine Familien-su(2) vom Typ 2 (+ 1), Generationen als
      Dublett. Der Majorana-Vektor auf N ist gerechnet und nicht festgelegt. Die dritte Generation als Singulett ist
      gegen Weg B geprüft (Quarks passen, Leptonen nicht). Die Achse auf dem τ-Dublett ist geprüft:
      nicht vorhanden. Empfehlung: die Linie ablegen, bis H100 oder H102 entschieden sind; wahlweise ein
      Statusvermerk zum Profil in einer neuen Runde (Autorentscheidung).
  - Auswahlprinzip (`op3_selection_principle_2026_11_13.*`, `op3_flux_two_thirds_2026_11_13.*`): Treue 1/2 und Fluss
    2/3 rad bleiben offen. γ/2 ist nur mit einer Konventionswahl erreichbar, die Einheit ist frei.
- **Aufgeräumt (14.11.):** Alle in `main` gemergten Zweige sind lokal und auf GitHub gelöscht. Auf GitHub waren das
  20, darunter `codex/*`, `research/v4.10-r06` … `r11` und `research/v5-*`. Der Worktree `qam-mml-mma-math-473bc4` ist
  entfernt; die PDF von dort liegt jetzt im Hauptordner.
  - Bleiben, weil nicht gemergt: auf GitHub `codex/op3-triality-mass-bridge`, `codex/v5-zenodo-release` und
    `codex/v5-zenodo-upload-record`; lokal `claude/quantenphysik-paper-herleitung-e723a3` und
    `claude/wizardly-mendel-c790d3`.
  - `claude/anthropic-skills-weitermachen-08cc3e` ist kein Vorfahre von `main`; sein einziger Commit c84b81b ist
    inhaltsgleich über PR #118 enthalten (`git cherry`). Er steht noch, Löschung braucht ein Wort des Autors.
  - Am 14.11. lokal gelöscht (gemergt): `ct-register-phase2`, `ct003-eintragung`, `claude/zealous-fermi-f46fd7`.
  - `git fetch --prune` meldet „Permission denied“ für verwaiste Einträge unter `.git/worktrees` (`gh_r09`–`gh_r11`,
    `qam-mml-mma-math-473bc4`, `wizardly-mendel-c790d3`).
- **Dauerauftrag des Autors (14.11.):** „bitte lösche zweige die weg können immer“. Gemergte Zweige ohne offenen PR
  werden nach jedem Merge ohne Rückfrage gelöscht, lokal und auf GitHub. Nicht gemergte bleiben stehen. Seit PR #111
  steht das als Regel in `AGENTS.md`.

## Früher am 13.11. erarbeitet, alles gemergt
- **H99b** mit NuFIT-6.1-Primärtabelle: verträglich, +1,80σ (nicht blind). **H100** vorab: R im nächsten NuFIT-Fit,
  A H99 0,030839 · B eine Skala 0,030087 · C Sumino c = 1 0,030375; Erwartung bei gleichem Mittel A ≈ +2,7σ, B ≈ +0,2σ, C ≈ +1,2σ.
- **NuFIT-Verlauf 2012–2025** mit Grafik (`nufit_verlauf_2026_11_13.*`).
- **Varianten zu H99** (`op3_neutrino_phase_candidates_2026_11_13.*`): Skala (Pol oder Kopplung), Koide-Spannung, Sumino-Weg,
  Exponent c = 1,8 ± 1,0.
- **Familien-U(3) und Sonden** (`op3_slot_u3_gauging_2026_11_13.*`): Auslesung A, α_F = 4α mit Überlappung als Feld,
  Zwei-Sonden-System als L/R-Tripel, Neutrino-Block Ω₁.
- **Form η und Fluss** (`op3_eta_form_search_2026_11_13.*`): Brannen-Phase = Bargmann-Phase/3, H99 = Fluss π/4; native
  Phasen geben nur Vielfache von π/6; Hyperladungs-Regel (HH gegen H) nachträglich.
- **Oktanten-Tripel** (exakt): Rand des Koide-Bogens = drei Spin-1/2-Zustände an orthogonalen Achsen; nur Spin 1/2 gibt
  Koide und π/4; Bahn unter der Hurwitz-Einheit −(1+i+j+k)/2 (2T über A4).
- **Trägersuche** (`op3_hopf_octant_*`, `op3_lorentz_octant_*`, `op3_neutral_su2_octant_*`, `op3_sedenion_reference_*`):
  kein farb- und ladungsneutraler nativer Träger (Isospin: Ladung; Oktonionen: Farbe; neutraler Dixon-Teil: Signatur (2,1);
  Sedenionen: ψ dreht die Ladungsachse, keine ψ-verträgliche Fortsetzung der Ladung).
- **Potential und T₁₂** (`op3_koide_potential_2026_11_13.*`): Koide nur mit abgestimmtem Grad-6-Verhältnis; T₁₂ dynamisch
  ohne Vorhersage; Koide = qubitartige Treue (Haar-Mittel in C² genau 2/3), Mittel erklärt die Genauigkeit nicht.

## Profil der fehlenden Struktur
(Teilweise gefunden: Das neutrale Qubit mit Z3 existiert in den Sedenionen, wenn die Ladung über e8 läuft. Es fehlt
der native Bezug.) Gesucht ist ein farb- und ladungsneutrales Qubit, auf dem der Generationszyklus als Element der Ordnung 3 wirkt (Hurwitz-Einheit), mit
einem Bezugszustand unter dem magischen Winkel arccos(1/√3) zur Zyklusachse, sichtbar nur im Majorana-Block.

## Inhaltlicher Stand
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; Guards unverändert. Koide 2/3 und die Phase nicht hergeleitet.

## Pflichten in jeder Sitzung
- `AGENTS.md`, `wiki/Gesamtbild.md`, einschlägige Anleitung unter `notes/anleitungen/`; Auslöser in
  `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen. Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung.
  Merges nur nach Freigabe. Wiki im selben PR. `.codex/environments/` bleibt unversioniert.
