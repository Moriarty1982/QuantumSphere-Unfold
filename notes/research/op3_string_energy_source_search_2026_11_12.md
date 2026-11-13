# Weg W-b: Quellensuche nach einer nicht konvexen Stringenergie

12. November 2026 (abends). Autorenentscheidung: „versuche erst W-b“.
Quellenauftrag mit analytischer, nicht blinder Erkundung. Einordnung
T8/T11/T13, OP3. Kein natives Companion-Gesetz, kein Hypothesentest, keine
neue H-/k-Nummer, kein MMA-Beleg, keine Änderung offener Guards.

## Auftrag

Nach op3_string_relaxation_backward_2026_11_12.md (B5) brauchen drei
gleiche Strings für drei verschiedene Längen bei gleicher Zugkraft ein
Kraftgesetz mit mindestens zwei Umkehrpunkten. Gesucht: eine solche
Energie und die Zahl L/ell_c in den Companion-Quellen.

## Vorwissen geprüft

Die Rückwärtssuche vom selben Tag, op3_string_length_exploration,
op3_gram_torus_bound (K<=1/2 auf dem farbfesten Torus), v4.9.0-r44.1(e)
(Zirkulante und Brannen-Form), v4.11-Abschnitt zur Koide-Phase
(zulässiger Bogen), zurückgestellte Ideen I1–I4. Volltextsuche in
sources/ (alle .tex) nach string tension, Nambu, winding, Regge, flux
tube, string breaking, T-dual, Hagedorn, elastic, stiffness, spring,
quartic, cosh, condensat, circulant, Brannen, cubic.

## Befund 1: Der Companion hat keine Stringenergie als Funktion einer Länge

- „String“ steht im Companion für den Zählparameter
  gamma_string=ln2/(pi*sqrt(3)) (Horizontzählung mit j=1/2, r03 F11a) und
  für den symmetrischen Sektor in thm:string-lqg-duality (T11, eine
  Lesart). Stringspannung, Wicklung, Nambu–Goto-Wirkung oder ein
  Kraft-Längen-Gesetz kommen in den Quellen nicht vor; die einzigen
  Treffer liegen im v5-Abschnitt zur offenen Frage selbst (dazu eine
  Stelle zur Verschlingung zweier Fasern ohne Energiebezug).
- thm:spring (Feder-Satz): Materie–Photon–Tachyon mit linearen Federn in
  z^-, ungedämpft (r18: „ein Gleichgewicht, keine Relaxation dorthin“).
  Linear heißt konvex; nach B2 wählt das keine ungleiche Aufteilung. Die
  drei Glieder sind Frames, keine drei Generationen. Nachträglich: die
  Amplituden 1:1:3 hätten als Längenanteile K=11/25=0,44.
- W2 (r82.1): Higgs-Potential V=-mu²|Phi|²+lambda|Phi|⁴. Das ist die
  einzige nicht konvexe Energie der Quellen mit begrenzendem zweiten Ast.
  Sie ist eine Eingabe (Standardmodell), gilt für ein Feld und nicht für
  eine Länge, und das Vorzeichen von -mu² ist als tachyonischer
  Übergangs-Konnektor q²=-2m²sinh(2 eta) gelesen, nicht hergeleitet
  (r81.9(c)). Der Geist-Term cX² (r83.4) ist ebenfalls Eingabe.
- I1 (String als Brücke zwischen Systemen) ist eine zurückgestellte Idee
  ohne Wirkung; Auslöser 3 (gamma_string) ist berührt, mehr nicht.

Damit ist W-b als Quellenauftrag negativ: Eine native Stringenergie mit
zwei Umkehrpunkten und eine native Länge ell_c gibt es nicht.

## Befund 2: Die kleinste solche Energie ist die Brannen-Form in anderer Schreibweise

Das einfachste Kraftgesetz mit zwei Umkehrpunkten ist kubisch, die
Energie also ein quartischer Doppeltopf um eine Mitte ell_0:

    U(ell) = (lam/4) ((ell-ell_0)² - v²)²,
    F(ell) = lam (ell-ell_0) ((ell-ell_0)² - v²).

Gleiche Zugkraft f bei drei verschiedenen Längen heißt: x_i=ell_i-ell_0
sind die drei reellen Wurzeln von x³ - v² x - f/lam = 0. Diese Wurzeln
haben Summe null und die Form

    ell_i = ell_0 + (2v/sqrt(3)) cos(theta + 2 pi i/3),
    f = lam (2v/sqrt(3))³ cos(3 theta) / 4.

Folgen:

1. **Mitte erzwungen.** sum ell_i=L verlangt ell_0=L/3. Liegt der Topf
   nicht genau bei L/3, gibt es kein Gleichgewicht mit drei verschiedenen
   Längen; die Minima haben dann zwei gleiche Längen (geprüft).
2. **Brannen-Form exakt.** Mit ell_0=L/3 ist
   ell_i=(L/3)(1+(2 sqrt(3) v/L) cos(theta+2 pi i/3)) und
   K = 1/3 + 2 v²/L². K=2/3 genau für v=L/sqrt(6). Das ist die Bedingung
   |b|=a/sqrt(2) aus r44.1(e) mit a=L/3, |b|=v/sqrt(3): Die Kraftgleichung
   ist die charakteristische Gleichung einer hermiteschen Zirkulante.
