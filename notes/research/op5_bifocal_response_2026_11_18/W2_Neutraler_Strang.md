# OP5: Trägt der W2-Higgssektor einen neutralen Strang?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [Zugtermprüfung](W2_Zugterm_Quelle.md) ließ einen unabhängigen neutralen Strang als Modell übrig. Hier wird die einfachste Herleitung aus der [ausgeschriebenen W2-Wirkung](../v4_10_0_r82/Wirkung_W2_Higgs.md) geprüft. Die frühere [Higgsgrenze](Grenze_W2.md) betraf eine ebene Wand mit zwei verschiedenen asymptotischen Radien. Die vorliegende Rechnung betrifft einen geraden Strang mit zwei transversalen Koordinaten und demselben Vakuum am transversalen Rand.

## Statischer Sektor und Energie pro Länge

Prüfe einen glatten, zeitunabhängigen und entlang der Achse $z$ translationsinvarianten Defekt im flachen Raum. Im Stranginneren gibt es keine Fermionquelle und keine weitere Eichverbindung. Das Higgsdublett ist unter dem in W1 ausgeschriebenen $J$-U(1) neutral. Seine transversale Energie pro Länge relativ zum gebrochenen Vakuum lautet damit

$$
\mathcal T[\Phi]=G+P,\qquad
G=\int_{\mathbb R^2}|\nabla_\perp\Phi|^2\,d^2x,\qquad
P=\int_{\mathbb R^2}\lambda\big(|\Phi|^2-v^2\big)^2\,d^2x,\qquad
v^2=\frac{\mu^2}{2\lambda}.
$$

Beide Beiträge seien endlich. Die vier reellen Komponenten des Dubletts dürfen frei variieren. Insbesondere wird die Orientierung nicht auf einen bestimmten komplexen Phasenkreis beschränkt. Die Vakuumsubtraktion betrifft ausschließlich diese transversale Defektenergie. Sie setzt keinen gravitativen Vakuumterm fest.

## Die transversale Skalierung schließt den Defekt aus

Unter $\Phi_s(x)=\Phi(sx)$ mit $s>0$ bleibt $G$ in zwei Dimensionen gleich, während $P$ zu $s^{-2}P$ wird. Damit fordert Stationarität bezüglich der Skalierung

$$
\left.\frac{d}{ds}\mathcal T[\Phi_s]\right|_{s=1}=-2P=0.
$$

Diese Bedingung folgt auch bei nur kompakt getragenen Testvariationen. Dazu multipliziert man den infinitesimalen Skalierungsvektor $x\cdot\nabla_\perp\Phi$ mit einem glatten radialen Abschneider, der auf $|x|\le L$ eins und auf $|x|\ge2L$ null ist. Nach partieller Integration ist der Fehler durch ein konstantes Vielfaches der Energie im Ring $L<|x|<2L$ beschränkt, weil $|x||\nabla\chi_L|$ dort gleichmäßig beschränkt ist. Aus endlicher Energie verschwindet dieser Fehler für $L\to\infty$. Der Spurfaktor des Gradientenanteils ist in zwei transversalen Dimensionen null, der des Potentials ist zwei.

Da das Potential nichtnegativ ist, folgt $|\Phi|=v$ überall. In der unbeschränkten W2-Euler-Lagrange-Gleichung verschwindet damit die Potentialableitung. Jede Komponente erfüllt $\Delta_\perp\Phi_i=0$ und ist wegen $|\Phi|=v$ beschränkt. Die Mittelwerteigenschaft für ganze harmonische Funktionen erzwingt Konstanz. Folglich ist $\mathcal T=0$. Ein separat eingesetztes Zwangsmodell mit $|\Phi|=v$ würde andere Variationsgleichungen haben. Hier folgt die Normbedingung aus der W2-Feldgleichung und der Skalierung.

Ein globaler Phasenwirbel in einem fest gewählten komplexen Teilraum entgeht dem Befund nicht. Hat er für große $r$ die Form $\Phi\to v e^{in\theta}\Phi_0$ mit $|\Phi_0|=1$ und $n\ne0$, so fällt die Winkelgradientenenergie wie $n^2v^2/r^2$ und ihr Integral divergiert logarithmisch. Die endliche Spannung aus dem bisherigen Zugmodell lässt sich damit nicht gewinnen.

## Welche Änderung könnte die Skalierungsbilanz tragen?

Das unabhängige $J$-Feld liefert im angenommenen glatten und quellenfreien Stranginneren keine stationäre Gegenwirkung auf das neutrale Dublett. Für statische, $z$-invariante freie Maxwell-Felder sind die Feldkomponenten harmonisch auf $\mathbb R^2$. Endliche Feldenergie pro Länge macht sie quadratintegrierbar, wodurch sie nach der Mittelwerteigenschaft verschwinden. Dies verwendet quellenfreies Maxwell auf der ganzen Transversalebene. Ein singulärer Flusskern oder eine längs verteilte Quelle fällt außerhalb dieser Annahme.

Die Skalierung liefert zugleich eine Bedingung für eine erweiterte Wirkung. Ein aktiv an das Dublett gekoppelter magnetischer Kanal könnte anders skalieren. Bei $A_s(x)=sA(sx)$ bliebe dann ein kovarianter Gradiententerm in zwei Dimensionen invariant, während die magnetische Energie zu $s^2M$ würde. Bei sonst unveränderter Bilanz wäre $M=P$ eine notwendige Virialbedingung. Dies zeigt die Rolle einer möglichen transversalen Eichdynamik. Ob sie eine lokalisierte Lösung, deren Stabilität und deren Bindung an Foki liefern kann, ist damit offen.

Im geprüften W2-Teilsystem kann der Higgsradius keine positive Strangspannung begründen. Ein langes endliches Profil kann sich auch dann anders verhalten, wenn es entlang $z$ variiert oder im Inneren weitere Quellen trägt. Ausgeschlossen ist die hier definierte glatte, quellenfreie, translationsinvariante positive Spannungsdichte, auch als entsprechender glatter Grenzzustand im Inneren. Für I1 fehlen weiterhin eine hergeleitete Strangdynamik und Endpunktbindung. I3 verlangt eine eigenständige Überschussdynamik. I4 wäre ein eigener Kondensatansatz mit begründeten Frame- und Quellenregeln. Native Randwirkung und H96 bleiben offen.
