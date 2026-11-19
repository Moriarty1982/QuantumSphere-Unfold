# OP5: Schützt eine Kramers-Paarung den orientierten Dipol?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im Materie-Ruhesystem. Die [Quantendipol-Rechnung](W2_Quantendipol.md) verlangt für einen stationären Dipol bei erhaltener Parität eine passende Entartung entgegengesetzter Paritäten. Ihre Coulomb-Gegenprobe verliert diese Entartung bereits durch den abgeschirmten Higgsanteil. Hier wird geprüft, was die im [I1-Endpunktabgleich zu OP1](../op1_i1_string_endpoints_2026_11_15/README.md) erwähnte Kramers-Struktur zu dieser Bedingung beitragen könnte. Es wird keine OP1-Zählregel übernommen.

## Ein einzelnes Kramers-Dublett reicht nicht

Sei $\Theta$ eine antiunitäre **physikalische Zeitumkehr**, $\Theta^2=-1$ und $\Theta H\Theta^{-1}=H$. Die folgenden Aussagen gelten nur, wenn $\Theta$ den betrachteten Zustandsträger und seine Randbedingungen tatsächlich erhält. Für die gewöhnliche Zeitumkehr mit festen internen Ladungen ist das räumliche Dichtedipolobservable $\mathbf D=\int\mathbf x\,\rho_{B-L}(\mathbf x)\,d^3x$ zeitumkehrgerade. Das ist eine andere Operation als die Tachyon-Abbildung $z\mapsto iz$. Eine Portumkehr, die zugleich die Ladungssektoren vertauscht, müsste getrennt typisiert werden. [Frame- und Ladungsabgleich](W2_Frame.md).

Sei $\Pi$ der Projektor auf einen isolierten zweidimensionalen Energieeigenraum. In einer Kramers-Basis hat $\Theta$ bis auf Konvention die Form $i\sigma_y K$ mit komplexer Konjugation $K$. Jede hermitesche projizierte Dipolkomponente lässt sich als

$$
\Pi D_i\Pi=d_i^{(0)}\,\mathbf 1+\sum_{j=1}^3 d_i^{(j)}\sigma_j
$$

mit reellen Koeffizienten schreiben. $\Theta$ kehrt alle drei Pauli-Matrizen um. Weil $D_i$ zeitumkehrgerade ist, müssen $d_i^{(j)}=0$ für $j>0$ gelten. Beide Kramers-Partner und jede ihrer Überlagerungen haben also dieselbe Dipolerwartung. Ist zusätzlich $P$ eine erhaltene Parität und gilt $P D_i P^{-1}=-D_i$, dann kehrt $P$ innerhalb desselben Eigenraums die skalare Komponente um. Die Identität selbst bleibt unter Konjugation gleich. Daher ist $\Pi D_i\Pi=0$. Für diesen letzten Schluss braucht man keine Annahme über das relative Kommutatorverhältnis von $P$ und $\Theta$.

Falls $\Theta$ und $P$ außerdem kommutieren, haben die beiden Partner ohnehin dieselbe Parität. Die Kramers-Paarung liefert dann auch direkt kein Paar der für den [Quantendipol](W2_Quantendipol.md) benötigten Art. Ohne Parität könnte ein vom Kramers-Partner unabhängiger skalarer Dipolwert vorliegen, etwa in einem bereits orientierten Hintergrund. Er wird durch die Wahl des Partners nicht ausgewählt.

## Was vier Zustände ermöglichen und was sie schützen

Bei kommutierenden $P$ und $\Theta$ besteht ein Eigenraum mit beiden Paritäten aus mindestens zwei Kramers-Dubletts. Ein explizites Vierzustandsmodell sei $P=\tau_z\otimes\mathbf 1$ und $\Theta=(\mathbf 1\otimes i\sigma_y)K$. Die Matrizen $\tau$ wirken auf der Parität, die Matrizen $\sigma$ auf dem Kramers-Index. Dann ist für eine feste Raumkomponente $D=d\,\tau_x\otimes\mathbf 1$ mit reellem $d$ paritätsungerade und zeitumkehrgerade. Bei genau gleichem Energieniveau der beiden Dubletts kann ein präparierter Zustand einen Dipol tragen.

Der Aufspaltungsterm $\delta\,\tau_z\otimes\mathbf 1$ ist jedoch mit beiden Symmetrien verträglich. Sie schützen daher nur die innere Paarung je Parität, nicht die Gleichheit der beiden Energien. Eine eigenständige Symmetrie, welche die Paritätsräume vertauscht und tatsächlich mit $H$ kommutiert, könnte diese Lücke schließen. Auch dann muss die physische Dipolkomponente zwischen den so gepaarten Zuständen einen nichtverschwindenden Matrixeintrag haben.

## Konsequenz für den Companion

Der OP1-Endpunktabgleich verwendet die Umkehrwalze für eine Zählfrage. Er liefert keinen Schutz einer physikalischen OP5-Paritätsentartung. Selbst bei einer Übertragung als physikalische Zeitumkehr würde ein einzelnes isoliertes Kramers-Dublett im paritätserhaltenden Kontrollmodell einen Dipol von null liefern. Eine ladungsvertauschende Antiunitäre aus dem Port-Formalismus könnte eine andere Transformationsregel haben. Dafür fehlen hier der Nachweis ihrer Wirkung auf den gebundenen Zustandsträger und der zugehörige Dipoloperator. Eine native Orientierung, ein geschütztes Paritätsdublett und H96 bleiben offen. I1 bleibt bedingt, I3 benötigt eine eigenständige Überschussdynamik.
