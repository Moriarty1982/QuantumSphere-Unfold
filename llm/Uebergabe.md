# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 13.11.2026, ca. 19:20 (Claude Opus)
- **GitHub:** zuletzt gemergt PR #103 als 83b2551 (OP3 nach v5.0.0, H99). **Offen: PR #104** (Zweig
  `research/v5-h99b-nufit61`, Kopf efe8360 plus dieser Übergabe-Commit), nicht gemergt; enthält auch den
  früheren lokalen Übergabe-Commit 0504201. Keine laufenden Actions; Wiki-Sync und Zwei-PDF zuletzt grün (43370355406/…373).
- **Lokal:** Hauptordner auf `main` 0504201 (nur lokal, liegt in PR #104). Arbeit lief im Worktree
  `.claude/worktrees/qam-mml-mma-math-473bc4`. Unversioniert: `llm/literatur/Dorau_Much_2026_arXiv_2510.24491v3.pdf`.
- **Zuletzt vergebene Hypothese:** H99 (nächste frei H100); letztes Skript k221. Alle Arbeiten seit H99b sind
  Erkundungen, nicht blind, ohne H-Nummer.
- **Offene Autorentscheidungen:** PR #104 mergen („PR 104 mergen“). H100 festschreiben oder erst η suchen.
- **Ausgelöste Zurückgestellte Ideen:** keine.
- **Nächster Schritt:** native Form η im neutralen Sektor suchen, die ρ² erhält und die Phase um den Bogenrand
  θ_b verschiebt (präzise Fassung des Ursprungs von H99). Werkzeuge: `notes/research/op3_slot_u3_gauging_2026_11_13.*`,
  `op3_indefinite_form_2026_11_13.md`, r44.1, r55.
  · zur Wahl: H100 vorab festschreiben (Kandidaten unten) · T₁₂ als dynamisches Feld · Potential für ρ² = 1/2 ·
  Vereinigung Platzindex-U(3) mit SU(2)_L.
- **Aufräumen:** Zweig `research/v5-string-relaxation-rueckwaertssuche` kann weg (PR #103 gemergt).

## Dieser Block (13.11., 15–19 Uhr), alles in PR #104
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
