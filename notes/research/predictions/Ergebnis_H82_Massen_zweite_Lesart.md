# Ergebnis H82: Massen und Kopplungen unter der zweiten Lesart – Eichkopplungen passen zu r19, die Gravitation nicht

Vorab-Notiz `Vorab_Notiz_H82_Massen_zweite_Lesart.md`, Commit `c3f956c` (nicht blind). Skript `k197_massen_zweite_lesart.py`, Ausgabe `k197_out.json`.

## H82a bestätigt (wie vorgerechnet)
- Massenterme: Sᵀ ε S = ε und S ε Sᵀ = ε (sympy). Majorana- und Dirac-Massen sind unter dem komplexen Boost invariant und gehen mit P ein.
- Faktoren (allgemein → Materie-Gewichte K = 1/γ, P = 1):

| Größe | Faktor | γ-Exponent |
|---|---|---|
| α (und α_s) | 1/K | 1 |
| Fermionmasse m_f = y·v | P/K | 1 |
| Majorana-Masse | P/K | 1 |
| Higgsmasse m_H | √(P/K) | ½ |
| Erwartungswert v | √K | −½ |
| W-Masse | 1 | 0 |
| θ_W | 1 | 0 |
| G_N | 1/K | 1 |
| ℓ_P = √G | 1/√K | ½ |
| m_P | √K | −½ |

Das unterschiedliche Wachstum folgt also einem festen Muster: Es hängt nur daran, wie viele Ableitungsterme und Nicht-Ableitungsterme eine Größe enthält. In diesem Sinn sind die verschiedenen Faktoren „gleichzeitig richtig“, wie der Autor vermutet hat.

## H82b widerlegt (wie erwartet)
- **Passt:** α (Exponent 1 = k), α_s (1 = k), θ_W (0, Auslesegröße).
- **Passt nicht:** G_N (Exponent 1, r19 k = 2), ℓ_P (½, r19 k = 3/2).

## Einordnung
- Die Eichseite der zweiten Lesart reproduziert die Gewichte von r19, die Gravitation nicht. Bei G_N fehlt genau ein Faktor γ: Das Gewicht 2 käme heraus, wenn der Gravitationsterm mit K² statt K einginge (der Koframe steht in e·R zweimal). Bei ℓ_P fehlt zusätzlich ein halber Exponent, der in r19 aus den Gewichten von ħ oder c stammt; die Reduktion hier hält ħ und c fest.
- Die Umrechnung von r19 (zwischen M und P) und die Reduktion hier (M und T zu einem Feld) sind nicht dieselbe Operation. Die Übereinstimmung bei α ist ein Hinweis, die Abweichung bei G kein Ausschluss.
- Alle Faktoren lassen sich in umdefinierte Parameter aufnehmen. Beobachtbar wird das Muster nur, wo die Struktur nackte Werte oder Gewichte festlegt.

## Nächste Frage (vorab benannt)
Wie geht der Einstein–Cartan-Term e∧e∧R unter dem vollständigen komplexen Boost und F3 ein: mit K (eine Ableitung, wie hier angenommen) oder mit K² (Koframe zweimal, je ein Gewicht)? Mit K² würde G_N das Gewicht 2 aus r19 treffen.
