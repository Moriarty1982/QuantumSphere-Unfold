# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Werkzeug zuerst

Für Querverweise, Rundenanlage, Guard-Prüfung, Ledger und Manifest gibt es den
Skill `quantum-sphaera` mit dem CLI `.claude/skills/quantum-sphaera/tools/qs.py`.
Theoremnummern **nie** von Hand zählen — `qs.py xref` bildet die LaTeX-Zähler nach.

## Was dieses Verzeichnis ist

Kein Software-Repository im üblichen Sinn, sondern ein einzelnes LaTeX-Monolith-Dokument: der *Quantum Sphaera Companion*, ein mathematisches Preprint von Marc Brendecke (über 1000 PDF-Seiten, über 71.000 Quellzeilen, rund 3,8 MB `.tex`). Keine Build-Skripte, keine Tests im üblichen Sinn. Die Qualitätssicherung läuft über LaTeX-Compile-Audits und Claim-Scope-Disziplin.

## Versionskontrolle

Git-Repository, Branch `main`, 74 Commits von v0.6.0 bis heute. Ein Commit pro Dokumentstand.

```
v0.6.0     1.238 Zeilen   Beginn der archivierten Historie
v1.0.0     1.378
v2.9.0     6.933
v3.0.0    20.034
v4.0.0    35.108          ab hier zweigeteilt: Kern + historischer Teil
v4.4      49.615          zu einem Monolithen zusammengeführt
v4.6.0    53.160
RC19      63.202  r84     Datei trägt ab hier ihren Release-Namen
RC20              r85     Zitatreparatur, Scope-Trennung
RC21              r86     C5-Kollar-Konsolidierung (Q5)
RC22              r88     Fensterkalibrierung (Q3), Non-Collar-Routen
                          — r87 darin fehlerhaft, siehe r89
                  r89     Korrektur von r87
RC23/RC24         r90/r91 Δ_γ-Rekonstruktion, Q4 ausgeführt
v4.8.0    65.000+ r94     + v4.8.0-r01 (Planck-Readout), r02 (Release)
RC25      67.700+ v480-r20 v4.8.0-r03 bis r20 auf dem Release; nur Tag, keine Snapshot-Datei
```

Bis v4.6.0 heißt die Datei `companion.tex` (bei zweigeteilten Ständen zusätzlich `companion_historical.tex`), ab RC19 `Quantum_Sphaera_Companion_v4_7_0_source.tex`, ab v4.8.0 `Quantum_Sphaera_Companion_v4_8_0_source.tex`. Git erkennt die Übergänge als Rename, `git log --follow` läuft durch.

**Die Daten vor v4.0.0 sind Archivierungs-, keine Entstehungsdaten** — die Quelldateien stammen aus einem Download-Ordner, in dem ganze Versionsblöcke denselben Zeitstempel tragen. Die *Reihenfolge* stimmt (aus den Versionsnummern), die Tage nicht. Ab v4.0.0 kommen die Daten aus den Release-Archiven und sind belastbar.

Aufgenommen sind die 58 Hauptversionen `x.y.0` aus v0–v3 plus alle v4-Stände. Die Mikroversionen (etwa v2.26.1 bis v2.26.44) und die Arbeitsstände liegen weiterhin in `C:\Users\marcb\Downloads\Quantum Sphere`. Zwei Versionen (v3.17.0, v3.29.0) fehlen: dort existiert nur eine Wrapper-Datei ohne Volltext.

**`.gitattributes` mit `* -text` ist nicht verhandelbar.** Die SHA256-Werte in den Manifesten gelten für die Bytes der Dateien. Jede Zeilenenden-Konvertierung beim Checkout würde jeden dieser Hashes brechen und die Provenienzkette entwerten. Verifiziert: ein Checkout von Tag `RC19` reproduziert `019e7a35…` exakt.

**PDFs sind ignoriert** — sie sind aus dem Quelltext reproduzierbar und machen über 75 % des Ordners aus; ihre Prüfsummen stehen in den Manifesten. Einzige Ausnahme ist `Quantum_Sphaera_Companion_v4_7_0.pdf` (RC19): es stammt aus einer anderen Toolchain (45 statt 58 Overfull) und lässt sich nicht bitgenau nachbauen.

**Künftige RCs brauchen keine Snapshot-Datei mehr.** Ein Tag leistet dasselbe. Die vorhandenen `..._RC19..._RC22_*_source.tex` bleiben, weil die Manifeste sie hashen — neue nicht mehr anlegen.

