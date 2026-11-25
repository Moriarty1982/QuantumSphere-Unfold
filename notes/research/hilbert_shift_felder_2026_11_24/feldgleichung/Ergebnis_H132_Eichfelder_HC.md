# Ergebnis H132: Auf der HC-Richtung bleibt kein Eichfeld masselos (Test k298, 25.11.2026)

**Urteil nach den vorab festgelegten Kriterien:** H132 ist **widerlegt**. K-a (masseloses Eichfeld) ist widerlegt, K-b (Verhältnis nur aus β_sym) trägt teilweise.
Das entspricht der Vorhersage der Vorab-Notiz, und der Überschlag dort stimmte bis auf das Vorzeichen der Nebendiagonale, das am Ergebnis nichts ändert.
Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H132_Eichfelder_HC_Richtung.md` (Commit 596cc91, vor dem ersten Skriptlauf).
**Teilweise nicht blind**, wie dort offengelegt: Der Überschlag im Kopf legte das Ergebnis weitgehend fest. Offen waren die Faktoren, die Formel für die Masse
des leichten Felds und der Vergleich mit SU(2).

Werkzeuge: Python mit sympy (exakt). Wolfram Language unabhängig mit Quaternionen als 2×2-Matrizen und der Norm als Determinante (k298b). Alle Größen stimmen überein.
Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

## Zahlen
Vakuum ψ₀ = f(cos θ + sin θ·j), tan θ = μ = β_sym² (eingesetzt). A = f²cos²θ, B = f²sin²θ.

**Stufe A, U(1) links × U(1) rechts (die Symmetrie des HC-Potentials):**
- Massenmatrix in (L, R): [[g_L²f², −g_Lg_R f² cos 2θ], [−g_Lg_R f² cos 2θ, g_R²f²]].
- **K-a:** Determinante = 4g_L²g_R²·A·B. Ungleich null, sobald Vorstufe und Anhang beide da sind. **Widerlegt.**
- **K-b:** m₋²/m₊² hängt allgemein an g_R/g_L (Beispiel cos 2θ = ½: 0,162 für g_R = 2g_L gegen 0,333 für g_R = g_L). Für g_L = g_R = g ist es genau μ²:
  m₊² = 2g²f²/(1 + μ²), m₋² = 2g²f²μ²/(1 + μ²), also **m₋/m₊ = μ = β_sym² = 0,3018**. **Trägt teilweise.**
- Für kleines μ: m₋² = 4e²μ²f² + O(μ⁴) mit e = g_Lg_R/√(g_L² + g_R²). Das leichte Feld ist das, das ohne Anhang masselos wäre; der Anhang gibt ihm eine Masse
  proportional zu seiner Amplitude.
- Ohne Anhang (θ = 0) ist die Kombination g_R·L + g_L·R masselos (unter ihr ist ψ₁ neutral).

**Stufe B, SU(2) links × U(1) rechts (k291 Punkt 6) auf demselben Vakuum:**
- Massenquadrate g²f²/4 (zweimal), (g² + g′²)f²/4 und **0**, unabhängig von θ. Die masselose Kombination dreht mit θ.
- **Aber:** Das HC-Potential ist nicht SU(2)-invariant. Unter einer Linksdrehung um j oder k ändert es sich um −4η(1 + μ²)(…)(μ²A − B), was nur auf der HC-Richtung
  selbst verschwindet, nicht in ihrer Umgebung. Die Eichung von SU(2) links und das HC-Potential vertragen sich nicht.

**Stufe C (ohne Kriterium), Schleifen-Skala mit Eichfeldern, g_L = g_R = g:**
m_s² = [16η²μ⁴(1 + μ²)² + 3g⁴(1 + μ⁴)]/(2π²(1 + μ²)²)·f². Mit μ = β_sym²: m_s² = (0,00672η² + 0,1287g⁴)·f².
Für g² ≫ ημ² dominieren die Eichfelder die Größenmode, wie bei Coleman–Weinberg.

## Was daraus folgt
1. **„Licht bleibt masselos“ und „HC wirkt im Anhang“ schließen sich auch mit Eichfeldern aus**, solange man nur die Symmetrie eicht, die das HC-Potential hat.
   Das ist dieselbe Spannung wie in H129 (κ > 0 macht die Vorstufe massiv), jetzt für die Eichfelder.
2. **Masseloses Licht braucht SU(2).** Mit SU(2) links gibt es immer ein masseloses Feld, auf jeder Richtung. Dann darf das Potential aber nicht vom Winkel zwischen
   Vorstufe und Anhang abhängen, das HC-Potential η(B − μ²A)² ist also verboten. Wer beides will, braucht eine andere Übersetzung des HC (k297 Grenzen:
   die quadratische Strafe war eine Setzung) oder einen Weg, auf dem der HC die SU(2) erst unterhalb einer Skala bricht.
3. **Die Zahl β_sym taucht als Massenverhältnis auf, wenn die Kopplungen gleich sind.** m₋/m₊ = β_sym² = 0,3018 ist eine exakte Folge des Ansatzes mit g_L = g_R.
   Eine Zuordnung zu gemessenen Massen ist nicht geprüft und wird hier nicht behauptet; gleiche Kopplungen links und rechts sind selbst eine Setzung.

## Grenzen
- Klassische Massenmatrix; Schleifen nur in Stufe C. Nur ℂ → ℍ, ohne Fermionen.
- Die Form des HC-Potentials ist eine Setzung (k297). β_sym ist eingesetzt (OP1 offen). Welche Kombination „Licht“ ist, ist eine Lesart.
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Möglicher nächster Schritt
Eine Übersetzung des HC, die mit SU(2) links verträglich ist: Der HC als Bedingung an den Strom J = ψ̄∂ψ statt an die Norm, oder als Projektion, die nur auf der
Rechtsseite wirkt. Dann ließe sich prüfen, ob masseloses Licht und die HC-Form zusammen gehen. Das ist nicht gerechnet.

## Dateien
`k298_test_h132.py` (`k298_out.txt`), `k298b_gegenprobe.wl` (`k298b_out.txt`).
