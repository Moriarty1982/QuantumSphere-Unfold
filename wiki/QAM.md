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

**Abgleich mit r08.** Unter der Zusatzannahme $\gamma_{\rm BI}/\gamma_{\rm string}=n/|s|$ ist der HC-Referenzboost die Halb-Rapidität aus F2. Das Feldmodell erlaubt jedoch jedes Verhältnis $n/|s|\ge1$. Die Zuordnung der beiden realen Beobachter zu M/T und die Auswahl der Zählregel bleiben gesonderte Nachweispflichten.

**Comparison with r08.** Given the additional identification $\gamma_{\rm BI}/\gamma_{\rm string}=n/|s|$, the HC reference boost realizes the half-rapidity in F2. The field model permits every ratio $n/|s|\ge1$. Identifying the two real observers with M/T and selecting the counting rule require separate arguments.

**Getrennter Beobachter- und Sektorschritt.** Der äußere HC-Boost erhält $s$ und kehrt den Fluss um. Die anschließende aktive Dualität wechselt das Vorzeichen von $s$ bei gleicher Feldskala und gleichem Fluss. Gemeinsam liefern die Schritte $(s,n,\mathbf P)\mapsto(-s,n,-\mathbf P)$. Der Lorentzfaktor der Uhren gehört zum Boost. Die M/T-Zuordnung und die Zählregel benötigen einen eigenen Nachweis.

**Separate observer and sector steps.** The outer HC boost preserves $s$ and reverses flux. Subsequent active duality changes the sign of $s$ and preserves scale and flux. Together they give $(s,n,\mathbf P)\mapsto(-s,n,-\mathbf P)$. The clock factor belongs to the boost. M/T identification and the counting rule require separate arguments.

**HC-Involution und zusammengesetzter Übergang.** Für reelles $s\ne0$ gilt $D L_F F=\operatorname{sgn}(s)J_BF$. Zweimalige Anwendung von $D L_F$ liefert $-F$, während $J_B^2F=F$. Die quadratischen Auslesungen verdecken dieses Gesamtvorzeichen. Für nichtreelles $s$ unterscheiden sich bereits die komplexen Auslesungen $-s$ und $-\bar s$.

**HC involution and composed transition.** For real $s\ne0$, $D L_F F=\operatorname{sgn}(s)J_BF$. Applying $D L_F$ twice gives $-F$, whereas $J_B^2F=F$. Quadratic readouts hide the overall sign. For nonreal $s$, the complex readouts $-s$ and $-\bar s$ already differ.

**Gerichteter HC-Rückweg.** Für reelles $s\ne0$ wählt $D^{\operatorname{sgn}(s)}L_F$ auf den beiden Sektoren inverse aktive Vierteldrehungen. Die zusammengesetzte Feldabbildung stimmt dann mit $J_B$ überein. Eine lineare Feldkomponente im Labor unterscheidet diesen geschlossenen Rückweg von der zweimaligen gleichgerichteten Dualität mit Ergebnis $-F$.

**Directed HC return.** For real $s\ne0$, $D^{\operatorname{sgn}(s)}L_F$ chooses inverse active quarter-turns on the two sectors. The composed field map then agrees with $J_B$. A linear laboratory field component distinguishes this closed return from repeating duality in the same direction, which gives $-F$.

**HC-Rückweg für komplexes $s$.** Auf dem nichtnullartigen Feldträger reproduzieren der äußere Beobachterboost und die aktive Dualitätsphase $\zeta(s)=i\bar s/|s|$ die Involution $J_B$. Beim Rückweg wird die Phase komplex konjugiert und der Boost invertiert. Auf reellem $s$ ergibt sich die sektorgebundene Vierteldrehung.

**HC return for complex $s$.** On the non-null field carrier, the outer observer boost followed by active duality with phase $\zeta(s)=i\bar s/|s|$ reproduces $J_B$. On return the phase is conjugated and the boost inverted. For real $s$ this reduces to the sector-dependent quarter-turn.

Das HC-Beispiel rechnet den komplexen Fall $s=3+4i$ mit nichtverschwindendem Fluss durch. Es exportiert den äußeren Boost $-15c/17$ und die aktive Dualitätsphase $(4+3i)/5$ getrennt. Die Feldausgabe ist die HC-Vertauschung, und $s$ wird zu $-3+4i$.

The HC example works through $s=3+4i$ with nonzero flux. It separately exports the outer boost $-15c/17$ and active duality phase $(4+3i)/5$. The field output is the HC exchange, and $s$ becomes $-3+4i$. The inverse boost and conjugate phase recover the laboratory observer and the original field separately.

Der explizite Rückweg im HC-Beispiel verwendet den inversen Boost und die konjugierte Phase. Der Export hält die Rückkehr des Laborbeobachters und der ursprünglichen Feldkomponenten fest.

**Nullartiger Rand der HC-Zerlegung.** Am nichtverschwindenden nullartigen Feld divergiert die äußere Boostrapidität, und die Dualitätsphase kann vom Annäherungsweg abhängen. Das zusammengesetzte Feldbild konvergiert dennoch zu $J_BF$. Am Rand realisiert eine räumliche Halbdrehung um $E+B$ die Feldvertauschung im selben Beobachterprofil.

**Null boundary of the HC decomposition.** At a nonzero null field the outer boost rapidity diverges and the duality phase can depend on the path of approach. The composed field value still tends to $J_BF$. At the boundary a spatial half-turn about $E+B$ realizes the field exchange within the same observer profile.

Das HC-Beispiel exportiert den nullartigen Rand als eigenen Fall im Laborprofil. Es führt die endliche kollineare Boostauslesung, die beiden Grenzphasen und die aktive räumliche Halbdrehung als getrennte Aussagen.

The HC example exports the null boundary as a separate case within the laboratory profile. It records the finite collinear boost readout, the two limiting phases, and the active spatial half-turn separately.

**Räumliche HC-Vertauschung.** Eine gemeinsame räumliche Drehung vertauscht $E,B$ genau dann, wenn ihre Normen gleich sind. Bei $E+B\ne0$ genügt die Halbdrehung um $E+B$. Der Bereich umfasst nullartige Felder und nichtnullartige Felder mit rein imaginärem $s$. Die Normdaten prüfen die Gleichnormbedingung, bestimmen aber die Drehachse im Allgemeinen nicht.

**Spatial HC exchange.** A common spatial rotation exchanges $E,B$ exactly when their norms agree. For $E+B\ne0$, a half-turn around $E+B$ suffices. This includes null fields and non-null fields with purely imaginary $s$. Norm data check equality of magnitudes but generally do not determine the rotation axis.

**HC als aktive Laborabbildung.** Für $s\ne0$ bestimmt der größte Eigenwert von $EE^{\mathsf T}+BB^{\mathsf T}$ eine eindeutige Hauptachse. Die Halbdrehung um diese Achse mit anschließender Dualität $i\bar s/|s|$ liefert $J_B$ im selben Beobachterprofil. Am nichtverschwindenden Nullfeld werden die beiden positiven Eigenwerte gleich. Dort gibt es die direkte Halbdrehung um $E+B$, aber keine über eine volle Umgebung stetig gewählte Dualitätsphase.

**HC as an active laboratory map.** For $s\ne0$, the largest eigenvalue of $EE^{\mathsf T}+BB^{\mathsf T}$ selects a unique principal axis. A half-turn around that axis followed by duality $i\bar s/|s|$ gives $J_B$ within the same observer profile. At a nonzero null field the two positive eigenvalues coincide. A direct half-turn about $E+B$ works there, while no continuous duality phase can be chosen across a full neighborhood.

Das HC-Beispiel vergleicht die aktive Laborabbildung und den äußeren Boost mit Dualität für denselben komplexen Eingang. Beide liefern in ausgerichteten Achsen $B+iE$. Die Lorentzfaktoren relativ zum Labor sind $1$ und $17/8$. Der Export übernimmt die äußere Feldausgabe ausdrücklich als Beobachterbericht.

The HC example compares the active laboratory map and the outer boost with duality for the same complex input. Both give $B+iE$ in aligned axes. Their Lorentz factors relative to the laboratory are $1$ and $17/8$. The export explicitly transfers the outer field output as an observer report.

**Familie von HC-Beobachterübergängen.** Ein zusätzlicher Boost entlang der Feldachse im flussfreien Zwischenprofil fixiert die Zwischenfelder. Die HC-Feldausgabe bleibt gleich, während sich der Lorentzfaktor relativ zum Labor zu $\cosh(2\eta)+\cosh^2\eta(\cosh\xi-1)$ ändert. Der Faktor $n/|s|$ ist innerhalb dieser Boostfamilie der kleinste. Die aktive Laborabbildung ist ein eigener Weg.

**Family of HC observer transitions.** An additional boost along the field axis in the flux-free intermediate profile fixes its fields. The HC field output is unchanged, while the laboratory Lorentz factor becomes $\cosh(2\eta)+\cosh^2\eta(\cosh\xi-1)$. The factor $n/|s|$ is the minimum within this boost family. The active laboratory map is a separate path.

**Auswahl des äußeren HC-Boosts.** In der Familie mit zusätzlichem Feldachsenboost hat die gerichtete Querkomponente des transformierten Zeitbasisvektors den Wert $\cosh\eta\,\sinh\xi$. Ihr Verschwinden wählt den direkten Weg. Ein Uhrvergleich lässt bei größerem Faktor die beiden Vorzeichen von $\xi$ offen, obwohl die Feldausgabe in beiden Fällen gleich ist.

**Selecting the outer HC boost.** In the family with an additional field-axis boost, the signed transverse component of the transformed time basis vector is $\cosh\eta\,\sinh\xi$. Its vanishing selects the direct path. At a larger clock factor the clock comparison leaves both signs of $\xi$ possible, with the same field output.

**Zählfaktor als Verträglichkeitsbedingung.** Für ein festes Feld ist ein Uhrfaktor $G$ in der konstruierten äußeren Boostfamilie genau dann erreichbar, wenn $r\ge1/G$. Der r08-Wert $1{,}8647$ ist daher bei $r=1/2$ nicht erreichbar, bei $r=3/5$ dagegen mit einem zusätzlichen Feldachsenboost. Kollinearität verlangt exakt $r=1/G$.

**Counting factor as a compatibility condition.** For a fixed field, clock factor $G$ is attainable in the constructed outer boost family exactly when $r\ge1/G$. The r08 value $1.8647$ is therefore unattainable at $r=1/2$, but attainable at $r=3/5$ with an additional field-axis boost. Collinearity requires exactly $r=1/G$.

**Trennbereich der r08-Faktoren.** Bei den nominalen Faktoren $1{,}8647$ und $2{,}15$ lässt $0{,}4651\lesssim r<0{,}5363$ innerhalb der erweiterten Boostfamilie nur den größeren Faktor zu. Bei streng kollinearem Übergang sind nur die jeweiligen reziproken Werte zulässig. Das beispielhafte Feldintervall $[0{,}48,0{,}52]$ schließt daher beide direkten Übergänge aus.

**Discrimination range for the r08 factors.** For nominal factors $1.8647$ and $2.15$, the band between their reciprocal thresholds admits only the larger factor in the extended boost family. Strict collinearity instead requires the exact reciprocal of the selected factor. The illustrative field interval $[0.48,0.52]$ therefore excludes both direct transitions.

**Zusätzliche Beobachterauslesung für r08.** Bei festem $r=1/2$ erfordert der nominale Uhrfaktor $G=2{,}15$ in der erweiterten Boostfamilie eine Geschwindigkeitskomponente entlang der Feldachse vom Betrag $3\sqrt{14}\,c/43$. Ein Uhrvergleich allein lässt die beiden Vorzeichen zu. Eine getrennte Bewegungsauslesung kann den berechneten Betrag prüfen.

**Additional observer readout for r08.** At fixed $r=1/2$, the nominal clock factor $G=2.15$ in the extended boost family requires a field-axis velocity component of magnitude $3\sqrt{14}\,c/43$. The clock comparison leaves both signs possible. An independent motion readout can check the computed magnitude.

**Bewegungsschranke für ein Feldintervall.** Bei festem $G=2{,}15$ und $r\in[0{,}48,0{,}52]$ liegt der vorhergesagte Betrag $|v_a|/c$ zwischen ungefähr $0{,}172$ und $0{,}325$. Eine unabhängige Obergrenze von $0{,}17$ würde die Zuordnung in dieser Boostfamilie für das gesamte Intervall ausschließen.

**Motion bound for a field interval.** At fixed $G=2.15$ and $r\in[0.48,0.52]$, the predicted magnitude $|v_a|/c$ lies between approximately $0.172$ and $0.325$. An independent upper bound of $0.17$ would exclude the assignment in this boost family throughout the interval.

**Uhrunsicherheit im Bewegungsabgleich.** Bei unabhängigen Intervallen für $r$ und $G$ wachsen die vorhergesagten Beträge mit beiden Größen auf dem zulässigen Bereich $Gr\ge1$. Für $r\in[0{,}48,0{,}52]$ und $G\in[2{,}14,2{,}16]$ ergibt sich ungefähr $[0{,}159,0{,}331]$ für $|v_a|/c$. Eine Bewegungsobergrenze von $0{,}17$ schließt die Zuordnung dann nicht mehr aus.

**Clock uncertainty in the motion comparison.** For independent intervals for $r$ and $G$, the predicted magnitude increases with both values on $Gr\ge1$. For $r\in[0.48,0.52]$ and $G\in[2.14,2.16]$, $|v_a|/c$ is approximately in $[0.159,0.331]$. An upper motion bound of $0.17$ no longer excludes the assignment.

**Rückrechnung aus Beobachterdaten.** Uhrfaktor $G$ und axiale Geschwindigkeit liefern in der HC-Boostfamilie $h=[G^2(v_a/c)^2+2(G+1)]/(G+1)^2$ und damit $r=h/(2-h)$. Dieser Wert lässt sich gegen die unabhängige Normauslesung prüfen. Bei $G=2{,}15$ und $v_a=0$ ergibt sich $r\approx0{,}4651$. Das HC-Beispiel exportiert die beiden Datenwege und zeigt sowohl Übereinstimmung als auch Widerspruch.

**Inverse observer readout.** In the HC boost family, clock factor $G$ and axial velocity give $h=[G^2(v_a/c)^2+2(G+1)]/(G+1)^2$ and hence $r=h/(2-h)$. This value can be checked against the independent norm readout. At $G=2.15$ and $v_a=0$, it gives $r\approx0.4651$. The HC example exports both data paths and shows both agreement and disagreement.

**Längsbewegung im HC-Abgleich.** In der deklarierten Boostfolge gilt $v_k/c=\sqrt{(1-r)/(1+r)}(1+1/G)$ entlang der ursprünglichen Flussachse. Uhrfaktor und Feldachsenkomponente allein können das Vorzeichen dieser Längsbewegung nicht prüfen. Eine gerichtete Längsauslesung ergänzt den Vergleich.

**Longitudinal motion in the HC comparison.** The declared boost sequence gives $v_k/c=\sqrt{(1-r)/(1+r)}(1+1/G)$ along the original flux axis. Clock factor and field-axis velocity alone cannot check the sign of this longitudinal motion. A signed longitudinal readout completes that comparison.

**Ausrichtung des HC-Zielprofils.** Bei festgehaltener aktiver Dualitätsphase bestimmen vollständige Beobachtergeschwindigkeit und zwei linear unabhängige gerichtete Zielfelder die Lorentzabbildung eindeutig. Im flussfreien Profil lassen parallele Felder Drehungen um ihre gemeinsame Achse offen.

**Alignment of the HC target profile.** With active duality fixed, full observer velocity and two linearly independent directed target fields determine the Lorentz map uniquely. In a flux-free profile, parallel fields leave rotations about their common axis undetermined.

**Dualitätsphase und Achsenausrichtung.** Bei festem Beobachter und nichtnullartigen, linear unabhängigen Feldern bleibt ohne deklarierte Dualitätsphase eine Zweideutigkeit. Ein Vorzeichenwechsel der Phase kann durch eine Halbdrehung um den Energiefluss kompensiert werden. Das HC-Beispiel exportiert diese Gleichheit der Feldausgaben für das komplexe Zahlenbeispiel. Am nichtverschwindenden nullartigen Feld gibt es eine kontinuierliche Familie solcher Kompensationen.

**Duality phase and axis alignment.** At fixed observer velocity, non-null independent fields leave a twofold ambiguity if the duality phase is free. A sign change in phase can be compensated by a half-turn around the energy flux. The HC example exports the equality of field outputs for its complex numerical case. A nonzero null field allows a continuous family of such compensations.

