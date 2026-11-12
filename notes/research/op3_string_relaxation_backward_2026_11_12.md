# Rückwärtssuche: Was eine stabile ungleiche Stringaufteilung verlangt

12. November 2026 (abends). Autorenentscheidung: erst Rückwärtssuche, noch
keine Netzsimulation. Analytische, nicht blinde Erkundung. Einordnung
T8/T9/T13, OP3/OP5. Kein natives Companion-Gesetz, kein Hypothesentest,
keine neue H-/k-Nummer, kein MMA-Beleg, keine Änderung offener Guards.

## Ziel und Vorgehen

Ziel aus op3_string_relaxation_lambda_2026_11_12.md: drei gekoppelte
Strings sollen bei fester Außenlänge L eine stabile ungleiche Aufteilung
ell_1, ell_2, ell_3 wählen, möglichst durch unterschiedliche Relaxation
unter Expansion. Mit der Ausleseannahme sqrt(m_i)=c*ell_i wären die
Zielanteile der geladenen Leptonen (bekannte Werte, kein Test)

    ell_i/L = 0,01345 : 0,19341 : 0,79314,   K = sum ell_i²/L² = 0,66666.

Statt weitere Modelle vorwärts zu simulieren, werden hier die notwendigen
Bedingungen festgehalten, die jedes Modell erfüllen muss, und daraus
Modellklassen ausgeschlossen. „Stabil“ heißt: Attraktor, zu dem kleine
Störungen mit sum delta_i=0 zurückkehren.

## Vorwissen geprüft

Gesamtbild (T8, T9, T13), op3_string_length_exploration_2026_11_12.md
(statisches Gleichgewicht, q=4+3*sqrt(2)), op3_string_relaxation_lambda_
2026_11_12.md (Maxwell-Vergleich, offene Frage), OP3-Torusgrenze
(1/3<=K<=1/2 auf dem farbfesten Trialitätstorus), zurückgestellte Ideen
I1–I4. Suche in notes/research und analysis nach Erweichung, Lokalisierung,
nichtkonvexer Stringenergie, Verzweigung der Längenaufteilung: kein
Vorbefund. I3 bleibt durch den Lambda-Bezug berührt, wird hier nicht benutzt.

## B1. Gleiche Zugkraft

Bei frei umverteilbaren Längen mit sum ell_i=L (Reihenschaltung, bewegliche
Verbindungspunkte) gilt im Gleichgewicht F_1=F_2=F_3=lambda. Ungleiche
Längen können deshalb nie aus ungleichen Kräften kommen, nur aus
unterschiedlichem Materialzustand (Steifigkeit, Ruhelänge, Ast des
Kraftgesetzes). Ungleiche Kräfte verlangen eine Geometrie mit festen
Winkeln oder Führungen (Knoten); die ist weiter nicht festgelegt.

## B2. Konvexe Energie: Relaxationszeiten wählen nichts aus

Hat jeder String eine strikt konvexe Gleichgewichtsenergie U_i(ell_i) und
ist die Kinetik rein dissipativ, dann ist der Endzustand das eindeutige
Minimum von sum U_i unter der Nebenbedingung. Viskositäten und
Relaxationszeiten bestimmen nur den Weg dorthin, nicht das Ziel. Für das
lineare Standardmodell (Gleichgewichtsfeder k_i^inf parallel zu einem
Maxwell-Arm) ist das wieder die Aufteilung der statischen Notiz,
ell_i - r_i^inf proportional 1/k_i^inf, unabhängig von allen tau_i.
Sind die drei Strings gleich, folgt ell_i=L/3 und K=1/3.

Folgerung: „unterschiedlich schnell relaxieren“ kann in dieser Klasse
keine Aufteilung wählen. Die Ungleichheit steckt vollständig in den
Gleichgewichtsmoduln, also in eingesetzten Materialdaten.

## B3. Reiner Maxwell-String: Aufteilung hängt an der Vorgeschichte

