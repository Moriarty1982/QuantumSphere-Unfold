# Ergebnis H150: Das Vorzeichen von 2a − b folgt nicht allein aus der Feldgleichung; es hängt am Vorzeichen der Kopplung κ und an der Wahl „skalenfrei“

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H150_Vorzeichen_2a_minus_b.md` (Commit fc17ee9; a und f nicht blind). Skripte `k333_vorzeichen_2a_b.py`
(`k333_out.txt`), `k333b_gegenprobe.wl` (`k333b_out.txt`, Wolfram). Status: a, d, e, f bestätigt; b für gleiche Komponentenzahl bestätigt, für die
Lage aus H149 (1 gegen 2 Komponenten) im Teil „Abschneidung“ widerlegt; c nach Wortlaut widerlegt (Teil r > 2).**

Anlass: Autor „ja“ auf den Vorschlag nach H149. Seine Regel: Das Vorzeichen soll aus der Feldgleichung folgen und nicht gesetzt werden. Seine Richtungsentscheidung
„skalenfrei oder Skala als Setzung“ ist offen, deshalb sind beide Fälle gerechnet. Werkzeuge: Python (sympy für β-Funktionen und Divergenzen, scipy für den Fluss),
Wolfram unabhängig (β-Funktionen über SolveAlways, Fluss mit NDSolve auf 25 Stellen): alle gemeinsamen Größen gleich, der Fluss auf zehn Stellen. Qiskit nicht
eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

Zuordnung (vorab): A = Norm der Vorstufe (φ = ReΨ), B = Norm der Kopienrichtung, also a = λ_A, b = κ, c = λ_B. Auf dem Tausch ist **2a − b = 2λ − κ**.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H150a | V(N): 2a − b = 0; β_κ − 2β_λ = 0 bei κ = 2λ für n = 1, n = 2 und auch für (1, 2) | exakt | **bestätigt** (nicht blind) |
| H150b | V₄ = λ − (2λ − κ)cos²θ sin²θ: Minimum bei π/4 genau für −2λ < κ < 2λ, sonst bei 0 bzw. π/2. Abschneidung: gleiche Komponentenzahl gibt gleiches δμ²; bei 1 gegen 2 ist δμ_A² − δμ_B² ∝ 2κ − 4λ, und θ wandert nach cos 2θ = c_L/f², unabhängig von λ, κ | Fenster exakt; Abschneidung verschiebt nicht | **Fenster bestätigt; Abschneidung für (1, 2) widerlegt** |
| H150c | r < 0: Klasse (iv), A = B, K = ⅔ exakt (190/190 für n = 1 und n = 2). 0 < r < 2: keine Skala, r → 2⁻. r > 2: für n = 2 nur 136 von 200 mit Skala bis τ = 10⁴; für n = 1 keiner, denn dort ist 16π²·dr/dt = −2λr(r − 2)(r − 6) und r = 2 zieht von beiden Seiten an | alle Gitterpunkte wie vorhergesagt | **nach Wortlaut widerlegt** (Teil r > 2), Teile r < 0 und 0 < r < 2 bestätigt |
| H150d | 1 gegen 2 Komponenten, Start auf λ_A = λ_B, κ < 0: alle in Klasse (iv), K am GW-Punkt 0,6667 … 0,6778, Median 0,6719; 57,9 % innerhalb 1 %. Zusatz 1 gegen 7: Median 0,697 | „überlebt“ bei ≥ 90 % | **Koide verschoben** (wie vorhergesagt) |
| H150e | gleiche Komponentenzahl, abseits der Linie: 836/836 Klasse-(iv)-Punkte enden näher am Tausch; 26,7 % mit \|K − ⅔\| < 1 % | anziehend ≥ 90 % | **anziehend**, Koide-Anteil unter 50 % (wie vorhergesagt) |
| H150f | η(B − μ²A)²: a = ημ⁴, b = −2ημ², c = η; Beschränktheit η ≥ 0 ⇒ κ ≤ 0, 2a − b = 2ημ²(μ² + 1) > 0; Minimum bei tan θ = μ | exakt | **bestätigt** (nicht blind) |

## Lesart: woran das Vorzeichen hängt
1. **Das Vorzeichen von 2a − b ist das Vorzeichen von 2λ − κ.** Die Feldgleichung (k290) lässt κ frei. Mit geeichter U(1) bzw. dem Potential der vollen Norm ist es
   genau null, θ ist flach, und das bleibt in jeder Ordnung so.
2. **Skala als Setzung:** Koide ist das Minimum für das ganze Fenster −2λ < κ < 2λ. Das Vorzeichen wird also nicht festgelegt, aber auch nicht fein abgestimmt:
   Es reicht κ < 2λ. **Mit einer Abschneidung zerstört der Ansatz den Koide-Punkt**, sobald Vorstufe und Kopienrichtung verschieden viele Komponenten haben (1 gegen 2
   in der Lage aus H149): Der Massenterm wird tauschungerade, und θ geht nach cos 2θ = c_L/f², gleich welche Kopplungen. Koide überlebt dort nur ohne quadratische
   Divergenzen, also in der skalenfreien Lesart.
3. **Skalenfrei:** Der einzige Weg zu einem Kondensat am Koide-Punkt ist **κ < 0** (Klasse (iv), die Klasse, in der immer eine Skala entsteht). Dann ist 2a − b > 0
   ohne weitere Wahl. Für 0 < κ < 2λ entsteht keine Skala und die Krümmung geht im Infraroten gegen null; bei einer reellen Vorstufe (n = 1) zieht die volle Norm
   sogar bis r = 6 an. **Das Vorzeichen folgt also aus der Feldgleichung, wenn man zwei Dinge verlangt: skalenfrei und die Skala soll entstehen.** Dann ist κ < 0 und
   θ = π/4 ein Minimum. Ohne die zweite Forderung bleibt es eine Wahl von κ.
4. **Aber nicht genau ⅔:** Mit der tatsächlichen Komponentenzahl (reelle Einheit gegen Kopien-Ebene) schiebt der Fluss den Kondensationspunkt auf K ≈ 0,672
   (+0,8 %), mit der ganzen Im𝕆 auf ≈ 0,70. Gemessen ist K auf 10⁻⁵ genau ⅔; die Frame-Maske der geladenen Leptonen ist Form S (H148) und ändert K nicht. Genau ⅔ gibt
   der Fluss nur bei gleicher Komponentenzahl oder mit passend gewählten Startkopplungen (λ_A ≠ λ_B), und das wäre wieder eine Anpassung.
5. **HC-Form:** Wer das Potential als quadratische Bedingung schreibt, bekommt das Vorzeichen geschenkt (Beschränktheit ⇒ κ < 0), aber das Minimum liegt bei
   tan θ = μ. Mit μ = β_sym² ist das K = 0,364 (H149), Koide nur bei μ = 1.

**Zur offenen Richtungsentscheidung des Autors:** Das Ergebnis hängt davon ab. *Skalenfrei:* Das Vorzeichen folgt, wenn die Skala durch Kondensation entsteht
(κ < 0), und der Koide-Punkt ist dann ein Minimum, allerdings um 0,8 % verschoben. *Skala als Setzung:* kein festes Vorzeichen, ein breites Fenster; mit Abschneidung
geht der Koide-Punkt verloren.

**Zurückgestellte Idee I4 getroffen:** Der Koide-Punkt wird skalenfrei nur über eine Kondensation mit κ < 0 erreicht. Das ist die Lage von I4 („Kondensation als Quelle
von Masse“). I4 wird dem Autor als möglicher Weg genannt; nicht umgesetzt.

## Grenzen
- Eine Schleife, ohne Eichfelder und ohne die Zusatzterme K₁–K₄ (die für homogene Felder verschwinden). Die Komponentenzahl der Kopienrichtung (2 oder 7) hängt an der
  Lesart der Auslesung (r13/k255).
- Der Teil r > 2 von H150c ist an τ ≤ 10⁴ gebunden (wie bei H129).
- OP3, OP4 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H150, k333. Nächste frei: H151, k334.
