# OP5 – Druckfreier Arbeitsspeicher mit lokaler Kraftreaktion

21. November 2026. Analytische Erkundung im Materieframe M, bis zur zweiten Ordnung in der Auslenkung $\epsilon$ und in linearer Gravitation. Für beide Kontinua der vorigen Schaltbahn wird ein positiver druckfreier Teilchenstrom mit veränderlicher Ruheenergie je Teilchen angesetzt. Die Bahn, Energieumwandlung und lokale Kraftreaktion werden rückwärts aus dem benötigten Leistungsfluss bestimmt.

## Vorwissen geprüft

Die [Umschaltung zwischen den Ruhelagen](OP5_J_Umschaltung_Ruhelagen.md) hat bei quadratischer Nachführung einen erhaltenen mechanischen Tensor ohne linearisierte Außenkrümmung. Dazu wurde ein mitbewegter Speicher mit Gegenfluss $\sigma_a v_a$ und verschwindendem zusätzlichem räumlichem Impulsfluss bis zur zweiten Ordnung angenommen. Der [ältere Reservoirabgleich](OP5_J_Reservoir_Quadrupolabgleich.md) verwendet einen separaten elastischen Träger. Die Suche nach Relativdrift, Teilchenzahl, veränderlicher Ruheenergie und lokaler Reaktionskraft in Vorab-Notizen, jüngeren Rundennotizen und OP5-Analysen ergab für diesen Schaltweg keine Bilanz eines Teilchenstroms. Die Frage gehört im [Gesamtbild](../../../wiki/Gesamtbild.md) zur lokalen Auslese. I3 erfordert weiterhin eine eigenständige kosmologische Bestandsdynamik.

## Trägerbahn und Ruheenergie

Betrachte jeweils eine Komponente und unterdrücke ihren Index $a$. Ihre Matrixbahn sei $x(t,X)$ aus der Vorarbeit, $v=\dot x$ am aktuellen Raumpunkt und $J=\det\nabla_X x$. Schreibe $\varphi$ für das zugehörige Profil, also im zweiten Kontinuum für $-\varphi_{\rm gemeinsam}/c$. Die Referenzruhedichte $\rho$ zerfällt in einen Matrixanteil $\rho-r_0>0$ und einen Speicheranteil $r_0=n_0m_0>0$. Hier sind $n_0$ die Referenzteilchenzahldichte und $m_0$ die anfängliche Ruheenergie pro Teilchen. Beide sind im aktiven Bereich konstant. Der nichtkonvektive Gegenfluss ist bis zur betrachteten Ordnung
$$
j=\sigma v
=\epsilon^2 \rho\,\dot s\,\ddot s\,\nabla\left(\frac{\varphi^2}{2}\right).
$$
Verschiebe die Trägerteilchen relativ zu dieser Matrixbahn um $d$ in der Darstellung $x_{\rm R}(t,X)=x(t,X)+d(t,X)$. Der kompakte Sollversatz
$$
d=\frac{\epsilon^2\rho}{2r_0}\dot s^2\nabla_X\left(\frac{\varphi^2}{2}\right)
$$
erfüllt $r_0\dot d=j$ bis zur betrachteten Ordnung. Die Differenz zwischen Referenz- und Raumposition im quadratischen Fluss wirkt erst in dritter Ordnung. Der relative Weg und der relative Geschwindigkeitsunterschied sind an beiden ruhenden Enden null. Der Fluss kehrt bei glattem monotonem Schalten sein Vorzeichen dort um, wo $\dot s$ nach dem Anstieg wieder abnimmt. Für kleines $\epsilon$ bei festem positivem $r_0$ bleibt die Bewegung glatt und langsam gegenüber der Lichtgeschwindigkeit.

