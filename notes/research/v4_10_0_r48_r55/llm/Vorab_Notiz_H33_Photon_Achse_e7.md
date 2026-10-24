# Vorab-Notiz H33: Ist e₇ die Photon-Achse?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „3. könntest du aber evtl. prüfen vorher“. Geprüft wird die Deutung 3 aus der Besprechung
nach r48: „Die Ladung ist die Kopplung an die Achse e₇; Farbe sind die Drehungen um sie; die Achse ist die Photon-Achse des Companion.“
Bezug: r34/r35 (Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}), r41/r42 (Aufteilung D, Q_em = T₃ + Y/2, Inhalt einer Generation), r48 (Sektoren aus O.mul).

## Textbefund (vor der Rechnung gelesen)

Der Companion setzt span(1, e₇) an drei Stellen ein: als Photon-Kern K₃ (Bild des Kompensators C, „singlet ℂ ⊂ 𝕆, photon kernel K₃ sector“,
Zeile 9287), als Träger von ν_R (Tabelle Zeile 6862, „Singlet e₇ … ν_R“) und als Ebene des symmetrischen Generationen-Punkts ω („the complex
plane at the end of the cascade“, v4.8.0-r15.2). Die Kaskade endet im Photon-Stratum S² (thm:hopf, thm:dark-energy).

## Offenlegung (vorab analytisch gesehen)

Operatoren, die nur aus L_{e₇}, R_{e₇} gebaut sind, wirken nur auf den 𝕆-Faktor und sind daher auf beiden Komponenten eines schwachen Dubletts
gleich. Vorab erwartet: 2(Q − ½) ist B − L; Q_em braucht den ℍ-Faktor. Die Rechnung ist daher eine Prüfung, keine Vorhersage.

## Hypothesen

- **H33a (Singulett-Ebene):** span_ℂ(1, e₇) ist genau die Summe der Sektoren (ℓ, r) = (1, 1) und (−1, −1), also Q = 0 und Q = 1. Auf ihr ist
  L_{e₇} = R_{e₇}.
- **H33b (Ladung der Achse):** Auf den 16 Zuständen einer Generation (Inhalt r42.1(b)) ist 2(Q − ½) = B − L, und Y/2 = (B − L)/2 + T₃^R mit
  T₃^R = (1 − C)T₃, also Q_em = T₃^L + T₃^R + (B − L)/2.
- **H33c (Photon braucht ℍ):** Kein Operator aus der von 1, iL_{e₇}, iR_{e₇} erzeugten Algebra wirkt auf der Generation als Q_em.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H33a–c bestätigt ⇒ Deutung 3 ist in der gestellten Form **widerlegt**: e₇ ist die Achse von B − L (und der Chiralität), nicht die des
  Photons. Das Photon ist erst die Mischung der e₇-Achse mit T₃ aus ℍ. Der Photon-Kern K₃ des Companion und ν_R liegen auf derselben Ebene
  span(1, e₇) (Doppelbelegung, wie Farbe/Generation in r36).
- H33c widerlegt ⇒ Deutung 3 bleibt möglich und wird weiter geprüft.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
