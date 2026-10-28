# OP5: Triadischer Stress, gemeinsamer Ruheframe und absolute Energie

Datum: 2026-10-26. Basis: a97e32d25b4b66ec2d534bdbc142df7b51883057.
Status: analytische bedingte Resultate. Native Closure, Gesamtwirkung und
kosmologische Konstante sind damit nicht bestimmt.

## 1. Ziel und bereits vorhandene Grundlage

Die modale Energiebilanz in `OP5_Triadic_Joint_Energy.md` genügt allein
nicht zur Bestimmung eines Raumzeit-Beobachters. Der nächste Test soll
einen wirklich ausgewerteten Tensor statt bloßer Modengewichte benutzen.

Eine geeignete bedingte Grundlage existiert bereits in
`HC_Dirac_State_Gravity.md`, Abschnitte 1–3. Sie setzt einen gemeinsamen,
unabhängig variierten metrischen Rahmen, eine reelle Dirac-Wirkung und eine
konstante hermitesche interne Kopplungsmatrix M voraus. Ihr Tensor wird
hier verwendet; seine Herleitung ist kein neues Ergebnis dieser Notiz.
Die ursprüngliche native Kompensator-/Projektor-/Gauge-Dynamik ist in
diesem Vergleich nicht enthalten. Die dortige konkrete Beispielmatrix
wird nicht nachträglich als positiv umgedeutet: unten wird ausdrücklich
eine andere, positive Familie als Spezialfall untersucht.

Metrik eta=diag(-1,1,1,1), hbar=c=1, beta=diag(1,1,-1,-1),
Gamma^0=beta, Gamma^i=beta alpha_i, {Gamma^a,Gamma^b}=-2eta^{ab}.
bar(Psi)=Psi†beta. Auf einer Lösung der deklarierten Dirac-Gleichung ist

    T_mu,nu = -i/4 [bar(Psi) Gamma_mu <->partial_nu Psi
                    +bar(Psi) Gamma_nu <->partial_mu Psi].

Die Kopplungen stecken über die Gleichung und die Zustände in diesem
Tensor. Kreuzterme dürfen nicht nochmals als unabhängiger Tensor addiert
werden, wenn sie bereits in dieser Auswertung enthalten sind.

## 2. Ein vollständig ausgerechneter homogener Probe-Spezialfall

Sei M eine konstante positive hermitesche 3x3-Matrix auf dem internen
Träger, mit nichtverschwindenden triadischen Kopplungen. Wähle einen
normierten konstanten Spinor s mit beta s=s und setze

    Psi(t,x)=a(t) tensor s,   a(t)=exp(-iMt)f,   f != 0.

Dann ist i Gamma^0 partial_t Psi - M Psi=0, weil i dot(a)=Ma
und beta s=s. Alle räumlichen Ableitungen verschwinden. Ferner gilt
s†alpha_i s=0, da alpha_i den positiven und negativen beta-Unterraum
vertauscht. Einsetzen in den Tensor liefert exakt

    T_00 = a†Ma = f†Mf = rho > 0,
    T_0i = 0,       T_ij = 0,
    T^{mu nu} = rho U^mu U^nu,   U=(1,0,0,0).

Zur Vorzeichenkontrolle: Gamma_0=-beta, also
bar(Psi)Gamma_0<->partial_0 Psi=2i a†Ma.
Der Faktor -i/2 in T_00 ergibt +a†Ma. Im gemischten Term verbleibt
ein alpha_i-Erwartungswert, der verschwindet.

Damit ist U der eindeutige zukünftige normierte zeitartige Eigenvektor
des gemischten T: Sein Eigenwert ist -rho, die drei räumlichen Eigenwerte
sind null. Die positive Norm des Modenraums wird hier zusätzlich durch
die ausgewertete positive Energie dieses besonderen Zustands ergänzt.

Das ist eine lokale homogene Lösung der Probe-Gleichung auf vorgegebener
flacher Geometrie. Sie hat auf ganz R3 keine endliche Gesamtenergie und
löst bei nichtverschwindendem Stress nicht zugleich eine flache
Einstein-Gleichung ohne weitere Beiträge. Es wird keine solche gemeinsame
Lösung und keine native M16/P_C7-Realisierung behauptet.

## 3. Phasen können die Dichte ändern, ohne den Ruheframe zu ändern