**Geschlossene Feldfolge und gerichtete Hauptachse.** Für $w(\theta)=e^{i\theta}R_z(\theta)(2e_x+i e_y)$ kehrt das Feld bei $\theta=\pi$ zurück. Eine stetig gerichtete Hauptachse endet mit umgekehrtem Vorzeichen. Ihr Projektor und die daraus gebildete HC-Halbdrehung kehren zurück. Gerichtete Auslesungen brauchen daher einen zusätzlichen Bezug oder entlang der Route mitgeführte Orientierung.

**Closed field path and directed principal axis.** For $w(\theta)=e^{i\theta}R_z(\theta)(2e_x+i e_y)$, the field returns at $\theta=\pi$. A continuously oriented principal axis returns with the opposite sign. Its projector and the HC half-turn return to their initial values. Signed readouts therefore need a reference or an orientation carried along the path.

**Umlaufregel für die Hauptachse.** Auf einem geschlossenen Feldweg mit $s\ne0$ endet die stetig mitgeführte Hauptachse bei $(-1)^m a(0)$, wobei $m$ die Umlaufzahl von $s$ um null ist. Der Projektor kehrt immer zurück. Für die gerichtete Auslesung ist die Parität eine Information über den Weg.

**Winding rule for the principal axis.** Along a closed field path with $s\ne0$, the continuously oriented principal axis ends at $(-1)^m a(0)$, where $m$ is the winding number of $s$ around zero. The projector always returns. The parity is path information for signed readouts.

**Robuste Umlaufparität.** Hat das geschlossene Messpolygon für $s$ einen Nullabstand größer als $\delta+L\Delta/2$, stimmt seine Umlaufparität mit der Feldroute überein. Dabei sind $\delta$ die komplexe Messfehlerschranke, $L$ die Lipschitz-Schranke und $\Delta$ die größte Abtastlücke. Acht gleichmäßig verteilte Werte genügen im gewählten Kreisbeispiel bei $\delta=0{,}1$ und $L=6\pi$.

**Robust winding parity.** If the closed measurement polygon for $s$ stays farther from zero than $\delta+L\Delta/2$, its winding parity agrees with the field path. Here $\delta$ bounds complex measurement error, $L$ is the Lipschitz bound, and $\Delta$ is the largest sampling gap. Eight equally spaced values suffice in the chosen circle example with $\delta=0.1$ and $L=6\pi$.

**Umlaufparität bei wechselndem Gain.** Die offsetfreie Auslesung erhält die Phase bei beliebigem positivem Gain pro Abtastpunkt. Sind wahre Winkeländerung und die beiden Phasenfehlerschranken zusammen kleiner als $\pi$, ist der gemessene Hauptwert des Phasenschritts eindeutig. Am geschlossenen Weg addieren sich diese Schritte zur wahren Umlaufzahl mal $2\pi$.

**Winding parity with varying gain.** The offset-free readout preserves phase under any positive gain at each sample. If true angular change plus both phase error bounds is below $\pi$, the principal phase increment is unambiguous. On the closed path these increments sum to the true winding number times $2\pi$.

Das HC-Beispiel exportiert die geschlossene Feldfolge, die umgekehrte gerichtete Hauptachse und den Nachweis aus abgetasteten Phasen getrennt. Acht Abtastschritte mit relativer Restfehlerschranke $0{,}1$ sichern im Kreisbeispiel Umlaufzahl eins.

The HC example exports the closed field path, reversed oriented axis, and sampled phase certificate separately. Eight sampling steps with a relative residual-error bound of $0.1$ certify winding number one in the circle example.

**Zwei Wege zum gleichen Sektorwert.** Zwei aktive Feldwege von $w_0=2e_x+i e_y$ nach $i w_0$ führen $s$ über entgegengesetzte Halbkreise von $3$ nach $-3$. Sie haben dieselben vollständigen Endfelder und entgegengesetzte stetig mitgeführte Zielachsen. Ihr zusammengesetzter geschlossener Weg hat Umlaufzahl eins. Das HC-Beispiel exportiert beide Wege und den Vorzeichenvergleich relativ zu derselben deklarierten Zielrichtung.

**Two paths to the same sector value.** Two active field paths from $w_0=2e_x+i e_y$ to $i w_0$ take $s$ from $3$ to $-3$ along opposite semicircles. Their full endpoint fields agree, while their continuously transported target axes point in opposite directions. Their combined closed path has winding number one. The HC example exports both paths and compares their signs relative to the same declared target direction.

**Zusammensetzung der Achsenvorzeichen.** Bei gemeinsamer Zwischenreferenz multiplizieren sich die Vorzeichen der Teilwege. Die beiden Sektorwege liefern bei Rückkehr auf derselben Route $+1$, bei Wechsel der Route $-1$. Das vollständige Feld kehrt in allen vier Fällen zurück. Das geschlossene Produkt ist unabhängig von der Wahl der Referenzen.

**Composition of axis signs.** With a shared intermediate reference, segment signs multiply. Returning along the same sector path gives $+1$, while returning along the other gives $-1$. The full field returns in all four cases. The closed product is independent of the chosen references.

**Orientierung im symmetrisierten Rückweg.** Der gleiche und der gemischte Sektorrückweg liefern dasselbe Feld, aber die gerichteten Werte $+1$ und $-1$. Ihr Mittel verschwindet. Der ungerichtete Achsenprojektor bleibt erhalten. Soll die gerichtete Achse selbst durch eine Klasse auslesbar sein, sind beide Rückwege in der lokalen Konstruktion nicht zugleich klassenwahrend.

**Orientation in the symmetrized return.** The same-path and mixed-path sector returns give the same field with directed values $+1$ and $-1$. Their mean vanishes. The unoriented axis projector is preserved. If the oriented axis factors through the class, the two local returns cannot both preserve that class.

**Parität aus Transportbausteinen.** Gewöhnliche Lorentzstücke halten $s$ fest, aktive Dualitätsstücke ändern seinen fortgeführten Winkel um das Doppelte ihres Dualitätswinkels. Auf einer geschlossenen nichtnullartigen Route bleibt die Achsenorientierung genau dann erhalten, wenn die Summe der Dualitätswinkel ein Vielfaches von $2\pi$ ist. Weitere Operationen benötigen eine eigene Wegdefinition.

**Parity from transport steps.** Ordinary Lorentz segments preserve $s$, while active duality segments change its lifted angle by twice their duality angle. On a closed non-null path the axis orientation returns exactly when the sum of duality angles is a multiple of $2\pi$. Other operations require their own path definitions.

**Native Phasenbindung und Feldphase.** Der historische OP3-Antiphasenkorridor bindet den sichtbaren Schalenquotienten. Eine Orientierungsaussage über das Feld benötigt zusätzlich eine durchgehende Zuordnung zur Phase von $s$. Beispielsweise würde ein vollständiger geschlossener Weg in einer Scheibe um $-1$ mit Radius kleiner als eins und eine positive reelle Skalierung des Quotienten zu $s$ Umlaufzahl null garantieren.

**Native phase screening and field phase.** The historical OP3 anti-phase corridor constrains the visible shell ratio. An orientation statement about the field additionally needs a pathwise link to the phase of $s$. For example, an entire closed path in a disk around $-1$ of radius less than one, with a positive real rescaling of the ratio to $s$, would guarantee zero winding.

**Paritätsbrücke zur Schalenphase.** Hat der Schalenquotient Umlaufzahl null, entscheidet die Parität von $s/\zeta_{\rm sh}$ über die Achsenrückkehr. Eine unabhängig konstruierte geschlossene Quadratwurzel dieses Quotienten genügt. Damit sind auch gerade, von null verschiedene Umlaufzahlen zulässig.

**Parity bridge to the shell phase.** If the shell ratio has winding number zero, the parity of $s/\zeta_{\rm sh}$ decides axis return. An independently constructed closed square root of this ratio suffices. This permits nonzero even winding numbers.

**Historische Schalenkonjugation.** Die exakte Balance setzt die beiden linearen Schalengewinne entgegengesetzt und ihren Quotienten auf $-1$. Sie liefert keine quadratische Beziehung zur elektromagnetischen Invariante $s$. Für eine Paritätsbrücke muss eine solche Beziehung entlang der Route separat nachgewiesen werden.

**Historical shell conjugacy.** Exact balance makes the two linear shell gains opposite and their ratio $-1$. It provides no quadratic relation to the electromagnetic invariant $s$. A parity bridge needs such a relation along the path.

**Lokales Feldwörterbuch für die Paritätsbrücke.** Ein festes komplexes Nullpaar mit gemischtem Produkt eins erlaubt die Konstruktion $w=q(\ell u_++\zeta u_-/(2\ell))$ und liefert $s=\zeta q^2$. Der freie Parameter $\ell$ ändert die Feldskala und damit $r$, während $s$ gleich bleibt. Die Modellabbildung macht die zusätzlichen Annahmen für einen nativen Anschluss sichtbar.

**Local field dictionary for the parity bridge.** A fixed complex null pair with cross product one in the bilinear form permits $w=q(\ell u_++\zeta u_-/(2\ell))$, giving $s=\zeta q^2$. The free parameter $\ell$ changes the field scale and hence $r$ while preserving $s$. The model exposes the additional assumptions required for a native bridge.

**Beobachterparameter des Feldwörterbuchs.** Ein kollinearer Boost entlang $e_1\times e_2$ ändert $\ell$ zu $e^{-\eta}\ell$ bei festem $q,\zeta$. Der flussfreie Wert ist $\ell_*=\sqrt{|\zeta|/2}$. Somit ist $r=\operatorname{sech}(2\log(\ell/\ell_*))$ eine beobachterabhängige Auslesung auf derselben Feldbahn.

**Observer parameter of the field dictionary.** A collinear boost along $e_1\times e_2$ changes $\ell$ to $e^{-\eta}\ell$ at fixed $q,\zeta$. The flux-free value is $\ell_*=\sqrt{|\zeta|/2}$. Hence $r=\operatorname{sech}(2\log(\ell/\ell_*))$ depends on the observer along the same field orbit.

**HC auf den Wörterbuchdaten.** Die Feldinvolution erhält $\zeta$ und sendet $(q,\ell)$ auf $(i\bar\zeta\,\bar q/|\zeta|,|\zeta|/(2\ell))$. Damit wechseln $s$ zu $-\bar s$ und die relative Rapiditätskoordinate ihr Vorzeichen. Zweimalige Anwendung bringt beide Eingabedaten zurück.

**HC on dictionary inputs.** The field involution preserves $\zeta$ and maps $(q,\ell)$ to $(i\bar\zeta\,\bar q/|\zeta|,|\zeta|/(2\ell))$. Thus $s$ becomes $-\bar s$ and the relative rapidity coordinate changes sign. Applying the map twice returns both inputs.

**Grenze der Schalengewinn-Zuordnung.** Bei exakter Antiphase negiert die Vertauschung der beiden Gewinne jede feste lineare Auslesung $q$. Ihr Quadrat und damit $s$ bleiben gleich. Ein HC-Sektorwechsel auf reellem $s\ne0$ braucht in diesem Wörterbuch eine zusätzliche komplexe Phasenzuordnung.

**Limit of the shell gain assignment.** At exact anti-phase, exchanging the two gains negates any fixed linear readout $q$. Its square and hence $s$ stay unchanged. An HC sector exchange on real $s\ne0$ needs an additional complex phase assignment in this dictionary.

**Zwei Komponenten des Feldfaktors.** Bei $\zeta=-1$ hat die HC-Regel $q\mapsto-i\bar q$ eine feste und eine vorzeichenwechselnde reelle Linie. Die historische exakte Gewinnlinie trägt unter Vertauschung nur den vorzeichenwechselnden Anteil. Für einen reellen Sektorwechsel kann ein erweitertes Modell beide unabhängigen Komponenten führen. Deren native Realisierung verlangt einen eigenen Nachweis.

**Two components of the field factor.** At $\zeta=-1$, the HC rule $q\mapsto-i\bar q$ has a fixed real line and a sign-changing real line. Under exchange the historical exact gain line supplies only the sign-changing part. An extended model can carry both independent components for a real sector exchange. Their native realization requires a separate argument.

**Nichtlineare Gewinnkopplung.** Die Wahl $u=|g|$, $v=g$ liefert bei $\zeta=-1$ die Invariante $s=-4|g|g$ und reproduziert den diskreten HC-Sektorwechsel unter $g\mapsto-g$. Für diese eingeschränkte reelle Familie genügt ein Gewinn. Eine stetige reelle Route zwischen den Sektoren muss allerdings $g=s=0$ passieren.

**Nonlinear gain coupling.** The choice $u=|g|$, $v=g$ at $\zeta=-1$ gives $s=-4|g|g$ and reproduces the discrete HC sector exchange under $g\mapsto-g$. One gain suffices for this restricted real family. A continuous real path between the sectors must pass through $g=s=0$.

**Komplexe Gewinnfortsetzung.** Auf dem punktierten komplexen Gewinnraum gibt es eine stetige nullfreie Fortsetzung der reellen Kopplung mit $q(-g)=-i\bar q(g)$. Sie erlaubt einen Sektorwechsel ohne $s=0$. Jede solche einwertige Kopplung hat auf geschlossenen Gewinnwegen Umlaufzahl null, weil die Eingabedrehung um $\pi$ die Umlaufzahl erhält und die Ausgabekonjugation sie umkehrt.

**Complex gain extension.** A continuous nonzero extension of the real coupling exists on the punctured complex gain plane with $q(-g)=-i\bar q(g)$. It permits a sector change without crossing $s=0$. Every such single-valued coupling has zero winding on closed gain paths because the input half-turn preserves winding and output conjugation reverses it.

**Regularität der Gewinnkopplung.** Eine holomorphe Kopplung mit $q(-g)=-i\bar q(g)$ auf einem zusammenhängenden, unter Vorzeichenwechsel stabilen offenen Bereich ist konstant. Die nichttriviale Fortsetzung ist reell-glatt. Eine andere, selbst konjugierende Eingabeabbildung kann mit holomorpher Kopplung verträglich sein und verlangt eine eigene Zuordnung.

**Regularity of the gain coupling.** A holomorphic coupling satisfying $q(-g)=-i\bar q(g)$ on a connected open sign-invariant domain is constant. The nontrivial extension is smooth as a real map. A different, conjugating input map can permit a holomorphic coupling and requires its own identification.

**Symmetrischer Gewinn nahe Antiphase.** Bei $|\Gamma_{\rm exp}/\Gamma_{\rm ph}+1|\le\rho<1$ ist der Betrag des symmetrischen Gewinnanteils relativ zum antisymmetrischen höchstens $\rho/(2-\rho)$. Eine feste lineare Feldkopplung, die daraus reelles nichtnullartiges $s$ erzeugen soll, braucht mindestens den inversen relativen Kalibrierfaktor. Bei exakter Antiphase verschwindet der symmetrische Anteil.

**Symmetric gain near anti-phase.** If $|\Gamma_{\rm exp}/\Gamma_{\rm ph}+1|\le\rho<1$, the symmetric gain is at most $\rho/(2-\rho)$ times the antisymmetric gain in magnitude. A fixed linear field coupling producing real non-null $s$ needs at least the reciprocal relative calibration factor. Exact anti-phase sets the symmetric part to zero.

**Phasenschranke der linearen Gewinnkopplung.** Bei relativer Kalibriergrenze $K$ und Antiphasenradius $\rho$ ist $d=K\rho/(2-\rho)$ eine Obergrenze für $|u/v|$. Für $d<1$ gilt $|\operatorname{Im}s|/|s|\ge(1-d^2)/(1+d^2)$. Gleiche Kalibrierstärke und $\rho=0{,}1$ erzwingen mindestens $180/181$ imaginären Anteil.

**Phase bound for linear gain coupling.** With relative calibration bound $K$ and anti-phase radius $\rho$, $d=K\rho/(2-\rho)$ bounds $|u/v|$. For $d<1$, $|\operatorname{Im}s|/|s|\ge(1-d^2)/(1+d^2)$. Equal calibration strength and $\rho=0.1$ force an imaginary fraction of at least $180/181$.

**Phasenschranke bei variablem Feldquotienten.** Bei $|u/v|\le d<1$ und $|\zeta+1|\le\sigma<1$ liegt $s=\zeta q^2$ höchstens im Winkelabstand $2\arctan d+\arcsin\sigma$ zur negativen imaginären Achse. Bleibt diese Summe unter $\pi/2$, ist reelles $s$ im gewählten linearen Modell ausgeschlossen.

**Phase bound with a varying field ratio.** With $|u/v|\le d<1$ and $|\zeta+1|\le\sigma<1$, the angular distance of $s=\zeta q^2$ from the negative imaginary axis is at most $2\arctan d+\arcsin\sigma$. Below $\pi/2$ the chosen linear model excludes real $s$.

