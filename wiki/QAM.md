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
