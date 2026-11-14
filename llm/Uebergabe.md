# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 14.11.2026 (Claude Opus)
- **GitHub:** **PR #109 gemergt als 963f557** (R_f-Nachtrag zu H103, Erkundung), auf „PR 109 mergen“; Läufe 43537048238
  (Wiki-Sync) und 43537048230 (Zwei-PDF) erfolgreich. **Offen: PR #110** (Generationen unter Q_*).
  **PR #108 gemergt als 91cbb69** (Ladung über e8, neutrales Qubit, H103 widerlegt).
  Am 13.11. gemergt: #104 (32fa42c), #105 (fcc87c6), #106 (ca29c5b), #107 (a08d918).
  Läufe 43534883771 (Wiki-Sync) und 43534883722 (Zwei-PDF) zu 91cbb69 erfolgreich.
- **Lokal:** Der Hauptordner steht auf `main` = 963f557 (vorgespult), dazu dieser Übergabe-Commit, nur lokal.
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
- **Offene Autorentscheidungen:** „PR 110 mergen“ (Generationen unter Q_*, Zweig `research/v5-generationen-qstar`).
- **14.11., Generationen unter Q_*** (`op3_sedenion_generations_estar_2026_11_14.*`, Erkundung, nicht blind):
  C⊗S hat unter Q_* genau zwei vollständige Generationen. Die ψ-Sektoren sind aber keine Generationen
  (1: ν, e⁺; ω: ν, u, d̄; ω̄: e⁺, u, d̄). ψ wirkt innerhalb der Generationen als Phase und ist kein Generationsschritt.
  N ist der Raum zweier Neutrino-Flavours; der dritte fehlt (K28).
- **Ausgelöste Zurückgestellte Ideen:** keine. I1–I5 sind geprüft.

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
    - **(a)** einen nativen Bezugszustand in N suchen. Stand 14.11.: H103 widerlegt; der Bezug ist auf die Wahl einer
      Richtung u ∈ Im H_n mit |⟨u, e8⟩| = 1/√3 zurückgeführt (Rechtsmodul). Offen ist, was diese Richtung auszeichnet. Gesucht ist ein Gewicht 2 sin(π/12), zum Beispiel aus einer
      Drehung um π/12 oder aus der Hurwitz-/2T-Struktur über H_n. Querbezug zum Auswahlprinzip: Der Abstand vom
      Oktanten ist dort π/12 − θ_e.
    - **(b)** erledigt am 14.11.: Ladungsinhalt richtig (zwei Generationen), ψ aber kein Generationsschritt.
      Folgefrage: ob der Qubit-Oktant als Zwei-Flavour-Phänomen trägt oder ob Weg B (Triality, drei Generationen)
      ein neutrales Qubit mit derselben Struktur hat.
    - **(c)** die zweite Familienstruktur mit neutralem Qubit (Profil unten).
  - Auswahlprinzip (`op3_selection_principle_2026_11_13.*`, `op3_flux_two_thirds_2026_11_13.*`): Treue 1/2 und Fluss
    2/3 rad bleiben offen. γ/2 ist nur mit einer Konventionswahl erreichbar, die Einheit ist frei.
- **Aufgeräumt (14.11., auf „Erst aufräumen“):**
  - entfernt: Worktree `qam-mml-mma-math-473bc4`;
  - lokal und auf GitHub gelöscht: die Zweige `research/v5-octant-weitersuche` und `research/v5-auswahlprinzip`;
  - auf GitHub gelöscht: `research/v5-sedenion-ladung-e8`.

  Alle drei waren vollständig in `main` enthalten. Die PDF `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf` lag
  nur im entfernten Worktree und ist vorher in den Hauptordner kopiert worden (byte-gleich geprüft).
  Übrig sind der Worktree dieser Sitzung (`anthropic-skills-weitermachen-08cc3e`, Zweig gemergt; wird mit dem
  Archivieren der Sitzung entfernt) und der gemergte Zweig `research/v5-rf-nachtrag` auf GitHub (kann weg). Nicht angefasst: `wizardly-mendel-c790d3` und `github-main`.

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