**HC-verträgliche Kopplung bei komplexem Quotienten.** Für $\zeta=-|\zeta|e^{i\delta}$ drehen sich die beiden reellen Gewinnlinien im Feldfaktor um $-\delta/2$. Beim Bilden von $s=\zeta q^2$ kürzt sich die Phase exakt heraus. Bei festem Quotienten unter der Gewinnvertauschung gilt daher dieselbe Phasenschranke wie bei $\zeta=-1$.

**HC-compatible coupling with a complex ratio.** For $\zeta=-|\zeta|e^{i\delta}$, the two real gain lines in the field factor rotate by $-\delta/2$. The phase cancels in $s=\zeta q^2$. When the ratio is fixed under gain exchange, the same phase bound as for $\zeta=-1$ applies.

**Feldquotient unter HC.** Bei festen Laborachsen und positiven $\ell$ muss der Feldquotient bei der HC-Abbildung seine Phase behalten. Eine positive Skalierung $\zeta\mapsto\lambda\zeta$ kann durch $q\mapsto q/\sqrt\lambda$ und $\ell\mapsto\sqrt\lambda\,\ell$ kompensiert werden und ändert das Feld nicht.

**Field ratio under HC.** With fixed laboratory axes and positive $\ell$, the field ratio must retain its phase under HC. A positive rescaling $\zeta\mapsto\lambda\zeta$ can be compensated by $q\mapsto q/\sqrt\lambda$ and $\ell\mapsto\sqrt\lambda\,\ell$ without changing the field.

**Achsendarstellung des Feldquotienten.** Eine Drehung der Basis um $\theta$ verändert die Koordinaten zu $q'=e^{i\theta}q$ und $\zeta'=e^{-2i\theta}\zeta$. Das geometrische Feld und $s$ bleiben gleich. Für den Vergleich mit dem historischen Schalenquotienten braucht QAM eine deklarierte Achsenkonvention.

**Axis representation of the field ratio.** Rotating the basis by $\theta$ changes the coordinates to $q'=e^{i\theta}q$ and $\zeta'=e^{-2i\theta}\zeta$. The geometric field and $s$ agree. Comparing against the historical shell ratio requires a declared axis convention.

**Umlaufparität und Achsenwahl.** In einer geschlossenen Darstellung gilt $m_s=m_\zeta+2m_q$. Geschlossene Achsendrehungen verschieben die Umlaufzahl von $\zeta$ nur um gerade Zahlen. Eine konstante Quotientenphase bei ungerader Feldparität erfordert in dieser Konstruktion umgekehrte Endachsen und einen umgekehrten Feldfaktor. Das HC-Beispiel exportiert die feste und die mitrotierende Darstellung desselben Feldkreises getrennt.

**Winding parity and axis choice.** In a closed representation, $m_s=m_\zeta+2m_q$. Closed axis rotations change the winding of $\zeta$ only by even integers. Holding the ratio phase constant at odd field parity requires reversed endpoint axes and a reversed field factor in this construction. The HC example exports the fixed and rotating representations of the same field loop separately.

**Parität aus lokalen Antiphasendarstellungen.** Sind die lokalen Feldquotienten auf $-1$ normiert, können sich benachbarte transversale Basen am gemeinsamen Feldpunkt um eine Halbdrehung unterscheiden. Das Produkt der Übergangsvorzeichen einschließlich des Schließübergangs ist $(-1)^{m_s}$. Lokale Referenzumkehrungen ändern jeweils zwei Faktoren und lassen das Produkt gleich. Das HC-Beispiel exportiert die zwei lokalen Stücke und ihre Übergangsvorzeichen $(-1,+1)$.

**Parity from local anti-phase representations.** With each local field ratio normalized to $-1$, neighboring transverse bases can differ by a half-turn at their shared field point. The product of transition signs, including closure, equals $(-1)^{m_s}$. Reversing a local reference changes two factors and preserves the product. The HC example exports the two local pieces and their transition signs $(-1,+1)$.

**Orientierung im Routennetz.** Teilwege zwischen deklarierten Zuständen tragen Vorzeichen. Ein Spannbaum legt die Knotenreferenzen fest. Die verbleibenden Kanten prüfen je einen Grundkreis. Eine gemeinsame gerichtete Orientierung existiert genau dann, wenn alle diese Kreisprodukte positiv sind.

**Orientation on a route network.** Segments between declared states carry signs. A spanning tree fixes the node references. Each remaining edge tests one fundamental cycle. A common directed orientation exists exactly when all these cycle products are positive.

**Orientierter Routenträger.** Für gerichtete Auslesungen kann QAM den Zustand als $(x,\sigma)$ mit Orientierungsbit führen. Eine Kante mit Vorzeichen $\epsilon$ liefert $(y,\epsilon\sigma)$. Ein negativer Feldkreis wechselt das Bit. Zweimaliger Durchlauf desselben Feldkreises bringt es zurück. Das HC-Beispiel exportiert beide Rückkehrstufen.

**Oriented route carrier.** For signed readouts, QAM can carry $(x,\sigma)$ with an orientation bit. An edge of sign $\epsilon$ gives $(y,\epsilon\sigma)$. A negative field cycle flips the bit. Traversing the same cycle twice returns it. The HC example exports both stages of return.

**Orientierung bei Routenverfeinerung.** Grober und verfeinerter Weg mit denselben Endfeldern transportieren die gerichtete Hauptachse genau dann gleich, wenn der geschlossene Vergleich mit dem inversen groben Weg gerade Umlaufzahl hat. Eine stetige Verformung bei festen Endfeldern und durchgehend $s\ne0$ genügt.

**Orientation under route refinement.** A coarse and refined path with the same endpoint fields carry the directed principal axis identically exactly when the comparison loop with the inverse coarse path has even winding. A continuous deformation fixing the endpoint fields and keeping $s\ne0$ suffices.

**Abstandsprüfung bei Verfeinerung.** Bleibt $|s_{\rm fein}-s_{\rm grob}|<|s_{\rm grob}|$ entlang des synchronisierten Wegs mit gleichen Endfeldern, hat der Quotient Umlaufzahl null. Grober und feiner Weg tragen dann dieselbe Orientierung. Aus Messpolygonen folgt eine hinreichende Prüfung, wenn die Abweichungen von den wahren Kurven separat beschränkt sind.

**Distance check for refinement.** If $|s_{\rm fine}-s_{\rm coarse}|<|s_{\rm coarse}|$ along synchronized paths with equal endpoint fields, the ratio has zero winding. Both paths carry the same orientation. Sampled polygons give a sufficient check when their deviations from the true curves are bounded separately.

**Kalibrierungsfreier Phasenvergleich.** Bei gleichen Endfeldern genügt es, wenn der normierte Phasenquotient von feinem und grobem Weg nie $-1$ erreicht. Er hat dann Umlaufzahl null. Getrennte positive Verstärkungen fallen heraus. Für abgetastete Daten braucht man Winkelgrenzen für Messfehler und Zwischenverlauf. Das HC-Beispiel exportiert den Vergleich für eine reine Betragsänderung und für die ungerade relative Umlaufzahl der beiden Sektorwege.

**Calibration-independent phase comparison.** With equal endpoint fields, it suffices for the normalized phase ratio of refined and coarse paths to avoid $-1$. It then has zero winding. Separate positive gains cancel. Sampled data require angular bounds on measurement errors and the path between samples. The HC example exports both a magnitude-only change and the odd relative winding of the two sector paths.

**Reeller historischer Schalenquotient.** Der Quotient $e_{\rm sh}/p_{\rm sh}$ besteht aus zwei vorzeichenbehafteten reellen Beiträgen. Jede Antiphase-Komponente bei festem Vorzeichen von $p_{\rm sh}$ ist konvex. Eine stetige nullfreie Feldinvariante, die auf der ganzen Komponente allein durch dieses Beitragspaar bestimmt wird, hätte auf geschlossenen Beitragswegen Umlaufzahl null. Das erforderliche Feldwörterbuch ist separat nachzuweisen.

**Real historical shell ratio.** The ratio $e_{\rm sh}/p_{\rm sh}$ uses two signed real contributions. Each anti-phase component at fixed sign of $p_{\rm sh}$ is convex. A continuous nonzero field invariant determined solely by this pair on the entire component would have zero winding on closed contribution paths. This requires a separate field dictionary.

**Exakter Schalenpunkt und Feldhintergrund.** Die historischen Schalenbeiträge sind Terme erster Ordnung in zwei Abweichungen und verschwinden am exakten Schalenpunkt. Eine homogene Feldkopplung erzwingt dort $s=0$. Ein nichtnullartiger Feldhintergrund benötigt einen eigenen Term $s_0$ und eine begründete Kontrolle der Abweichung davon.

**Exact shell point and field background.** The historical shell contributions are first-order terms in two defects and vanish at the exact shell point. A homogeneous field coupling forces $s=0$ there. A non-null field background requires its own term $s_0$ and a justified bound on deviations from it.

**HC-fester Feldhintergrund.** Ein nichtverschwindendes Feld, das von $J_B$ festgehalten wird, hat $E_0=B_0$ und rein imaginäres $s_0$. Bleibt $|s-s_0|<|s_0|$, sind reelle Sektorwerte ausgeschlossen und geschlossene Wege haben Umlaufzahl null. Reelle nichtnullartige Hintergrundwerte können stattdessen als HC-gepaartes Paar $s_0,-s_0$ auftreten.

**HC-fixed field background.** A nonzero field fixed by $J_B$ has $E_0=B_0$ and purely imaginary $s_0$. If $|s-s_0|<|s_0|$, real sector values are excluded and closed paths have zero winding. Real non-null backgrounds can instead form an HC-related pair $s_0,-s_0$.

**HC-gepaarte Schalenhintergründe.** Zwei affine Feldprofile mit $w_-=J_Bw_+$ und Störung $pV+eJ_BV$ erfüllen $J_BW_+(p,e)=W_-(e,p)$. Kleine Schalenabweichungen halten die Invarianten in getrennten nullfreien Scheiben um die beiden Hintergrundwerte. Die Hintergründe und die Feldkopplung der Abweichungen sind zusätzliche Modelldaten.

**HC-related shell backgrounds.** Two affine field profiles with $w_-=J_Bw_+$ and perturbation $pV+eJ_BV$ satisfy $J_BW_+(p,e)=W_-(e,p)$. Small shell deviations keep the invariants in separate nonzero disks around the background values. The backgrounds and the field coupling of the deviations are additional model data.

**Reeller Sektor der affinen Kopplung.** In $W_\pm=w_\pm+pV+eJ_BV$ erzeugt $V\cdot J_BV=i\|V\|^2$ einen gemischten Imaginärterm. Auf der exakten Antiphasenlinie $e=-p$ kann $s$ über ein ganzes Intervall nur dann reell bleiben, wenn die affine Störung dort verschwindet.

**Real sector of the affine coupling.** In $W_\pm=w_\pm+pV+eJ_BV$, the identity $V\cdot J_BV=i\|V\|^2$ produces a mixed imaginary term. Along the exact anti-phase line $e=-p$, $s$ can stay real on an entire interval only when the affine perturbation vanishes there.

**Profilabhängige affine Kopplung.** Wenn die Koeffizienten beider Profile separat und durch HC verknüpft sind, kann eine affine Feldkopplung $s$ entlang exakter Antiphase reell halten und variieren. Im Modell ergeben sich $3+6p$ und $-3+6p$. HC wechselt dabei das Profil und vertauscht die Beiträge.

**Profile-dependent affine coupling.** With separate HC-related coefficients for the two profiles, an affine field coupling can keep $s$ real and vary it along exact anti-phase. The model gives $3+6p$ and $-3+6p$. HC exchanges the profiles and the two contributions.

**Uhrfaktor auf der Antiphasenlinie.** Im profilierten affinen Modell bleibt $e/p=-1$, während der äußere Faktor $G=(5+2p+2p^2)/(3+6p)$ variiert. Der exakte Schalenpunkt hat $G=5/3$. Der nominale r08-Wert $1{,}8647$ entspricht in diesem Modell ungefähr $p=-0{,}064$.

**Clock factor on the anti-phase line.** In the profiled affine model, $e/p=-1$ while the outer factor $G=(5+2p+2p^2)/(3+6p)$ varies. The exact shell point has $G=5/3$. In this model the nominal r08 value $1.8647$ corresponds to approximately $p=-0.064$.

**Schalenrest und Auswahl des Uhrfaktors.** Auf $e=-p$ verschwindet der lineare Rest für jeden $p$. Eine nachgewiesene nichtverschwindende quadratische Restkrümmung könnte $p$ lokal begrenzen. Die historische obere Restschranke allein liefert diese Information nicht. Ein vertauschungsinvarianter Rest ließe zudem das Vorzeichen von $p$ offen.

**Shell residual and clock-factor selection.** Along $e=-p$, the linear residual vanishes for every $p$. A proven nonzero quadratic residual coefficient could locally bound $p$. The historical upper remainder bound alone does not supply this information. An exchange-invariant residual would also leave the sign of $p$ undetermined.

**Quadratischer Rest und Nullkurve.** Der Koeffizient $\kappa$ entlang $e=-p$ benötigt die Hesse-Matrix der sichtbaren Schalenamplitude. Die historische erste Ordnung legt ihn nicht fest. Bei glatter zweidimensionaler Auslesung mit $\partial_eF(0,0)=1$ verläuft die exakte Nullkurve lokal als $e=-p-\kappa p^2+o(p^2)$. Sichtbare Restnull kann daher im Antiphasenkorridor auch bei $p\ne0$ auftreten.

**Quadratic residual and zero curve.** The coefficient $\kappa$ along $e=-p$ requires the Hessian of the visible shell amplitude. The historical first-order formula leaves it undetermined. With a smooth two-dimensional readout and $\partial_eF(0,0)=1$, the exact zero curve is locally $e=-p-\kappa p^2+o(p^2)$. Visible residual zero can therefore occur in the anti-phase corridor with $p\ne0$.

**Ein-Schalenkoordinaten-Route.** Bei linearer Balance $Aa=-Bb=g$ ist der quadratische Restkoeffizient auf der Route $p_2+e_2+\kappa g^2$. Er enthält die Krümmung der Beitragsroute und die Hesse-Ableitungen der sichtbaren Auslesung. Die historischen quadratischen Obergrenzen legen diesen Koeffizienten nicht fest.

**Single-shell-coordinate route.** With linear balance $Aa=-Bb=g$, the quadratic residual coefficient along the route is $p_2+e_2+\kappa g^2$. It depends on both route curvature and the Hessian of the visible readout. The historical quadratic upper bounds leave it undetermined.

**Vertauschung und Schalenkrümmung.** Auch die exakte Symmetrie $p(-\xi)=e(\xi)$ lässt einen quadratischen Term im symmetrischen Beitrag zu. Für $F=2U+V^2$ erfüllen die Routen $(U,V)=(0,\xi)$ und $(-\xi^2/2,\xi)$ dieselbe Vertauschung und liefern Rest $\xi^2$ beziehungsweise null.

**Exchange and shell curvature.** Even exact symmetry $p(-\xi)=e(\xi)$ allows a quadratic term in the symmetric contribution. For $F=2U+V^2$, routes $(U,V)=(0,\xi)$ and $(-\xi^2/2,\xi)$ obey the same exchange and give residual $\xi^2$ and zero, respectively.

**Koordinatenwechsel der Schalenkrümmung.** Die Umparametrisierung $e'=e+cp^2$ verschiebt die Routenkrümmung um $+c$ und den quadratischen Auslesekoeffizienten um $-c$. Ihre Summe bleibt gleich. Sie entscheidet, ob sich zulässige Route und Nullkurve in zweiter Ordnung trennen.

**Coordinate change of shell curvature.** The reparametrization $e'=e+cp^2$ shifts route curvature by $+c$ and the quadratic readout coefficient by $-c$. Their sum is unchanged and determines whether the admissible route and the zero curve separate at second order.

**Direkte Auslesung des quadratischen Schalenrests.** Der symmetrische Vergleich $[f(h)+f(-h)-2f(0)]/(2h^2)$ schätzt den gemeinsamen quadratischen Koeffizienten entlang der Route. Eine Schranke der vierten Ableitung und garantierte Messfehler liefern ein Intervall. Nur wenn es null ausschließt, ist die Trennung in zweiter Ordnung nachgewiesen.

**Direct readout of the quadratic shell residual.** The symmetric comparison $[f(h)+f(-h)-2f(0)]/(2h^2)$ estimates the combined quadratic coefficient along the route. A fourth-derivative bound and guaranteed measurement errors give an interval. Separation at second order is certified when that interval excludes zero.

