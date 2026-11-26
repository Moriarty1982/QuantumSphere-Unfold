# v4.10.0-r70: Portgewichte gegen Amplituden, der HC auf der Zustandskugel, Berichtigung zu r69.4

**Stand:** 26.11.2026. Auftrag des Autors vom 26.11.2026 („ja, korrigiere das“). **Erkundung, nicht blind:** Jede Aussage ist eine Identität
oder eine Nachrechnung; kein Test mit Kriterium, keine H-Nummer. Vergeben: Runde **r70**, Skripte **k381, k381b**. Kein Guard berührt,
kein Status eines offenen Problems geändert. Ältere Runden und Notizen sind nicht umgeschrieben.

| Stück | Inhalt |
|---|---|
| r70.1 | b_S² + b_C² + b_3² = 1 mit b_S = (\|E\|² − \|B\|²)/(2u), b_C = E·B/u, b_3 = \|E×B\|/u. Schub η quer zum Feld: b_C = sech 2η, b_3 = tanh 2η. Frames: R (1; 0), M (1/γ_L; tanh 2ε), P (0; 1), T (−1/γ_L; tanh 2ε). D und ϑ tauschen M und T, J_B lässt alle fest. |
| r70.2 | Der HC ist die Messung entlang b_C: p₊ = (1 + b_C)/2 = \|E + B\|²/(4u); das behaltene Stück liegt am Pol R, der Partner am Gegenpol; nicht selektiv bleibt der Schatten auf der Achse. Zwei Wege von R auf die Höhe von M (Schub; Dualitätsdrehung α mit HC, r27). |
| r70.3 | Zwei Rollen von x = β_sym²: als Gewichtsverhältnis (Konvention F) b/a = β_sym, Achsen e^{2ε} = 3,4386, Winkel 57,57°; als Amplitudenverhältnis (k292, k297) Gewichte 1 : x² = 91,65 : 8,35, Achsen γ_L, Winkel 33,59°, das ist ein Schub mit Geschwindigkeit β_sym². |
| r70.4 | Berichtigung: in r69.4 bleibt die Angabe der Portgewichte; die Ellipse mit b/a = x beschreibt nicht den Materie-Frame. Statusvermerk an `thm:hc-quasiconformal` (und `thm:tribonacci-beltrami`). Der Tausch a ↔ b aus k297/k350 ist, mit den Kreisanteilen als Ports gelesen, D oder ϑ und nicht die Involution des HC; Typisierung offen. |
| r70.5 | Nachrechnung k381 von neun Skripten mit b/a = β_sym: kein Urteil kippt (H132, H133, H136, H159). Der Winkel aus k292 wird 57,57° (Lage von M, = 2α aus r66). Der Zahlentreffer κ = (γ_L + 1/γ_L)/2 aus k303 gibt es nur für b/a = x; mit b/a = β_sym ist 1/cos 2θ = γ_L. |

## Vorwissen geprüft
v4.9.0-r04.1 bis r04.3 (Dublett, Scheibe, HC als Messung entlang σ_x), r17, r22 (Konvention F), r24.3 (\|b\| = sech 2η), r27 (HC-Achse, nicht
selektiver Schritt, Kickwinkel), r28 (Tachyon-Abbildung z ↦ iz tauscht die Ports), v4.10.0-r23.2 (Bild des HC ist R), r66/H164 (Boost führt R
auf die Besetzungen von M, Winkel 2α), r69.4; `thm:hc-quasiconformal`, `thm:tribonacci-beltrami`; Notizen k253, k292, k297 bis k305, k350.
Eine Halbkugel mit b_3 = \|E×B\|/u habe ich im Bestand nicht gefunden; r04.2 hat die Identität u² − det G = ¼\|s\|², aus der sie folgt.

## Werkzeuge und Prüfungen
- Python mit sympy (exakt): Identitäten in `../frames_kugelbild_2026_11_26/frames_kugelbild.py` (Ausgabe `kontrolle_out.txt` dort).
- `k381_nachrechnung.py`: lässt die neun Skripte unverändert und mit b/a = β_sym laufen (die Zeile, die μ setzt, wird nur im Speicher ersetzt)
  und gibt die geänderten Zeilen aus: `k381_out.txt`.
- Wolfram Language unabhängig: `k381b_gegenprobe.wl`, Ausgabe `k381b_out.txt` (W1 bis W12, alle Reste 0, keine Warnungen).
- Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf).
- **Nicht neu gerechnet:** die Wolfram-Gegenproben der neun Skripte selbst (k292b usw.).
- `tools/qs.py guards` auf der Schichtdatei: 0 Kandidaten.

## Grenzen
β_sym ist eingesetzt (Bezugswert aus r67), OP1 bis OP5 offen. Die Lesart „Kreisanteile = Ports“ stammt aus k253 und ist nicht hergeleitet.
Offen bleiben: welche Achse der Scheibe die Frames trägt (HC-Achse b_C oder Sektorachse b_S), der Typ des Tauschs a ↔ b, und ob der
Zahlentreffer aus k303 Zufall ist.

## Dateien
- `rounds/v4100_r70_round.tex`: Rundentext, wörtlich angehängt an `sources/research/parts/v4100-post-release-layers.tex`.
- `k381_nachrechnung.py`, `k381_out.txt`, `k381b_gegenprobe.wl`, `k381b_out.txt`.
- Zeichnung: `notes/research/frames_kugelbild_2026_11_26/`.

Hinweis: Der Ordner `notes/research/v4_10_0_r70/` gehört zur alten Schicht v4.9.0-r70 und hat mit dieser Runde nichts zu tun.
