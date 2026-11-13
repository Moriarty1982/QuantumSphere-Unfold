# Erkundung: rho-ungerade Platzkopplung aus der Trialitätsform

12./13. November 2026. Autorenauftrag „mach das mal“ zum nächsten Schritt
aus op3_phase_source_search_2026_11_12.md. Strukturerkundung ohne
Entscheidungskriterium, nicht blind, kein Hypothesentest, keine neue
H-/k-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung
T8/T13, OP3/OP4.

## Frage

Welche tau-invariante, rho-ungerade Kopplung der drei Plätze erlaubt die
chirale Struktur, und legt sie ein Verhältnis zu ihrem rho-geraden
Partner fest?

## Vorwissen geprüft

- r44.1(e): hermitesche Platzmatrix M = a + b P + conj(b) P²;
  rho-symmetrisch heißt b reell. Allein aus tau und den Eichsymmetrien
  ist b frei; r45: Stärke der rho-Brechung nicht festgelegt.
- r45.1, k86: Modell I, C_ch = (1 + i L_e7)/2 auf jedem Platz; rho
  bildet C_ch auf die anomale Wahl ab. Modell II scheidet aus.
- r46.1: Readouts aus dem Generationen-Shift vertauschen mit tau und
  bleiben zirkulant. r47: Masken brechen tau (anderer Weg).
- r13 (Assoziator, Farbe und Generation), r15 (Hopf-Träger), r16/r26
  (t in Potentialen), r49 (Achse e_7 trägt B-L).
- Suche nach einer Platzkopplung „t mit festgehaltenem drittem Platz“ in
  sources/ und notes/research: kein Vorbefund gefunden.

## Konstruktion (Kandidat, kein natives Gesetz)

Die einzige trilineare Größe des Companion auf den drei Plätzen ist die
Trialitätsform t(x,y,z) = Re((xy)z). Hält man das Element h des dritten
Platzes fest, koppelt t die beiden anderen Plätze. Wegen der Zyklizität
entsteht für ein linkes Feld u (Bild von C_ch) und ein rechtes Partnerfeld
conj(w) (Kern) die Platzmatrix

    M = a + alpha P + beta P²,
    alpha = t(u, conj w, h),   beta = t(conj w, u, h),

mit einem platzdiagonalen Term a, den t nicht liefert. Der rho-gerade
Anteil ist (alpha+beta)/2, der rho-ungerade (alpha-beta)/2. Gerechnet
wird nur der Oktonionenfaktor von C⊗H⊗O (Konvention r04, Ladung Q_8 wie
in k85); der H-Faktor bleibt außen vor. Farbverträglichkeit verlangt
h in span(1, e_7).

## Ergebnis

1. **Quarks.** Für das Farbtriplett im Bild von C_ch und reelles
   h = h_0 + h_7 e_7 gilt exakt, farbdiagonal,

       alpha = -2 (h_0 - i h_7),   beta = -2 (h_0 + i h_7).

   Die Platzmatrix ist dann von selbst hermitesch und hat genau die
   Brannen-Form mit b = alpha. Der rho-gerade Anteil sitzt an der
   Komponente von h entlang 1, der rho-ungerade an der Komponente entlang
   e_7. Die Brannen-Phase ist bis auf pi der Winkel von h in der Ebene
   (1, e_7); |b|/a = 2|h|/a.
2. **Kein festes Verhältnis.** t legt das Verhältnis h_7/h_0 nicht fest.
   Die gesuchte Zahl wird zur Frage, wo das Element des dritten Platzes
   zwischen 1 und e_7 steht. Für h_7 = 0 gibt es zwei gleiche
   Eigenwerte.
3. **Chirales h.** Für h = 1 ± i e_7 überlebt genau ein Umlaufsinn
   (alpha = -4, beta = 0 oder umgekehrt). Das ist maximale rho-Brechung
   mit nur einer Harmonischen neben a; nach coupling-scale-candidate gilt
   dann K <= 1/2.
