# QAM – Buchführungsprüfung für Forschungstexte

## Frame-Schnittstellensprache und Physikmapping

**Umgesetzt am 7.11.2026:** Das Zusatzpaket [`qam-physics.sty`](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/tex/qam-physics.sty) bietet deklarierte Physikprofile und gruppenlokale Standardkontexte. `\qamprofile` ordnet Frame, Sprachrolle, Status und Interpretation zu; innerhalb von `qamcontext` schreibt `\qamformula` eine gewöhnliche TeX-Formel mit dieser Zuordnung. Die linken Rollen entfallen im passenden Profil. `\qamphys` zeigt sie bei Wiederverwendung in einem anderen oder keinem Kontext automatisch, `\qamphys*` immer. Verschachtelte Kontexte stellen den äußeren Standard wieder her.

Der `.qam`-Export hält Frame, Sprachprofil, Formelpayload und Herkunft ausdrücklich fest. `\qamphysconvert` verlangt eine deklarierte Map und einen expliziten Zielausdruck; es überträgt keine ART- oder QM-Physik stillschweigend. Quellen-/Zielprofil, Status und Eingabeherkunft bleiben verknüpft. Die Erweiterung prüft diese Zuordnung, nicht die physikalische Wahrheit der Formel oder eine allgemeine Tensoralgebra. Sie ergänzt die bestehenden Buchführungswerkzeuge, ohne deren Lean-Theoreme zu ändern. [ART-/QM-Beispiel](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/physics.tex) · [Befehle und Prüfgrenzen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/README.md).

**Autorpräzisierung vom 6.11.2026:** QAM ist als Schnittstellensprache für Frames zu lesen. Ein ausdrücklich zugeordnetes Physikmapping legt fest, welche gewöhnlichen physikalischen Objekte und Gleichungen in einem Frame gemeint sind. Die ART ist beispielsweise ein solches Mapping im dafür deklarierten Frame; QAM muss die ART nicht neu herleiten und setzt ihre Gültigkeit nicht für jeden anderen Frame voraus.

Die zweiseitige Darstellung trennt links Frame-/Ausleserollen und rechts die gewöhnlichen Struktur-/Tensorrollen. Beim Wechsel zu einem anderen Frame wird eine eigene, deklarierte Schnittstelle verwendet. Sie muss weder automatisch invertierbar sein noch die Physikinterpretation des ersten Frames unverändert fortsetzen. Die Gleichungen werden innerhalb des jeweiligen Mappings mit ihrem bisherigen mathematischen beziehungsweise physikalischen Status verwendet.

Der [quellenbasierte Schnittstellenentwurf](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/qam_frame_physics_interface_design_2026_11_06.md) entwickelt dies am ART-Beispiel; sein Nachtrag vom 7.11. beschreibt die erste Umsetzung. Die anschließend beschriebenen TeX-/Lean-Buchführungsprüfungen sind eine vorhandene Werkzeugschicht, nicht die gesamte mögliche Semantik der QAM-Sprache. Sie führen keine allgemeine physikalische Berechnung der ART oder QM aus.

**Standardkontext als Kurzschreibweise (Autorwunsch 6.11., Paketumsetzung 7.11.):** Wird für einen Abschnitt ein eindeutiger Frame samt Physikprofil deklariert, dürfen dessen linke QAM-Rollen im Druck entfallen. Im ART-Standardkontext steht dann unmittelbar die gewöhnliche Einstein-Gleichung; beim Expandieren werden die linken Rollen wieder ergänzt. Abweichende Frames und Übergänge bleiben ausdrücklich markiert. Exporte müssen den Kontext erhalten oder ausschreiben. Das ist eine Notationsvereinbarung, keine neue physikalische Annahme. Die Umsetzung arbeitet mit registrierten gewöhnlichen TeX-Formelpayloads, nicht mit einem allgemeinen Physikparser.

**Rindler-Fallstudie (7.11.2026):** Die QAM-Übersetzung von Dorau–Much trennt den Wechsel zur beschleunigten Uhr von der Einschränkung des Zustands auf die zugängliche Keilalgebra. Der anschließende Horizont-Skalierungsgrenzfall liefert das Profil für kohärente Skalarfeldanregungen. Dort gilt $S_H=2\pi J_B$ für den gewichteten Boost-Fluss; eine affine Skalierung der Horizontkoordinate ändert bei mittransformierten Daten beide Werte nicht. Die zusätzliche Flächenregel $\delta A=4S_H$ in Planck-Einheiten verbindet zwei Auslesungen desselben Beobachters. Sie bleibt eine Annahme; die semiklassische Einstein-Gleichung gilt in der lokalen Näherung, mit freiem $\Lambda$. Rindler wird keinem QSC-Frame M/T/P gleichgesetzt. [Fallstudie und Wertvergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/qam_dorau_much_rindler_2026_11_07.md).

**Rindler case study (7 November 2026):** The QAM translation of Dorau–Much separates the accelerated clock from restriction of the state to the accessible wedge algebra. A further horizon scaling limit supplies the profile for coherent scalar excitations. Here $S_H=2\pi J_B$ for the weighted boost flux; affine rescaling with the data transformed accordingly preserves both values. The additional area law $\delta A=4S_H$ in Planck units links two readouts for the same observer. It is an assumption; the semiclassical Einstein equation holds in the local approximation, with $\Lambda$ free. No identification with QSC frames M/T/P is made.

**Lorentz-Boost und Gram-Auslesung (7.11.2026).** Zwei Felder mit $\mathbf E=2e_x$ und $\mathbf B=\pm e_y$ haben dasselbe normierte Gram-Register $\operatorname{diag}(4,1)/5$. Beim Boost mit $v=1/4$ entlang $z$ ergeben sich daraus $\operatorname{diag}(49,4)/53$ und $\operatorname{diag}(9,4)/13$. Der Boost ist auf dem reduzierten Register allein deshalb mehrdeutig. Mit Orientierung und Skala kann QAM auf dem Rang-zwei-Chart den Weg „Feld rekonstruieren, boosten, neu auslesen“ deklarieren. Die Orientierung unterscheidet die Eingaben. Die Skala wird zur Rekonstruktion des vollständigen Feldes benötigt und kürzt sich im normierten Ergebnis heraus. [QAM-Rechenbeispiel](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/gram-boost.tex).

