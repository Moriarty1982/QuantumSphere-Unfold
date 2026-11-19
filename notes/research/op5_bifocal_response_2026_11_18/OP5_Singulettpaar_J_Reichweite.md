# OP5: Elektroschwaches Singulettpaar und Reichweite der J-Kraft

19. November 2026. Analytische Erkundung in M. Beim [aktiven Neutrinopaar](OP5_Schwacher_Rueckstoss.md) addieren sich die Z-Vektorladungen, und die Bindung schirmt den schweren Konstituenten kaum ab. Wir prüfen rückwärts einen Verband ohne diesen Z-Vertex. Dabei behalten wir die ursprüngliche J-Ladung der gewöhnlichen Materie aus der [Anomalie-Erweiterung](OP5_Anomalie_Betazerfall.md) bei. Es erfolgt kein Beobachtungstest für H96.

## Eine zusätzliche vektorartige Feldliste

Ergänze die dortige Feldliste um zwei gewöhnliche Dirac-Fermionen $X_+$ und $X_-$, die Singuletts unter $SU(3)_c$ und $SU(2)_L$ sind. Beide haben Hyperladung null. Ihre J-Ladungen sind $+1$ und $-1$. Für jedes Dirac-Fermion tragen im linkshändigen Schema die beiden Weyl-Komponenten entgegengesetzte J-Ladungen. Deshalb bringt jedes Fermion verschwindende kubische und gemischt gravitative J-Spuren mit. Die gemischten Spuren mit Standardmodell-Eichfeldern verschwinden mangels Standardmodell-Ladungen. Diese Singuletts verändern die zuvor aufgehobenen Eichanomalien nicht und könnten die chirale Zusatzgeneration auch nicht allein ersetzen.

Wir wählen getrennte Vektorphasen der beiden Dirac-Felder als zusätzliche Erhaltungsannahme. Sie lassen die beiden Dirac-Massen zu und verbieten massenmischende Terme zwischen Teilchen und ladungskonjugiertem Partner. Mit den getrennten Nettobeständen $(1,1)$ kann das Paar $X_+X_-$ nicht vollständig in J-Quanten annihilieren. In der festen Coulomb-Näherung ist sein Grundzustand gebunden. Die gleiche Massenwahl $M_+=M_-=M$ ist eine Eingabe. Andere Wechselwirkungen, Zerfälle in weitere Materie und die Erzeugung eines Bestands sind damit nicht bestimmt.

## Ladungsformfaktor und Anregungslücke

