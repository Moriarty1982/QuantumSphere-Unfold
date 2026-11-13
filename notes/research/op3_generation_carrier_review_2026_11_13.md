# Weg C: Sind die Generationen zyklisch gekoppelte gleiche Kopien?

13. November 2026. Autorenentscheidung „C“: die Platzstruktur selbst
prüfen. Quellenprüfung mit einer kleinen analytischen und numerischen
Erkundung, nicht blind. Kein Hypothesentest, keine neue H-/k-Nummer, kein
MMA-Beleg, keine Änderung offener Guards. Einordnung T5/T7 (Träger), T8
(Massen), OP3/OP4.

## Übersehenes Vorwissen (Korrektur zu den beiden Kopplungsnotizen)

Die Notizen op3_rho_odd_coupling_2026_11_12.md und
op3_dixon_slot_coupling_2026_11_13.md haben behauptet, zu einer
Platzkopplung über die Trialitätsform gebe es keinen Vorbefund. Das war
falsch. Einschlägig und dort nicht genannt:

- **v4.9.0-r53 (H37):** Kopplung zweier Generationen über t mit einem
  Higgs-Wert im dritten Platz, T(v) reell symmetrisch, dazu die Norm als
  Diagonalterm. Ergebnis: t allein ist verboten (spurfrei, also
  m_3 = m_1 + m_2); Norm plus t gibt keine Quarkmischung; die Lesart
  H gegen H-Schlange der beiden Formen ist widerlegt (H37c).
- **r47, r50, r52, r54:** Generationenmaske aus der trialitäts-kovarianten
  Chiralität (diag(0,-2,-1) für Quarks, diag(0,0,-3) für Leptonen) mit
  zirkulanten Kopplungen; als schwache Störung und in den exakten Formen
  K und S an der Mischung widerlegt; mit einem epsilon je Sektor ein Fit.
- **r55–r60:** Auslesung je Teilchenart über Untergruppen von A_4 (Z_3
  für Dirac-Sektoren, Z_2 für Neutrinos), bekanntes TM2-Muster; mit der
  Maske als Korrektur und epsilon = artanh(beta_sym) verträglich, nicht
  blind; offene Vorhersagen H42, H46.
- **r56:** die Einstellungen (Brannen-Größen je Sektor) zeigen keine
  Struktur jenseits des Zufalls; |b|/|a| ≈ 1 bei Quarks ist eine
  Eigenschaft hierarchischer Spektren.
- **12.11.:** op3_generation_embedding_gate, op3_triality_carrier_gate,
  op3_dixon_gram_bridge, op3_gram_torus_bound, op3_triality_mass_bridge.

Was die beiden Kopplungsnotizen darüber hinaus enthalten, bleibt gültig:
der chirale, komplexe Anteil der Kopplung (r53 nahm T(v) reell
symmetrisch), die Sektorformel mit den Idempotenten, die Rolle der
Hyperladung für den Rückweg. Ihre Einordnung als „neu“ war zu stark.

## Die vier vorhandenen Träger, mit heutigem Wissen

| Träger | Quelle | Stand |
|---|---|---|
| Farbtriplett e_4, e_5, e_6 | Kern (thm:three-generations) | ausgeschieden: unter Farbinvarianz ist die Kompression skalar (12.11.) |
| Quaternionen-Richtungen i, j, k mit Gram-Labels | r33 | ausgeschieden als Generationenlabel, siehe unten (neu) |
| Hopf-Träger (ab)c = 1 mit H18-Gesetz | r15, r33 | K <= 1/2 auf dem farbfesten Torus (12.11.) |
| Drei gleiche lineare Kopien, zyklisch gekoppelt (Modell I) | r37, r45 | widerspruchsfrei, aber ohne Vorhersage: siehe unten |

### Neu: Die Gram-Labels aus r33 sind nicht ladungsinvariant

r33 legt die drei Plätze in die Quaternionen-Richtungen,
E(x) = i⊗x_1 + j⊗x_2 + k⊗x_3, und liest
mu_i = 2(|x_j|²|x_k|² - <x_j,x_k>²) aus. Seit r40–r43 ist die
Rechtsmultiplikation in H der schwache Isospin, und Q_em enthält T_3.
Vorausgesetzt ist, dass der Quaternionenfaktor von r33 derselbe ist.

- Die Label-Matrix N_ij = sum (A_i)(A_j) ist N = 2 adj(S) mit der
  Gram-Matrix S der drei Plätze; mu_i ist ihre Diagonale.
- Unter Lorentz-Drehungen und Boosts sind die mu_i invariant (wie in r33).
- Unter der ungebrochenen elektrischen Ladung drehen sich die Richtungen
  i und j ineinander, k mischt mit 1. mu_1 und mu_2 ändern sich, mu_3
  nicht. Invariant sind nur die Eigenwerte von N.