3. **Phase bleibt frei.** Auf dem Kreis sind sum x_i² und sum x_i⁴
   konstant, die Energie also exakt entartet in theta. Die radiale Mode
   ist stabil (Hesse-Eigenwert 2 lam v²), theta ist neutral. Die
   Lepton-Phase theta=0,22223 (cos 3theta=0,786) wird nicht gewählt; sie
   entspräche einer bestimmten Zugkraft f, die das Modell nicht festlegt.
4. **Positive Längen.** v=L/sqrt(6) heißt v/ell_0=sqrt(3/2)>1: der untere
   Topf liegt bei negativer Länge. Positive Längen verlangen
   |theta|<=pi/12 (modulo 2 pi/3), derselbe Bogen wie im v4.11-Abschnitt.
   Die Leptonen liegen darin (0,2222 < 0,2618), nahe am Rand.
5. **Jenseits der Quartik.** Für gleiche Strings hängt die Energie auf der
   Ebene sum ell_i=L nur von sum x_i² und e_3=x_1 x_2 x_3 ab. Zusatzterme
   heben die Entartung auf: x⁶ allein wählt cos 3theta=0, ein genügend
   großer x⁵-Term wählt cos 3theta=±1 (zwei gleiche Längen), dazwischen
   liegt theta bei einem von den Koeffizienten bestimmten Wert (Beispiel
   cos 3theta=-0,49). K und theta sind dann beide durch die Form von U
   und L/ell_c festgelegt: zwei Zielzahlen gegen mindestens zwei
   Formzahlen.

## Bewertung

- Der W-b-Mechanismus kann in seiner kleinsten Form genau das, was die
  Zirkulante in r44.1(e) kann: Brannen-Form mit freiem |b|/a und freiem
  theta. Die Stringsprache fügt keine Information hinzu; die offenen
  Größen heißen nur v/L und f statt |b|/a und theta.
- Die Expansion spielt in diesem Bild keine Rolle für die Auswahl. Wegen
  der neutralen Phase würde Dissipation theta dort stehen lassen, wo die
  Vorgeschichte es hinlegt (wie B3).
- Zusätzlich nötig und nicht nativ: Topfmitte genau bei L/3 (oder eine
  Energie, die nur von ell_i - L/3 abhängt, also keine Eigenschaft des
  einzelnen Strings ist), v/L=1/sqrt(6), ein Wert für f, und die
  Auslesung sqrt(m_i)=c ell_i.
- Lesart mit W2: Würde man die Abweichungen x_i als Feldwerte in einem
  gemeinsamen quartischen Potential lesen, gäbe W2 die Form, aber weder
  das Verhältnis v/L noch die Phase; das wäre eine neue Identifikation
  und bleibt hier ausdrücklich ungenutzt.

Ergebnis: W-b liefert keine native Operation und führt auf den bekannten
offenen Punkt aus r44 zurück (Verhältnis |b|/a und Phase theta, OP3/OP4).
Weder Koide 2/3 noch die Phase oder das Leptonspektrum sind hergeleitet.
Die Stringfrage aus Version 5 bleibt offen. OP1–OP5, C5, C6/T2
unverändert.

## Was danach bleibt

- W-a (ungleiche Moduln) und W-c (Knotengeometrie) sind ungeprüft.
- Eine enger gefasste Quellenfrage wäre lohnender als weitere
  Stringmodelle: Gibt es im Companion eine Größe, die auf dem Brannen-
  Kreis von e_3 abhängt (also theta sieht) und deren Extremum nicht bei
  zwei gleichen Massen liegt? Das ist die Phasenfrage von OP3 in der
  Sprache dieser Notiz.

## Selbstprüfung

op3_string_energy_source_search_2026_11_12.py: Kreis der Gleichgewichte
(Kraftdifferenz 4e-17, K=2/3 auf zwölf Stellen, Energieschwankung 9e-18,
Hesse flach 2e-16 und radial 0,333333=2 lam v²); Topf neben L/3 gibt in
200 Minimierungen stets zwei gleiche Längen (Abstand <= 4e-8);
Zusatzterme wie in Punkt 5; Leptonwerte (Amplitude 1,414201, theta
0,222230). Die Suchbegriffe stehen im Abschnitt
„Vorwissen geprüft“; gelesen wurden thm:spring, thm:koide-triolic,
thm:string-lqg-duality, r18, r44.1(e), r81.9, r82.1, r83.4 und der
v4.11-Abschnitt zur Koide-Phase. Keine externen Quellen.

## Nachtrag (12.11., später am Abend): übersehenes Vorwissen

Der Abschnitt „Vorwissen geprüft“ oben war unvollständig. Nicht genannt
wurden v4.8.0-r10 bis r12, r16 (H11), v4.9.0-r26 (H16, r26.1), r45 sowie
koide-and-kernel, generation-coupling und coupling-scale-candidate. Sie
enthalten die Brannen-Form, die freie Phase und das Scheitern
symmetrischer Potentiale bereits. Einordnung und Folgerung stehen in
op3_phase_source_search_2026_11_12.md.
