# Erkundung: Oktant in einer neutralen SU(2) (Sumino) und die Rolle von Spin 1/2

13. November 2026, spät. Autorenauftrag: „aufräumen, dann weitersuchen“. Weitergesucht wurde beim offenen Hindernis
der Oktanten-Lesart: Im Isospinfaktor bricht sie die Ladung (r33), im Oktonionenfaktor die Farbe, im neutralen
Dixon-Teil verhindert die Signatur (2,1) den exakten Oktanten (`op3_hopf_octant_2026_11_13.md`). Erkundung, nicht
blind, kein Datenvergleich. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T5/T8, OP3.
Skript `op3_neutral_su2_octant_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_eta_form_search_2026_11_13.md` (Oktanten-Tripel der Qubits: ρ² = 1/2, Rang 2, π/4), `op3_hopf_octant_2026_11_13.md`
  (Orte und Hindernisse), `op3_slot_u3_gauging_2026_11_13.md` (Platzindex-U(3), Sumino-Abgleich).
- r33 (i, j, k als Labels im Isospinfaktor nicht Q_em-invariant), Gram-Notiz (Hopf-Träger K ≤ 1/2).
- Sumino, arXiv:0812.2103, Abschnitte 2 und 5 (nachgelesen): Φ transformiert unter U(3) × SU(2) als Φ → U Φ Oᵀ mit
  O ∈ SO(3). Die SU(2) wird geeicht und bei hoher Skala gebrochen; sie ist farb- und ladungsneutral. Die Massenmatrix
  ist ψ̄_L Φ Φᵀ e_R; im Vakuum ist Φ diagonal, die drei Generationen sitzen also auf drei orthogonalen Achsen des
  SO(3)-Vektorindex. Suminos „Vereinigung mit SU(2)_L“ bei 10²–10³ TeV ist eine Gleichheit der Kopplungen, kein
  gemeinsamer Gruppenschritt.

## Ergebnis

**1. Der Oktant ist in Suminos Vakuum schon angelegt.** Die drei Generationen stehen auf drei orthogonalen Achsen einer
neutralen SO(3). Ein Oktanten-Tripel in dieser Gruppe bricht weder Ladung noch Farbe; das Hindernis aus r33 entfällt,
wenn das Qubit zu dieser SU(2) gehört statt zum Isospin.

**2. Nur Spin 1/2 gibt Koide und π/4.** Für Zustände höchsten Gewichts mit Spin j entlang x, y, z (numerisch exakt):

| j | Treue = (1/2)^{2j} | ρ² | K | Bargmann-Phase j · π/2 |
|---|---|---|---|---|
| 1/2 | 0,5 | 0,5 | **2/3** | **π/4** |
| 1 | 0,25 | 0,25 | 1/2 | π/2 |
| 3/2 | 0,125 | 0,125 | 5/12 | 3π/4 |
| 2 | 0,0625 | 0,0625 | 3/8 | π |

Die reellen SO(3)-Vektoren selbst (Suminos zweiter Index) sind orthogonal: Überlappung 0, keine Phase. Koide
(ρ² = 1/2) und die Verschiebung π/4 gehören also zusammen zu Spin 1/2 an drei orthogonalen Achsen. Nebenbefund:
j = 1 gibt K = 1/2, den Wert, den die Gram-Notiz für den Hopf-Träger und das Tensorprodukt fand.

**3. Lesart.** H99 hieße dann: Die Neutrinos tragen gegenüber den geladenen Leptonen die Phase eines Spin-1/2-Objekts
der neutralen Familien-SU(2), dessen Richtung an den drei Generationen auf Suminos orthogonalen Achsen steht. Die
geladenen Leptonen koppeln über den Vektorindex (keine Phase aus dieser Gruppe), die Neutrinos über einen Spinor.

## Bewertung
- Ein farb- und ladungsneutraler Ort für das Oktanten-Tripel ist gefunden, aber nicht im Companion, sondern in Suminos
  Modell (neutrale SU(2) mit SO(3)-Vektorindex). Dort ist er durch das Vakuum vorgegeben.
- Spin 1/2 ist ausgezeichnet: Nur er verbindet Koide-Überlappung und Phase π/4.
- Nicht gezeigt: dass ein Feld des Neutrino-Sektors ein Spinor dieser SU(2) ist und die geladenen Leptonen nicht; dass
  der Companion eine solche neutrale SU(2) enthält. Gesichtete Kandidaten im Companion tragen Ladung (Isospin, r33),
  Farbe (quaternionische Unteralgebren der Oktonionen) oder brechen die Isotropie (räumliche Drehungen).
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nächste Fragen
- Hat der Companion eine neutrale SU(2), deren Vektorindex die Generationen trägt (etwa ein zweiter Quaternionenfaktor
  oder der Platzindex selbst, als SO(3) ⊂ U(3))? Suminos SU(2)_V ⊂ U(3) × SU(2) wirkt als 3 auf (Φ_2, Φ_5, Φ_7).
- Welches Neutrino-Feld könnte deren Spinor sein (ν^c aus r44.1(d))?

## Nachtrag: neutrale SU(2) im Companion gesucht (13.11., spät, Autor: „Neutrale SU(2) suchen“)

Skript, Abschnitt „Wo eine neutrale SU(2) sitzen kann“. Nicht blind, kein Datenvergleich.

**1. Wo eine neutrale SU(2) überhaupt sitzen kann.** Eine SU(2), die mit Farbe, Isospin, Hyperladung und Lorentz-Gruppe
vertauscht, kann nach dem Schur-Lemma innerhalb einer Generation nur als Vielfaches der Eins wirken; sie wirkt also
nur auf den Generationsindex. Gesucht ist damit eine Familien-Symmetrie, keine innere Symmetrie des Dixon-Raums.
Bestätigung im Oktonionenfaktor: Der Zentralisator der Farb-su(3) in g_2 ist null (numerisch).