Teilchenzahl bleibt durch Pushforward von $n_0\,d^3X$ erhalten. Der relative Versatz ändert bei zunächst gleicher Ruheenergie die räumliche Trägerdichte gegenüber dem mitbewegten Hintergrund um $-r_0\operatorname{div}d$. Die relative kinetische Energiekorrektur ist wegen $v=O(\epsilon)$ und $\dot d=O(\epsilon^2)$ mindestens dritter Ordnung. Sei $\mathcal E$ wie zuvor die Summe aus gemeinsamer kinetischer Energie beider Anteile, elastischer Energie und Stellenergie pro Referenzvolumen. Wähle die Änderung $\delta m$ der Ruheenergie je Teilchen so, dass
$$
n_0\delta m=-\mathcal E+r_0\operatorname{Div}_X d.
$$
Dann beträgt die relative Energiedichteänderung des Speichers $-\mathcal E/J$ bis zur betrachteten Ordnung. $m_0+\delta m$ ist für kleine $\epsilon$ positiv. Beide Endzustände haben $\delta m=0$. Durch Zeitableitung und $r_0\dot d=\sigma v$ folgt $n_0\partial_t\delta m=-\mathcal W$ in der Konvention $\partial_t\mathcal E=\operatorname{div}(\sigma v)+\mathcal W$ bis zur betrachteten Ordnung. Hier ist $\mathcal W$ die an Matrix und Stellfreiheitsgrade übertragene Leistung aus der Änderung der Ruheenergie. Der Druckfluss entfällt in diesem ersten Modell. Bei unveränderlicher Ruheenergie pro Teilchen wäre der integrierte Beitrag der reinen Umverteilung null. Er könnte die im Übergang positive integrierte kinetische und gespeicherte Energie allein nicht ausgleichen.

## Symmetrische Tensoren und lokale Reaktionen

