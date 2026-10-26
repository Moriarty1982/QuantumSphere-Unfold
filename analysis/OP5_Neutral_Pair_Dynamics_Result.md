# OP5: konstruktiver Versuch einer neutralen Paardynamik

Datum: 26. Oktober 2026. Checkpoint: `OP5-PAIR-DYNAMICS-2026-10-26`.
Basis: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Der vorherige Frame-/Lambda-Audit wurde auf Wunsch des Autors auf einem
Forschungszweig committed, per Fast-forward nach main übernommen und zu
origin/main gepusht. Dieser Text dokumentiert die anschließende Forschung.
Keine Änderung an den mathematischen Aussagen des Papers oder den Releases.

## Auftrag und präziser Ertrag

Untersucht wurde, ob aus dem Paarbezug eine konkrete Dynamik entsteht, die
einen neutralen Zustand erzeugt, einen relativen Abstand stabilisiert und
einen kosmologischen Vakuumbeitrag bestimmt.

Die ersten beiden Aufgaben lassen sich in ausdrücklich deklarierten
Vergleichsmodellen konstruktiv erfüllen. Die dritte folgt daraus nicht:
dieselbe neutrale Konfiguration verträgt unterschiedliche konstante
Vakuumenergien. Diese Unbestimmtheit wurde in einer gemeinsamen
metrikabhängigen Skalarwirkung ausdrücklich nachgewiesen.

Die Kanaldynamik und die Skalarwirkung sind **zwei getrennte Konstruktionen**.
Eine native Abbildung zwischen Dichtematrix, Paarrapidität und Raumzeitwirkung
wurde nicht erfunden. Die Skalarwirkung ist ein gebauter positiver Kontrollfall,
keine aus dem Framework abgeleitete Wechselwirkung.

## Route A: Dynamik, die einen neutralen Zustand tatsächlich erzeugt

Mit der korrigierten Gegenabbildung U=sigma_y auf dem realen Zustandsdisk ist

\[
\dot\rho=k(U\rho U-\rho),\qquad k>0
\]

eine vollständig positive spurtreue Markov-Dynamik. Die Lösung lautet

\[
\rho(t)=(1-p(t))\rho_0+p(t)U\rho_0U,
\quad p(t)=\frac{1-e^{-2kt}}2.
\]

Der Bloch-Vektor auf diesem Disk schrumpft mit exp(-2kt). I/2 ist dort der
eindeutige Attraktor. Außerhalb des realen Disks bleibt die sigma_y-Komponente
erhalten; auf dem gesamten Bloch-Ball ist I/2 daher nicht eindeutig.
Das ist eine nützliche und explizite Bereichsgrenze.

Die Gleichgewichtsmischung wurde nicht einfach vorausgesetzt: Für zwei
klassische Präparationslabels mit Raten a und b ist die stationäre
Asymmetrie (b-a)/(a+b). Die neutrale Mischung folgt genau bei gleichen Raten
(oder bereits neutralen Eingaben). Die Symmetrie bzw. ihr mikroskopischer
Mechanismus muss deshalb nativ begründet werden. Eine thermische Auslegung
erfordert zusätzlich eine Energiebilanz und detailliertes Gleichgewicht.

Eine endliche Wechselwirkung mit einem zweiten Quantensystem kann I/2 auf
dem Disk sogar exakt erzeugen:

\[
W_\theta=\exp[-i\theta(\sigma_y\otimes\sigma_x)],
\quad \rho_{\rm ancilla}=|0\rangle\langle0|,
\]

\[
\operatorname{Tr}_{\rm ancilla}
[W_\theta(\rho\otimes\rho_{\rm ancilla})W_\theta^\dagger]
=\cos^2\theta\,\rho+\sin^2\theta\,U\rho U.
\]

Bei theta=pi/4 ist das Ergebnis I/2. Ein geschlossenes Ancilla-System kehrt
aber später zurück; es ist kein irreversibler Attraktor. Irreversible
Markov-Zeit benötigt Reservoir-/Erneuerungsannahmen, und ihr exakter Nullzustand
wird aus einem nichtneutralen Start nur asymptotisch erreicht.

