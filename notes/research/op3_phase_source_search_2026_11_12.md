# Quellensuche: Welche Größe im Companion sieht die Koide-Phase?

12. November 2026 (abends). Autorenauftrag: im Companion suchen und dabei
beachten, dass die Bausteine weiter oben in der Hierarchie meist älter
sind und das heutige Wissen noch nicht haben. Quellenprüfung mit
analytischer, nicht blinder Einordnung. Einordnung T8/T13, OP3/OP4. Kein
natives Gesetz, kein Hypothesentest, keine neue H-/k-Nummer, kein
MMA-Beleg, keine Änderung offener Guards.

## Frage

Aus op3_string_energy_source_search_2026_11_12.md: Gibt es im Companion
eine Größe, die auf dem Brannen-Kreis
v_k = t (1 + sqrt(2) r cos(delta + 2 pi k/3)) von der Phase delta abhängt
und deren Auswahl nicht bei zwei gleichen Massen liegt?

## Nachtrag zum Vorwissen (in der W-b-Notiz übersehen)

Die W-b-Notiz hat die folgenden Vorbefunde nicht genannt. Sie decken
einen großen Teil ihres zweiten Befunds bereits ab:

- v4.8.0-r10.1/r10.2: Brannen-Form als Skalar plus Triole; die
  Invarianten der Lesart B legen weder |c|/t noch arg c fest.
- v4.8.0-r10 (Phase): keiner der vorab festgelegten kanonischen Winkel
  gibt delta_obs = 0,222225.
- v4.8.0-r11 (H1): delta = K/3 bzw. 2/9 widerlegt (Quarks, laufende
  Leptonmassen); gilt nur für Lepton-Polmassen, dort Kalibrierung.
- v4.8.0-r12.1: v_0 v_1 v_2 = t³ (1 - 3r²/2 + r³ cos(3 delta)/sqrt(2)).
  Das Produkt der Wurzeln ist die im Companion schon geschriebene
  phasenabhängige Größe.
- v4.8.0-r16 (H11, widerlegt) und v4.9.0-r26 (H16, widerlegt, mit
  r26.1): Potentiale in den Slot-Normen bis Grad sechs haben kein Minimum
  mit drei verschiedenen Normen; Grad acht wäre nötig.
- koide-and-kernel (v480:koide-radius-phase), generation-coupling
  (zyklische Kopplung, Phasenkammern, gemeinsame Taktphase fällt heraus),
  coupling-scale-candidate (Drei-Kanal-Kandidat mit der alten
  Phasenformel: e/tau um 12,7 % daneben; zwei Harmonische geben K <= 1/2).
- v4.9.0-r38, r44.1(e), r45 (H30 bestätigt): Die Spiegelung rho der
  Trialitätsform wird durch die Chiralität gebrochen, tau bleibt (Modell
  I); dann Brannen-Form, „wie stark rho gebrochen ist, die Phase theta
  und |b|/a, ist nicht festgelegt“.
- koide_original_op3_cycle_phase.md und
  op3_original_question_operator_map_2026_11_11.md: Phase als
  Umlaufprodukt (verlangt |q Phi| ≈ 0,00257, kein nativer Fluss); drei
  getrennte OP3-Fragen.

Verhältnis zu r26.1: Die W-b-Rechnung hat zusätzlich die Nebenbedingung
sum ell_i = L und ungerade Potenzen der Länge; deshalb widerspricht ihr
Kreis von Gleichgewichten r26.1 nicht. Inhaltlich neu war dort wenig.

## Befund 1: Was die Phase strukturell ist

Auf dem Brannen-Kreis wirkt die zyklische Verschiebung tau als
delta -> delta + 2 pi/3 und die Spiegelung rho (ein Platz fest, zwei
getauscht) als delta -> -delta. Mit x_k = v_k - t und Amplitude A gilt

    x_0 x_1 x_2 = (A³/4) cos(3 delta)                (rho-gerade),
    (x_0-x_1)(x_1-x_2)(x_2-x_0) = ±(3 sqrt(3)/4) A³ sin(3 delta)
                                                     (rho-ungerade).

Jede unter tau und rho invariante Größe hängt nur von cos(3 delta) ab
und hat sin(3 delta) = 0, also zwei gleiche Massen, immer als kritische
Punkte. Eine Phase daneben verlangt eine rho-ungerade, tau-gerade Größe
(proportional sin(3 delta), in der Zirkulante Im b³) oder eine eigens
eingestellte Form. Mit E = kappa e_3 + chi Vandermonde auf dem flachen
Kreis der W-b-Quartik liegt das Minimum bei
tan(3 delta) = 3 sqrt(3) chi/kappa (geprüft). Die Leptonen haben
cos(3 delta) = 0,78587, |tan(3 delta)| = 0,78688.

Die Phase misst also das Verhältnis von rho-ungeradem zu rho-geradem
Anteil. Das ist r45 in anderen Worten und keine Herleitung.

## Befund 2: Die älteren Bausteine sind alle rho-symmetrisch

Mit dem Wissen aus r38–r45 gelesen:

