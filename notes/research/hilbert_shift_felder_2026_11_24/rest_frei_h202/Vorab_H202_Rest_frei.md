# Vorab-Notiz H202 / k412 — Folgt der ~0,9-%-Rest (D/B−1) aus den Invariant-Koeffizienten, oder ist er frei?

**Datum:** 2026-11-27
**Strang:** Quarkmassen, Feldgleichung (Schritt 2 nach H201)
**Nummern:** Test H202, Skript k412 (vor Push gegen `main` geprüft; Parallel-Thread HS(−1) vergibt ebenfalls k-Nummern)
**Freigabe:** Autor „ja bitte" (27.11., 11:26 UTC) für (1) **und** danach (2).

## Frage

H201 hat die vier Massenkoeffizienten nach Feldgrad zerlegt. Jetzt Schritt (2): Ist das
Verhältnis D/B = 1,0085 (und damit der ~0,9-%-Rest D/B − 1) aus der **Struktur** vorhergesagt,
oder bleibt es ein **freier Eingabewert** (Kopplungskonstanten der Invarianten)?

Die effektiven Koeffizienten entstehen aus Strukturkoeffizienten (exakt, aus H201) mal
**Kopplungskonstanten** (wie stark jede Invariante im Potential steht):

- gerade F4-Invarianten, Kopplungen g₃, g₄, g₅, …:
  A = −6 g₃ − 24 g₄ − 60 g₅ − …   (l_k);  B = −30 g₅ − 234 g₆ − …   (l_k², erst ab Grad 5)
- ungerade H186-Formen (Grad 4), Kopplungen h₂ (c2), h₄₅ (c4/c5), h₇₉ (c7/c9), h₁₁ (c11):
  C = −⅓ h₂ − h₇₉ − h₁₁   (l_k);   D = −⅓ h₄₅ + ⅙ h₇₉ − ⅙ h₁₁   (l_k²)

D/B ist genau dann **vorhergesagt**, wenn die Kopplungen nicht alle frei sind — wenn ein Prinzip
(oder eine minimale Invariant-Zahl) weniger Kopplungen als Koeffizienten erzwingt.

## Vorwissen geprüft

- `grad_selektion_h201/` (H201): Strukturkoeffizienten je Grad (oben). B nur ab Grad 5, D ab Grad 4.
- `symmetrie_db_h197/` (H197): Rang der (gerade, ungerade)-l_k²-Quellen = 2 → D/B frei (bereits
  gezeigt für den l_k²-Block allein). **Neu hier:** der volle Rang der Abbildung (alle Kopplungen)
  → (A, B, C, D) und die Frage nach einer minimalen Invariant-Basis.
- `ladung_zaehler_h196/` (H196): Fit A=1,082e-3, B=3,291e-2, C=−2,224e-3, D=3,320e-2; D/B=1,0085.
  D/C = −14,9 (trifft keine einzelne ungerade Form: c7/c9 gäbe D/C=−1/6, c11 gäbe +1/6).
- Vakuum-Identitäten l_i+l_j=3−l_k, l_i²+l_j²=6−l_k², l_i l_j=3/2−3l_k+l_k².

## Test

**(A) Rang der vollen Abbildung (nicht blind für den l_k²-Block, neu für den vollen Satz).**
Die Matrix M: (g₃, g₅, h₄₅, h₇₉) ↦ (A, B, C, D) aufstellen (minimaler Satz, der alle vier erreicht)
und ihren Rang bestimmen. Rang 4 ⇒ die vier Koeffizienten (und damit D/B) sind unabhängig
einstellbar ⇒ D/B **frei**.

**(B) Minimale Invariant-Basis (blind).** Für jede Teilmenge der Kopplungen mit ≤ 3 Elementen
prüfen, ob sie alle vier Massen innerhalb der Fehler fittet (χ²/dof akzeptabel). Trägt eine
≤ 3-Kopplungs-Basis, so ist D/B eine **Vorhersage** (dann den vorhergesagten Wert gegen 1,0085
halten). Trägt keine, so braucht es ≥ 4 Kopplungen = so viele wie Koeffizienten ⇒ D/B frei.

Konkret: ungerade Formen, die **beide** (C und D) tragen, sind nur c7/c9 (D/C=−1/6) und c11
(D/C=+1/6). Beobachtet ist D/C=−14,9. Eine 3-Kopplungs-Basis (2 gerade + 1 ungerade) fixiert D/C
auf den Wert dieser einen Form → Test, ob das mit den Daten verträglich ist.

## Entscheidungskriterium (vorab)

- **(K1) D/B vorhergesagt**, wenn eine Basis mit ≤ 3 Kopplungen alle vier Massen innerhalb der
  Fehler trifft (χ² akzeptabel, p > 0,05). Dann D/B = struktureller Wert, Vergleich mit 1,0085.
- **(K2) D/B frei**, wenn die volle Abbildung Rang 4 hat **und** jede ≤ 3-Kopplungs-Basis
  ausgeschlossen ist (χ² groß). Dann ist der ~0,9-%-Rest ein **Eingabewert**: die Quark-Yukawas
  bleiben in diesem Rahmen frei; kein Struktur-, Symmetrie-, Grad- oder Holomorphie-Argument legt
  sie fest.

**Erwartung** (aus H197-Rang 2 und D/C=−14,9, nicht Teil des blinden Teils B): voraussichtlich
**(K2)** — D/B frei. Der analytische Teil (Rang) ist **nicht blind**; der Basis-Test ist blind.
Dann ist die Konsequenz eine **Bilanz/Weggabelung für den Autor**: der chirale/holomorphe Strang
ist durchgerechnet, alle Bausteine identifiziert (Grad-5-gerade + Grad-4-ungerade Invarianten,
exakte Strukturkoeffizienten), aber die Kopplungen sind frei. Ein weiterer Schritt im selben
Rahmen bringt nichts Neues; es braucht eine **neue Eingabe** (ein Prinzip, das die Kopplungen
bindet — z. B. Kopplung an den Lepton-Sektor oder an δ). Das lege ich dem Autor vor.

## Rechenwerkzeug

- numpy (Rang der Abbildung, geschachtelte χ²-Fits der Teil-Basen) + sympy (exakte Strukturmatrix).
- Wolfram Language als unabhängige Kontrolle des Rangs und der besten ≤ 3-Kopplungs-χ².
- Qiskit nicht einschlägig.

## Festhalten

Werkzeugwahl, geprüfte Basen, erste Abweichung, offene Voraussetzungen in die Ergebnis-Notiz.
Symbolische Nullreste, Rückgabewerte, Warnungen getrennt. Rang-Teil nicht blind, Basis-Test blind.