**Verhältnis zu GitHub** (`github` = `Moriarty1982/QuantumSphere-Unfold`). Die lokale Historie ist aus Archiven rekonstruiert und hat **keinen gemeinsamen Vorfahren** mit `github/main`; Inhalte werden übertragen, nicht gemergt. Auf GitHub ist der Kandidat modular (`sources/research/v480-companion.tex`); die 38 v4.7-Fragmente in `parts/v470/` waren bis v4.9.0 **eingefroren**; seit der **4.10-Basis** (PR #25, 2026-10-22, Autorentscheidung) sind sie nach der Überarbeitungsregel aus r25 editierbar, der eingefrorene Stand liegt unter Tag `v4.9.0`. Der Kandidat trägt `\workingversion` = `4.10.0-draft`, das Archiv steht in `parts/v4100-archive.tex`. Die Runden liegen dort wortgleich in `parts/v480-release-layers.tex` (r85–r94), `parts/v480-post-release-layers.tex` (v4.8.0-r01–r20) und `parts/v490-post-release-layers.tex` (v4.9.0-r01–r31), Notizordner `notes/research/v4_8_0_r03_r12/`, `v4_9_0_r01_r16/`, `v4_9_0_r17_r19/`, `v4_10_0_base/`, `v4_10_0_r26_r31/`. Übertragen: PR #19 (`b2a05a5`), PR #23 (`67f965f`, r01–r16), PR #24 (`0480f89`, r17–r19), **PR #25 (4.10-Basis: Überarbeitung des Hauptkorpus in den Fragmenten, r20–r25; am 2026-10-22 gemergt, `1dbc0e8`, Build auf `main` grün)**, **PR #27 (r26–r31 und erweiterter Statusvermerk zu thm:dark-energy; am 2026-10-22 gemergt, `b240e56`, Build auf `main` grün)**; Lokalgeschichte auf `research/v4.8.0-r03-r12-lokalgeschichte` bis zum jeweils letzten lokalen Commit gepusht (2026-10-23); **PR #28** (v4.9.0-r32 und r33, Dixon-Prüfung, H17/H18, `formal/QSFormal/Dixon.lean` und `Lesarten.lean`, Notizordner `notes/research/v4_10_0_r32_r33/`, neuer Workflow `.github/workflows/lean-build.yml`: `lake build` mit Mathlib-Cache, Prüfung auf sorry/admit/native_decide und Axiome) am 2026-10-23 vom Autor gemergt (`a1d28ed`), Zweig gelöscht; LaTeX- und Lean-Build auf `main` grün. **PR #29** (QSC-Audit-MCP-Server `mcp/qsc_mcp_server.py` für MCP-SDK 1.x und 2.x mit `run_guard_lint`, `list_layers`, `build_research_candidate`; Audit-Skripte in `scripts/qsc_audit/` beschleunigt, Freeze-Audit 12 s statt > 20 min) am 2026-10-23 gemergt (`a046885`), schließt Issue #3; Release-Audit auf `main` grün. **PR #30** (v4.9.0-r34 bis r47, Statusvermerke an thm:three-generations und thm:SM über `llm/revision_spec_v490_r36.py`, Notizordner `notes/research/v4_10_0_r34_r47/`, Lean-Modul `formal/QSFormal/Ladungen.lean`; Kandidat 1224 → 1259 Seiten, Lean-Workflow grün) am 2026-10-24 gemergt (`f650e12`); Zweig `research/v4.10-r34-r42` kann weg (Löschen über den Proxy gesperrt). **PR #31** (2026-10-24, `8595193`): Die lokale Historie (270 Commits bis `a93f82d`) ist per `git merge -s ours --allow-unrelated-histories` in die Geschichte von `main` aufgenommen, ohne Dateiänderung; die Commits der Vorab-Notizen sind damit von `main` aus erreichbar. **Künftig:** neue lokale Commits auf einen Zweig von `main` per ours-Merge nachführen (PR, Merge-Commit, nicht Squash/Rebase); die Zweige `research/v4.8.0-r03-r12-lokalgeschichte`, `history/lokalgeschichte-in-main` und `research/v4.10-r34-r42` können weg. Alte Zweige auf GitHub gelöscht; übrig `main`, die Lokalgeschichte und `pilot/qsc-mcp-server` (in #29 aufgegangen, kann weg). Issues #10–#16 am 2026-10-23 mit Fortschrittsberichten versehen, #5 zum Schließen vorgeschlagen, Tags `RC25` und `vor-aufraeumen-v490-r24` gepusht. Lokaler MiKTeX-Build des 4.10-Kandidaten: 1220 Seiten / 3789 Labels, Overfull 58, harte Werte 0. **Künftige Übertragungen:** neue Runden an `v490-post-release-layers.tex` anhängen (bzw. eine 4.10-Schichtdatei, sobald angelegt); künftige Hauptkorpus-Überarbeitungen als Patch-Spezifikation festhalten (`llm/revision_spec_v490.py` für r25 über `llm/aufraeumen_v410_github.py`; ab r31 `llm/revision_spec_v490_rNN.py` über `llm/apply_patches.py`, lokal wie auf `sources/research/parts/v470/`), damit lokal und GitHub gleich bleiben. Ablauf: Skill `zenodo-release` (Abschnitt Klon) und die bisherigen PRs als Muster.

Das Repository liegt in einem OneDrive-Ordner. Bisher unauffällig; falls je Sync-Konflikte im `.git`-Verzeichnis auftreten, ist ein Umzug außerhalb der Cloud die Abhilfe.

## Dateien

| Datei | Rolle |
|---|---|
| `Quantum_Sphaera_Companion_v4_8_0_source.tex` | **Die Arbeitsdatei.** Hier wird editiert. |
| `Quantum_Sphaera_Companion_v4_8_0.pdf` + `V4_8_0_*` + `v4_8_0_release_summary.json` | **Release v4.8.0**, Zenodo-Entwurf 23365244 |
| `Quantum_Sphaera_Companion_v4_8_0_r20.pdf` + `V4_8_0_RC25_*` + `v4_8_0_RC25_post_release_layers_summary.json` | **RC25 (Stand v4.8.0-r20)**, Tag `RC25`, keine neue DOI, kein Release |
| `Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_source.tex` | **Eingefrorener RC19-Snapshot** — nicht editieren |
| `Quantum_Sphaera_Companion_v4_7_0.pdf` | RC19-PDF — eingefroren, nie überschreiben |
| `..._RC20_citation_repair_source.tex` + `..._r85.pdf` + `V4_7_0_RC20_*` | RC20 (Stand r85), eingefroren |
| `..._RC21_c5_collar_consolidation_source.tex` + `..._r86.pdf` + `V4_7_0_RC21_*` | RC21 (Stand r86), eingefroren |
| `..._RC22_clock_window_collar_routes_source.tex` + `..._r88.pdf` + `V4_7_0_RC22_*` | RC22 (Stand r88), eingefroren |
| `quantum_sphaera_v3_1_4_monolith_stable_main (1).tex` | Hauptpapier, Bibkey `brendecke2026main` |
| `riemann_arxiv_v4__15_ (1).tex` | Riemann-Arbeit v4.15, Bibkey `brendecke2026rh`. **Seit v4.8.0-r04 keine Beweisquelle mehr** (Gutachten `llm/Pruefung_Riemann_Paper_v4_15.md`); nur noch Startpunkt und klassische Arithmetik |
| `V4_7_0_RC19_CONCEPT_DOI_RESTORE_AUDIT_REPORT.md` | Compile-Audit der letzten Runde |
| `v4_7_0_RC19_concept_doi_restore_summary.json` | Dieselben Audit-Zahlen maschinenlesbar |
| `V4_7_0_RC19_SHA256_MANIFEST.csv` | Hashes aller Release-Dateien |
| `V4_7_0_RC19_ZENODO_METADATA_DRAFT.txt` | Zenodo-Upload-Metadaten |

Die vier RC19-Begleitdateien gehören zusammen: wer den Quelltext ändert und neu kompiliert, muss alle vier aktualisieren, sonst driften Hashes und Audit-Zahlen auseinander.

Nicht in diesem Verzeichnis, aber referenziert: `RC14_uncompressed_reference_source.tex` im RC16-Quellpaket enthält den ungekürzten r55–r80-Solve-Log. Er wird gebraucht, sobald an C5 oder C4 inhaltlich gearbeitet wird.

## Dokumentaufbau

`article`-Klasse, keine `\input`/`\include` — alles in einer Datei. Zeilen ungefähr (Stand v4.9.0-r25), mit `qs.py outline` nachprüfen:

| Zeilen | Inhalt |
|---|---|
| 1 – ~51.700 | Mathematischer Hauptkorpus (QAM-über-ZF, MML/MMA, Heisenberg-Kompensator, Millennium-Matrix, OP-Architektur), seit r25 mit Statusvermerken `\qsstatus`; am Ende die v4.7.0-Schichten r01/r02 |
| ~51.870 | **Archiv-Anhang** `sec:v490-archive`: wortgleiche Originale archivierter Hauptkorpus-Aussagen (r25) |
| ~52.340 – ~62.870 | Solve-Log r03 – r54 |
| ~62.880 | r55 – r80, komprimiert |
| ~62.900 – ~65.060 | r81 – r94 |
| ~65.060 – ~67.910 | v4.8.0-r01 – r20 |
| ~67.920 – Ende | v4.9.0-r01 – r25 |

## Der Runden-Workflow

Die **Runden** wachsen append-only: eine neue Runde ist ein neuer Abschnitt unmittelbar vor `\end{document}`, bestehende Runden werden nicht umgeschrieben. Aktueller Stand: **r94**, **v4.8.0-r20**, **v4.9.0-r54**. Runden der v4.8.0-Linie heißen `v4.8.0-rNN` (Labels `sec:v480-rNN-...`), danach `v4.9.0-rNN` (`sec:v490-rNN-...`); `qs.py outline` und `ledger` erkennen alle Formen. Inhalt jeder Runde ausführlich in der Kernkarte (`llm/Kernkarte_Quantum_Sphaera_v1.md`, Abschnitt 7).

**Der Hauptkorpus wird seit v4.9.0-r25 überarbeitet** (Autorauftrag 2026-10-22: alte Arbeit nicht verlieren, falsche Aussagen nicht stehen lassen). Regel (`sec:v490-r25-main-body-revision`, Skript `llm/aufraeumen_v490.py`):
- **(A) Sackgasse** (widerlegt, ausgeschlossen, zurückgezogen): Original wortgleich in den Archiv-Anhang `sec:v490-archive`; an der alten Stelle bleibt dieselbe Umgebung mit **gleicher Nummer und gleichem Label**, kurzer Aussage dessen, was bleibt, und Verweis. Alle `\ref` lösen weiter auf.
- **(B) Bekannter Fehler**: im Text korrigieren, `\qsstatus{...}` mit altem Wortlaut und begründender Runde.
- **(C) Umgedeutet oder offen**: Text bleibt, `\qsstatus{...}` mit Stand und Runden.
- Runden, Vorab-Notizen und Testergebnisse werden **nie** archiviert oder umgeschrieben. Vor jeder Überarbeitung ein Sicherungstag (zuletzt `vor-aufraeumen-v490-r24`).

**Wer einen älteren Satz zitiert**, prüft zuerst seinen `\qsstatus`-Vermerk bzw. den Archiv-Anhang, dann die Register `sec:v480-r09-p2-p3-reclassification` (Stand v4.8.0) und `sec:v490-r15-consolidated-register` (v4.9.0-r01–r14).

**Neue Vorhersagen nur mit Vorab-Notiz:** Hypothese, Daten und Kriterium unter `llm/Vorab_Notiz_*.md` committen, erst dann rechnen. Ausstehend: **H15** (m_W = 80,3615 ± 0,0018 GeV, Vergleich mit der ersten m_W-Weltmittelung nach 2026-10-21).

Guard-Linter für neue Runden: `python llm/training/guard_linter.py <tex> --start N` (prüft verbotene Aussagen und ab r22 den Frame-Abschnitt).

### v4.9.0-Runden in Kurzform

| Runde | Ergebnis |
|---|---|
| r01 | Photon-Frame als neutrale Achse; Lorentzfaktor-Umrechnung komponiert nicht, Doppler schon; Wege A–C |
| r02 | Umkehrwalze antilinear (J_B: E ↔ B); Seitenwechsel z → −z = C = PT |
| r03 | Kompensator als Zweiarm-Interferometer; Sichtbarkeit 1/cosh 2η |
| r04 | Kompensator als 2×2-Matrix ½(1+σ_x); Zustandsscheibe, Bloch-Vektor |
| r05 | Millennium-Matrix auf dem Dublett nur Portgewichtung; Lesename „layer-transport matrix“ (M₁₆) |
| r06 | Tachyon-Trefferkette, Kegel 56,68°; Higgs als Portgewichtung (formal) |
| r07 | H14 widerlegt (z = +8,2); H15 vorab festgelegt; cot θ_W on-shell ≈ γ_L |
| r08 | Drift aus prop:H0-tension durch Atomuhren ausgeschlossen; k(α) = +1; Compton-Uhr k = 0 |
| r09 | lokaler Frame-Faktor nur als Potentialkopplung; P5 → 1/2 |
| r10–r11 | C5-Faktor 3/4 als „π/6 drehen, dann kompensieren“; gekickte Dualitätsdrehung; Form-(iii)-Zeugen aus Lesart B ausgeschlossen |
| r12 | Δ_γ < 1/5 unter (P1)–(P4) rekonstruiert (r65-Text verloren) |
| r13–r14 | Zeitskala: Kick = Schwebung/6; Kick-Richtungen Triole ∪ J_B(Triole) |
| r15–r16 | Sammelregister r01–r14; Autorentscheidungen (frame-offset strukturell, C5-Lesart Autorlesart; offen: Wege A–C, Epoche von thm:dark-energy) |
| r17 | Zustandsscheibe: γ_L = 1/abs(b), Eigenwerte 3/4, 1/4 am Hopf-Punkt; Photon = Informationssingularität; Skalen-Dimension σ |
| r18–r19 | Klassentrennung: Skalengrößen Weg C (e^{kη}), Auslesegrößen Weg A (γ_L); auf den Hauptkorpus angewandt (angebotene Lesart) |
| r20–r21 | Herkunft von Δ_γ < 1/5: Photon-Frame-Uhrgewinn am Hopf-Punkt; 1/5 als einzige frame-konsistente Schranke hergeleitet (D1–D5), gemessen Materie 0,1925 |
| r22 | **Konvention F**: Materie M, Tachyon T = Bild unter z → iz (β² → 1/β², γ → −γ, Ports getauscht; in r22 als „J_B-Bild“ bezeichnet, korrigiert in r28), Photon P = entarteter Fixpunkt; Pflichtabschnitt `subsec:v490-rNN-frames` |
| r23 | F auf 113 Hauptkorpus-Aussagen angewandt (Liste `llm/k62_frame_regel_hauptkorpus.py`) |
| r24 | Widersprüche als Ein-Frame-Artefakte: β-Vorzeichen = Orientierungscode, Hauptkorpus-Tachyon = Projektion T\|_R (−β), Hauptkorpus-„Photon-Frame“ = Bezugsframe R (reiner Zustand); F5–F7 |
| r25 | **Überarbeitung des Hauptkorpus**: 15 Sackgassen archiviert, bekannte Fehler korrigiert, Statusvermerke |
| r26 | Vorab-Test H16 (Grad-6-Potentiale auf dem Tripel-Raum) widerlegt; Theoremlet r26.1: bis Grad 6 ist jeder kritische Punkt mit drei verschiedenen Normen ein Sattel, Minima mit Hierarchie brauchen Grad ≥ 8 |
| r27 | **Dynamik-Modell**: Dualitätsdrehung plus Kompensator-Messung; selektiv 3/4 je Schritt, n = 20; ein Kick aus R gibt den Hopf-Zustand, gemessener Abstand ⇔ Kickwinkel 28,78°; Photon Attraktor; ändert s (außerhalb Lesart-B-Transporte); kein endlicher Score-Nullpunkt |
| r28 | Tachyon als Messgerät: ideal aus Bezugszustand mit T-Kopplung, nicht über J_B/C; Selbstmessung durch Tausch mit eigenem Tachyonbild; Feld allein nicht selbststabilisierend, mit nachgefülltem Tachyon-Reservoir eindeutiger Attraktor (am Hopf-Punkt selbstkonsistent, nachträglich); **Korrektur: Tachyon-Abbildung in r21/r22/r27 ist z → iz, nicht J_B** |
| r29 | Quelle des Tachyon-Reservoirs: Paarerzeugung aus dem Vakuum R (liefert genau den Tachyon-Bezugszustand); Horizont, übrige Moden, Trefferkette scheiden aus, warmes Bad nur teilweise; Kaskade β² als Austauschstärke nur kohärent selbstkonsistent; offen: Paarrate, Kohärenz |
| r30 | Kompensator umgeht die klassische 1/2 (Autorhinweis): Mischung gibt immer 1/2, kohärente Kombination einen eindeutigen Port; „Light as HC of the universe“ nur amplitudenweise; C = ½(1+J) Projektor nur für J_B, J_B = (z → iz) ∘ T → Partner = Tachyon durch T (wie r28); Austausch kohärent per Konstruktion, r29-Frage beantwortet |
| r31 | Markov-Kaskade (Autorabsicht: Vorhersage und Selbststabilisierungstest): geschlossen nur Photon stationär; mit Rückweg S² → S⁸ eindeutig stationär, Flussanteile β², 1 − β² für jede Rate; Statusvermerk zu thm:dark-energy erweitert (`llm/revision_spec_v490_r31.py`, Anwendung mit `llm/apply_patches.py`) |
| r32 | Vorab-Test H17 (Realteil-Invarianten L = ΣRe a_k, R₂, L² auf dem Tripel-Raum) widerlegt; Theoremlet r32.1: auf der reellen Achse linear in e₃, wieder Sattelpunkte; meiste Minima auf der Achse (G₂ ungebrochen); nächster Weg explizite S₃-Brechung |
| r33 | Dixon-Ablage als Register aller Konfigurationen (Autorabsicht): Tripel = (Im ℍ)⊗𝕆, gemeinsame Symmetrie A₄ = Konjugation mit 2T; J_B = R∘T vertauscht die ℂ-Hälften, nur D₄ erhält das M/T-Etikett; links-invariante Etiketten μ_i = Fläche der anderen beiden Plätze (Lorentz-Konflikt für Etiketten lösbar); Vorab-Test H18 (Massen aus μ an den Minima) widerlegt; Lean `formal/QSFormal/Dixon.lean`, `Lesarten.lean` |
| r34 | Ladungen aus der Dixon-Ablage (Vorab-Test H19, Bestandsaufnahme Test 1): Zahloperator nach Furey mit der Farbe Stab(e₇) verträglich, Sektoren Q = 0, 1 (Singuletts 1 ± i·e₇) und 1/3, 2/3 (konjugierte Tripletts); wörtliche Companion-Zuordnung (Farbe auf e₄..e₆, ν_R auf e₇) widerlegt; J_B bildet Q auf 1 − Q ab, die U(1)-Zeile von thm:SM muss ihren Frame nennen |
| r35 | Innere gegen äußere komplexe Einheit (Vorab-Test H20, Autorhinweis „fester Frame“): Farb- und ν_R-Zuordnung im inneren Frame J = L_{e₇} richtig, über P₋ = ½(1 + iJ) deckungsgleich mit Furey; Anti-Triplett-Satz in thm:three-generations falsch (Frame-Vermischung); Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}, der Skalar it allein ist nur globale Phase; Lesart von r34.1(c) korrigiert |
| r36 | Frame-Regel für komplexe Einheiten übernommen (Autor, Konvention F, Punkt 7 im Rundenformat); Statusvermerke an thm:three-generations und thm:SM (`llm/revision_spec_v490_r36.py`); Vorab-Test H21: die Triolen-Symmetrie e₄ → e₅ → e₆ ist der einzige solche Automorphismus und eine Farbdrehung in SU(3)_c, Farbe und Generation sind dasselbe Objekt; Generationen brauchen eine Dreierstruktur außerhalb von 𝕆 |
| r37 | Triality als Selbstdurchwanderung (Vorab-Test H22, Autorabsicht „Triole = Darstellung der Sphäre“, Perioden nicht festgelegt): t = Re((xy)z) ist die Spin(8)-Triality-Form, Platzverschiebung = äußere Triality, Fixgruppe G₂ ⊃ SU(3)_c (Generation = Bahn, Farbe = Fixgruppe); kein Verbot einer vierten Generation; Perioden {1, 2, 3, 4, 6, 12}; drei Triolen im Korpus (Frames M/P/T, Kerne 120°, Plätze) |
| r38 | Frame-Triole als Spiegelseite der Triality (Vorab-Test H23): ρ = (x̄, z̄, ȳ) äußerer Automorphismus der Ordnung 2, feste Gruppe Spin(7) mit Platz 1 = 1 ⊕ 7, Plätze 2, 3 gleich; Photon = Vektor-Platz, Materie/Tachyon = Spinor-Plätze (Lesart); 120°- und Frame-Triole = zwei Ansichten derselben S₃; Frames und Generationen brauchen verschiedene Ebenen |
| r39 | Ketten verschiedener Länge unter Hilbert-Shift-Zoom und gemischten Readouts (Vorab-Test H24, Autoridee „Generationen bilden beim Zoom einen Kreis“): ab Stufe 2 bleibt in S₃ × D₄ nur der Triality-Kreis, Orientierung wechselt mit der Stufe (= ρ-Spiegel); Frames grob, Generationen tief; Masken Σ (Kontraktion) 1 oder 3 Generationen, ∨ (Maske) 3; Autorhinweis zur zweiseitigen Kontraktion und zum Ein-Frame-Problem |
| r40 | Zweiseitige Kontraktion erstmals über Frames (Vorab-Test H25): Regel 1 nur bis auf Konjugation (T, J_B), bilinearer Vergleich wechselt unter z ↦ iz das Vorzeichen (m² ↦ −m²), hermitesch frame-blind; Frame-Klausel vorgeschlagen; kein 𝔰𝔲(2) der Triality vertauscht mit Farbe (Zentralisator = span(L_{e₇}, R_{e₇})), schwache SU(2) nur im ℍ-Faktor links oder rechts |
| r41 | Verteilung der ℍ-Rollen (Vorab-Test H26): Aufteilung D (Lorentz links, schwach rechts, Generationen Triality) hebt die Überbelegung auf; mit Y/2 = Q − ½ gibt Q_em = T₃ + Y/2 die linkshändigen Dubletts und Konjugierten (Muster vorab analytisch offengelegt); Frame T = Ladungskonjugation; schwache Singuletts fehlen, Chiralität offen |
| r42 | Kompensator der MM-Matrix als Chiralitätsprojektor (Vorab-Test H27, Autorhinweis „MM-Matrix mit verschiedenen HC“): C_ch = ½(id + J), J = i·L_{e₇}; schwache SU(2) nur auf dem Bild, Y/2 = Q − ½ + (1 − C_ch)T₃ ⇒ voller linkshändiger Inhalt einer Generation mit ν_R, anomaliefrei; T vertauscht die chiralen Hälften; Konstruktion unter Wahlen, Muster vorab offengelegt; Erstlauf mit Rundungsfehler im Skript dokumentiert |
| r43 | Wahl des Chiralitätsprojektors durch Anomaliefreiheit (Vorab-Test H28, Autorfrage „wieso genau diese Wahl“): unter den Annahmen genau vier Projektoren ±iL_{e₇}, ±iR_{e₇}; Tr Y = 0 ⇒ s = −½; anomaliefrei nur die Linksmultiplikation ⇒ SM und Frame-Spiegel; Annahmen nicht hergeleitet |
| r44 | Massenterme als Frame-Kopplungen (Vorab-Test H29): farb-/Lorentz-verträgliche Massenterme sind antilinear (enthalten T), tragen H/H̃-Quantenzahlen; lineare MM-Blöcke geben keine; eichinvariant nur ν^c-Majorana; Plätze: S₃ ⇒ ≤ 2 Massen, ρ-Brechung ⇒ Brannen-Form (Koide bei \|b\| = a/√2), Mischung ⇐ τ-Brechung |
| r45 | Chiralität bricht ρ (Vorab-Test H30): ρ enthält die Oktonion-Konjugation, c L_{e₇} c = −R_{e₇}, bildet die anomaliefreie Chiralität auf die anomale ab ⇒ ρ-Brechung strukturell (Massenaufspaltung); τ bleibt bei gleicher Chiralität; triality-kovariante Chiralität existiert nicht ⇒ Generationen äquivalente Kopien; Mischung offen |
| r46 | Gemischte Readouts und τ-Brechung (Vorab-Test H31): Readouts aus den Verschiebungen (Σ, ∨, Selektor-Kontraktion) vertauschen mit τ ⇒ keine Mischung; Art-Masken auf einzelne Generationen brechen τ ⇒ Mischung ∝ Gewicht, unterdrückt durch Massenabstände; Maske muss Teil der Kopplungen sein, Herkunft offen |
| r47 | Generationen-Maske aus der triality-kovarianten Chiralität (Vorab-Test H32, Modellannahme: Abweichung als schwache Störung): Form fest, Quarks diag(0, −2, −1), Leptonen diag(0, 0, −3), demokratisch in der Generationen-Basis, Leptonen √3 stärker; H32c (Linearität bei ε = 10⁻³/10⁻⁴) in 4/200 fast entarteten Fällen widerlegt; Zahlen offen |
| r48 | Ladungs-Sektoren aus der Oktonionen-Multiplikation in Lean (`formal/QSFormal/Sektoren.lean`, keine Vorhersage, keine Vorab-Notiz): (iL)² = (iR)² = 1, iL iR = iR iL; vier orthogonale Projektoren P_s mit Summe 1; Sp(LR) = 4, Ränge 1, 3, 3, 1; 6Q und die r47-Gewichte auf den Sektoren; T P_(ℓ,r) = P_(−ℓ,−r) T; σ bleibt im Sektor. Damit sind die Tabellen von `Ladungen.lean` hergeleitet statt gesetzt |
| r49 | e₇-Achse trägt B − L, nicht die Ladung (Vorab-Test H33, Deutung nach r48): span_ℂ(1, e₇) = Sektoren Q = 0, 1; 2(Q − ½) = B − L, Q_em = T₃^L + T₃^R + (B − L)/2; Photon braucht T₃ aus ℍ; Photon-Kern K₃ und ν_R auf derselben Ebene (Doppelbelegung, Statusvermerk-Kandidat); Lean `b_minus_l` |
| r50 | Mischung aus der Maske von r47 (Vorab-Test H34, Daten M_Z-Massen, NuFIT 6.0, PDG 2024): Hierarchie begrenzt ε (≲ 0.06 up), CKM in keiner Kombination auf ±20 %, PMNS auch allein nicht; Modellannahme für die Mischung widerlegt, Form der Maske bleibt |
| r51 | e₇ und die Frames (Vorab-Test H35): Tachyon-Abbildung z ↦ iz (äußere Einheit) lässt alle Sektoren fest, T und J_B tauschen sie; L_{e₇} ist inneres Gegenstück von z ↦ iz, für T, J_B gibt es auf dem Triplett keins; Frame-Ebene = span(1, e₇). **Korrektur:** „T“ als Ladungskonjugation in r41–r49 = Zeitumkehr (Porttausch), nicht Tachyon-Frame; Lean `R_P4` |
| r52 | Exakte Kopplungsformen der Maske (Vorab-Test H36): D C D (Partner über T) und D C D⁻¹ (über die Tachyon-Abbildung), D = exp(εW); CKM in keiner Kombination auf ±20 % (nächster Fall 36 %), Leptonen auch nicht; Reihenfolge der CKM-Elemente stimmt; fehlende Zutat offene Wahl |
| r53 | Kopplungen aus der Triality-Form (Vorab-Test H37): reine Triality-Kopplung spurfrei ⇒ m₃ = m₁ + m₂, für u, d, e falsch, für Dirac-ν Σm = 0.115 eV > DESI 0.0642 eV (Verbot aus der Struktur); Norm + Triality: keine Quark-Mischung, Leptonen nur bei ausgeschlossenen m₁; H/H̃-Lesart widerlegt |
| r54 | Ein ε je Sektor (Vorab-Test H38): Form S trifft CKM (0.0009 %, ε_u ∈ [1.36, 1.63], ε_d ∈ [1.42, 1.47]) und PMNS (ε_e ∈ [0.44, 0.82], ε_ν ∈ [0.27, 0.55], kosmologisch zulässige m₁); Form K verfehlt die Quarks knapp (20.2 %); dritte Größe nicht scharf (|V_ub| typisch ×5) ⇒ Anpassung, keine Erklärung; Zählung von r52 korrigiert |

