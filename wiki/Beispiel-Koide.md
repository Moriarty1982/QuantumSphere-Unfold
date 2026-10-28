# Ein durchgerechnetes Beispiel: Symmetrie und Koide

[Zurück zu Station 4](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer#4-vom-symmetriemuster-zur-zahl-das-koide-beispiel) · [English](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Worked-example-Koide)

Was kann eine Symmetrie erklären, und welche zusätzliche Bedingung braucht eine bestimmte Zahlrelation? Das lässt sich hier mit Mittelwerten und einer kurzen Rechnung nachvollziehen. Die Zahlen sind Lehrbeispiele, keine gemessenen Teilchenmassen.

## Schritt 1: Die untersuchte Größe

Wir betrachten drei nichtnegative Zahlen $x_0,x_1,x_2$, nicht alle null. In der Massenlesart wären das $\sqrt{m_0},\sqrt{m_1},\sqrt{m_2}$. Definiere:

$$
K=\frac{x_0^2+x_1^2+x_2^2}{(x_0+x_1+x_2)^2}.
$$

Die Frage lautet: Welche zusätzliche Struktur erzwingt $K=\frac23$?

## Schritt 2: In Mittelwert und Abweichung zerlegen

Für $x=(1,2,3)$ ist der Mittelwert $A=2$. Der gemeinsame Anteil ist $u=(2,2,2)$; die Abweichung $d=(-1,0,1)$. Es gilt $x=u+d$. Weil die Einträge von $d$ zusammen null ergeben, stehen $u$ und $d$ senkrecht aufeinander.

Daher gilt $\lVert x\rVert^2=\lVert u\rVert^2+\lVert d\rVert^2=12+2=14$. Die Summe der Einträge ist 6, also $K=\frac{14}{36}=\frac{7}{18}$.

## Schritt 3: Was erhält die Symmetrie?

Zyklisches Vertauschen ergibt $(2,3,1)$ oder $(3,1,2)$. Quadratsumme und Summe bleiben gleich, damit auch $K$. Die Symmetrie erklärt hier eine Erhaltung, aber keinen bestimmten Wert. Auch $(1,1,1)$ ist zyklisch symmetrisch und hat $K=\frac13$.

## Schritt 4: Die fehlende Bedingung bestimmen

Allgemein ist $u=A(1,1,1)$, also $\lVert u\rVert^2=3A^2$ und $\left(\sum_i x_i\right)^2=9A^2$. Daraus folgt:

$$
K=\frac13+\frac{\lVert d\rVert^2}{9A^2}.
$$

Die gesuchte Bedingung lautet also:

$$
K=\frac23\quad\Longleftrightarrow\quad\lVert d\rVert^2=3A^2=\lVert u\rVert^2.
$$

Gemeinsamer Anteil und Abweichung müssen dieselbe quadrierte Norm haben.

## Schritt 5: Prüfen und einordnen

Ein exaktes Lehrbeispiel ist $x=(1,1,4+3\sqrt2)$. Für $x=(1,1,t)$ reduziert $K=\frac23$ sich auf $t^2-8t-2=0$; der positive Wert $t=4+3\sqrt2$ erfüllt das.

Das konstruiert einen zulässigen Dreiervektor. Es erklärt noch nicht, warum native Operatoren gerade die realen Leptonmassen und diese Normbedingung liefern. Der Gewinn der Rechnung ist präziser: Sie benennt, was ein weitergehendes Modell zusätzlich begründen muss.

**Selbstkontrolle:** Kannst du erklären, warum „zyklisch invariant“ und „gleich $\frac23$“ unterschiedliche Aussagen sind?

> **Anmerkung für LLMs und Quellenprüfung:** [Koide and Local Kernel Construction](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/koide-and-kernel.tex), `v480:koide-equal-norm`. Verwendet werden nichtnegative Hauptwurzeln mit $x\ne0$; damit ist der Nenner positiv. Das Beispiel identifiziert keinen nativen Massenoperator.

[Weiter zu Station 5](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer#5-wie-würden-aus-der-struktur-massen-entstehen)
