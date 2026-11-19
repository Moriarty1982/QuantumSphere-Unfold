# OP5: B−L aus neutralen elektroschwachen Strömen

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im gemeinsamen statischen Materie-Ruhesystem. Geprüft wird eine Dirac-Generation einschließlich $\nu_R$, ohne Majorana-Masse. Die elektroschwachen Gleichungen unten sind eine zusätzliche Standardmodell-Referenz auf Baumebene.

## Rückwärtssuche und Wirkungsabgleich

Der [J-Eichkanal](W2_J_Eichkanal.md) und der [Higgsradius](W2_Higgsquelle.md) können gemeinsam unverändert bleiben, wenn der $B-L$-Dipol sein Vorzeichen wechselt. Die [Ladungsprüfung](W2_Ladung.md) liefert einen globalen Strom, die [Frame-Prüfung](W2_Frame.md) begrenzt dessen M/T-Deutung, und die [Sondenform](Sondenform.md) setzt getrennte Signale voraus. Gegenüber dem eingefrorenen Modell der [OP5-Anleitung](../../anleitungen/op5-vergleichsmodell-rechnen.md) betrifft diese Rechnung eine andere Wirkung und eine andere Auslese.

Die ausgeschriebene [W1-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) variiert ein $J$-Maxwell-Potential. Der [W2-Aufbau](../v4_10_0_r82/Wirkung_W2_Higgs.md) ergänzt das Higgsdublett und Yukawa-Monomiale mit elektroschwachen Quantenzahlen. Er schreibt keine unabhängig variierten Photon- und Z-Neutralfelder mit ihren beiden Quellgleichungen aus. Die folgenden Standardmodellströme prüfen deshalb, welche Information eine solche Ergänzung enthalten könnte. Die Konvention für den Z-Strom folgt [PDG, Electroweak Model and Constraints on New Physics, Gl. 10.2 und 10.6](https://pdg.lbl.gov/2023/reviews/rpp2023-rev-standard-model.pdf).

## Lokale Rekonstruktion aus zwei Vektorquellen

Sei $d_i$ die signierte Teilchendichte der Dirac-Art $i$ mit Farben in der Quarksumme. Für $i=(u,d,\nu,e)$ sind die Gewichte

| Gewicht | $u$ | $d$ | $\nu$ | $e$ |
|---|---:|---:|---:|---:|
| $Q_i$ | $2/3$ | $-1/3$ | $0$ | $-1$ |
| $t_i=T_{3L}$ | $1/2$ | $-1/2$ | $1/2$ | $-1/2$ |
| $(B-L)_i$ | $1/3$ | $1/3$ | $-1$ | $-1$ |

Im Vektorteil ist das Z-Gewicht $t_i/2-s_W^2Q_i$ mit $s_W=\sin\theta_W$ und $g_Z=g/\cos\theta_W$. Die gesamte fermionische Z-Quelle enthält außerdem einen axialen Strom. Für spinunpolarisierte ruhende Quellen mit verschwindender axialer Dichte ist die gemessene zeitliche Fermionquelle gleich ihrem Vektorteil. Schreibe

$$
\rho_\gamma=e\sum_i Q_i d_i,\qquad
\rho_Z^V=g_Z\sum_i(t_i/2-s_W^2Q_i)d_i.
$$

Es gilt artenweise $(B-L)_i=2(Q_i-t_i)$, folglich

$$
\rho_{B-L}=(2-4s_W^2)\frac{\rho_\gamma}{e}-4\frac{\rho_Z^V}{g_Z}.
$$

Dies liefert die lokale signierte Dichte bei separat verfügbaren und kalibrierten fermionischen Vektorquellen. Für polarisierte Quellen ist der axiale Anteil getrennt zu bestimmen. Auf ein festes Materie-Ruhesystem beschränkt bleibt auch die Vorzeichenkonvention klar: Die Kombination bildet globale Ladung ab. Sie erzwingt keine Umkehr unter $z\mapsto iz$.

## Außenfelder reichen im allgemeinen Quellenraum nicht

Betrachte zur Kontrolle die linearen statischen Gleichungen auf $\mathbb R^3$ bei konstantem Vakuum-Higgswert, ohne geladene Bosonhintergründe und mit abklingenden Feldern. In dieser Reduktion erfüllen die Potentiale $-\Delta A_0=\rho_\gamma$ und $(-\Delta+m_Z^2)Z_0=\rho_Z^V$. Im Quellgebiet kann man die Formel oben mit den beiden Differentialoperatoren verwenden. Am Rand außerhalb des Quellgebiets sind beide rechten Seiten bereits null. Es bleibt zu prüfen, ob die Randfelder das gewöhnliche Dipolmoment trotzdem eindeutig festlegen.

Wähle einen glatten, kompakten Test von der Form $\chi=\partial_{x_1}\eta$, wobei $\eta$ im Inneren getragen ist und ein nichtverschwindendes Integral hat. Setze $\rho_\gamma=0$ und $\rho_Z^V=(-\Delta+m_Z^2)\chi$. Die abklingende Lösung ist $A_0=0$ und $Z_0=\chi$. Außen verschwinden beide Potentiale und sämtliche Ableitungen. Dennoch ist

$$
\int x_1\,\rho_{B-L}\,d^3x
=-\frac{4m_Z^2}{g_Z}\int x_1\chi\,d^3x
=\frac{4m_Z^2}{g_Z}\int\eta\,d^3x\ne0.
$$

Der Laplace-Anteil trägt wegen $\Delta x_1=0$ und kompaktem Träger nichts zu diesem Moment bei. Zudem ist die Gesamtladung null. Der Vorzeichenwechsel $\chi\mapsto-\chi$ kehrt das Moment um und hält die Außenfelder fest.

Das Beispiel ist mit den Dirac-Gewichten verträglich. Für $(d_u,d_d,d_\nu,d_e)=(0,3,-2,-1)f$ gilt $\rho_J=\rho_\gamma=0$, $\rho_Z^V=-g_Z f$ und $\rho_{B-L}=4f$. Wähle $f=-(-\Delta+m_Z^2)\chi/g_Z$. Hinreichend kleine Amplitude und gleiche artspezifische Besetzungssummen halten die Besetzungen zulässig und die radiale fermionische Higgsquelle beim Vorzeichenwechsel fest. Diese Konstruktion benutzt frei vorgegebene glatte Quellen. Sie beweist die Mehrdeutigkeit äußerer Messungen in dieser Klasse. Eine zusätzlich begründete Einschränkung auf bekannte starre Fokusprofile kann die inverse Aufgabe ändern. Rückreaktion auf Higgs, Geometrie und Randbewegung liegt außerhalb der linearen Kontrolle.

## Konsequenz

Eine zweite Ladungsprojektion ist im Standardmodell-Vergleich lokal verfügbar. Für OP5 fehlen die Herleitung der beiden Neutralfeldgleichungen aus der vorgesehenen Wirkung, ein nachweislich zugänglicher Messraum oder eine physikalische Einschränkung der Quellen sowie eine Formkraft aus derselben Wirkung. Die lokale Stromidentität setzt keinen Randterm fest. I3 braucht weiterhin eine eigenständige Überschussdynamik. OP5 und H96 bleiben offen.
