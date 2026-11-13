# Quellenauftrag: Hat der Companion eine indefinite Form auf den Plätzen?

13. November 2026. Autorenentscheidung: als zusätzliche Bedingung ein
indefinites Skalarprodukt prüfen, damit die negative Wurzel der Neutrinos
aus H2 eine Folge der Signatur wäre. Quellenprüfung mit kleiner
Erkundung, nicht blind; rechnet keine Neutrinomassen. Keine neue
H-/k-Nummer in dieser Notiz, kein MMA-Beleg, keine Änderung offener
Guards. Einordnung T2/T3 (Frames), T8 (Massen), OP3.

## Vorwissen geprüft

def:biquaternion (Kern) mit Statusvermerk; v4.8.0-r06 (Lesart B),
r10.2, r10.3; Konvention F (M, T, P) mit z ↦ iz; v4.10.0-r03 (H94,
gewichtete Norm); r44.1(d) (einziger eichinvarianter Verbinder wirkt auf
nu^c); H2 (Neutrino-Triole, negative Wurzel); r33 und die Notizen vom
12./13.11. Suche in sources/ nach indefinite, signature, Krein, negative
norm, weighted norm, per-kernel, light-like.

## Befund

1. **Kern.** Die Biquaternion-Norm -(ct)² + |z_1|² + |z_2|² + |z_3|² ist
   indefinit zwischen Zeitanteil und Kernen, unter den drei Kernen aber
   positiv. Seit der Revision gilt Lesart B mit N(q) = -t² + s,
   s = z_1² + z_2² + z_3².
2. **Lesart B.** Die einzige quadratische Lorentz-Invariante auf dem
   Kernvektor z = E + iB in C³ ist s (r10.3). Ihr Realteil E² - B² hat
   auf den sechs reellen Richtungen die Signatur (3,3). Die Tachyon-
   Abbildung z ↦ iz kehrt das Vorzeichen um; eine 120°-Triole
   z = c(1, omega, omega²) ist für jedes c ein Nullvektor (r10.2). Eine
   indefinite Form auf den Kernrichtungen ist also nativ, und sie ist die
   einzige, die Boosts respektiert.
3. **Dixon-Raum.** Auf C⊗H⊗O ist die komplex-bilineare Form x^T y
   invariant unter Lorentz-Drehungen und Boosts, Farbe und der
   elektrischen Ladung (Q_em ist i mal eine reelle antisymmetrische
   Matrix). Die hermitesche Form ist unter Boosts nicht invariant. Die
   bilineare Form paart Ladung +q mit -q: Auf Zuständen fester Ladung
   q ≠ 0 verschwindet sie identisch, auf den elektrisch neutralen
   Zuständen (Neutrino und nu^c, vier komplexe Dimensionen) nicht. Das
   passt zu r44.1(d): Nur im neutralen Sektor gibt es einen
   eichinvarianten Term ohne Higgs.
4. **Folge für die Eigenwert-Auslesung.** Mit einer indefiniten Form
   können drei Plätze der Norm +1 einen Raum der Signatur (2,1)
   aufspannen; dann ist ein Eigenwert der Gram-Matrix negativ. Die
   Formeln s_k = 1 + 2 rho cos(theta + 2 pi k/3), K = (1 + 2 rho²)/3 und
   det S = 1 - 3 rho² + 2 rho³ cos(3 theta) gelten unverändert. Bei
   rho² = 1/2 ist ein Eigenwert genau dann negativ, wenn |theta| > pi/12.
   Der Rand des v4.11-Bogens trennt also die beiden Signaturen.
5. **Gewichtete Norm (H94).** Am Urknall-Übergang wechselt die Bosonen-
   Norm von +1 nach -1, die der Fermionen ist -1. Das ist eine weitere
   native indefinite Norm zwischen M- und T-Lesart; ihr Bezug zu den drei
   Plätzen ist nicht hergestellt.

## Bewertung

- Ja: Der Companion hat eine indefinite, vollständig Lorentz-invariante
  Form, und sie steht genau im elektrisch neutralen Sektor zur Verfügung.
  Geladene Leptonen brauchen die hermitesche (Dirac-artige) Paarung mit
  positiven Eigenwerten; für Neutrinos ist die bilineare Form erlaubt,
  und ein negativer Eigenwert ist dort keine Zusatzannahme, sondern eine
  mögliche Signatur.
- Damit ist die negative Wurzel von H2 strukturell einordenbar: geladene
  Leptonen innerhalb des Bogens (Signatur (3,0)), Neutrinos außerhalb
  (Signatur (2,1)).
- Nicht gezeigt ist, dass die Neutrinos die Signatur (2,1) haben müssen,
  dass Massenwurzeln Eigenwerte sind, und was Phase und Überlappung
  festlegt. Zahlen folgen aus dieser Einordnung allein nicht; H2 bleibt
  die einzige festgeschriebene Vorhersage.
- OP3/OP4 bleiben offen; OP1–OP5, C5, C6/T2 unverändert.

## Anschluss

Die Einordnung legt eine Bedingung nahe, die beide Sektoren verbindet:
dieselbe Überlappung und eine Phase, die sich um die halbe Bogenbreite
pi/12 unterscheidet. Sie ist in der Literatur bekannt (Brannen, „Koide
Mass Formula for Neutrinos“). Sie wird als H99 vorab festgelegt, bevor
ihr Wert für das Verhältnis der Massendifferenzen gerechnet wird.

## Selbstprüfung

op3_indefinite_form_2026_11_13.py: Signatur (3,3) von Re s, Triole null;
bilineare Gram-Eigenwerte invariant unter Lorentz-Drehung, Boost und
Q_em (1e-15), nicht unter Y/2; Q_em + Q_em^T = 0; bilineare Gram-Matrix
null auf Zuständen mit Q = -1, nicht null auf neutralen; in Signatur
(2,1) haben drei raumartige Einheitsvektoren stets einen negativen
Eigenwert, und K = (1 + 2 rho²)/3 gilt weiter.