| Baustein | Alter | Was er zur Phase sagt | Heute |
|---|---|---|---|
| thm:koide-triolic, Phasenformel theta_K = pi - sqrt(2) arcsin(beta_sym) (P2) | Kern, vor v4.8 | Phase aus dem Frame-Versatz, also aus einer rho-ungeraden Größe | Idee passt zur Struktur, Zahl an Daten mit 300–400 sigma ausgeschlossen (r09), archiviert |
| thm:spring (Materie–Photon–Tachyon) | Kern | spiegelsymmetrisch, Amplituden 1:1:3 | rho-symmetrischer Punkt, delta = 0; nach r38 ist die Frame-Triole gerade die Spiegelseite |
| Bemerkung „The 2/3 factor is everywhere“ | Kern | zählt Sektoren, keine Phase | ohne Statusvermerk; Koide ist nach r09 empirisch |
| thm:dirac-probe, Taktphase exp(i pi beta_sym) | Kern | gemeinsame Phase | fällt aus der Gram-Matrix heraus (generation-coupling) |
| v470/17 Genealogie: „Koide/triolic block structurally closed“ | Kern | erklärt die Frage für erledigt | steht ohne Statusvermerk im Text; nach r09/r10 offen |
| Slot-Norm-Potentiale r16, r26 | v4.8/v4.9 | S, Q, P, t sind unter rho invariant | deshalb höchstens zwei Normen; r45 nennt den Grund („kannten die Chiralität nicht“) |
| Stringfrage v5 (gleiche Strings, sum U(ell_i)) | 12.11. | unter allen Vertauschungen symmetrisch | gleiche Klasse: flach oder zwei gleiche Längen (W-b) |

Die Stringfrage und die alten Kernbausteine scheitern damit aus demselben
Grund an der Phase: Sie kennen die Chiralität nicht.

## Befund 3: Rho-ungerade Größen, die der Companion heute hat

1. Chiralitätsprojektor C_ch = (1 + i L_e7)/2 (r42); rho bildet ihn auf
   (1 - i R_e7)/2 ab (r45.1(b)).
2. Assoziator des Generationentripels, [e_4, e_5, e_6] = -2 e_7 (r13.1):
   total antisymmetrisch, also tau-gerade und rho-ungerade, fest unter dem
   Stabilisator von e_7. H10 fand damit keine Auswahl; Farbe und
   Generation sitzen dort auf demselben Objekt (r13, r14, 12.11.).
3. U(1)-Ladung Q_J = i L_e7 der Wirkung W1 mit der Umlauf-Lesart der
   Phase; ein nativer Fluss fehlt.
4. Vorzeichen des Frame-Versatzes (M bei +eta, T bei -eta), Gewichte
   a ≠ b und Gebiet G2. Die alte Phasenformel hat genau diese Größe
   benutzt.

Alle vier zeigen in dieselbe Richtung (e_7 bzw. M gegen T). Keine trägt
einen Betrag: Es gibt keine native Zahl für das Verhältnis
rho-ungerade zu rho-gerade. Damit ist die Quellensuche für die Phase
negativ, mit einer genau benannten Lücke.

## Ergebnis

- Eine Größe, die die Phase sieht, steht im Companion (r12.1), aber als
  rho-gerade Größe wählt sie nur zwei gleiche Massen.
- Die native Operation, die fehlt, ist eine tau-invariante, rho-ungerade
  Kopplung der drei Plätze mit hergeleitetem Betrag. Der Ort dafür ist
  die Chiralität (r45), nicht eine Stringenergie.
- Weder die Phase noch K = 2/3 oder das Leptonspektrum sind hergeleitet.
  OP3/OP4 und die Stringfrage bleiben offen; Guards unverändert.

## Ältere Stellen ohne heutigen Stand (nur gemeldet, nicht geändert)

- v470/17_open_question_genealogy.tex, Zeilen 18 und 194: Koide-Block
  „structurally closed“.
- v470/10_sphaera_and_physics.tex, Bemerkung „The 2/3 factor is
  everywhere“ und rem:koide-mass-discrepancy (schreibt die Abweichung der
  Näherung von beta_sym zu; nach coupling-scale-candidate behebt der
  exakte Wert sie nicht).

Die veröffentlichten Quellen bleiben unverändert (append-only). Ein
Statusvermerk wäre Sache einer neuen Runde.

## Selbstprüfung

op3_phase_source_search_2026_11_12.py: Identitäten für e_3, Vandermonde
und die Wirkung von rho und tau (Fehler 1e-14 an 1000 Zufallspunkten);
Minimum mit rho-ungeradem Zusatz gegen die Formel (drei Fälle, sechs
Stellen); Leptonwerte. Nachträglich: Das per Definition summenfreie
Tripel (gamma_string, gamma_BI, gamma_3) hat cos(3 delta) = -0,869, kein
Treffer. Gelesen: thm:koide-triolic, thm:spring, v470/17, v4.8.0-r09 bis
r13 und r16, v4.9.0-r26, r38, r44, r45, koide-and-kernel,
generation-coupling, coupling-scale-candidate, sec:v4110-koide-overlap
und die beiden OP3-Notizen. Keine externen Quellen.