Ohne Gleichgewichtsfeder (das Modell der Notiz vom Mittag) gilt bei fester
Summe mit c=sum 1/k_j, f=sum 1/eta_j:

    lambda(t) = lambda(0) * exp(-f t/c),
    ell_i(inf) = r_i(0) + (L - sum_j r_j(0)) * (1/eta_i)/f.

Die Kraft fällt auf null; die Endaufteilung ist die anfängliche Ruhelänge
plus ein Anteil des Überschusses nach Fluidität 1/eta_i. Für r_i(0)=0 ist
ell_i(inf)/L=(1/eta_i)/f, unabhängig von den Steifigkeiten. Hier bestimmt
die Relaxation tatsächlich die Aufteilung, aber:

- Jede Aufteilung mit ell_i=r_i ist kraftfreies Gleichgewicht. Es gibt ein
  Kontinuum neutraler Zustände, keinen Attraktor. Eine Störung wird nur
  teilweise zurückgeführt und hinterlässt eine neue Aufteilung.
- Das Verhältnis ist das eingesetzte Verhältnis der eta_i (K=2/3 bei
  q:1:1 wieder mit q=4+3*sqrt(2), jetzt für die Fluiditäten).
- Die gesamte elastische Energie U(0)=(L-sum r_j(0))²/(2c) wird
  dissipiert. Am Ende trägt kein String Zugkraft; eine Auslesung, die an
  Spannung oder gespeicherter Energie hängt, hat dann keinen Träger.

## B4. Echter Attraktor nur bei wachsender Außenlänge

Wächst die Summe mit dem Skalenfaktor, L(t)=L_0*exp(Ht) (de Sitter), so
löst lambda=H*L/(H*c+f) die Bilanz, und die Anteile laufen unabhängig von
den Anfangsdaten (Abweichung fällt wie 1/a) gegen

    ell_i/L -> (1/eta_i + H/k_i) / (f + H*c).

Das ist die einzige hier gefundene Stelle, an der die Expansionsrate H
selbst in die Aufteilung eingeht: für H*tau_i<<1 zählt die Fluidität, für
H*tau_i>>1 die elastische Nachgiebigkeit. Aber die Voraussetzung
widerspricht der festen Außenlänge (ein de-Sitter-Horizontumfang ist
konstant), gleiche Strings geben wieder 1/3, und die Zugkraft wächst
proportional L. Die Expansion leistet die Arbeit lambda*dot(L); davon wird
sum lambda²/eta_i dissipiert, der Rest gespeichert. Diese Leistung müsste
in der Friedmann-Bilanz erscheinen und ist nicht gerechnet.

Bei fester Summe gibt es keinen Antrieb: sum dot(ell_i)=0. Ein
stationärer getriebener Zustand bräuchte dann schrumpfende Ruhelängen
oder zeitabhängige Moduln als zusätzliche, bisher unbegründete Kopplung.

## B5. Gleiche Strings: ungleiche Aufteilung nur durch Symmetriebruch

Die drei Strings sind im Companion durch Trialität verbunden; unabhängig
begründete ungleiche Materialdaten gibt es nicht. Mit gleichen Strings
folgt aus B1: F(ell_1)=F(ell_2)=F(ell_3) für ein und dasselbe Kraftgesetz
F. Ungleiche Längen verlangen daher ein nicht monotones F, also eine
nicht konvexe Energie (Erweichung jenseits einer Länge ell_c).

Stabilität: Die Hesse-Form sum F'(ell_i)*delta_i² auf sum delta_i=0 ist
genau dann positiv definit, wenn alle F'>0 sind oder genau ein F'<0 ist
und sum 1/F'(ell_i)<0 gilt. Zwei Strings auf fallenden Ästen sind immer
instabil.

