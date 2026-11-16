# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 17.11.2026, nachts (Claude Opus 5.5)

### Release v5.2.0 in Arbeit (Entscheidung des Autors vom 17.11.)
- **Zenodo-Entwurf 24294648**, reservierte Version-DOI **10.5281/zenodo.24294648**, **unveröffentlicht**.
  Concept-DOI 10.5281/zenodo.19210728; Vorgänger v5.1.0 (10.5281/zenodo.24237112).
- Läufe: Trockenlauf 43978552171, Reservierung 43978639426, Paarbau 43978954178 (Commit 8fb6e93; Vollausgabe 1457 S.,
  Physik 30 S., 0 undefinierte Verweise, 0 Overfull), Upload-Trockenlauf 43981250074, **Upload 43981330807**.
- Upload: 8 geerbte v5.1.0-Dateien entfernt, 8 neue Dateien hochgeladen; Metadaten mit DOI gesetzt. Geprüft im Lauf:
  unveröffentlicht, DOI, Version v5.2.0, alle 8 MD5-Summen gleich. **Gescheitert nur die Vorschau-Prüfung** (wie bei
  v5.1.0: das Werkzeug setzt die Vorschau nicht). Der Autor setzt die Vorschau auf `Quantum_Sphaera_Companion_v5_2_0_full.pdf`.
- **PR #166** (`release/v5.2.0-prep`, offen): Runde v4.10.0-r28, Physik-Abschnitt 5.8 („Where the missing number comes
  from“) und ein Satz im Ausblick, `release/zenodo/metadata_v5_2_0.json`, `release/v5.2.0/README.md`, DOI auf Titelseite
  (`working-preamble.tex`), `qam/editions/v5_release.json`, `tools/qs.py` DOI_ROLES, `AGENTS.md`, Wiki. Issues #17, #10, #131 nachgezogen.

### Nächste Schritte (je nur mit ausdrücklicher Freigabe des Autors)
1. Autor: Vorschau im Entwurf setzen, Entwurf ansehen, veröffentlichen (oder Veröffentlichung über
   `zenodo-v5-candidate.yml` mit `publish=true`, `confirm_publish=true`, `deposition_id=24294648`).
2. Nach der Veröffentlichung: öffentlichen Record prüfen (8 Dateien, MD5, Vorschau, Version, Relation zu v5.1.0);
   `release/v5.2.0/README.md` auf „Published“ ziehen; `AGENTS.md` Baseline auf v5.2.0; Wiki Home, Versionen-und-Quellen, Gesamtbild.
3. PR #166 mergen (Freigabe), Tag `v5.2.0` auf den Paketquellstand 8fb6e9378f6e6789697c60d3ba8b748cc2b56de6, GitHub-Release.
4. Gemergten Zweig löschen.

### Forschung
- **Letzte Runde:** v4.10.0-r28 (Stand Restbiegung und Zählregel, r28.1–r28.7, PR #166). Davor r27 (PR #156).
- **Hypothesen:** zuletzt vergeben **H111** (k233, widerlegt). Frei: **H112, k234**.
- **Inhaltlicher Stand:** Die Phase ist im Träger starr (H106–H111 widerlegt); der bewachte Kern (φ = π/4 − γ_M/2) entgeht
  dem über die Verbindung, seine Größe kommt nur aus der Zählregel von M (Gewicht 2, gewählt). H102 (m_τ = 1777,134 MeV,
  +2,3σ) prüft Kernlesart, U(1)-Zählung und Spektrum √(j(j+1)) gemeinsam. Register-Entropie erklärt P (2j+1) und R, nicht M;
  Regel von M = reine Stränge mit unbekanntem Port. Offen: warum M mit Gewicht 2 zählt (OP1). Möglicher nächster Schritt:
  prüfen, ob die Stränge masselos sind und normal queren (S1′); Test nur mit Vorab-Notiz (H112).
- OP1–OP5, C5, C6/T2 offen. Notizen unter `notes/research/op1_*_2026_11_1[67]/`, `op3_*_2026_11_16/`, `v4_10_0_r28/`.