Ältere Runden (r03–r94, v4.8.0-r01–r20): Kernkarte und die genannten Register. Kurzstand v4.8.0: Lesart B (ℂ³, SO(3,ℂ)) als Arbeitslesart, Sektoren nach Vorzeichen von s, vorab festgelegte Tests H2–H13 mit Ergebnissen, Riemann-Arbeit seit r04 keine Beweisquelle.

Eine Runde folgt einem festen Muster:

1. `\section{v4.7.0-rNN <Titel>}` bzw. `\section*{...}` plus `\addcontentsline{toc}{section}{...}` — beide Varianten kommen vor; ab r82 wird durchgängig `\section*` mit `addcontentsline` verwendet
2. `\label{sec:rNN-<kebab-case-titel>}`, jede Unterüberschrift bekommt ebenfalls ein `\label{subsec:rNN-...}`
3. Source-only-Klausel (kein PDF, keine neue DOI, kein Public Release, sofern nicht ausdrücklich anders beauftragt) mit der v4.9.0-Version-DOI
4. Inhalt als Theoremlet mit `\paragraph{Theoremlet rNN.}` und `\paragraph{Proof sketch.}`, abgeschlossen mit `\(\square\)`
5. Guard-Update am Ende: die Residual- und Guard-Vektoren der Runde
6. **Ab v4.9.0-r22 (Konvention F):** ein Abschnitt `\subsection*{v4.9.0-rNN status in the three frames}` mit `\label{subsec:v490-rNN-frames}`, der für jedes Ergebnis den Stand in Materie-, Tachyon- und Photon-Frame angibt (Tachyon = Bild unter der Dualitätsdrehung z → iz, nicht J_B; Photon = entarteter Fixpunkt; frame-frei nur, wenn Materie und Tachyon übereinstimmen). Der Guard-Linter meldet Runden ab r22 ohne dieses Label.
7. **Ab v4.9.0-r36 (Konvention F, komplexe Einheiten; Autorentscheidung 2026-10-23):** Aussagen über Farbe oder Ladung nennen ihre komplexe Einheit: innen J = L_{e₇} auf 𝕆 (Farbe, keine Ladung) oder außen i = ℂ-Faktor der Dixon-Ablage (mit Ladungsoperator Q); eine Übersetzung nennt ihr Vorzeichen P₊ oder P₋ = ½(1 ∓ iJ) (v4.9.0-r35).

