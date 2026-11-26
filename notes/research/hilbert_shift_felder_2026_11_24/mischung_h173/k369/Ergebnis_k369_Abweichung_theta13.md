# Erkundung k369: Abweichung bei θ₁₃ beziffern und Herkunft eingrenzen (26.11.2026)

**Status: Erkundung, nicht blind.** Keine Vorab-Notiz, kein Entscheidungskriterium. Die Messwerte und das Ergebnis von H173 waren vor der Rechnung bekannt.
Auftrag des Autors: „berechne die abweichung und schau nach woher die kommen könnte“. Einordnung: OP3/OP4, Strang 3 (Mischung), Fortsetzung von H173 (k368).

Werkzeuge: Python (`k369_abweichung.py`, Ausgabe `k369_out.txt`), Wolfram zur Gegenrechnung der Teile 1 bis 3 (`k369b_exakt.wl`, Ausgabe `k369b_out.txt`).
Qiskit ist ungeeignet (keine Schaltung). Teile 4 und 5 sind nur numerisch in Python gerechnet.

## 1. Die Abweichung in Zahlen

| Größe | Ein-Feld-Form (H173) | Messung | Verhältnis |
|---|---|---|---|
| sin²θ₁₃ | 0,014263 | 0,02248 ± 0,00056 | 1,576 ± 0,039 (−14,7σ) |
| Amplitude \|U_e3\| | 0,11943 | 0,14993 ± 0,00187 | 1,255 |
| Drehwinkel φ | 11,94° | 15,05° ± 0,19° | 1,261 ± 0,016 |
| Versatz x der Phase | 0,039577 (geladene Leptonen) | 0,064887 ± 0,001798 (aus θ₁₃) | 1,640 ± 0,045 |

Der Kern: In der Ein-Feld-Form hängt θ₁₃ nur am Versatz x = π/6 − δ_ν (für kleine x: sin²θ₁₃ ≈ 2x/(3√3)). Die Mischung verlangt
x_th = 0,0649. Die Massen verlangen weniger: x = 0,0396 aus den geladenen Leptonen, x_R = 0,0434 ± 0,0021 aus dem Verhältnis R der Neutrino-Massendifferenzen.
x_th − x_R = 0,0215 (7,7σ). **Die Mischung braucht das 1,5-fache (gegen x_R) bis 1,64-fache (gegen x) des Versatzes, den die Massen hergeben.**
Eine einzige Phase kann nicht beides tragen.

Nebenbefund: Die TM1-Beziehung gibt beim gemessenen θ₁₃ sin²θ₁₂ = 0,3180 (JUNO +2,25σ, NuFIT +1,37σ). Jede Reparatur, die TM1 behält, erbt diese Spannung.

## 2. Woher kann die Abweichung kommen? Vier Kandidaten

Jeder Kandidat gibt genau eine Annahme von H173 auf. Keiner ist hergeleitet; die Zahlen sagen nur, wie groß die jeweilige Änderung sein müsste.

**(a) Koide-Wert der Neutrinos (ρ frei).** Exakt (Wolfram, Nullrest): tan² 2φ = 3 tan²(δ_ν + 2π/3) − 1 hängt nicht von ρ ab. θ₁₃ legt dann δ_ν fest und
R legt ρ fest: ρ = 0,9423 ± 0,0072, also K_ν = 0,6293 statt ⅔ (Abweichung −0,037 ± 0,005). Massen 0,12 / 8,68 / 50,09 meV, Summe 58,9 meV.
Preis: K = ⅔ gilt für Neutrinos nicht mehr, und ρ ist eine neue freie Zahl für eine Messgröße. TM1 bleibt.

**(b) Ungleiche Diagonale (K = ⅔ bleibt).** Nötig ist d − f = +0,048 (x aus den Leptonen) oder +0,041 (x_R), also 4 bis 5 % der Diagonale.
Preis: Das ist genau die Bedingung, die H173 gesetzt hat (Ein-Feld-Form). Wieder eine freie Zahl für eine Messgröße. TM1 bleibt.

**(c) Maske mit anderem ε.** Mit dem postulierten ε = artanh β_sym = 0,6175 ist die Maske weit weg (χ² ≈ 11 000, H173 d). Ein kleines ε ≈ 0,02 bis 0,03
würde passen (χ² = 6,1 bei ε = 0,03 mit x; 7,5 bei ε = 0,02 mit x_R; Raster nur in Schritten von 0,01). Preis: ε ist durch das Zählpostulat festgelegt;
ein zweites, kleines ε hat im Rahmen bisher keinen Platz. Das ist deshalb kein Ausweg, sondern nur eine Größenangabe.

