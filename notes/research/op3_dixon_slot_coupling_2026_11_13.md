# Erkundung: Platzkopplung auf dem vollen Dixon-Raum, Leptonen und Quarks

13. November 2026. Autorenauftrag: den Lepton-Fall auf C⊗H⊗O versuchen
und den vollen Dixon-Raum auch auf die Quarks anwenden. Strukturerkundung
ohne Entscheidungskriterium, nicht blind, kein Hypothesentest, keine neue
H-/k-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung
T8/T13, OP3/OP4.

## Vorwissen geprüft

op3_rho_odd_coupling_2026_11_12.md (nur Oktonionenfaktor: Quarks
Brannen-Form, Leptonen null); r41–r45, r49 (Rollen des H-Faktors,
Chiralität, e_7 trägt B-L), k85 (Zustände und Ladungen auf C⊗H⊗O),
r44.1(e), r46.1; v4.8.0-r11 (Phasen der drei geladenen Tripel bei M_Z).
Suche nach einer Platzkopplung über das Dixon-Produkt: kein Vorbefund.

## Konstruktion (Kandidat, kein natives Gesetz)

V = C⊗H⊗O mit dem Dixon-Produkt, <.> die Komponente an 1⊗1. Für ein
festes Element h des dritten Platzes, ein Feld psi im Bild von C_ch
(Dubletts) und ein Feld chi im Kern (Singuletts):

    F_0(x,y,h) = <(x y) h>,
    F_a(x,y,h) = <(x~ y) h>   (~ nur Quaternionen-Konjugation),
    F_b(x,y,h) = <(x^ y) h>   (^ Quaternionen- und Oktonionen-Konjugation),

Platzmatrix M_s = a_s + alpha_s P + beta_s P² mit alpha_s = F(psi,chi,h),
beta_s = F(chi,psi,h) für die Sektoren s = e, nu, u, d (Zustände wie in
k85 über Q_em, Q_8 und C_ch bestimmt). Lorentz-Drehungen wirken durch
Linksmultiplikation in H; F_a und F_b sind darunter invariant, wenn h
nicht mitgedreht wird.

## Ergebnis

1. **Kein zyklischer Spinor-Term.** Auf H³ gibt es keine trilineare
   Form, die unter gemeinsamer Linksdrehung aller drei Einträge invariant
   ist (Dimension 0). Drei gleichartige Spinor-Plätze lassen sich nicht
   Lorentz-invariant trilinear koppeln; das Element des dritten Platzes
   muss sich anders transformieren (Skalar).
2. **Welche h koppeln.** Nur die vier neutralen Richtungen 1⊗1, 1⊗e_7,
   e_3⊗1, e_3⊗e_7 tragen bei; e_1 und e_2 im H-Faktor tragen Ladung und
   geben null.
3. **Leptonen.** Ohne Oktonionen-Konjugation (F_0, F_a) bleibt die
   Lepton-Kopplung null, wie im Oktonionenfaktor allein. Mit der vollen
   Dixon-Konjugation (F_b) koppeln Leptonen und Quarks gleichartig.
4. **Sektorformel (F_b).** Für h = (a_0 + a_3 e_3)⊗(o_0 + o_7 e_7) gilt
   in jedem Sektor alpha_s = kappa_s J_s mit einer festen invarianten
   Matrix J_s und

       kappa_s = (a_0 + i sigma_s a_3)(o_0 + i lambda_s o_7),
       sigma = +1 für e, d;  -1 für nu, u;
       lambda = +1 für Leptonen;  -1 für Quarks.

   Für reelle Komponenten ist beta_s = conj(alpha_s): Die Platzmatrix ist
   hermitesch und hat Brannen-Form mit der Phase

       theta_s = sigma_s phi_H + lambda_s phi_O,
       phi_H = arctan(a_3/a_0),  phi_O = arctan(o_7/o_0).

   |kappa_s| ist in allen vier Sektoren gleich.