**Lorentz boost and Gram readout (7 November 2026).** The fields $\mathbf E=2e_x$, $\mathbf B=\pm e_y$ share the normalized Gram register $\operatorname{diag}(4,1)/5$. At $v=1/4$ along $z$ their registers become $\operatorname{diag}(49,4)/53$ and $\operatorname{diag}(9,4)/13$. The reduced register alone cannot determine its boosted value. Orientation and scale permit reconstruction, boosting and re-encoding on the rank-two chart. Orientation distinguishes the inputs. Scale recovers the full field and cancels from the normalized output.

**Quelle–Rückweg und C5 (7.11.2026).** Der OP1–OP5-Satz vergleicht eine feste Invariante am symmetrisierten Rückweg. Das Mittel $m=(f+b)/2$ kann die Richtung einzelner Rückwegwerte verdecken. Der Zusatz $d=(f-b)/2$ erlaubt die Rekonstruktion beider Werte als $m\pm d$. Historisch zeigt C5 dieselbe Art von Informationsverlust. Bei der Schwelle $1/256$ sehen die exakte Null und $(3/4)^{20}$ gleich aus. Selbst die nächste Anzeige hängt im Kontraktionsmodell davon ab, wo der Wert innerhalb seines aktuellen Schwellenbereichs liegt. [Erkundung und Geltungsgrenzen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/qam_quelle_rueckweg_auslesung_2026_11_07.md).

**Source–return and C5 (7 November 2026).** The OP1–OP5 theorem compares a fixed invariant at the symmetrized return. The mean $m=(f+b)/2$ can hide which value belongs to which direction. Retaining $d=(f-b)/2$ recovers both values as $m\pm d$. The historical C5 detector likewise gives the same reading for exact zero and $(3/4)^{20}$ at threshold $1/256$. Even the next reading in the contraction model depends on where the value lies within its current threshold range.

**Nachtrag zur Route.** Die Erhaltungsannahmen legen die gerichteten Auslesungen nicht fest. In einem linearen Vergleichsmodell addiert der Hintransport eine verborgene Koordinate und der inverse Transport zieht sie ab. Die Invariante bleibt erhalten, während sich der Zusatz im Mittel aufhebt. Bei einer injektiven Invariante stimmen dagegen beide gerichteten Werte überein. Die konkrete QSC-Route braucht zur Entscheidung auswertbare Transporte und Auslesungen.

**Route follow-up.** The conservation assumptions leave the directed readouts undetermined. In a linear comparison model the forward transport adds a hidden coordinate and its inverse subtracts it. The invariant survives while the addition cancels in the mean. An injective invariant instead forces the two directed values to agree. Deciding the QSC route requires evaluable transports and readouts.

**r27-Richtungen und Kompensatormessung (7.11.2026).** Bei $\alpha=\pi/6$ haben die reinen Bloch-Eingaben $(0,\pm1)$ dasselbe Portmittel $1/2$, aber vertauschte gerichtete Portwerte $(2\pm\sqrt3)/4$. Das volle Richtungsmittel ist bei diesem Winkel invertierbar. Der Informationsverlust betrifft die Portreduktion. Für die Eingabe $(1,0)$ löscht die nichtselektive Messung dagegen den Richtungsunterschied und senkt die Bloch-Länge von $1$ auf $1/2$. [Rechenwege und Geltungsbereich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/qam_r27_richtungsreadout_2026_11_07.md).

**r27 directions and compensator measurement (7 November 2026).** At $\alpha=\pi/6$, the pure Bloch inputs $(0,\pm1)$ have the same mean port probability $1/2$ and swapped directed values $(2\pm\sqrt3)/4$. The full directional mean is invertible at this angle. Port reduction loses the distinction. For input $(1,0)$, nonselective measurement instead erases the directional difference and reduces the Bloch length from $1$ to $1/2$.

**Rekonstruktion in r27.** Zwei getrennte Portwahrscheinlichkeiten bei entgegengesetzter Rotation bestimmen den normierten Bloch-Zustand, sofern $\cos 2\alpha$ und $\sin 2\alpha$ beide von null verschieden sind. Auf der vollen normierten Scheibe sind die affinen Invarianten einer nichttrivialen Rotation konstant. Die erhaltene Bloch-Länge ist nicht affin.

**Reconstruction in r27.** Two separate port probabilities for opposite rotations determine the normalized Bloch state when both $\cos 2\alpha$ and $\sin 2\alpha$ are nonzero. On the full normalized disk every affine invariant of a nontrivial rotation is constant. The preserved Bloch length is nonaffine.

**Quadratisches r27-Register.** Für den Bloch-Vektor $v$ macht das Register $Q(v)=vv^{\mathsf T}$ seine quadrierte Länge als lineare Spur auslesbar. Die Spur bleibt unter beiden Rotationsrichtungen und ihrer Mittelung im quadratischen Register erhalten. Quadriert man erst das Bloch-Mittel $m$, fehlt dagegen $|d|^2$ mit der halben Richtungsdifferenz $d$. Die Kompensatormessung entfernt zusätzlich das Quadrat der quer zur Messachse liegenden Komponente.

**Quadratic r27 register.** The trace of $Q(v)=vv^{\mathsf T}$ reads out the squared Bloch length linearly. Both rotations and averaging in the quadratic register preserve it. Squaring the Bloch mean $m$ instead loses $|d|^2$, where $d$ is half the directional difference. Compensator measurement removes the squared component perpendicular to its axis.

**Messzugang zum quadratischen Register.** Aus getrennten Portreihen mit $q_\pm=2p_\pm-1$ folgt $|v|^2=(q_++q_-)^2/(4\cos^2 2\alpha)+(q_+-q_-)^2/(4\sin^2 2\alpha)$, wenn beide Nenner von null verschieden sind. Bei $\alpha=\pi/8$ vereinfacht sich dies zu $q_+^2+q_-^2$. Produkte unabhängiger Portausgänge auf gleich präparierten Kopien liefern die Quadrate im Erwartungswert.

**Measurement access to the quadratic register.** Separate port series with $q_\pm=2p_\pm-1$ give $|v|^2=(q_++q_-)^2/(4\cos^2 2\alpha)+(q_+-q_-)^2/(4\sin^2 2\alpha)$ when both denominators are nonzero. At $\alpha=\pi/8$ this becomes $q_+^2+q_-^2$. Products of independent port outcomes on identically prepared copies yield the squares in expectation.

