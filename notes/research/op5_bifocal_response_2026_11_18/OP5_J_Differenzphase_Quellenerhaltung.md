# OP5: Quellenerhaltung und differentielle J-Laufzeit

20. November 2026. Analytische Erkundung in M. Der [massive Tensorvermittler](OP5_J_Massiver_Tensorvermittler.md) erzeugt eine lokale J–D-Kopplung für konservierte Quellen. Hier nehmen wir zu diesem Vergleich ein gewöhnliches elektromagnetisches Maxwell-Feld als mögliches Referenzsignal hinzu. Die [ursprüngliche W1-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) wird dabei um diesen expliziten Referenzsektor erweitert. Wir prüfen den vereinfachten konservierten Baumabgleich, ohne H96-Datenvergleich.

## Erhaltung in der geladenen sichtbaren Materie

Sei $T_O$ der Energie-Impuls-Tensor der Materie, die sowohl mit J als auch mit dem elektromagnetischen Feld $A$ Impuls austauscht. Für kanonisch normierte, minimal gekoppelte Maxwell-Felder ohne kinetische Mischung lauten die lokalen Bilanzen in flacher Hintergrundnäherung
$$
\begin{aligned}
\partial_\mu T_J^{\mu\nu}&=-F_J^{\nu\lambda}j_{J,\lambda},\\
\partial_\mu T_A^{\mu\nu}&=-F_A^{\nu\lambda}j_{A,\lambda},\\
\partial_\mu T_O^{\mu\nu}&=F_J^{\nu\lambda}j_{J,\lambda}+F_A^{\nu\lambda}j_{A,\lambda}.
\end{aligned}
$$
Die physikalischen Eichkopplungen sind in den Strömen enthalten. Der vollständige D-Tensor werde in nullter Ordnung des neuen Spin-2-Operators separat erhalten. Sei
$$
S^{\mu\nu}=g_J T_J^{\mu\nu}+g_A T_A^{\mu\nu}+g_O T_O^{\mu\nu}+g_D T_D^{\mu\nu}
$$
die Quelle eines massiven Vermittlers. Die hier verwendeten $g$ sind die dimensionierten Spin-2-Kopplungen, nicht die Maxwell-Eichkopplungen. Dann gilt
$$
\partial_\mu S^{\mu\nu}=(g_O-g_J)F_J^{\nu\lambda}j_{J,\lambda}
+(g_O-g_A)F_A^{\nu\lambda}j_{A,\lambda}.
$$
Die beiden Kraftdichten lassen sich in unabhängigen Feldkonfigurationen einzeln variieren, solange beide Wechselwirkungen vorhanden sind. Soll der gewichtete Tensor auf allen betrachteten Lösungen erhalten sein, folgen $g_J=g_A=g_O=g_V$. Die Gleichheit ist eine Bedingung an den konservierten Quellenansatz mit diesen konstanten Gewichten. Sie folgt nicht aus einer einzelnen zufällig quellfreien Wellenkonfiguration. In einer größeren Materiefeldliste wiederholt sich dieselbe Bedingung entlang unabhängiger Austauschkanäle; die Rechnung verlangt keine Gleichheit zu einem in nullter Ordnung getrennten D-Sektor.

## Folge für die Phasendifferenz

Setze $T_V=T_J+T_A+T_O$. Für mehrere massengekoppelte Pole im Sinn des [Niederenergieabgleichs](OP5_J_Massiver_Tensorvermittler.md) ist der gemischte Koeffizient $C_{VD}=\sum_i g_{Vi}g_{Di}/m_i^2$. Wegen der Spurfreiheit der beiden Maxwell-Tensoren enthält der Operator aus der Spin-2-Spurprojektion für beide Wellen jeweils dieselbe Kontraktion $C_{VD} T_I^{\mu\nu}T^D_{\mu\nu}$ für $I=J,A$. Im ruhenden, dünnen D-Hintergrund liefert der vollständige D-Tensor denselben elektrischen und magnetischen Zusatz $\zeta_J=\zeta_A=C_{VD}\rho_D$ in der Konvention der [Tensorkopplung](OP5_J_Tensorkopplung.md). Die Aussage betrifft die Wellenantwort auf den D-Hintergrund. Im selben Modell kann der sichtbare Eigenoperator einen ebenfalls gemeinsamen Beitrag von ruhender sichtbarer Materie liefern.

Für zwei idealisierte, masselose Wellen im selben Gebiet ohne weitere Mediumsterme und ohne makroskopische J- oder elektromagnetische Hintergrundfelder ergibt sich im führenden schwachen Abgleich
$$
\frac{\Delta\varphi_J}{\omega_J}
=\frac{\Delta\varphi_A}{\omega_A}
=C_{VD}\int\rho_D\,d\ell .
$$
Es wird die Phasendifferenz pro Frequenz verglichen, damit ein bloßer Frequenzunterschied keine unterschiedliche Laufzeit vortäuscht. Der gemeinsame Beitrag kann gegenüber einer separat festgelegten Geometrie oder einem Signal außerhalb dieses Wechselwirkungsverbunds weiterhin vorhanden sein. Im Vergleich von J gegen gewöhnliches Licht unter diesen Bedingungen fällt er heraus. Plasma, eigene höhere Operatoren, andere Kopplungen an Detektoren und physische Emissionszeiten sind getrennte Eingaben.

## Was bei ungleichen Gewichten zusätzlich gerechnet werden muss

Ein massives Spin-2-Feld kann formal auch an nichtkonservierte Quellen gekoppelt werden. Dann kann der einfache konservierte Abgleich nicht unverändert verwendet werden. Schematisch zeigt dies die Stückelberg-Zerlegung des linearen massiven Spin-2-Feldes,
$$
h_{\mu\nu}=\widehat h_{\mu\nu}
+\frac{\partial_\mu B_\nu+\partial_\nu B_\mu}{m}
+\frac{2\partial_\mu\partial_\nu\pi}{m^2}.
$$
Diese Wahl dient zur Kennzeichnung der Ableitungsstrukturen; kanonische Normierung und Diagonalisierung des Skalars können konstante Faktoren und einen zusätzlichen Spurterm liefern. Einsetzen in $h_{\mu\nu}S^{\mu\nu}$ und partielle Integration ergeben Beiträge proportional zu $-B_\nu\partial_\mu S^{\mu\nu}/m$ und $\pi\partial_\mu\partial_\nu S^{\mu\nu}/m^2$. Die oben berechneten Kraftdichten sind genau die Quellen dieser zusätzlichen Terme bei ungleichen Gewichten. [Hinterbichler, Stückelberg-Zerlegung des massiven Spin-2-Felds](https://arxiv.org/abs/1105.3735)

Im quellfreien Wellengebiet können diese Divergenzterme im Hintergrund verschwinden. Das begründet eine lokale Rechnung im quellfreien Gebiet, bestimmt aber keinen vollständigen Vergleich mit geladenem Sender und Empfänger. Für einen solchen Vergleich wären eine wirksame Theorie der longitudinalen Moden, ihr Gültigkeitsbereich und die Kopplung der Apparatur zu bestimmen. Die Erhaltungsschlussfolgerung ist daher bedingt, kein allgemeines Verbot nichtuniverseller massiver Spin-2-Kopplungen. H96 bleibt offen.
