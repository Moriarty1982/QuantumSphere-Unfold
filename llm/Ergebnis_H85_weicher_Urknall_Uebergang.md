# Ergebnis H85: Weicher komplexer Übergang am Urknall – beide Kriterien verfehlt, nachträglich eine CPT-artige Struktur

Vorab-Notiz `Vorab_Notiz_H85_weicher_Urknall_Uebergang.md`, Commit `4ac77a0` (teilweise nicht blind). Skript `k200_weicher_urknall.py`, Ausgabe `k200_out.json`.

## Ergebnisse (Δ = 1, Materie-Gewichte; scharf: C₀ = 0,6509, D₀ = 0,3491)
| k | |C| | |D| (+iπ) | |D| (−iπ) |
|---|---|---|---|
| 0,01 | 0,6508 | 0,338 | 0,360 |
| 0,1 | 0,640 | 0,239 | 0,452 |
| 1 | 0,170 | 0,379 | 0,722 |
| 2 | 0,0131 | 0,469 | 0,643 |
| 3 | 0,00079 | 0,495 | 0,610 |
| 5 | < 10⁻⁵ | 0,516 | 0,585 |

Kontrolle: holomorphe Wronski-Determinante konstant auf 6·10⁻¹¹.

- **H85a widerlegt (quantitativ):** C trifft den scharfen Wert schon bei k = 0,01 auf 2·10⁻⁴, D aber nur auf 3,5 % (Kriterium 1 %). Die Abweichung von D wächst linear mit kΔ (3,5 % bei 0,01; 10,5 % bei 0,03); der Grenzwert kΔ → 0 wird erreicht, aber langsamer als vorab angenommen.
- **H85b widerlegt (wie formuliert):** Bei k = 5 ist |D/C| ≈ 10⁵, nicht < 10⁻³. Die Erwartung hatte die Rollen von C und D vertauscht.
- **H85c:** Die beiden Drehrichtungen geben verschiedene |D| (bei k = 0,01: 0,338 und 0,360; bei k = 5: 0,516 und 0,585). Ihr geometrisches Mittel liegt bei den Grenzwerten 0,349 bzw. √(b/a) = 0,549.

## Nachträglich bemerkt (nicht vorregistriert)
- Im adiabatischen Grenzfall (große kΔ) läuft die Mode e^{+ikτ}, die vor dem Urknall positive Norm hat (Gewicht −b), unverändert als e^{+ikτ} weiter, mit der WKB-Amplitude |w|^{−½}, also |D| → √(b/a) = 0,549 im Mittel der beiden Richtungen. Nach dem Urknall (Gewicht a) ist e^{+ikτ} aber die Mode **negativer** Frequenz. Ein Teilchen der Tachyon-Lesart vor dem Urknall wird ein Antiteilchen-artiger Zustand danach. Das ist die CPT-Zuordnung von Boyle–Finn–Turok: Die Zeit ist gespiegelt.
- Die **Beimischung** der anderen Frequenz ist C. Sie fällt für kΔ ≳ 1 exponentiell ab (0,17; 0,013; 0,0008 bei k = 1, 2, 3). Das Spektrum der Beimischung ist also endlich, mit Abschneideskala 1/Δ. Für große Wellenlängen ist die Beimischung die des scharfen Übergangs.
- Die Richtungsabhängigkeit (H85c) ist eine Asymmetrie der Ordnung kΔ zwischen den beiden Drehsinnen der Wick-Drehung. Ob das mit einer Asymmetrie zwischen Teilchen und Antiteilchen zusammenhängt, ist eine Frage, keine Aussage.
- Eine Bestätigung dieser Lesart braucht einen neuen, vorab festgelegten Test (Kriterien für C statt D, Exponent des Abfalls, Asymmetrie).

## Folge
Unter G2 mit komplexem Übergang ist der Urknall für jede Mode eine Zuordnung „Teilchen vor dem Urknall ↦ Antiteilchen danach“ (CPT), plus eine Beimischung, die für lange Wellen durch β_sym festgelegt ist und oberhalb von 1/Δ exponentiell verschwindet. Δ bleibt eine freie Skala. OP5 ist nicht berührt.