Wähle M=(m-g)I+g 1 1^T, m>g>0. Mit zeta=exp(2pi i/3) sind

    f_A=(1,1,1)/sqrt(3),       rho_A=m+2g,
    f_B=(1,zeta,zeta²)/sqrt(3), rho_B=m-g.

Beide Zustände haben dauerhaft dieselben internen Populationen. Im eben
ausgewerteten Raumzeitmodell haben sie verschiedene positive Dichten,
aber denselben eindeutigen U. Die interne Zirkulation der Normströme bei
f_B ist kein räumlicher Energiefluss. Das frühere Phasen-Gegenbeispiel
beweist eine Energielücke in den Populationen, nicht automatisch eine
Verschiedenheit der Raumzeit-Ruheframes.

Die Existenz von U in diesem Fall folgt aus der homogenen räumlichen
Präparation und dem Stress. Sie folgt nicht allein aus dem Wort „Triade“
oder aus ausgeglichenen internen Modengewichten.

## 4. Exakter Beobachtertest mit einem räumlichen Fluss

Für einen allgemeinen reellen symmetrischen Tensor der Form

    T^{mu nu} = [[rho,q,0,0], [q,p,0,0],
                 [0,0,p2,0], [0,0,0,p3]]

suche U=(cosh eta,sinh eta,0,0), Z=(sinh eta,cosh eta,0,0).
U ist zeitartig normiert und U.Z=0. Kein Energiefluss in Z-Richtung
bedeutet T_mu,nu U^mu Z^nu=0, somit

    (rho+p)/2 sinh(2eta) - q cosh(2eta) = 0.

Setze s=rho+p und Delta=s²-4q². Für |s|>2|q| gibt es genau einen
zukünftigen normierten U in dieser Ebene:

    eta = (1/2) artanh(2q/s),
    rho_rest = [rho-p+sign(s)sqrt(Delta)]/2,
    p_rest   = [p-rho+sign(s)sqrt(Delta)]/2.

Der gemischte Tensor hat dort Eigenwerte -rho_rest und p_rest.
Für Delta<0 oder Delta=0 bei (s,q)!=(0,0) existiert kein zeitartiger
Eigenvektor in dieser Ebene. Im zweiten Fall wird nur eine nullartige
Grenzrichtung erreicht. Für s=q=0 ist jeder Boost in der Ebene erlaubt.
Es wurde keine Energiebedingung angenommen; insbesondere darf s<0 sein.

Volle Eindeutigkeit in 3+1 Dimensionen verlangt zusätzlich
p2 != -rho_rest und p3 != -rho_rest. Bei Gleichheit kann man den
zeitartigen Eigenvektor mit der betreffenden räumlichen Eigenrichtung
boosten, ohne den Eigenwert zu ändern. Ein eindeutiger ebener Test allein
beweist also keine volle Eindeutigkeit. Die separate algebraische Prüfung
steht in `OP5_Stress_Observer_Independent.md`.

## 5. Ein Vakuumterm bleibt für diesen Beobachtertest unsichtbar

Für konstanten C ergänze T um einen reinen Vakuumterm:

    T_new^{mu nu}=T^{mu nu}-C g^{mu nu},
    T_new^mu_nu=T^mu_nu-C delta^mu_nu.

Alle Eigenräume und deren zeitartiger Charakter bleiben gleich. Die
Eigenwerte verschieben sich gemeinsam. Im ebenen Test werden
rho->rho+C, p->p-C, p2->p2-C, p3->p3-C, q->q.
Damit bleiben s, Delta, eta und die Entartungsbedingungen unverändert.
Für jeden normierten Beobachter steigt die gemessene Dichte um C.

Im homogenen Triadenfall ist daher

    T_new = rho U U - C g,
    density_U = rho+C,   pressure_U = -C.

U ist für rho>0 für jedes C derselbe eindeutige Ruhebeobachter.
Folglich kann selbst eine perfekte Bestimmung dieses Frames C nicht
bestimmen. Dies ist eine exakte Unempfindlichkeit des Eigenraumtests,
keine Behauptung, C sei physikalisch unbeobachtbar: Es verändert die
metrische Feldgleichung. Ein veränderter selbstkonsistenter Hintergrund
kann wiederum Materiezustand und Bewegung verändern. Verglichen wird
hier zunächst derselbe punktweise Materietensor.

