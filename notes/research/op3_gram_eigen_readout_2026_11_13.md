# Erkundung: eichinvariante Dreifachauslesung als Eigenwerte der Platz-Gram-Matrix

13. November 2026. Auftrag „weiter“ nach Weg C: untersuchen, welche
Auslesung einer Konfiguration dreier Plätze eichinvariant ist und drei
Werte liefert. Analytische Erkundung mit numerischer Selbstprüfung, nicht
blind. Kein natives Massengesetz, kein Hypothesentest, keine neue
H-/k-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung
T5/T7 (Träger), T8 (Massen), OP3.

## Vorwissen geprüft

- v4.8.0-r10.1: jedes Tripel hat die Brannen-Form (Mittel, Radius, Phase).
- v4.8.0-r12.1: v_0 v_1 v_2 = t³(1 - 3r²/2 + r³ cos(3 delta)/sqrt2).
- v4.9.0-r53.1(b): das Spektrum von alpha·1 + T(v) hängt nur von alpha,
  sum v_k² und v_1 v_2 v_3 ab; als Massenmatrix mit Mischung getestet
  (Quarks passen nicht, Leptonen nur bei ausgeschlossenen
  Neutrinomassen).
- r33/H18 und op3_gram_torus_bound_2026_11_12.md: Diagonal-Labels mu_i
  mit m = kappa sqrt(mu) geben auf dem farbfesten Torus K <= 1/2.
- sec:v4110-koide-overlap: Mittelung phasenverschobener Präparationen,
  K = (1 + |Z|²)/3, zulässiger Bogen [-pi/12, pi/12].
- op3_generation_carrier_review_2026_11_13.md: die mu_i sind nicht
  ladungsinvariant, die Eigenwerte schon.
- `v480:hc-mass-triole-bound` (Nullsummenvektoren, anderes Massengesetz)
  wurde nicht verglichen.

## Auslesung

Für drei Plätze x_1, x_2, x_3 sei S_ab = <x_a, x_b> die Gram-Matrix. Ihre
Eigenwerte hängen von keiner Platzbasis ab und sind invariant unter jeder
Wirkung, die auf allen Plätzen gleich und unitär ist. Für drei Zustände in
C⊗H⊗O mit dem hermiteschen Skalarprodukt gilt das für Lorentz-Drehungen,
Q_em, schwaches SU(2), Hyperladung und Farbe (geprüft), nicht für Boosts.
Eine Massenzuordnung der Eigenwerte ist eine Annahme, hier
sqrt(m_k) proportional s_k.

## Ergebnis

1. **Geschlossene Form.** Für drei Einheitsvektoren mit Überlappungen
   c_12, c_13, c_23 sind die Eigenwerte

       s_k = 1 + 2 rho cos(theta + 2 pi k/3),
       rho² = (c_12² + c_13² + c_23²)/3,   cos(3 theta) = c_12 c_13 c_23 / rho³,

   und det S = 1 - 3 rho² + 2 rho³ cos(3 theta). Das ist r53.1(b) mit
   alpha = 1 und r12.1, gelesen als Gram-Matrix.
2. **Koide als Überlappung.** K = sum s_k²/(sum s_k)² = (1 + 2 rho²)/3.
   Koide 2/3 gilt genau bei mittlerer quadratischer Überlappung 1/2.
3. **Der Bogen folgt aus der Positivität.** Bei rho² = 1/2 ist
   det S = -1/2 + cos(3 theta)/sqrt2 >= 0 genau für |theta| <= pi/12, der
   Bogen aus dem v4.11-Abschnitt. Der Rand theta = pi/12 sind drei Plätze
   in einer Ebene (Rang 2) mit Eigenwerten (0, 0,634, 2,366), also einem
   masselosen leichtesten Zustand.
4. **Zahl der Massen = Rang.** Die Zahl nichtverschwindender Eigenwerte
   ist die Dimension, die die drei Plätze aufspannen. Auf der farbfesten
   Ebene span(1, e_7) ist ein Eigenwert immer null. Drei parallele Plätze
   (gleicher Zustand in jedem Platz) geben (3, 0, 0).
5. **Mittelwert.** Über zufällige Einheitsvektoren im R^n ist das Mittel
   von K genau (1 + 2/n)/3: 2/3 für n = 2, 1/2 für n = 4, 5/12 für n = 8.
   Auf dem farbfesten Hopf-Torus von r15 (Phasen mit Summe null) liegt K
   zwischen 1/2 und 1, und das Mittel über den Torus ist genau 2/3. Auf
   dem allgemeinen Träger (ab)c = 1 liegt K zwischen 1/3 und etwa 0,95,
   Mittel 5/12.
6. **Unterschied zur H18-Auslesung.** Dieselben Konfigurationen, die mit
   den Diagonal-Labels K <= 1/2 geben, geben mit den Eigenwerten
   K >= 1/2. Der Ausschluss vom 12.11. gilt für das H18-Gesetz, nicht für
   die ladungsinvariante Auslesung.