**Zweikopien-Auslesung in r27.** Auf zwei gleich präparierten unabhängigen Kopien misst die Observable $H=\sigma_x\otimes\sigma_x+\sigma_z\otimes\sigma_z$ die quadrierte Bloch-Länge als Erwartungswert. Gemeinsame Rotation erhält $H$. Die Kompensatormessung auf beiden Kopien entfernt den $z$-Term. Beim Mittel beider Rotationsrichtungen muss die Richtung pro Kopienpaar gemeinsam gewählt werden.

**Two-copy readout in r27.** On independent identically prepared copies, $H=\sigma_x\otimes\sigma_x+\sigma_z\otimes\sigma_z$ has expectation equal to the squared Bloch length. Common rotation preserves $H$. Compensator measurement on both copies removes its $z$ term. Averaging the two rotations uses a shared direction within each pair.

Das [QAM-Beispiel mit zwei Kopien](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/r27-two-copy.tex) deklariert beide Rotationsprotokolle im selben Profil. Für die Kompensator-Eingabe bei $\alpha=\pi/6$ haben beide dieselbe Ein-Kopien-Auslesung. Die Zweikopien-Observable liefert bei gemeinsamer Richtungswahl $1$, bei unabhängiger Wahl $1/4$. Die Messung auf beiden gemeinsam rotierten Kopien liefert ebenfalls $1/4$.

The [two-copy QAM example](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/r27-two-copy.tex) declares both protocols within one profile. For the compensator input at $\alpha=\pi/6$, their single-copy marginals coincide. The two-copy observable gives $1$ for a shared direction and $1/4$ for independent directions. Measuring both copies in the shared protocol also gives $1/4$.

**Teilweise gekoppelte r27-Richtungen.** Bei gleichverteilten Einzelrichtungen und Paarkorrelation $k$ liefert die Zweikopien-Observable $(\cos^2 2\alpha+k\sin^2 2\alpha)|v|^2$. Nach der Kompensatormessung ist der Wert $\cos^2(2\alpha)x^2+k\sin^2(2\alpha)z^2$. Das zeigt, wann die Messung den Unterschied zwischen Richtungsprotokollen sichtbar lässt.

**Partially coupled r27 directions.** With fair individual directions and pair correlation $k$, the two-copy observable gives $(\cos^2 2\alpha+k\sin^2 2\alpha)|v|^2$. After compensator measurement it gives $\cos^2(2\alpha)x^2+k\sin^2(2\alpha)z^2$. This identifies when the measurement preserves the distinction between direction protocols.

**Unbekannte r27-Präparation.** Hinter dem Kompensator bestimmen die beiden Portausgänge bei fester Messachse die Größen $x$ und $kz^2$, sofern die entsprechenden Winkelfaktoren von null verschieden sind. Ein zweiter Durchlauf mit gemeinsamer Vorrotation $U_{\pi/4}$ liefert die vertauschten Komponenten und trennt die Kopplung $k$ vom Eingangszustand. Der vollständig gemischte Eingang bleibt unempfindlich gegenüber $k$.

**Unknown r27 preparation.** For a fixed measurement axis, the compensator port pair determines $x$ and $kz^2$ when the corresponding angle factors are nonzero. A second run with common pre-rotation $U_{\pi/4}$ exchanges the components and separates coupling $k$ from preparation. The maximally mixed input remains insensitive to $k$.

**Grenze der skalaren Zweikopien-Auslesung.** Bei $\alpha=\pi/6$ liefern die Präparationen $(1/2,0)$ mit $k=1$ und $(0,\sqrt3/2)$ mit $k=1/9$ nach der Kompensatormessung dieselbe Korrelationskurve für alle gemeinsamen Vorrotationen. Ein Einzelportmittel trennt sie bereits ohne Vorrotation.

**Limit of the scalar two-copy readout.** At $\alpha=\pi/6$, preparations $(1/2,0)$ with $k=1$ and $(0,\sqrt3/2)$ with $k=1/9$ give the same correlation curve after compensator measurement for every common pre-rotation. A single-port mean distinguishes them without pre-rotation.

Das Zweikopien-Beispiel exportiert nun auch beide Auslesewege. Die skalare Korrelationskurve hat eine exakte Kollision. Einzelportmittel und Kovarianzen aus zwei Messanordnungen liefern dagegen $x,z,k$ auf dem angegebenen Bereich. Die zweite Anordnung verwendet dieselbe Präparation und Kopplung sowie eine bekannte Vorrotation.

The two-copy example now exports both readout paths. The scalar correlation curve has an exact collision. Single-port means and covariances from two settings recover $x,z,k$ on the stated domain. The second setting uses the same preparation and coupling with a known pre-rotation.

**Rekonstruktion und Modellabgleich in r27.** Zwei Portmittel und eine nach der größeren Eingangskomponente ausgewählte Kovarianz bestimmen $x,z,k$ für einen nichtverschwindenden Eingang. Die zweite Kovarianz erlaubt den Abgleich $x^2C=z^2C'$ für die Annahme einer gemeinsamen Kopplung in beiden Reihen. Das Zweikopien-Beispiel exportiert die Rekonstruktion und diesen Abgleich getrennt. Bei festen Mittelwerten und $C$ liefert die adaptive Rechnung $k=1/2$, während ein geänderter vierter Wert den gemeinsamen Modellabgleich verletzt.

**Reconstruction and model consistency in r27.** Two port means and one covariance chosen using the larger input component recover $x,z,k$ for a nonzero input. The other covariance permits the check $x^2C=z^2C'$ for a common coupling across the two settings.

**r27 und native Klassen.** Die Felder $(2e_x,e_y)$ und $(4e_x,2e_y)$ haben dasselbe normierte Gram-Register, aber $|s|=3$ bzw. $12$. Die Lorentz-/Dualitätstransporte erhalten $|s|$ und können die beiden Felder daher nicht verbinden. Eine aktive Dualitätsvierteldrehung kann dagegen das Vorzeichen von reellem $s$ umkehren. Der native OP1–OP5-Vergleich benötigt zusätzlich die Zulassung der Felder und den Nachweis, welche Größen seine Klassenerzeuger erhalten.

**r27 and native classes.** The fields $(2e_x,e_y)$ and $(4e_x,2e_y)$ share the normalized Gram register but have $|s|=3$ and $12$. Lorentz and duality transports preserve $|s|$, so they cannot connect the pair. An active duality quarter-turn can reverse the sign of real $s$. The native OP1–OP5 comparison additionally requires admission of the fields and proof of what its class-generating maps preserve.