## Guard-Disziplin — die wichtigste Regel

Das Dokument arbeitet mit einem expliziten System erlaubter und verbotener Aussagen. **Neuer Text darf niemals eine der verbotenen Aussagen behaupten**, auch nicht implizit oder in abgeschwächter Formulierung.

Erlaubt (effektiv/lokal/frame-typisiert):

```
0_M^ε ⇒ 0_termdata                          Matter-Frame-Epsilon-Terminalität
ℓ_T² = −λ_T², λ_T > 0                       Tachyon-Frame-Vorzeichenskala
OP5_eff                                      effektive OP5-Schließung
C5_det/eff bei θ = 1/256 nach n = 20         Detektor-Schwellen-Terminalität
W_clk^loc unter Δ_γ < 1/5                    lokale Photon-Clock-Selektor-Erhaltung
C_mix^typed lokal                            typisierte Mixed-Comparison-Kontrolle
```

Verboten (exakt/global):

```
C5 = 0                    exakte endliche C5-Null-Schließung
0_termdata ⇒ 0_all        exakte All-Readout-Terminalität
C6 / T2                   T2-Schließung
W_γ^glob                  globales Photon-Clock-/RH-Theorem
W_all                     globale All-Readout-Schließung
```

Die sichere Release-Formulierung lautet: *guarded effective/local and frame-typed closures, not exact global closure.*

