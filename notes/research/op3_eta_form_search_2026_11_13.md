# Erkundung: Suche nach der Form η im neutralen Sektor

13. November 2026, abends. Autorenauftrag: „mach das“ (nächster Schritt laut Übergabe), nach Festschreiben von H100
(Commit 9c77ddd). Erkundung, analytisch mit numerischer Selbstprüfung; **kein Datenvergleich** außer der bekannten
Zielgröße aus H99b. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T8, OP3.
Skript `op3_eta_form_search_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_slot_u3_gauging_2026_11_13.md`, Nachtrag Neutrino-Block: ν_L und e_L teilen das linke Tripel X; geladen
  T_12 ∝ (XᵀX)*, neutral Ω_1 ∝ Xᵀ η X; der Sektorunterschied liegt ganz in η.
- `op3_indefinite_form_2026_11_13.md` (bilineare Form x^T y, Lesart B mit Signatur (3,3)), r10.2 (120°-Triole ist
  Nullvektor), r44.1(e) (zirkulante hermitesche Kopplung gibt die Brannen-Form), r55 (Majorana mit Z_2).
- Suche nach Bargmann, Pancharatnam, geometrischer Phase, Berry in notes/ und sources/: kein Treffer.

## Ergebnis

**1. Die Brannen-Phase ist ein Drittel der Bargmann-Phase der Plätze.** Für jede Gram-Matrix mit Einheitsdiagonale
(hermitesch, auch komplex) gilt

    s_k = 1 + 2ρ cos(θ + 2πk/3),   cos 3θ = Re(c_12 c_23 c_31)/ρ³

(numerisch 2·10⁻¹⁵). Haben die drei Überlappungen gleichen Betrag (zirkulanter Fall, Brannen-Form der geladenen
Leptonen nach r44.1(e)), ist 3θ = Φ = arg(c_12 c_23 c_31), die Bargmann-Invariante des Tripels, also seine
geometrische Phase. Sie hängt nicht von der Phasenwahl der einzelnen Plätze ab.

**2. H99 als Bedingung an die geometrische Phase.** Gleiche Überlappung und Verschiebung um den Bogenrand heißt:

    ΔΦ = Φ_ν − Φ_e = 3θ_b = π/4   (bei ρ² = 1/2).

NuFIT 6.1 verlangt 3 · 0,25802 = 0,774 statt π/4 = 0,785 (die Fassung bei einer Skala liegt dazwischen). Gesucht ist
also eine Form η, die jede Überlappung im Betrag erhält und die geometrische Phase des Tripels um π/4 dreht.

**3. Was dafür nicht in Frage kommt.**
- **Umphasen der Plätze** (x_a → e^{iφ_a} x_a): Φ ist invariant (numerisch geprüft). Eine bloße Konvention auf den
  Plätzen erzeugt keine Verschiebung.
- **η diagonal in der Eigenbasis** (Vorzeichenwechsel einzelner Eigenwerte) im zirkulanten Fall: Die Beträge der
  Wurzeln bleiben die der geladenen Leptonen; die Massenverhältnisse wären gleich. Ausgeschlossen.
- **Reelle Formen auf reellen Plätzen**: Φ ∈ {0, π}; θ ändert sich nur über die Beträge der einzelnen Überlappungen.
  Das ist möglich, bricht aber die zyklische Gleichheit der Beträge. Die zirkulante Lesart verlangt eine komplexe
  Struktur.
- **Lesart B allein** (geladen hermitesch x†y, neutral bilinear xᵀy auf denselben komplexen Plätzen): Bei 4000
  Tripeln mit ρ_e² = 0,50 streut ΔΦ mit 1,36 um null und Δρ² stark; keines erfüllt beide Bedingungen. Der Wechsel
  von hermitesch zu bilinear legt keine Verschiebung fest.