Nachträglich, nicht blind: Liest man die geladenen Leptonen so, ist
rho² = 0,499991 und det S = 0,0557; die drei Plätze wären fast, aber
nicht ganz koplanar (theta = 0,2222 gegen den Rand 0,2618). Am Rand wäre
m_mu/m_tau = 0,0718 gegen gemessen 0,0595.

## Bewertung

- Die Eigenwert-Auslesung ist die naheliegende eichinvariante Fassung von
  „drei Auslesungen einer Konfiguration“. Sie braucht weder tau noch rho
  als Symmetrie der Konfiguration; die Phase kommt aus dem Dreierprodukt
  der Überlappungen und ist rho-gerade.
- Koide wird damit zu einer Aussage über die Konfiguration: mittlere
  quadratische Überlappung 1/2. In einer reellen Ebene ist das der
  Mittelwert über alle Richtungen. Das ist ein Mittel von K über
  Konfigurationen, keine Eigenschaft einer einzelnen Konfiguration und
  kein Mittel der Massen; ob eine Auslesung so mittelt, ist offen. Die
  Zahl 2/3 ist deshalb nicht hergeleitet, und der Fund kann Zufall der
  Dimension zwei sein (Vorsicht Numerologie).
- Die farbfeste Ebene gibt genau einen masselosen Zustand. Eine
  Elektronmasse verlangt eine dritte Richtung, die farbneutral nicht
  vorhanden ist; komplexe Koeffizienten ändern den Rang nicht.
- Offen und nicht nativ: warum Massenwurzeln die Eigenwerte sein sollen,
  was die Konfiguration festlegt, und wie drei Plätze gleicher
  Quantenzahlen linear unabhängig sein können (gleiche Zustände sind
  parallel). Das letzte ist dieselbe Lücke wie in Weg C.
- Als Massenmatrix mit Mischung ist die Form in r53 bereits geprüft und
  gescheitert. Weder Koide 2/3 noch Phase oder Spektrum sind hergeleitet.
  OP3/OP4 bleiben offen; OP1–OP5, C5, C6/T2 unverändert.

## Selbstprüfung

op3_gram_eigen_readout_2026_11_13.py: Formeln für Eigenwerte, K und det an
2000 Zufallstripeln (Fehler 4e-15); Mittelwerte für n = 2, 4, 6, 8 an je
200000 Tripeln (innerhalb des statistischen Fehlers); Bogen und
Randwerte; hermitesche Gram-Eigenwerte unter fünf Erzeugern (invariant
bis 1e-15, Boost ändert sie); Hopf-Träger allgemein und farbfest an je
200000 Punkten. Die Bereichsgrenzen des allgemeinen Trägers sind
Stichprobenwerte, kein Beweis.

## Nachtrag (13.11., ca. 04:30): Bedingung „Überlappung 1/2 auch für Neutrinos“

Autorenentscheidung: als zusätzliche Bedingung die mittlere quadratische
Überlappung 1/2 für beide farbneutralen Sektoren ansetzen. Vor dem
Schreiben einer Vorab-Notiz verlangt die Anleitung die Vorwissen-Suche;
sie hat die Frage als bereits beantwortet gezeigt. **Es wurde keine
H-Nummer vergeben und kein neuer Test gerechnet.**

- **H2 (v4.8.0-r12, Vorab 434c5a8 vom 20.10.2026, Skript k15):** „Jeder
  Kern lichtartig, r = 1“ für alle Leptonen, also K = 2/3 auch für
  Neutrinos. Vorbefund dort: Mit ausschließlich positiven Wurzeln
  erreichen die Neutrinos bei den gemessenen Massendifferenzen höchstens
  K = 0,585 (normale Ordnung, m_1 = 0) bzw. 0,500 (invertiert). K = 2/3
  geht nur mit einer negativen Wurzel; dann normale Ordnung,
  Summe 0,0592 ± 0,0002 eV, verträglich, aber schwach trennend und in der
  Literatur bekannt (Brannen 2006). Status dort: verträglich, als
  Vorhersage festgeschrieben.
- **Folge für die Gram-Lesart (ohne neue Rechnung):** Eigenwerte einer
  Gram-Matrix sind nie negativ. Mit sqrt(m_k) proportional s_k sind alle
  Wurzeln positiv, und die Bedingung rho² = 1/2 ist für die Neutrinos mit
  den bekannten Massendifferenzen nicht erfüllbar: höchstens
  rho² = 0,378 (normale Ordnung) bzw. 0,25 (invertiert). Die Bedingung in
  dieser Lesart scheitert also an bereits bekannten Daten. Das ist kein
  blinder Befund, sondern eine Folge aus H2 (Zahlen dort; die
  Grenzwerte hier mit den H2-Eingaben nachgerechnet).
- **Was bliebe:** Die negative Wurzel von H2 entspräche einem negativen
  Eigenwert, also einer „Gram-Matrix“ zu einem indefiniten Skalarprodukt
  (det S < 0, Phase außerhalb des Bogens). Ob der Companion dafür eine
  native Form hat, ist nicht geprüft; die Zahlen wären dieselben wie in
  H2 und brächten keine neue Vorhersage.

Zuletzt vergebene Hypothese bleibt H98.