**Isolierte Restnull.** Bei $f(0)=f'(0)=0$, $|f''(0)|/2\ge k_*>0$ und $|f'''|\le M_3$ gilt lokal $|f(p)|\ge p^2(k_*-M_3|p|/6)$. Im kontrollierten Bereich $M_3|p|\le3k_*$ ist null der einzige exakte Nullpunkt. Eine Restschwelle begrenzt dort auch $|p|$.

**Isolated residual zero.** If $f(0)=f'(0)=0$, $|f''(0)|/2\ge k_*>0$, and $|f'''|\le M_3$, then locally $|f(p)|\ge p^2(k_*-M_3|p|/6)$. In the controlled region $M_3|p|\le3k_*$, zero is the only exact root. A residual threshold also bounds $|p|$ there.

**Restnull bei ungleichen linearen Schalengewinnen.** Die historischen Restschranken ergeben entlang einer Ein-Schalenkoordinaten-Route $|f-D\xi|\le C_*|\xi|^2$ mit Gewinnüberschuss $D$. Für $D\ne0$ ist im Bereich $C_*|\xi|\le |D|/2$ die exakte Schale die einzige Restnull. Bei exakter Gewinnbalance braucht es wieder die höhere Ordnung.

**Residual zero with unequal linear shell gains.** The historical remainder bounds give $|f-D\xi|\le C_*|\xi|^2$ along a single-coordinate route, where $D$ is the gain imbalance. For $D\ne0$, the exact shell is the only zero where $C_*|\xi|\le |D|/2$. Exact gain balance still requires higher-order data.

Das [QAM-Beispiel zur Schalenrestnull](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/shell-residual.tex) führt den linearen Ausschluss bei Gewinnüberschuss und den quadratischen Nachweis bei exakter Balance getrennt. Zwei gewählte Routen mit identischer linearer Balance liefern die Restkoeffizienten $1$ und $0$.

The [shell residual QAM example](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/shell-residual.tex) separates the linear certificate at gain imbalance from the quadratic certificate at exact balance. Two chosen routes with identical linear balance give residual coefficients $1$ and $0$.

**Einseitige Schalenroute.** Der quadratische Koeffizient lässt sich auch aus den Restwerten bei $0,h,2h$ abschätzen. Bei einer Schranke $M_3$ für die dritte Ableitung beträgt der Fehler der exakten Differenz höchstens $M_3h/2$. Die lineare Balance muss für den Nullnachweis separat feststehen. Das Schalenrest-Beispiel exportiert auch diese Variante.

**One-sided shell route.** Residual values at $0,h,2h$ also estimate the quadratic coefficient. With a third-derivative bound $M_3$, the error of the exact difference is at most $M_3h/2$. Linear balance must be established separately for the zero certificate. The shell residual example also exports this variant.

**Einseitige Auslesung der linearen Balance.** Aus denselben Werten bei $0,h,2h$ schätzt $[-3f(0)+4f(h)-f(2h)]/(2h)$ den linearen Koeffizienten. Bei $|f'''|\le M_3$ ist der Fehler der exakten Differenz höchstens $M_3h^2/3$. Ein Intervall um null belegt keine exakte Balance.

**One-sided readout of linear balance.** The same values at $0,h,2h$ give the linear estimate $[-3f(0)+4f(h)-f(2h)]/(2h)$. With $|f'''|\le M_3$, the error of the exact difference is at most $M_3h^2/3$. An interval containing zero does not establish exact balance.

**Zusätzliche Restnull bei unklarem linearem Vorzeichen.** Dieselben drei einseitigen Datenintervalle können mit $f(\xi)=\xi^2$ und $f(\xi)=-\xi/1000+(201/200)\xi^2$ vereinbar sein. Beide haben positive Krümmung, aber die zweite Funktion hat bei $1/1005$ eine weitere Null. Ein abgesichertes nichtnegatives lineares Vorzeichen schließt diesen Fall im kontrollierten quadratischen Bereich aus.

**Additional residual zero with uncertain linear sign.** The same three one-sided data intervals can admit $f(\xi)=\xi^2$ and $f(\xi)=-\xi/1000+(201/200)\xi^2$. Both have positive curvature, but the second has another zero at $1/1005$. A certified nonnegative linear term excludes this case in the controlled quadratic region.

**Scharfer Bereich für eine zweite Restnull.** Im exakt quadratischen Modell mit $f(0)=0$ ergeben die gemeinsamen Rohdatenintervalle bei $h=0{,}1$ und $2h$ für eine zusätzliche positive Null genau den möglichen Bereich $(0,1/406]$. Die äußerste Ecke der beiden Intervalle erreicht die Grenze. Höhere Restordnungen brauchen eine eigene Abschätzung.

**Sharp range for a second residual zero.** For an exactly quadratic model with $f(0)=0$, the joint raw intervals at $h=0.1$ and $2h$ give the exact possible range $(0,1/406]$ for an additional positive zero. A corner of the two intervals attains the bound. Higher-order residuals require a separate estimate.

**Restnull mit höherer Ordnung.** Bei den Modellintervallen bei $0,0{,}1,0{,}2$ und zusätzlicher Schranke $|f'''|\le0{,}1$ liegt eine mögliche zweite positive Null höchstens bei etwa $0{,}002778$ auf der abgetasteten Strecke. Eine kubische Extremfunktion erreicht die Grenze. Für verschwindende dritte Ableitung ergibt sich wieder $1/406$.

**Residual zero with higher-order terms.** With the model intervals at $0,0.1,0.2$ and the additional bound $|f'''|\le0.1$, a possible second positive zero on the sampled interval lies at or below approximately $0.002778$. A cubic extremizer attains the bound. A vanishing third derivative recovers $1/406$.

**HC-Boost und Flächenquantum.** Ein unitärer Profilwechsel desselben Flächenoperators erhält sein Spektrum. Hat dieses eine kleinste positive Fläche, kann ein solcher Wechsel die Fläche nicht um den r10-Faktor $1/G$ skalieren, außer $G=1$. Der HC-Uhrfaktor benötigt für die r10-Zählannahme eine zusätzliche Spektralabbildung.

**HC boost and area quantum.** A unitary profile change of the same area operator preserves its spectrum. If there is a smallest positive area, this change cannot scale it by the r10 factor $1/G$ unless $G=1$. The HC clock factor needs a separate spectral map for the r10 counting assumption.

**Eingeschränkter Horizontzugang.** Eine Auswahl vorhandener Spektralstufen kann die kleinste positive Fläche desselben Operators nicht senken. Eine Kompression auf einen nicht reduzierenden Teilraum kann kleinere Eigenwerte liefern. Diese gehören zu einem effektiven Operator und sind im Zweiniveaubeispiel Erwartungswerte der ursprünglichen Flächenmessung.

**Restricted horizon access.** Selecting existing spectral levels cannot lower the smallest positive area of the same operator. Compressing onto a nonreducing subspace can give smaller eigenvalues. These belong to an effective operator and are expectation values of the original area measurement in the two-level example.

**Varianzprüfung der Flächenauslesung.** Für Ausgänge in $\{0\}\cup[a,\infty)$ und Mittelwert $0<\mu<a$ gilt $\operatorname{Var}(A)\ge\mu(a-\mu)$. Ein scharfer effektiver Wert $\mu=a/G$ hat dagegen Varianz null bezüglich seiner eigenen Messung. So lassen sich derselbe Mittelwert und verschiedene Flächenauslesungen auseinanderhalten.

**Variance check of the area readout.** For outcomes in $\{0\}\cup[a,\infty)$ and mean $0<\mu<a$, $\operatorname{Var}(A)\ge\mu(a-\mu)$. A sharp effective value $\mu=a/G$ instead has zero variance under its own measurement. This distinguishes area readouts with the same mean.

**Exponentielles Flächengewicht.** Für Flächenausgänge in $\{0\}\cup[a,\infty)$ und mittlere Fläche $a/G$ mit $G>1$ gilt $\mathbb E[e^{-\lambda A}]\ge1-1/G+e^{-\lambda a}/G>e^{-\lambda a/G}$ bei $\lambda>0$. Das Gewicht eines scharfen effektiven Werts unterscheidet sich somit vom spektral gemittelten Gewicht. Die vollständige Horizontzählung benötigt zusätzlich ihre Zustandsgewichte und Entartungen.

**Exponential area weight.** For area outcomes in $\{0\}\cup[a,\infty)$ and mean area $a/G$ with $G>1$, $\mathbb E[e^{-\lambda A}]\ge1-1/G+e^{-\lambda a}/G>e^{-\lambda a/G}$ for $\lambda>0$. A sharp effective value therefore has a different weight from the spectral average. The full horizon count also requires its state weights and degeneracies.

**Angepasste Fläche aus einem Gewicht.** Der Wert $-\log\mathbb E[e^{-\lambda A}]/\lambda$ stellt ein einzelnes exponentielles Gewicht als scharfen Flächenwert dar. Für eine nichtkonstante Flächenverteilung fällt er streng mit $\lambda$. Zwei unterschiedliche Gewichtungen derselben Auslesung können daher einen konstanten scharfen Wert von einer Mischung unterscheiden.

**Area fitted from one weight.** The value $-\log\mathbb E[e^{-\lambda A}]/\lambda$ represents one exponential weight as a sharp area. For a nonconstant area distribution it strictly decreases with $\lambda$. Two distinct weightings of the same readout can therefore distinguish a constant sharp value from a mixture.

**Kompression und Gewichtung.** Im endlichen Modell unterscheiden sich $P e^{-\lambda A}P$ und $e^{-\lambda PAP}$ auf dem zugänglichen Teilraum erstmals durch den quadratischen Term $\lambda^2 PA(I-P)AP/2$, sofern er von null verschieden ist. Der Term misst die Kopplung an die ausgeblendeten Zustände. Ist der Teilraum reduzierend, stimmen beide Gewichtungen überein.

**Compression and weighting.** In the finite model, $P e^{-\lambda A}P$ and $e^{-\lambda PAP}$ on the accessible subspace first differ by the quadratic term $\lambda^2 PA(I-P)AP/2$ when it is nonzero. This term measures coupling to excluded states. Both weightings agree on a reducing subspace.

**Spurvergleich bei fester Gewichtung.** Im endlichen Modell gilt $\operatorname{tr}_P(Pe^{-\lambda A}P)\ge\operatorname{tr}_P e^{-\lambda A_{\rm eff}}$ für jedes $\lambda>0$. Gleichheit bei einem solchen Parameter gilt genau für einen reduzierenden Teilraum. Der Vergleich ist eine Spuraussage bei gemeinsamem Gewichtungsmaß.

**Trace comparison at fixed weighting.** In the finite model, $\operatorname{tr}_P(Pe^{-\lambda A}P)\ge\operatorname{tr}_P e^{-\lambda A_{\rm eff}}$ for every $\lambda>0$. Equality at any such parameter holds exactly for a reducing subspace. This compares traces with a common weighting measure.

**Spektralauswahl und Neunormierung in r10.** Entfernt man bei festem $\gamma$ positive Spinbeiträge aus der auf eins normierten Zählsumme, fällt die Summe unter eins. Erst ihre erneute Normierung erfordert ein kleineres $\gamma$. Die Spin-Auswahl allein ändert keine vorhandene Flächenstufe desselben Operators.

**Spectral selection and renormalization in r10.** At fixed $\gamma$, removing positive spin contributions lowers the normalized counting sum below one. Restoring normalization then requires a smaller $\gamma$. Spin selection alone does not change an existing area level of the same operator.

**Boost und Minimalspinzugang.** Im Ein-Punkt-Vergleich mit gemeinsamem Flächenoperator und $K\propto A$ ist die Minimalspinmaske eine Spektralprojektion des Boostgenerators. Eine unitäre Abbildung, die mit dessen Spektralprojektionen kommutiert, erhält diese Maske und den vollen Zugang jeweils separat. Eine native Einschränkung auf Minimalspin verlangt eine eigene Zugangsregel.

**Boost and minimal-spin access.** In the single-puncture comparison with a shared area operator and $K\propto A$, the minimal-spin mask is a spectral projection of the boost generator. A unitary commuting with its spectral projections preserves that mask and full access separately. Native restriction to minimal spin requires its own access rule.

**Gesamtfläche und Minimalspin.** Im additiven Mehrpunktmodell haben vier Minimalspinpunkte dieselbe Gesamtfläche wie ein Punkt mit $j=3$. Ein gemeinsamer Boostgenerator proportional zur Gesamtfläche kann die Belegungen nicht unterscheiden. Die Minimalspinmaske braucht auf einem Träger mit beiden Belegungen zusätzliche Punktdaten.

**Total area and minimal spin.** In the additive multi-puncture model, four minimal-spin punctures have the same total area as one puncture with $j=3$. A shared boost generator proportional to total area cannot distinguish the configurations. A minimal-spin mask needs additional puncture data if both configurations are admitted.

**Fläche und Punktzahl.** Im additiven Horizontmodell mit $j\ge1/2$ erkennt der Überschuss $X=\mathcal A-a(1/2)N$ die Minimalspinbelegung bei $N>0$ exakt. Die kleinste positive Abweichung beträgt $\sqrt2-\sqrt3/2$. Gesamtfläche und Punktzahl genügen gemeinsam. Die native Zugänglichkeit der Punktzahl und die Auswahl durch T bleiben eigene Bedingungen.

**Area and puncture count.** In the additive horizon model with $j\ge1/2$, the excess $X=\mathcal A-a(1/2)N$ identifies all-minimal spin when $N>0$. The smallest positive deviation is $\sqrt2-\sqrt3/2$. Total area and puncture count suffice jointly. Native access to puncture count and T selection remain separate requirements.

**Thermisches Gewicht und Minimalspin.** Bei fester Punktzahl ändert der Wechsel von Gesamtfläche zu $X=\mathcal A-a(1/2)N$ die normierte Spinverteilung nicht. Eine zusätzliche endliche Unterdrückung $e^{-\nu X}$ lässt höheren Spins positives Gewicht. Exakte Auswahl der Nullfaser braucht eine Projektion oder einen separat begründeten Grenzprozess.

**Thermal weighting and minimal spin.** At fixed puncture count, replacing total area by $X=\mathcal A-a(1/2)N$ leaves the normalized spin distribution unchanged. An extra finite penalty $e^{-\nu X}$ leaves higher spins with positive weight. Exact selection of the zero fiber requires a projection or a separately justified limit.

**Thermische Unterdrückung bei vielen Punkten.** Im unabhängigen Vergleichsmodell ist die Wahrscheinlichkeit einer vollständig minimalen Belegung $(1+R_\nu)^{-N}$. Für feste Zielgenauigkeit muss das höhere Spingewicht pro Punkt von der Größenordnung $1/N$ sein. Im Zweiniveaumodell braucht dies eine Strafe von der Größenordnung $(\log N)/\Delta$.

**Thermal suppression across many punctures.** In the independent comparison model the probability of an entirely minimal configuration is $(1+R_\nu)^{-N}$. At fixed target accuracy, the higher-spin weight per puncture needs to be of order $1/N$. In the two-level model this takes a penalty of order $(\log N)/\Delta$.

**Korrelationen und Minimalspin.** Bei gleicher höherer Einzelspinwahrscheinlichkeit $p$ und beliebiger Kopplung liegt die Wahrscheinlichkeit für ausschließlich Minimalspin scharf zwischen $\max(0,1-Np)$ und $1-p$. Die Einzelstatistik allein bestimmt die gemeinsame Maske nicht.

**Correlations and minimal spin.** With the same higher-spin marginal probability $p$ and arbitrary dependence, the probability of an entirely minimal configuration lies sharply between $\max(0,1-Np)$ and $1-p$. Single-puncture statistics alone do not determine the joint mask.

**Flächenmomente und gemeinsame Spinmaske.** Bei $\mu=\mathbb E[X]$, $M_2=\mathbb E[X^2]>0$ und Überschusslücke $\Delta$ gilt ohne Unabhängigkeit $\max(0,1-\mu/\Delta)\le P(X=0)\le1-\mu^2/M_2$. Das zweite Moment liefert Information über die gemeinsame Belegung, die dem Mittelwert fehlt.

**Area moments and the joint spin mask.** With $\mu=\mathbb E[X]$, $M_2=\mathbb E[X^2]>0$, and excess gap $\Delta$, the bounds $\max(0,1-\mu/\Delta)\le P(X=0)\le1-\mu^2/M_2$ hold without independence. The second moment adds information about joint occupancy beyond the mean.

**Exponentielle Auslesung der Minimalspinmaske.** Für $W_\nu=\mathbb E[e^{-\nu X}]$, Überschusslücke $\Delta>0$ und $q_\nu=e^{-\nu\Delta}$ gilt $\max(0,(W_\nu-q_\nu)/(1-q_\nu))\le P(X=0)\le W_\nu$. Das prüft die Maske im festgehaltenen Zustand ohne Unabhängigkeit der Punkte.