Die reduzierte radiale Abbildung ist in r28 bereits als Partial-Swap mit dem
Gegenzustand enthalten. Hier wurden die kontinuierliche Dynamik, ein eigener
expliziter Ancilla-Aufbau und die Grenzen dieser Interpretation ausgearbeitet.
Es wäre falsch, dies als neue native Herleitung oder als identisch mit dem
allgemeinen r27-Rotations-/Messkanal auszugeben.

Die vollständige Ableitung und exakte Kontrollen stehen in
[OP5_Neutral_Pair_Dynamics.md](OP5_Neutral_Pair_Dynamics.md) und
[OP5_Neutral_Pair_Dynamics_Check.py](OP5_Neutral_Pair_Dynamics_Check.py).

## Route B: Ein stabiler nichtverschwindender Paarabstand

Der einfache vorher geprüfte Ansatz V(chi)=M^4 tanh²(chi/2) hatte bei endlichem
chi nur den stationären Punkt null. Um konstruktiv zu unterscheiden, ob ein
nichtverschwindender Paarabstand prinzipiell stabilisierbar ist, wurde eine
positive Matching-Strafe als **zusätzliche Vergleichswirkung** gebaut:

\[
S_C=\int d^4x\sqrt{-g}\left[
A R-\frac{f^2}{2}\sum_{i=1}^2(\nabla\eta_i)^2
-C-\lambda f^4\big(\cosh(\eta_1-\eta_2)-g_0\big)^2\right].
\]

Konventionen: Signatur (-,+,+,+), c=hbar=1, A>0, f>0, lambda>0 und g_0>1.
eta_i sind dimensionslose Vergleichsskalare, keine behaupteten nativen
raumzeitlichen Tachyonbeobachter. g_0 ist ein vorgegebener dimensionsloser
Vergleichswert. Die Potentialform wurde gerade zur Realisierung der gewünschten
Relation gewählt; ihre Existenz ist keine Vorhersage und kein Beleg für eine
native Wechselwirkung.

Mit N=(eta_1+eta_2)/2 und chi=eta_1-eta_2 hängt das Potential nur von chi ab.
Es ist invariant unter Austausch und gemeinsamem Shift. Seine Minima sind

\[
\chi_*=\pm\operatorname{arcosh}g_0,
\qquad
q_{\rm rel}=\tanh^2(\chi_*/2)=\frac{g_0-1}{g_0+1}.
\]

Der gemeinsame Mittelpunkt N bleibt frei. Das ist bei einer relationalen
Definition erwünscht: Die Theorie zeichnet keinen absoluten Wert N=0 aus.
Die relative Richtung ist dagegen stabil. Die kanonisch normierten
Feldkoordinaten sind Phi_N=sqrt(2) f N und Phi_chi=f chi/sqrt(2). Die Massen sind

\[
m_N^2=0,\qquad m_\chi^2=4\lambda f^2(g_0^2-1)>0.
\]

Der stationäre Punkt chi=0 hat für g_0>1 negative Potentialkrümmung und ist
nicht das stabile Paarminimum. Es gibt also einen vollständig ausgeschriebenen
Vergleich mit stabilem, nichtverschwindendem relativem Abstand und neutralem
gemeinsamem Mittelpunkt. Das ist eine lokale Baumebenen-/Skalarkontrolle,
keine globale oder quantenmechanische Stabilitätsaussage.

Mit dem historischen Input g_0=1.864441... ergibt sich chi_*=1.234895... und
q_rel=0.3017835..., wie zuvor. Diese Übereinstimmung ist eingebaut, nicht
unabhängig erklärt.

## Route C: Weshalb diese Dynamik Lambda noch nicht festlegt

