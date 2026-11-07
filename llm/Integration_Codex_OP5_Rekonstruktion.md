# Integration der Codex-OP5-Rekonstruktion vom 6./7. November 2026 (Runde v4.10.0-r11)

Stand: 7. November 2026 (Claude). Auftrag aus der Sitzung, die r06–r10 geschrieben hat: die Arbeit, die der Autor parallel mit
Codex auf GitHub gebracht hat, lokal übernehmen und als Runde einordnen, ohne bestehende Runden umzuschreiben. Muster:
v4.9.0-r69 (`llm/Integration_OP5_Serie.md`).

## Quelle

GitHub `main`, Merge `4ae32c9` (Zweig `codex/op5-question-rebuild`, Commit `4ec7994` und Vorgänger), nach PR #86 (r09) gelandet.
Diff `0fca1e1..4ae32c9`: 52 Dateien, 3265 Zeilen.

| Gruppe | Dateien |
|---|---|
| OP5-Rückverfolgung (6.11.) | `notes/research/op5_neuaufbau`, `op5_route_inventory`, `op5_field_readout_inventory`, `op5_operations_inventory`, `op5_frame_identification`, `op5_denominator_audit`, `op5_reconstruction_verdict`, `op5_state_selection_exploration`, `op5_spin_selection_audit`, `op5_common_state_access`, `op5_projector_spin_bridge` (alle `_2026_11_06.md`) |
| Rückgang zur Grundidee | `notes/research/qsc_back_to_basic_idea_2026_11_06.md` |
| QAM-Notizen | `qam_frame_physics_interface_design_2026_11_06.md`, `qam_dorau_much_rindler_2026_11_07.md`, `qam_quelle_rueckweg_auslesung_2026_11_07.md`, `qam_r27_richtungsreadout_2026_11_07.md` |
| QAM-Software | `qam/tex/qam-physics.sty` (Profile, Kontexte, Formel-Export, deklarierte Konversion), Beispiele `qam/examples/{physics,dorau-much,gram-boost,hc-return,r27-two-copy}.tex`, Tests `qam/tex/tests/*` (34 Fälle, `run_tests.py`), `qam/README.md`, `qam/tools/qamhash.py` |
| CI | `.github/workflows/qam-lean.yml`, `qam-tex.yml` |
| Wiki | `QAM.md`, `Offene-Probleme.md`, `Gesamtbild.md`, `Wiki-Pflege.md`, `Hinweise-fuer-LLMs.md` |
| Übergabe | `llm/Uebergabe.md` (auf GitHub neu angelegt, Codex-Stand) |

Lokal übernommen mit `git checkout 4ae32c9 -- <notes/ und qam/>` (44 Dateien). Die Codex-Übergabe liegt lokal als
`llm/Uebergabe_Codex_2026-11-07.md`; die lokale `llm/Uebergabe.md` bleibt die Claude-Übergabe. `.github/` und `wiki/` gibt es lokal
nicht (sie leben nur auf GitHub). Der lokale `qam/`-Ordner enthält nur die neuen Dateien; bauen lässt sich QAM nur im GitHub-Klon.

## Aussagen in Kürze

1. **Autorentscheidung (6.11., über Codex):** Die historische Herleitung der OP5-Auslöschungsaufgabe (spektraler Term → metrische
   Wirkung → nackter Λ-Term → Auslöschung durch Θ und R) wird als Grundlage ausgesetzt; Wirkung und Skala waren nie hergeleitet
   (v4.8.0-r04/r05). Neue Arbeitsfrage: welche unabhängig definierte Messgröße lässt sich begründet auslesen.
2. **Quelle–Rückweg (Teile 21/22):** bedingtes Schema, als solches richtig; keine native Route mit auswertbaren A₂, A₃, A₄,
   Klassentest und Auslesung instanziiert. Das Mittel m = (f + b)/2 verliert die Zweiginformation d = (f − b)/2 (Scherungsbeispiel).
3. **Feld/Port/Operationen:** p₊ = ½ + E·B/tr G; Portprojektion ist rangsenkend, kein passiver Framewechsel; J_B, z ↦ iz, Zeitumkehr,
   Boost sind verschiedene Operationen.
4. **Frames/Parameter:** R ≠ P (r24); γ_L vergleicht M mit R; q = λ₋/λ₊ = tanh²η, kleinerer Eigenanteil q/(1 + q).
5. **Nenner:** Eigenwertverhältnis, Ausflussanteil aus S⁸, γ-Kontrast und Ω_M haben verschiedene Nenner; r31 setzt β² ein.
6. **Zustandsauswahl:** Familie E_q, B_q mit beliebigem q bei gleicher Skala, Orientierung, Sektor; Energiegewichte machen aus q
   jeden Anteil w₋q/(w₊ + w₋q).