**4. Was die Bedingung verlangt** (korrigiert im Nachtrag unten). Eine Phase e^{iθ_b} auf jeder Kante a → a+1 des
Platzdreiecks, in Gegenrichtung konjugiert, erhält alle Beträge und dreht Φ um 3θ_b = π/4. Das ist mit hermiteschen
und mit bilinearen Überlappungen verträglich. Gesucht ist also ein Fluss π/4 durch das Dreieck der drei Plätze im
neutralen Sektor, relativ zum geladenen.

## Bewertung
- Die Frage nach η ist auf eine geometrische Bedingung zurückgeführt: Bargmann-Phase π/4 bei erhaltenen Beträgen.
  Das ist neu im Projekt (kein Vorbefund) und in der zirkulanten Lesart äquivalent zu H99.
- Ausgeschlossen sind Umphasen, Vorzeichenwechsel in der Eigenbasis und der bloße Wechsel hermitesch → bilinear.
- Nicht gefunden: eine native Quelle für den Fluss π/4 (siehe Nachtrag).
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert. H100 ist davon unberührt (Kandidaten festgeschrieben).

## Nächste Fragen
- Gibt es im Companion eine Paar-Phase im neutralen Sektor, etwa aus dem Assoziator, aus Q_J = iL_e7 oder aus der
  Lesart B auf dem Kern, die auf jedem Paar gleich ist?
- Hat die geometrische Phase der geladenen Leptonen (Φ_e = 3θ_e = 0,667) selbst eine native Deutung?

## Nachtrag: Paar-Phase π/12 gesucht (13.11., abends, Autor: „Paar-Phase π/12 suchen“)

**Korrektur.** Punkt 4 behauptete zuerst, eine gleichmäßige Phase je Überlappung gehe nur bei bilinearen
Überlappungen. Das ist falsch: Gerichtete Kantenphasen (a → a+1 mit e^{iθ_b}, Gegenrichtung konjugiert) halten die
Gram-Matrix hermitesch, erhalten ρ² und verschieben θ genau um θ_b (numerisch geprüft). Die Bedingung ist ein
**Fluss** durch das Platzdreieck: Umphasen der Plätze verteilt die Kantenphasen um, die Summe 3θ_b bleibt
(eichinvariant). Punkt 4 ist oben berichtigt.

**Native Phasen im Companion.** Gesammelt wurden die Phasen, die native Strukturen auf drei Plätze bringen:
- ω = e^{2πi/3}: Triole, zyklische Platzsymmetrie τ, Sedenion-Rotation ψ (r13);
- i: Komplexstruktur L_e7 und Q_J = iL_e7, Tachyon-Abbildung z ↦ iz;
- −1: Spiegelungen, ρ, Vorzeichen der indefiniten Form η.

Alle Produkte daraus sind Vielfache von π/6 (numerisch: Flüsse 0, 2, 4, …, 22 in Einheiten π/12). **π/4 = 3 · π/12
ist nicht darunter**, und das gilt allgemein: 8a + 6b + 12c = 3 + 24n hat keine ganzzahlige Lösung, weil links eine
gerade, rechts eine ungerade Zahl steht. Der gesuchte Fluss braucht eine achte Einheitswurzel e^{iπ/4}; Kubik- und
Viertelwurzeln reichen nicht. Die nächsten erreichbaren Flüsse π/6 und π/3 liegen je π/12 daneben (nicht mit Daten
verglichen).

**Woher π/4 sonst kommt.** Der Fluss π/4 ist genau die Bargmann-Phase eines koplanaren Koide-Tripels (ρ² = 1/2,
det S = 0, numerisch 10⁻¹⁶): cos(π/4) = 1/√2 = ρ. H99 heißt damit: Die geometrische Phase der Neutrinos ist die der
geladenen Leptonen plus die eines koplanaren Koide-Tripels. Das ist eine Umformulierung des Bogenrands, keine
Herleitung; sie zeigt aber, dass π/4 aus der Koide-Geometrie selbst kommt (ρ = 1/√2) und nicht aus einer
Symmetriephase.