### Ledger-Notation

Jede Runde bilanziert am Ende:

- `Γ_guard = (1,1,1,1,1)` — alle fünf Guards stehen. Eine `1` heißt: der Guard ist **nicht ausgegeben**. Ein Guard darf nur mit ausdrücklicher Zustimmung des Nutzers fallen.
- `R_glob = (0,1,1,1,1)` — globales Residuum. Seit r60 unverändert; die erste Komponente fiel damals durch die konservative C4-Relative-Seam-Behandlung.
- `R_eff/local = (0,0,0,0,0)` gegen `R_exact/global = (1,1,1,1,1)`
- `β₄ = 1/256` ist der ungespendete C4-Guard.

Wenn eine neue Runde diese Vektoren nicht verändert, ist das der Normalfall und muss so deklariert werden. Wenn sie einen Wert verändert, ist das ein Ereignis, das explizit begründet gehört.

## DOI-Disziplin

DOIs, die nie vermischt werden dürfen:

- **Version-DOI** `10.5281/zenodo.23534954` — **v4.9.0, veröffentlicht 2026-10-21** (Zenodo-Record `23534954`, vom Nutzer veröffentlicht), aktuelle Version; gehört als einzige sichtbare DOI-Zeile auf die Titelseite eines 4.9.x-Stands
- **Vorgänger-DOI** `10.5281/zenodo.23365244` — v4.8.0, seit v4.9.0 nur Provenienz
- **Frühere Version-DOI** `10.5281/zenodo.20232911` — v4.7.0, nur Provenienz
- **Concept-DOI** `10.5281/zenodo.19210728` — stabil über alle Versionen
- **Previous/Baseline-DOI** `10.5281/zenodo.20117361` — v4.6.0, nur Provenienz, nie als aktuelle DOI

