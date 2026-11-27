# Ergebnis H195: Die Feldgleichung gibt den Nenner der H188-Form her, nicht ihre Koeffizienten (Test, k403, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H195_H188_Form_aus_der_Feldgleichung.md`, Commit a5f2f6d,
vor der Rechnung). H195a ist nicht blind (Herleitung). **Werkzeuge:** Python (numpy, sympy) für die kinetischen Normen, die
Krümmungs-Reduktion und die Fits (`k403a_peirce_check.py`, `k403_test_h195.py`/`k403_out.txt`, `k403c_zaehler_grad.py`/`k403c_out.txt`);
Wolfram Language für die Grad-Leiter der F₄-Krümmungen und die Norm-Identität (`k403b_out.txt`), bestätigt Python/sympy exakt.
Qiskit nicht nötig. **Anlass:** „ja" des Autors (27.11., 09:40) zur Herleitung der H188-Form aus der Feldgleichung.

## Was hergeleitet ist

**Der Nenner (l_i+l_j)² — hergeleitet.** Jede Quark-Farbmode ist ein Off-Diagonal-Oktonion X in Position (i,j) der Albert-Algebra
H₃(𝕆). Die Peirce-Zerlegung am Vakuum W₀ gibt exakt (verifiziert über die H₃(𝕆)-Algebra aus k387, konstant über alle acht
Komponenten):

  **W₀∘X = ½(l_i+l_j)·X.**

Damit skalieren die kinetischen Normen der Mode: flach N₀ = Tr(X∘X) = const; W-gewichtet N₁ = ½(l_i+l_j)N₀; **W²-gewichtet
N₂ = Tr((W₀∘X)∘(W₀∘X)) = ¼(l_i+l_j)²·N₀**. Eine kinetische Form ∝ Tr((W∘∂W)∘(W∘∂W)) gibt der Mode (i,j) also den
Normierungsfaktor ¼(l_i+l_j)². Da die Masse = Krümmung / kinetische Norm ist, erscheint der **Nenner (l_i+l_j)²** der H188-Form
direkt aus der kinetischen Struktur, ohne Einsetzen von Hand.

## Was nicht hergeleitet ist

**Der Zähler — eine freie Polynomwahl, nicht vorhergesagt.** Die zweite Variation eines F₄-invarianten Potentials v = x^n gibt der
Mode (i,j) die Krümmung 2n·h_{n−2}(l_i,l_j). Auf dem **festen** Vakuum (Tr W₀ = 3 gesetzt, K = ⅔ ⇒ e₂ = 3/2) wird das eine
Funktion von l_k allein. Die Grad-Leiter (sympy und Wolfram, exakt):

| Potentialgrad n | Krümmung der Mode (i,j) auf dem Vakuum | Grad in l_k |
|---|---|---|
| 2 | 4 | 0 (const) |
| 3 | 18 − 6 l_k | 1 |
| 4 | 60 − 24 l_k | 1 |
| 5 | 180 − 60 l_k − 30 l_k² + 10 l_k³ | 3 |
| 6 | 513 − 108 l_k − 234 l_k² + 108 l_k³ − 12 l_k⁴ | 4 |

**l_k² erscheint zuerst bei Potentialgrad 5.** Der Zähler ist damit ein Polynom in l_k, dessen Grad die Potentialordnung setzt;
die Koeffizienten sind die freien Potentialkoeffizienten.

## H195b (Test): die hergeleitete einfache Form trifft nicht
Die niedrigste hergeleitete Form (Potentialgrad ≤ 4, Zähler **A + B·l_k**) über dem Nenner (l_i+l_j)²:

| Form | Up χ² | Down χ² | Urteil |
|---|---|---|---|
| (A + B l_k)/(l_i+l_j)² (Grad ≤ 4) | **16990** (92,7σ) | 93 (9,1σ) | trifft keinen Sektor |
| (a l_k + b l_k²)/(l_i+l_j)² (H188, Grad 5) | 4,8 | 3,1 | trifft (wie H194) |
| (A + B l_k + C l_k²)/(l_i+l_j)² (Grad 5, 3 Param) | 0,0 | 0,0 | exakt (0 Freiheitsgrade) |