**Exponential readout of the minimal-spin mask.** For $W_\nu=\mathbb E[e^{-\nu X}]$, excess gap $\Delta>0$, and $q_\nu=e^{-\nu\Delta}$, the bound is $\max(0,(W_\nu-q_\nu)/(1-q_\nu))\le P(X=0)\le W_\nu$. This checks the mask in a fixed state without assuming independent punctures.

Das [QAM-Beispiel zum Horizontzugang](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/horizon-access.tex) exportiert den Flächengleichstand, die durch Punktzahl ergänzte Minimalspinmaske und die Schranken aus Momenten oder exponentieller Auslesung getrennt.

The [QAM horizon-access example](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/qam/examples/horizon-access.tex) separately exports the area collision, the minimal-spin mask augmented by puncture count, and bounds from moments or exponential readout.

**Flächengleichstand bei Gesamtspin null.** Vier Minimalspin-Singulettpaare und ein Singulettpaar aus zwei $j=3$-Punkten haben im additiven Vergleichsmodell beide Gesamtfläche $4\sqrt3$ und Gesamtspin null. Die Minimalspinmaske unterscheidet sie. Gesamtfläche und Gesamtspin allein genügen auf diesem Träger daher nicht.

**Area degeneracy at zero total spin.** Four minimal-spin singlet pairs and one singlet pair of two $j=3$ punctures both have area $4\sqrt3$ and total spin zero in the additive comparison model. The minimal-spin mask distinguishes them. Total area and total spin therefore do not suffice on this carrier.

**Maximale Punktzahl bei fester Fläche.** Ist $A_*=m\,a(1/2)$ und eine zulässige Belegung mit $m$ Minimalspinpunkten vorhanden, ist die Faser maximaler Punktzahl genau die Minimalspinmaske. Ohne eine solche sättigende Belegung kann die Maximalpunktregel höhere Spins auswählen. Ihre native Begründung bleibt offen.

**Maximum puncture count at fixed area.** If $A_*=m\,a(1/2)$ and an admissible all-minimal configuration with $m$ punctures exists, the maximum-count fiber is exactly the minimal-spin mask. Without a saturating configuration, maximum count can select higher spins. A native justification remains open.

**Singulettzahl beim Flächengleichstand.** Im gewöhnlichen Tensorproduktmodell haben acht Minimalspinpunkte $14$ unabhängige Singuletts und zwei Spin-$3$-Punkte eines. Bei Gleichgewichtung innerhalb dieser beiden flächengleichen Konfigurationen hat die Minimalbelegung Gewicht $14/15$. Der höhere Spin bleibt zugänglich.

**Singlet count at equal area.** In the ordinary tensor-product model, eight minimal-spin punctures have $14$ independent singlets and two spin-$3$ punctures have one. Equal weighting within these two equal-area configurations gives minimal occupancy weight $14/15$. Higher spin remains accessible.

**Vollständige Flächenfaser im Singulettvergleich.** Bei exakt $4\sqrt3$ sind im additiven Modell nur die drei Belegungen $(n_{1/2},n_3)=(8,0),(4,1),(0,2)$ möglich. Die Mischbelegung kann keinen Gesamtspin null tragen. Daher gilt der Minimalspinanteil $14/15$ für die ganze exakte Flächenfaser unter dem gewählten Tensorprodukt-Zählmaß.

**Complete area fiber in the singlet comparison.** At exact area $4\sqrt3$, the additive model allows only $(n_{1/2},n_3)=(8,0),(4,1),(0,2)$. The mixed configuration cannot have total spin zero. Thus the minimal-spin share $14/15$ holds on the entire exact area fiber under the chosen tensor-product count.

**Minimalspin bei wachsender exakter Fläche.** Bei geradem $N$ kann man vier Minimalspinpunkte durch einen Spin-$3$-Punkt ersetzen, ohne die Fläche zu ändern. Die Singulettzahl einer solchen festen Mischanordnung verhält sich zur reinen Minimalbelegung asymptotisch wie $7/16$. Bei gleicher Gewichtung und Zulassung beider Belegungen bleibt der Minimalspinanteil damit asymptotisch höchstens $16/23$.

**Minimal spin at growing exact area.** For even $N$, replacing four minimal-spin punctures by one spin-$3$ puncture preserves area. The singlet count of one fixed mixed arrangement is asymptotically $7/16$ of the all-minimal count. With equal weighting and both configurations admitted, the minimal-spin share has asymptotic upper bound $16/23$.

**Platzierungsentartung bei gleicher Fläche.** Werden Spinlisten geordnet gezählt, hat ein einzelner Spin-$3$-Punkt in der Mischbelegung $N-3$ mögliche Positionen. Diese Konkurrenten allein drücken den Minimalspinanteil im Vergleichsmodell auf $O(1/N)$. Eine zusätzliche Gewichtung $e^{\chi N}$ müsste für feste Zielgenauigkeit mindestens $\chi\sim(\log N)/3$ erreichen, um diese Familie zu unterdrücken.

**Placement degeneracy at equal area.** With ordered spin lists, the one spin-$3$ puncture in the mixed configuration has $N-3$ possible positions. These competitors alone bound the minimal-spin share by $O(1/N)$ in the comparison model. An extra weight $e^{\chi N}$ needs at least logarithmic growth $\chi\sim(\log N)/3$ at fixed target accuracy to suppress this family.

**Mehrere Spin-3-Ersetzungen.** Bei geordneten Belegungen und $\chi=(\log N)/3+b$ liefern feste Ersetzungszahlen relative Grenzgewichte $\Lambda^m/m!$ mit $\Lambda=(7/16)e^{-3b}$. Diese Belegungen allein geben $\limsup P_{\rm minimal}\le e^{-\Lambda}$. Ein fester Zusatz zur logarithmischen Gewichtung reicht für exakte Konzentration im Grenzwert nicht aus.

**Multiple spin-3 replacements.** With ordered configurations and $\chi=(\log N)/3+b$, fixed replacement counts have limiting relative weights $\Lambda^m/m!$ with $\Lambda=(7/16)e^{-3b}$. These configurations alone give $\limsup P_{\rm minimal}\le e^{-\Lambda}$. A fixed additive correction to logarithmic weighting does not yield full concentration in the limit.

**Schwelle für die gesamte additive Flächenfaser.** Bei exakter Fläche $N a(1/2)$, geordneten Spinlisten und gewöhnlicher Singulettzählung geht der gewichtete Minimalspinanteil genau dann gegen eins, wenn $\chi-(\log N)/3\to+\infty$. Die hinreichende Richtung zählt auch höhere Flächenstufen mit. Eine native Herleitung des Gewichts bleibt offen.

**Threshold for the full additive area fiber.** At exact area $N a(1/2)$ with ordered spin lists and ordinary singlet counting, the weighted minimal-spin share tends to one exactly when $\chi-(\log N)/3\to+\infty$. The sufficient bound includes higher area levels. A native derivation of the weight remains open.

**Grenzwert an der Punktzahlschwelle.** Bei $\chi=(\log N)/3+b$ hat die gesamte additive Flächenfaser im geordneten Singulettmodell den Minimalspin-Grenzanteil $\exp[-(7/16)e^{-3b}]$. Die Anzahl der Spin-$3$-Punkte wird im Grenzwert Poisson-verteilt. Höhere Flächenstufen tragen asymptotisch kein Gewicht.

**Limit at the puncture-count threshold.** At $\chi=(\log N)/3+b$, the entire additive area fiber in the ordered singlet model has limiting minimal-spin share $\exp[-(7/16)e^{-3b}]$. The spin-$3$ count tends to a Poisson law. Higher area levels have vanishing weight.

**Gegenrechnung bei endlicher Fläche.** Eine direkte Zählung nach Fläche und magnetischer Komponente liefert bei kritischer Punktzahlgewichtung und $b=0$ für $N=64,128,256$ die Minimalspinanteile $0{,}73470$, $0{,}69260$, $0{,}66979$. Der analytische Grenzwert ist $0{,}64565$.

**Finite-area cross-check.** Direct counting by area and magnetic component at critical puncture weighting with $b=0$ gives minimal-spin shares $0.73470$, $0.69260$, and $0.66979$ at $N=64,128,256$. The analytic limit is $0.64565$.

**Punktzahlgewicht und Horizontgenerator.** Das Modellgewicht $e^{-\lambda A+\chi N_{\rm Punkte}}$ ändert bei gleicher Fläche die relativen Gewichte verschiedener Punktzahlen. Zugängliche Übergänge zwischen solchen Zuständen würden beim Generator $K_\chi$ eine relative Phase tragen. Bei Zugang nur innerhalb fester Punktzahlsektoren legt der Fluss die Gewichte zwischen Sektoren nicht fest.

**Puncture weighting and horizon generator.** The model weight $e^{-\lambda A+\chi N_{\rm Punkte}}$ changes relative weights at equal area. Accessible transitions between different counts would acquire a relative phase under $K_\chi$. With access only within fixed-count sectors, the flow leaves weights across sectors undetermined.

**OP1-Ausschlusskorridor.** Der nominale T-Zielwert $a_T/a_M\approx0{,}5363$ liegt außerhalb unitärer Wechsel, reiner Spektralauswahl und Kompression auf den positiven M-Sektor. Auf einem gemeinsamen positiven Sektor schließt eine relative Formschranke unter $0{,}4637$ den Zielwert aus. Eine Kompression, die ihn erreicht, braucht mindestens $0{,}4637$ Überlappungsgewicht mit dem ursprünglichen Nullraum.

**OP1 exclusion range.** The nominal T target $a_T/a_M\approx0.5363$ lies outside unitary changes, spectral selection, and compression confined to the positive M sector. On a common positive sector, a relative form bound below $0.4637$ excludes the target. A compression reaching it requires at least $0.4637$ overlap weight with the original null space.

**T-Flächenoperator als Referenzdefinition.** Im additiven Durchstoßpunktmodell liest der M-Operator die Wurzel des Spin-Casimirs aus. Die Maxwell-Dualität aus r07 definiert keine Abbildung des gravitativen Flusses. Ein explizites Produktmodell mit unveränderter Geometrie liefert einen T-Operator mit derselben kleinsten Flächenstufe. Eine nichttriviale gleichförmige Reskalierung der normierten Spinoperatoren erhält ihre Kommutatoren nicht.

**Reference definition of the T area operator.** In the additive puncture model the M operator reads out the square root of the spin Casimir. The Maxwell duality in r07 specifies no map of gravitational flux. An explicit product model with unchanged geometry gives the same minimum area in T. A nontrivial uniform rescaling of normalized spin generators does not preserve their commutators.

**T-Fluss vor der Quantisierung.** Eine gleichförmige Coframe-Skalierung ändert die klassische Fläche desselben Schnitts und ist unter der r10-Annahme gleicher Geometrie ausgeschlossen. Ein kanonischer Koordinatenwechsel erhält die ursprüngliche Flächenauslesung, wenn sie mittransformiert wird. Ein anderes Quantisierungsergebnis braucht eine begründete Änderung der gravitativen Auslesung oder ihrer Randdaten.

**T flux before quantization.** A uniform coframe rescaling changes the classical area of the same section and is excluded under the r10 shared-geometry assumption. A canonical coordinate change preserves the original area readout when it is transformed along with the coordinates. A different quantized result needs a justified change in the gravitational readout or its boundary data.

**Palatini-Randprüfung.** Hält T Coframe, Verbindung und Randbedingungen fest, bleibt der gravitative Palatini-Strom unverändert. Eine reine totale Ableitung verschiebt das lokale Randpotential um eine exakte Feldvariation und ändert den antisymmetrisierten Strom unter denselben Variations- und Eckendaten nicht. Eine andere T-Quantisierung braucht hier zusätzliche Randstruktur.

**Palatini boundary check.** If T keeps the coframe, connection and boundary conditions fixed, the gravitational Palatini current is unchanged. A total derivative adds an exact field variation to the local boundary potential and preserves the antisymmetrized current under the same variation and corner data. A different T quantization needs additional boundary structure here.

**Minimales Randmodell für eine andere Flächenstufe.** Bei einem periodischen Randwinkel, Fluss $P$ und Randterm $kP\dot\theta$ ist die klassische Fläche $|P|$ und die kleinste positive Stufe bei periodischer Quantisierung $\hbar/k$. Ein veränderter symplektischer Koeffizient kann so die Stufe bei gleicher klassischer Auslesung ändern. Der native Koeffizient und die Zuordnung zu Horizontspins bleiben nachzuweisen.

**Minimal boundary model for a different area step.** With a periodic boundary angle, flux $P$, and boundary term $kP\dot\theta$, the classical area is $|P|$ and the smallest positive step under periodic quantization is $\hbar/k$. Changing the symplectic coefficient can thus change the step at fixed classical readout. The native coefficient and identification with horizon spins remain to be derived.

**Randwinkel und Flächenstufe.** Die periodische Randquantisierung liefert $a_{\min}=2\pi\hbar/(kL)$. Eine Winkelumnormierung erhält $kL$. Eine Kreisüberlagerung vom Grad $d$ gibt bei voller Quantisierung die Stufe $a_M/d$, bei ausschließlich zurückgezogenen M-Zuständen wieder $a_M$. Der nominale r10-Faktor ist kein ganzzahliger Grad.

**Boundary angle and area step.** Periodic boundary quantization gives $a_{\min}=2\pi\hbar/(kL)$. Rescaling the angle preserves $kL$. A degree-$d$ cover gives the step $a_M/d$ on the full quantization and $a_M$ on pulled-back M states only. The nominal r10 factor is not an integer degree.

**Randphase und Flächenlücke.** Bei festem $k$, vollständigem Winkelimpulsspektrum und Fläche $|P|$ liefert eine Randphase $\alpha$ die Stufe $a_T/a_M=\min(\alpha,1-\alpha)$ für $0<\alpha<1$. Die periodische Wahl liefert $1$. Der nominale r10-Wert $0{,}5363$ liegt außerhalb dieses Korridors.

**Boundary phase and area gap.** At fixed $k$, with the full angular momentum spectrum and area $|P|$, a boundary phase $\alpha$ gives $a_T/a_M=\min(\alpha,1-\alpha)$ for $0<\alpha<1$. Periodic quantization gives $1$. The nominal r10 value $0.5363$ lies outside this range.

**Flussumkehr und Randphase.** Die kanonische Umkehr $(\theta,P)\mapsto(-\theta,-P)$ sendet die Randphase $\alpha$ auf $-\alpha$ modulo eins. Gepaarte Profile haben dasselbe Betragsflächenspektrum. Innerhalb eines Profils sind nur die Phasen $0$ und $1/2$ fest.

**Flux reversal and boundary phase.** Canonical reversal $(\theta,P)\mapsto(-\theta,-P)$ sends phase $\alpha$ to $-\alpha$ modulo one. Paired profiles have the same absolute area spectrum. Only phases $0$ and $1/2$ are fixed within a single profile.

**Kanonischer Wechsel auf dem Randzylinder.** Eine glatte invertierbare Abbildung mit $|P_T|=|P|$ und gleichen Winkelperioden kann die Symplektik $k\,dP\wedge d\theta$ nur bei $k_T=k_M$ transportieren. Die Winkelabbildung muss auf jeder Flussfaser Grad $\pm1$ haben. Flussabhängige Winkelverschiebungen ändern die Stufe bei periodischer Quantisierung nicht.

**Canonical change on the boundary cylinder.** A smooth invertible map with $|P_T|=|P|$ and equal angle periods can transport $k\,dP\wedge d\theta$ only when $k_T=k_M$. The angle map must have degree $\pm1$ on each flux fiber. Flux-dependent angle shifts do not change the step under periodic quantization.

**Zwei Randkanäle.** Bei fester Gesamtfläche $|P_1|+|P_2|=|P|$ und Flussanteil $w$ ergibt eine Reduktion mit Winkelwindungen $(2,1)$ den symplektischen Faktor $1+w$. Bei anschließender periodischer Quantisierung liegt $a_T/a_M$ in $[1/2,1]$. Der r10-Wert liegt darin, erfordert aber eine unabhängig bestimmte Flussaufteilung und eine Begründung der Quantisierungsreihenfolge.

**Two boundary channels.** With fixed total area $|P_1|+|P_2|=|P|$ and flux share $w$, reduction with angle windings $(2,1)$ gives symplectic factor $1+w$. Subsequent periodic quantization gives $a_T/a_M$ in $[1/2,1]$. The r10 target lies in this range, but requires an independently determined split and justification of the quantization order.

**Quantisierungsreihenfolge der Randkanäle.** Bei getrennt quantisierten Kanälen und exakt ausgewähltem Flussanteil $w=p/q$ ist die kleinste positive Gesamtfläche $q a_M$. Irrationales $w$ lässt nur den Nullwert zu. Die Winkelbindung und die Flussbindung haben eine von null verschiedene Poisson-Klammer. Eine kleinere Stufe im Modell beruht auf der gekoppelten Reduktion vor der Quantisierung.