Abgelaufen und nicht mehr zu verwenden: `10.5281/zenodo.20181842`.

**Achtung, lokale Arbeitsdatei:** `Quantum_Sphaera_Companion_v4_8_0_source.tex` trägt auf ihrer Titelseite weiterhin die v4.8.0-DOI und in den Source-only-Klauseln der Runden „v4.8.0 Version DOI … unchanged". Das ist für die Runden bis v4.8.0-r20 richtig (sie sind so in v4.9.0 veröffentlicht). Neue Runden nach dem 4.9.0-Release heißen **`v4.9.0-rNN`** (Labels `sec:v490-rNN-...`) und nennen in ihrer Source-only-Klausel die v4.9.0-Version-DOI. `qs.py doi` kennt ohne Parameter v4.9.0 als aktuell (seit 2026-10-22).

**4.9.0-Release auf GitHub abgeschlossen (2026-10-22):** PR #21 in `main` gemergt (Merge-Commit `a412bd7`), Tag und GitHub-Release `v4.9.0` angelegt (https://github.com/Moriarty1982/QuantumSphere-Unfold/releases/tag/v4.9.0). `DOI_ROLES` in `qs.py` steht auf v4.9.0; für PDFs der lokalen Arbeitsdatei (Titelseite noch v4.8.0) `qs.py doi <pdf> --version-doi 10.5281/zenodo.23365244 --version-label v4.8.0` verwenden. Projektlokale Freigaberegel in `.claude/settings.local.json` (global gitignored): `gh pr ready`/`gh pr merge` für dieses GitHub-Repository.