- **Ein Höcker** (F steigt, dann fällt): Eine Kraft hat höchstens zwei
  Urbilder. Die einzigen stabilen gebrochenen Zustände haben die Form
  (lang, kurz, kurz): zwei gleiche Längen, also zwei gleiche Massen. Das
  Leptonspektrum ist damit ausgeschlossen, K=2/3 nicht. K ist dann eine
  Funktion von L/ell_c allein; K=2/3 legt diese eine Zahl fest. Beispiel
  F=ell*exp(-ell/ell_c): kurz=ln(q)/(q-1)*ell_c=0,29124 ell_c,
  L=2,98303 ell_c, Hesse-Eigenwerte 0,092 und 0,530 (stabil). Beim selben
  L ist auch der symmetrische Zustand stabil (F'(L/3)>0): Koexistenz, die
  Vorgeschichte entscheidet.
- **Drei verschiedene Längen** verlangen, dass F denselben Wert an drei
  Stellen annimmt: mindestens zwei Umkehrpunkte (steigt, fällt, steigt).
  Stabil ist die Belegung je ein String auf den beiden steigenden Ästen
  und einer auf dem fallenden, mit 1/|F'_fall| > 1/F'_a + 1/F'_b. Der
  zweite steigende Ast ist zugleich der gesuchte Mechanismus, der die
  Relaxation begrenzt.

Ein solches Kraftgesetz lässt sich zu jedem Zieltripel konstruieren. Die
drei Leptonanteile wären dann drei abgelesene Punkte einer frei gewählten
Kurve, keine Herleitung.

## Was die Rückwärtssuche ausschließt und was bleibt

Ausgeschlossen als Auswahlmechanismus bei fester Außenlänge:

1. unterschiedliche Relaxationszeiten bei konvexer Energie (B2);
2. reine Maxwell-Relaxation als stabile Wahl (B3: neutral, kraftfrei);
3. Expansion als Antrieb, solange die Summe fest ist (B4);
4. gleiche Strings mit einhöckrigem Kraftgesetz für drei verschiedene
   Längen (B5).

Übrig bleiben genau drei Wege, jeder mit einer benannten Lücke:

- **W-a, ungleiche Strings:** verlangt eine native Herkunft ungleicher
  Gleichgewichtsmoduln. Die Trialität spricht dagegen.
- **W-b, gleiche Strings mit zweifach umkehrendem Kraftgesetz:** verlangt
  eine native Stringenergie mit zwei Umkehrpunkten und die Zahl L/ell_c.
  Die Rolle der Expansion wäre dann nur, L/ell_c über die Schwelle zu
  führen; die Kinetik entscheidet, welcher String auf welchen Ast fällt.
- **W-c, andere Geometrie:** Knoten mit festen Winkeln oder Wicklungen,
  bei denen B1 nicht gilt. Die Torusgrenze K<=1/2 und die Dreiecksgrenze
  der statischen Notiz stehen dem bisher entgegen.

Die fehlende native Operation ist damit benannt: eine nicht konvexe
Energie des einzelnen Strings (oder eine Herkunft ungleicher Moduln) aus
dem Companion. Ohne sie ändert weitere Simulation von Maxwell-Netzen
nichts. Die Frage aus Version 5 bleibt offen; für die Maxwell-Klasse bei
fester Außenlänge ist sie negativ beantwortet. Weder Lambda noch Koide 2/3
oder das Leptonspektrum folgen daraus. OP1–OP5, C5, C6/T2 unverändert.

## Selbstprüfung

op3_string_relaxation_backward_2026_11_12.py (Python, scipy) prüft die
Formeln aus B3 und B4 an zufälligen Materialwerten gegen die integrierten
Gleichungen (Abweichung 7e-13 bzw. 3e-13), das Ein-Höcker-Beispiel aus B5
(K=2/3 auf zwölf Stellen, Hesse-Eigenwerte, sum 1/F'=-4,10) und die
Leptonanteile. B1, B2 und das Stabilitätskriterium sind elementar
(Lagrange-Bedingung, Trägheit einer Diagonalform auf einer Hyperebene)
und nur am Beispiel gegengeprüft. Keine externen Quellen neu gelesen.
