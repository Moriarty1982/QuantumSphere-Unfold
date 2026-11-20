# OP5 — Was Sende- und Empfangsanschlüsse von der sichtbaren Mischung erfassen

20. November 2026. Analytische Erkundung im Materieframe M. Ausgehend vom axialen Dirac-Schwellenvergleich wird die Auslese rückwärts untersucht. Gesucht sind die Bedingungen, unter denen die beiden Eigenlaufzeiten in einer Messung bestimmbar sind.

Vorwissen geprüft. Der [Dirac-Schwellenvergleich](OP5_J_Dirac_Schwellenabgleich.md) gibt bei gemeinsamer effektiver Metrikkopplung eine symmetrische Ladungsmatrix vor. Die [Endpunktdrift](OP5_J_Endpunktdrift.md) zeigt, dass profilgebundene Apparaturantworten durch Wiederholung allein untrennbar vom Streckenkontrast bleiben. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dieser Schritt zur lokalen OP5-Auslese vor H96. Die für I3 relevante Populationsdynamik wird durch die Anschlussrechnung nicht geliefert.

## Kinetische Mischung und physische Ladungen

Seien $F=(F_J,F_A)^{\mathsf T}$ und $K=K^{\mathsf T}>0$ die Feldstärken und die konstante flache kinetische Matrix. In einer zunächst nicht kanonischen Basis sei $D=D^{\mathsf T}$ die entlang des gleichen idealen Strahls integrierte Änderung der Laufzeitmatrix. Bei $F_c=K^{1/2}F$ werden aus einem Strom mit Ladungsvektor $q$ und der Matrix $D$
$$
w=K^{-1/2}q,\qquad T=K^{-1/2}D K^{-1/2}.
$$
Die Ausbreitungslaufzeiten relativ zur gemeinsamen Grundlaufzeit sind die Eigenwerte $\tau_j$ von $T$. Sie folgen auch aus $\det(D-\tau K)=0$, denn $D-\tau K=K^{1/2}(T-\tau I)K^{1/2}$. Die Gram-Matrix des vorigen Schwellenvergleichs ist in den kanonischen Ladungen zu bilden. Bei gemeinsamem axialem Profil gilt $D=\gamma\sum_i n_i q_i q_i^{\mathsf T}/m_i^2$, wobei $\gamma$ den integrierten geometrischen Faktor einschließlich der gemeinsamen Vorzahl enthält. Die invertierbare Normierung erhält den Rang jeder Familie von Anschlussladungen.

## Was der A/B-Vergleich bestimmt

Vorausgesetzt sind ein statischer, verlustfreier Einwegvergleich auf demselben Strahl, eine schwache geometrische Störung und fest orientierte, entlang des Strahls kommutierende lokale Antwortmatrizen. Letzteres gilt bei einer gemeinsamen Profilfunktion vor einer festen Ladungsmatrix. In diesem Modell wird nach Ausklammern der gemeinsamen Grundphase der A/B-Streckenkontrast durch $U(\omega)=\exp(i\omega T)$ dargestellt. Die Laufzeit ist hier mit der Phasenkonvention $+i\omega\tau$ definiert.

Mit zwei kohärent ausgewerteten Eingängen und zwei Ausgängen seien die gemessenen Matrizen $M_A=L R$ und $M_B=L U R$. Die komplexen Anschlussmatrizen $L$ und $R$ dürfen frequenzabhängig sein. Bei jeder Frequenz müssen beide invertierbar und zwischen A und B unverändert sein. Dann gilt
$$
M_A^{-1}M_B=R^{-1}U R.
$$
Daher liefern die entfalteten Eigenphasen von $M_A^{-1}M_B$ die Laufzeitdifferenzen über ihre Steigungen. Die Frequenzen müssen die Zuordnung und Entfaltung der Phasen erlauben. Gleichheit der Phasen an einer einzelnen Frequenz kann auch durch einen ganzzahligen $2\pi$-Umlauf entstehen. Geprüft werden die Eigenphasen selbst, sodass bei frequenzabhängigem $R$ keine Ableitung von $R$ in die Auswertung eingeht. Profilgebundene Änderungen von $L$ oder $R$, Reflexionen, Mehrwege und ein zweiter, nichtkommutierender Streckenbeitrag erfordern eine zusätzliche Modellierung oder Kontrolle.

