# Übergabe: Stand der letzten Sitzung

**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.** Sie ist der Einstiegspunkt für die nächste Sitzung, egal mit welchem Modell. Die Geschichte steht in `AGENTS.md` (Rundentabelle), in der Kernkarte und in den Runden.

## Stand vom 6. November 2026 (Claude)
- **PR #72 gemergt als e6e55cc** (6.11.; `research/v4.10-r86-wolfram-pruefung`, https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/72), Runde **v4.9.0-r86**: unabhängige Prüfung mit Wolfram, H87 (a, c bestätigt, b widerlegt wie formuliert), H88 bestätigt (W1-Feldgleichungen), H89 bestätigt (Energie-Impuls-Tensor; T^(4f) Λ-Form, homogen ρ = p > 0), Korrektur r86.4 zur Lesart der W1-Notiz. Inhalt: Runde in `parts/v490-post-release-layers.tex`, Notizen `notes/research/v4_10_0_r86/` (k202–k204), H87–H89 unter `predictions/`, W1-Notiz mit Nachträgen, Wiki (6 Seiten), ours-Merge der lokalen Historie bis f4b1ebc. CI-Build auf dem Zweig per workflow_dispatch angestoßen. CI-Lauf 42129615268 grün; AGENTS-Zeile und Kernkarte nachgezogen. Wiki-Sync läuft nach dem Merge automatisch.
- **Lokal eingebaut (f4b1ebc):** 1335 Seiten, 3982 Labels, harte Werte 0, Guard-Linter 0. Overfull 58 unter MiKTeX 25.12 (keine in r86; TeX Live liefert 45). Kandidat lokal gebaut: 1361 Seiten, harte Werte 0. AGENTS-Zeile r86, Kernkarte K136 (v15.2). **Nächste Bundle-/ours-Basis: der Commit dieser Übergabe** (Repo-Worktree teilt Objekte mit dem lokalen Repo, kein Bundle nötig).
- GitHub-Worktree `$HOME/gh_r86` nach dem Merge entfernt; Zweig `research/v4.10-r86-wolfram-pruefung` kann weg.
- **Zuletzt vergebene Hypothese:** H89. Nächste freie Nummer **H90**.
- **Zurückgestellte Idee I3** (Λ als Folge der Dunkle-Materie-Rechnung): Auslöser „weitere Λ-Rechnung“ durch H89 berührt (Vier-Fermionen-Term in Λ-Form), dem Autor genannt.
- **Branches, die weg können** (Löschen über den Proxy gesperrt): `rechnen/h59`, `rechnen/h65`, `rechnen/h67`, `rechnen/hintergrund`, `research/v4.10-w1-wirkung-test`, die gemergten `research/v4.10-r69…r85-*`.

## Release v4.10.0 in Vorbereitung (Autor 6.11.: „Ja, vorbereiten“)
- Zweig **`release/v4.10.0-prep`** auf GitHub (9708427), Worktree lokal unter `$HOME/rel410`. Enthält `release/zenodo/metadata_v4_10_0.json` (Beschreibung aus belegtem Inhalt, Guard-Linter 0, Version-DOI als Platzhalter „[to be filled after reservation]“, `publication_date` vorläufig 2026-11-06) und das Gesamtbild auf Stand nach r86.
- Trockenlauf der Reservierung grün (Lauf 42130551910, `new_version_of=23534954`, alle Eingaben gesetzt).
- **Nächster Schritt, braucht Freigabe:** Reservierung mit `dry_run=false` (legt einen unveröffentlichten, verwerfbaren Entwurf an). Danach: DOI in Metadaten, CLAUDE.md/AGENTS.md (DOI-Disziplin, reserviert), `CITATION.cff`, Titelseite (`sources/research/parts/working-preamble.tex`: `\workingversion` 4.10.0, Version-DOI-Zeile, `pdftitle`/`pdfsubject`), `qs.py doi --version-doi`, Payload unter `release/v4.10.0/` (Vorschlag: Einzeldatei wie v4.9.0; PDF aus dem TeX-Live-Container), Manifest, README; PR; Upload mit `deposition_id` und `replace_files=true`; Autor prüft den Entwurf; Veröffentlichen nur auf ausdrückliches Wort.
- **Nach der Veröffentlichung nicht vergessen (Autor 6.11.):** Tag `v4.10.0` und GitHub-Release auf dem Merge-Commit setzen, `DOI_ROLES` in `qs.py`, DOI-Disziplin umstellen; künftige Runden heißen `v4.10.0-rNN`.
- Overfull: 58 unter MiKTeX, 45 unter TeX Live (toolchain-abhängig, laut Release-Anleitung); kein Befund.

## Nächster Schritt (Autor wählt)
1. Volle nichtlineare Einstein-Gleichung und Bianchi-Identität von W1 (Wolfram, in Teile zerlegt wegen ca. 100 s Laufzeitgrenze; `llm/k204_w1_einstein.wl` als Ausgang).
2. Vorab festgelegter Test des Abfalls e^{−πkΔ} mit Potenzvorfaktor bis kΔ ≈ 60 (Fit-Modell vorab festlegen; `llm/k202_wolfram_gegenprobe.wl`).
3. Übergangsbedingung für Fermionen am Urknall (G2); Bedeutung der Asymmetrie der Drehsinne; Dauer Δ; Vergleich mit Boyle–Finn–Turok; G mit γ¹ statt γ² gegen r19; I1; Skala von Λ; I3 (Auslöser berührt).
- Offene Vorhersagen H15, H42, H46 warten auf Daten.

