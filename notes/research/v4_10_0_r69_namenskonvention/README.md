# v4.10.0-r69: Namenskonvention für die Frames und die Lepton-Sektoren

**Stand:** 26.11.2026. Konvention nach Entscheidung des Autors vom 26.11.2026 („Beides wie vorgeschlagen“). Keine Rechnung, kein Test,
kein Status geändert, kein Guard berührt. Die Buchstaben M, T, P, R und alle bisherigen Namen bleiben gültig; ältere Runden werden nicht
umgeschrieben.

| Stück | Inhalt |
|---|---|
| Konvention r69.1 | Frames: R **Ruheframe** (rest frame; bisher Referenz- bzw. Bezugsframe), M **Materie-Frame** (unverändert), T **Dual-Frame** (dual frame; bisher Tachyon-Frame), P **Lichtpunkt** (light point; bisher Photon-Eigenframe). „Licht-Frame“ wird für R nicht benutzt, lichtartig ist P. |
| Konvention r69.2 | Lepton-Sektoren: **Re-Sektor** (neutrale Leptonen, c = 0) und **Im-Sektor** (geladene Leptonen, c = 1) nach H170, nur für Leptonen, Lesart unter H99. Quarks behalten Up- und Down-Sektor (H172). Die zwei Ausgänge des Kompensators heißen Ports. |
| Bemerkung r69.3 | „Bosonisch/fermionisch“ wird nicht als Name benutzt: Die Frames sind Zustände eines Spin-1-Felddubletts und keine Teilchensorten; die Statistik je Frame ist eine nicht begründbare Setzung (r17, r24); T11 benutzt die Wörter für die Ports; beide Lepton-Sektoren sind Fermionen. |
| Bemerkung r69.4 | Lesart: Ein Frame ist die Verteilung desselben Zustands auf die zwei Ports des Kompensators (R 1 : 0, M 1 : x, T x : 1, P 1 : 1, x = β_sym² = 0,301847; M hat 76,8 % im Kompensatorport). Im Bild von k292/k297 Ellipsen mit Achsenverhältnis γ_L und getauschtem Drehsinn; R als Kreis und P als Grenzfall sind aus der Parametrisierung gelesen, nicht eigens gerechnet. |

## Werkzeuge und Grenzen
Keine Rechnung, deshalb weder Wolfram Language noch Qiskit noch HDL-Vergleich. Die Zahlen 0,301847, 76,8 % und γ_L = 1,8647 sind die
Werte aus r67 (nachgerechnet: 1/(1 + x) = 0,768140, (1 + x)/(1 − x) = 1,864700). Die Lesarten zu H168 bis H170 stehen bisher nur in den
Notizen unter `notes/research/hilbert_shift_felder_2026_11_24/`, nicht in einer Runde. OP1 bis OP5 offen.

## Dateien
- `rounds/v4100_r69_round.tex`: Rundentext, wörtlich angehängt an `sources/research/parts/v4100-post-release-layers.tex`.

Hinweis: Der Ordner `notes/research/v4_10_0_r69/` gehört zur alten Schicht v4.9.0-r69 und hat mit dieser Runde nichts zu tun.