Die Daten **verwerfen** den Zähler A + B·l_k (Potentialgrad ≤ 4): Up 92,7σ. Andere kinetische Nenner (flach, W-Norm) sind noch
schlechter (Up 56000 bzw. 48000 χ²). Das von H188 benötigte l_k² gelingt erst ab Potentialgrad 5.

## H195c (Test): woher das l_k²?
Das l_k² hat sehr wohl eine Feldgleichungs-Quelle — einen **Quintik-Term** (Potentialgrad 5) im Potential. Der H188-Zähler ist
damit feldgleichungs-**fähig**, aber nicht **vorhergesagt**: Mit einem Potential vom Grad 5 ist der Zähler ein beliebiges Polynom
A + B l_k + C l_k² (drei freie Koeffizienten je Sektor); die H188-Wahl (nur l_k und l_k², keine Konstante) ist ein 2-Parameter-
Spezialfall, dessen fehlende Konstante eine Setzung ist, keine Folge. Warum Up die Quadratform und Down die Linearform bevorzugt
(verschiedene b/a, Faktor 680, H194), bleibt frei — beide Sektoren nutzen dieselbe Basis {l_k, l_k²}, nur mit anderen
Koeffizienten.

## Gesamturteil: teilweise
Nach dem vorab festgelegten Kriterium: H195b widerlegt (die hergeleitete einfache Form trifft keinen Sektor und schlechter als
H188); H195c zeigt aber, dass der l_k²-Zähler feldgleichungs-fähig ist (Quintik). Der **Nenner ist hergeleitet**, der **Zähler ist
feldgleichungs-kompatibel, aber nicht eindeutig vorhergesagt** (freie Koeffizienten, Potentialgrad ≥ 5 nötig): **teilweise**.

Konkret auf die Frage des Autors „warum gerade (a l_k + b l_k²)/(l_i+l_j)²":
- **Nenner (l_i+l_j)²:** aus der kinetischen Normierung (Peirce-Eigenwert ½(l_i+l_j), W²-Gewichtung) — hergeleitet.
- **Zähler l_k, l_k²:** die ersten beiden nichttrivialen Potenzen, die ein Potential vom Grad ≤ 5 erzeugt; die Koeffizienten
  (a, b) und das Fehlen der Konstante sind frei — nicht hergeleitet.
- **Up quadratisch / Down linear:** nicht erklärt; die verschiedenen b/a bleiben zwei angepasste Zahlen je Sektor.

## Kontrolle
2000 erfundene Massensätze durch den Fit der hergeleiteten einfachen Form: ein Sektor < 3σ in 0,8 % (Up) bzw. 0,7 % (Down), beide
in 0,0 %. Die einfache Form ist also nicht knapp daneben, sondern strukturell falsch — es braucht wirklich das l_k² (Grad 5).

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Masse = Krümmung / kinetische Norm | gesetzt (Lesart aus H188) |
| Peirce-Eigenwert ½(l_i+l_j), N₂ = ¼(l_i+l_j)² N₀ | hergeleitet (exakt, verifiziert) |
| Nenner (l_i+l_j)² | hergeleitet (W²-Gewichtung) |
| Form der kinetischen Gewichtung (W²) | gesetzt (W-Norm und flach treffen schlechter) |
| Zähler-Grad (l_k²) ⇒ Potentialgrad ≥ 5 | hergeleitet (Grad-Leiter) |
| Zähler-Koeffizienten a, b, fehlende Konstante | angepasst (frei) |
| Up ≠ Down (b/a verschieden) | nicht erklärt |

## Grenzen
Zweite Variation um das ruhende Vakuum, keine vollständige Lösung der Feldgleichung; die kinetische Form und der Potentialgrad
bleiben Setzungen. OP3/OP4 bleiben offen. Nächste frei: H196, k404.
