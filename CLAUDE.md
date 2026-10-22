# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Werkzeug zuerst

Für Querverweise, Rundenanlage, Guard-Prüfung, Ledger und Manifest gibt es den
Skill `quantum-sphaera` mit dem CLI `.claude/skills/quantum-sphaera/tools/qs.py`.
Theoremnummern **nie** von Hand zählen — `qs.py xref` bildet die LaTeX-Zähler nach.

## Was dieses Verzeichnis ist

Kein Software-Repository im üblichen Sinn, sondern ein einzelnes LaTeX-Monolith-Dokument: der *Quantum Sphaera Companion*, ein mathematisches Preprint von Marc Brendecke (über 1000 PDF-Seiten, über 64.000 Quellzeilen, 3,4 MB `.tex`). Keine Build-Skripte, keine Tests im üblichen Sinn. Die Qualitätssicherung läuft über LaTeX-Compile-Audits und Claim-Scope-Disziplin.

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

**Verhältnis zu GitHub** (`github` = `Moriarty1982/QuantumSphere-Unfold`). Die lokale Historie ist aus Archiven rekonstruiert und hat **keinen gemeinsamen Vorfahren** mit `github/main`; ein Merge ist nicht möglich, Inhalte werden übertragen. Auf GitHub ist der v4.9.0-Kandidat modular (`sources/research/v480-companion.tex`, 38 eingefrorene v4.7-Fragmente in `parts/v470/`, die **nicht editiert** werden dürfen; Korrekturen dort als Qualifikation in `parts/premise-audit.tex`). Seit PR #19 (am 2026-10-21 in `main` gemergt, Merge-Commit `b2a05a5`) trägt er die Runden r85–r94 und v4.8.0-r01–r20 als `parts/v480-release-layers.tex` und `parts/v480-post-release-layers.tex`, wortgleich aus der lokalen Arbeitsdatei; der Notizordner dort ist `notes/research/v4_8_0_r03_r12/`. Die lokale Historie liegt per Fast-Forward auf `research/v4.8.0-r03-r12-lokalgeschichte` (Belege für die Vorab-Notizen), Tag `RC25` ist gepusht. Neue Runden entstehen weiter lokal; für 4.9.0 müssen sie danach in `parts/v480-post-release-layers.tex` und den Notizordner nachgetragen und die Lokalgeschichte nachgeschoben werden. Builds unter MiKTeX: v4.9-Kandidat vorher 1044 Seiten / 3404 Labels, integriert 1124 / 3590, Overfull 58.

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

`article`-Klasse, keine `\input`/`\include` — alles in einer Datei.

| Zeilen | Inhalt |
|---|---|
| 1 – ~52.111 | Mathematischer Hauptkorpus: QAM-über-ZF, MML/MMA, Heisenberg-Compensator, Millennium Matrix, OP-Architektur |
| 52.112 – 62.648 | Solve-Log, Runden r03 – r54, je ein `\section` pro Runde |
| 62.649 – 62.705 | r55 – r80, auf ein Invariantentheoremlet komprimiert |
| 62.706 – Ende | r81 – r84: Frame-Skalen-Typisierung und Release-Scope |

## Der Runden-Workflow

