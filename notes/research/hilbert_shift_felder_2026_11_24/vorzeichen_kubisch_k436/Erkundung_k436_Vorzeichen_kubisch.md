# Erkundung k436: Das Vorzeichen des Zweigwahl-Terms folgt weder aus J noch aus Stabilität

**Datum:** 2026-11-28. **Erkundung, nicht blind** (keine Vorab-Notiz): Die Antworten auf 1 und 2 stehen vorab aus den J-Regeln von H158c bzw. aus der Spiegelung
φ → −φ fest; 3 ist eine direkte Folge aus H222. **Werkzeuge:** Python/sympy (`k436_vorzeichen.py` → `k436_out.txt`), Wolfram unabhängig (`k436b_gegenprobe.wl` →
`k436b_out.txt`); alle Zahlen stimmen überein. Anlass: nach H222 (Zweig = Vorzeichen der kubischen Invariante) die Frage, ob das Vorzeichen aus der Feldgleichung folgt.

## Befunde
1. **Das Quadrat der kubischen Norm ist unter J nicht erlaubt.** N² = φ⁶ − 6φ⁴r² + 9φ²r⁴ + 2r⁶ + 4φr³(φ² − 3r²) cos 3δ + 2r⁶ cos 6δ (beide Werkzeuge).
   Die Teile φr⁵ cos 3δ und r⁶ cos 6δ haben keinen J-Partner (Regel aus H158c). Die Lesart „Potential nur aus N, Stabilität verlangt +N²“, die das richtige
   Vorzeichen gäbe (H222: kleineres |det| = größeres cos 3δ), ist mit dem Postulat J unverträglich. Unter J bleibt bei Ordnung 6 nur β₃ φ³r³ cos 3δ, daneben c₄ φ³r³ cos δ.
2. **Stabilität legt das Vorzeichen nicht fest.** Für die ganze J-erlaubte Ordnung 6 gilt exakt F₆(φ; −c₄, −β₃) = F₆(−φ; c₄, β₃). Da der Feldraum φ < 0 enthält,
   ist das Potential für (β₃, c₄) genau dann beschränkt, wenn es für (−β₃, −c₄) beschränkt ist (Stichproben: min F₆ jeweils gleich). Physikalisch ist das Vorzeichen
   trotzdem nicht leer: Bei festem Vorzeichen von φ sind die beiden Zweige verschiedene Spektren (H167b).
3. **Mit beiden J-erlaubten Termen wird die Regel ein Keil.** V(Daten) − V(andere) = 2β₃ sin(3p + π/4) − 2c₄ cos(p + π/4) (Im-Sektor) und 2β₃ sin 3p − 2c₄ sin p
   (Re-Sektor). Beide Sektoren wählen den Daten-Zweig für β₃/c₄ unterhalb 0,334 (Re-Grenze, bei c₄ > 0) bzw. 0,863 (Im-Grenze, bei c₄ < 0): ein Keil mit 43,8 % aller
   Richtungen in der (β₃, c₄)-Ebene. Nur cos 3δ verlangt β₃ < 0 (H222); nur cos δ verlangt c₄ > 0, auch das wählt in beiden Sektoren richtig.

## Lesart
Das offene Vorzeichen aus H222 ist eine echte Setzung des Potentials: Weder das Postulat J noch die Beschränktheit legen es fest, und die einzige Form, die es über
Stabilität festlegen würde (N²), verbietet J. Nach der Regel des Autors soll ein solches Vorzeichen aus der finalen Feldgleichung folgen; die ist hier nicht vorhanden.
Was das Vorzeichen festlegen könnte, ohne dass es hier gerechnet ist: ein gemeinsamer Elternterm, der β₃ (bzw. c₄) an das Vorzeichen des Spin-1-Terms α′ bindet;
oder eine Lesart, in der die Wurzelmatrix im Im-Sektor positiv sein muss (dann β₃ < 0 im Im-Sektor, und die Universalität aus H221 trägt es in den Re-Sektor, wo es
den 51σ-Test aus H222 besteht). Beides ist eine Setzung, keine Herleitung.

## Grenzen
Zirkulantensektor, Baumniveau, J in der Ebenen-Lesart (H157/H158). Ordnung 6 vollständig im J-erlaubten Raum (H158c: φ⁶ + r⁶, φ²r⁴ + φ⁴r², dieselben mit cos 2δ,
φ³r³ cos δ, φ³r³ cos 3δ). Höhere Ordnungen nicht betrachtet. Kein Guard berührt; OP3/OP4 offen.

Vergeben: k436 (Erkundung, keine H-Nummer). Nächste frei: H223, k437.