**Zum Vergleich:** Der Fluss der geladenen Leptonen ist 3θ_e = 0,6667 rad (Brannens 2/9 mal 3). Er ist kein
rationales Vielfaches von π, stammt also ebenfalls aus keiner Einheitswurzel.

**Bewertung.**
- Ausgeschlossen: alle Flüsse aus den nativen Phasen ω, i, −1 (Paritätsargument).
- Verbleibend: ein Fluss, dessen Wert aus der Koide-Geometrie folgt (Rand des Bogens), oder eine native achte
  Einheitswurzel. Kandidaten für die zweite (ohne Prüfung): Spin(8)/Trialität, Periodizität 8 von Cl(n),
  Hadamard-artige Faktoren (1 + i)/√2. Keiner ist untersucht; nichts davon zählt als Treffer.
- Für die erste Möglichkeit wäre ein Mechanismus nötig, der den Fluss einer koplanaren Koide-Konfiguration im
  neutralen Sektor zu dem der geladenen addiert, etwa ein koplanarer (Rang-2-)Block, der nur neutral existiert. Der
  native Majorana-Verbinder für ν^c (r44.1(d)) ist ein möglicher Ort; ob er Rang 2 hat, ist nicht geprüft.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.

## Nachtrag: π/4 = (3/2) · π/6 (13.11., Autor: „erst π/6 · 3/2 rechnen und schauen, wo die 3/2 herkommen“)

π/6 ist nativ: ω · i⁻¹ = e^{i(2π/3 − π/2)} = e^{iπ/6} (Skript, Abschnitt 5). Gesucht ist also ein Faktor 3/2.
Gesammelt und geprüft, ob sie einen Mechanismus liefern oder nur die Zahl:

| Herkunft der 3/2 | gilt nur bei ρ² = 1/2? | Mechanismus |
|---|---|---|
| 3ρ² (Koide-Überlappung) | ja: bei ρ² = 0,40 bzw. 0,60 weicht Φ_b von (π/6)·3ρ² um 0,54 bzw. 0,41 ab | keiner |
| 1/K | ja: Abweichung 0,29 bzw. 0,18 | keiner |
| 3α/2π (QED-Log), Spin 3/2, Ladungsdifferenzen der Blöcke (Leptonzahl 2, T₃ 1/2, Y 1/2) | – | keiner, oder Zahl passt nicht |
| **3 · 1/2: drei Kanten, Spinor-Halbierung** | nein, struktureller Faktor | **ja, als Lesart** |

**Lesart „drei Kanten mal Spinor“.** Eine Drehung um π/6 im Vektorbild wirkt auf Spinoren mit e^{±iπ/12} (SU(2)
als Doppelüberlagerung). Ist der Transport von Platz zu Platz eine solche Drehung und sind die Plätze Spinoren, trägt
jede Kante π/12, und die drei Kanten des Dreiecks geben den Fluss 3 · π/12 = π/4. Das passt zum Zwei-Sonden-System:
Die Sonden Ψ_1, Ψ_2 sind Dirac-Spinoren. Ein nativer Winkel π/6 kommt außer aus ω · i⁻¹ auch als Winkel zwischen
Wurzel und Gewicht im Wurzelsystem A_2 vor (die Bemerkung zum Auslese-Sechseck in v490 nennt A_2 für die sechs
Richtungen im Abstand von 60°).

**Was dafür fehlt.**
- Warum der Transport zwischen benachbarten Plätzen gerade eine Drehung um π/6 ist.
- Warum er nur im neutralen (Majorana-)Block wirkt und nicht im geladenen (Dirac-)Block. Ein Hinweis zum Prüfen:
  Unter einer Phasendrehung bleibt ψ̄ψ unverändert, ψᵀψ nicht; ob sich daraus die Beschränkung auf den neutralen
  Block ergibt, ist nicht gerechnet.
- Die anderen Herkünfte der 3/2 treffen die Zahl nur an der Stelle ρ² = 1/2 und sind daher Numerologie.

