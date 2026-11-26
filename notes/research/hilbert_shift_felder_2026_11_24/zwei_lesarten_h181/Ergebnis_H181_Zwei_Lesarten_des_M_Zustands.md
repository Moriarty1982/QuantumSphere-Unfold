# Ergebnis H181: Der Zustand mit b/a = β_sym² trägt die übrigen Ablesungen nicht (Test k383, 26.11.2026)

**Urteil nach den vorab festgelegten Kriterien:** H181 ist **widerlegt**. Lesart A (b/a = β_sym²) verfehlt im gemeinsamen Wörterbuch D alle vier
Stellen Q1 bis Q4; Lesart W (b/a = β_sym, r70) trägt alle vier und verfehlt Q5 (m_h).
Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H181_Zwei_Lesarten_des_M_Zustands.md` (Commit 84d53c8, vor dem ersten Skriptlauf).
**Teil 1 nicht blind** (geschlossene Formeln, Ausgang erwartet und so eingetreten). **Blind war nur Teil 2** (Maskenscan).
Anlass: Autor, 26.11.2026, 21:52 UTC: „kannst du beides mal nachrechnen“.

Werkzeuge: Python mit mpmath (30 Stellen) und der unveränderte Maskencode k105 (numpy); Wolfram Language unabhängig (`k383b_gegenprobe.wl`,
symbolische Reste W1 bis W3 exakt 0, Zahlen stimmen überein). Qiskit nicht eingesetzt (keine Schaltung). Kein RUN_TAPE betroffen.

## Teil 1: ein Wörterbuch, zwei Zustände
Wörterbuch D: cot θ_W = cosh 2η, Ω_M = tanh² η, sin²θ₁₂ = tanh² η/(1 − s₁₃), Maske ε = η, κ = cosh 2η; η_W = 0,617530, η_A = 0,311550.

| Größe | W (b/a = β_sym) | A (b/a = β_sym²) | Messung |
|---|---|---|---|
| Q1 m_W | 80,3611 GeV, z = −0,17, trägt | 70,064 GeV, z = −1302, widerlegt | 80,3625 ± 0,0077 GeV |
| Q2 Ω_M | 0,30185, z = +0,51 (DESI), −1,88 (Planck), trägt | 0,09111, z = −24,0 / −32,0, widerlegt | 0,2975 ± 0,0086; 0,315 ± 0,007 |
| Q3 sin²θ₁₂ | 0,30868, z = +0,79, trägt | 0,09318, z = −32,9, widerlegt | 0,3036 ± 0,0064 |
| Q4 Maske | ε = 0,6175, im Fenster; Scan 168 / 1552 Treffer | ε = 0,3116, außerhalb; Scan **0 Treffer** | Fenster 0,611 bis 0,647 |
| Q5 m_h | κ = 1,8647, 201,4 GeV (+60,9 %), widerlegt | κ = 1,2005, 124,8 GeV (−0,3 %), trägt (kein Beleg) | 125,20 GeV |

Der Zustand, an dem der κ-Treffer hängt, ist nicht der Zustand, an dem m_W, Ω_M und die Mischung hängen.

## Teil 1b (Erkundung, nachträglich zu lesen)
1. **Der κ-Treffer trennt die Lesarten nicht.** Aus derselben festen Liste von 20 einfachen Funktionen liegen im 5-%-Fenster um κ* = 1,2039:
   für W zwei (cosh η = 1,19681, −0,59 %, 124,4 GeV; coth 2η = 1,18478, −1,59 %, 122,9 GeV), für A einer (cosh 2η = 1,20049, −0,28 %, 124,8 GeV).
   cosh η_W ist der Lorentz-Faktor zur Geschwindigkeit β_sym. Eine Zahl nahe 1,2 ist in beiden Lesarten zu haben; das stützt die Einordnung
   aus k303 und r64.4 (Zufallsniveau).
2. **Zweites Wörterbuch D′ für A:** cot θ_W = e^{2η_A} (Achsenverhältnis), Ω_M = tanh η_A (Amplituden- statt Gewichtsverhältnis), ε = 2η_A, κ = cosh 2η_A.
   Wegen e^{2η_A} = γ_L und tanh η_A = β_sym² (exakt) kommen Q1 bis Q3 identisch zu W heraus, und Q5 trägt. Der Preis: Die Portgewichte wären
   0,9165 : 0,0835, Konvention F verlangt 0,7681 : 0,2319 (x als Gewichtsverhältnis, v4.9.0-r22 bis r24). D′ ist also keine zweite Lesart von
   Konvention F, sondern ein anderer Zustand mit umbenannten Ablesungen.
3. **Müsste Konvention F zwei M-Zustände unterscheiden?** Nur wenn man den κ-Treffer als Befund behalten will. Dann gäbe es den Frame-Zustand M
   (η_W, Gewichte 76,8 : 23,2) und einen HC-Zustand (η_A, Gewichte 91,65 : 8,35), verbunden durch cosh 2η_W = e^{2η_A} = γ_L. Eine Regel, die diesen
   zweiten Zustand verlangt, gibt es im Bestand nicht; sie wäre eine neue Setzung.

## Teil 2 (blind): Maskenscan
| ε | Variante A | Variante B | sin²θ₂₃ | \|sin δ\| |
|---|---|---|---|---|
| η_A = 0,3116 | 0 Treffer | 0 Treffer | | |
| η_W = 0,6175 | 168 | 1552 | 0,4908 bis 0,4975 | 0,169 bis 0,998 |
| 2η_A = ln γ_L = 0,6231 | 232 | 1936 | 0,4911 bis 0,4977 | 0,179 bis 0,999 |

- ε = η_A gibt keine Treffer: Q4 ist für A in D auch am Scan verfehlt.
- Die Mitten der sin²θ₂₃-Fenster von η_W und 2η_A liegen 0,0003 auseinander (Kriterium 0,005): **Die Maske trennt W mit D nicht von A mit D′.**
  Dafür wäre eine Messung von sin²θ₂₃ auf etwa 10⁻⁴ nötig, und die Fenster selbst sind 0,0067 breit. Mit heutigen Daten ist das nicht entscheidbar.
- Die drei Zeilen „H45a/b/c“ am Ende der Ausgabe stammen aus dem unveränderten Code k105 und beziehen sich auf dessen alte Kandidatennamen; sie sind
  hier ohne Bedeutung. Trefferzahlen hängen am Raster (k358) und sind kein Maß.

## Was daraus folgt
1. Auf die Weggabelung: Die Rechnung spricht für **„der Treffer war Zufall“**. Die alte Lesart als gemeinsamer Zustand ist widerlegt; als zweiter
   Zustand ist sie nicht widerlegbar, aber sie verlangt eine neue Setzung und bringt nur eine Zahl, die auch in W zweimal vorkommt.
2. Eine messbare Größe, die „W“ von „A mit D′“ trennt, gibt es im Bestand nicht: Beide liefern für Q1 bis Q3 dieselben Zahlen, die Maske
   unterscheidet sie nicht. Der einzige Unterschied sind die Portgewichte, für die es keine Messgröße gibt.
3. r70 bleibt, wie es ist. Kein Urteil älterer Tests ändert sich.

## Grenzen
- D ist eine Setzung dieser Notiz; im Bestand sind Q1 bis Q3 einzeln gesetzte Gleichsetzungen. β_sym ist das Postulat r67 (OP1 offen).
- m_Z = 91,1876 GeV; k358 rechnet mit 91,1880 (m_W dort 80,3615). Der Unterschied von 0,4 MeV ändert kein Urteil.
- m_h aus κ über die Ein-Schleifen-Formel von k303 (einige Prozent genau), Anteile gerundet. Die Liste der 20 Funktionen ist meine Wahl.
- In der Vorab-Notiz steht 2η_A = 0,623105; richtig ist 0,623100 (Tippfehler, gerechnet wurde mit dem exakten Ausdruck).
- Kein Guard berührt; OP1 bis OP5 bleiben offen. Vergeben: H181, k383. Nächste frei: H182, k384 (vor Vergabe prüfen).

## Dateien
`k383_test_h181.py` (`k383_out.txt`), `k383b_gegenprobe.wl` (`k383b_out.txt`).
