# Ergebnis H164: β_sym ist der Überlapp des Hopf-Zustands mit dem Gegenpol; der zugehörige Boost führt den R-Zustand auf die Besetzungen des Materie-Zustands

**Stand:** 2026-11-26. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H164_Beta_sym_Ueberlapp_zweier_Auslesen.md` (Commit 45be2d4, vor dem ersten Lauf).
**Überwiegend nicht blind** (in der Vorab-Notiz offengelegt). Skripte: `k355_test_h164.py` (sympy; Qiskit 2.6.2 `quantum_info` für Zustände, Überlappe,
Dichtematrizen), `k355b_gegenprobe.wl` (Wolfram, exakt, mit der Aberrationsformel statt der SL(2,ℂ)-Matrix). Ausgaben: `k355_out.txt`, `k355b_out.txt`.
Kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf). Kein Guard berührt.

## Frage
H161 fand: Zwei Lichtrichtungen im Winkel θ liegen nach einem Boost mit β = cos(θ/2) gegenüber, und der Überlapp der zwei Spinoren ist dieses β. Spielt β_sym
(θ = 113,35°) in dieser Rolle im Modell eine Rolle?

## Urteil nach den vorab festgelegten Kriterien
| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a benanntes Paar mit Überlapp β als Identität | bestätigt | **bestätigt** |
| K-b Boost-Identitäten (β, ε der Maske, γ_L, sech 2ε) | bestätigt | **bestätigt** |
| K-c Mischung der zwei Auslesen = Materie-Zustand | widerlegt | **widerlegt** |
| K-d Bilder unter dem Boost auf benannten Winkeln | offen (Vermutung: widerlegt) | **nach Wortlaut widerlegt, im Kern bestätigt** (siehe Befund 4) |
| Gesamt | trägt teilweise | **trägt teilweise** |

## Befunde
1. **Das Paar gibt es schon im Companion (K-a).** θ = 113,355° ist das Supplement des Hopf-Winkels θ_H = 66,645° aus `thm:bsym-hopf`: β_sym = sin(θ_H/2) =
   cos((π − θ_H)/2). Die zwei Auslesen sind der reine Hopf-Zustand K₁ (im Winkel θ_H vom Pol N) und der **Gegenpol S**. Unter 78 Paaren von 13 benannten Zuständen
   ist |⟨ψ₁|ψ₂⟩| = β genau für (K₁, S) und seine Bilder unter Tausch und Tachyon-Abbildung eine Identität. Einziger bloßer Zahlentreffer: (h, getauschtes h) in
   HS(2) mit 2β²/(1 + β⁴) = 0,5532 (+0,7 %), keine Identität.
2. **Der Boost ist die Maske (K-b).** Der Boost, der K₁ und S auf Gegenpunkte legt, hat die Geschwindigkeit β_sym und die Rapidität ε = artanh β_sym = 0,6174,
   das ε der Maske aus H45. Zwei Frames mit ±β gegen das System der Gegenpunkte haben den relativen Lorentz-Faktor γ_L = (1 + β²)/(1 − β²) = 1,86444, und
   sech 2ε = 1/γ_L (r24.3). Alles exakt (sympy und Wolfram). Die invariante Masse des Paars ist M = 2E·√(1 − β²).
   Damit ist die Stelle im Beweis von `thm:bsym-hopf`, die den Versatz „nach der üblichen Halbwinkelbeziehung“ mit sin(θ_H/2) gleichsetzt, in dieser Lesart
   ein Satz: Der Überlapp zweier Lichtrichtungen **ist** die Geschwindigkeit des Systems, in dem sie gegenüberliegen (H161, K-e).
3. **Die Mischung der zwei Auslesen ist nicht der Materie-Zustand (K-c).** Sie hat die Bloch-Länge β = 0,5493 und die Besetzungen (0,7747; 0,2253); der
   Materie-Zustand der Konvention F hat 1/γ_L = 0,5364 und (0,7682; 0,2318). Gleich wären sie nur für β³ + β² + β − 1 = 0, β = 0,5437 (Zahl ohne Bedeutung im Bestand).
4. **Der Boost trägt den R-Zustand auf die Besetzungen des Materie-Zustands (K-d).** Unter dem Boost wird der Winkel zwischen dem Pol und dem Hopf-Zustand von
   θ_H (cos = 1 − 2β²) zu **2α mit cos 2α = (1 − β²)/(1 + β²) = 1/γ_L**, also 66,64° → 57,56° (tan α = β, der Kickwinkel aus r27). Die Besetzungen von K₁′ entlang
   der Achse des Polbilds N′ sind exakt 1/(1 + β²) und β²/(1 + β²), die des Materie-Zustands; dephasiert um diese Achse hat K₁′ die Bloch-Länge 1/γ_L
   (Wolfram: Differenzen exakt null). Am Hopf-Wert: 70,53° → 60°, Besetzungen (⅔, ⅓) → (¾, ¼), genau das Zahlenpaar aus dem Statusvermerk zu `thm:bsym-hopf`.
   Der Grund ist kurz: (1 − cos)·E₁E₂ ist invariant, und die Doppler-Faktoren von N und K₁ sind γ(1 + β²) und γ(1 − β²).
   **Nach Wortlaut ist K-d widerlegt:** Die Bilder der Äquatorpunkte liegen auf keinem benannten Winkel (z. B. 89,51°, 50,77°), und N′–S′ ist π − 2α, kein Gegenpunkt.
   *Offengelegt:* Die Beziehung N′–K₁′ = 2α habe ich nach dem Commit der Vorab-Notiz und vor dem ersten Lauf im Kopf hergeleitet; die Vorhersage „offen“ stand da schon.

## Was das bedeutet
- Der Statusvermerk zu `thm:bsym-hopf` (r61) hält fest, dass der Satz einen R-Zustand als Materie-Versatz liest. H164 gibt die fehlende Abbildung an: Der Boost
  mit β_sym, der den Hopf-Zustand und den Gegenpol gegenüberstellt, macht aus dem reinen R-Zustand (Besetzung β² am Gegenpol) einen Zustand mit den
  Materie-Besetzungen (β²/(1 + β²)). Die zwei Lesarten von β_sym, Winkel und Geschwindigkeit, sind in der Himmelskugel-Lesart dieselbe Aussage.
- Gesetzt bleibt: die Lesart „Hopf-Sphäre = Himmelskugel von Lichtrichtungen“, die Wahl des Gegenpols als zweite Auslese und der Schritt des Dephasierens.
  Der Boost ist nicht unitär; das Bild des Pols ist nicht mehr der Gegenpunkt des Bilds des Gegenpols.
- **β_sym selbst wird nicht hergeleitet.** Jede Aussage hier ist eine Identität in β und gilt für jeden Wert. OP1 bleibt offen.

## Erkundung ohne Kriterium
- Am Hopf-Wert β = 1/√3 ist θ = arccos(−1/3) = 109,47°, der Tetraederwinkel. Vier Zustände mit paarweisem Überlapp 1/√3 bilden ein Tetraeder, und ihre
  Projektoren summieren sich zum Doppelten der Eins: Das ist die symmetrische vollständige Messung eines Qubits mit vier Ausgängen. Vier paarweise gleichwinklige
  Richtungen gibt es nur bei diesem Winkel; beim gemessenen β (113,36°) höchstens drei. Die Hopf-Lücke ist in dieser Lesart der Abstand von einer Anordnung, die
  sich zu vier gleichberechtigten Auslesen schließt. Ob das mit der ℤ/3-Bahn aus `rem:bsym-hopf-gap` zusammenhängt (drei Kerne im gleichen Abstand vom Pol,
  also Pol plus drei), ist nicht untersucht; die Zahlen passen (drei Tetraederecken liegen im Winkel 109,47° vom vierten).

## Grenzen
Die Lesart ist gesetzt; frames: (K₁, S) ist nach r24/r61 ein Paar von R-Zuständen, die Aussage über den Materie-Zustand betrifft nur dessen Besetzungen und
Bloch-Länge. Kein Datenvergleich. β_sym bleibt Eingabe (OP1). OP1 bis OP5 bleiben offen.