**Bewertung.** Die Zerlegung trägt als Lesart: Fluss = 3 Kanten · (π/6)/2. Sie macht aus „achte Einheitswurzel
fehlt“ die Frage „Spinor-Transport um π/6 je Kante“. Nicht hergeleitet; kein Datenvergleich; H100 unberührt.
OP3/OP4 offen.

## Nachtrag: Spinor-Transport geprüft (13.11., Autor: „Spinor-Transport prüfen“)

Skript, Abschnitt 6. Nicht blind (Ziel π/4 bekannt), kein Datenvergleich.

**1. Raumzeitlicher Spinor-Transport scheidet aus.** Drehungen (SU(2)) und Boosts (SL(2,C)) erfüllen Uᵀ ε U = ε,
Drehungen zusätzlich U†U = 1. Jeder Lorentz-invariante Massenterm (Dirac ψ̄ψ, Majorana ψᵀεψ) ist deshalb blind für
einen solchen Kantentransport: Der Fluss bleibt numerisch unverändert (1,95980 vor und nach einer Drehung um π/6 auf
jeder Kante). Die Phase π/12 je Kante erscheint nur in der Übergangsamplitude χ†Uχ, die kein Massenterm ist. Die
Halbierung muss also aus einem **inneren** Transport kommen, nicht aus der Raumzeit.

**2. Innerer Transport (U(1) auf dem Platzindex).** Mit Kantenwinkel A je Ladungseinheit sieht ein Massenblock den
Fluss q · 3A, wobei q die Ladung des transportierten Partners ist (numerisch: q = 1 gibt π/2, q = 1/2 gibt π/4 bei
A = π/6). Der Dirac-Block transportiert e_R, der Majorana-Block ℓ_L. Der Unterschied der Sektoren ist

    Φ_ν − Φ_e = (q_L − q_R) · 3A.

Mit dem nativen A = π/6 verlangt H99 also **q_L − q_R = 1/2**.

| Ladungszuordnung | q_L − q_R | Φ_ν − Φ_e bei A = π/6 |
|---|---|---|
| Sumino (3, +1) und (3̄, −1) | 2 | π (passt nicht) |
| vektorartig | 0 | 0 |
| Sumino mit halben Ladungen | 1 | π/2 |
| **Hyperladung Y/2: ℓ_L −1/2, e_R −1** | **1/2** | **π/4** |

**3. Nachträglicher Fund, mit Vorbehalt.** Die verlangte Differenz 1/2 ist genau die Hyperladung des Higgs-Dubletts
(Y_H/2 = 1/2), festgelegt durch die Eichinvarianz der Yukawa-Kopplung ℓ̄ H e. Die 3/2 aus π/4 = (3/2) · π/6 wären
dann: drei Kanten mal Hyperladungsdifferenz 1/2. Das passt zum Vorbefund der Dixon-Platzkopplung
(`op3_dixon_slot_coupling_2026_11_13.md`): Dort trägt die Sektorphase θ_s = σ φ_H + λ φ_O ein Vorzeichen σ, das an
Y/2 hängt (e und d gegen ν und u).

Vorbehalte:
- Gesucht wurde nach einer Ladungsdifferenz 1/2, und davon gibt es mehrere (T₃, Y/2, Spinor-Halbierung). Der Treffer
  bei der Hyperladung ist deshalb schwach.
- Ein Fluss der Hyperladung durch das Dreieck der Generationsplätze verbindet Eichfeld und Familienraum. Das ist
  im Companion nicht angelegt und physikalisch ungewöhnlich.
- Suminos Aufhebung der QED-Korrektur braucht konjugierte Familienladungen (Differenz 2). Der Fluss müsste dann an
  eine andere U(1) koppeln als Suminos Familien-U(1), etwa an die Hyperladung.
- Warum der Kantenwinkel π/6 ist, bleibt offen (nativ verfügbar als ω · i⁻¹).