## Pflichten in jeder Sitzung
- Auslöser in `llm/Zurueckgestellte_Ideen.md` prüfen (beim Start und wenn ein Ansatz scheitert).
- Zuerst `AGENTS.md` lesen, dann die einschlägige Anleitung mit dem Abschnitt „Bereits beantwortet“, dann diese Datei.
- Vorwissen-Pflicht und Vorab-Notizen beachten. Merges nur nach „PR NN mergen“.
- Wiki im selben PR mitziehen.
- Am Ende diese Datei aktualisieren.

## Davor (5.11., 23:20)
- **PR #70 gemergt als a5bf106** (5.11., 23:13; `research/v4.10-r85-urknall-cpt`), Runde **v4.9.0-r85**: H82–H86, Erkundungen Spinorphase und Urknall, Autorentscheidung G2, Arbeitsannahme F3-Gewicht 1. Wiki im PR; Bestandsaufnahme auf GitHub aktualisiert. ours-Merge der lokalen Historie bis 13d4432 (Vorab-Commits c3f956c, 36ec8e7, d2a19f2, 4ac77a0, 851297a). CI-Lauf 42119464656.
- **Lokal eingebaut (13d4432):** 1331 Seiten, 3977 Labels, Overfull 45, harte Werte 0, Guard-Linter 0. AGENTS-Zeile r85, Kernkarte K135 (v15.1). **Nächste Bundle-Basis: 13d4432.**
- **PR #71 gemergt als 9adebdc** (5.11., 23:19; `docs/wiki-stand-r85`): nur Wiki, zieht Home, Gesamtbild (Thesen T1, T9, T10, T11, Mindmap, Entwicklung r75–r85), Hinweise für LLMs, Versionen und Quellen, Begriffe, Dokumentführer und Vorhersagen-Kopf auf den Stand nach r85.
- **Wolfram-Connector verbunden (5.11., 23:21).** **H87 (Vorab 61b7132, nicht blind, Code `llm/k202_wolfram_gegenprobe.wl`):** c bestätigt (Formeln scharfer Übergang symbolisch), a bestätigt (H86-Werte unabhängig auf ≤ 5·10⁻⁷), b widerlegt wie formuliert (Steigung 20–30 = 2,956, 5,9 % unter π; lokale Steigungen steigen langsam). Methode: Integration entlang τ = x + ih unterhalb der Singularität iπΔ/2 (gut konditioniert, |C| bis 10⁻³⁷). Nachträglich: Fit mit (kΔ)^p e^{−s kΔ} gibt s ≈ π (3,15 bzw. 3,08), p ≈ 3–5. `llm/Ergebnis_H87_Wolfram_Gegenprobe_Abfall.md`. Hinweis: Wolfram-Cloud bricht Rechnungen > ca. 100 s ab (Bad Gateway).
- **H88 bestätigt (Vorab 06a8380, nicht blind, Wolfram, `llm/k203_w1_feldgleichungen.wl`):** W1-Feldgleichungen unabhängig hergeleitet: Erzeuger kovariant, Torsion −(3/16)κ j·j aus den Definitionen (24 Kontorsionskomponenten, zwei Weyl-Spinoren), Weyl-Gleichung exakt, Ward-Identität. Keine Abweichung. Offen: Einstein-Gleichung von W1 und Bianchi-Identität (Laufzeitgrenze). Nachtrag in `llm/Wirkung_W1_Dixon_U1.md`. Noch nicht auf GitHub: H87, H88 → Runde r86.
- **H89 bestätigt (Vorab 6355d15, nicht blind, Wolfram, `llm/k204_w1_einstein.wl`):** T^(4f) = (3κ/16) j² g (Λ-Form allein); homogener Zustand ρ = p = (3κ/16)n² > 0; Vierbein-Variation erster Ordnung = −Belinfante, symmetrisch. Offenlegung: zwei Fehler in meinem Prüfcode (ConjugateTranspose, η-Faktoren in ωΣ), nach Konventionsprüfung gefunden. Nachtrag mit Korrektur in `llm/Wirkung_W1_Dixon_U1.md` (Vorzeichen von ρ, Λ-Form des 4f-Terms). Offen: volle nichtlineare Einstein-Gleichung, Bianchi. Noch nicht auf GitHub: H87–H89, Nachträge W1 → Runde r86.
- **Nächste Schritte zur Wahl:** Übergangsbedingung für Fermionen am Urknall (G2); Bedeutung der Asymmetrie der Drehsinne (Teilchen/Antiteilchen?); Dauer Δ des Übergangs (Skala); Vergleich mit Boyle–Finn–Turok (dunkle Materie als ν^c, r82.4); Gravitation und r19 (G γ¹ statt γ²); I1; Skala von Λ.
