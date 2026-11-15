# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 15.11.2026 (Claude Opus)
- **GitHub:** **PR #126 gemergt als 823802e** (Abbildung C⊗S → C⊗H⊗O, gebogene Achsen), davor #125 (087d13f,
  Dauerauftrag Versionsverwaltung) und #124 (f5ede73, OP3-Rückwärtssuche). **Keine offenen PRs.** Gemergte Zweige
  lokal und auf GitHub gelöscht. Davor gemergt: #123 (14856e3, Codex), #122 (f04c6ad), #121 (f39ca00, r13), #120,
  #119, #108–#118.
  Nicht geprüft: die Darstellung von Mindmap und Formeln im GitHub-Wiki (im Browser des Modells gesperrt).
- **Dauerauftrag 15.11. (AGENTS.md):** Interne Nummern (H, k, Runden, CT) ohne Rückfrage vergeben; Übergabe- und
  Buchführungs-Commits ohne Rückfrage auf `main` pushen. Inhalt nur über PR; Zenodo und neue Versionen nur mit Freigabe.
- **Autorentscheidung 15.11. zur nächsten Version:** Erst weiterforschen, bis genug Stoff für eine neue Version
  *beider* Ausgaben (Vollausgabe und Physik-Paper) da ist; jetzt kein Ergänzungsentwurf. Seit v5.0.0 ist der Text des
  Physik-Papers unverändert (`qam/editions/v5_physics_article.tex`). Kandidaten für eine spätere Ergänzung:
  Generation und Spin über Farbe und Ladung nicht trennbar (15.11.); H102 als Vorhersage mit Platzhaltern (CT-001/CT-002, sieben Guards, nicht blind) neben dem Satz „No lepton masses …
  predicted“; das präzisierte Generationenhindernis (Weg A gegen Weg B, r13); die benannte Auswahlregel
  (Gleichgewichtung zweier unverzerrter Terme = F-Selbstdualität, PRs #123/#124).
- **Neu, 15.11. (`notes/research/op3_cs_dixon_map_2026_11_15/`, Erkundung, nicht blind, Zweig
  gemergt über PR #126):** Abbildung C⊗S → C⊗H⊗O.
  - Farb- und ladungstreue Abbildungen bilden eine 20-dimensionale Familie.
  - Die Familien-su(2) geht nur auf die Linkswirkung von H (Lorentz-Spin), sektorweise mit entgegengesetzter
    Orientierung (Leptonen det −1, Quarks det +1). Auf Isospin und r33-Slotdrehung geht sie nie.
  - Lesart: Die zwei Generationen von CT-003 sitzen am Platz des Spins; Farbe und Ladung trennen Generation und Spin
    nicht. Das schwächt Weg A.
  - Kandidat für das Physik-Paper (Abschnitt particles).
  - Nachtrag „gebogene Achsen“ (`bent_axes.py`): det G = (√2 cos φ − 1)/2. Der flache Oktant (φ = π/4) ist der
    Qubit-Grenzfall mit einer Masse null. Mit φ = 2/3 rad ergeben sich die drei Leptonmassen mit Koide 2/3; die
    Biegung π/4 − 2/3 = 0,1187 rad ist der CT-001/002-Fluss. Kandidat für das Physik-Paper (Abschnitt masses).
  - Nächste mögliche Frage: Was unterscheidet eine Generation von einem Spinzustand (etwa Lorentz-Verhalten, Boosts,
    Chiralität)?
- **Lokal:** Hauptordner auf `main` = 823802e (plus dieser Übergabe-Commit).
- **Neu, 14.11. (`notes/research/op3_action_balance_search_2026_11_14/`, Erkundung, nicht blind, Rückwärtssuche,
  auf „Wirkung suchen“ des Autors):** Gesucht war eine vorhandene Wirkung, die H = −a(Q + R) mit gebunden gleichen
  Kopplungen liefert (nächster Ansatz aus der Codex-Notiz `op3_reference_energy_selection_2026_11_14`).
  **Keine gefunden.**
  - Native Slotsymmetrien (monomial, 1296 Elemente) bilden ⟨D⟩ nie auf ⟨τ⟩ ab, können a = b also nicht erzwingen.
  - Alle 54 gleich gewichteten Paare von Eigenlinien aus zwei verschiedenen Weyl-Untergruppen (MUBs) wählen den
    Oktanten-Bezug (K_orb = 2/3, π/4), denn die Überlappung ist stets 1/3. Q und R sind nicht ausgezeichnet,
    offen ist nur die Gleichgewichtung.
  - Demokratische Zählregeln treffen nicht (alle vier Eigenwert-1-Linien: K_orb = 3/5).
  - Lesart: Das Gleichgewicht ist die F-Selbstdualität von −J(Z+Z†) − h(X+X†) bei J = h. In einer Potts-Kette wäre
    das der kritische Punkt. Eine solche Kette gibt es im Companion nicht.
  - **Das ist die fünfte Variante mit derselben offenen Voraussetzung (nativer Bezug bzw. F). Die OP3-Linie ruht.**
- **Codex-Stand vom selben Tag (PR #123):** Die Bezugsauswahl durch H = −(aQ + bR) braucht a = b. Ein festes H bricht
  S, das Minimum ist keine Präparation, die Bahn-Gram-Matrix hat Rang zwei. Die aktive Fourier-Route ruht: F erhält
  die Trialitätsform nicht, tau-erhaltende Dynamik erzeugt F nicht.
- **Hypothesen:** zuletzt H104 (k226) widerlegt. **Als Nächstes frei: H105, k227.**
  - H100 (nächster NuFIT-Fit, Frist 31.12.2027) ist offen; am 14.11. war NuFIT 6.1 die neueste Version.
  - H102 ist offen: m_τ = 1777,134 MeV gegen die erste PDG-Ausgabe nach dem 13.11.2026.
- **Platzhalter:** CT-001 partially_constrained, CT-002/CT-003 placeholder, keiner strukturell abgeglichen.
  CT-001/CT-002 ruhen bis H102.
- **Ideen I1–I5:** geprüft, kein neuer Auslöser.
- **Letzte Runde:** v4.10.0-r13 (PR #121). Seither nur Erkundungen, keine neue Runde.
- **Zweige, die stehen bleiben (nicht gemergt):**
  - auf GitHub `codex/op3-triality-mass-bridge`, `codex/v5-zenodo-release` und `codex/v5-zenodo-upload-record`;
  - lokal `claude/quantenphysik-paper-herleitung-e723a3` und `claude/wizardly-mendel-c790d3`;
  - lokal `claude/anthropic-skills-weitermachen-08cc3e`: inhaltsgleich in #118, Löschung braucht ein Wort des Autors.
  - `git fetch --prune` meldet weiterhin „Permission denied“ für verwaiste `.git/worktrees`-Einträge.

- **Nachtrag (Durchsicht der Teilbäume):** Die Mischung r46/r47 hat dieselbe Form (Zirkulante plus Einslot-Maske).
  Die Leptonmaske W_l = diag(0, 0, −3) ist ein reiner Projektor, die Quarkmaske nicht. In r47-Form gilt K_orb = 2/3
  bei ε = 1/12; ε ist in r47 nicht hergeleitet. Weitere Kandidaten: r07 (z ↦ iz als EM-Dualität, es fehlt das
  Wörterbuch D, τ ↔ B, E). Δ(96) scheidet aus, weil die Gruppe monomial ist.
  Chern-Simons und modulare S-Matrix kommen im Companion nicht vor.

## Nächster Schritt
- **Bewachter Kern als flussverdrängende Kappe (15.11., Erkundung, `notes/research/op3_guarded_core_flux_2026_11_15/`,
  Zweig `research/op3-guarded-core-flux`):**
  - Fundstelle v470/05 (X = S³ ∖ B_ε(K)).
  - Der Kern muss keinen Fluss tragen; ausschließen reicht. Liegt er im Dreieck, ist das Vorzeichen richtig, und die
    genaue Lage spielt keine Rolle.
  - Verlässt der verdrängte Fluss das Dreieck, gilt φ = π/4 − γ_M/2 (die H102-Beziehung). Verteilt er sich
    gleichmäßig, gilt φ = 0,6795.
  - Offen: warum der Fluss das Dreieck verlässt und warum Ω = γ_M; dazu Kugel B_ε(K) gegen Faser-Volltorus.
  - Mögliche Brücke: der bewachte Kollapskern als Horizont-Punktierung (CT-002, I1).
  - Faden 1: Abfluss = Lesart „removed“ (v470/05: „removed or shielded“); Stützen in v470/05, v470/32 und v470/10.
  - Faden 2: Berichtigung, H99 legt die Neutrinos ein Oktant über den Oktanten (negative Wurzel), nicht auf ihn.
    Beide Sektoren verlieren denselben Kern γ_M; „Ladung legt den Kern ins Dreieck“ ist verworfen.
  - Faden 3: Die Kugel B_ε(K) bricht die Fasern über einer Kappe vom Radius 2ε. γ_M entspricht ε = 7,90° (binär) oder
    einem Volumenanteil γ_M/(4π) des S³ (gewichtet, ε = 25,94°). ε ist im Paper frei.
  - Schritt 1: Die Zählregel legt den Kern nicht fest. Literatur (ABK gr-qc/0005126, ENP 0905.3168, über alphaXiv
    geprüft): gleiche Struktur, aber kein fester Winkel γ_M (Level 4π/γ_M = 52,9 nicht ganzzahlig).
  - Schritt 2: Genau ein Kern ist topologisch ausgezeichnet: Biegung ohne freien Parameter. Kein Kern biegt nicht; ab
    zwei Kernen gibt es n − 1 freie AB-Holonomien. Berichtigung zu Faden 1: Bei einem Kern entweicht kein Fluss; A heißt
    flussfreier Kern mit verdrängtem Fluss außerhalb des Dreiecks (Gegenpol, Dirac-Faden).
  - Umkehrwalze (Hinweis des Autors, Enigma-Analogie; r02.2/r02.3, v470/24): Eine fixpunktfreie antilineare Involution
    ist auf Spin ½ die Antipodenabbildung (Θ² = −1). Liest man den Kern als Umkehrwalze, geht der verdrängte Fluss
    zum Gegenpol; das ist Fall A in beiden Sektoren. Lesart.
  - Offen bleibt nur Ω = γ_M.
  - PR #127 offen (Zweig `research/op3-guarded-core-flux`); Schritt 2 wird nachgeschoben.
- **Stand 15.11.:** Die Notiz mit den Nachträgen 1–9 ist über PR #124 auf main.
  Inhalt der Nachträge: r47-Maske, ε-Vorwissen r50–r56, ε* = (1/3)ln((1+√3)/2), Photonengewichte,
  Frame-Kreuzprodukte (sl(2,R)), Levi-Civita, geordnete Produkte und r33.
- **Befund der r33-Prüfung (Nachtrag 8):** r33 ist nicht der Engpass. Die Nachträge 4–7 sind dort berichtigt.
  Jede Frame-Ebene ist kommutativ, und die Frame-Triole ist eine Transposition (r38). Das Levi-Civita-Tripel mit
  Hurwitz-Zyklus liegt nativ auf Im H (r33.1(a,b)), bricht dort aber Q_em.
- **H105 nicht vergeben**; frei sind weiterhin H105 und k227.
- **e8 geprüft (Nachtrag 9):** Die Frage war schon beantwortet (`op3_family_su2_right_action_2026_11_14.md`).
  Unter e8 wirkt das Tripel R_e7, R_e8, R_e15 neutral als Levi-Civita-Tripel mit Hurwitz-Zyklus, trägt aber nur zwei
  Generationen als Dublett. In r33 sind die Generationen dagegen die drei Achsen, dort aber nicht neutral.
  Gesucht ist eine Struktur, in der beide Rollen zusammenfallen. Nicht gerechnet ist die Lage von H_n relativ zum
  r33-Faktor H; die Abbildung C⊗S ↔ C⊗H⊗O fehlt.
- **Mögliche nächste Frage (Autorentscheidung):** Abbildung C⊗S ↔ C⊗H⊗O suchen und die Lage von H_n zum r33-Faktor H bestimmen. Vorher Vorwissen und Suchrichtung prüfen.
- **Offen:** H100 und H102 bei neuen Daten auswerten
  (`k222_test_h100.py`, `k224_test_h102.py`).

## Profil der fehlenden Struktur
Gesucht ist ein farb- und ladungsneutrales Qubit, auf dem der Generationszyklus als Element der Ordnung 3 wirkt,
mit einem Bezugszustand unter dem magischen Winkel arccos(1/√3) zur Zyklusachse. Gleichwertig nach dem 14.11.:
eine native Begründung für die F-Selbstdualität (gleiche Gewichte zweier unverzerrter Rang-eins-Terme).

## Inhaltlicher Stand
OP3/OP4 offen; OP1–OP5, C5, C6/T2 und die Guards sind unverändert. Koide 2/3, die Phase und die native
Massenbrücke sind nicht hergeleitet. v5.0.0 bleibt die Baseline; keine neue Veröffentlichung vorbereitet.

## Pflichten in jeder Sitzung
`AGENTS.md`, `wiki/Gesamtbild.md`, die einschlägige Anleitung unter `notes/anleitungen/`, die Auslöser in
`notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md`. Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen.
Merges nur nach Freigabe. Wiki im selben PR. `.codex/environments/` bleibt unversioniert.