**Bewertung.** Der Spinor-Transport in der Raumzeit ist ausgeschlossen. Ein innerer Transport mit dem nativen Winkel
π/6 je Kante erzeugt den H99-Unterschied genau dann, wenn die Ladungen von ℓ_L und e_R sich um 1/2 unterscheiden; die
Hyperladung erfüllt das. Lesart, nicht hergeleitet; nachträglich gefunden. OP3/OP4 offen; H100 unberührt.

## Nachtrag: Dixon-Sektorphase geprüft (13.11., Autor: „Dixon-Sektorphase prüfen“)

Vorwissen: `op3_dixon_slot_coupling_2026_11_13.md`, Punkte 4 und 6 und Nachtrag Hyperladung: θ_s = σ_s φ_H + λ_s φ_O
mit σ = +1 (e, d), −1 (ν, u), λ = +1 (Leptonen), −1 (Quarks); Verbinder mit Y/2 = +1/2 (e, d), −1/2 (ν, u);
Spiegelung θ_u = −θ_e, θ_d = −θ_ν. Skript, Abschnitt 7. Nicht blind.

**1. Die Struktur passt qualitativ.** Die Neutrino-Phase unterscheidet sich von der der geladenen Leptonen nur durch
das Vorzeichen von φ_H: θ_ν − θ_e = −2φ_H. Das ist die Kopplung an die beiden Dublett-Richtungen (Y/2 = ±1/2,
Higgs und konjugiertes Higgs). Der Sektorunterschied ist damit hyperladungsgebunden, wie im vorigen Nachtrag vermutet.

**2. Die Zahl passt mit nativen Phasen nicht.** Weil die Brannen-Phase nur bis auf θ → −θ und θ → θ + 2π/3 bestimmt
ist, gibt es mehrere Zweige. In allen verlangt H99 einen Wert φ_H oder φ_O, der ein **ungerades Vielfaches von π/24**
ist (7, 15, 23, … in Einheiten π/24). Native Phasen sind Vielfache von π/6 = 4 · π/24. Mit nativen Werten von
φ_H und φ_O ist H99 in der Sektorformel also nicht erreichbar (Paritätsargument wie zuvor).

**3. Die Ladungsdifferenz ist 1, nicht 1/2.** In der Sektorformel trägt die Verbinder-Hyperladung (±1/2, Differenz 1),
nicht die Differenz von ℓ_L und e_R (1/2). Mit π/6 je Einheit ergibt sich θ_ν − θ_e = π/6, also der nächste native
Wert, der um π/12 neben H99 liegt.

**4. Die Spiegelung widerspricht den Quarks.** Im hermiteschen Fall folgt |θ_u| = |θ_e| = 0,221 (r11 bei M_Z: 0,052)
und mit H99 |θ_d| = |θ_ν| = 0,483 (r11: 0,100). Das war für die Up-Quarks schon bekannt; für die Down-Quarks ist es
mit H99 nachträglich neu und ebenso deutlich verfehlt.

**Bewertung.** Die Dixon-Sektorphase trägt die richtige Struktur (hyperladungsgebundenes Vorzeichen zwischen e und ν),
aber nicht den Fluss π/4: Mit nativen Phasen gibt sie Vielfache von π/6, und ihre Spiegelung auf die Quarks passt nicht
zu den Daten. In der einfachsten Form ist sie damit als Quelle ausgeschlossen. Offen bleiben ein je Sektor verschiedenes
h (dann keine Spiegelung mehr) und eine Quelle für die halbe Ladungsdifferenz (ℓ_L gegen e_R statt Verbinder).
OP3/OP4 offen; H100 unberührt.

## Nachtrag: halbe Ladungsdifferenz gesucht (13.11., Autor: „Halbe Ladungsdifferenz suchen“)

Vorwissen: Hyperladungstabelle aus r44 (Y/2: (ν, e)_L −1/2, e^c +1, ν^c 0; Higgs +1/2), r44.1(d) (Majorana-Verbinder
für ν^c ohne Higgs), Seesaw-Bemerkung in der v490-Schicht (Majorana-Masse für ν^c, über den Seesaw kleine
Neutrinomassen), Dixon-Nachtrag (Verbinder Y/2 = +1/2 für e, −1/2 für ν). Skript, Abschnitt 8. Nicht blind.

