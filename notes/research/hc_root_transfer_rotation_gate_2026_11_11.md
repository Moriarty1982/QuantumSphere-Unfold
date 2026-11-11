# HC-Balance zu positiven Wurzeln: Basisrotation und Zweigauswahl

11. November 2026, Codex. Analytische Erkundung, nicht blind; keine neue
H-/k-Nummer, kein numerischer Fit und keine Änderung historischer Runden.
Fortsetzung auf `codex/hc-native-selection` nach 9c5d574.

## Vorwissen und Ziel

`hc_native_selection_gate_2026_11_11.md` zeigte für die dort explizite
J=diag(1,-1)-Zuordnung die bedingte Schranke K<=5/9. Gesucht wird jetzt
rückwärts, ob eine andere feste Zwei-Moden-Basis diese konkrete
quadratische Auslesung auf der gesamten HC-Balancefamilie repariert.

Geprüft: `analysis/HC_Root_Readout.md`, insbesondere die Abschnitte zu
Metriktransfer, globaler Positivität und eingeschränktem isometrischem
Zweig; `analysis/HC_Root_Phase_Dynamics.md`; die Propositionen
`v480:hc-root-domain` in `hc-dynamics-and-geometry.tex` und
`v480:generation-phase-chambers` in `generation-coupling.tex`.
Schon bekannt: volle Positivität der vorliegenden Dichtematrix-Auslesung
verlangt eta<=1/sqrt(2). Ein eingeschränkter eta=1-Zweig benötigt eine
zusätzliche native Zulässigkeits- und Erhaltungsvorschrift.
QAM-Suche `root-readout`: kein Treffer; keine MMA-Belege verwendet.
Die zurückgestellten Ideen liefern keine bereits konstruierte native
Basisabbildung oder Zweigauswahl; kein neuer Auslöser nachgewiesen.

Einordnung: Algebra-Kern zu Massen-/Koide-Auslesung im Gesamtbild.
Alle folgenden Zustände sind normierte reine Zwei-Moden-Zustände auf
einem ausdrücklich deklarierten positiven komplexen Vergleichsträger.
Die verwendeten Basisachsen sind keine M/T/P-Frames.

## 1. Alle festen Basisrotationen gleichzeitig prüfen

Schreibe x=(X1,X2,X3)/X0 mit |x|=1. Eine nichttriviale selbstadjungierte
Zwei-Moden-Involution lässt sich als J=j·sigma mit |j|=1 schreiben.
HC-Balance bedeutet j·x=0, also einen ganzen Großkreis.

Eine feste unitäre Basisrotation der vorhandenen Auslesung entspricht
einem orthonormalen Achsentripel (a,b,n). Mit denselben zyklischen
Wurzelmatrizen E0,E1,E2 wie im Paper lautet sie

$$
L(x)=X_0\bigl[E_0+\eta(a\cdot x)E_1+\eta(b\cdot x)E_2\bigr],
\qquad K(x)=\tfrac13\bigl[1+\eta^2(1-(n\cdot x)^2)\bigr].
$$

eta>=0 ist ein freier Transferparameter, nicht die Riemannsche Zeta.
Die K-Formel gilt als physikalischer Hauptwurzelquotient nur für L>=0.

Fordert man K=2/3 für JEDES x mit j·x=0, muss (n·x)² auf diesem
Großkreis konstant sein. Die Projektion von n auf seine Ebene erzeugt
aber eine Kosinusfunktion, deren Quadrat nur bei verschwindender
Projektion konstant ist. Also n=±j und eta=1.

Damit durchläuft (a·x,b·x) den gesamten Einheitskreis. Mindestens einer
der drei Wurzelwerte kann dann

$$
\ell_{\min}=\frac{X_0}{\sqrt3}(1-\sqrt2)<0
$$

werden: Wähle die Kreisrichtung entgegen der entsprechenden zyklischen
Ausleseachse. Soll derselbe gesamte Kreis positiv bleiben, ist stattdessen
eta<=1/sqrt(2) nötig, und dann gilt K<=1/2.