- Unter schwachem SU(2) und Hyperladung sind auch die Eigenwerte nicht
  invariant.

Die drei Richtungen i, j, k sind im heutigen Companion also die
Komponenten (geladen, geladen, neutral) des Isospins und keine drei
Generationen. Dazu passt der Befund der Dixon-Notiz, dass nur e_3 im
H-Faktor neutral koppelt. Zwei der drei „Massen“ wären unter einer
elektromagnetischen Eichtransformation nicht fest. Die ladungsinvariante
Fassung, die Eigenwerte von N, gibt auf der farbfesten Ebene span(1, e_7)
stets (0, 0, m): Drei Vektoren einer Ebene haben eine Gram-Matrix vom Rang
höchstens zwei.

### Modell I: was feststeht

- Symmetrie legt die Kopplungsmatrix nicht fest (r44.1(e), r45, r56,
  Kommutantenargument vom 12.11.).
- t allein ist verboten (r53); der Diagonalterm ist nötig.
- Diese Sitzung: Der rho-ungerade Anteil existiert, hängt an e_7 und e_3,
  die Hyperladung erlaubt den Rückweg nur über das konjugierte Element,
  und bei einem Dublett trägt das Element keine Phase. Phase und
  Verhältnis |b|/a sind freie Kopplungskonstanten.
- Für die Mischung muss tau gebrochen werden (r46); die Maske leistet das
  nur als Fit (r50–r54), die A_4-Auslesung als bekanntes Muster (r55).

## Antwort auf C

Im heutigen Companion gibt es keinen Träger, der die Zahl drei und die
Massen zugleich liefert:

1. Zwei ältere Träger (Farbtriplett, Quaternionen-Richtungen) scheiden
   aus, weil ihre drei Einträge eine Eichquantenzahl tragen (Farbe bzw.
   Isospin und Ladung). Eine Generation ist aber gerade eine Wiederholung
   bei gleichen Quantenzahlen.
2. Der Hopf-Träger mit dem H18-Gesetz erreicht Koide nicht.
3. Modell I ist die einzige widerspruchsfreie Lesart. Dort sind die
   Generationen ein Vielfachheitsraum, und die Struktur sagt über seine
   Kopplungen nichts aus, was nicht eingesetzt wird.

„Zyklisch gekoppelte gleiche Kopien“ ist also weder widerlegt noch
gestützt: Es ist die Lesart, die übrig bleibt, wenn man die Wiederholung
hinzunimmt, statt sie herzuleiten. Die Brannen-Form folgt aus ihr nur als
Form; die Zahlen der Koide-Relation folgen nicht. Was fehlt, ist kein
weiterer Kopplungsansatz, sondern ein Grund für die Wiederholung selbst:
ein nativer Mehrfachraum gleicher Quantenzahlen (die Frage der
embedding-gate-Notiz) oder eine eichinvariante Dreifachauslesung einer
Konfiguration. Gesamtbild T7 nennt dieselbe Lücke („ein Verbot einer
vierten Generation fehlt“).

Weder Koide 2/3 noch Phase oder Spektrum sind hergeleitet. OP3/OP4 bleiben
offen; OP1–OP5, C5, C6/T2 unverändert. I1–I4: kein neuer Auslöser.

## Mögliche nächste Schritte (Autorentscheidung)

- Eichinvariante Dreifachauslesung: Welche Funktionen einer
  Konfiguration in O³ sind unter Farbe, Q_em und Lorentz invariant und
  liefern drei Werte? Die Eigenwerte von adj(S) sind ein Beispiel;
  farbfest geben sie (0, 0, m).
- Statusvermerke in einer neuen Runde: r33-Labels (Ladung), die älteren
  Koide-Stellen aus op3_phase_source_search, thm:three-generations.
- Die Linie ablegen und bei den offenen Vorhersagen bleiben (H15, H42,
  H46, H96).

## Selbstprüfung

op3_generation_carrier_review_2026_11_13.py: N = 2 adj(S) (Fehler 1e-14);
Labels und Invarianten von N unter Lorentz-Drehung, Boost, Q_em,
schwachem T'_1, T'_3 und Y/2 (Zahlen in der Ausgabe); Q_em dreht i und j
ineinander; farbfeste Ebene gibt Eigenwerte (0, 0, m). Gelesen: r33 über
op3_dixon_gram_bridge, r47, r50, r52–r60 (Urteile), r53 vollständig, die
fünf Notizen vom 12.11. in den genannten Teilen. Der Quaternionenfaktor
von r33 wurde nicht gesondert mit dem von r40 abgeglichen; die Aussage
zur Ladung steht unter dieser Voraussetzung.
