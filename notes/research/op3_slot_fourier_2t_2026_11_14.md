# Erkundung: Die Fourier-Transformation der drei Slots erzeugt 2T mit dem magischen Winkel

14. November 2026. Autor: „dann OP3“. Rückwärtssuche zur Lücke aus v4.10.0-r13.6: Gesucht war eine nicht monomiale
Slotoperation, die auf einem Dublett des Slotraums eine zweizählige Achse unter dem magischen Winkel hat. Erkundung
ohne Vorab-Notiz, kein Datenvergleich, keine H-Nummer, kein MMA-Beleg, keine Änderung an Guards. Einordnung T5/T7/T8,
OP3. Skript `op3_slot_fourier_2t_2026_11_14.py`, Ausgabe `..._out.txt`.

**Blindheit: nicht blind.** Das Ziel stand in der Übergabe (K = 2/3, Phase π/4, tan(θ/2) = 2 sin(π/12)). Die Rechnung
bestätigt, was sich vorher von Hand ergab. Das ist ein nachträglich gefundener Bau, keine Vorhersage.

## Vorwissen geprüft
- v4.10.0-r13.6 und `op3_tau_doublet_axis_2026_11_14.md`: Monomiale Slotoperationen geben auf dem τ-Dublett nur 0° und
  90°; das gesuchte Element überlagert alle drei Slots. Als ungeprüft genannt: eine Struktur, in der Summen von
  Slotoperationen selbst Operationen sind.
- `op3_third_generation_singlet_2026_11_14.md`: τ-symmetrisches 2 + 1 über die Fourier-Moden; nur S_3.
- `op3_hurwitz_2t_neutral_qubit_2026_11_14.md`: In Weg A entsteht 2T aus halbzahligen Summen monomialer Operationen.
- `op3_triality_carrier_gate_2026_11_12.md`: Slotoperationen τ und ρ(x,y,z) = (x̄,z̄,ȳ) auf O³.
- Übergabe vom 13.11.: „Nötig wäre tan(θ/2) = 2 sin(π/12).“
- r55 bis r60 (über `op3_generation_carrier_review_2026_11_13.md`): A_4-Auslesung, TM2-Muster.
- Suche nach „Fourier“, „Clifford“, „Heisenberg-Gruppe“, „Jordan“, „F_4“ in den Notizen: Fourier-Moden kommen als
  Zerlegung vor, die Fourier-Transformation als Operation nicht.

## Suchrichtung (rückwärts)
Die Bedingung aus r13.6 verlangt zweierlei: eine Zerlegung 2 + 1 des Slotraums C³ und darauf eine Gruppe 2T. In Weg A
kam 2T daher, dass die Algebra halbzahlige Summen der drei monomialen Operationen erlaubt. Rückwärts gefragt: Welche
gleichgewichtete Summe monomialer Slotoperationen ist unitär? Die monomialen Grundoperationen auf drei Slots sind der
Zyklus τ und die Uhr D = diag(1, ω, ω²); ihre neun Produkte τᵃDᵇ sind eine Basis aller 3×3-Matrizen. Eine
gleichgewichtete unitäre Summe ist die diskrete Fourier-Transformation F. Sie ist nicht die einzige; andere Elemente
derselben Gruppe (Punkt 7) sind ebenfalls solche Summen.

## Ergebnis

**1. F ist die gleichgewichtete Summe der neun monomialen Operationen.** F = Σ c_ab τᵃDᵇ mit |c_ab| = 1/3 für alle
neun Terme. F ist unitär, hat neun Einträge ungleich null, und F² = P vertauscht die Slots 1 und 2. P ist der Slotteil
der nativen Operation ρ.

**2. Die Parität P zerlegt den Slotraum in 2 + 1.** Gerade: e_0 und u = (e_1 + e_2)/√2. Ungerade: (e_1 − e_2)/√2. Die
Phase S = diag(1, ω, ω) und F vertauschen mit P und mischen die beiden Teile nicht. τ und D tun das nicht.

**3. S und F erzeugen auf dem Dublett die Gruppe 2T.** Auf dem geraden Dublett ist S = diag(1, ω) und

F = [[1/√3, √(2/3)], [√(2/3), −1/√3]].