Das Dokument wächst **append-only in nummerierten Runden** (`rNN`). Eine neue Runde ist ein neuer Abschnitt unmittelbar vor `\end{document}`; bestehende Runden werden nicht umgeschrieben. Aktueller Stand: **r94**, **v4.8.0-r20** und **v4.9.0-r13** (v4.9.0-r13: Zeitskala der gekickten Dualitätsdynamik aus dem r15-Uhrenmodell — ω = 1/σ_V, Kickabstand = Schwebungsperiode/6 für jedes Frequenzpaar, mit γ₁, γ₂ 0,15205 Uhreneinheiten, keine Sekunden (keine Identifikation Nullstellen ↔ Photonen, kein W_γ^glob); eine C5-Stufe passt nur in die R_A-Fenster V3/V5; 3/4 = Kontinuumswert der Hopf-Lesart) (v4.9.0-r12: r65-Text laut Autor verloren; Δ_γ < 1/5 strikt rekonstruiert aus P1 r14-Daten, P2 strikter r23-Bedingung, P3 multiplikativem Verlust je Auslese, P4 Uhrenfenster-Charts V3/V5 von R_A; bindend V3 als einzige Chart mit κ(N−1) = 1; tolerierte Drift tan α < 1/2, C5-Stufe außerhalb; Provenienz offen) (v4.9.0-r11: Modellvorschlag gekickte Dualitätsdrehung — Drehung z → e^{iωt}z, Kompensator-Kicks bei nτ, Partner-Reservoir; 3/4 eindeutig bei ωτ = π/6, Kick ändert s, kein endlicher Abschluss, Skala offen) (v4.9.0-r10: Deutung des C5-Faktors 3/4 als „drehen um π/6, dann kompensieren“ — C_HC R_α C_HC = cos α C_HC, reproduziert 3/4, 9/16, 27/64, 81/256 und n = 20, π/6 triolisch oder Hopf; unter der Deutung keine Form-(iii)-Zeugen aus der Transportgruppe von Lesart B (Isometrien verlagern, Boosts Boden |s|, Nullfelder nur Grenzwert); keine C5-Null-Aussage; Kern-Protokoll `llm/Erkundungsprotokoll_Kern.md`) (v4.9.0-r09: lokaler Frame-Faktor hängt laut Quelle von Beobachter, Zeit, Erdbahn und Potential ab, ohne Feldgesetz; Widersprüche thm:frame-offset ↔ thm:k-values strukturell aufgelöst; Geschwindigkeitslesart um ~10¹³ ausgeschlossen, nur Potentialkopplung β_X = k(X)κ überlebt (Compton-Uhr ungekoppelt), erklärt H0 nicht; P5 auf k(α)/k(G_N) = 1/2 korrigiert) (v4.9.0-r08: fest bei der Drift sind Photon-Frame-Werte, k = 0 und das strukturelle γ_L = γ_BI/γ_string; Vorzeichen k(α) = +1 für α gelöst (schließt r03 F2); Drift aus prop:H0-tension über den lokalen Faktor gegen Atomuhren (Yb⁺ 1,0(1,1)·10⁻¹⁸/Jahr) um ~6 Größenordnungen ausgeschlossen, statische Typisierung und Frühzeit-Änderung tragen nicht; Compton-Uhr m_e c²/ħ als k = 0-Uhr; H15 sagt konstantes θ_W voraus) (v4.9.0-r07: H14 Kegelwinkel = 2θ_W exakt widerlegt (z = +8,2), als Baumgraphen-Beziehung nicht entscheidbar; gezählte Erkundung (`llm/Erkundungsprotokoll_Weinberg_Kegel.md`), reale Teilcheneffekte durch m_W auf ≤ ¼ der Lücke begrenzt; Kegel = Parallelitätswinkel Π(η), H14 = Kopplungsverhältnis g/g′ = e^η, in MS-bar auf keiner Skala; Beobachtung cot θ_W on-shell ≈ γ_L; **H15 vorab festgelegt: m_W = 80,3615 ± 0,0018 GeV, Vergleich mit der ersten m_W-Weltmittelung nach 2026-10-21 ausstehend**) (v4.9.0-r06: Kreisschluss präzisiert — ein Photon- plus ein Tachyonbein lassen die Lücke d(1 − 1/v), zwei Tachyonbeine (Tolman) schließen; Trefferkette mit Kegel cos ϑ = 1/v = β_sym (56,68°), alle Treffer gleichzeitig im Materie-Frame, dort Tachyon = Phase iπ/2; beschleunigter Tachyon: unendliche Geschwindigkeit an einem Punkt, Paarereignis; elektroschwache Massenmatrix als Portgewichtung mit masselosem Photonport, bei θ_W = 45° Kompensator-Port, formal) (v4.9.0-r05: Millennium-Matrix auf dem Dublett nur als Portgewichtung λ₊C + λ₋A — (T4) schließt Boosts und allgemeine Dualitätsdrehungen aus; **Lesename seit r05: „layer-transport matrix“ für M_16, „port-weighting matrix“ für die Dublett-Einschränkung**, frühere Wortlaute unverändert; dritte Achse = Helizität bei komplexen Amplituden, Kerr-Krümmung Ψ₂ komplex mit entgegengesetzten Seiten in den Halbkugeln; Photon aus Materie + Tachyon nur bei gekreuzter Orientierung, rücklaufendes Photon kann das Tachyon nicht erzeugen) (v4.9.0-r04: Kompensator als 2×2-Matrix auf dem (E, B)-Dublett — J_B = σ_x, T = σ_z, Dualität = Drehung, C = −1 erzeugen O(2), C_HC = ½(1+σ_x) linear; Zustandsmatrix G = FᵀF mit Bloch-Vektor (Re s, Im s)/2u in der Einheitsscheibe, Licht in der Mitte, |b| = 1/cosh 2η_f; Interferometer misst b; Identifikation mit der Millennium-Matrix offen) (v4.9.0-r03: Kompensator als Zweiarm-Interferometer — C, A sind die Ausgänge, mit antilinearem J nur reell-linear; Ladung → Dyon, Licht → E ∥ B; Auslese D(φ) = Im(e^{iφ}s), Sichtbarkeit 1/cosh 2η_f; Orthogonalität aus prop:compensator gilt für das Produkt z × J_B z = 2E×B, nicht für den Mittelwert) (v4.9.0-r02: Rundlauf M→P→T→P→M — Seite des Durchgangs = sign(E·B), Seitenwechsel gibt z → −z = Ladungskonjugation C = PT; involutive Umkehrwalze muss antilinear sein, Vertreter J_B: E ↔ B = Dualität(π/2) nach T, Eigenkanäle je auf einer Seite des Photons; thm:core-Kompensator liefert nur Re s = 0, kein Nullfeld; OP5-Leckdiagnosen mit J_B null nur für reelle Drehungen, Entsprechung Wendepunkt/Durchgang nicht übernommen) (v4.9.0-r01: Photon-Frame als neutrale Achse — Autorangabe —, γ_L bis v2.29.0 als 1,197 = cosh η geführt, seit v2.29.1 1,864; Lorentzfaktor-Umrechnung komponiert über drei Frames nicht, Doppler-Gesetz schon; thm:tribonacci ⇔ cosh 2η = e^η; Wege (A)–(C) offen) (r03: Dimensions- und Zahlenaudit der Konstantenschicht; r04: Entkopplung von der Riemann-Arbeit, eigenständiger Heisenberg-Kompensator, Kaskade und reparierte Triolen-Hierarchie; r05: korrigierte explizite Formel in der Feldgleichungsschicht, Θ-Summen-Vermutung widerlegt, GUE empirisch; r06: Signatur des Biquaternion-Kerns, Lesart B (ℂ³ mit SO(3,ℂ)) als Arbeitslesart, Triolen-Lemma, Nullkegel = S₀; r07: Sektor-Zuordnung s > 0 Materie / s < 0 Tachyon, Dualitätswinkel; r08: Test von P1, Photon-Frame-Entfaltung nicht bestätigt; r09: P2 durch Daten ausgeschlossen, P3 Koinzidenz, Register aller Vorhersagen und Hauptsätze mit aktuellem Status; r10: Koide-Form als Triole, Lesart B ist Kinematik, Dynamik fehlt; r11: erster vorab festgelegter Test, δ = K/3 widerlegt; r12: vorab festgelegte Neutrino- und Mischungstests H2–H8, Stab(+e₇) mit Δ(96)-Invarianten, Cayley–Dickson-Involution als CP (θ₂₃ = 45°, δ_CP = 270°), `prop:pmns-z3` widerlegt; r13: Nachprüfung mit JUNO 2026 (TM1 und H8 disfavorisiert, H2 gestützt), H9 β_sym-Vorhersage für JUNO, H10 Assoziator [e₄,e₅,e₆] = −2e₇ ohne Auswahl, Farbe und Generation auf demselben Triplett, Abgleich mit dem v4.9-Kandidaten; r14: Trennung von Farbe und Generation (Sedenionen nur 2 farbige Generationen; Triality-Form Re((xy)z) mit 3 × 3 unabhängigen Zuständen empfohlen), Δ(96)-Mischungs-Lesart zurückgezogen; r15: oktonionische Hopf-Faserung als Träger der drei Triality-Plätze, symmetrischer Punkt ω mit Stabilisator SU(3) = Farbe; r16: vorab festgelegter Test H11, Massen aus invarianten Funktionen auf dem Tripel-Raum widerlegt (bis Grad 4 höchstens zwei verschiedene Normen, Grad ≥ 6 nötig); r17: Zeitrichtung der kosmologischen Anteile, `thm:dark-energy` mit `prop:H0-tension`/`prop:saturation` nicht vereinbar (dβ_sym/dt umgekehrt), Auswege offen; r18: Drei-Frame-Typisierung von `\bsym` in Rapiditäten (Nachbar-Kreuzterm γ = 1,197, Gegenüber γ_L = 1,864), γ_L in der Konstantenumrechnung ist der Materie–Tachyon-Term, z₋ = 0,422 Halbierung in der falschen Variablen, r17 auf `prop:saturation` (2) eingegrenzt; r19: Auslesewürfel pro Frame mit Übergängen tragen nur über die Holonomie Neues, in Lesart B keine Lorentz-Verbindung zwischen Materie, Tachyon und Photon (nur Dualitätsdrehung, Z₂-Holonomie um das Photon), alte Lesart als photonzentrierte Sicht, H12 und K39 festgehalten; r20: H13 (Wigner-Holonomie) widerlegt, Halbwinkel-Nachbefund nicht registriert, Tachyon-Frame mit gleicher Holonomie und Hauptspinoren wie Materie, Überlichtrapidität artanh(1/v) + iπ/2 als Brücke zwischen alter Lesart (Realteil) und Lesart B (Imaginärteil = Dualitätswinkel), Kreuzterme mit dem Tachyon imaginär; alle source-only). **Neue Vorhersagen nur mit Vorab-Notiz:** Hypothese, Daten und Kriterium unter `llm/Vorab_Notiz_*.md` committen, erst dann rechnen. Wer einen älteren Satz zitiert, prüft zuerst das Register in `sec:v480-r09-p2-p3-reclassification`. Guard-Linter für neue Runden: `python llm/training/guard_linter.py <tex> --start N`. Runden der v4.8.0-Linie heißen `v4.8.0-rNN`, Labels `sec:v480-rNN-...`; `qs.py outline` und `ledger` erkennen beide Formen.