**Ansatz.** Nicht die Ladung eines der beiden Fermionen, sondern die Hyperladung des **Verbinders**, der die Plätze
koppelt, bestimmt die Phase: Mit dem nativen Winkel π/6 je Einheit Y/2 verschiebt ein Block seine Brannen-Phase um
(Y/2 des Verbinders) · π/6. Das ist unabhängig davon, welches Fermion man „transportiert“ denkt.

| Block | Verbinder | Y/2 | Verschiebung gegen geladen |
|---|---|---|---|
| geladene Leptonen, Dirac (ℓ H e^c) | H | +1/2 | 0 |
| Neutrinos, Dirac (ℓ H̃ ν^c) | H̃ | −1/2 | −π/6 |
| **Neutrinos, Majorana (Weinberg ℓℓHH, auch über Seesaw)** | **HH** | **+1** | **+π/12** |
| ν^c-Majorana allein (r44.1(d)) | – | 0 | −π/12 |

**Ergebnis.** Die halbe Ladungsdifferenz ist Y(HH) − Y(H) = 1 − 1/2 = 1/2: Ein Majorana-Neutrino braucht zwei
Higgs-Einsetzungen, ein geladenes Lepton eine. Mit π/6 je Einheit ergibt das genau die Verschiebung π/12 von H99,
mit dem richtigen Vorzeichen. Die 3/2 aus π/4 = (3/2) · π/6 lesen sich dann als drei Kanten mal eine zusätzliche
Higgs-Einsetzung mal deren Hyperladung 1/2.

**Gegenprobe ohne Anpassung.** Dieselbe Regel gibt für Dirac-Neutrinos (Verbinder H̃) den Betrag π/6. Das ist genau
der Wert, den die Dixon-Sektorphase im vorigen Nachtrag lieferte (Verbinder-Differenz 1). Beide Rechnungen stimmen
also überein, und der Unterschied zwischen ihnen ist Dirac gegen Majorana.

**Vorbehalte.**
- Nachträglich gefunden, nach gezielter Suche nach einer Differenz 1/2.
- Dass die Hyperladung eines Verbinders eine Phase auf den Kanten des Familiendreiecks erzeugt (π/6 je Einheit), ist
  eine Annahme ohne Mechanismus; sie verbindet Eichladung und Familienraum.
- Für einen symmetrischen (Majorana-)Block ist ein Fluss nicht wie bei einer hermiteschen Matrix definiert; die
  Rechnung benutzt die hermitesche Gram-Lesart der Neutrinos aus H99.
- Die Lesart sagt voraus, dass die Neutrinos Majorana-Teilchen sind. Mit Dirac-Neutrinos verschöbe sich die Phase um
  π/6; daraus folgende Werte für R sind nicht gerechnet und nicht mit Daten verglichen.

**Bewertung.** Die halbe Ladungsdifferenz hat eine strukturelle Quelle: die zweite Higgs-Einsetzung des
Majorana-Terms. Die Regel ist einfach, erklärt H99 und den Dixon-Befund zugleich, und sie ist nicht hergeleitet.
OP3/OP4 offen; H100 unberührt.

## Nachtrag: Mechanismus gesucht (13.11., Autor: „Mechanismus suchen“)

Vorwissen: r33 (Quaternionen-Richtungen i, j, k als Generationslabel ausgeschieden, weil nicht Q_em-invariant), r15
(Hopf-Faserung als Träger der Trialitätsplätze), Gram-Notiz (Hopf-Torus, Rand = koplanar, Rang 2), Status zu
thm:three-generations (Triplett e_4, e_5, e_6 und ν_R ↔ e_7 im inneren Frame J = L_e7). Skript, Abschnitt 9.