**HC-Port und native Zulassung.** Die konkrete HC-Auswahl verändert beim Skalenpaar $|s|$ von $3,12$ auf $5/2,10$. Ob dieser Schritt zur nativen Klasse gehört, verlangt einen eigenen Zulassungsnachweis. Beide Portvektoren erhalten gemeinsam die Information für $s$. Ihre Normen allein können den gemischten Term $(E+B)\cdot(E-B)$ verdecken.

**HC port and native admissibility.** For the scaled field pair, the explicit HC selection changes $|s|$ from $3,12$ to $5/2,10$. Native admission of this step requires a separate argument. The two port vectors together retain the data for $s$. Their norms alone can hide the cross term $(E+B)\cdot(E-B)$.

**Lokaler HC-Rückweg.** Aus den beiden Portvektoren $A=E+B$, $D=E-B$ gewinnt man das volle Feld als $((A+D)/2,(A-D)/2)$ zurück. Für $s$ genügen die drei Normquadrate $|A|^2,|D|^2,|A+D|^2$. Die dritte Auslesung liefert per Polarisation den gemischten Term. Die lineare Auslesung von $s$ aus diesen drei Werten erhält die Invariante auch beim Mittel zweier gewöhnlicher Lorentz-Richtungen.

**Local HC return.** The two port vectors $A=E+B$, $D=E-B$ recover the field as $((A+D)/2,(A-D)/2)$. For $s$, the three squared norms $|A|^2,|D|^2,|A+D|^2$ suffice. The third recovers the cross term by polarization. The linear readout of $s$ from these values also preserves the invariant when averaging two ordinary Lorentz directions.

**Dualität im HC-Rückweg.** Die beiden Dualitätsrichtungen $\alpha=\pm\pi/4$ schicken $s=3$ auf $\pm3i$. Das komplexe Mittel ergibt null, obwohl beide Zweige nichtnullartig bleiben. Im vor der Mittelung gebildeten zweiten Moment von $(\operatorname{Re}s,\operatorname{Im}s)$ bleibt die Spur $|s|^2=9$. Sie ist für gewöhnliche Lorentztransporte und aktive Dualitätsrotationen eine lineare Auslesung dieses Registers.

**Duality in the HC return.** The two duality directions $\alpha=\pm\pi/4$ send $s=3$ to $\pm3i$. The complex mean vanishes while both branches remain non-null. Taking the second moment of $(\operatorname{Re}s,\operatorname{Im}s)$ before averaging preserves its trace $|s|^2=9$. This is a linear readout on the second-moment register for ordinary Lorentz transports and active duality rotations.

**Nullprüfung im gewichteten Rückweg.** Das zweite Moment $M_2=\sum_jp_j|s_j|^2$ verschwindet bei nichtnegativen Gewichten genau dann, wenn alle Zweige mit positivem Gewicht $s_j=0$ haben. Eine Schwelle $M_2\le\varepsilon^2$ liefert nur $|s_j|\le\varepsilon/\sqrt{p_j}$. Die zusätzliche Feldskala $n_j=|E_j|^2+|B_j|^2$ trennt ein nichtverschwindendes nullartiges Feld vom Nullfeld.

**Zero check for weighted returns.** With nonnegative weights, $M_2=\sum_jp_j|s_j|^2$ vanishes exactly when every positive-weight branch has $s_j=0$. A threshold $M_2\le\varepsilon^2$ only bounds $|s_j|\le\varepsilon/\sqrt{p_j}$. Field scale $n_j=|E_j|^2+|B_j|^2$ distinguishes a nonzero null field from the zero field.

Das [HC-QAM-Beispiel](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/hc-return.tex) exportiert Mittelwert, Zweig-Nulltest, Schwellenabschätzung und Feldskala getrennt. Im Dualitätspaar ist das komplexe Mittel null und das zweite Moment $9$. Ein positives Skalenmittel bei verschwindendem zweiten Moment belegt mindestens einen nichtverschwindenden nullartigen Zweig.

The [HC QAM example](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/hc-return.tex) exports the mean, branch zero check, threshold bound, and field scale separately. For the duality pair, the complex mean vanishes and the second moment is $9$. A positive mean scale with zero second moment certifies at least one nonzero null branch.

**Nullprüfung der HC-Einzelports.** Bei der konkreten Feldinvolution $J_Bw=i\bar w$ sind die Portinvarianten $i|E+B|^2/2$ und $-i|E-B|^2/2$. Ihr gleichgewichtetes zweites Moment ist für jedes nichtverschwindende Eingangsfeld mindestens $n^2/4$ mit $n=|E|^2+|B|^2$. Das komplexe Mittel kann bei orthogonalen Feldern null sein.

**HC single-port zero check.** For the field involution $J_Bw=i\bar w$, the port invariants are $i|E+B|^2/2$ and $-i|E-B|^2/2$. Their equally weighted second moment is at least $n^2/4$ for every nonzero input field, with $n=|E|^2+|B|^2$. The complex mean can vanish for orthogonal fields.

**Nullartigkeit des HC-Eingangs.** Die beiden Portnormen fixieren den Imaginärteil von $s$ und lassen für den Realteil das ganze Intervall $[-\sqrt{N_+N_-},\sqrt{N_+N_-}]$ zu. Bei gleichen positiven Portnormen entscheidet die kohärente Zusatznorm $N_E$ über Nullartigkeit. Es gilt $s=0$ genau bei $N_E=2N_+$. Das HC-Beispiel exportiert diesen Eingangstest getrennt vom Nulltest der projizierten Zweige und enthält die zwei Tripel $(5,5,16)$ und $(5,5,10)$ mit verschiedenen Eingangsinvarianten.

**Nullity of the HC input.** The port norms fix the imaginary part of $s$ and leave the entire interval $[-\sqrt{N_+N_-},\sqrt{N_+N_-}]$ for its real part. For equal positive port norms, the coherent additional norm $N_E$ decides nullity. Then $s=0$ exactly when $N_E=2N_+$.

**HC-Nulltest bei Messintervallen.** Ein nichtverschwindendes nullartiges Eingangsfeld ist mit drei reinen Intervallangaben genau dann vereinbar, wenn $I_+\cap I_-\cap(I_E/2)$ einen positiven Wert enthält. Mit Fehlerschranken $0{,}1$ schließt das Tripel $(5,5,16)$ Nullartigkeit aus. Beim Tripel $(5,5,10)$ ist sie vereinbar und es gilt die scharfe Schranke $|s|\le0{,}15$.