Eine Runde folgt einem festen Muster:

1. `\section{v4.7.0-rNN <Titel>}` bzw. `\section*{...}` plus `\addcontentsline{toc}{section}{...}` — beide Varianten kommen vor; ab r82 wird durchgängig `\section*` mit `addcontentsline` verwendet
2. `\label{sec:rNN-<kebab-case-titel>}`, jede Unterüberschrift bekommt ebenfalls ein `\label{subsec:rNN-...}`
3. Source-only-Klausel: kein PDF, keine neue DOI, kein Public Release, sofern nicht ausdrücklich anders beauftragt
4. Inhalt als Theoremlet mit `\paragraph{Theoremlet rNN.}` und `\paragraph{Proof sketch.}`, abgeschlossen mit `\(\square\)`
5. Guard-Update am Ende: die Residual- und Guard-Vektoren der Runde

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

**Achtung, lokale Arbeitsdatei:** `Quantum_Sphaera_Companion_v4_8_0_source.tex` trägt auf ihrer Titelseite weiterhin die v4.8.0-DOI und in den Source-only-Klauseln der Runden „v4.8.0 Version DOI … unchanged". Das ist für die Runden bis v4.8.0-r20 richtig (sie sind so in v4.9.0 veröffentlicht). Neue Runden nach dem 4.9.0-Release heißen **`v4.9.0-rNN`** (Labels `sec:v490-rNN-...`) und nennen in ihrer Source-only-Klausel die v4.9.0-Version-DOI. `qs.py doi` kennt ohne Parameter noch v4.8.0 als aktuell; für 4.9.x-PDFs `--version-doi 10.5281/zenodo.23534954 --version-label v4.9.0` angeben.