**Order of boundary-channel quantization.** Separate channel quantization followed by exact selection of flux share $w=p/q$ gives minimum positive total area $q a_M$. Irrational $w$ leaves only zero. The angle and flux constraints have a nonzero Poisson bracket. A smaller step in the model relies on coupled reduction before quantization.

**Variationsregel der Randaufteilung.** Die Minimierung einer positiven quadratischen Randenergie bei festem Gesamtfluss ergibt $w=c_2/(c_1+c_2)$. Für die deklarierte Winkelbindung $(2,1)$ liefert gleiche Steifigkeit den Flächenquotienten $2/3$. Der nominale r10-Faktor würde ein unabhängig hergeleitetes Steifigkeitsverhältnis von etwa $6{,}39$ verlangen.

**Variational flux split.** Minimizing a positive quadratic boundary energy at fixed total flux gives $w=c_2/(c_1+c_2)$. For the declared $(2,1)$ angle constraint, equal stiffness gives area ratio $2/3$. The nominal r10 factor would require an independently derived stiffness ratio of about $6.39$.

**Dynamische Bindung der Randwinkel.** Ein Potential mit Minimum bei $\theta_1-2\theta_2=0$ hält diese Winkelbindung nur bei $c_1P_1=2c_2P_2$ dauerhaft fest. Der zugehörige erhaltene Impuls ist $2P_1+P_2$. Für gleiche Steifigkeiten liefert die Reduktion die Flächenstufe $3/5$ relativ zu M.

**Dynamical locking of boundary angles.** A potential minimized at $\theta_1-2\theta_2=0$ preserves locking when $c_1P_1=2c_2P_2$. The associated conserved momentum is $2P_1+P_2$. Equal stiffness then gives area-step ratio $3/5$ after reduction.

**Flächenmessung im voll quantisierten Zweikanalmodell.** Die Winkelbindung mischt Flussbelegungen bei festem Gesamtimpulsindex $n=2m_1+m_2$. Die ursprüngliche Fläche liefert weiterhin ganzzahlige Vielfache von $a_M$, im Sektor $n=1$ mindestens $a_M$. Der reduzierte Wert $3a_M/5$ erfordert daher eine eigene Flächenauslesung.

**Area measurement in the fully quantized two-channel model.** Angle locking mixes flux configurations at fixed total momentum index $n=2m_1+m_2$. The original area still gives integer multiples of $a_M$, at least $a_M$ in sector $n=1$. The reduced value $3a_M/5$ therefore requires a distinct area readout.

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

**Gemischte Auslesung im Zweikanal-Randmodell.** Für ein nichtkonstantes Potential der relativen Phase erzwingt Erhaltung im linearen orientierten Aggregat das Verhältnis $2:1$. Kalibriert man den Betrag dieses Aggregats auf die klassische Fläche der gebundenen Teilfläche, ist der quantisierte Ausgang im Sektor $n$ genau $a_M|n|(c_1+2c_2)/(c_1+4c_2)$. Bei gleichen Steifigkeiten ergibt sich im ersten positiven Sektor $3a_M/5$. Die native T-Auslesung und das für den nominalen Zielwert erforderliche Steifigkeitsverhältnis bleiben offen.

**Mixed readout in the two-channel boundary model.** A nonconstant relative-phase potential forces the ratio $2:1$ in a conserved linear aggregate of the oriented fluxes. Calibrating its absolute value against the classical area on the locked submanifold gives the quantized outcome $a_M|n|(c_1+2c_2)/(c_1+4c_2)$ in sector $n$. Equal stiffnesses give $3a_M/5$ in the first positive sector. The native T readout and the stiffness ratio needed for the nominal target remain open.

**Qiskit-Erkundung.** Ein Qubit kodiert zwei benachbarte Fouriermoden im Sektor $n=1$. Für eine gleichgewichtete Überlagerung liefert die additive Auslesung $a_M$ und $2a_M$ mit je $1/2$, die gemischte Auslesung $3a_M/5$ mit Wahrscheinlichkeit eins. Das sind die analytischen Sollwerte für die Schaltung in `notes/research/qam_hc_area_qiskit.py`.

**Qiskit exploration.** One qubit encodes two adjacent Fourier modes in sector $n=1$. For an equal-weight superposition, the additive readout gives $a_M$ and $2a_M$ with probability $1/2$ each. The mixed readout gives $3a_M/5$ with probability one. These are the analytic expected values for the circuit in `notes/research/qam_hc_area_qiskit.py`.

**Qiskit-Simulator für QAM-Modelle.** Das optionale Modul `qam.simulation` kodiert endliche Zustandsräume mit expliziten Frame- und Basislabels. Schaltungen entwickeln den Zustand oder beschreiben einen vorgeschlagenen Frameübergang mit deklarierter Zielbasis. Diagonale Auslesungen gruppieren die Basiswahrscheinlichkeiten nach Messwert. Das Flächenbeispiel vergleicht additive und gemischte Auslesung auf demselben Zustand.

**Qiskit simulator for QAM models.** The optional `qam.simulation` module encodes finite state spaces with explicit frame and basis labels. Circuits evolve a state or represent a proposed frame transition with a declared target basis. Diagonal readouts group basis probabilities by measurement outcome. The area example compares additive and mixed readouts on the same state.

**Informationsbedarf der gemischten Flächenauslesung.** Zwei Moden mit gleicher additiver Fläche können verschiedene Werte von $|2m_1+m_2|$ haben. Auf der additiven Faser $s=|m_1|+|m_2|$ erfordert exakte klassische Dekodierung deshalb mindestens $s+1$ Zusatzsymbole. Der Betrag des erhaltenen Flusses ist selbst ein hinreichendes Ausleselabel.

**Information required by the mixed area readout.** Modes with the same additive area can have different values of $|2m_1+m_2|$. On the additive fiber $s=|m_1|+|m_2|$, exact classical decoding therefore requires at least $s+1$ auxiliary symbols. The magnitude of the conserved flux is itself a sufficient readout label.

**Qiskit-Flusszeiger.** Auf der additiven Faser $s=1$ schreibt ein CNOT das Sektorlabel $n-1$ auf ein Zeigerqubit. Beide Moden liefern dieselbe additive Fläche, aber verschiedene scharfe Zeigerwerte. Die Simulation reproduziert auch die vollständige Korrelation in der gleichgewichteten Überlagerung.

**Qiskit flux pointer.** On the additive fiber $s=1$, a CNOT writes the sector label $n-1$ to a pointer qubit. Both modes give the same additive area and distinct sharp pointer values. The simulation also reproduces their perfect correlation in an equal-weight superposition.

**Betragszeiger und Kohärenz.** Im Ausschnitt $|n|=1$ liefert der Qiskit-Betragszeiger denselben Flächenwert mit oder ohne zusätzlichen Vorzeichenrekord. Ein Hadamard-Rückweg trennt die Fälle: Ohne Vorzeichenrekord ist das Interferenzbit sicher null, mit ihm gleichverteilt.

**Magnitude pointer and coherence.** In the $|n|=1$ truncation, the Qiskit magnitude pointer gives the same area with or without a sign record. A Hadamard return distinguishes the cases: The interference bit is certainly zero without the sign record and uniformly distributed with it.

**Zugang zur Vorzeichenphase.** Operationen, die den Randfluss $n$ erhalten, können die Phase zwischen $+n$ und $-n$ allein am Rand nicht auslesen. Ein Referenzkanal könnte die Phase im festen Gesamtflusssektor sichtbar machen, sofern eine Kopplung zwei Flusseinheiten zwischen Rand und Referenz austauschen darf.

**Access to the sign phase.** Operations conserving the boundary flux $n$ cannot read the phase between $+n$ and $-n$ on the boundary alone. A reference channel could reveal that phase in a fixed total flux sector if an admissible coupling exchanges two units of flux between the boundary and the reference.

**Relationaler Kompensatorport.** Die phasensensitive Portstruktur aus r30 liefert ein Modell für einen gemeinsamen Rand-Referenz-Port. Ein einzelner Port ergibt im festen Gesamtflusssektor null stets Wahrscheinlichkeit $1/2$. Der gemeinsame Austauschport unterscheidet dort symmetrische und antisymmetrische Überlagerungen. Die native Zuordnung der Doublets und die Zulassung des gemeinsamen Ports bleiben offen.

**Relational compensator port.** The phase-sensitive port structure from r30 provides a model for a joint boundary-reference port. A single port gives probability $1/2$ in the zero-total-flux sector. The joint exchange port distinguishes symmetric and antisymmetric superpositions there. The native identification of the doublets and admissibility of the joint port remain open.

**Austauschanteil in r27.** Bei versuchsweiser Zuordnung der r27-Z-Achse zum Flussvorzeichen enthält die vorhandene Zweikopien-Observable im Gesamtflusssektor null den gesuchten Austausch. Eine gemeinsame Phasenmittelung entfernt die gesamtflussändernden Terme auf dem vollen Doubletprodukt. Die native Achsenzuordnung und eine kohärente Präparation des Gesamtsektors bleiben zu begründen.

**Exchange component in r27.** If the r27 Z axis is identified with the flux sign, the existing two-copy observable contains the required exchange in the zero-total-flux sector. A common phase average removes the total-flux-changing terms on the full doublet product. The native axis identification and coherent preparation of the total sector remain open.

**Kohärente Gesamtflussauswahl im Modell.** Ein gemeinsames Paritätsbit wählt den Nullsektor mit Wahrscheinlichkeit $1/2$ aus und erhält dort die Austauschinterferenz. Werden auch die lokalen Vorzeichen gespeichert, sinkt die bedingte Wahrscheinlichkeit des positiven Austauschports von eins auf $1/2$. Die Simulation setzt die Zuordnung von Vorzeichendoublets und Randfluss voraus.

**Coherent total-flux selection in the model.** A shared parity bit selects the zero sector with probability $1/2$ and preserves exchange interference there. Recording the local signs as well lowers the conditional probability of the positive exchange port from one to $1/2$. The simulation assumes the identification of sign doublets with boundary flux.

**Orbit-Parität und Gesamtfluss.** Auf den zwei Vorzeichendoublets wählt der gerade Orbit-Projektor für den Modellindex $j=(n+r)/2$ genau den Nullsektor aus. Beide gegenläufigen Zustände benötigen getrennte interne Labels, die der Zeiger gemeinsam behandelt. Auf einem größeren Flussbereich erfasst dieselbe Parität auch Gesamtflüsse $\pm4,\pm8,\ldots$. Die native Indexzuordnung bleibt offen.

**Orbit parity and total flux.** On two sign doublets, the even orbit projector with model index $j=(n+r)/2$ selects exactly the zero sector. The opposing-sign states require distinct internal labels that the pointer treats identically. On a larger flux range, the same parity also selects total fluxes $\pm4,\pm8,\ldots$. The native index identification remains open.

**Gemeinsamer Phasenzeiger.** Ein Zeiger für $j\bmod L$ verallgemeinert die Orbit-Parität auf dem Modellindex $j=(n+r)/2$. Bei $|j|<L$ wählt der Zeigerausgang null genau den Gesamtfluss null und erhält die Kohärenz innerhalb dieses Sektors. Auf dem unbeschränkten Gitter bleiben Mehrdeutigkeiten für jedes feste $L$.

**Common phase pointer.** A pointer for $j\bmod L$ generalizes orbit parity on the model index $j=(n+r)/2$. For $|j|<L$, pointer outcome zero selects precisely zero total flux and preserves coherence within that sector. On the unbounded lattice, aliases remain for every fixed $L$.

**Grenze von Orbit-Shift und Parität.** Beide Operationen kommutieren mit dem Zweiershift. Ein daraus gebauter gemeinsamer Zeiger gibt bei den Orbit-Indizes null und zwei dieselbe Ausgangsstatistik. Ein Modulo-Zeiger mit $L>2$ braucht eine zusätzliche Operation, etwa eine Diagonalphase des Gesamtflusses.

**Limit of orbit shift and parity.** Both operations commute with the double shift. A common pointer built from them has the same output statistics at orbit indices zero and two. A modulo pointer with $L>2$ requires another operation, such as a diagonal phase of total flux.

**Relationaler Orbit-Vergleich.** Ein gemeinsamer Gleichheitszeiger wäre unter gleichzeitiger Translation invariant. Mit scharfem Referenzindex null wählt er den Systemindex null aus. Bei unscharfer Referenz ist die Akzeptanz bei Index $j$ gleich dem Referenzgewicht $p_j$. Die getrennten Shift- und Paritätsoperationen liefern den Gleichheitsvergleich allein nicht.

**Relational orbit comparison.** A joint equality pointer would be invariant under simultaneous translation. A sharp reference at index zero selects system index zero. With an uncertain reference, acceptance at index $j$ equals its reference weight $p_j$. The separate shift and parity operations alone do not supply the equality comparison.

**Gleichheitszeiger aus kontrollierten Shifts.** Zwei kohärent kontrollierte Orbit-Shifts berechnen die Differenz von System- und Referenzindex in einem Arbeitsregister. Nach einem binären Nulltest löschen die inversen Shifts die Differenz wieder. Der Zeiger speichert nur Gleichheit. Der Aufbau setzt kontrollierte Shift-Potenzen und einen Nulltest voraus.

**Equality pointer from controlled shifts.** Two coherently controlled orbit shifts compute the difference of the system and reference indices in a work register. After a binary zero test, the inverse shifts erase that difference. The pointer retains only equality. This construction requires controlled shift powers and a zero test.

**Orbit-Vergleich über Referenzkopien.** Ein symmetrischer Projektor auf dem Systemindex und $k$ scharfen Referenzkopien akzeptiert gleiche Indizes sicher und verschiedene mit Wahrscheinlichkeit $1/(k+1)$. Bei endlichem $k$ liefert er einen näherungsweisen Vergleich. Die interne Flussaufteilung muss für den Kohärenzerhalt von der Registerpermutation getrennt bleiben.

**Orbit comparison using reference copies.** A symmetric projector on the system index and $k$ sharp reference copies accepts equal indices with certainty and different ones with probability $1/(k+1)$. At finite $k$ this gives an approximate comparison. To preserve coherence, the internal flux allocation must be kept separate from register permutations.

**Grenze des basisunabhängigen Kopienvergleichs.** Sichere Akzeptanz gleicher Zustände in jeder Indexbasis erzwingt Akzeptanz des gesamten symmetrischen Unterraums. Für einen orthogonalen Systemzustand und $k$ identische Referenzkopien ist die Falschakzeptanz deshalb mindestens $1/(k+1)$. Der Symmetrieprojektor erreicht diese Schranke.

**Limit of basis-independent copy comparison.** Certain acceptance of equal states in every index basis forces acceptance of the full symmetric subspace. For an orthogonal system state and $k$ identical reference copies the false acceptance probability is therefore at least $1/(k+1)$. The symmetric projector attains this bound.

**Relativer Shift und Indexphase.** Die Spektralstatistik des relativen Shifts ist für alle Index-Basispaare gleichverteilt und erkennt Gleichheit nicht. Das Produkt entgegengesetzter diagonaler Indexphasen trägt dagegen den Indexunterschied als Eigenphase. Sein Eins-Sektor ist auf dem zyklischen Orbit der Gleichheitssektor.

**Relative shift and index phase.** The spectral statistics of the relative shift are uniform for every index basis pair and cannot detect equality. Opposite diagonal index phases instead encode the index difference as an eigenphase. Their unit-eigenvalue sector is the equality sector on the cyclic orbit.

**r11-Stufenphase und Orbit-Zeiger.** Ein unitäres Shift-Phase-Paar mit Phasenschritt $30^\circ$ verlangt mindestens zwölf orthogonale Indexsektoren. Die r11-Bloch-Doublet-Darstellung kann das allein nicht realisieren. Eine Anwendung als gemeinsamer Randflusszeiger benötigt einen separaten Indexträger und eine begründete Kopplung.

**r11 stage phase and orbit pointer.** A unitary shift-phase pair with a $30^\circ$ phase step requires at least twelve orthogonal index sectors. The r11 Bloch doublet alone cannot realize it. A joint boundary-flux pointer needs a separate index carrier and a justified coupling.

**Zusammengesetzter Zwölferindex.** Diagonale Charaktere modulo drei und vier auf demselben Indexträger ergeben gemeinsam einen Charakter modulo zwölf. Der Modellträger kann als Produkt eines Dreier- und Viererregisters organisiert werden. Der endgültige Nullzeiger bleibt binär. Die native Zuordnung beider Phasen zum selben Randindex ist offen.