5. **Rho-gerade und rho-ungerade.** Der Platztausch ist die
   Dixon-Konjugation von h. Gerade sind 1⊗1 und e_3⊗e_7, ungerade 1⊗e_7
   und e_3⊗1. Die Phase hat also zwei Quellen: die e_7-Richtung im
   Oktonionenfaktor (wie zuvor) und die e_3-Richtung im
   Quaternionenfaktor (schwacher Isospin).
6. **Spiegelung zwischen Leptonen und Quarks.** Für beliebiges komplexes
   neutrales h gilt beta_e = alpha_u, beta_u = alpha_e, beta_nu = alpha_d,
   beta_d = alpha_nu. Die Platzmatrix der Up-Quarks ist das rho-Bild der
   Platzmatrix der geladenen Leptonen, die der Down-Quarks das rho-Bild
   der Neutrinos. Im hermiteschen Fall heißt das theta_u = -theta_e und
   theta_d = -theta_nu; das Spektrum hängt nur vom Betrag der Phase ab.
7. **Mit nur dem Oktonionenfaktor oder F_a** haben die Quarks dieselbe
   Formel; die Leptonen fallen aus.

## Bewertung

- Auf dem vollen Dixon-Raum gibt es eine tau-invariante Platzkopplung mit
  rho-ungeradem Anteil für Leptonen und Quarks. Sie verlangt die volle
  Dixon-Konjugation am ersten Eintrag; das ist die Form, die für h = 1
  das euklidische Skalarprodukt ergibt.
- Ein festes Verhältnis rho-ungerade zu rho-gerade liefert die Struktur
  nicht: Die beiden Winkel phi_H und phi_O sind frei. Aus vier
  Sektorphasen werden aber zwei Winkel, und die Beträge sind gleich.
- Nachträglich, nicht blind, kein Test: Im hermiteschen Fall mit einem
  gemeinsamen h müssten Up-Quarks und geladene Leptonen denselben
  Phasenbetrag haben. r11 gibt bei M_Z in der Wurzel-Lesart 0,0518 für
  die Up-Quarks gegen 0,2211 für die Leptonen (Down-Quarks 0,1001). Der
  Kandidat in dieser einfachsten Form passt also nicht zu den bekannten
  Massen. Offen bleiben ein je Sektor verschiedenes h, komplexe
  Komponenten (dann nicht hermitesch) und eine andere Lesart der
  Eigenwerte; jede dieser Öffnungen kostet freie Zahlen.
- Die Konstruktion ist ein Kandidat. Dass Massen über das Dixon-Produkt
  mit einem festen dritten Platz entstehen, steht nicht im Companion; der
  Diagonalterm a_s, die Herkunft von h und die Lesart der Eigenwerte sind
  offen. Der Bezug zu den Verbindern aus r44.1(b) ist nicht geprüft.
- Weder Phase noch Koide 2/3 noch ein Spektrum sind hergeleitet. OP3/OP4
  bleiben offen; OP1–OP5, C5, C6/T2 unverändert.

## Was danach bleibt

- Prüfen, ob die F_b-Kopplung mit neutralem h genau die neutralen
  Mitglieder des antilinearen Verbinderblocks aus r44.1(b) trifft
  (Y/2 = ±1/2). Das würde h als Dublett-Richtung festlegen und phi_H an
  die Brechungsrichtung binden.
- Erst mit einer nativen Bedingung an phi_H und phi_O (oder an den
  Diagonalterm) wäre ein vorab festgelegter Test sinnvoll (H99). Die
  Beziehung zwischen Down-Quarks und Neutrinos wäre dabei die einzige
  Aussage, deren Ergebnis noch nicht bekannt ist.

## Selbstprüfung

op3_dixon_slot_coupling_2026_11_13.py: Zustände der vier Sektoren (je
zwei Lepton- und sechs Quarkzustände in Bild und Kern); Koeffizienten für
F_0, F_a, F_b (Reste <= 1e-15); geladene h tragen 1e-15 bei; Sektorformel
(Fehler 3e-17); Spiegelung an 50 zufälligen komplexen h (2e-15);
Dimension 0 der invarianten trilinearen Formen auf H³. Die Zahlen aus r11
wurden übernommen, nicht neu gerechnet.
