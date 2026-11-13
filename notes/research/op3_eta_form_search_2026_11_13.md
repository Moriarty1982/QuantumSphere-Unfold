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