7. **Spinauswahl, gemeinsamer Zustand, Projektorbrücke:** Sättigung wählt m = ±j, nicht j = ½; endliche Spinmengen geben
   verschiedene γ; eingeschränkter Zugriff ≠ Energie null; C_ch vertauscht mit der Tachyon-Abbildung (r51), eine kompatible
   Brücke gäbe gleiche Masken weiter.
8. **Grundidee:** vier Bedeutungen von „ein Objekt“; Dualität verbindet s > 0 und s < 0 gleichen Betrags, nicht s ≠ 0 mit s = 0;
   Kompensatorbild hat s′ = 2i|E′|² ≠ 0.
9. **QAM (7.11., Autorpräzisierung):** QAM ist Frame-Schnittstellensprache; ART/QM gelten im zugeordneten Frame; Übergänge nur mit
   deklarierter Map und Zielformel. Dorau–Much als QAM-Beispiel (Rindler nicht mit M/T/P identifiziert). r27: Richtungsmittel
   verliert d, das quadratische Register erhält die Spur; γ_L = 1/r = cosh 2η_ref ist der gewöhnliche Lorentzfaktor zwischen zwei
   Profilen gleicher Feldskala mit Gegenfluss.

## Nachrechnung (`llm/k219_nachrechnung_codex_op5.py`, Ausgabe `llm/k219_out.txt`)

31 Prüfungen, alle bestätigt: Zustandsfamilie und Port (A1–A5), Energiegewichte (B1–B3), Sättigung und Spinmengen
(γ{½} = ln2/(π√3) = 0,127384, γ{½,1} = 0,201784; C1–C4), r31-Stationarität und Ausflussanteil (D1–D3), Scherung (E1–E3),
r27-Register und Portkollision (F1–F5), s-Schalen und Kompensatorbild (G1–G4), doppelte Rapidität (H1–H4). Die Kommutation
C_ch mit z ↦ iz ist in `formal/QSFormal/Sektoren.lean` (`R_iL`, `R_P4`, r51) schon formalisiert und wurde nicht neu gerechnet.

## Abgleich mit r05–r10

| Lokale Runde | Codex-Befund | Verhältnis |
|---|---|---|
| r05.3(i) OP5-Kern „lokal geschlossen“ | Schema bedingt richtig, keine native Instanz | **Präzisierung:** geschlossen als Schema unter seinen Annahmen; native Route offen |
| r05.3(ii) Λ-Auslesung als Kaskaden-Verzweigung; r05-Fundstellen „r31: Verhältnis aus Dynamik“ | r31 setzt β² ein, stabilisiert nur | **Präzisierung** der Fundstellennotiz; deckt sich mit r08 (K1 = Annahme) |
| r08 Annahmenliste, H15/H46/H96 am γ_L-Kern | gleiche Kette, zusätzlich vier Nenner und q ≠ λ₋ | bestätigt, ergänzt |
| r09 H98, Prinzip P | Sättigung wählt j nicht; endliche Spinmengen geben verschiedene γ | in r10.4 schon aufgenommen; H98 bleibt (sein Regelraum ist genau diese Freiheit) |
| r10.2/r10.3 | Projektorbrücke: Tachyon-Abbildung erhält die inneren Sektoren | bestätigt r10.3 von der inneren Seite |
| r22/r24 Konvention F, R ≠ P | s-Schalen, Kompensatorbild nicht null | bestätigt (r03.2, r22, r24) |
| r07.2 | QAM-Regel „deklarierte Map + Zielformel“ | r07.2 ist eine solche Konversion; bestätigt |
| r10.3 offener Grund (Boost-Teil) | γ_L = Lorentzfaktor zwischen Gegenfluss-Profilen | **Lesart-Kandidat**, nachträglich, keine Herleitung |

Kein Widerspruch gefunden. Keine neue H-Nummer; Guards unverändert.

## Offen (für den Autor)

- Auf GitHub ist `llm/Uebergabe.md` jetzt die Codex-Übergabe; lokal ist es die Claude-Übergabe. Eine gemeinsame Datei wäre sauberer.
- Codex schlägt als nächsten Prüfgegenstand die Bedeutung von „ein Objekt“ vor (vor jedem weiteren Spin-/Zählzweig).
