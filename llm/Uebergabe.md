# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 14.11.2026, abends (Claude Opus)
- **GitHub:** `main` = 0f8fda0 (PR #123 von Codex, gemergt als 14856e3, alle Läufe grün). **Keine offenen PRs.**
  Der gemergte Zweig `codex/op3-fourier-native-gate` ist auf GitHub gelöscht (Dauerauftrag).
  Davor gemergt: #122 (f04c6ad), #121 (f39ca00, r13), #120, #119, #108–#118.
  Nicht geprüft: die Darstellung von Mindmap und Formeln im GitHub-Wiki (im Browser des Modells gesperrt).
- **Lokal:** Hauptordner auf dem Zweig `research/op3-action-balance-search` (von 0f8fda0), 15 Commits, **gepusht, PR #124 offen**. Er enthält die Erkundung unten, das Wiki (Forschungsstand, Offene-Probleme, Wiki-Pflege) und
  diese Übergabe.
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
- **Stand 15.11.:** Zweig `research/op3-action-balance-search`, gepusht, PR #124 offen.
  Notiz mit den Nachträgen 1–8: r47-Maske, ε-Vorwissen r50–r56, ε* = (1/3)ln((1+√3)/2), Photonengewichte,
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
- **PR #124 offen** (https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/124), Zweig gepusht. Merge nur auf „PR 124 mergen“.
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