Für den Träger gilt $T_{\rm R}^{\mu\nu}=n\,m\,U_{\rm R}^{\mu}U_{\rm R}^{\nu}$ mit der Eigenzahldichte $n$. Bei erhaltener Teilchenzahl und vorgegebener Kraft hat seine Divergenz die Form
$$
Q^\nu=\partial_\mu T_{\rm R}^{\mu\nu}
=n\,\frac{dm}{d\tau}\,U_{\rm R}^{\nu}+nm\,\frac{dU_{\rm R}^{\nu}}{d\tau}.
$$
Damit sind Leistung aus der Ruheenergie und Beschleunigungskraft unabhängig spezifiziert. Der lokale Gegenport der Matrix ist $-Q^\nu$. Die vorgegebene Reaktion ist punktweise und überträgt in diesem Kontinuumsmodell kein getrenntes Kraftpaar über eine endliche Strecke. [Carroll zur Teilchenzahl und zum druckfreien Tensor](https://ned.ipac.caltech.edu/level5/March01/Carroll3/Carroll1.html)

Bezüglich einer Referenz, in der der Speicher exakt mit der Matrix mitgeführt wird und seine Anfangsruheenergie behält, gilt
$$
\Delta T_{\rm R}^{00}=-\mathcal E/J,\qquad
\Delta T_{\rm R}^{0i}=j_i,\qquad
\Delta T_{\rm R}^{ij}=0
\quad\text{bis zur zweiten Ordnung}.
$$
Die gemeinsame konvektive Spannung $r_0v_iv_j/J$ steckt bereits im ursprünglich mitbewegten Speicheranteil. Mit Cauchy-Spannung $\sigma$ im Vorzeichen der Vorarbeit enthält der symmetrische Matrixtensor den Fluss $-\sigma v$. Seine Zeitkomponenten folgen aus der Orthogonalität der mechanischen Spannung zur Materialvierergeschwindigkeit. Die zugehörige Spannungskorrektur in $T^{00}$ ist von Ordnung $v^{\mathsf T}\sigma v=O(\epsilon^3)$. Die Änderung des Speicherflusses hebt den mechanischen Fluss daher in Energie- und Impulsbilanz zugleich auf. Nach Addition beider Tensoren bleiben der Pushforward der gesamten Referenzruheenergie $\rho$, ihr konvektiver Strom und der räumliche Impulsfluss $\rho v_iv_j/J-\sigma_{ij}$. Das ist der zur retardierten Außenkompensation verwendete Tensor.

Mit Materialbeschleunigung $D_tv$ und Euler-Zeitableitung $\partial_t$ am festen Raumpunkt erhält man
$$
Q^i=\frac{r_0}{J}(D_tv)_i+\partial_t j_i+O(\epsilon^3),\qquad
Q^0=\frac{r_0}{J}v\cdot D_tv-\mathcal W+O(\epsilon^3).
$$
Der Unterschied zwischen räumlicher und Referenzleistungsdichte bei $\mathcal W=O(\epsilon^2)$ fällt in den Rest. Der Kräfteabgleich verwendet $\rho D_tv/J=\operatorname{div}\sigma$. In der Matriximpulsbilanz tritt aus ihrem symmetrischen Leistungsfluss zusätzlich $-\partial_t j$ auf. Daher ergibt sich dort gerade $-Q^i$. Die Energiereaktion schließt den Arbeitsanteil $-r_0v\cdot D_tv/J$ für die Mitnahme des Speichers ein. Die führende mechanische Kraft auf den Speicher ist von Ordnung $\epsilon$. Ein passives Draggesetz mit beschränktem Faktor, dessen Kraft proportional zur Relativgeschwindigkeit $O(\epsilon^2)$ ist, kann diese Mitnahme im druckfreien Modell nicht liefern. Die expliziten Ports sind somit eine aktive Kontinuumsrealisierung. Eine mikroskopische Vorrichtung, die beide Ports samt eigenen Quellen liefert, ist weiterhin offen.

## Empfindlichkeit gegenüber zusätzlichem Speicherstress

Hat der Speicher eine bekannte kompakte symmetrische räumliche Spannung $\Pi=O(\epsilon^2)$ als **positiven** Beitrag zu $T_{\rm R}^{ij}$, können ihre durch die Bewegung erzeugten Zeitkomponenten erst oberhalb der betrachteten Ordnung beitragen. Bei unveränderter Energie- und Flussbilanz kann die Matrix den zusätzlichen räumlichen Beitrag durch $\sigma\mapsto\sigma+\Pi$ ausgleichen. Dafür wird die Zielmetrik um
$$
\Delta G_*=-2\mathsf C^{-1}\left[J F^{-1}\Pi F^{-\mathsf T}\right]
$$
korrigiert. Der Speicherport ändert sich räumlich um $\operatorname{div}\Pi$. Die zusätzliche mechanische Leistung $\Pi v$ ist von dritter Ordnung. Damit bleibt bei diesem Nachstellen der gesamte Tensor und folglich seine gewöhnliche linearisierte Außenkrümmung bis zur betrachteten Ordnung erhalten. Soll die spannungsfreie Endmetrik erhalten bleiben, muss auch $\Pi$ dort null sein. Eigenständige Änderungen der Speicher- oder Aktorenergiedichte, ihres Flusses oder der Kräfte außerhalb der idealisierten Überlagerung verlangen eine eigene Bilanz. Die lineare lokale W2-Quelle bleibt im Vergleich erhalten. Die native Higgs–OP5-Kopplung, die Quelle realer Apparaturfelder und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_druckfreier_arbeitsspeicher.wl) · [Tatsächliche Ausgabe](op5_j_druckfreier_arbeitsspeicher.txt) · [Laufmanifest](op5_j_druckfreier_arbeitsspeicher.json)

Wolfram kontrollierte Teilchenweg, Ruheenergieumwandlung, Entwicklung des druckfreien Tensors, lokale Kraft- und Leistungsreaktionen sowie die Druckkorrektur beim isotropen Materialgesetz für diagonales $F$. Die allgemeine Spannungsumrechnung folgt durch Pullback und Pushforward. Die Rechnung ist klassische Kontinuumsmechanik. Reproduzierbar mit **wolframscript -file op5_j_druckfreier_arbeitsspeicher.wl**.