4. **Leptonen.** Die Oktonionenanteile aller Leptonzustände liegen in der
   kommutativen Ebene span_C(1, e_7). Dort ist t symmetrisch, h außerhalb
   der Ebene trägt nichts bei, und die sesquilineare Kopplung
   t(l, conj l, h) verschwindet für jedes h, weil
   (1 + i e_7)(1 - i e_7) = 0. Über t entsteht für Leptonen also weder
   ein rho-ungerader noch überhaupt ein Platz-Kopplungsterm: b = 0, drei
   gleiche Eigenwerte. Nicht null ist nur die gleichchirale Größe
   t(l, l, l) = 4, symmetrisch.
5. **Drei Farbtripletts.** Stehen alle drei Einträge im Farbtriplett des
   Bildes, ist t total antisymmetrisch (Betrag 4). Das ist der
   epsilon-Tensor der Farbe, kein Massenterm.

## Bewertung

- Es gibt im Companion eine native tau-invariante, rho-ungerade
  Platzkopplung: die e_7-Komponente des dritten Platzes in der
  Trialitätsform. Sie zeigt in dieselbe Richtung wie Chiralität,
  Assoziator, Q_J und B-L (alle e_7). Ihr rho-gerader Partner ist die
  Komponente entlang 1. Das Verhältnis ist ein Winkel, den die Struktur
  nicht festlegt.
- Der Mechanismus greift nur für farbige Zustände. Für die Leptonen, bei
  denen die Koide-Relation am genauesten gilt, liefert er nichts. Eine
  Lepton-Phase muss daher aus dem H-Faktor, dem Frame-Wechsel oder einer
  anderen Kopplung als t kommen; das ist hier nicht untersucht.
- Die Konstruktion ist ein Kandidat. Dass Massen über t mit einem festen
  dritten Platz entstehen, steht nirgends im Companion; der Diagonalterm
  a, die Lesart der Eigenwerte (Masse oder Wurzel) und die Herkunft von h
  sind offen. Ein Vergleich mit Quarkmassen wurde nicht gemacht.
- Weder Phase noch Koide 2/3 noch ein Spektrum sind hergeleitet. OP3/OP4
  und die Stringfrage bleiben offen; OP1–OP5, C5, C6/T2 unverändert.

## Was danach bleibt

- Für Quarks: Gibt es eine native Bedingung an das Element des dritten
  Platzes (etwa aus dem Hopf-Träger (ab)c = 1 von r15 oder aus der
  Dublett-Richtung von r44.1(b)), die den Winkel in der Ebene (1, e_7)
  festlegt? Das wäre eine vorab festlegbare Aussage (H99).
- Für Leptonen: dieselbe Frage im H-Faktor stellen, also welche
  Platzkopplung die Lepton-Verbinder aus r44.1(b) zulassen, wenn t
  ausfällt.

## Selbstprüfung

op3_rho_odd_coupling_2026_11_12.py (Python, Oktonionenprodukt aus
k69_test_h17.py): Lepton-Ebene (Antisymmetrie 0, Beitrag von h außerhalb
0, sesquilineare Kopplung 0 an 200 zufälligen h, t(l,l,l) = 4);
Quarkformel an 300 zufälligen reellen h (Fehler 3e-15, keine
Lepton-Quark-Mischung); chirales h; Platzmatrix hermitesch und in
Brannen-Form (2e-15), mit h_7 = 0 zwei gleiche Eigenwerte; drei
Farbtripletts total antisymmetrisch. Gelesen: r44, r45, r46, k85, k86.

## Nachtrag (13.11.): übersehenes Vorwissen

Die Angabe „kein Vorbefund“ zur Platzkopplung über die Trialitätsform war
falsch. v4.9.0-r53 (H37) hat eine solche Kopplung mit reell symmetrischem
T(v) und Norm-Diagonalterm bereits getestet (t allein verboten, keine
Quarkmischung, H/H-Schlange-Lesart widerlegt); r47–r60 behandeln Masken
und A_4-Auslesung. Einordnung in op3_generation_carrier_review_2026_11_13.md.