**HC nullity with measurement intervals.** A nonzero null input is compatible with three interval bounds exactly when $I_+\cap I_-\cap(I_E/2)$ contains a positive value. With error bounds of $0.1$, the triple $(5,5,16)$ excludes nullity. For $(5,5,10)$ nullity is compatible and the sharp bound is $|s|\le0.15$.

Das HC-Beispiel exportiert die Intervallvereinbarkeit und die scharfe Betragsschranke als getrennte Aussagen. Die vierte Norm erlaubt zusätzlich, den gemeinsamen Offset zu bestimmen und bei separat begrenzten Restfehlern eine Schranke für den Fehler in $gs$ anzugeben.

The HC example exports interval compatibility and the sharp modulus bound as separate statements. The fourth norm also determines the shared offset in the exact calibration model and bounds the error in $gs$ when the residual errors are bounded separately.

**Gemeinsame Kalibrierung im HC-Nulltest.** Für gemessene Normquadrate $\widehat N=gN+b(1,1,1)$ gilt $\widehat s=gs-b/2$. Ein gemeinsamer positiver Verstärkungsfaktor erhält Nullartigkeit. Ein gemeinsamer Offset verschiebt den Realteil. Beim Messwert $(5,5,10)$ liefert ein auf $0{,}1$ beschränkter gemeinsamer Offset bei $g=1$ die scharfe Schranke $|s|\le0{,}05$.

**Shared calibration in the HC zero check.** For measured squared norms $\widehat N=gN+b(1,1,1)$, the readout is $\widehat s=gs-b/2$. A shared positive gain preserves nullity. A shared offset shifts the real part. For $(5,5,10)$ and $g=1$, a shared offset bounded by $0.1$ gives the sharp bound $|s|\le0.05$.

**Offsetfreie HC-Auslesung.** Die vierte Norm $N_B=|A-D|^2$ erlaubt die Differenzauslesung $(N_E-N_B)/4+i(N_+-N_-)/2$. Ein gemeinsamer additiver Offset fällt heraus. Ein gemeinsamer positiver Gain skaliert den Wert und erhält die Nullentscheidung. Das Parallelogrammgesetz erlaubt zusätzlich die Bestimmung des Offsets.

**Offset-free HC readout.** The fourth norm $N_B=|A-D|^2$ permits the difference readout $(N_E-N_B)/4+i(N_+-N_-)/2$. A shared additive offset cancels. A shared positive gain scales the value and preserves the zero decision. The parallelogram identity also determines the offset.

**Normierte HC-Auslesung bei unbekanntem Gain.** Die Differenz der Summen der vier Normwerte liefert nach Halbierung die skalierte Feldnorm $gn$. Der Quotient mit dem Betrag der Differenzauslesung ergibt $|s|/n$ im selben Beobachterprofil. Bei separat begrenzten Restfehlern erlaubt eine positive Untergrenze für die skalierte Feldnorm eine Schranke für diesen Quotienten.

**Normalized HC readout with unknown gain.** Half the difference between the sums of the four norm values gives the scaled field norm $gn$. Dividing the modulus of the difference readout by it gives $|s|/n$ in the same observer profile. With bounded residual errors, a positive lower bound on the scaled field norm permits a bound on the ratio.

**Beobachterwechsel der normierten HC-Auslesung.** Der Quotient $|s|/n$ ist bei gemeinsamer affiner Kalibrierung bestimmbar, hängt aber vom Beobachter ab. Für $(E,B)=(2e_x,e_y)$ liefern Labor und die Boosts $v=\pm1/4$ die Werte $3/5$, $45/53$ und $5/13$, während $s=3$ bleibt. Die exakte Nullentscheidung ist Lorentz-invariant. Eine positive Schwelle des Quotienten gehört zum jeweiligen Profil.

**Observer change of the normalized HC readout.** The ratio $|s|/n$ is identifiable under shared affine calibration and depends on the observer. For $(E,B)=(2e_x,e_y)$ the laboratory and boosts $v=\pm1/4$ give $3/5$, $45/53$, and $5/13$, with $s=3$ throughout. Exact nullity is Lorentz invariant. A positive threshold on the ratio belongs to its observer profile.

**Referenzbeobachter für die Feldskala.** Über gewöhnliche Lorentz-Beobachter gilt $\inf n=|s|$. Für $s\ne0$ erreicht ein endlicher Boost entlang des Energieflusses einen Beobachter mit $E'\times B'=0$. Für ein nichtverschwindendes nullartiges Feld wird das Infimum erst im Grenzfall erreicht. Im minimierenden nichtnullartigen Profil gilt $|s|/n=1$.

**Reference observer for field scale.** Over ordinary Lorentz observers, $\inf n=|s|$. For $s\ne0$, a finite boost along the energy flux reaches an observer with $E'\times B'=0$. A nonzero null field approaches the infimum only in the limit. In the minimizing non-null profile, $|s|/n=1$.

**Referenzboost aus Normdaten.** Bei $r=|s|/n>0$ ergibt sich der Betrag $v_{\rm ref}/c=\sqrt{(1-r)/(1+r)}$ aus der kalibrierungsfreien Auslesung. Zwei Felder mit gleichen Normdaten können entgegengesetzte Flussrichtungen und damit entgegengesetzte Boostvektoren haben. Eine obere Schranke für $r$ liefert für nichtnullartige Eingänge eine untere Schranke für die Boostgeschwindigkeit.

**Reference boost from norm data.** For $r=|s|/n>0$, the calibration-independent readout gives the speed $v_{\rm ref}/c=\sqrt{(1-r)/(1+r)}$. Equal norm data can hide opposite flux directions and therefore opposite boost vectors. An upper bound on $r$ gives a lower bound on the speed for non-null inputs.

Das HC-Beispiel ergänzt die Normdaten um den gerichteten Fluss $F_g=2g(E\times B)$ in denselben Laborachsen und mit demselben Gain. Dann liefert $F_g/(T+|S_\Delta|)$ den Referenzboost für $s\ne0$. Die Gleichung $|F_g|^2=T^2-|S_\Delta|^2$ erlaubt einen Abgleich der exakten Eingaben.

The HC example adds the directed flux $F_g=2g(E\times B)$ in the same laboratory axes and with the same gain. Then $F_g/(T+|S_\Delta|)$ gives the reference boost for $s\ne0$. The identity $|F_g|^2=T^2-|S_\Delta|^2$ checks consistency of the exact inputs.

