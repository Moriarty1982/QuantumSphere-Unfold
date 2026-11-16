# v4.10.0-r28: Stand der Restbiegung und der Zählregel nach den Erkundungen vom 16./17.11.

17. November 2026. Auftrag des Autors: „neue Version für Zenodo anlegen“, mit der Entscheidung, die Arbeit seit r27 als Runde r28 in die
Vollausgabe zu bringen. Die Runde fasst die Tests H106–H111 und die Erkundungen zu OP3 und OP1 zusammen, die bisher nur in Notizen standen. Sie
steht als Datei `rounds/v4100_r28_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Keine neue Rechnung,
keine H-Nummer, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r28.1 | H106–H111 widerlegt (Singulett, verschachtelte Normierung, verschränkte Generationen, Frames je Generation, Betrachter-Hälfte, Zeitoktant; H111 mit nachträglich erkanntem Rangfehler); laufende Massen 3δ = 0,663370; C⊗H⊗O⊗S ist HS(10) | `predictions/`, `op3_renormalisation_*`, `op3_dixon_times_sedenions_*` |
| r28.2 | Diagnose: Phase im Träger starr; Berichtigung (bewachter Kern, H102 übersehen); kein natives κ; Kette endet bei der Zählregel von M | `op3_chain_diagnosis_*`, `op3_native_kappa_*`, `op3_frame_*` |
| r28.3 | H102: Messdaten korrekt, +2,3σ; hängt an U(1)-Zählung (SU(2) → 1868 MeV) und Spektrum √(j(j+1)) (j: 0,3497; j+½: 0,2206) | `op1_counting_rule_data_*`, `op1_r_readout_precheck_*` |
| r28.4 | U(1)-Achse nativ (Dualität, Helizitätsachse, Ports); (A) setzt zwei SU(2) gleich; (S1′) gibt Gewicht 2, bricht (A) in der r24-Form; Literatur ABK/Mitra/Bianchi | `op1_u1_check_*`, `op1_s1_check_*` |
| r28.5 | Korrekturterm: auf S keine Dynamik sichtbar; zeitabhängige Verbindung leert einen Saum (Ausschluss); undurchlässiger Rand mit Punktierung hinreichend, nicht begründet | `op3_correction_term_*` |
| r28.6 | Topologie: ein Kern = Kernpaar ±z_c in ℝP²; Borsuk–Ulam; γ_M/2 topologisch nicht erreichbar; mehrere Umkehrwalzen; Raster D3 gegen D4 | `op3_topology_core_*` |
| r28.7 | Zählung je Frame: verwischte Auslesung, HC je Frame (T ⊆ M ⊆ P), Lage von P in Rapidität, Register-Entropie (P und R folgen, M nicht) | `op1_hc_blur_*`, `op1_entropy_count_*` |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3798`): 0 Kandidaten in den Zeilen 3798–3980.
- Kandidaten-Build: siehe PR.

OP1–OP5, C5, C6/T2 offen.