**Ergebnis:** Keine feste unitäre Zwei-Moden-Basisrotation innerhalb
dieser Auslesefamilie transportiert ALLE balancierten reinen Zustände
zu positiven Koide-Wurzeln. Eine native Auswahl einer kleineren
Zustandsmenge oder ein anderes Wurzelgesetz bleibt möglich.

## 2. Schon ein antipodales Paar erzwingt eine Zweigentscheidung

Für x und -x hat diese Auslesung denselben isotropen Grundanteil:

$$
L_+=cI_3+D,\quad L_-=cI_3-D,\quad c=X_0/\sqrt3>0,
\quad D=D^*,\quad \operatorname{Tr}D=0.
$$

Das folgende Argument braucht nicht die spezielle E1/E2-Darstellung.
Sind beide L_± positiv, liegen die drei Eigenwerte d_i von D in [-c,c]
und summieren sich zu null. Auf diesem ebenen Würfelschnitt ist die
konvexe Funktion Summe d_i² höchstens 2c²: Die Ecken sind die
Permutationen von (c,0,-c), und dort wird das Maximum erreicht.
Daher

$$
K_\pm=\frac{3c^2+\operatorname{Tr}D^2}{9c^2}\leq\frac59.
$$

Koide würde Tr(D²)=3c² verlangen. Also können die beiden antipodalen
Auslesungen nicht zugleich positiv sein und K=2/3 haben. Die 5/9-Schranke
ist scharf, etwa bei D=diag(c,0,-c). Sie ist eine Positivitätsaussage
für ein Paar um einen isotropen Grundanteil, kein universelles Massen-No-go.

Die orthogonalen Eigenzustände eines nichttrivialen Zwei-Moden-Operators
haben antipodale Bloch-Vektoren. Ein natives T=-iJA mit einem isolierten
Singularpaar kann daher zwar zwei balancierte Auswahlzustände liefern;
dieses Wurzelgesetz kann aber nicht beide als positive Koide-Zweige lesen.
Die Zulassung nur eines Vorzeichenzweigs braucht eine physikalische Regel.
Bei höheren Entartungen gilt der Paarbezug nur auf dem ausgewiesenen
Zwei-Moden-Singularblock, nicht für beliebige Eigenvektorpaare.

## 3. Was eine begrenzte Route noch zulässt

Bei n=±j und eta=1 gibt es weiterhin die schon bekannten drei positiven
Phasenkammern. Ihre jeweiligen Halbbreiten sind pi/12, ihre Mittelpunkte
2pi k/3. Sie bedecken zusammen ein Viertel des vollen Kreises. Das ist
keine Wahrscheinlichkeit ohne ein zusätzliches Maß beziehungsweise
Präparationsgesetz. Die antipodale Verschiebung um pi führt keinen
zugelassenen Koide-Punkt in eine dieser Kammern zurück.

Damit wird die fehlende native Angabe konkreter: Eine Kopplung müsste
eine Basis-/Transferabbildung UND eine zulässige Kammer beziehungsweise
einen Vorzeichenzweig unabhängig von den gemessenen Massen auswählen
und dynamisch erhalten. Bereits geprüfte, zusätzlich postulierte
überdämpfte Phasengesetze werden dadurch nicht zu nativer Dynamik.

## 4. Positive Energie ist eine stärkere Regel als positive Masse

Der anschließende Quellenabgleich in den geprüften Kopplungs-, Operator-
und Dynamikabschnitten liefert keine bereits begründete Auswahl des
positiven Spektrums der hier gesuchten neuen Kopplung. Die Möglichkeit
lässt sich aber exakt von der vorhandenen positiven Gram-Auslesung trennen.

Sei A beschränkt selbstadjungiert und AJ=-JA. Für seinen positiven
Spektralprojektor F_+=1_(0,infinity)(A) gilt

$$
JF_+J=F_-,\qquad F_+JF_+=0.
$$

