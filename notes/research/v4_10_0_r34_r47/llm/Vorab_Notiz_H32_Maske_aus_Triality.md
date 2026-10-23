# Vorab-Notiz H32: Liefert die Abweichung der triality-kovarianten Chiralität eine Generationen-Maske?

Festgelegt am 2026-10-23, **vor** der Rechnung. Autor: „versuche es mal“. Bezug: r45 (Modell I: Chiralität iL_{e₇} auf allen Plätzen;
Modell II: triality-kovariant i(L_{e₇}, R_{e₇}, −L_{e₇} − R_{e₇}), als exakte Symmetrie unmöglich), r46 (Mischung erst durch generationen-selektive
Masken, linear im Gewicht), r43 (iL_{e₇} = +1 auf den Q-Sektoren {0, 2/3}, iR_{e₇} = +1 auf {0, 1/3}), r41 (Frame T = Ladungskonjugation).

## Modellannahme (offen gelegt, nicht hergeleitet)

Die exakte Chiralität ist die von Modell I. Die Abweichung Δ := J_II − J_I, also auf Platz i: Δ_i = i(B_i − L_{e₇}) mit B = (L_{e₇}, R_{e₇},
−L_{e₇} − R_{e₇}), wirkt als **schwache Störung** der Kopplungen mit kleinem Gewicht ε. Der rechtshändige Partner eines Teilchens wird im
T-Frame gelesen (r41: T = Ladungskonjugation). Eine Massenkopplung M auf den Plätzen wird dann zu M + ε(W M + M W) mit W = diag der
Platz-Gewichte des Sektors.

## Offenlegung (vorab aus der Sektortabelle von r43 abgeleitet)

Auf einem Q-Sektor sind iL_{e₇}, iR_{e₇} Zahlen ±1, also ist Δ_i dort eine Zahl. Vorab erwartet: Sektor 0 (0, 0, −3), 2/3 (0, −2, −1), 1/3 (0, 2, 1),
1 (0, 0, 3). Ebenso vorab: T Δ T⁻¹ = −Δ. Nicht vorab gerechnet: die Mischungs-Prüfung (H32c) und das Verhältnis der Fourier-Kopplungen (H32d).

## Hypothesen

- **H32a (Gewichte):** Δ_i ist auf jedem Q-Sektor skalar, mit den Platz-Gewichten der Offenlegung.
- **H32b (Frame):** T Δ T⁻¹ = −Δ; die Gewichte sind antisymmetrisch unter q ↔ 1 − q. Damit trägt der im T-Frame gelesene rechtshändige
  Partner dieselben Gewichte wie das linkshändige Teilchen: Quarks (up wie down) W_q = diag(0, −2, −1), Leptonen W_l = diag(0, 0, −3).
- **H32c (Mischung):** W_q und W_l vertauschen nicht mit τ. Mit ℤ₃-zirkulanten, hermiteschen M_u, M_d und derselben Maske W_q ist die Mischung
  für ε > 0 von null verschieden und linear in ε (200 Zufallsfälle, wie r46).
- **H32d (Form in der Generationen-Basis):** In der Fourier-Basis der Generationen (Eigenbasis von τ) sind die Nebendiagonal-Einträge von W_q
  alle gleich groß, |·| = 1/√3, die von W_l alle gleich 1. Das Verhältnis Lepton zu Quark ist √3.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H32a–d bestätigt ⇒ Unter der Modellannahme kommt die Generationen-Maske aus der Struktur: aus der Triality-Kovarianz, die als exakte
  Symmetrie verboten, als schwache Störung aber möglich ist. Ihre **Form** ist dann festgelegt, gewählt ist nur das Gewicht ε. In der
  Generationen-Basis ist sie „demokratisch“ (gleiche Kopplung aller Paare), für Leptonen um √3 stärker als für Quarks.
- Die Modellannahme selbst (die Abweichung als Störung) ist **nicht** hergeleitet. Zahlenwerte für Mischungswinkel folgen nicht, solange die
  Zirkulanten-Parameter und ε offen sind.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
