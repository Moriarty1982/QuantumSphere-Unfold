# Rückwärtssuche: Welche Regel gäbe κ ≈ 1,2? (k303)

**Stand:** 2026-11-25. **Erkundung, nicht blind.** Das Ziel war aus k300 und H133 (k302) bekannt. Der Zahlentreffer in Abschnitt 3 fiel mir beim Planen auf,
bevor die Kandidatenliste feststand; er ist deshalb als nachträglich zu lesen.
Anlass: Autor, 25.11.2026, 11:32 UTC: „ja“ auf den Vorschlag, rückwärts zu suchen. Vorgehen nach AGENTS.md „Suchrichtung prüfen“: Ziel und notwendige
Bedingungen festhalten, daraus Kandidaten erzeugen oder ausschließen.
Skripte: `k303_rueckwaerts_kappa.py` (Python: numpy, sympy), Ausgabe `k303_out.txt`; Gegenprobe `k303b_gegenprobe.wl` (Wolfram Language), Ausgabe
`k303b_out.txt`. Qiskit nicht eingesetzt (keine Schaltung). Kein Guard berührt. OP1 bis OP5 bleiben offen.

## Vorwissen geprüft
k300 (fehlende Summe 8,52·10¹⁰ GeV⁴), H133/k302 (ein Term κ·A·C, vier entartete Felder, m_S² = 2κv², Regeln R1 bis R3 liefern den Wert nicht),
k292 (Linksladung ω(a² + b²), Rechtsladung ω(a² − b²)), k297 und k299 (HC-Zahlen μ = β_sym² = 0,3018, γ_L = 1,8644, Winkel tan θ = μ; eingesetzt, OP1).
Suche im Repo nach „Veltman“ und „Unitarität“ im Zusammenhang mit einer Kopplung (25.11.): keine Fundstelle.

## 1. Ziel und notwendige Bedingung
- Ziel: κ* = 1,2039 (m_S = 382,1 GeV). Mit den Unsicherheiten von m_t (±0,7 GeV) und m_h (±0,2 GeV) liegt κ* zwischen 1,202 und 1,206.
- In Kopplungen geschrieben: **16κ² = 8π²·m_h²/v² − (3/8)g⁴ − (3/16)(g² + g′²)² + 3y_t⁴.** Die Anteile sind 20,42, −0,07, −0,06 und +2,90.
- Folgerung: Eine Regel, die κ festlegt, sagt im skalenfreien Bild die Higgs-Masse vorher. Man kann die Frage also umdrehen: **jede Regel liefert ein m_h.**
  Die Abhängigkeit ist fast linear (1 % in κ sind 1,1 % in m_h). Unter κ = 0,416 (m_S = 225 GeV) gibt es kein Minimum.

## 2. Regeln mit einem Prinzip dahinter
| Regel | κ | m_S | vorhergesagtes m_h |
|---|---|---|---|
| R1 volle Norm (auch schwache Wirkung plus su(3)) | 0 | 0 | kein Minimum |
| Sp M⁴ = 0 (endliches Ein-Schleifen-Potential) | 0,416 | 225 GeV | 0 |
| Veltman-Bedingung (keine quadratische Divergenz), skalenfrei | 0,606 | 271 GeV | 48,8 GeV |
| Veltman-Bedingung mit gemessenem m_h | 0,509 | 248 GeV | 32,4 GeV |
| Veltman-Bedingung, m_h selbstkonsistent | 0,592 | 268 GeV | 46,7 GeV |
| Unitaritätsgrenze gesättigt, κ = 4π/√(NM) = π | 3,142 | 617 GeV | 345 GeV |
| fester Punkt von κ mit Eichfeldern und Top | keiner außer κ ≤ 0 | | |

Keine dieser Regeln trifft das Fenster 1,08 bis 1,32. Die Veltman-Bedingung ist die naheliegendste, sie gibt etwa die Hälfte von κ* und 47 bis 49 GeV.
Die Formel für den festen Punkt stammt aus dem Gedächtnis (Zwei-Dublett-Modelle, λ₃ = 4κ); ihr skalarer Teil stimmt mit k302 überein.

Variante: Statt der vier Skalare könnten die drei Eichfelder der eigenen su(2) des Anhangs die Summe liefern (9 Freiheitsgrade, nötig 312 GeV). Mit
derselben Kopplung g und dem HC-Wert des Anhangs μ·v kommen 24 GeV heraus. Nötig wäre ein Anhang-Wert von 3,9·v. Das trägt nicht.

## 3. Reine Zahlen des HC als Kopplung (Zahlensuche, kein Prinzip)
14 Zahlen aus μ und γ_L (mit Kehrwerten, Quadraten, Wurzeln, den Winkelfunktionen von 2θ) in drei Normierungen (κ, 2κ, 4κ), zusammen 42 Kandidaten.
- **Genau ein Kandidat liegt im Fenster: κ = 1/cos 2θ = (1 + μ²)/(1 − μ²) = (γ_L + 1/γ_L)/2 = 1,2004.** Abweichung vom Ziel −0,29 %, das gäbe m_h = 124,8 GeV.
- Bei log-gleichverteilten Kandidaten wären im Fenster 1,2 Zufallstreffer zu erwarten, bei ±5 % (ungefähre Genauigkeit der Ein-Schleifen-Formel) 0,7,
  bei ±0,3 % nur 0,04. Die Formel ist aber nicht auf 0,3 % genau, deshalb zählt die grobe Zahl: **Ein Treffer bei etwa einem erwarteten ist kein Beleg.**
- Die Zahl hängt an γ_L, das eingesetzt ist (OP1): γ_L = 1,86 gibt 124,6 GeV, 1,87 gibt 125,0 GeV. Mit der Tribonacci-Zahl 1,839 kämen 123,7 GeV heraus,
  mit der Silberzahl 149,8 GeV.
- Mögliche Lesart: 1/cos 2θ = (a² + b²)/(a² − b²) ist auf der HC-Richtung das Verhältnis von Linksladung zu Rechtsladung (k292). Eine Herleitung,
  warum die Kopplung des nächsten Anhangs diesem Verhältnis gleichen sollte, gibt es nicht.

## Befund
1. Die Rückwärtssuche findet **keine Regel mit einem Prinzip dahinter**, die κ ≈ 1,2 liefert. Die bekannten Kandidaten (volle Norm, Veltman, Sp M⁴,
   Unitarität, fester Punkt) geben 0, 0,5 bis 0,6 oder 3,1.
2. Es gibt **einen Zahlentreffer**: κ = (γ_L + 1/γ_L)/2. Er ist nach der Zählung oben mit Zufall verträglich und beruht auf einer eingesetzten Zahl.
   Er ist ein Kandidat für eine Regel, mehr nicht.
3. Prüfbar würde er erst durch eine Herleitung: Wenn der Turm aus eigenem Grund κ = Linksladung/Rechtsladung verlangt, wäre das ein blinder Test wert
   (H134 ist frei). Ohne Herleitung bleibt es eine Auffälligkeit.

## Grenzen
Eine Schleife, skalenfreies Bild, Lesart S-a aus k302 (vier Felder). Massen und v aus dem Gedächtnis wie in k300. Die Kandidatenliste in Abschnitt 3
habe ich selbst gewählt, nachdem mir der Treffer aufgefallen war; die Zählung der Zufallstreffer hängt an dieser Wahl und an der angenommenen
Verteilung. Die Genauigkeit der Ein-Schleifen-Formel (einige Prozent) ist geschätzt, nicht gerechnet. Der Pol bei etwa 14 TeV aus k302 bleibt bestehen.
