# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 13.11.2026, ca. 23:59 (Claude Opus)
- **GitHub:** **PR #106 gemergt als ca29c5b** (13.11., auf „PR 106 mergen“; Merge-Commit, Kopf 65f4e8e). Läufe 43495772155
  (QSC LaTeX PDF Build), 43495772054 (Zwei-PDF), 43495772194 (Wiki-Sync) erfolgreich. Vorher heute gemergt: #104 (32fa42c),
  #105 (fcc87c6). **Offen: PR #107** (Zweig `research/v5-auswahlprinzip`, Rückwärtssuche Auswahlprinzip), nicht gemergt.
- **Lokal:** Hauptordner per Fast-Forward auf ca29c5b; dieser Übergabe-Commit liegt nur lokal auf `main`. Unversioniert:
  `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf`. Rundentabelle und Kernkarte (Schritt 10 der Runden-Anleitung) gibt es
  im Repo-Klon nicht mehr; Runden stehen in `notes/research/v4_10_0_rNN/README.md` und im Wiki.
- **Letzte Runde:** v4.10.0-r12 (Statusvermerke), Teil von PR #106; Build lokal und in CI ok (1406 Seiten, 0 Overfull).
- **Zuletzt vergebene Hypothese:** H100 (Vorab 9c77ddd, offen); nächste frei H101; letztes Skript k222.
- **Offene Autorentscheidungen:** keine.
- **Ausgelöste Zurückgestellte Ideen:** keine neuen (I4 durch den ν^c-Kanal berührt, am 6.11. bereits negativ eingeordnet).
- **Nächster Schritt:** H100 auswerten, sobald eine neue NuFIT-Version erscheint:
  `python notes/research/predictions/k222_test_h100.py dm21 sig21 dm31 sig31` (Spalte mit SK, normale Ordnung,
  asymmetrische Fehler gemittelt; Frist 31.12.2027).
  · Auswahlprinzip (Rückwärtssuche 13.11., `op3_selection_principle_2026_11_13.*`): zwei Zahlen festzulegen, Treue 1/2 und
    Abstand vom Qubit-Oktanten (= √m_e/⟨√m⟩ ≈ π/12 − θ_e = 0,04); offen.
    **Herleitungsversuch:** K = (1 + cos²β)/2 für Qubit-Bahnen; in A4 ist 2/3 der einzige Wert ⇒ Koide bedingt hergeleitet
    (Qubit-Träger, Klein-ℤ₂-Bezug, ℤ₃-Bahn = Auslesungen aus r55). Elektronmasse = A4-Bruch, Größe offen; Kandidat
    Generationsmaske r47 (nur mit Vorab-Notiz prüfen).
  · zur Wahl: zweite Familienstruktur mit neutralem Qubit (Profil unten) ·
  Fortsetzung der Ladung auf die Sedenionen anders als über e7.
- **Aufräumen:** Zweig `research/v5-octant-weitersuche` (PR #106) und Worktree `.claude/worktrees/qam-mml-mma-math-473bc4`
  können weg.

## Heute (13.11.) erarbeitet, alles gemergt
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
Ein farb- und ladungsneutrales Qubit, auf dem der Generationszyklus als Element der Ordnung 3 wirkt (Hurwitz-Einheit), mit
einem Bezugszustand unter dem magischen Winkel arccos(1/√3) zur Zyklusachse, sichtbar nur im Majorana-Block.

## Inhaltlicher Stand
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; Guards unverändert. Koide 2/3 und die Phase nicht hergeleitet.

## Pflichten in jeder Sitzung
- `AGENTS.md`, `wiki/Gesamtbild.md`, einschlägige Anleitung unter `notes/anleitungen/`; Auslöser in
  `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen. Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung.
  Merges nur nach Freigabe. Wiki im selben PR. `.codex/environments/` bleibt unversioniert.