J bildet also den positiven auf den negativen Spektralraum ab. Jeder
normierte Zustand im positiven Spektralraum erfüllt <J>=0, auch eine
Superposition verschiedener positiver Eigenwerte oder ein Wellenpaket
in einem kontinuierlichen positiven Spektrum. Es sind dafür keine
normalisierbaren Eigenvektoren erforderlich. Die negative Spektralseite
leistet dieselbe Balance. Nullmoden sind von dieser Aussage ausgenommen.

Dies eröffnet eine mathematische Alternative zur zuvor gescheiterten
exakten T-Eigenzustandsauswahl beim Zeta-Multiplikator: Sofern man A durch
das dortige selbstadjungierte T_sigma ersetzt, bildet die Parität J auch
dessen positive und negative Spektralseite ineinander ab. Ein positiver
Spektralraum kann existieren, obwohl es keine L²-Eigenzustände gibt.
Für den nichtnulligen T_sigma existieren beide Seiten: seine Spektral-
symmetrie und Selbstadjungiertheit würden andernfalls T_sigma=0 erzwingen.

Aber F_+ ist eine zusätzliche Zustandsbeschränkung. Sie wird nicht von
Robertson oder dem Vorhandensein der Primzahlreihe vorgeschrieben. Der
Träger im positiven Spektralraum ist außerdem nicht unter J invariant.
Eine native Bedeutung als physikalisch zugelassener Energieraum muss
separat begründet werden. Kontinuierliche Spektralpakete beseitigen
auch nicht automatisch die früheren Impulsdomänenprobleme einer scharfen
Spektralprojektion. Eine solche Auswahl erzeugt noch keine positive
Drei-Generationen-Wurzelauslesung oder deren Phasenkammer.

Für den positiven Massenkandidaten |A|=sqrt(A²) gilt dagegen
[|A|,J]=0. Ebenso kommutiert A² mit J. Seine Positivität wählt keinen
Vorzeichenzweig von A. Im einfachsten Singularblock

$$
J=\operatorname{diag}(1,-1),\quad
A=\begin{pmatrix}0&s\\s&0\end{pmatrix},\quad
|A|=sI_2,\quad s>0,
$$

haben die unbalancierten Zustände (1,0) und (0,1) dieselbe strikt
positive Masse wie die balancierten Zustände. Deshalb ist die schon
vorhandene Gram-/Normpositivität kein Nachweis der benötigten Auswahl.

Ein selbstadjungierter Hamiltonoperator, der mit F_+ kommutiert, würde
den einmal präparierten positiven Spektralraum erhalten. Ob der native
Generator diesen Projektor respektiert und wie der Raum präpariert wird,
ist offen; die formale Mastergleichung garantiert das nicht.

## Grenzen und nächster Schritt

Die Untersuchung variiert nur feste unitäre Zwei-Moden-Basen derselben
quadratischen, im Zustand linear-in-density formulierten Auslesung.
Nichtlineare Normierung, nichtisotrope Grundanteile, andere
Generationenabbildungen und nichtkommutierende Wurzelgesetze sind nicht
ausgeschlossen. Ein passender freier Parameter wäre allein kein Fortschritt.

Nächster Prüfpunkt: Kann der positive Spektralprojektor des arithmetischen
T_sigma mit einem nativ zugelassenen Energieraum und einer erhaltenden
Dynamik identifiziert werden, UND wie würde dieser Raum in eine positive
Wurzelkammer abgebildet? Das ist eine neue offen ausgewiesene Auswahlroute,
keine Wiederherstellung der historischen Zeta-Nullstellenspektralbehauptung.
Keine weiteren Basiswinkel oder Massenfits vor diesem Abgleich.

Validierung: analytische Selbstprüfung der Großkreisbedingung, der
Positivitätsgrenze und des scharfen antipodalen Paararguments. Keine
Simulation, keine QAM-Beweisfreigabe und keine OP-Schließung.
