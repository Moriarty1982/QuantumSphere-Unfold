# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 14.11.2026 (Claude Opus)
- **GitHub:** **PR #113 gemergt als 10d670e** (CT-001-Entwurf, Platzhalter-Methode Schritte 1–3), auf „PR 113
  mergen“; Läufe 43543589360 (Wiki-Sync) und 43543589359 (Zwei-PDF) erfolgreich. Zweig gelöscht.
  Am 14.11. außerdem gemergt: #112 (ad7756f, Hurwitz/2T), #111 (c247ea3, AGENTS.md), #110 (8606691), #109 (963f557),
  #108 (91cbb69). Am 13.11.: #104–#107.
  Auf GitHub liegt außerdem `claude/zealous-fermi-f46fd7` aus der Sitzung „Counterterm-Registry Phase 1“; er ist noch
  nicht gemergt und bleibt stehen. **Offen: PR #114** (I1-String-Brücke).
- **Lokal:** Der Hauptordner steht auf `main` = 10d670e (vorgespult), dazu dieser Übergabe-Commit, nur lokal.
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
- **Offene Autorentscheidungen:** „PR 114 mergen“ (Zweig `research/i1-string-bruecke`).
- **Counterterm-Registry (14.11.):** Der Autor will damit Rapid Prototyping betreiben: Gegenterme setzen und später
  durch Herleitungen ersetzen. Phase 1 läuft in einer eigenen Sitzung (Schema, Validator, Weitergabe der Guards,
  Fixture CT-000-TEST). Ergänzt um die Herkunft der Fitdaten, eine Blindheitsprüfung, Δ als Prüfstein sowie diskrete
  Konventionswahlen mit Versuchszahl. Phase 2 ist die Exporttabelle.
  **Erster echter Platzhalter (Autorenwahl): CT-001, die Einheit bei ΔΦ = γ_M/2.** Der Entwurf liegt unter
  `notes/research/counterterms/CT-001_gamma_halbe_einheit_entwurf.md`; registriert wird er nach dem Merge von Phase 1.
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
- **14.11., Hurwitz-Einheiten auf N** (`op3_hurwitz_2t_neutral_qubit_2026_11_14.*`, Erkundung, nicht blind):
  Die 24 Hurwitz-Einheiten von H_n wirken von rechts treu auf N als 2T (projektiv A4). N ist also ein natives
  2T-Dublett. Die ψ-Achse e8 ist zweizählig, die vier dreizähligen Achsen liegen unter 1/√3 dazu. Der Bezug ist ein
  Eigenzustand einer Hurwitz-Einheit der Ordnung 3 und gibt K = 2/3, π/4. ψ normalisiert 2T nicht. Die Frage zu Weg B
  war schon beantwortet (`op3_neutral_su2_octant`, Punkt 3: dort nur der A4-Vektor).
- **14.11., Generationen unter Q_*** (`op3_sedenion_generations_estar_2026_11_14.*`, Erkundung, nicht blind):
  C⊗S hat unter Q_* genau zwei vollständige Generationen. Die ψ-Sektoren sind aber keine Generationen
  (1: ν, e⁺; ω: ν, u, d̄; ω̄: e⁺, u, d̄). ψ wirkt innerhalb der Generationen als Phase und ist kein Generationsschritt.
  N ist der Raum zweier Neutrino-Flavours; der dritte fehlt (K28).
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
    - **(c)** die zweite Familienstruktur mit neutralem Qubit (Profil unten).
  - Auswahlprinzip (`op3_selection_principle_2026_11_13.*`, `op3_flux_two_thirds_2026_11_13.*`): Treue 1/2 und Fluss
    2/3 rad bleiben offen. γ/2 ist nur mit einer Konventionswahl erreichbar, die Einheit ist frei.
- **Aufgeräumt (14.11.):** Alle in `main` gemergten Zweige sind lokal und auf GitHub gelöscht. Auf GitHub waren das
  20, darunter `codex/*`, `research/v4.10-r06` … `r11` und `research/v5-*`. Der Worktree `qam-mml-mma-math-473bc4` ist
  entfernt; die PDF von dort liegt jetzt im Hauptordner.
  - Bleiben, weil nicht gemergt: auf GitHub `codex/op3-triality-mass-bridge`, `codex/v5-zenodo-release` und
    `codex/v5-zenodo-upload-record`; lokal `claude/quantenphysik-paper-herleitung-e723a3` und
    `claude/wizardly-mendel-c790d3`.
  - Der Zweig dieser Sitzung, `claude/anthropic-skills-weitermachen-08cc3e`, ist gemergt, aber noch ausgecheckt. Er
    verschwindet mit dem Worktree beim Archivieren.
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
