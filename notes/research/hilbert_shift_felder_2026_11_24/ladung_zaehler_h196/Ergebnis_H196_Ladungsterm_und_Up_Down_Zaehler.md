# Ergebnis H196: Der Ladungsterm verschiebt das Quintik-Glied wirklich — aber als Umparametrisierung, nicht als Vorhersage (Test, k404, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H196_Ladungsterm_und_Up_Down_Zaehler.md`, Commit 8cfd9c5,
vor der Rechnung). H196a nicht blind (Reduktion). **Werkzeuge:** Python (numpy, scipy, sympy) für die gemeinsamen Fits und die
Kontrolle (`k404_test_h196.py`/`k404_out.txt`); Wolfram Language für die exakten ladungsungeraden Krümmungen (`k404b_out.txt`),
bestätigt sympy exakt. Qiskit nicht nötig. **Anlass:** „mach das" des Autors (27.11., 10:13): verschiebt der Ladungsterm aus H182
das Quintik-Glied (l_k²) für Up anders als für Down?

## Frage und Ansatz
H182: Up (Ladung ⅔) und Down (Ladung ⅓) unterscheiden sich durch das **Vorzeichen** s = ±1 eines ladungsungeraden Anteils. H195:
Masse = Zähler(l_k) / (l_i+l_j)². H186 hat die ladungsungeraden Krümmungen schon als **direkte** Quelle (ohne Nenner) geprüft und
widerlegt (r₂ ≈ 1). Neu: dieselben ladungsungeraden Zähler **über dem H195-Nenner** (l_i+l_j)², der die schwerste Mode verstärkt.
Modell: m_s(k) = [A·l_k + B·l_k² + s·γ·O(l_k)] / (l_i+l_j)², O ein fester H186-Kandidat.

## Ergebnis

**H196b (Test — fester Kandidat, 3 Parameter): widerlegt.** Kein einzelner ladungsungerader Kandidat (c1, c2, c4/c5, c7/c9, c11)
trägt beide Sektoren mit gemeinsamem (A, B, γ): alle geben **Up ≈ 237σ** (Down ≈ 9σ). Der gemeinsame ladungsgerade Teil (A, B)
zwingt beide Sektoren in dieselbe Skalenstruktur; ein einzelnes γ·O kann die sehr verschiedenen b/a (−57,9 vs −0,085, Faktor 680)
nicht überbrücken. Der H195-Nenner behebt H186 hier **nicht**. Kontrolle: erfundene Massenpaare erreichen χ² < 12 in 0,0 %.

**H196c (Bericht — volle Ladungsstruktur, 4 Parameter): trifft (χ² = 7,9; 2 dof; max 2,1σ).** Mit
m_s = [A·l_k + B·l_k² + s(C·l_k + D·l_k²)]/(l_i+l_j)²:
- ladungsgerade A = 1,08·10⁻³, **B = 3,29·10⁻²**; ladungsungerade C = −2,22·10⁻³, **D = 3,32·10⁻²**.
- **Antwort auf die Frage: ja.** Das ladungsungerade l_k² (D) ist nötig, hat das **Vorzeichen +**, und **D ≈ B**. Damit ist
  b_up = B + D = 0,066 (starkes l_k²) und b_down = B − D = −2,8·10⁻⁴ (**l_k² praktisch abgeschaltet**). Die Ladung verdoppelt das
  Quadratische für Up und löscht es für Down — genau das gesuchte „Up quadratisch, Down linear".
- **Aber keine Vorhersage.** Die vier Parameter (A, B, C, D) sind eine **Umparametrisierung** der vier Sektor-Koeffizienten aus
  H194 (b/a Up −57,9, Down −0,085 kommen exakt wieder heraus); es ist nichts an Zahlen gewonnen. Das gesuchte ladungsungerade
  Verhältnis D/C = −14,9 trifft **keinen** der H186-Kandidaten (deren l²/l-Verhältnisse 0 bzw. ±0,167 sind). Die Näherung D ≈ B
  (Down-l_k² ≈ 0) ist mit 2 Freiheitsgraden ein gefitteter Zufall, nicht erzwungen.

## Lesart
- **Strukturell beantwortet die Ladung die Frage.** In der Feldgleichung sitzt der Up/Down-Unterschied im Vorzeichen eines
  ladungsungeraden Terms (H182); die Rechnung zeigt, dass dieser Term das l_k²-Glied tragen **kann** und mit dem richtigen
  Vorzeichen Up quadratisch und Down linear macht. Das ist der Ort des Unterschieds, sauber benannt.
- **Quantitativ bleibt es ein Fit.** Weder trägt ein einzelner feldgleichungs-fester Kandidat (3 Parameter, Up 237σ), noch ist die
  Näherung D ≈ B (die Down's Quadratform löscht) erzwungen. Die vier Zahlen je Modell sind dieselben vier wie in H194, nur anders
  geschrieben. Der H195-Nenner, der H186 hätte beheben können, reicht dafür nicht.
- **Was ein Befund wäre:** ein ladungsungerader Term, dessen Form **und** Stärke festliegen (etwa D = B aus einer Symmetrie, oder
  ein Kandidat mit D/C ≈ −15). Das ist nicht gefunden.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Nenner (l_i+l_j)² | hergeleitet (H195) |
| Ladung → Vorzeichen s des ungeraden Anteils | hergeleitet (H182) |
| ladungsungerades l_k² (D) nötig, Vorzeichen + | **hergeleitet aus dem Fit** (die Frage ist mit Ja beantwortet) |
| Stärke D (D ≈ B, Down-l_k² ≈ 0) | angepasst (2 dof, nicht erzwungen) |
| feste ungerade Form (ein H186-Kandidat) | widerlegt (Up 237σ) |
| vier Koeffizienten A, B, C, D | angepasst (= H194 umparametrisiert) |

## Grenzen
Zweite Variation um das ruhende Vakuum; die ladungsungeraden Krümmungen aus H186. Die volle Struktur trifft nur, weil sie so viele
freie Zahlen hat wie H194. OP3/OP4 bleiben offen. Nächste frei: H197, k405.
