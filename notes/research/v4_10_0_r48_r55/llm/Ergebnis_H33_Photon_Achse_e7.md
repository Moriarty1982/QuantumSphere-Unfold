# Ergebnis H33: e₇ ist die Achse von B − L, nicht die des Photons

Vorab-Notiz: `Vorab_Notiz_H33_Photon_Achse_e7.md`, Commit ec06de3 (2026-10-24 03:30 MESZ), vor der Rechnung. Vorab offengelegt: Operatoren aus
L_{e₇}, R_{e₇} sind auf einem schwachen Dublett konstant; die Rechnung ist eine Prüfung, keine Vorhersage. Skript `k89_test_h33.py`, Ausgabe `k89_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H33a Singulett-Ebene | **bestätigt** | span_ℂ(1, e₇) ist genau die Summe der Sektoren Q = 0 und Q = 1; auf ihr ist L_{e₇} = R_{e₇} |
| H33b Ladung der Achse | **bestätigt** | Auf allen 16 Zuständen einer Generation: 2(Q − ½) = B − L, Y/2 = (B − L)/2 + T₃^R, Q_em = T₃^L + T₃^R + (B − L)/2 |
| H33c Photon braucht ℍ | **bestätigt** | Keine Kombination a + b·iL + c·iR + d·iL·iR gibt Q_em; die beste weicht um ½ ab, genau um die T₃-Aufspaltung im Dublett |

## Einordnung

1. **Deutung 3 ist in der gestellten Form widerlegt.** Die Achse e₇ trägt die Ladung B − L (und mit iL_{e₇} die Chiralität), nicht die
   elektrische Ladung. Das Photon braucht zusätzlich T₃ aus dem ℍ-Faktor: Es ist die Mischung der e₇-Achse mit der schwachen Isospin-Richtung.
   Farbe sind weiterhin die Drehungen, die e₇ festhalten, und sie vertauschen mit B − L.
2. **Die Struktur ist links-rechts-symmetrisch.** Q_em = T₃^L + T₃^R + (B − L)/2 ist die Ladungsformel der Pati-Salam- bzw.
   links-rechts-symmetrischen Modelle: die e₇-Achse ist das U(1)_{B−L}, T₃^R kommt von den rechtshändigen (im T-Frame gelesenen) Partnern.
   Die Hyperladung ist erst die Kombination Y/2 = T₃^R + (B − L)/2.
3. **Doppelbelegung im Companion.** span(1, e₇) ist dort zugleich Photon-Kern K₃ (Bild des Kompensators, Zeile 9287), Träger von ν_R
   (Zeile 6862) und Ebene des symmetrischen Generationen-Punkts ω (v4.8.0-r15.2). Im äußeren Frame trägt diese Ebene die Lepton-Singuletts
   Q = 0 und Q = 1. Der Photon-Kern als Zustand und das Photon als Generator sind verschiedene Dinge; die Zuordnung „Photon = Singulett ℂ“
   ist eine Doppelbelegung derselben Art wie Farbe/Generation (r36). Kandidat für einen Statusvermerk.
4. **Was bleibt:** e₇ kann Bezugsachse der Frames sein (Photon-Frame als neutrale Achse, r01); das ist hier nicht geprüft. Die U(1)-Faser
   der Hopf-Abbildung S³ → S² (thm:hopf) ist auf der Singulett-Ebene die Phase e^{θ e₇}, also in der Aufteilung D das U(1)_{B−L}.