**Composite twelve-sector index.** Diagonal characters modulo three and four on the same index carrier combine into a character modulo twelve. The model carrier can use a product of three- and four-state registers. The final zero pointer remains binary. The native identification of both phases with the same boundary index is open.

**r11-Rotation als Kanal oder kontrollierte Phase.** Die $30^\circ$-Rotationen nach $j$ und $j+6$ Schritten unterscheiden sich durch ein globales Minuszeichen und geben denselben Rotationskanal. Ein kohärent kontrollierter Zugriff könnte dieses Zeichen als Zeigerphase sichtbar machen. Dafür müsste der gemeinsame Randindex die Rotationspotenz steuern.

**r11 rotation as a channel or a controlled phase.** The $30^\circ$ rotations after $j$ and $j+6$ steps differ by a global minus sign and give the same rotation channel. Coherent control could reveal this sign as a pointer phase. This requires the joint boundary index to control the rotation power.

**Gemeinsamer Zeiger mit lokalen Kopplungen.** Zwei gleich starke kontrollierte Phasen am selben Zeiger addieren sich zur Phase des Gesamtflusses. Bei einer Abweichung $\delta$ der beiden Kopplungswinkel sinkt nach Ignorieren des Zeigers die Vorzeichenkohärenz im Nullsektor um den Faktor $|\cos\delta|$.

**Common pointer with local couplings.** Two equally strong controlled phases on the same pointer add to the total-flux phase. If the two coupling angles differ by $\delta$, discarding the pointer reduces the zero-sector sign coherence by a factor of $|\cos\delta|$.

**Qiskit-Abgleich der lokalen Pulse.** Die Zweizustandskodierung trennt $j=0$ und $j=6$ bei gleichen Pulsen sicher. Im Nullsektor ergibt der feste Interferenzport bei Winkeldifferenz $\delta$ die Wahrscheinlichkeit $(1+\cos^2\delta)/2$. Die phasenoptimierte Sichtbarkeit beträgt $|\cos\delta|$.

**Qiskit check of the local pulses.** The two-state encoding separates $j=0$ and $j=6$ with certainty for equal pulses. In the zero sector the fixed interference port has probability $(1+\cos^2\delta)/2$ at angle mismatch $\delta$. Phase-optimized visibility is $|\cos\delta|$.

**Qiskit-Zwölferzeiger.** Ein Zeiger mit zwölf besetzten Basisstufen akzeptiert in der Simulation genau den Rest null modulo zwölf. Die Flussbelegungen sind feste Schaltungsparameter.

**Qiskit modulo-12 pointer.** A pointer with twelve populated basis levels accepts exactly residue zero modulo twelve in the simulation. Flux configurations are fixed circuit parameters.

**Kohärenter Qiskit-Zwölferzeiger.** Zwei Flussqubits steuern die lokalen Phasen. Die Rückrechnung löscht den Arbeitszeiger und lässt das binäre Nullbit zurück. Der akzeptierte Zweig zeigt die volle Austauschinterferenz für die beiden gegenläufigen Flusspaare.

**Coherent Qiskit modulo-12 pointer.** Two flux qubits control the local phases. Uncomputation resets the work pointer and retains the binary zero bit. The accepted branch exhibits full exchange interference for the opposing flux pairs.

**Flussphase aus quadratischer Drift.** Ein kontrollierter Shift mit quadratischer Drift, Rückshift und Gegenevolution erzeugt eine lineare Flussphase. Der lokale Shift benötigt während des Pulses einen Ausgleich, falls Gesamtflusserhaltung für jeden Zwischenschritt gilt. Der direkte flusserhaltende Austausch erzeugt bei gleichen quadratischen Driften eine Differenzphase.

**Flux phase from quadratic drift.** A controlled shift, quadratic drift, reverse shift and reverse evolution generate a linear flux phase. A local shift needs compensation if total flux must be conserved at each step. Direct flux-conserving exchange with equal quadratic drifts generates a difference phase.

**Flusserhaltender Pufferzeiger.** Ein Puffer kann gleichzeitig je eine Flusseinheit an Rand und Referenz abgeben. Bei gleichen quadratischen Driftkoeffizienten und scharfem Pufferfluss ergibt der Rückshift mit Gegenevolution eine Phase des gemeinsamen Rand-Referenz-Flusses. Der Gesamtfluss aller drei Kanäle bleibt auch in den Zwischenschritten erhalten.

**Flux-conserving buffer pointer.** A buffer can transfer one flux unit each to the boundary and reference. With equal quadratic drift coefficients and a sharp buffer flux, reverse transfer and reverse evolution yield a phase of the joint boundary-reference flux. Total flux across the three channels is conserved throughout.

**Pufferzeiger mit Vorwärtsdrift.** Driftet der verschobene und der unverschobene Zeigerzweig gleich lange, liefert ihre relative Phase den Summenzeiger ohne inverse Drift. Die gemeinsame Drift bleibt auf dem Flussregister und ist für die beiden gegenläufigen Paare bei gleichen Koeffizienten global.

**Buffer pointer with forward evolution.** Equal forward drift times in the shifted and unshifted pointer branches supply the sum phase without inverse drift. The common drift remains on the flux register and is global for the two opposing pairs at equal coefficients.

**Grenze des Zweikanal-Transfers.** Bei einer festen positiv semidefiniten quadratischen Drift kann ein gesamtflusserhaltender Transfer keinen reinen linearen Summengenerator liefern. Das gilt auch mit Kreuzterm. Umschaltbare Driften oder diskrete Phasenübereinstimmungen liegen außerhalb des Ausschlusses.

**Limit of two-channel transfer.** With a fixed positive semidefinite quadratic drift, a total-flux-conserving transfer cannot produce a nonzero linear sum generator. This includes cross terms. Switchable drifts and discrete phase coincidences are outside the exclusion.

**Summenzeiger mit umschaltbarer Drift.** Zwei positive quadratische Driften mit vertauschten Kanalgewichten und entgegengesetzten kontrollierten Transfers ergeben gemeinsam eine Phase proportional zu $(a-b)(n+r)$. Der Gesamtfluss bleibt in jedem Schritt erhalten. Ein kohärenter Registertausch könnte die umgeschaltete Drift realisieren, sofern er nativ zugelassen ist.

**Sum pointer with switchable drift.** Two positive quadratic drifts with swapped channel weights and opposite controlled transfers yield a phase proportional to $(a-b)(n+r)$. Total flux is conserved at each step. A coherent register swap could implement the switched drift if it is natively admissible.

**Diskrete Summenphase bei fester Drift.** Auf dem ganzzahligen Gitter wird der Referenzterm bei $t(a+b)\in\pi\mathbb Z$ zu einer vollen Phase. Ein einzelner kontrollierter Hin- und Rücktransfer erzeugt dann eine Zeigerphase der Summe. Das gewählte Modellverhältnis $a:b=1:23$ liefert auf dem geraden Gesamtflussgitter einen Charakter modulo zwölf.

**Discrete sum phase with fixed drift.** On the integer lattice, the reference term wraps to a full phase at $t(a+b)\in\pi\mathbb Z$. A single controlled transfer and its reversal then yield a sum-dependent pointer phase. The model ratio $a:b=1:23$ gives a modulo-twelve character on the even total-flux lattice.

**Maximaler Modulus der Driftresonanz.** Für das gekürzte Verhältnis $a:b=u:v$ unterscheidet die Resonanz auf dem geraden Gesamtflussgitter höchstens modulo $(u+v)/\gcd(2,u+v)$. Symmetrische Drift liefert dort kein Signal. Bei irrationalem Verhältnis kommen Nichtnull-Indizes der Nullphase beliebig nahe; endlich viele feste Resonanzabfragen geben auf dem unbeschränkten Gitter keine exakte Nullselektion.

**Maximum modulus of drift resonance.** For the reduced ratio $a:b=u:v$, resonance on the even total-flux lattice distinguishes at most modulo $(u+v)/\gcd(2,u+v)$. Symmetric drift gives no signal there. At an irrational ratio nonzero indices approach the zero phase arbitrarily closely; finitely many fixed resonance queries cannot select zero exactly on the unbounded lattice.

**Sektordrift und relative Winkelmode.** Die ursprüngliche Winkelbindung liefert nach klassischer Minimierung eine quadratische Sektordrift. Zwei identische reduzierte Kopien erzeugen damit auf dem geraden Gesamtflussgitter kein Resonanzsignal. In der vollen Quantisierung bleibt zusätzlich eine sektorabhängige Verschiebung des relativen Fourierimpulses. Bei gleichen Steifigkeiten führt erst ein Sektorschritt um fünf diese Verschiebung durch einen ganzzahligen Fourier-Shift exakt mit.

**Sector drift and relative angle mode.** The original angle locking yields a quadratic sector drift after classical minimization. Two identical reduced copies give no resonance signal on the even total-flux lattice. Full quantization retains a sector-dependent shift of relative Fourier momentum. At equal stiffnesses a five-sector step is the smallest positive step that can carry this shift exactly by an integer Fourier translation.

**Winkelharmonische des Fünfertransfers.** Bei gleichen Steifigkeiten entspricht der exakte Sektorschritt um fünf der Windung $(2,1)$ in den ursprünglichen Randwinkeln. Die entgegengesetzte Windung einer Referenzkopie erhält den Gesamtfluss und führt die relative Winkelmode mit. Das vorhandene Bindungspotential erzeugt diese kopienübergreifende Harmonische nicht.

**Angular harmonic of the five-unit transfer.** At equal stiffnesses the exact five-sector step corresponds to winding $(2,1)$ in the original boundary angles. The opposite winding on a reference copy conserves total flux and carries along the relative angle mode. The existing locking potential does not generate this cross-copy harmonic.

**Gerichteter Transfer mit Hilfsdoublet.** Ein hermitescher Austausch koppelt den Fünfer-Hintransfer an den Flip des Hilfsdoublets und den Rücktransfer an den inversen Flip. Bei isoliertem Puls erzeugt dies eine gerichtete Verschiebung und setzt das Doublet nach dem zweiten Puls zurück. Die native Kopplung und die Pulskontrolle bleiben offen.

**Directed transfer with an auxiliary doublet.** A Hermitian exchange ties the forward five-unit transfer to an auxiliary flip and the reverse transfer to the inverse flip. An isolated pulse gives a directed shift, and the second pulse resets the doublet. Native coupling and pulse control remain open.

**Grenze des konstanten Transferpulses.** Bei gleichzeitig laufender quadratischer Drift haben die beiden gegenläufigen Flusspaare verschiedene Verstimmungen. Ein gemeinsamer Rechteckpuls kann deshalb bei endlicher Kopplung nicht beide vollständig übertragen. Die optimale gemeinsame Transferwahrscheinlichkeit bei mittiger Abstimmung ist $g^2/[g^2+q^2(a+b)^2]$.

**Limit of the constant transfer pulse.** With quadratic drift active, the two opposing flux pairs have different detunings. A common rectangular pulse at finite coupling cannot transfer both completely. At midpoint tuning, the optimal common transfer probability is $g^2/[g^2+q^2(a+b)^2]$.

**Doppelpuls bei laufender Drift.** Für die mittig abgestimmten Verstimmungen $\pm2d$ bewirken zwei gleich lange Pulse mit Kopplungen $+d,-d$ exakten Transfer in beiden Nullsektorblöcken. Die zentrierten Flip-Vorzeichen heben sich beim Rückweg bis auf eine gemeinsame Phase auf. Die mittleren Blockenergien bleiben in der Zeigerbilanz zu berücksichtigen.

**Double pulse with active drift.** For midpoint detunings $\pm2d$, equal-duration pulses with couplings $+d,-d$ give exact transfer in both zero-sector blocks. The centered flip signs cancel on return up to a common phase. The mean block energies still enter the pointer phase balance.

**Phasenabgleich des Doppelpulses.** Die mittleren Blockenergien verlängern die effektive Wartezeit um zwei Einzelpulsdauern. Bei $T=\pi(1-1/\sqrt2)/d$ stimmen die Zeigerphasen der beiden gegenläufigen Paare nach dem vollständigen Rückweg überein.

**Double-pulse phase matching.** The mean block energies extend the effective wait by two single-pulse durations. At $T=\pi(1-1/\sqrt2)/d$, the two opposing flux pairs give identical pointer phases after the full return.

**Nullselektion mit symmetrischer Drift.** Auf den vier Vorzeichenpaaren selektiert der Doppelpuls bei gleichen Driftgewichten den Nullsektor exakt. Die gegenläufigen Paare geben Zeigerphase minus eins, die gleichgerichteten plus eins. Beim Modellverhältnis $1:23$ akzeptiert dieselbe Nullsektor-Abstimmung gleichgerichtete Paare dagegen zu rund 93 Prozent.

**Zero selection with symmetric drift.** On the four sign pairs the double pulse with equal drift weights selects the zero sector exactly. Opposing pairs give pointer phase minus one and aligned pairs plus one. At model ratio $1:23$, the same zero-sector tuning instead accepts aligned pairs about 93 percent of the time.

**Verstimmungskollision auf dem Flussgitter.** Bei symmetrischer Drift haben $(1,-1)$ und $(2,0)$ denselben Transferblock. Der Doppelpuls akzeptiert daher beide sicher. Auch ein geformter Puls im selben Blockmodell kann diese Kollision nicht auflösen. Auf begrenzten Gittern sind disjunkte Verstimmungsmengen eine notwendige Voraussetzung für exakte Nullselektion.

**Detuning collision on the flux lattice.** With symmetric drift, $(1,-1)$ and $(2,0)$ have the same transfer block, so the double pulse accepts both with certainty. Pulse shaping within the same block model cannot resolve this collision. On bounded lattices, disjoint detuning sets are necessary for exact zero selection.

**Selektive Pulssteuerung auf endlichem Flussgitter.** Bei getrennten Verstimmungen und zwei unabhängigen Kopplungsquadraturen isoliert die erzeugte Lie-Algebra die einzelnen Transferblöcke. Das eröffnet im idealen reversiblen Kontrollmodell eine selektive Auslesung. Die native Verfügbarkeit der Quadraturen und der vollständigen Rückrechnung bleibt offen.

**Selective pulse control on a finite flux lattice.** With distinct detunings and two independent coupling quadratures, the generated Lie algebra isolates the individual transfer blocks. This permits selective readout in the ideal reversible control model. Native availability of both quadratures and full uncomputation remains open.

**Qiskit-Selektor für fünf Flusspaare.** Der kodierte Modulo-8-Vergleich markiert die Verstimmungslabels $\pm3$ gemeinsam und weist die drei anderen Modellpaare sicher ab. Die Rückrechnung erhält die relative Phase im ausgewählten Zweig. Der Zugriff auf das Verstimmungslabel wird vorausgesetzt.

**Qiskit selector for five flux pairs.** The encoded modulo-eight comparison marks detuning labels $\pm3$ together and rejects the three other model pairs with certainty. Uncomputation preserves the relative phase in the selected branch. Access to the detuning label is assumed.

**Numerische selektive Pulsfolge.** Eine gemeinsame Folge aus 16 Abschnitten dreht im Transfermodell die Verstimmungsblöcke $\pm3$ um und lässt das Hilfsbit in den Blöcken $-1,1,2$ bei null, jeweils bis auf numerische Genauigkeit. Die Verstimmung wirkt als Drift. Die kohärente Rückrechnung und die native Pulskontrolle bleiben offen.

**Numerical selective pulse sequence.** A common 16-segment sequence flips the auxiliary bit in detuning blocks $\pm3$ and leaves it at zero in blocks $-1,1,2$ to numerical precision. Detuning acts through the drift. Coherent uncomputation and native pulse control remain open.

**Rückrechnung und Verstimmungsfehler.** Der vollständige berechnete Pulszeiger erreicht auf fünf Sollblöcken einen maximalen Zustandsvektorfehler von rund $1{,}1\cdot10^{-14}$. Ein gemeinsamer Verstimmungsoffset $0{,}05$ erhöht die maximale Fehlklassifikation auf rund $8{,}6$ Prozent. Die Simulation setzt jeweils den exakt inversen Propagator voraus.

**Uncomputation and detuning errors.** The calculated full pulse pointer has a maximum state-vector error of about $1.1\cdot10^{-14}$ on five target blocks. A common detuning offset of $0.05$ raises the maximum misclassification probability to about $8.6$ percent. The simulation assumes an exactly inverted propagator in each case.

**Robustere selektive Pulsfolge.** Eine auf drei Verstimmungsoffsets optimierte 24-Abschnittsfolge erreicht auf 98 zusätzlichen Zwischenwerten eine maximale numerische Fehlklassifikation von rund $1{,}68\cdot10^{-6}$. Die frühere 16-Abschnittsfolge erreicht dort rund $0{,}0824$. Die Aussage gilt für das gesampelte Gitter.

