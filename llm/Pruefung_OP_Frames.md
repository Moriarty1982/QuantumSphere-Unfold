# Prüfung: Haben die offenen Probleme OP1–OP5 falsche Frame-Konfigurationen untersucht?

Stand 2026-10-24, nach v4.9.0-r60. Autor: „sieh dir op1 nochmal an, da könnte das selbe problem vorgelegen haben das es falsche frame konfigurationen untersucht hat,
genauso wie die anderen op“. Prüfung (keine Vorhersage) nach Konvention F (r22, F1–F7 aus r24), der Klassentrennung (r18/r19: Skalengrößen Weg C e^{kη}, Auslesegrößen
Weg A γ_L) und der Einheitenregel 7 (r36). Eine Rechnung (`k101_fenster_eta.py`) ist Beobachtung, kein Test.

## OP1 (β_sym als Fixpunkt der Kaskade, ohne γ_BI/γ_string)

Drei Werte stehen im Korpus nebeneinander: Hopf 1/√3 (γ_L = 2), Tribonacci 1/𝕋 = 0.5437 (γ_L = 𝕋 = 1.8393), gemessen 0.5493 (γ_L = γ_BI/γ_string = 1.864). Die
„Lücken“ zwischen ihnen sollte die Gitterkorrektur δ_CL schließen (OP4), die als Zufall archiviert ist (v4.8.0-r09).

1. **Tribonacci (`thm:tribonacci`) mischt Frames und Klassen.** Die Bedingung γ_L = 1/β setzt eine Auslesegröße des Materie-Frames (γ_L, kehrt in T das Vorzeichen um)
   gleich 1/β = β_T, dem Offset im eigenen Maß des Tachyons (r24.2: β_T² = 1/β²). Der Statusvermerk sagt dasselbe in der Sprache der Klassen: äquivalent zu cosh 2η = e^η,
   also Weg A = Weg C. Beides sind Gleichsetzungen über Frame- bzw. Klassengrenzen; ein frame-konsistenter Fixpunkt ist das nicht.
2. **Hopf (`thm:bsym-hopf`, `rem:bsym-hopf-gap`) liest einen reinen R-Zustand als Materie-Offset.** β = sin(θ_H/2) ist die Halbwinkel-Relation eines **reinen** Zustands auf
   S³, gemessen vom Photon-Pol; der Hauptkorpus-„Photon-Frame“ ist nach r24 der Bezugsframe R (rein, |b| = 1). Der Materie-Frame von Konvention F ist bei demselben β
   **gemischt**: Bei β² = 1/3 hat der reine Hopf-Zustand die Besetzungen (2/3, 1/3), der Materie-Zustand (3/4, 1/4) mit |b| = 1/2 (r17). Dasselbe β bezeichnet also zwei
   verschiedene Zustände; die Hopf-Herleitung vergleicht R mit M.
3. **Gemessen (`thm:symmetric-frame`) ist frame-konsistent.** γ_L = γ_BI/γ_string ist der Lorentz-Faktor zwischen den realen Projektionen von M und T (r24.2) und nach r24.3 das
   Verhältnis der Bloch-Längen |b_R|/|b_M|. Er bleibt aber Eingabe; OP1 selbst ist offen.
4. **Folge für OP4:** Die Hopf-Lücke (4.9 %) und die Tribonacci-Lücke (1.35 %) vergleichen den gemessenen M-Wert mit Werten aus einem anderen Frame bzw. einer anderen
   Klasse. Sie sind mindestens teilweise Artefakte der Konfiguration; eine Gitterkorrektur, die sie „schließt“, ist dafür nicht nötig.
5. **Beobachtung (k101, kein Test):** Unter der Lesart von r55/r57/r60 legt die Leptonmischung die Rapidität unabhängig von γ_BI/γ_string fest: η ∈ [0.611, 0.647], also
   β_sym ∈ [0.545, 0.570] und γ_L ∈ [1.844, 1.961]. Der gemessene Wert liegt darin, **Hopf (2.0) und Tribonacci (1.839) liegen beide knapp außerhalb**. Über das ganze
   Fenster bleibt sin²θ₂₃ ∈ [0.491, 0.498] (H46 hängt nicht am genauen ε). Nicht blind, weil die Lesart ε = η nach den Fenstern gewählt wurde.

## OP2 (Dirac-Operator auf H⁺₋)

Bis auf (T4) geschlossen; (T4) ist OP1 (`thm:op2-T4-equals-op1`): γ_L als Verhältnis der GOE- und GUE-Entfaltungsskalen. Das setzt Skalengrößen (Spektren, Weg C) gleich
einer Auslesegröße (Weg A), dieselbe Klassenmischung wie in OP1 Punkt 1.

## OP3 (Koide-Block)

Strukturell geschlossen; die Phasenformel θ_K = π − √2 arcsin β_sym ist durch Daten ausgeschlossen (Statusvermerk). Hier nicht nachgeprüft.

## OP4 (Kontinuumskorrektur δ_CL)

Siehe OP1 Punkt 4: Der Gegenstand von OP4 sind gerade die Lücken zwischen Werten verschiedener Frames bzw. Klassen. Nach dieser Prüfung ist OP4 in der bisherigen Form
falsch gestellt; offen bleibt nur OP1 (woher der M-Wert kommt).

## OP5 (Λ_obs, Θ–R-Bilanz, Schritt B)

Die Θ-Summe (`def:theta-sum-B`) verwendet „Photon-Frame“-Nullstellen γ_n/γ_L und den Abschnitt T = γ_L^{−3/2}: Frequenzen und Längen sind Skalengrößen (Weg C), umgerechnet
wird mit γ_L (Weg A). Das ist eine Klassenmischung. Sie erklärt das Scheitern aber nicht: e^η = 1.854 und γ_L = 1.864 unterscheiden sich nur um 0.5 %, die Abweichung der
Vermutung beträgt 1.003 (K7.3). Diese Lücke von etwa 1 bleibt ein eigener Befund (vermutlich ein fehlender Konstantterm der expliziten Formel, siehe Datensatz).

## Ergebnis

- OP1: Zwei der drei Werte (Hopf, Tribonacci) stammen aus Konfigurationen, die Frames bzw. Klassen mischen; nur der gemessene Wert ist frame-konsistent. OP1 bleibt offen,
  aber die Zielgröße ist der M-Wert selbst, nicht eine Korrektur von Hopf oder Tribonacci.
- OP4 ist in der bisherigen Form falsch gestellt.
- OP2 (T4) trägt dieselbe Klassenmischung wie OP1.
- OP5: Klassenmischung vorhanden, aber nicht die Ursache des Fehlers.
- Neu: Die Leptonmischung bestimmt unter der Lesart r55–r60 ein Fenster für β_sym, das den gemessenen Wert enthält und Hopf und Tribonacci ausschließt.