Für die Rekonstruktion des Referenzboosts genügt eine **gerichtete Flussachse** mit beliebiger positiver Verstärkung. Die Normen liefern den Geschwindigkeitsbetrag, die Flussauslesung die Richtung. Bei $r=1$ ist der Referenzboost null. Der Abgleich der Flussstärke mit den Normdaten setzt weiterhin eine gemeinsame Kalibrierung voraus.

Reconstructing the reference boost requires only a **signed flux direction** with any positive gain. The norms supply the speed and the flux readout supplies the direction. At $r=1$ the reference boost is zero. Comparing flux magnitude against the norm data still requires matched calibration.

**Flussrichtung aus Boostpaaren.** Aus zwei bekannten entgegengesetzten Boosts entlang $a$ folgt $n(-va)-n(+va)=8\gamma^2v\,a\cdot(E\times B)$. Drei orthonormale Achsen liefern die Richtung bei gemeinsamem positivem Gain. Ein gleicher Offset innerhalb jedes Paars kürzt sich heraus. Die Skalen gehören zu ausdrücklich verbundenen Beobachterprofilen.

**Flux direction from boost pairs.** Two known opposite boosts along $a$ give $n(-va)-n(+va)=8\gamma^2v\,a\cdot(E\times B)$. Three orthonormal axes recover the direction with a shared positive gain. An equal offset within each pair cancels. The scales belong to explicitly linked observer profiles.

**Zwei Boostachsen und Spiegelmehrdeutigkeit.** Selbst bei bekannter Flussstärke lassen zwei feste Boostachsen im Allgemeinen zwei Flussvektoren zu, die an der Ebene der Achsen gespiegelt sind. Bei bekannten Ebenenkomponenten genügt das Vorzeichen einer Differenz entlang der Normalen, um sie zu trennen.

**Two boost axes and reflection ambiguity.** Even with known flux magnitude, two fixed boost axes generally leave two flux vectors related by reflection in their plane. With the planar components known, the sign of a normal-axis difference resolves the ambiguity.

Das HC-Beispiel exportiert die beiden $z$-Boosts in getrennten Beobachterprofilen und die Rückführung ihrer Messberichte für den Vergleich. Für $E=2e_x$, $B=\pm e_y$ erhält es die Differenzen $\pm64/15$. Die Übernahme eines Berichts bewahrt seine Zuordnung zum messenden Beobachter.

The HC example exports the two $z$ boosts in separate observer profiles and transfers their reports for comparison. For $E=2e_x$, $B=\pm e_y$ it gives differences $\pm64/15$. Transferring a report preserves its association with the observer who measured it.

**Kontrolle im Referenzprofil.** Drei unabhängige entgegengesetzte Kontrollboostpaare im erreichten Profil haben genau bei verschwindendem Energiefluss gleiche Feldskalen pro Paar. Dafür genügt gleicher Offset und gleicher positiver Gain innerhalb jedes Paars. Beim Feld $(2e_x,e_y)$ liefert der richtige Referenzboost drei Nulldifferenzen, der Boost mit falschem Vorzeichen dagegen die $z$-Differenz $128/9$ bei Kontrollgeschwindigkeit $1/4$.

**Check in the reference profile.** Three independent opposite probe pairs in the resulting profile give equal scales within every pair exactly when its energy flux vanishes. An equal offset and positive gain within each pair suffice. For $(2e_x,e_y)$ the correct reference boost gives three zero differences. Reversing its sign instead gives a $z$ difference of $128/9$ at probe speed $1/4$.

