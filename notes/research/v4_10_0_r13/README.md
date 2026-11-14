# v4.10.0-r13: Statusvermerke zum neutralen Qubit und zur zweiten Familienstruktur

14. November 2026. Autorenauftrag: „Statusvermerk-Runde r13“. Runde als Datei `rounds/v4100_r13_round.tex`, angehängt
an `sources/research/parts/v4100-post-release-layers.tex`. Kein neuer Test, keine neue H-Nummer; Guards unverändert.
Außer H103 sind alle Einträge Erkundungen ohne Vorab-Notiz und ohne Datenvergleich.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r13.1 | Berichtigung zu r12.4(c): Unter der angenommenen Ladungsachse e₈ gibt es das neutrale Qubit N = ker Q_*; Annahme als Platzhalter CT-003 (drei Register-Guards); H103a widerlegt | `op3_sedenion_charge_2026_11_13.md`, `predictions/Ergebnis_H103_Bezug_im_neutralen_Qubit.md`, `counterterms/Bilanz_2026_11_14.md` |
| r13.2 | Hurwitz-Einheiten von H_n wirken auf N als 2T; Bezug = Eigenzustand einer Einheit der Ordnung 3 (K = 2/3, π/4), Konstruktion mit bekanntem Ziel | `op3_hurwitz_2t_neutral_qubit_2026_11_14.md`, `op3_rf_reference_2026_11_14.*` |
| r13.3 | C⊗S trägt unter Q_* zwei Generationen; ψ ist eine Phase darin, kein Generationsschritt | `op3_sedenion_generations_estar_2026_11_14.md` |
| r13.4 | Rechtswirkung von H_n vertauscht mit Farbe und Ladung; su(2) für Leptonen ⊕ su(2) für Quarks; jede Teilchenart ein Dublett | `op3_family_su2_right_action_2026_11_14.md` |
| r13.5 | Majorana-Vektor auf N nicht festgelegt; keine drei Massen; Paarkanal r82.4 seit v4.10.0-r01.3(d) abstoßend | `op3_majorana_vector_n_2026_11_14.md` |
| r13.6 | S ⊕ O gegen O³; e₈-Ladung nicht τ-symmetrisch; Weg B mit τ-symmetrischem 2 + 1, aber nur S₃; keine Achse unter dem magischen Winkel; Profil mit dem Bestand nicht erfüllbar | `op3_third_generation_singlet_2026_11_14.md`, `op3_tau_doublet_axis_2026_11_14.md` |

## Berichtigung einer Vornotiz
`op3_neutral_su2_octant_2026_11_13.md`, Feldsuche Punkt 2, nennt die Torsionswechselwirkung im Paarkanal ν^c ν^c
anziehend. Seit v4.10.0-r01.3(d) ist der Kanal abstoßend und bildet kein Kondensat. Die Notiz bleibt unverändert
(append-only); die Berichtigung steht in r13.5.

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 1626`):
  0 Kandidaten in den Zeilen 1626–1785.
- Kandidaten-Build lokal (`.github/scripts/qsc_latex_build.py --source-dir sources/research`, MiKTeX): Status ok,
  1409 Seiten, 0 fatale Fehler, 0 Overfull. `qs.py audit`: undefinierte Verweise 0, undefinierte Zitate 0,
  doppelte Labels 0, Rerun 0; 4166 Labels.
- Die lokale Monolith-Fassung und das Bündel aus der Anleitung entfallen wie bei r12: Der lokale Ordner ist ein Klon
  des Repos.
