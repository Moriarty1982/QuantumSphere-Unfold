# OP5: Einbettung in die triadische Kopplung

26. Oktober 2026. Lokale analytische Fortsetzung von
`OP5_Native_Closure_Block_Reduction.md`. Keine Manuskriptänderung.

## Ergebnis und präziser Status

Das im nativen Ansatz ausgezeichnete ursprüngliche Modenpaar ist unter
dem triadischen Kopplungsterm im Allgemeinen nicht invariant. Ein speziell
symmetrischer hermitescher Dreimodengenerator besitzt dagegen eine exakte
invariante Ebene, die im Allgemeinen alle drei ursprünglichen Moden mischt.
Auf dieser Ebene entsteht der zuvor betrachtete sigma_y-Generator.

Das ist eine **bedingte Einbettung in das angegebene Blockmuster**, keine
Einbettung in eine bereits gelöste native Feldgleichung. Der kleinste offene
Übergang ist die gleichzeitige Invarianz dieser Ebene unter den übrigen
nativen Generatoranteilen und der tatsächlichen Auslesung.

Quellen: `sources/research/parts/v470/10_sphaera_and_physics.tex`,
`prop:triadic-two-probe`, Definition von Omega und geordnete Mastergleichung;
`sources/research/parts/hc-dynamics-and-geometry.tex`, Abschnitt „Projection
Retains Hidden States and Moving Frames“. Endlichdimensionale Ableitungen
unten sind vollständig ausgeschrieben, ohne numerische Stichproben.

## 1. Das ursprüngliche Paar: exakter Invarianztest

Zunächst zusätzliche Voraussetzungen: feste endliche Moden, positives
gewöhnliches Skalarprodukt, hbar=1, konservative Dynamik i dot Psi=H Psi.
Die Identifikation dieses H mit dem nativen Omega-Block erfordert eine
separate Reduktion des Gamma-/Transportanteils und wird hier nicht behauptet.

Ein hermitesches Dreimodenmodell mit dem nativen Blockmuster hat die Form

    H = [[H_2,V],[V†,epsilon]],    Psi=(psi,zeta),
    V = chi (T_1perp,T_2perp)^T,    epsilon real.

Hier sind die T-Einträge skalare reduzierte Kopplungen. Für operatorwertige
Einträge wären die entsprechenden gemeinsamen invarianten Räume anzugeben.
Mit Pi=diag(1,1,0) ist das ursprüngliche Paar genau dann für alle seine
Anfangszustände invariant, wenn V†=0, also V=0. Denn bei zeta=0 ist

    dot zeta = -i V† psi.

Für einen bestimmten normierten Anfangszustand mit V†psi != 0 folgt

    p_perp(t) = t² |V†psi|² + O(t³).

Eine spezielle dunkle Richtung d in ker(V†) bleibt nur dann für alle Zeiten
dunkel, wenn H_2 d wieder in dieser Geraden liegt. Bei V != 0 ist der
Kern in zwei Dimensionen eindimensional. Das liefert höchstens eine solche
Gerade, keine vollständige geschlossene ursprüngliche Zweimodenebene.

Die generische Leckage dieses einzelnen Kopplungsterms ist kein Satz über
jede mögliche Summe nativer Terme: Zusätzliche Terme könnten Querblöcke
kompensieren. Solche Kompensation muss ausdrücklich nachgewiesen werden.

## 2. Die dritte Mode behalten statt als Dämpfung ersetzen

Für konstante Blöcke ist ihre exakte Elimination

    zeta(t) = exp(-i epsilon t) zeta(0)
              - i integral_0^t exp[-i epsilon(t-s)] V† psi(s) ds,

    dot psi(t) = -i H_2 psi(t) - i V exp(-i epsilon t) zeta(0)
                 - integral_0^t V exp[-i epsilon(t-s)] V† psi(s) ds.

Anfangsinformation und Gedächtnisterm bleiben erhalten. Eine einzelne
endliche dritte Mode ist kein hergeleitetes Markov-Reservoir. Die volle
hermitesche Dynamik bewahrt die Gesamtnorm; projizierte Verluste können
zurückkehren. Ein neutraler Mittelwert nach grober Zeitauflösung wäre ohne
weitere Argumente kein eindeutiger dynamischer Attraktor.

## 3. Ein exakter eingebetteter Kandidat mit drei aktiven Kopplungen

Wähle nun ausdrücklich den zusätzlichen symmetrischen Sektor

    H = m I + i A,
    A = [[0,-omega,-mu],[omega,0,-nu],[mu,nu,0]],
    m,omega,mu,nu real.

Dieser H ist hermitesch und passt mit entsprechend rein imaginären,
adjungierten Kopplungen in das triadische Blockmuster. Gleiche Diagonalen
und diese Kopplungsphasen sind zusätzliche Bedingungen, keine aus der
gedruckten Blockform folgenden Identitäten.

Setze a=(nu,-mu,omega)^T und Omega=sqrt(omega²+mu²+nu²)>0.
Dann ist A f = a cross f. Die Gerade entlang a ist invariant, und auch
die reelle Ebene a^perp ist invariant. Nach Entfernen der globalen Phase
exp(-i m t) lautet die volle Gleichung dot f=A f. Ihre Lösung ist eine
Rotation um a mit Winkel Omega t.