Mit Determinante 1 erzeugen sie 24 Elemente mit den Ordnungen 1:1, 2:1, 3:8, 4:6, 6:8. Auf C³ sind es 96 Elemente,
projektiv 24.

**4. Der magische Winkel ist der Eintrag ⟨e_0|F|e_0⟩ = 1/√3.** S dreht um 120°, F um 180°, und zwischen den beiden
Achsen ist |cos| = 0,5773502692 = 1/√3. Der Winkel kommt also aus der Zahl der Slots: Für n Slots ist der Eintrag
1/√n.

**5. Der Oktant entsteht.** Die Bahn eines F-Eigenzustands unter S gibt ρ² = 1/2, K = 2/3 und die Bargmann-Phase π/4.
Der Eigenzustand zum Eigenwert +1 ist der Slot-Vektor (1 + √3, 1, 1), der unter der Fourier-Transformation fest
bleibt. Für ihn ist tan(θ/2) = 0,517638 = 2 sin(π/12), genau die Bedingung aus der Übergabe.

**6. n = 3 ist ausgezeichnet.** Der gerade Teil unter j → −j hat die Dimension ⌊n/2⌋ + 1. Nur für n = 3 ist er ein
Qubit mit einem Singulett daneben (n = 2: Qubit ohne Singulett; n ≥ 4: Dimension ≥ 3).

**7. τ gehört nicht zu dieser Gruppe, wird aber von ihr normalisiert.** τ und D erzeugen die Heisenberg-Gruppe mit 27
Elementen. F und S bilden sie in sich ab; F τ F⁻¹ ist D oder D⁻¹. Der Slotzyklus selbst erhält das Dublett nicht.

## Bewertung
- **Was gewonnen ist:** Die Lücke aus r13.6 ist auf eine benennbare Operation zurückgeführt. Mit der
  Fourier-Transformation der Slots und einer Slot-Phase der Ordnung 3 gibt es auf dem Träger mit **drei** Generationen
  ein Dublett mit 2T, dem magischen Winkel und dem Oktanten. Die Zerlegung 2 + 1 ist die Parität der nativen Operation
  ρ. Der magische Winkel ist dann 1/√3 wegen der drei Slots.
- **Was dafür angenommen wird (nicht hergeleitet):**
  - F als Operation. Im Bestand des Companion gibt es keine Slotoperation, die Slots überlagert. Das ist dieselbe
    Lücke wie in r13.6, jetzt mit Namen.
  - S = diag(1, ω, ω) als Operation, also eine Phase ω auf zwei Slots gegen den dritten. Ob die slotweise Wirkung der
    Trialität genau diese Phase liefert, ist nicht geprüft.
- **Was nicht passt:**
  - Das Element der Ordnung 3 ist die Phase S, nicht der Slotzyklus τ. τ steht zu der Gruppe nur über die
    Heisenberg-Gruppe in Beziehung. Das Profil verlangte den Generationszyklus selbst.
  - Das Dublett tragen alle Teilchenarten. „Nur im Majorana-Block“ bleibt unerfüllt.
  - Die Generationen wären e_0, (e_1 + e_2)/√2 und (e_1 − e_2)/√2, also nicht die Slots. Was das für die Massen
    heißt, ist nicht untersucht.
- **Zu F_4 (aus Vorwissen, nicht geprüft):** In der Jordan-Algebra der hermiteschen 3×3-Matrizen über O ist der
  Zentralisator der Farb-SU(3) in F_4 eine SU(3), die auf den farbigen Teilen der drei Slots als Fundamentale wirkt.
  Sie enthielte F und S, aber als stetige Gruppe zeichnet sie nichts aus. Die Auswahl leistet hier die endliche
  Heisenberg-Gruppe aus τ und D. Eine Rechnung in der Jordan-Algebra wurde nicht gemacht.
- Koide 2/3 und die Phase sind **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert.
  H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.

## Mögliche nächste Schritte (Autorentscheidung)
- Die native Herkunft von F suchen: Gibt es im Companion eine Operation, die Slotposition und Slotphase vertauscht
  (F τ F⁻¹ = D)?
- Prüfen, ob die Trialität die Phase S liefert.
- Die Massenfrage: Was gibt eine Massenmatrix, die unter 2T auf dem Dublett invariant ist, für drei Generationen?
