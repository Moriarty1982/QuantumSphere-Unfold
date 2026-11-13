# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 13.11.2026, ca. 20:30 (Claude Opus)
- **GitHub:** **PR #104 gemergt als 32fa42c** (13.11., auf „pr 104 mergen“; Merge-Commit, Kopf bf51772).
  Läufe 43481979108 (Zwei-PDF) und 43481979426 (Wiki-Sync) erfolgreich. **Offen: PR #105** vom Zweig
  `research/v5-h100-eta` (H100-Vorab 9c77ddd, η-Suche, Wiki); nicht gemergt.
- **Lokal:** Hauptordner auf `main` f405c05 (Übergabe-Commit nach dem Merge, liegt in PR #105).
  Unversioniert: `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf`.
- **Zuletzt vergebene Hypothese:** **H100** (Vorab 9c77ddd, offen bis zur nächsten NuFIT-Version, längstens 31.12.2027);
  nächste frei H101; letztes Skript k222. Auswertung: `python k222_test_h100.py dm21 sig21 dm31 sig31`.
- **Offene Autorentscheidungen:** PR #105 mergen („PR 105 mergen“).
- **Ausgelöste Zurückgestellte Ideen:** keine.
- **Nächster Schritt:** Spinor-Transport geprüft: raumzeitlich ausgeschlossen; innerer Transport π/6 je Kante gibt
  Φ_ν − Φ_e = (q_L − q_R)·π/2, H99 verlangt q_L − q_R = 1/2 = Hyperladung des Higgs (nachträglich, schwach).
  Dixon-Sektorphase geprüft: Struktur passt (e/ν nur im Vorzeichen von φ_H), Zahl nicht (H99 verlangt ungerade
  Vielfache von π/24; Verbinder-Differenz 1 gibt π/6), Quark-Spiegelung widerspricht Daten. Als Nächstes: Quelle der
  halben Ladungsdifferenz (ℓ_L gegen e_R) im Companion suchen; alternativ ν^c-Verbinder (r44.1(d)); oder Pause bis
  zur nächsten NuFIT-Version (H100).
  Werkzeuge: `notes/research/op3_eta_form_search_2026_11_13.*`, `op3_slot_u3_gauging_2026_11_13.*`.
  · zur Wahl: H100 vorab festschreiben (Kandidaten unten) · T₁₂ als dynamisches Feld · Potential für ρ² = 1/2 ·
  Vereinigung Platzindex-U(3) mit SU(2)_L.
- **Aufräumen:** Zweige `research/v5-string-relaxation-rueckwaertssuche` (PR #103) und `research/v5-h99b-nufit61`
  (PR #104) können weg; Worktree `qam-mml-mma-math-473bc4` ebenso.

## Block 19:40–20:30 (PR #105)
- **H100** vorab (siehe oben); Erwartung bei gleichem Mittelwert: A ≈ +2,7σ, B ≈ +0,2σ, C ≈ +1,2σ.
- **Form η** (`op3_eta_form_search_2026_11_13.*`): Brannen-Phase = Bargmann-Phase/3; H99 ⇔ ΔΦ = π/4 bei gleichen
  Beträgen. Ausgeschlossen: Umphasen, Vorzeichen in der Eigenbasis, hermitesch → bilinear allein (0/4000).
  Verlangt: Fluss π/4 durch das Platzdreieck (hermitesch möglich). Native Phasen ω, i, −1 geben nur Vielfache
  von π/6 (Paritätsargument). π/4 = Bargmann-Phase eines koplanaren Koide-Tripels.

## Block 15–19 Uhr, alles in PR #104 (gemergt)
- **H99b** mit NuFIT-6.1-Primärtabelle (IC24 mit SK): verträglich, +1,80σ (nicht blind). Sekundärwerte überholt.
- **NuFIT-Verlauf 2012–2025** (`nufit_verlauf_2026_11_13.*`, Grafik): Δm²₂₁ flach; Δm²₃₁ bis 2017 gestiegen;
  R lag 2013/14 nur wegen des niedrigen Δm²₃₁ beim H99-Wert.
- **Varianten zu H99** (`op3_neutrino_phase_candidates_2026_11_13.*`): 24er-Raster, nur H99-Form passt. Skala:
  jede kurzreichweitige Skala gibt R ≈ 0,0301 (+0,16σ); Wahl ist Pol oder Kopplung. Koide-Spannung: Pol-Koide
  kein Zufall. Sumino (arXiv:0812.2103): Familienkorrektur hebt QED auf; Neutrinos mit c = 1 (PMNS-gemittelt)
  +0,7σ; c für z = 0 ist 1,8 ± 1,0 (c als Verhältnis zweier Log-Integrale).
- **Familiensymmetrie** (`op3_slot_u3_gauging_2026_11_13.*`): keine native; Platzindex-U(3) geeicht ⇒ Bosonen
  massiv. Auslesung A (√m ∝ s) gewählt (nur sie trägt die negative Neutrino-Wurzel). α_F = 4α, wenn die
  Überlappung das Feld ist. **Zwei-Sonden-System** (prop:triadic-two-probe) liefert L/R-Tripel, T₁₂ als
  Massenblock (±s), Ψ_⊥ als dritten Platz. **Neutrino-Block** Ω₁ ∝ Xᵀ η X: c = 1, Signatur (2,1) ⇒ genau eine
  negative Wurzel; Seesaw mit geladener Struktur und Tensorprodukt ausgeschlossen; Sektorunterschied liegt ganz in η.

## Kandidaten für H100 (noch nicht festgeschrieben)
- H99 (Pol): R = 0,030840 · Kopplungsseite (eine Skala): R ≈ 0,0301 · Sumino c = 1, PMNS-gemittelt: R ≈ 0,0304.
  Künftige JUNO-Daten trennen H99 von den beiden anderen mit etwa 2–3σ. Kriterium und Wahl vorab festlegen.

## Inhaltlicher Stand
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert. Koide 2/3 und die Phase nicht hergeleitet.
- Tragendes Bild (Erkundung): drei Plätze, Gram-Auslesung A, Zwei-Sonden-Block für Dirac-Massen, Majorana-Block
  mit indefiniter Form für Neutrinos, Familien-U(3) auf dem Platzindex. Fehlt: native η, Dynamik von T₁₂,
  Potential, α_F.

## Pflichten in jeder Sitzung
- `AGENTS.md`, `wiki/Gesamtbild.md`, einschlägige Anleitung unter `notes/anleitungen/`; Auslöser in
  `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen. Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung.
  Merges nur nach Freigabe. Wiki im selben PR. `.codex/environments/` bleibt unversioniert.