**1. Die Regel als Holonomie.** „π/6 je Kante und Einheit Y/2“ heißt: Der Umlauf über die drei Plätze trägt je
Einheit Y/2 den Faktor e^{iπ/2} = i, also die Komplexstruktur J. Ein Block mit Verbinder-Hyperladung y sieht J^y.
H99 ist dann J^1 / J^{1/2} = J^{1/2} = e^{iπ/4}. Die achte Einheitswurzel, die native Phasen nicht liefern, entsteht als
Wurzel aus J wegen der halbzahligen Hyperladung des Higgs. Pro Kante ist das ω · i⁻¹ = e^{iπ/6}, dessen Kubus i ist.

**2. Geometrische Quelle von π/4: das Oktanten-Tripel.** Drei Qubit-Zustände (Spin 1/2) entlang dreier orthogonaler
Achsen x, y, z haben (numerisch exakt):
- paarweise |Überlappung|² = 1/2, also **ρ² = 1/2 (Koide)**;
- Rang 2 (der Qubit-Raum ist zweidimensional), also **det S = 0 (Rand des Bogens)**;
- Bargmann-Phase **+π/4**, also **θ = π/12**; das ist der halbe Raumwinkel des Oktanten (π/2). Allgemein ist die
  Bargmann-Phase dreier Qubits der halbe Raumwinkel ihres sphärischen Dreiecks (numerisch 10⁻¹⁴).

Umgekehrt: Paarweise Überlappung 1/2 heißt paarweise orthogonale Bloch-Vektoren. **Das Rand-Tripel des Koide-Bogens
ist also bis auf eine Drehung genau das Oktanten-Tripel**; die Händigkeit (x, y, z gegen x, z, y) legt das Vorzeichen
fest (+π/4 gegen −π/4). Mit den Quaternionen i, j, k als −iσ ist die Händigkeit durch ijk = −1 festgelegt. Das ist
eine exakte Aussage, kein Datenvergleich.

**3. Mechanismus-Kandidat.** Der Weinberg-Term hat gegenüber dem Dirac-Term ein zusätzliches Higgs-Dublett, also ein
zusätzliches Qubit (schwacher Isospin). Zeigt dessen Richtung an den drei Plätzen entlang dreier orthogonaler Achsen
und wird es entlang der Kanten stetig transportiert (Berry-Zusammenhang auf geodätischen Bögen), trägt der Umlauf die
reine Phase π/4 ohne Betragsverlust. Das ist genau die verlangte Verschiebung, und es erklärt alle drei Zahlen der
Rand-Bedingung zugleich (Überlappung 1/2, Rang 2, Phase π/4).

**Was dagegen spricht oder fehlt.**
- r33: Richtungen i, j, k im Isospinraum sind nicht Q_em-invariant. Ein Higgs-Dublett, das an den drei Plätzen in
  verschiedene Isospin-Richtungen zeigt, bräche die elektrische Ladung je Platz. Das Qubit müsste ein anderes sein
  (etwa die Hopf-Faser aus r15) oder die Q_em-Frage anders gelöst werden.
- Ein Tensorprodukt mit dem Qubit-Tripel ist ausgeschlossen (K = 1/2); nur der stetige Transport (Holonomie) trägt.
  Warum der Transport stetig und nicht projektiv ist, ist nicht begründet.
- Warum die Orientierungen orthogonal sind, ist nicht hergeleitet; es ist die einzige Wahl mit Überlappung 1/2.
- Nachträglich, nach Kenntnis von π/4 gesucht.

**Bewertung.** Der Rand des Koide-Bogens hat eine exakte geometrische Bedeutung: drei Spin-1/2-Zustände entlang
orthogonaler Achsen. H99 liest sich damit als: Die Neutrino-Plätze tragen gegenüber den geladenen zusätzlich die
geometrische Phase eines solchen Oktanten-Tripels, passend zum zusätzlichen Higgs-Dublett des Majorana-Terms.
Lesart mit einem klaren Hindernis (Q_em, r33). OP3/OP4 offen; H100 unberührt.