**Offener Arbeitsschritt zum 4.9.0-Release (auf Wunsch des Nutzers für die nächste Version zurückgestellt):** PR #21 (`release/v4.9.0-prep`, enthält Payload, Titelseite, `CITATION.cff`, README mit DOI-Badge) in `main` mergen, Tag `v4.9.0` setzen, GitHub-Release `v4.9.0` mit Verweis auf DOI und Zenodo-Record anlegen; danach `DOI_ROLES` in `qs.py` auf v4.9.0 umstellen. Bis dahin zeigt GitHub `main` noch v4.8.0 als aktuelle Version. Details im Skill `zenodo-release`.

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

Unter MiKTeX 25.12: v4.8.0 (Tag neu gebaut) 1045 Seiten / 3369 Labels, RC25 (v4.8.0-r20) 1096 / 3474, Overfull durchgehend 58 (das v4.8.0-Release meldete unter TeX Live 45), alle harten Werte 0.

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

**Nie die ganze Datei lesen.** Über 64.000 Zeilen. Mit `sed -n` gezielt Bereiche holen oder das Grep-Tool mit `-C` verwenden.

**Nie behaupten, ein Datum fehle, ohne die Nachbarrunden zu prüfen.** Die Solve-Kette tabelliert in einer Runde und verbraucht in einer anderen. r87 behauptete, die V9-Chart-Parameter seien nicht dokumentiert — sie stehen in r14, eine Runde vor der gelesenen, und der zugehörige Lift in r17, zwei Runden danach. Die Korrektur ist als r89 protokolliert. Eine Aussage über Fehlen betrifft den ganzen Monolithen und braucht einen Grep über die gesamte Datei plus die angrenzenden Runden.