**Korrekturboost aus Restfluss.** Für $s\ne0$ liefert der Restfluss im erreichten Profil die kleinste Korrekturrapidität $\tfrac12\operatorname{arsinh}(2|\mathbf P'|/|s|)$ zu einem flussfreien Beobachter. Beim bisherigen falschen Boost $-c/2$ ist der Korrekturboost $4c/5$ entlang $+z$. Fehlerschranken für Restfluss und eine positive Untergrenze für $|s|$ begrenzen gemeinsam die nötige Korrektur.

**Corrective boost from residual flux.** For $s\ne0$, the residual flux in the resulting profile gives the minimum corrective rapidity $\tfrac12\operatorname{arsinh}(2|\mathbf P'|/|s|)$ to a flux-free observer. In the example with the wrong boost $-c/2$, the correction is $4c/5$ along $+z$. An upper bound on residual flux and a positive lower bound on $|s|$ jointly bound the correction.

Das HC-Beispiel führt den falschen Laborboost und seine Korrektur als zwei erklärte Profilwechsel. Die Korrektur $4c/5$ gilt relativ zum Zwischenbeobachter. Ihre Zusammensetzung mit $-c/2$ ergibt den Laborboost $+c/2$. Der Export hält die Flussprüfung im erreichten Zielprofil fest.

The HC example declares the wrong laboratory boost and its correction as separate profile changes. The correction $4c/5$ is relative to the intermediate observer. Composing it with $-c/2$ gives laboratory velocity $+c/2$. The export records the flux check in the resulting profile.

**Flussfreiheit und Wahl des Zielbeobachters.** Ein weiterer Boost entlang der gemeinsamen Feldachse eines flussfreien Profils erhält den verschwindenden Energiefluss. Die Feldkontrolle prüft daher eine Eigenschaft des Zielprofils. Die Auswahl des konkreten Beobachters verlangt zusätzlich die deklarierte Boostabbildung oder eine unabhängige Beobachterauslesung.

**Zero flux and choice of target observer.** A further boost along the common field axis of a flux-free profile preserves zero energy flux. The field check therefore tests a property of the target profile. Identifying the specific observer additionally requires the declared boost map or an independent observer readout.

**Uhrvergleich im flussfreien Zielprofil.** Ein weiterer Boost entlang der Feldachse mit Rapidität $\xi$ ergibt relativ zum Labor $\gamma_{\rm Ziel}=\gamma_{\rm ref}\cosh\xi$. Damit identifiziert der skalare Uhrvergleich den minimalen Referenzbeobachter innerhalb der flussfreien Familie. Für die Richtung einer von null verschiedenen Abweichung braucht es ein Vorzeichen. Das HC-Beispiel exportiert die flussfreie Familie, die Auswahl per Uhrvergleich und die beiden gleich schnellen Abweichungen getrennt.

**Clock comparison in the flux-free target profile.** A further boost along the field axis with rapidity $\xi$ gives laboratory factor $\gamma_{\rm Ziel}=\gamma_{\rm ref}\cosh\xi$. This scalar clock comparison identifies the minimum-speed reference observer within the flux-free family. A nonzero deviation requires sign information to determine its direction. The HC example exports the flux-free family, the clock selection, and the two equal-speed deviations separately.

**r27-Faktor und Referenzbeobachter.** Für dasselbe Feldregister mit $r=|s|/n>0$ erfüllt der r27-Faktor $1/r$ die Beziehung $1/r=\cosh(2\eta_{\rm ref})=2\gamma_{\rm ref}^2-1$. Bei $r=1/2$ liefert r27 den Faktor $2$, der minimale Laborboost dagegen $\sqrt{3/2}$. Die Zuordnung betrifft die Parameter desselben Feldregisters. Die Messung in r27 und der Lorentz-Boost haben getrennte Abbildungen.

**r27 factor and reference observer.** For the same field register with $r=|s|/n>0$, the r27 factor satisfies $1/r=\cosh(2\eta_{\rm ref})=2\gamma_{\rm ref}^2-1$. At $r=1/2$, r27 gives $2$ and the minimum laboratory boost gives $\sqrt{3/2}$. This relates parameters of the same register. The r27 measurement and Lorentz boost have separate maps.

**Beobachter bei doppelter Rapidität.** Der kollineare Boost mit doppelter Referenzrapidität erhält die Laborfeldskala und kehrt den gerichteten Energiefluss um. Das flussfreie Profil liegt in der Mitte. Bei dieser definierten Abbildung ist $1/r$ der Lorentzfaktor zwischen Labor und dem Beobachter mit umgekehrtem Fluss.

**Observer at twice the rapidity.** The collinear boost at twice the reference rapidity preserves the laboratory field scale and reverses directed energy flux. The flux-free profile is the midpoint. For this specified map, $1/r$ is the Lorentz factor between the laboratory and the observer with reversed flux.

**Volles Feld bei doppelter Rapidität.** In gemeinsam ausgerichteten Achsen unterscheiden sich die beiden äußeren Feldausgaben durch eine räumliche Halbdrehung um die gemeinsame Feldachse des flussfreien Zwischenprofils. Ihre vier HC-Normen stimmen überein. Der gerichtete Fluss wechselt das Vorzeichen. Die räumliche Drehung und der Beobachterboost werden als getrennte Abbildungen geführt.

**Full field at twice the rapidity.** In aligned axes, the outer field readouts differ by a half-turn around the common field axis of the flux-free intermediate profile. Their four HC norms agree, while the directed flux reverses. The spatial rotation and observer boost are distinct maps.

## Vorhandene Buchführungswerkzeuge

Die vorhandene Werkzeugschicht realisiert typisierte Buchführungsprüfungen für lange Forschungstexte, mit oder ohne Sprachmodelle. Sie hängt **nicht** am Projekt Quantum Sphaera; das Projekt ist nur ihre erste Fallstudie. Ausführlich: Methodenpapier `paper/qam/` (Entwurf, 12 Seiten, nur Zenodo). Diese Werkzeugbeschreibung ersetzt nicht die oben erklärte Frame-Schnittstellenrolle.

## Drei Fehler, drei Regeln

| Fehler | Regel | TeX (`qam.sty`) | Lean (`QAM.Provenance`, `QAM.QamFile`) |
|---|---|---|---|
| **Beförderung**: eine bedingte oder gerechnete Aussage wird als bewiesen behandelt | eine Folgerung hat höchstens den Status ihrer schwächsten Prämisse | Fehler bei `\qamderive`, `\qamconvert` | `no_promotion`, `proved_only_from_proved` |
| **Eingabe als Ergebnis**: ein von Hand eingesetzter Wert wird später als hergeleitet zitiert | jede Aussage trägt die Eingaben mit, auf denen sie beruht; keine geht verloren, keine wird erfunden | Fehler bei `\qamindependent` | `inputs_tracked`, `inputs_sourced`, `independent_iff` |
| **Frame-Vermischung**: Größen verschiedener Frames werden verglichen oder verknüpft | nur innerhalb eines Frames verknüpfen und vergleichen; Frame-Wechsel nur über eine erklärte Abbildung | Fehler bei `\qamderive`, `\qamcompare`, `\qamconvert` | `frames_declared`, `no_maps_same_frame` |

Statusordnung: `open < reading < conditional < computed < proved`. Der Frame `*` ist konventionsfrei (passt zu jedem Frame); `\qamcompose{K}{G}{H}` erklärt die Verkettung zweier Abbildungen. Zusätzlich lehnt das TeX-Paket Schlüssel ab, die vor ihrer Erklärung benutzt oder doppelt erklärt werden (der Text ist append-only).

## Prüfung beim Kompilieren

Das LaTeX-Paket `qam/tex/qam.sty` lässt den TeX-Compiler beim ersten Regelverstoß mit einer Fehlermeldung anhalten (Option `mode=warning` nur Warnungen). Beispiel aus der Fallstudie, die Frame-Verschiebung β aus zwei Literaturwerten:

```latex
\qamframe{M} \qamframe{T} \qammap{G}{M}{T}
\qaminput{gamma}{M}{computed}               % zwei Literaturwerte, eingesetzt
\qamclaim{counting}{M}{proved}              % die Zählformel
\qamderive{beta}{computed}{gamma,counting}  % geht durch
\qamderive{beta2}{proved}{gamma,counting}   % hält an:
% ! Package qam Error: Promotion: `beta2' is declared `proved', but its weakest
% (qam)                premise `gamma' is only `computed'.
\qamindependent{beta}                       % hält an: beta beruht auf gamma
```

`\qamshow{beta}` setzt `[computed | frame M | inputs: gamma]`. Das Methodenpapier benutzt das Paket selbst. Tests (Dokumente, die durchlaufen müssen, und solche, die mit einem bestimmten Fehler anhalten müssen): `sh qam/tex/tests/run_tests.sh`, Workflow `qam-tex.yml`.

## Automatisch erzeugte QAM-Schreibweise

Die Erklärungen enthalten alles, was die QAM-Schreibweise braucht; das Paket setzt sie selbst. Das optionale erste Argument ist das Symbol (`\qaminput[\gamma]{gamma}{M}{computed}` usw.). Dann liefert

- `\qam{gamma}` → `^M γ := R(w_γ), w_γ = ⟨6, γ⟩ [computed]` (Eingabe als Auslese eines Witness),
- `\qam{beta}` → `^M β ⇐ ^M γ, ^M κ, W = {w_γ} [computed]` (Prämissen und Witness-Menge),
- `\qam{betaT}` → `^T β' = ^T_M G ^M β, W = {w_γ} [conditional]` (Frame-Wechsel mit Quelle und Ziel),
- `\qam*{…}` ohne Status, `\qamledger` eine Tabelle aller Aussagen in Erklärungsreihenfolge.

Mit `\usepackage[export]{qam}` wird jede Aussage zusätzlich als Zeile in `\jobname.qam` geschrieben, z. B. `beta := derive(gamma,counting); frame M; status computed; inputs {gamma}`, lesbar für andere Werkzeuge. Weil nichts von Hand getippt wird, kann die Schreibweise nicht von den Erklärungen abweichen.

## Prüfung der exportierten Datei in Lean

`qam/lean/QAM/QamFile.lean` liest eine `.qam`-Datei und prüft jede Zeile gegen den Stand davor; aufgerufen mit `cd qam/lean && lake build && lake exe qamcheck ../examples/example.qam` (eigenständiges Lean-Paket ohne Mathlib, baut in Sekunden). Der Prüfer ist eine Lean-Funktion, und Lean beweist, was sein Erfolg bedeutet: jede hergeleitete Aussage ist neu, hat Prämissen, höchstens deren Status und deren Frame (`derive_sound`, `checked_no_promotion`), ihre Eingaben sind genau die der Prämissen; ein Frame-Wechsel nutzt eine erklärte Abbildung mit passender Quelle (`convert_sound`); Unabhängigkeit und Vergleiche stimmen (`indep_sound`, `compare_sound`). Für den ganzen Stand beweist Lean außerdem: in jedem akzeptierten Stand hat keine Aussage einen höheren Status als irgendetwas, worauf sie – über beliebig viele Schritte – beruht, eine bewiesene Aussage beruht nur auf Bewiesenem, keine Eingabe geht verloren, und eine als unabhängig erklärte Aussage beruht auf nichts mit Eingaben (`checked_no_promotion_record`, `checked_proved_record`, `checked_inputs_record`, `checked_independent_record`). Die Prüfung ist unabhängig vom TeX-Paket: eine von Hand geänderte Datei (Beispiel `bad_inputs.qam`, eine Eingabe gelöscht) wird trotzdem abgelehnt. Nicht verifiziert ist nur das Einlesen der Textzeilen.

## Hash-Kette ab der Ausgangsthese

Ein Papier startet meist mit einer Ausgangsthese; jede weitere Aussage entsteht daraus durch weitere Schritte. `\qamthesis[\tau]{thesis}{M}{conditional}{Wortlaut}` erklärt die These, ihr Wortlaut geht in den Hash ein. Jede Aussage bekommt einen Hash: MD5 von `Art;Name;Frame;Status;Eingaben;Quellen;Wortlaut`, wobei *Quellen* die Hashes ihrer Prämissen sind. Eine hergeleitete Aussage nennt damit genau die Fassungen, aus denen sie stammt. Ändert sich ein Wort der These, ändern sich alle Hashes darunter; was nicht davon abhängt, behält seinen Hash (Beispiel `qam/examples/thesis.tex`: Eingabe und Zählung bleiben gleich, x und z ändern sich).

Geprüft wird unabhängig von TeX zweifach: `qam/tools/qamhash.py verify` rechnet jeden Hash nach, Lean (`qamcheck`) prüft die Verkettung (`link_derive_sound` u. a.). Für eine Veröffentlichung schreibt `qamhash.py manifest` die SHA-256-Summen von Quelle, PDF und `.qam` samt Record-Hash. Gleiche Hashes heißen gleicher Stand, nicht richtiger Inhalt.

## Unabhängige Begutachtung (4. Nov. 2026)

Ein unabhängiger Agent spielte einen Mathematiker mit vier offenen Projekten (Zahlentheorie-Numerik, Kombinatorik mit Computersuche, Differentialgeometrie mit mehreren Konventionen, vorregistrierte Statistik), suchte zuerst selbst nach Werkzeugen und probierte dann das Paket. Urteil: „would try on one project“. Nützlich und anderswo nicht im Dokument selbst vorhanden: Frame-Prüfung und die Verfolgung angepasster gegenüber hergeleiteten Werten; in der Differentialgeometrie fand das Paket genau seinen echten Fehler (−+++ gegen +−−− verglichen). Für die Statistik reicht OSF. Gefundene Fehler (behoben): Leerzeichen in Prämissenlisten, Unterstrich im Namen, doppelt erklärte Abbildung, Umrechnung über unerklärte Abbildung im Warnmodus. Umgesetzt aus seinen Wünschen: eigenständiges Lean-Paket ohne Mathlib, Sätze über den ganzen Stand, konventionsfreier Frame `*`, verkettete Abbildungen (`\qamcompose`). Offen: belegpflichtige Ausgangsaussagen (Literatur, Lean-Name, Zertifikat-Hash, Wert/Skript/Commit im Hash), selbst definierbare Statusordnung, Frames mit mehreren Konventionsachsen.

**Grenze:** Geprüft wird nur, was erklärt ist, und eine Erklärung kann falsch sein. Ob `gamma` wirklich eine Eingabe ist, sagt der Autor, nicht das Paket. Die QAM sichert die Form, nicht den Inhalt.

## Was sonst in Lean bewiesen ist

- `QSFormal.QAM`: acht Objektarten (Zustand, Schicht, Operator, Auslese, Zweig, Schale, Witness, Tensor) sind disjunkt; Hilbert-Verschiebung exakt umkehrbar; zulässige Transportketten erhalten Abschlussklassen und verträgliche Auslesen.
- `QSFormal.Models`: die Axiome haben triviale Modelle – sie legen nicht fest, was zulässig ist.
- `QSFormal.Route`: Pfade über Frames bleiben zulässig; Schleifen ändern die Klasse nicht.
- `QSFormal.Store`, `StoreProgress`: die Speicher-Maschine verlässt nie einen zulässigen Zustand, bleibt nie hängen, weist ungültige Schritte ohne Nebenwirkung ab, protokolliert jeden Schritt und kann keine falsche Aussage zertifizieren.

Alles ohne `sorry`, in CI gebaut (`lean-build.yml`).