## 6. Warum auch die metrische Fortsetzung festgelegt werden muss

Ein zusätzlicher Unterschied kann bereits bei gleicher flacher
Probe-Dynamik auftreten. Sei F ein reeller, metrisch unabhängig gehaltener
Skalar und füge einer kovarianten Vergleichswirkung hinzu

    Delta S = xi integral sqrt(-g) R F.

Mit T_mu,nu=-2/sqrt(-g) delta S/delta g^{mu nu} ergibt Variation
unter kompakten Variationen bzw. passenden Randbedingungen

    Delta T_mu,nu = -2xi [F G_mu,nu
                          +(g_mu,nu Box - nabla_mu nabla_nu)F].

Dabei werden Variation des Volumens und zweimalige partielle Integration
der Krümmungsvariation berücksichtigt. In flacher Geometrie bleibt

    Delta T_mu,nu = 2xi (partial_mu partial_nu - eta_mu,nu Box)F.

Der Zusatz zur Wirkung und zur flachen Materiegleichung ist bei R=0
null, aber die metrische Ableitung braucht nicht null zu sein. Die flache
Divergenz des angezeigten Zusatzes verschwindet identisch durch
Vertauschen der Ableitungen. Dies ist kein neuer willkürlicher Tensor
innerhalb einer festgelegten Wirkung: Es sind verschiedene kovariante
Wirkungen, deren flache Materiegesetze übereinstimmen können.

Primärquellenkontrolle: Figueroa et al., *Lattice simulations of
non-minimally coupled scalar fields in the Jordan frame*, SciPost Phys.
15, 077 (2023), Appendix B, (B.1)–(B.4):
https://inspirehep.net/files/2fc7740683cadf924893c51786d4dcdb
Die dortige Konvention ist -xi_source phi² R/2; mit
xi F=-xi_source phi²/2 stimmt das Vorzeichen überein. Übernommen wird
nur die Variationsidentität, keine skalare Ersatztheorie für die Probe.

Als lokaler diagnostischer Jet F=F0+a t x ist Box F=0 und
Delta T_01=2xi a, also Delta T^{01}=-2xi a. Damit kann eine solche
Fortsetzung auch den Flusstest ändern. Dieser Jet ist kein behaupteter
nativer on-shell-Probe-Bilinear. Falls F aus der Probe gewonnen werden
soll, müssen seine zulässigen Jets und sein Variationsgesetz erst aus
dieser Probe bestimmt werden. Für konstantes F verschwindet der flache
Zusatz; dieses Gegenargument betrifft dann gerade nicht diesen Fall.

## 7. Ergebnis und Fortsetzung

Erledigt ist ein echter Raumzeit-Spezialfall der bisherigen modalen
Triade: Die gemeinsame Energie ergibt einen expliziten Tensor mit
eindeutigem Ruheframe. Ebenfalls erledigt sind der allgemeine ebene
Flusstest und seine Grenzen in 3+1 Dimensionen. Alle Resultate sind auf
die angegebenen Hypothesen beschränkt.

Die Behauptung, eine neutrale Framewahl könne allein den absoluten
Vakuumbeitrag bestimmen, ist durch die Familie T-Cg widerlegt. Die
Behauptung, der flache Generator bestimme ohne weitere Angaben die
metrische Antwort, scheitert in der größeren Klasse mit RF-Kopplungen.
Keines dieser Ergebnisse widerlegt eine zusätzliche native Auswahlregel.

Die native Route bleibt offen: realer Wirkungs-/Adjungiertenvertrag,
erlaubte metrische Abhängigkeiten und tatsächliche gemeinsame
M16/P_C7/Probe-Zustände müssen identifiziert werden. Erst danach sind
Rückkopplung und ein räumlich variierender triadischer Stress zu lösen.
Die vorliegende positive Vergleichsmatrix und die RF-Erweiterung sind
keine neuen Postulate für das Manuskript. OP5 bleibt offen.

Prüfung: direkte Dirac- und Tensor-Einsetzung, Phaseneigenzustände,
Lorentz-Kontraktionen und alle Diskriminanten-Grenzfälle; separate
unabhängige Algebra und Abgleich mit der Primärquelle. Keine numerische
Vollfeldlösung oder neue empirische Aussage wird beansprucht.
