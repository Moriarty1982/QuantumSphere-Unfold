# Erkundung: vier Bedingungen und Cartan-Test hochgenau (3. Nov. 2026)

**Status: Erkundung, nicht vorregistriert, nicht blind.** Die Hypothese (H58: g''_p = 477, 594, 723, 865; involutiv erst bei p = 8) war vor dem Lauf bekannt. Es gibt keine Vorab-Notiz für diesen Lauf. Das Ergebnis bestätigt H58 nur als Erkundung und ersetzt keinen vorregistrierten Test.

## Daten
- Linearisierung: `k153b_hp_linear.py` (mpmath, dps 160, HJ = 1e-55, HX = 1e-25) → `hp_work2/AB_taylor2.pkl`. Gegenüber den alten hp-Daten weicht Grad 1 um 2e-21 ab, Grad 2 um 2e-19; die alten Daten waren die Genauigkeitsgrenze.
- Werkzeuge: `k154_hp_tools.py` (arb über python-flint; Umwandlung mit `nstr(v,120)`).

## Die vier Bedingungen (k157, QS_DPS=70)
- c8 eliminiert: Rang 3171, linker Kern 834, Residuum 1e-66.
- c7 eliminiert: Rang 2274, linker Kern 1368, Residuum 9e-52.
- Gram-Matrix der Bedingungen auf dem 6-Jet-Kern N6 (501): 24 Eigenwerte ≥ 5.1e-13, dann 1.9e-71 (Lücke 1e58).
- Damit ist die 6-Jet-Faser exakt 477 = 501 − 24: das sind 20 Ω-Prolongationen plus genau 4 Bedingungen. Eine fünfte Bedingung gibt es nicht.

## Cartan-Test des erweiterten Symbols (k158)
- ker C hochgenau: 477, Residuum 6e-45.
- Die Prolongation wird in double gerechnet (SVD ohne volle U): g''_7 = 594 (Verh. 8e12), g''_8 = 723 (9e8), g''_9 = 865 (2e9).
- Die Charaktere sind in allen drei Rahmen (seeds 1–3) gleich:
  - p = 6: [477,107,12,0], Summe 596 > 594, also nicht involutiv;
  - p = 7: [594,118,12,0], Summe 724 > 723, also nicht involutiv;
  - p = 8: [723,130,12,0], Summe 865 = 865, also **involutiv**.
- Lücken ≥ 1e8.

## Lesart
- Die vier versteckten Bedingungen sind exakt, und es sind genau vier.
- g''_8 = 723; der Wert 724 war ein Artefakt (H57).
- Das erweiterte Symbol ist erst bei p = 8 involutiv, mit 12 Funktionen von drei Variablen.
- Offen bleibt, ob 7- und 8-Jets weitere versteckte Bedingungen haben. Spencer lässt dort höchstens 4 bzw. 3 zu. Für die Entscheidung braucht es A und B vom Grad 3 hochgenau und größere Eliminationen.