**Keine externen Grafiken.** `\safegraphic` ist in der Präambel definiert, wird aber nirgends aufgerufen — es fehlen keine Asset-Dateien, und ein Platzhalterrahmen im PDF wäre ein Fehler, kein Normalzustand.

**Der RC19-Snapshot ist eingefroren.** `_RC19_concept_doi_restore_source.tex` dokumentiert den Zustand, der als RC19 kompiliert und im Manifest gehasht wurde. Er wird nicht nachträglich verändert — sonst geht die Provenienz verloren. Alle Änderungen laufen in `_source.tex` und gehören zum nächsten RC. Seit der ersten Post-RC19-Änderung sind die beiden Dateien deshalb **nicht mehr byte-identisch**, und der Manifest-Eintrag für `_source.tex` ist überholt; beides ist gewollt. Ein neuer RC bekommt einen neuen Snapshot unter neuem Namen und ein neu erzeugtes Manifest.

## Offene Zweige

Aus der r48-Branch-Queue: Q₁ (r49–r54), Q₂ (r55–r80), Q₅ (r86) abgearbeitet, Q₃ in r87 kalibriert. Stand nach r90–r94 und v4.9.0-r10:

- **Q₄** C4-Mixed-Kernel-Lokalisierung — durch r91 ausgeführt: `β₄ = 1/256` ist eine terminale Schwellenskala, ihre Ausgabe wäre der verbotene Schritt; **geschlossen als „nicht ausgebbar“**
- **Q₃ Restteil**: `Δ_γ < 1/5` — r90 (Kohärenzschranke 2/9) und r92 (exakt als relative Verstärkungsreserve von V3 auf der Kette R_A, 1 − (8/5)/2) rekonstruiert; **v4.9.0-r12 leitet die strikte Schranke unter offengelegten Prämissen (P1)–(P4) her**; der r65-Volltext ist laut Autor verloren (2026-10-22), die Provenienz bleibt offen
- **C5-Faktor 3/4**: r94 deklariert, nicht hergeleitet; v4.9.0-r10 bietet eine Deutung (drehen um π/6, dann kompensieren)
- **C5 Form (iii)**: offen; v4.9.0-r10 schließt unter seiner Deutung Zeugen aus der Transportgruppe von Lesart B aus

Eine konkrete, guard-neutrale Datenlücke: **der unkomprimierte r65-Text** für `Δ_γ < 1/5`. Er liegt nicht im Projektordner und auch nicht in `C:\Users\marcb\Downloads\Quantum Sphere` — jener Ordner enthält 841 `.tex` der Versionen v0.1 bis v3.35, aber kein v4-Material und keinen einzigen Treffer für `Delta_\gamma`.

Zum C5-Stand nach r86/r88: Die Frage „gibt es einen endlichen Abschluss?" zerfällt in (a) *innerhalb* der multiplikativen Kollar-Rekursion — beweisbar nein, allein wegen `q > 0` — und (b) *außerhalb* davon. r88 schließt von den drei Kandidatenformen für (b) zwei: der subtraktive Kanal trifft die Null nur bei maßnull-abgestimmtem `c` und verlässt danach den zulässigen Bereich, braucht also eine Stoppregel — und die ist die von `LG₅^bd` verbotene Abschneidung. Offen bleibt nur Form (iii): ein Zeuge außerhalb der Kollar-Iteration, der die Obstruktion selbst erreicht statt den Score.