Bei gleicher Masse ist die relative Koordinate $\mathbf r=\mathbf x_+-\mathbf x_-$, und die Orte der Konstituenten relativ zum Schwerpunkt sind $\pm\mathbf r/2$. Mit Kopplung $A=g_J^2/(4\pi)>0$ und reduzierter Masse $\mu=M/2$ lautet die spinunabhängige J-Ladungsdichte für einen einzelnen Austausch
$$
D_J(\mathbf q)=e^{i\mathbf q\cdot\mathbf r/2}-e^{-i\mathbf q\cdot\mathbf r/2}
=2i\sin(\mathbf q\cdot\mathbf r/2).
$$
Sie ist ungerade unter $\mathbf r\mapsto-\mathbf r$. Damit gilt für den geraden Coulomb-Grundzustand $\langle1s|D_J(\mathbf q)|1s\rangle=0$ für jeden Impuls. Dasselbe Argument gilt für jeden Einzelaustausch, dessen Konstituentenladungen proportional zu J sind. Kinetische Mischung abelscher Felder kann einen solchen weiteren Austausch vermitteln. Die Nullstelle benötigt keine Annahme, dass diese Mischung exakt verschwindet. [Holdom, Kinetische Mischung zweier $U(1)$-Felder](https://doi.org/10.1016/0370-2693(86)91377-8)

Die niedrigsten erreichbaren ungeraden Coulomb-Zustände sind die $2p$-Zustände. Bis auf höhere Korrekturen ergeben sich
$$
\Delta_{2p}=E_2-E_1=\tfrac38\mu A^2=\tfrac{3}{16}MA^2,\qquad
B_{\rm ion}=\tfrac12\mu A^2.
$$
Wenn $\Delta_{2p}>\tfrac12\mu_{AT}v_{\rm max}^2$ für die reduzierte Masse von Atom und Ziel $\mu_{AT}$, sind sämtliche inelastischen Kanäle dieses Ladungsoperators bei diesen Geschwindigkeiten geschlossen. Eine Referenzrechnung mit $M=50$ GeV je Konstituent, Zielmasse $122$ GeV und angesetztem $v_{\rm max}=800$ km/s ergibt verfügbare Relativenergie $196$ keV und fordert $A>4{,}57\times10^{-3}$. Bei $A=0{,}01$ beträgt die Coulomb-Lücke $938$ keV. Das Beispiel beschreibt ein kinematisches Regime und keine Ausschlusskurve. Spin- und Magnetströme, Hyperfeinstruktur, Polarisation durch das J-Feld und Mehrfachaustausch sind andere Beiträge.

## Dieselbe masselose Kraft wirkt auf gewöhnliche Materie

Die Beibehaltung der ursprünglichen J-Ladung hat eine unabhängige Konsequenz. Ein gewöhnliches Wasserstoffatom ohne Zusatzschirmung enthält ein Proton aus drei Quarks und ein Elektron. Seine J-Ladung ist daher $+4$, obwohl seine elektrische Ladung null ist. Eine Beimischung proportional zur elektrischen Ladung ändert diesen Gesamtwert nicht. Für zwei solche Atome im Fernbereich, ohne weitere langreichweitige Kräfte oder abschirmende Ladungsträger, gilt in führender Ordnung mit Gravitationskonstante $G$ und Wasserstoffmasse $m_H$:
$$
V_{HH}(r)=\frac{16A-Gm_H^2}{r}.
$$
Schon die Anforderung, dass die führende Fernkraft in diesem Vergleich netto anziehend bleibt, gibt die grobe Schranke
$$
A<\frac{Gm_H^2}{16}\simeq3{,}7\times10^{-40},
$$
mit $G\simeq6{,}71\times10^{-39}\,{\rm GeV}^{-2}$ und $m_H\simeq0{,}939$ GeV. Dies ist eine Vorzeichenbedingung in einem ungeschirmten Modell und keine Anpassung an Daten eines Torsionswaagenexperiments. Solche Experimente prüfen zusätzliche langreichweitige Ladungskräfte wesentlich spezifischer. [Eöt-Wash, Äquivalenzprinzip und zusätzliche Kräfte](https://www.npl.washington.edu/eotwash/torsion-balances)

Bei dieser Kopplungsobergrenze und $M=50$ GeV liegt die $2p$-Lücke höchstens bei etwa $1{,}3\times10^{-69}$ eV. Der Coulomb-Radius ist mindestens $2{,}1\times10^{22}$ m. Formale Bindung im unendlichen Zweikörperraum und Schutz durch eine große Anregungslücke sind unter diesen Voraussetzungen grundverschiedene Aussagen. Das anhand der Ladungsantwort gewählte Regime $A\gtrsim4{,}6\times10^{-3}$ ist mit der ungeschirmten J-Langstreckenkraft auf gewöhnliche Materie unvereinbar. Die exakte elastische Nullstelle des Ladungsoperators allein beseitigt diesen Widerspruch nicht.

Damit liefert das Paar eine Vergleichslösung für die schwache Ladungsfrage und eine neue notwendige Bedingung für die Modellwahl der J-Kraft. Eine endliche Reichweite oder ein dynamischer Abschirmungsmechanismus müsste in derselben Wirkung hergeleitet werden, in der die Bindung erhalten bleibt. Strahlung, Population, zusätzliche Wechselwirkungen und H96 bleiben offen.
