# OP5: Gauss-Hindernis für Folgen von Feldoperationen

19. November 2026. Analytische Erkundung mit vollständiger Induktion. OP5/T9 in einem festen Materie-Chart. [PR #198](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/198) zeigte das Gauss-Hindernis für die einzelne [Umkehrwalze](W2_Port_Dipol.md). Hier wird geprüft, ob eine beliebig lange Komposition der dokumentierten Vierteldrehung und Konjugation den geladenen Zustand erhalten und zugleich die beiden räumlichen Feldparitäten vertauschen kann. Die [Kramers-Prüfung](W2_Kramers_Dipol.md) und der [Frame-Abgleich](W2_Frame.md) bilden den Bezug zum stationären Dipol. Die Rechnung betrifft die flache J-Maxwell-Reduktion mit einer lokal nichtverschwindenden elektrischen Quelle und ohne magnetische Quelle.

## Vollständige Induktion über die Wortlänge

Auf $(E_J,B_J)$ wirken $R:(E,B)\mapsto(-B,E)$ und $K:(E,B)\mapsto(E,-B)$. Es gilt $R^4=K^2=1$, $KR=R^{-1}K$ und $J_B=RK$. Die räumliche Parität ist $\mathsf P=\operatorname{diag}(-1,1)$ zusammen mit $x\mapsto-x$.

**Induktionsbehauptung.** Jedes Wort der Länge $n$ in $R,K$ hat nach Anwendung auf das Feld die Form $R^aK^b$ mit $a\in\mathbb Z/4$, $b\in\mathbb Z/2$. Die Parität von $a$ stimmt mit der Anzahl der Vierteldrehungen modulo zwei überein.

**Anfang.** Das leere Wort hat $a=b=0$.

**Schritt.** Fügt man links $R$ an, wird $a$ zu $a+1$ und $b$ bleibt. Fügt man links $K$ an, gilt $KR^aK^b=R^{-a}K^{b+1}$. $R$ kippt die Parität von $a$, $K$ erhält sie. Damit gilt die Behauptung für alle endlichen Wortlängen. Inverse Generatoren erfordern keine neuen Fälle, da $R^{-1}=R^3$ und $K^{-1}=K$.

Da die Argumentreflexion mit den konstanten Feldmatrizen kommutiert, gilt $\mathsf P R^aK^b=(-1)^a R^aK^b\mathsf P$. Genau die Wörter mit ungeradem $a$ vertauschen also die beiden Feldparitäten.

## Lokale Quellbilanz für jedes Wort

Der zugehörige Gauss-Vektor ist $(\nabla\cdot E_J,\nabla\cdot B_J)=(g_J\rho_J,0)$. Die konstanten Matrizen wirken auf ihn genauso wie auf die Felder. Für gerades $a$ bleibt der Vektor auf der elektrischen Achse, möglicherweise mit umgekehrtem Vorzeichen. Für ungerades $a$ liegt er auf der magnetischen Achse. Wo $\rho_J\ne0$ ist, scheitert dann die magnetische Gauss-Gleichung. Dasselbe lässt sich an einer geschlossenen Fläche um genau einen Fokus prüfen, auch wenn die Gesamtladung des Paars null ist.

Damit fällt jedes paritätsvertauschende Wort aus der glatten elektrisch geladenen W1-Feldklasse. Die geraden Wörter sind lediglich **mit der magnetischen Gauss-Bedingung verträglich**. Ob sie den vollen Materiezustand und sämtliche dynamischen Gleichungen erhalten, folgt aus dieser Prüfung nicht. Bereits der erste Vierteldrehungsschritt eines physisch ausgeführten Wortes verlässt die Feldklasse, sofern die lokalen Quellen zu diesem Zeitpunkt noch vorhanden sind.

## Über die acht diskreten Feldmatrizen hinaus

Das Hindernis gilt auch für jede invertierbare konstante reelle lineare Mischung $M$ auf dem elektrischen und magnetischen Doppelindex, die den Raum durch $M$ selbst abbildet. Paritätsvertauschung verlangt $\mathsf PM=-M\mathsf P$ und damit eine rein antidiagonale Matrix. Die elektrische Quellenachse bleibt nur dann in der elektrischen Achse, wenn $M_{21}=0$. Eine antidiagonale Matrix mit $M_{21}=0$ ist singulär. Sie vernichtet außerdem den elektrischen Quellvektor. Somit kann auch eine allgemeine invertierbare konstante Mischung nicht gleichzeitig die Feldparitäten vertauschen und die elektrische Quellenachse erhalten.

Eine Folge mit einer Portprojektion $(1\pm J_B)/2$ ist auf dem ursprünglichen Doppelträger nicht invertierbar. Sie kann deshalb dort nicht als Symmetrie dienen, die beide Paritätsräume bijektiv vertauscht. Operatoren auf einem erweiterten Zustandsträger, ortsabhängige Feldabbildungen und eigenständige Transformationen der Materie sind von der Rechnung nicht erfasst.

## Ergebnis

Die Induktion schließt beliebig lange Folgen der dokumentierten Operationen als Umgehung des lokalen Gauss-Hindernisses aus. Für eine native Paritätsvertauschung bleibt ein anderer physischer Träger oder eine Wirkung mit zusätzlichen Quellen nötig. Eine solche Erweiterung müsste weiterhin den gebundenen Hamiltonoperator erhalten und einen nichtverschwindenden B−L-Dipolmatrixeintrag liefern. I1 bleibt bedingt, I3 braucht eigenständige Überschussdynamik. Native Randwirkung und H96 bleiben offen.
