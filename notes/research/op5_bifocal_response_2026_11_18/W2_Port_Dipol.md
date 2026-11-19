# OP5: Vertauscht die Umkehrwalze die physikalischen Paritätsräume?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im Materie-Ruhesystem. Die [Kramers-Prüfung](W2_Kramers_Dipol.md) ließ eine zusätzliche Symmetrie offen, die entgegengesetzte Paritäten bei gleicher Energie verbindet. Hier wird rückwärts geprüft, ob die vorhandene Umkehrwalze diese Rolle übernehmen kann. Grundlage sind die [Definition von J_B in r02](../v4_9_0_r01_r16/rounds/v490_r02_round.tex), die [Korrektur der Frame-Abbildungen in r51](../v4_10_0_r48_r55/rounds/v490_r51_round.tex), die [OP5-Operationsübersicht](../op5_operations_inventory_2026_11_06.md) und die [B−L-Frameprüfung](W2_Frame.md).

## Auf freien Feldamplituden stimmt die Paritätsalgebra

Schreibe das elektromagnetische Doppelfeld als $z=E+iB$. $J_B z=i\bar z$ bedeutet $(E,B)\mapsto(B,E)$ an einem Zeitschnitt. Es ist eine reell-lineare Involution mit $J_B^2=1$. Die räumliche Parität wirkt auf das polare elektrische und das axiale magnetische Feld als

$$
(\mathsf P z)(x)=-\bar z(-x).
$$

Daraus folgen

$$
(\mathsf P J_Bz)(x)=i z(-x),\qquad
(J_B\mathsf Pz)(x)=-i z(-x).
$$

Die beiden Operationen antikommutieren auf diesem reellen Feldträger. Damit vertauscht $J_B$ seine beiden räumlichen Paritätseigenräume. Der Vorzeichenfaktor ist die Umkehrung des Feldes, das hier als reelle Amplitude behandelt wird. Er ist keine Identifikation zweier Quantenstrahlen. Die reine Konjugation $z\mapsto\bar z$ kommutiert dagegen mit $\mathsf P$, während die Tachyon-Vierteldrehung $z\mapsto iz$ ebenfalls antikommutiert. Das ist eine algebraische Aussage auf freien Doppelamplituden. Sie bestimmt weder einen Spektralprojektor des geladenen Zweikörpersystems noch einen Dipolmatrixeintrag. Eine einzelne Portprojektion $(1\pm J_B)/2$ ist zudem eine Projektion und kein invertierbarer Symmetrieoperator.

## Die Gauss-Bedingungen sperren dieselbe Operation bei geladenen Foki

Übertrage die freie Operation versuchsweise auf das J-Maxwell-Feld der [W1-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md). In der geprüften flachen statischen Reduktion gilt

$$
\nabla\cdot E_J=g_J\rho_J,\qquad \nabla\cdot B_J=0 .
$$

Die zweite Gleichung folgt für das glatte Feld aus der Bianchi-Identität. Unter dem Tausch $E'_J=B_J$, $B'_J=E_J$ wäre

$$
\nabla\cdot E'_J=0,\qquad \nabla\cdot B'_J=g_J\rho_J.
$$

Damit verlässt jeder Zustand mit lokal nichtverschwindender elektrischer J-Quelle die zulässige W1-Feldklasse. Eine Zeitspiegelung oder eine Vorzeichenkonvention der Vierteldrehung ändert dieses Hindernis nicht. Das Argument braucht keine Aussage über die Transformation der Materie; die magnetische Gleichung allein scheitert.

Auch ein insgesamt neutrales Paar entgegengesetzter J-Ladungen hilft nicht. Eine geschlossene Fläche um genau einen getrennten Fokus trägt elektrischen Fluss $g_J Q_i$ und magnetischen Fluss null. Nach dem Tausch hätte dieselbe Fläche magnetischen Fluss $g_J Q_i\ne0$. Auf der Außendomäne ohne die Foki kann die Punktabbildung zwar weiterhin die lokalen quellenfreien Gleichungen erfüllen. Ihr getauschtes Feld lässt sich aber nicht als glatte magnetisch quellenfreie W1-Lösung durch diesen Fokus fortsetzen. Die Gesamtfläche um beide Foki verdeckt das Problem, weil sich dort die beiden Flüsse additiv aufheben.

## Welche Erweiterung dafür fehlen würde

Eine Theorie mit elektrischen und magnetischen Quellen könnte die beiden Gauss-Gleichungen unter einem entsprechenden Quellentausch untereinander abbilden. Für OP5 wären dann eine Wirkung auf beide Zustandsträger, ihre End- und Randbedingungen und ein Kommutator mit dem vollständigen gebundenen Hamiltonoperator nachzuweisen. Erst danach wäre zu prüfen, ob der physische B−L-Dipol zwischen den entarteten Paritäten einen nichtverschwindenden Matrixeintrag hat. Der [elektroschwache Vergleich](W2_Z_Strang.md) hat magnetische Enddaten in einem anderen Eichkanal. Er liefert keine magnetische J-Quelle und keine Gleichsetzung von J-Fluss und B−L-Dichte.

Somit ist die freie Paritätsvertauschung mathematisch vorhanden, aber sie kann auf dem konkreten elektrisch gebundenen Fokuszweig nicht durch die dokumentierte Feldoperation fortgesetzt werden. Eine andere Wirkung der Umkehrwalze auf den gebundenen Materieträger ist im geprüften Bestand nicht hergeleitet. Native Randwirkung und H96 bleiben offen. I1 bleibt bedingt und I3 braucht eigenständige Überschussdynamik.