**More robust selective pulse sequence.** A 24-segment sequence optimized at three detuning offsets reaches a maximum numerical misclassification of about $1.68\cdot10^{-6}$ at 98 additional intermediate points. The earlier 16-segment sequence gives about $0.0824$ there. The result applies to the sampled grid.

**Intervallschranke für den Pulsfehler.** Die Krümmung der Fehlamplitude ist bei statischem Offset durch $T^2$ begrenzt. Analytische Interpolation mit numerischen Stützstellen ergibt über das ganze Modellintervall eine Fehlerschranke von rund $1{,}727\cdot10^{-6}$. Die Stützstellen sind nicht intervallzertifiziert.

**Interval bound on pulse error.** The curvature of the error amplitude under a static offset is bounded by $T^2$. Analytic interpolation with numerical grid values gives an error bound of about $1.727\cdot10^{-6}$ over the model interval. The grid values are not interval-certified.

**Intervallabgleich der Pulsfolge.** Alle 505 Stützstellenamplituden der fixierten 24-Abschnittsfolge wurden mit Intervallarithmetik eingeschlossen. Mit der analytischen Interpolation bleibt die Fehlklassifikationswahrscheinlichkeit im idealen Modell über das ganze Offsetintervall unter $1{,}73\cdot10^{-6}$.

**Interval check of the pulse sequence.** All 505 grid amplitudes of the fixed 24-segment sequence were enclosed using interval arithmetic. Analytic interpolation keeps the ideal-model misclassification probability below $1.73\cdot10^{-6}$ throughout the offset interval.

**Echo-Rückrechnung.** Zwei gemeinsame Hilfsflips und eine zeitlich gespiegelte Pulsfolge invertieren den zentrierten Transferblock bei vorwärts laufender Drift. Eine zusätzliche Wartezeit im verschobenen Zustand gleicht die skalare Blockphase für die ganzzahligen Labels aus. Ideale gemeinsame Hilfsflips sind eine zusätzliche Voraussetzung.

**Echo uncomputation.** Two common auxiliary flips and a time-reversed control sequence invert the centered transfer block with forward drift. An additional wait in the shifted state aligns the scalar block phases for integer labels. Ideal common auxiliary flips are an additional requirement.

**Endlicher gemeinsamer Hilfsflip.** Eine 32-Abschnittsfolge approximiert das phasenfeste Gatter $-iX$ auf allen fünf Verstimmungsblöcken. Auf dem geprüften Offsetgitter beträgt der größte Operatornormfehler rund $0{,}00156$. Die zusätzlichen Blockphasen der endlichen Pulsdauer gehen in die Wartezeitbilanz ein.

**Finite common auxiliary flip.** A 32-segment sequence approximates the phase-matched gate $-iX$ on all five detuning blocks. The largest operator-norm error on the sampled offset grid is about $0.00156$. The finite gate duration contributes additional block phases to the wait-time balance.

**Vollständiger endlicher Echo-Zeiger.** Auf fünf Blöcken und 101 Offsetpunkten ergibt die Simulation maximal rund $3{,}60\cdot10^{-6}$ Fehlklassifikation und $6{,}71\cdot10^{-6}$ Restanregung des Hilfsdoubletts. Der vollständige Zustandsvektorabstand ist höchstens rund $0{,}003294$ auf diesen Prüfpunkten.

**Full finite-pulse echo pointer.** Across five blocks and 101 offset points the simulation gives maximum misclassification of about $3.60\cdot10^{-6}$ and residual auxiliary excitation of $6.71\cdot10^{-6}$. The full state-vector distance is at most about $0.003294$ at those sampled points.

**Intervallschätzung für den vollständigen Echo-Zeiger.** Analytische Interpolation mit numerischen Stützstellen ergibt rund $9{,}05\cdot10^{-6}$ maximale Fehlklassifikation und $1{,}37\cdot10^{-5}$ Restanregung im gemeinsamen statischen Offsetintervall. Die Stützwerte des Gesamtprotokolls sind noch nicht intervallzertifiziert.

**Interval estimate for the full echo pointer.** Analytic interpolation with numerical grid values gives about $9.05\cdot10^{-6}$ maximum misclassification and $1.37\cdot10^{-5}$ residual excitation over the common static offset interval. The full protocol's grid values are not interval-certified.

**Intervallabgleich des vollständigen Echo-Zeigers.** Die fixierten Pulsfolgen wurden an allen 505 Stützstellen mit Intervallarithmetik geprüft. Für das gesamte statische Offsetintervall ergeben sich Fehlklassifikation unter $9{,}06\cdot10^{-6}$ und Restanregung unter $1{,}371\cdot10^{-5}$ im idealisierten Blockmodell.

**Interval check of the full echo pointer.** The fixed pulse sequences were checked with interval arithmetic at all 505 grid points. Over the full static-offset interval, misclassification is below $9.06\cdot10^{-6}$ and residual excitation below $1.371\cdot10^{-5}$ in the idealized block model.

**Kopierpuls bei laufender Drift.** Zwei komplementär gesteuerte Kopierhälften mit Hilfsflip dazwischen lassen beide Hilfszustände gleich lange auf beiden Driftenergien liegen. Der Zeiger registriert weiterhin das ursprüngliche Hilfsbit. Die endliche Kopierzeit und die zusätzlichen Hilfsflips ändern die Wartezeitbilanz.

**Copy pulse with active drift.** Two complementary controlled copy halves with an auxiliary flip in between let both auxiliary states spend equal times at both drift energies. The pointer still records the original auxiliary bit. The finite copy duration and additional flips change the wait-time balance.

**Endlicher Kopierpuls im vollständigen Zeiger.** Mit sechs endlichen Hilfsflips und zwei Kopierhälften bei laufender Drift liefert die Simulation auf 505 Prüfpunkten höchstens rund $4{,}40\cdot10^{-6}$ Fehlklassifikation und $1{,}51\cdot10^{-5}$ Restanregung. Die komplementären diagonalen Kopierkopplungen bleiben Modellannahmen.

**Finite copy pulse in the full pointer.** With six finite auxiliary flips and two copy halves under active drift, the simulation gives maximum misclassification of about $4.40\cdot10^{-6}$ and residual excitation of $1.51\cdot10^{-5}$ at 505 sampled points. The complementary diagonal copy couplings remain model assumptions.

**Intervallprüfung des endlichen Kopierpulses.** Für fünf Blöcke und das ganze statische Offsetintervall bleiben Fehlklassifikation und Restanregung unter $1{,}658\cdot10^{-5}$ und $3{,}431\cdot10^{-5}$. Die Rechnung verwendet die modellierten komplementären Kopierkopplungen.

**Interval check of the finite copy pulse.** Across five blocks and the full static offset interval, misclassification and residual excitation remain below $1.658\cdot10^{-5}$ and $3.431\cdot10^{-5}$. The calculation uses the model's complementary copy couplings.

**Eine bedingte Kopplung für beide Kopierhälften.** Die komplementäre Hälfte entsteht aus einer freien Zeigerrotation und derselben bedingten Kopplung mit umgekehrtem Vorzeichen. Bei gleichzeitiger Anwendung bleibt die zertifizierte Modellsequenz identisch. Eine Umkehr nur der transversalen Komponente erfordert zusätzlich eine bedingte Phasenkorrektur.

**One conditional coupling for both copy halves.** The complementary half combines a free pointer rotation with the same conditional coupling at reversed sign. With simultaneous application the certified model sequence is identical. Reversing only the transverse component requires an additional conditional phase correction.

**Kopierhälften mit positiver Kopplung.** Die Periodizität der Zeigerrotation erlaubt, die inverse Kopierhälfte durch einen längeren positiven Puls und eine freie Zeigerrotation zu ersetzen. Ein zusätzlicher Driftabschnitt in der ersten Hälfte erhält den Phasenausgleich. Die Fehler der längeren Sequenz sind separat zu prüfen.

**Copy halves with positive coupling.** Pointer rotation periodicity replaces the inverse copy half with a longer positive pulse and a free pointer rotation. Additional idle drift in the first half preserves phase balance. The longer sequence requires its own error check.

**Intervallprüfung mit positiver Kopierkopplung.** Die verlängerte Kopierfolge hält im Modell über das gesamte statische Offsetintervall die Fehlklassifikation unter $1{,}091\cdot10^{-5}$ und die Restanregung unter $1{,}866\cdot10^{-5}$. Vorausgesetzt sind exakte Kopierpulsflächen und die freie Zeigerrotation.

**Interval check with positive copy coupling.** Throughout the static offset interval the longer copy sequence keeps model misclassification below $1.091\cdot10^{-5}$ and residual excitation below $1.866\cdot10^{-5}$. The calculation assumes exact copy pulse areas and free pointer rotation.

**Toleranz der Kopierpulsflächen.** Bei festen Abschnittsdauern und relativen Kopierflächenfehlern bis $0{,}1$ Prozent bleibt die Fehlklassifikation im Modell unter $1{,}25\cdot10^{-4}$. Die Schranke addiert die aus den Kopierfehlern resultierende Amplitudenabweichung zum zertifizierten Modellwert.

**Copy pulse area tolerance.** At fixed segment durations, relative copy area errors up to $0.1$ percent keep model misclassification below $1.25\cdot10^{-4}$. The bound adds the copy-induced amplitude error to the certified model value.

**Unabhängige Verstimmungsoffsets.** Die Klassifikationsschranke bleibt blockweise gültig, aber verschiedene Offsets der akzeptierten Paare erzeugen eine relative Phase $40\pi(\epsilon_{+3}-\epsilon_{-3})$. Schon eine Differenz von $0{,}025$ vertauscht im Modell die Austauschports, obwohl der Nullzeiger korrekt selektiert.

**Independent detuning offsets.** The classification bound remains valid block by block, but different offsets in the accepted pair produce a relative phase $40\pi(\epsilon_{+3}-\epsilon_{-3})$. A difference of $0.025$ already exchanges the model's interference ports while the zero pointer still selects correctly.

**Austausch-Echo für statische Blockphasen.** Zwei Zeigerläufe mit kohärentem Tausch der Nullzustände dazwischen geben beiden Zuständen dieselbe Summe der Blockphasen. Bei frischen Hilfsregistern und idealem Tausch ist der leerlaufbereinigte Zustandsvektorfehler im Null-Doublet kleiner als $0{,}010714$.

**Exchange echo for static block phases.** Two pointer runs with a coherent swap of the zero states between them give both states the same sum of block phases. With fresh auxiliary registers and an ideal swap, the idle-corrected state-vector error in the zero doublet is below $0.010714$.

**Modellschluss und native OP1-Brücke.** Auf dem periodischen Randmodell liefert die erhaltene und klassisch kalibrierte gemischte Auslesung $v a_M|n|$. Der relationale Nullselektor und ein kohärenter Registertausch ermöglichen einen gesamtflusserhaltenden Kohärenztest. Der Partial-Swap aus r28 und r30 ist eine Vorlage; die Identifikation seiner Register mit gravitativen Randflüssen und die native T-Flächenkalibrierung bleiben offen.

**Model result and native OP1 bridge.** On the periodic boundary model, the conserved and classically calibrated mixed readout gives $v a_M|n|$. The relational zero selector and a coherent register swap permit a total-flux-conserving coherence test. The partial swap in r28 and r30 supplies a template; identification of its registers with gravitational boundary fluxes and native T-area calibration remain open.

**Zählnormierung und T-Selektor.** Gleichförmige Flächenskalierung ändert bei festem Spinträger den Normierungsparameter invers, lässt aber alle normierten Spingewichte gleich. Die Minimalspinzählung aus r63 benötigt eine eigene Einschränkung auf den Casimirsektor $J^2=3/4$ und das Zählgewicht zwei. Der Flusszeiger des Randmodells weist diese Zuordnung nicht nach.

**Counting normalization and T selector.** Uniform area scaling at fixed spin support changes the normalization parameter inversely while leaving all normalized spin weights unchanged. The r63 minimal-spin counting requires a separate restriction to the Casimir sector $J^2=3/4$ and counting weight two. The boundary-model flux pointer does not establish that identification.

**Transversaler Minimalspin-Selektor.** Das einzelne Flusslabel $m=\pm1/2$ tritt auch bei höheren halbzahligen Spins auf. Der Spektralwert $1/2$ der gemeinsamen Quadratsumme $J_x^2+J_y^2$ wählt dagegen genau den Spin-$1/2$-Sektor. Die native Realisierung dieser Auslesung und das effektive Zählgewicht bleiben zu prüfen.

**Transverse minimal-spin selector.** The single flux label $m=\pm1/2$ also occurs at higher half-integer spins. The spectral value $1/2$ of the joint quadratic observable $J_x^2+J_y^2$ instead selects exactly the spin-$1/2$ sector. Native implementation of this readout and its effective counting weight remain open.

**Alternierende Minimalspin-Filter.** Die Betragsfilter $J_x^2=1/4$ und $J_y^2=1/4$ lassen beide Minimalspinzustände kohärent passieren. Auf einem Träger mit Spinobergrenze $J$ sinkt die Falschakzeptanz nach $k$ alternierenden Abfragen des zweiten Filters höchstens wie $(1-1/(J+1/2))^k$. Die beiden binären Instrumente bleiben native Voraussetzungen.

**Alternating minimal-spin filters.** The magnitude filters $J_x^2=1/4$ and $J_y^2=1/4$ pass both minimal-spin states coherently. With spin cutoff $J$, false acceptance after $k$ alternating queries of the second filter is bounded by $(1-1/(J+1/2))^k$. Both binary instruments remain native requirements.

**Kronecker-Delta als Spinfilter.** In der Eigenbasis markiert $\delta_{4m_x^2,1}$ beide Vorzeichen gemeinsam. Auf einem begrenzten Spinträger kann eine gemeinsame kontrollierte quadratische Phase diesen Filter als endliche Charakter-Mittelung umsetzen. Die entsprechende Phase von $2(J_x^2+J_y^2)-I$ liefert direkt den Minimalspinfilter.

**Minimalspin-Delta mit Referenzdoublet.** Eine gemeinsame Singulettauswahl mit Spin-$1/2$-Referenz erkennt nur den Minimalspin und hat zunächst Erfolg $1/4$. Zwei kohärente Reflexionen verstärken die Auswahl im idealen Modell exakt, ohne die magnetischen Zustände zu unterscheiden. Die Singulettreflexion ist eine zusätzliche native Voraussetzung.

**Isotroper Referenzaustausch und Zählgewicht.** Der Eigenwert $-3/2$ von $2\mathbf J\cdot\mathbf R$ mit Spin-$1/2$-Referenz isoliert den gemeinsamen Singulettsektor. Kohärente Rückrechnung lässt lokal beide magnetischen Systemzustände bestehen. Globale magnetische Projektion und volle Singulettprojektion liefern verschiedene endliche Zählungen und denselben führenden Exponenten pro Punkt. Native Austauschkopplung und Horizontprojektion bleiben offen.

**Gemeinsame M- und T-Zählmasken.** Im Einpunktmodell wählt $B_u-|J_u|=0$ die beiden Extremzustände jedes nichttrivialen Spins. $B_u=1/2$ wählt nur den Minimalspin. Eine einzelne U(1)-Komponente kann diese Masken nicht unterscheiden. Die Achsenmittelung erhält das M-Zählgewicht zwei je Irrep, ergibt bei höheren Spins aber einen probabilistischen Effekt.

**Common M and T counting masks.** In the single-puncture model, $B_u-|J_u|=0$ selects the two extremal states in each nontrivial spin. $B_u=1/2$ selects only minimal spin. A single U(1) component cannot implement these masks. Axis averaging preserves the M counting weight of two per irrep but gives a probabilistic effect at higher spins.

**QAM-Rückwärtssuche für Spin-Zählungen.** Das Werkzeug `python -m qam.tools.spin_readout_search` berechnet erzwungene Effekte und rotationsinvariante Kandidaten aus exakten Zählgewichten. Die verschachtelten magnetischen Labels je Parität liefern einen vollständigen Machbarkeitstest für eine gemeinsame Funktion von $2m$. Für OP1 scheitert T beim Übergang von $j=1/2$ zu $j=3/2$: Die geforderte Spur sinkt um zwei, obwohl zwei neue Labels hinzukommen und alle Effekte nichtnegativ sind. Auf dem kleineren Träger bis $j=1$ gelingt der T-Filter. Die Befunde betreffen die deklarierten Spinträger und Zugriffsarten.

**QAM inverse search for spin counts.** The solver computes forced effects, rotation-invariant candidates, and exact single-axis witnesses or trace-increment obstructions. In OP1, the single-axis T effect becomes impossible as soon as both spin $1/2$ and spin $3/2$ are included.