Am konstanten Paarminimum verschwinden die Gradienten und die Matching-Strafe.
Der Potentialwert ist exakt C. Die Skalarfeldgleichungen und ihre relative
Massenmatrix sind unabhängig von C. Die Metrikvariation ergibt dagegen

\[
G_{\mu\nu}+\frac{C}{2A}g_{\mu\nu}=0,
\quad \Lambda_{\rm cos}=\frac{C}{2A},\quad R=\frac{2C}{A}.
\]

Dieselben konstanten neutralen Paarfelder können daher zu lokalen Einstein-
Raumzeiten mit negativem, verschwindendem oder positivem Lambda gehören.
Die Prüfung hat für drei Mittelpunkte und drei Potentialhöhen dieselbe
relative Konfiguration bei jeweils anderer Krümmung kontrolliert. Die
beliebigen Beispielhöhen -1,0,1 sind keine physikalischen Messwerte.

Das ist ein konkreter Unbestimmtheitsnachweis für diesen Aufgabenvertrag:
**Neutralität, Austausch-/Shift-Symmetrie und relative Stabilität bestimmen
nicht allein die absolute Vakuumhöhe.** Ein Zusatz C ändert die ausdrücklich
ausgeschriebene gravitative Theorie; er wird nicht als bedeutungslose
Umdefinition innerhalb einer festgelegten Wirkung ausgegeben. Ohne eine
zusätzliche native Vorgabe lassen die internen Bedingungen aber diese
verschiedenen gravitativen Vervollständigungen zu.

Dasselbe zeigt die Kanaldynamik: H->H+C I ändert keine Mischgleichung und
keine normierten Zustandswahrscheinlichkeiten, verschiebt jedoch den mittleren
Energiewert. Neutralität des Zustands kann deshalb dessen absolute Energie
nicht festlegen. Für einen H, der mit U kommutiert, kann die Mischung sogar
bei erhaltener Systemenergie verlaufen. Andernfalls muss Energieaustausch mit
Umgebung und Wechselwirkung bilanziert werden.

Eine native Vorschrift könnte diese Freiheit einschränken. Die geprüften
Quellen liefern diesen Zusatz derzeit nicht. Die tatsächlichen positiven
Closure-Strafen setzen ihren eigenen klassischen Minimalbeitrag auf null;
die Closurefunktion Lambda_cl ist aber nicht Lambda_cos. Aus ihr folgt noch
kein Nullwert der gesamten effektiven Vakuumdichte einschließlich Fluktuationen.

## 4. Kontrollen gegen eine scheinbare Frame-Kompensation

Die [native Quellenprüfung](OP5_Native_Pair_Potential_Audit.md) verfolgt die
existierenden Wirkungen, r27/r28, r31 und r67. Sie bestätigt: Flussfraktionen,
Kanalgleichgewichte und Counting-Relationen enthalten noch keine abgeleitete
absolute Energiedichte.

Auch der bilineare Vorzeichenwechsel z->iz ist keine negative statistische
Gewichtung einer Vakuumdeterminante. Bei gleich gewichteten Vergleichsmoden
mit Massenquadraten q und -q gilt vielmehr

\[
e^{-s q}+e^{s q}=2\cosh(s q),
\]

also keine Kompensation; für q>0 kommt beim negativen Massenquadrat zusätzlich
die IR-Instabilität des flachen Vergleichsoperators hinzu. Unitär äquivalente
hermitesche Operatoren haben gleiche, nicht entgegengesetzte Wärmespuren.
Entgegengesetzte Determinantengewichte brauchen begründeten Feldinhalt und ein Maß;
sie folgen nicht aus einem Frame-Etikett.

Die schon vorhandene zusätzliche skalare/fermionische Paarung bleibt eine
bedingte Möglichkeit für selektive Vakuumkompensation. Ihre nativen Partner
und der Schutz der notwendigen Relationen sind weiterhin nicht abgeleitet.
Ein neutraler Paarzustand darf nicht mit dieser zusätzlichen Feldtheorie
gleichgesetzt werden.