**2. In der Familien-U(3) des Platzindex gibt es zwei Einbettungen, und keine passt.**

| Einbettung | Spins in 3 | in 6 | in 8 | Generationen als Vektor? | Spinor? |
|---|---|---|---|---|---|
| SO(3) als reelle Drehungen | 1 | 0, 2 | 1, 2 | ja | nein |
| SU(2) als 2 + 1 | 0, 1/2 | 0, 1/2, 1 | 0, 1/2, 1 | nein | ja |

Entweder stehen die Generationen als Vektor auf drei orthogonalen Achsen, dann enthalten die Darstellungen der U(3)
nur ganzzahlige Spins und kein Spinor-Objekt; oder es gibt Spinoren, dann sind die Generationen ein Dublett plus
Singulett und keine drei gleichberechtigten Achsen. Die Oktanten-Lesart (drei orthogonale Achsen und ein Spin-1/2-Objekt)
ist innerhalb der Familien-U(3) allein nicht möglich.

**3. Was bleibt.** Eine zusätzliche Familien-SU(2) neben der U(3), wie bei Sumino (U(3) × SU(2) mit Φ → U Φ Oᵀ), und ein
Feld, das deren Dublett ist. Suminos Modell enthält ein solches Dublett-Feld nicht; der Companion enthält weder die
zusätzliche SU(2) noch das Feld. Ein Kandidat wäre ν^c (r44.1(d)) als Dublett dieser Gruppe; das ist ein neues
Strukturelement.

**Bewertung.** Die neutrale SU(2) für die Oktanten-Lesart muss eine Familien-Symmetrie sein (Schur), und sie kann
nicht in der Platzindex-U(3) liegen (Einbettungen). Gebraucht würde eine zweite Familien-SU(2) mit einem
Spinor-Feld im neutralen Sektor. Im Companion ist sie nicht angelegt. Die Suche nach einem nativen Ort ist damit
negativ abgeschlossen, solange keine zweite Familienstruktur eingeführt wird (vgl. r14/r33: „Generationen brauchen
eine zweite Dreierstruktur außerhalb von O“). OP3/OP4 offen; H100 unberührt.

## Nachtrag: das Feld gesucht (13.11., spät, Autor: „dann suche so ein Feld“)

Skript, Abschnitt „Feldsuche“. Nicht blind, kein Datenvergleich.

**Anforderungen (Rückwärtssuche).** Das Feld muss farb-, ladungs- und hyperladungsneutral sein, nur im Neutrino-Block
(Majorana) auftreten und ein Dublett (Spin 1/2) einer neutralen Familien-SU(2) tragen, deren Vektorindex die drei
Generationen auf orthogonalen Achsen hält.

**1. Im Dixon-Raum C⊗H⊗O gibt es keinen Platz dafür.**
- Der H-Faktor trägt zwei SU(2): Linksmultiplikation ist die Lorentz-Gruppe, Rechtsmultiplikation der schwache Isospin
  (Konvention der Dixon-Notiz und von k85). Beide sind vergeben, keine ist neutral im verlangten Sinn.
- Im Oktonionenfaktor ist der Zentralisator der Farb-su(3) in so(8) zweidimensional, also nur abelsch (numerisch); auch
  die Trialitäts-Spin(8) enthält keine SU(2), die mit der Farbe vertauscht.
- Zusammen mit dem Schur-Argument: Ein solches Dublett-Feld liegt nicht in C⊗H⊗O.

**2. Der einzige native Kandidat im Neutrino-Sektor trägt nicht.** Nach r82.4 ist ν^c ν^c der einzige eichinvariante
Paarkanal (ψᵀεψ, Torsionswechselwirkung anziehend); ein Kondensat dort wäre neutral und gehörte nur zu den Neutrinos.
Seine Spin-Struktur ist aber die Lorentz-Struktur. Liest man die Spins der drei ν^c entlang x, y, z, gibt die
Paarungsmatrix Diagonale 0 und Nebendiagonalen |·|² = 1/2, aber das entartete Spektrum (0; 1,22; 1,22). Mit einer
gemeinsamen Diagonale (0,5; 1; 1,5) bleibt K bei 0,46; 0,42; 0,39 mit positiven Wurzeln. Kein Koide, kein H99.

**3. Was bleibt.** Ein Feld mit den verlangten Eigenschaften braucht eine Erweiterung außerhalb von C⊗H⊗O, etwa einen
eigenen Familienfaktor mit einer SU(2) (wie Suminos U(3) × SU(2)) und ein neutrales Dublett darin. Das ist die
„zweite Dreierstruktur außerhalb von O“ aus r14/r33, jetzt mit der zusätzlichen Forderung nach einer stetigen SU(2)
und Spin 1/2. Die Sedenionen (r13) liefern nur eine diskrete S_3.

**Zurückgestellte Ideen.** I4 (Kondensation als Massenquelle) ist durch den ν^c-Kanal berührt; sie wurde am 6.11.
unter den geltenden Lesarten als nicht verwirklichbar eingeordnet (`Erkundung_I4_Kondensat.md`). Kein neuer Auslöser.

**Bewertung.** Die Feldsuche ist im Companion negativ: Weder der Dixon-Raum noch der native ν^c-Paarkanal trägt ein
Spin-1/2-Feld einer neutralen Familien-SU(2). Die Oktanten-Lesart von H99 bleibt damit eine Lesart, die eine
Erweiterung des Companion verlangt. OP3/OP4 offen; H100 unberührt.