Die **Compact-Titlepage-Regel**: auf der Titelseite steht genau eine Version-DOI-Zeile und eine Concept-DOI-Zeile. Release-Hinweise, Provenienz der Vorgänger-DOI und Claim-Scope-Erklärungen gehören in den Fließtext, nicht auf die Titelseite.

## Kompilieren

**MiKTeX 25.12** ist als User-Installation eingerichtet:

```
%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64
```

Es liegt **nicht im PATH** — den Pfad im Aufruf voranstellen oder für die Sitzung setzen. Automatisches Paketnachladen ist aktiviert (`[MPM]AutoInstall=1`), fehlende Pakete werden also ohne Dialog geholt. Alle Pakete der Präambel sind verfügbar, einschließlich `slashed`, `centernot` und `datetime2`.

Gebaut wird mit **drei pdfLaTeX-Durchläufen**, außerhalb des Projektverzeichnisses:

```bash
pdflatex -interaction=nonstopmode Quantum_Sphaera_Companion_v4_8_0_source.tex
```

Danach `qs.py audit <log>` gegen die Baseline. Das RC19-PDF im Projektordner nie überschreiben — es ist im Manifest gehasht.

Die Präambel setzt `\pdfcompresslevel=0` und `\pdfobjcompresslevel=0` — daher die 14 MB PDF-Größe. Das ist Absicht (Diffbarkeit), nicht zu „optimieren".

PDF-Lesezeichen sind seit dem Stand nach v4.8.0 wieder an (`bookmarks=true,bookmarksnumbered=true`); der r25/r27-Notbehelf `bookmarks=false` ist entfernt. Getestet mit drei pdfLaTeX-Läufen unter TeX Live 2022: 968 Lesezeichen, Seiten, Labels und harte Audit-Werte unverändert. `\pdfstringdefDisableCommands` in der Präambel hält Symbole wie `\to` und `\Lambda` im Lesezeichentext lesbar; die übrigen „Token not allowed in PDF string“-Warnungen (37) sind harmlos. Das veröffentlichte v4.8.0-PDF ist noch ohne Lesezeichen gebaut. Unter MiKTeX 25.12 seit RC25 geprüft: 986 Lesezeichen, Seiten, Labels und harte Audit-Werte unverändert gegenüber den Einzelbuilds.

Unter MiKTeX 25.12: v4.8.0 (Tag neu gebaut) 1045 Seiten / 3369 Labels, RC25 (v4.8.0-r20) 1096 / 3474, Arbeitsdatei nach v4.9.0-r25 1176 / 3635, Overfull durchgehend 58 (das v4.8.0-Release meldete unter TeX Live 45), alle harten Werte 0.

### Audit-Baseline (RC19)

Nach jedem Rebuild gegen diese Werte prüfen:

| Prüfung | Sollwert |
|---|---:|
| PDF-Seiten | 1014 |
| Undefinierte Referenzen / Zitate | 0 / 0 |
| Duplikat-Label-Warnungen | 0 |
| Rerun-Warnungen | 0 |
| Rohe `??`-Marker in Quelle / PDF | 0 / 0 |
| Labels gesamt | 3290 |
| Overfull-hbox-Warnungen | 45 (siehe unten) |
| Sichtbare Version-DOI-Zeilen auf Titelseite | 1 |
| Sichtbare Concept-DOI-Zeilen auf Titelseite | 1 |
| Treffer der abgelaufenen DOI im PDF | 0 |

**Die Overfull-Zahl ist toolchain-abhängig und taugt nicht als fester Sollwert.** Der ursprüngliche RC19-Build meldete 45; derselbe Quelltext liefert unter MiKTeX 25.12 reproduzierbar **58** — bei identischer Seitenzahl (1014) und Labelzahl (3290). Für eine belastbare Aussage den Vergleichsstand mitbauen und `qs.py audit <neu.log> --compare <ref.log>` verwenden. Nur `undefined_refs`, `undefined_cites`, `duplicate_labels` und `rerun` sind harte Nullwerte.

Unter derselben Toolchain: RC19 1014 Seiten / 3290 Labels, RC20 1016 / 3296, RC21 1019 / 3305, RC22 1025 / 3322. Overfull durchgehend 58, alle harten Werte 0.

## Fallstricke

**Backslashes in Bash-Argumenten werden verschluckt.** `grep -F "\section{" datei.tex` liefert hier 0 Treffer, obwohl der String tausendfach vorkommt — und `grep -oE '\\(a|b)'` matcht die literale Klammer statt der Gruppe. Für alles, was LaTeX-Befehle sucht oder schreibt, das **Grep-Tool** und **Write/Edit** verwenden, nicht Bash mit `grep`/`sed`/Heredoc. `sed -n 'A,Bp'` für Zeilenbereiche ist unproblematisch, weil dort keine Backslashes im Muster stehen.

**Nie die ganze Datei lesen.** Über 71.000 Zeilen. Mit `sed -n` gezielt Bereiche holen oder das Grep-Tool mit `-C` verwenden.

**Nie behaupten, ein Datum fehle, ohne die Nachbarrunden zu prüfen.** Die Solve-Kette tabelliert in einer Runde und verbraucht in einer anderen. r87 behauptete, die V9-Chart-Parameter seien nicht dokumentiert — sie stehen in r14, eine Runde vor der gelesenen, und der zugehörige Lift in r17, zwei Runden danach. Die Korrektur ist als r89 protokolliert. Eine Aussage über Fehlen betrifft den ganzen Monolithen und braucht einen Grep über die gesamte Datei plus die angrenzenden Runden.

**Keine externen Grafiken.** `\safegraphic` ist in der Präambel definiert, wird aber nirgends aufgerufen — es fehlen keine Asset-Dateien, und ein Platzhalterrahmen im PDF wäre ein Fehler, kein Normalzustand.

**Der RC19-Snapshot ist eingefroren.** `_RC19_concept_doi_restore_source.tex` dokumentiert den Zustand, der als RC19 kompiliert und im Manifest gehasht wurde. Er wird nicht nachträglich verändert — sonst geht die Provenienz verloren. Alle Änderungen laufen in `_source.tex` und gehören zum nächsten RC. Seit der ersten Post-RC19-Änderung sind die beiden Dateien deshalb **nicht mehr byte-identisch**, und der Manifest-Eintrag für `_source.tex` ist überholt; beides ist gewollt. Ein neuer RC bekommt einen neuen Snapshot unter neuem Namen und ein neu erzeugtes Manifest.

## Offene Zweige

- **Q₄** C4-Mixed-Kernel-Lokalisierung — r91: `β₄ = 1/256` ist terminale Schwellenskala, Ausgabe wäre der verbotene Schritt; **geschlossen als „nicht ausgebbar“**.
- **Q₃ Restteil `Δ_γ < 1/5`** — r90/r92 rekonstruiert, v4.9.0-r12 unter (P1)–(P4) hergeleitet, r20 Herkunft (Photon-Frame-Uhrgewinn am Hopf-Punkt), r21 als einzige frame-konsistente Schranke hergeleitet; gemessen im Materie-Frame 0,1925. Der r65-Volltext ist laut Autor verloren (nicht im Projektordner, nicht in `C:\Users\marcb\Downloads\Quantum Sphere`).
- **C5-Faktor 3/4** — r94 deklariert; Autorlesart seit v4.9.0-r16: gekickte Dualitätsdrehung (r10, r11, r14); als Eigenwert 3/4 = p₊ am Hopf-Punkt (r17).
- **C5 Form (iii)** — offen; Zeugen aus der Transportgruppe von Lesart B ausgeschlossen (r10); bräuchte Dynamik.
- **Autorentscheidungen offen:** Wege A–C der Konstantenumrechnung (Klassentrennung r18/r19 angeboten), Epoche von `thm:dark-energy`, Reservierung einer 4.10-Version-DOI, sobald 4.10 veröffentlicht werden soll.
- **Dynamik**: v4.9.0-r27 schlägt ein Modell vor (Drehung plus Kompensator-Messung, ändert s); r28: Messgerät kann der Tachyon sein (T-Kopplung), stabiler Zustand nur mit nachgefülltem Tachyon-Reservoir; r29: Quelle vorgeschlagen = Vakuumpaare; r30: Kohärenz folgt aus dem Kompensator; offen bleibt die Paarerzeugungsrate, die Einheit der Uhr, κ und ein Form-(iii)-Zeuge mit endlichem Nullpunkt (das Modell liefert keinen).

Zum C5-Stand: Die Frage „gibt es einen endlichen Abschluss?" zerfällt in (a) *innerhalb* der multiplikativen Kollar-Rekursion — beweisbar nein, allein wegen `q > 0` — und (b) *außerhalb* davon. r88 schließt zwei der drei Kandidatenformen für (b); offen bleibt nur Form (iii): ein Zeuge außerhalb der Kollar-Iteration, der die Obstruktion selbst erreicht statt den Score.