Wähle orthonormale reelle e_1,e_2 in a^perp mit e_2=(a/Omega) cross e_1.
Dann gilt A e_1=Omega e_2 und A e_2=-Omega e_1. Auf ihrer komplexen
linearen Hülle hat der Hamiltonoperator daher exakt die Darstellung

    H_plane = m I_2 + Omega sigma_y.

Damit ist der zuvor verwendete Zweimodengenerator in einen vollständig
erhaltenen Dreimodengenerator eingebettet. Die neue Ebene ist im Allgemeinen
nicht das ursprüngliche Paar: Dessen Ebene ist nur bei mu=nu=0 invariant
(für diesen Generator). Für Omega=0 fehlt eine bestimmte Rotationsachse
und es gibt keine solche nichttriviale Uhr.

Die vollen Energieeigenwerte sind m, m+Omega, m-Omega. Falls man positive
Energieeigenwerte verlangt, kann man m>Omega annehmen; die Rotation legt m
jedoch nicht fest. Auf der Ebene ist der Abstand 2 Omega. Für einen binären
Projektor auf eine reelle Ebenenachse oszillieren Wahrscheinlichkeiten mit
Winkelfrequenz 2 Omega. Reelle normierte Ebenenvektoren haben dennoch alle
den Energieerwartungswert m, weil f^T A f=0. Derselbe Energieerwartungswert
ist kein Beweis gleicher Zustände oder fehlender zeitlicher Entwicklung.

## 4. Der neue Sektor verlangt eine passende Auslesung

Sei S der orthogonale Projektor auf die neue Ebene. Das ursprüngliche
Modenobservable P_1=|u_1><u_1|, u_1=(1,0,0)^T, wird dort zu

    E_1 = S P_1 S |_plane = |S u_1><S u_1|,
    nichtverschwindender Eigenwert = 1 - nu²/Omega².

Im allgemeinen Fall 0<1-nu²/Omega²<1 ist das ein unvollständig scharfer
Effekt und kein Projektor auf eine normierte neue Modenachse. Im Grenzfall
nu²=Omega² ist E_1=0. Nur wenn nu=0 ist seine nichtverschwindende Richtung
ein scharfer Ebenenprojektor. Deshalb darf man die alten Readout-Regeln
nicht unverändert auf die neu gemischten Moden übertragen.

Mit einer physisch begründeten scharfen Ebenenauslesung und zwei geeigneten
Zeitpunkten funktioniert die vorangehende Zweiauslesungs-Rekonstruktion.
Eine solche neue Messkopplung ist jedoch nicht allein durch die Existenz
der Ebene bereitgestellt. Statische Umbenennung der Moden und tatsächlicher
Umbau einer Messapparatur sind getrennte Schritte.

## 5. Verträglichkeit mit der vollständigen nativen Gleichung

Für eine feste Ebene und den vollständigen Generator G ist der notwendige
und hinreichende endliche Invarianztest

    (I-S) G S = 0.

Für einen bewegten orthogonalen Projektor S(t), solange der Zustand im
Bereich von S liegt, lautet der Test

    (I-S) G S = dot S S.

Er folgt aus dem Ableiten von S Psi=Psi. Die Bewegung des Sektors gehört
also in die Bedingung und darf nicht als zusätzliche physische Dämpfung
ausgegeben werden. Bei einem selbstadjungierten zeitabhängigen H gelten
entsprechend diese Bedingungen mit G=-iH.

Der native G enthält zusätzlich Verbindung, räumliche Ableitungen,
Gamma-Faktoren und H_C. Für eine vollständige Einbettung sind diese Teile
zusammen zu testen. Insbesondere gilt:

- Das bisherige P im Closure-Funktional ist nicht ohne Nachweis S oder Pi.
- Omega ist nativ nicht einfach M: Es enthält m_0 I, alpha P M P,
  beta g_Y T und gamma H_C. Der frühere Modellansatz H_phys=M war eine
  zusätzliche Identifikation; die triadische Blockform hebt sie nicht auf.
- Die skalare Closure-Identität des isolierten Zweimodensektors beweist
  nicht, dass der volle H_C die neu gefundene Ebene erhält.
- Die hier verwendete positive Norm und Zeiteinheit müssen aus dem nativen
  Strom und der physikalischen Zeitnormalisierung gewonnen werden.
- Eine Probe-Gleichung auf festem Hintergrund löst noch nicht die
  Resonanz-, Closure- und Hintergrundgleichungen mit ihren Quellen.

## Konsequenz

Ein Zwei-Auslesungs-Kandidat lässt sich also in ein echtes Dreimodenmodell
einbetten, ohne die dritte Kopplung zu ignorieren. Die geschlossene Ebene
wird dabei durch die gesamte Kopplungsgeometrie bestimmt. Das gibt der Idee
einer zusammengesetzten Referenz einen präziseren bedingten Inhalt.

Es folgt weder ein eindeutiger neutraler Attraktor noch eine absolute
Vakuumenergie. Die normierte Ebenenmischung S/2 ist stationär, wird aber von
der unitären Dynamik nicht aus beliebigen Zuständen angezogen. Auch der
Achsenprojektor ist stationär, ebenso Mischungen in einer Energieeigenbasis.
Der Offset m bleibt frei. OP5 bleibt offen; ein konkreter Invarianz- und
Auslesetest ersetzt nun die freie Wahl eines abgeschlossenen Modenpaars.
