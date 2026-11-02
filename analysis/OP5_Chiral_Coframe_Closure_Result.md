# OP5: chirale Erweiterung und Coframe-Verträglichkeit
28.10.2026. Fortsetzung von Commit 337d9cb. Exakte Matrixalgebra im bisherigen Vergleichsmodell; keine OP5-Schließung.

## Vertrag
D_mu=partial_mu+i A_mu, K=(I,alpha), H=T tensor gamma5, T=diag(1,1,-1), U=exp(i chi H/2). S_AB=S_BA=1/2, Q=S tensor K. E=Re Psi† Q D Psi. Verbindung A=G tensor I mit G_AC=p, G_BC=q. Massenterm M=Y_AB tensor beta. Verbindungs- und Massenkonvention wie in den bisherigen Gegenstromprüfungen. Lokale reelle Funktion chi; regulärer Ansatzbereich vorausgesetzt.

## Allgemeine exakte Aussagen
[Q,H]=0 und QH hermitesch. Deshalb ist Re(i partial_mu chi Psi†QH Psi/2)=0: Der Winkelgradient trägt direkt nichts zur reellen Cross-Coframe bei. Bei festgehaltener Verbindung bleibt jedoch
Delta E = (i/2) Psi†[Q,U† A U-A]Psi.
Dieser Ausdruck verschwindet nicht allgemein. Das Skript enthält einen exakten Gegenfall mit Delta E=1/2.

Wegen {H,A}=0 und {H,M}=0:
U† A U=A cos(chi)+i A H sin(chi),
U† M U=M cos(chi)+i M H sin(chi).
Damit erscheinen in umgeschriebenen Gleichungen gamma5-abhängige Kopplungen. Das ist bei einer bloßen Variablenumformung keine neue Physik: Diese Terme sind vollständig durch die alten Gleichungen bestimmt. Eine aktive chirale Symmetrie der eingeschränkten Kopplungsklasse folgt daraus dagegen nicht.

Die volle kovariante Transformation der Verbindung lautet
A'_mu=U A_mu U†-(partial_mu chi)H/2.
Bloße Konjugation erhält zwar hier die reelle Coframe, aber nicht den vollständigen kovarianten Ableitungsoperator. Eine neue unabhängige axiale Verbindung darf ohne Wirkung/Herleitung nicht eingeführt werden.

## Stärkeres Resultat für unsere tatsächliche Startfamilie
Psi=(c u,d u,w), c,d reell, p=k c, q=-k d mit reellem k.
Dies trifft die bisherige Gegenstromfamilie mit c=cos(theta), d=sin(theta), k=3/(2 rho Delta).

Für diese Familie gilt bei festgehaltener ursprünglicher Verbindung:
E[U Psi,A]=E[Psi,A]
für jeden Winkel chi und jeden Winkelgradienten, solange die Beziehungen als Felder gelten und die Ausgangsableitungen entsprechend transformiert werden. Der Verbindungsbeitrag verschwindet wegen cq+dp=0 und proportionaler A/B-Spinoren.

Prüfung: Mit F(u,w)=(c u,d u,w) wurden für alle vier K die beiden Matrixidentitäten
F† (i/2)[Q,A] F=0 und F† (i/2)[Q,iAH] F=0
symbolisch nach Einsetzen p=kc,q=-kd verifiziert. Sie decken unabhängig die Koeffizienten cos(chi)-1 und sin(chi) ab. Kein numerischer Punktfit.

## Bedeutung und verbleibende Grenze
Wir können den fehlenden chiralen Winkel in der bestehenden Startfamilie zulassen, ohne dadurch allein ihre Cross-Coframe zu zerstören. Dies ist eine echte Erweiterung des kinematischen Ansatzes und stärker als die bisherige Zweipunktprüfung.

Es löst die Dynamik nicht. Frühere Fits zeigten, dass die starre Gegenstromrelation trotz chiraler Richtung einen großen Restfehler lässt. Sobald die für die vollständige Dynamik nötigen unabhängigen Entwicklungen die A/B-Proportionalität oder cq+dp=0 verlassen, ist die Coframe-Invarianz neu zu prüfen. Die veränderte Geometrie muss dann in den Operator zurückgeführt werden. Ein chiraler Winkel allein ist kein Ersatz für diese Rückkopplung.

Nächster konkreter Test: Die vollständigen Dirac-Gleichungen in der erweiterten Familie ausdrücken und prüfen, ob die Proportionalitätsbedingung und Kopplungsrelation erhalten werden können; dabei feste räumliche Daten als Kontrolle behalten und freigegebene Ableitungen ausdrücklich benennen. Nicht aus der Coframe-Invarianz auf eine neue Eichsymmetrie schließen.

## Prüfung und Dateien
OP5_Chiral_Coframe_Closure_Check.py und .json: exakte SymPy-Identitäten, allgemeiner Gegenfall und spezielle allwinkelgültige Identitäten. Unabhängige algebraische Gegenprüfung durch einen Teilagenten; entscheidende Spezialaussage anschließend lokal symbolisch nachgerechnet. Keine zeitliche Integration, kein Existenzbeweis, keine native M16/C7-Herleitung, kein Lambda-Ergebnis. Lokal gesichert; in diesem Schritt nicht committed.
