# OP5: Können chirale Z-String-Nullmoden B−L im Kern tragen?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im gemeinsamen Materie-Ruhesystem. Der [Endzonenvergleich](W2_Z_Endzonen.md) lässt eine stabilisierende Quelle im Strangkern als Alternative offen. Geprüft wird hier die lineare Besetzung der chiral propagierenden Dirac-Nullmoden eines statischen, entlang seiner Achse translationsinvarianten Z-Strings. Die [elektroschwache Referenz](W2_Neutralstroeme.md) wird durch den unabhängigen, masselosen [J-Maxwell-Kanal](W2_J_Eichkanal.md) ergänzt. Es gibt keine äußeren Rückströme, Abschirmung oder zusätzliche Beiträge zu den integrierten Ladungen und Strömen.

## Ladungsbilanz der beiden Laufrichtungen

Im Einheitswirbel laufen Up-Quarks und Dirac-Neutrinos in einer Richtung, Down-Quarks und geladene Leptonen in der anderen. Dies entspricht der entgegengesetzten Windung der beiden Yukawa-Massenterme. Die Richtung der Achse sei so gewählt, dass der erste Block Geschwindigkeit $+1$ hat. Die Besetzungsrechnung nimmt normalisierbare Moden und, soweit ein Neutrino einbezogen wird, eine nichtverschwindende Dirac-Yukawa-Masse an. Fehlt die Neutrinomode, ist ihre Dichte auf null zu setzen. [Laufrichtungen](https://arxiv.org/abs/hep-ph/9411375), [Dirac- und Majorana-Fälle](https://arxiv.org/abs/2402.19417).

Seien $u,d,\nu,e_\ell$ die signierten Teilchenüberschüsse pro Länge, mit Farben und gegebenenfalls Familien summiert. Teilchen und Löcher einer linearen chiralen Mode tragen den gleichen Geschwindigkeitsfaktor in der Beziehung zwischen Strom und signierter Dichte. Definiere die integrierten Ladungen ohne Eichkopplungen durch $N_J=u+d+\nu+e_\ell$ und $N_Q=2u/3-d/3-e_\ell$. Die entsprechenden longitudinalen Ströme sind $I_J=u+\nu-d-e_\ell$ und $I_Q=2u/3+d/3+e_\ell$. Für die globale Ladung und ihren Strom folgt direkt

$$
N_{B-L}=2N_Q-I_J,\qquad
I_{B-L}=2I_Q-N_J .
$$

Die Identitäten gelten auch, wenn mehrere Familien mit denselben Gewichten und Laufrichtungen addiert werden. Ein Modell mit massiven gebundenen Moden, einer Mischung der Laufrichtungen oder anderen Ladungsquellen hat diese lineare Zuordnung im Allgemeinen nicht.

## Endliche Maxwell-Energie verlangt vier verschwindende Momente

Für einen unabhängigen masselosen Maxwell-Kanal mit kanonisch normierten Feldern seien $q$ die physische Ladung pro Länge und $i$ der physische Längsstrom. Auf einem großen Kreis mit Radius $r$ haben der radiale elektrische Fluss und die magnetische Zirkulation die Integrale $q$ bzw. $i$. Mit Cauchy–Schwarz auf dem Kreis ist die Energie pro Länge in einem quellenfreien Ring zwischen $r_0$ und $L$ mindestens

$$
\mathcal T_{\rm Ring}\ge
\frac{q^2+i^2}{4\pi}\log\frac{L}{r_0}.
$$

Zylindersymmetrie ist für diese Schranke entbehrlich. Für glatte lokalisierte Profile mit Ausläufern gilt dieselbe logarithmische Schlussfolgerung, wenn die eingeschlossenen Momente gegen nichtverschwindende Werte konvergieren. Mit zwei unabhängigen Kanälen addieren sich die positiven Beiträge. Die physisch normierten Momente sind $(q_{\rm em},i_{\rm em})=e(N_Q,I_Q)$ und $(q_J,i_J)=g_J(N_J,I_J)$ mit $e,g_J>0$. Endliche Energie pro Länge für einen unendlich ausgedehnten geraden Strang erzwingt darum $N_Q=I_Q=N_J=I_J=0$.

Damit verschwinden $N_{B-L}$ und $I_{B-L}$. Die Bedingung ist sogar quantitativ: Bei kompaktem Querschnitt liefert ein weiteres Cauchy–Schwarz

$$
\mathcal T_{\rm Ring}\ge
\frac{N_{B-L}^2+I_{B-L}^2}
{4\pi(4/e^2+1/g_J^2)}\log\frac{L}{r_0},
$$

denn $N_{B-L}=2q_{\rm em}/e-i_J/g_J$ und $I_{B-L}=2i_{\rm em}/e-q_J/g_J$. Im Ein-Generationen-Modell verschwinden unter den vier Neutralitätsbedingungen auch alle vier aggregierten Besetzungsdifferenzen: Ladung und Strom trennen die beiden Laufrichtungen, und innerhalb jeder Richtung haben die beiden Arten unterschiedliche elektrische Ladungen. Verborgene Differenzen zwischen Familien oder Farben gleicher Ladung bleiben möglich. Sie tragen zu den beiden aggregierten B−L-Momenten nichts bei.

## Grenze für OP5

Dieser Dirac-Nullmodensektor kann einen unendlichen Strang mit endlicher positiver Energie pro Länge nicht zugleich mit einem signierten B−L-Überschuss oder B−L-Strom beladen. Die Aussage verbietet keine Neutralbesetzung mit Energie und entscheidet nicht deren Einfluss auf die negative bosonische Mode. Auch ein endliches Segment kann Fluss und Strom über Rückwege, zusätzliche Moden oder Endpunkte schließen. Dafür sind die Beiträge der Rückwege und ihre Wirkung auf die Stabilität gesondert zu berechnen. Eine aus W2 abgeleitete Kopplung an die Foki und H96 bleiben offen. I3 braucht weiterhin eine eigenständige Überschussdynamik.