## Grenzen eines einzelnen Anschlusses

Für frequenzunabhängige ideale Anregungs- und Empfangsvektoren ergibt sich die skalare Übertragung aus den orthonormalen Eigenvektoren $v_j$ von $T$:
$$
S(\omega)=w_{\rm rx}^{\dagger}U(\omega)w_{\rm tx}
=\sum_j(w_{\rm rx}^{\dagger}v_j)(v_j^{\dagger}w_{\rm tx})e^{i\omega\tau_j}.
$$
Bei zwei nichtverschwindenden Projektionen kann das Spektrum Informationen über beide Laufzeiten tragen. Ist das Gewicht einer Mode null, kann ihr Laufzeitwert aus dieser Übertragung nicht bestimmt werden.

Betrachtet man allein eine Elektronenschwelle und Anschlüsse, die jeweils ausschließlich an dieselbe Elektronenladung koppeln, gilt $D=g\,q_e q_e^{\mathsf T}$ mit $g=\gamma/m_e^2$. Dann ist $w_e$ die helle Eigenrichtung mit $\tau_{\rm hell}=g\,q_e^{\mathsf T}K^{-1}q_e$. Jede dazu orthogonale Richtung hat in diesem Modell $\tau_{\rm dunkel}=0$. Die normierte elektronische Übertragung ist allein $e^{i\omega\tau_{\rm hell}}$. Aus ihr lässt sich die modellierte Nulllaufzeit der dunklen Richtung nicht unabhängig bestimmen. Eine beliebige konstante positiv definite kinetische Mischung erhält diese Rang-eins-Grenze. Für die vollständige Matrixmessung muss die Apparatur an beiden Enden eine zweite unabhängige Richtung wirksam ansprechen. Eine formal unabhängige Ladung allein belegt noch keine technische Realisierung.

## Rechenkontrollen

[Wolfram Language](op5_j_sende_empfangsports.wl) prüft die exakte Normierung für $K_{11}=K_{22}=1$, $K_{12}=1/4$ und $q_e=(1,-2)^{\mathsf T}$. Der Modellwert für die helle Laufzeit beträgt $32g/5$. Bei der hypothetischen zweiten Ladung $(1,0)^{\mathsf T}$ ist die Gram-Determinante positiv. Der Ähnlichkeits- und der Polynomrest werden mit festen invertierbaren Anschlüssen und symbolischer Streckenmatrix berechnet. Die tatsächliche Print-Ausgabe lautet

```text
K eigenvalues = {3/4, 5/4}
electron K^-1 norm squared = 32/5
normalized generalized characteristic polynomial = -1/5*((32*g - 5*t)*t)
rank one electron port = 1
two-port Gram determinant = 64/15
similarity residual = {{0, 0}, {0, 0}}
characteristic polynomial residual = 0
```

Der separate Rückgabewert der Wolfram-Auswertung war `Null`.

[Qiskit](op5_j_sende_empfangsports_qiskit.py) simuliert dieselbe ideale Zweimodenübertragung als Ein-Qubit-Unitary bei relativer Phase $\pi/3$. Die Phase wird aus der komplexen Überlappungsamplitude gegenüber A bestimmt. Die sehr kleine Elektron-zu-Dunkel-Wahrscheinlichkeit ist numerisches Rundungsrauschen. Ein idealer Basiszustand hat dagegen bei der Auslese in der kanonischen Feldbasis eine messbare simulierte Konversion. Tatsächliche Python-Ausgabe

```text
electron channel phase [rad] = 1.047197551197
dark channel absolute phase [rad] = 0.000000000000
electron -> dark probability = 5.811e-33
basis 0 -> basis 1 probability = 0.191406250000
```

Offen bleiben der physische Ursprung der vorausgesetzten Kopplungen, die unabhängigen Ladungsantworten realer Anschlüsse und deren Stabilität beim Profilwechsel. Das Dirac-Schwellenmodell gilt nur unter seinen Niederenergie- und Massenannahmen. H96 bleibt offen.