## 5. Rechenprovenienz und Review

Neue Skalar-/Gravitationsrechnung:
[Skript](OP5_Relational_Pair_Gravity_Check.py),
[Vertrag](OP5_Relational_Pair_Gravity_Check.contract.json),
[Ergebnis](op5-relational-pair-run-2026-10-26/result.json),
[Manifest](op5-relational-pair-run-2026-10-26/manifest.json).

Exakte symbolische Prüfungen: gemeinsame Shift-/Austauschsymmetrie,
Paargradient und Hessian, Mittelpunkt-Nullmode, relative kanonische Masse,
Potentialhöhenfreiheit, Gegenkontrolle am instabilen Ursprung, gleiche
Wärmegewichte und Referenzsubtraktion. Neun konstante Hintergrundfälle mit
45 Dezimalstellen, Toleranz 1e-40. Manifeststatus `completed`, Validierung mit
aktueller Projektwurzel bestanden. Keine neue Anpassung an H0 oder beobachtetes
Lambda; alle dimensionalen Modellparameter bleiben Eingaben.

Die getrennte Kanalkontrolle wurde mit SymPy exakt ausgeführt: Generator,
Lösung, Semigruppeneigenschaft, Bereichsgrenze, Ancilla-Unitarität und Partial-
spur, Wiederkehr, ungleiche Raten sowie Hamilton-Offsetfreiheit. Die Rohquelle
wurde mit r27 und r28 abgeglichen. Die Skalarminima, kanonischen Massen und
Einstein-Vakuumfamilien wurden zusätzlich in einer getrennten Ableitung
gegengeprüft. Dabei wurde ausdrücklich festgehalten: Der Mittelpunkt ist ein
flacher Modulus, kein eindeutiger Attraktor; die relative positive Masse ist
nur eine lokale Baumebenenkontrolle. Separate Subagentenableitungen und
Koordinatorprüfung sind kein externer Peer Review der physikalischen Theorie.
Die abschließende mathematische Textprüfung betraf nur diese neue Notiz;
zwei Sprachkorrekturen, keine mathematischen Tokenänderungen und keine
ungeklärten lokalen Notationsfehler. Ein TeX-Build ist für die separate
Markdown-Notiz nicht vorgesehen.

## 6. Checkpoint und Fortsetzung

| Route | Ertrag | Offene Fortsetzung |
| --- | --- | --- |
| Symmetrische Mischung | Exakter neutraler Attraktor auf dem realen Disk; endlicher unitärer Mischaufbau möglich. | Native Rate, Zeitmaß, Gegenzustandspräparation und gesamte Energiebilanz bestimmen. |
| Relationales Paarpotential | Expliziter stabiler relativer Abstand als positiver Vergleichsfall. | Potentialform und kinetische Normierung aus nativen Variablen ableiten, statt die gewünschte Relation einzubauen. |
| Gravitative Zuordnung | Identische neutrale Konfiguration bei verschiedenen Lambda-Werten; interne Neutralität reicht nicht aus. | Gemeinsame metrikabhängige effektive Wirkung, Maß und eine eigenständig begründete Vakuum-/Matching-Bedingung auswerten. |
| Native Kompensation | Keine Aufhebung allein aus dem Frame-Vorzeichen. Vorhandene echte Zusatzfeldkompensation bleibt bedingt. | Reduzierten nativen Fluktuationsoperator samt Constraints/Ghosts und Wärmekoeffizienten bestimmen; Schutz/Stabilität der Kompensation zeigen. |

Der konstruktive Versuch ist bis zu diesem nachprüfbaren Punkt ausgeführt.
OP5 und die physikalische Lambda-Erklärung bleiben offen. Die nächste
entscheidende Pflicht ist jetzt genauer lokalisiert: das konstante Volumen-
glied der vollständigen nativen effektiven Wirkung. Eine weitere Suche nach
einem „noch neutraleren“ Bezugspunkt würde diese Pflicht nicht ersetzen.