**(d) Kleine Drehung der geladenen Leptonen (e–μ), ℤ₃ leicht gebrochen.** Der kleinste Winkel, der θ₁₃ erreicht, ist 0,044 (x) bzw. 0,037 (x_R).
Beste Anpassung mit freier Phase: θ_e = 0,0516 (x) bzw. 0,0451 (x_R), χ² = 2,3 bzw. 2,4 bei drei Messgrößen und zwei Parametern; dabei
sin²θ₁₃ = 0,0225, sin²θ₁₂ = 0,3036, sin²θ₂₃ = 0,496, sin δ = ±0,993. Der Rest-χ² stammt fast ganz aus θ₂₃ (+1,5σ), das sich kaum bewegt.
Größenvergleich: √(m_e/m_μ) = 0,0695. Mit genau diesem Winkel und passender Phase für θ₁₃ kommt sin²θ₁₂ = 0,2844 (JUNO −3,0σ) heraus; der Wert passt also nicht.
Preis: zwei neue Zahlen (Winkel, Phase) für effektiv zwei Messgrößen; die Anpassung ist deshalb kein Beleg. TM1 wird aufgegeben.

## 3. Was die Kandidaten unterscheidet

- (a) und (b) behalten TM1: sin²θ₁₂ = 0,318 beim gemessenen θ₁₃, |sin δ| = 1, sin²θ₂₃ = ½. Wird der JUNO-Wert 0,3036 bei kleinerem Fehler bestätigt, fallen beide.
- (d) löst die θ₁₂-Spannung mit, verlangt aber |sin δ| ≈ 0,993 statt 1 und sin²θ₂₃ ≈ 0,496; das ist mit heutigen Daten nicht von TM1 zu trennen.
- (a) sagt zusätzlich eine leichteste Masse von 0,12 meV und eine Summe von 58,9 meV; das liegt am unteren Rand dessen, was für normale Ordnung möglich ist,
  und unterscheidet sich kaum vom K = ⅔-Fall.

## 4. Bilanz der Setzungen

Gesetzt (unverändert aus H173): Gruppe und Darstellung aus k262, Majorana-Neutrinos, Ein-Feld-Form, Brannen-Spektrum mit K = ⅔, Zuordnung der Eigenwerte.
Hergeleitet: Die Abweichung ist eine Lücke im Versatz, Faktor 1,5 bis 1,64, und sie ist unabhängig vom Koide-Wert der Neutrinos (exakt).
Gewandert: Die offene Wahl sitzt jetzt in genau einer von vier Stellen (ρ, Diagonale, zweites ε, Drehung der geladenen Leptonen). Welche, ist offen.

## 5. Grenzen

- Nicht blind; alle vier Kandidaten sind nachträglich an die Messung angepasst. Jeder hat mindestens so viele freie Zahlen wie erklärte Messgrößen.
- Vier Kandidaten wurden nebeneinander probiert (Mehrfachvergleich). Dass (d) am besten passt, ist deshalb kein Hinweis darauf, dass (d) richtig ist.
- Es wurde bewusst nicht nach „schönen“ Zahlen für 1,5 oder 1,64 gesucht.
- Der Materie-Frame ist berücksichtigt, soweit Variante A der Maske ihn abbildet (H173 d, Teil 4); andere Übertragungen sind nicht geprüft.
- OP3 und OP4 bleiben offen. Guards unverändert.

## 6. Was daraus für den nächsten Schritt folgt (nicht begonnen)

- Die Eigenvektoren einer Matrix ändern sich nicht, wenn man sie quadriert oder die Wurzel zieht. Ob die Ein-Feld-Form für das Feld (√m) oder für die Masse gilt,
  ändert die Mischung also nicht. Eine Reparatur muss die Form selbst ändern (b, d) oder die Seite der geladenen Leptonen.
- Die geladenen Leptonen sind im Aufbau zirkulant (ℤ₃). Eine zirkulante Matrix wird für jede Phase δ von derselben Fourier-Matrix diagonalisiert; ihr eigener
  Versatz x erzeugt deshalb keine Drehung. Kandidat (d) verlangt einen Term, der ℤ₃ bricht, in der Größe 0,04 bis 0,05. Ein solcher Term ist bisher nirgends hergeleitet.
- Ein Test mit Vorab-Notiz (H174) wäre erst sinnvoll, wenn eine der vier Stellen aus der Algebra eine Zahl bekommt.
