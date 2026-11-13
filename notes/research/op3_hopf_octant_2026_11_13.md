# Erkundung: Das Oktanten-Tripel im Hopf-Träger von r15

13. November 2026, spät. Autorenauftrag: „Hopf-Faser prüfen“. Anlass: Das Rand-Tripel des Koide-Bogens ist das
Oktanten-Tripel dreier Qubits (`op3_eta_form_search_2026_11_13.md`, Nachtrag Mechanismus); als Isospin-Richtungen
scheitert es an r33 (Q_em). Erkundung, analytisch mit numerischer Prüfung, nicht blind (Ziel π/4 bekannt), kein
Datenvergleich. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T5/T8, OP3.
Skript `op3_hopf_octant_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- v4.8.0-r15: Plätze als Einheits-Oktonionen (a, b, c) mit (ab)c = 1; symmetrischer Punkt a = b = c mit a³ = 1,
  a = exp(2πu/3); für u = e_7 bricht er G_2 auf die Farb-SU(3). Direkte Lesart der Koide-Phasen als diese Phasen
  scheiterte (3δ ≡ 0 gegen δ = 0,2222).
- r14 (Trialitätsplätze als Generationsindex), r33 (Isospin-Richtungen nicht Q_em-invariant), Status zu
  thm:three-generations (J = L_e7, e_7 als Ladungsachse im inneren Frame).
- Gram-Notiz (Rand des Bogens = koplanar, Rang 2), η-Notiz (Fluss π/4, Oktanten-Tripel).

## Ergebnis

**1. (ab)c = 1 ist das Schließen einer Schleife.** Liest man die Platz-Oktonionen als Transport, liegt nach k Schritten
die Richtung p_k = s_k f s_k⁻¹ mit s_1 = a, s_2 = ab, s_3 = (ab)c. Die Bedingung von r15 heißt dann: Nach drei
Schritten ist man zurück. Am symmetrischen Punkt ist jeder Schritt dieselbe Konjugation mit a = exp(2πe_7/3).

**2. Dieser Schritt ist Q_em-verträglich.** Numerisch (10⁻¹⁴): Die Konjugation mit a ist ein Automorphismus der
Oktonionen, fixiert e_7 und vertauscht mit L_e7. Auf dem Komplement von e_7 wirkt sie als Drehung um 4π/3 in jeder
komplexen Ebene (g, e_7 g), also als Skalar ω² auf C³: das Zentrum der Farb-SU(3). Sie vertauscht mit allem
Elektroschwachen.

**3. Das Oktanten-Tripel entsteht am magischen Winkel.** Für f = (e_7 + √2 g)/√3 mit g ⊥ e_7, also unter dem Winkel
arccos(1/√3) = 54,7° zur Ladungsachse, sind f, a f a⁻¹, a² f a⁻² paarweise orthogonal und spannen eine assoziative
(quaternionische) Unteralgebra auf (f_0 f_1 = ± f_2). Nach drei Schritten ist man wieder bei f. Andere Winkel geben
keine Orthogonalität (⟨h, Ch⟩ = −0,50; −0,37; 0; +0,46 für cos = 0; 0,3; 1/√3; 0,8). Die Ladungsachse e_7 ist die
Raumdiagonale dieses Oktanten.

**4. Als Qubits gelesen** (Bloch-Kugel der quaternionischen Unteralgebra): ρ² = 1/2, Rang 2, Bargmann-Phase π/4 im
Betrag (Vorzeichen durch die Orientierung). Das ist genau das Rand-Tripel des Koide-Bogens.

## Bewertung
- Der Hopf-Träger von r15 enthält das Oktanten-Tripel: Am symmetrischen Generationspunkt a = exp(2πe_7/3) erzeugt der
  Transport aus jeder Richtung unter dem Winkel arccos(1/√3) zur Ladungsachse genau die Konfiguration mit Überlappung
  1/2, Rang 2 und Phase π/4. Der Schritt ist das Farbzentrum und damit Q_em-verträglich. **Das Hindernis aus r33
  entfällt** für diesen Träger, weil nicht im Isospinraum gedreht wird, sondern um die Ladungsachse.
- Die Lesart von H99 wird damit: Die Neutrino-Plätze tragen gegenüber den geladenen zusätzlich die geometrische Phase
  dieses Transports.
- Nicht hergeleitet:
  - warum eine Richtung gerade unter dem magischen Winkel steht (gleichwertig: warum die Ladungsachse Raumdiagonale
    eines assoziativen Dreibeins ist);
  - warum nur der Majorana-Block die Phase trägt (Anschluss an die zweite Higgs-Einsetzung offen);
  - ob der Transport stetig (Holonomie, reine Phase) oder projektiv (mit Beträgen) wirkt;
  - r14 trennt Farbe und Generation; hier wird das Zentrum der Farb-SU(3) als Generationsschritt gelesen, wie r15 es
    mit dem symmetrischen Punkt vorschlägt. Ob das mit r14 verträglich ist, ist zu prüfen.
- Nachträglich, mit bekanntem Ziel. OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nächste Fragen
- Gibt es im Companion eine native Richtung unter dem Winkel arccos(1/√3) zu e_7 (etwa aus dem Assoziator
  [e_4, e_5, e_6] = −2e_7, dessen drei Faktoren mit e_7 ein Dreibein bilden könnten)?
- Wie hängt diese Richtung am Majorana-Verbinder für ν^c (r44.1(d)) oder an der zweiten Higgs-Einsetzung?

## Nachtrag: magischer Winkel gesucht (13.11., spät, Autor: „Magischen Winkel suchen“)

Skript, Abschnitte „Magischer Winkel“ und „Neutrale Dixon-Richtungen“. Nicht blind, kein Datenvergleich.

**1. Der Winkel ist keine eigene Zahl.** Eine 120°-Drehung, die ein Orthonormal-Dreibein zyklisch vertauscht, hat
dessen Raumdiagonale als Achse; jeder Vektor des Dreibeins steht dann unter arccos(1/√3) zur Achse. Die Forderung
„magischer Winkel zur Ladungsachse“ ist also gleichwertig mit: **Die drei Platzrichtungen sind orthonormal**, und der
Generationsschritt aus r15 (Drehung um e_7) vertauscht sie. Ein natives Beispiel ist die Raumdiagonale einer
Fano-Linie durch e_7, etwa (e_1 + e_6 + e_7)/√3 (Winkel zu e_7 genau arccos(1/√3)).

**2. Im Oktonionenfaktor kostet das die Farbe.** Die einzige imaginäre Richtung, die die Farb-SU(3) festhält, ist e_7
(numerisch). Jede Richtung unter dem magischen Winkel hat daher Farbanteile. Der Stabilisator in G_2 fällt von 8
(SU(3), nur e_7 fest) auf 3 (e_7 und f fest, ebenso für die Fano-Diagonale): Als Feldwert gelesen bräche eine solche
Richtung die Farbe auf SU(2). Das Hindernis aus r33 (Ladung, Isospinfaktor) kehrt im Oktonionenfaktor als
Farbhindernis wieder. Unschädlich ist es nur, wenn die Platzrichtungen reine Etiketten des Trägers sind und kein
Feldwert.

**3. Der neutrale Teil des Dixon-Raums hat die Signatur (2,1).** Die farb- und ladungsneutralen Richtungen e_3⊗1,
1⊗e_7 und e_3⊗e_7 haben die Quadrate −1, −1, +1. Das ist genau die indefinite Signatur, die die negative
Neutrino-Wurzel verlangt. In Signatur (2,1) gibt es aber keine drei paarweise orthogonalen raumartigen
Einheitsvektoren; ein exakter Oktant ist dort nicht möglich. Eine Lorentz-Fassung (Phase als hyperbolische Fläche)
wäre eine eigene Rechnung.

**Bewertung.**
- Der magische Winkel ist auf die Bedingung „orthonormale Platzrichtungen“ zurückgeführt; native Kandidaten dafür
  gibt es (Fano-Diagonalen).
- Ein Ort, an dem das Oktanten-Tripel zugleich farb- und ladungsneutral wäre, ist nicht gefunden: Im Isospinfaktor
  bricht es die Ladung (r33), im Oktonionenfaktor die Farbe, im neutralen Teil verhindert die Signatur (2,1) den
  exakten Oktanten.
- Die Signatur (2,1) des neutralen Teils passt dafür zur negativen Wurzel; ob eine Lorentz-Fassung der Bargmann-Phase
  dort π/4 geben kann, ist die nächste offene Rechnung.
- OP3/OP4 offen; H100 unberührt.
