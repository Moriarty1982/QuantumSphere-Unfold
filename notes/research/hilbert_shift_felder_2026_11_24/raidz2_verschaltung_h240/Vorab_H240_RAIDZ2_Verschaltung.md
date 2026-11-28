# Vorab H240 (k456): Zwei RAIDZ2, anders zusammengeschaltet? Verschaltungen und G₂-angepasste Koordinaten

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (20:06): „ok, was wäre wenn wir zwei raidz2 haben die noch anders zusammengeschaltet
sind?“ Anschluss an H239.

## Vorwissen geprüft
- **H239/k455:** Der Code eines Nullteilers C_x = Bild(L_x) hat Rang 12. An der Wand e₈ liegt er generisch (4 + 4), und allgemeine Nullteiler spalten an
  keiner der 6435 Aufteilungen 8 + 8. Basis-Nullteiler spalten an 210 Aufteilungen, aber nur trivial.
- **k455c (nachträglich):** Basis-Nullteiler (e_i ± e_j)/√2 zerfallen in 4 Spiegelpaare und 8 ungeschützte Koordinaten. Bei allgemeinen Nullteilern
  sind e₀ und e₈ ungeschützt. Die Ausfallprofile sind schlechter als bei Zufallscodes.
- **k254, H138:** Aut(𝕊) ⊇ G₂, das diagonal auf beiden Hälften wirkt. G₂ wirkt transitiv auf Paare orthonormaler imaginärer Oktonionen
  (Standardsatz, nicht nachgeprüft).

## Verschaltungen (gesetzt), jeweils als [16, k]-Code
- **V1 gespiegelt:** RAID1 über zwei RAIDZ2. Kapazität 6/16.
- **V2 verschränkt:** zwei RAIDZ2-Gruppen quer zur Wand, also jede Aufteilung 8 + 8. Kapazität 12/16.
- **V3 Produktcode 4 × 4:** Zeilen- und Spaltenparität ergeben Kapazität 9/16. Die Variante nur mit Zeilenparität ist 4 × RAID5 zu je 4, mit Kapazität 12/16.
- **V4 verschachtelt:** RAIDZ2 aus RAIDZ2-Gruppen oder ein verketteter Code. Er ist keine direkte Summe, aber jede Platte ist geschützt (Mindestabstand ≥ 2).

**Werkzeug für alle Direktsummen-Verschaltungen zugleich:** Ein linearer Code zerfällt genau dann über eine Koordinatenaufteilung, wenn sein Matroid
unzusammenhängend ist. Die feinste Zerlegung sind die Zusammenhangskomponenten. Sie werden über die Fundamentalkreise zu einer Basis der
Paritätsprüfmatrix bestimmt. Je Komponente werden Länge n, Dimension k und Mindestabstand d angegeben (Ausfalltoleranz d − 1).

## Teil A (teilweise nicht blind): Standardkoordinaten
- **A1 (nicht blind):** V1 und V3 mit beiden Paritäten scheiden schon an der Kapazität aus (6 bzw. 9 ≠ 12). V2 schied in H239 aus.
- **A2 (blind):** die Komponenten von C_x für Z1 (alle 84 Basis-Diagonalen) und Z2 (200 allgemeine Nullteiler wie in H239).
  Passt eine Verschaltung, also zwei Komponenten [8, 6, 3] oder vier Komponenten [4, 3, 2]?
- **A3 (nicht blind, aus k455c):** Sind Koordinaten ungeschützt (Komponenten der Länge 1 mit k = 1)? Dann scheidet V4 aus, und mit ihm jede
  Verschaltung, die alle Platten schützt.

## Teil B (nicht blind vorhergesagt, numerisch geprüft): G₂-angepasste Koordinaten
Für einen allgemeinen Nullteiler x = (a, b)/√2 wird ein Automorphismus g ∈ G₂ ⊂ Aut(𝕊) gebaut, mit e₁ ↦ a, e₂ ↦ b, e₄ ↦ c, wobei c ein Einheitsvektor
⟂ a, b, ab ist. Diagonal wirkt g auf beide Hälften. Geprüft wird, dass g ein Automorphismus von 𝕊 ist. Dann wird C_x in der Basis g(e_k) beschrieben.
- **Vorhersage (nicht blind):** In angepassten Koordinaten ist jeder allgemeine Nullteiler ein Basis-Nullteiler (e₁ + e₁₀)/√2. Seine Code-Struktur ist
  also für alle gleich: 4 Spiegelpaare und 8 ungeschützte Koordinaten.
- **B2 (blind):** die invariante Beschreibung, ob C_x ⊇ ℍ_x ⊕ ℍ_x·e₈ mit ℍ_x = span{1, a, b, ab}. Ist das 8-dim. Komplement zur Hälfte im Code
  (4-dim) und enthält es den ganzen Kern?

## Zufallskontrolle
200 zufällige [16, 12]-Codes: Komponenten und Mindestabstand.

## Urteil
- **trägt:** In Standard- oder angepassten Koordinaten zerfällt C_x für alle Nullteiler in eine Verschaltung aus zwei RAIDZ2 (V1–V4), mit Toleranz ≥ 2 je
  Gruppe.
- **trägt teilweise:** Es gibt eine feste, für alle Nullteiler gleiche RAID-Verschaltung, aber nicht aus zwei RAIDZ2, oder mit schlechterer Toleranz als
  Zufallscodes.
- **widerlegt:** Keine feste Verschaltung; die Codes sind zusammenhängend und von Nullteiler zu Nullteiler verschieden.

## Werkzeuge
Python k456 (Komponenten, Mindestabstände, G₂-Rahmen, Zufallskontrolle), Wolfram k456b (exakt für einen rationalen Nullteiler: B2). Qiskit nicht einschlägig.
