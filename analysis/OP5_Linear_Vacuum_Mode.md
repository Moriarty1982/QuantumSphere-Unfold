# OP5: Vakuumempfindlicher Störungskanal und Schutz durch Closure

2026-10-26. Fortsetzung der Notiz OP5_Affine_Vacuum_Response.md.
Letzter in dieser Unterhaltung bestätigter Git-Stand: a97e32d.
Der aktuelle Git-Stand konnte im jetzigen Zugriffskontext nicht erneut
gelesen werden; die tatsächlich gelesenen Quelldateien werden separat
mit SHA-256 festgehalten. Neue Ergebnisse liegen im Arbeitsordner dieser
Unterhaltung, nicht im Repository.

## 1. Fragestellung und genauer Bereich

Die vorige Rechnung bewies eine Familie identischer Hintergründe für
beliebige konstante Vakuumdichte rho_v im ausdrücklich alternativen
affinen Parent-Modell. Sie bewies auch eine rho_v-abhängige zweite
Variation, aber keine Instabilität. Jetzt wird ein echter linearer
Dynamikkanal einschließlich aller übrigen linearen Feldgleichungen
ausgewertet. Es ist NICHT das vollständige Stabilitätsspektrum aller
Störungen um den räumlich variierenden gekrümmten Hintergrund.

Quellen im Repository QuantumSphere-Unfold:
- analysis/HC_Two_Frame_Action_Bridge.md, Wirkung (12), Lösung (13),
  Multiplikatorreaktion (8).
- analysis/OP5_Affine_Vacuum_Response.md samt unabhängiger Prüfung.
- analysis/OP5_Common_Operator_Representation.md und
  analysis/OP5_Spinor_Separation_And_Dirac_Limit.md für den internen
  C7-Projektor und die deklarierte Spinorfaktorisierung.

## 2. Konstanter Unterfall des vorhandenen Lösungszweigs

Setze b_x=b_y=0 in der vorhandenen logarithmischen Lösung, also h=h0
konstant. Dann sind E0=I+kappa h0 l n^T und g0 konstant und flach;
F_mu,nu=0. Psi0=(1,0,1,0)/sqrt(2), l=(1,0,0,1), n=(-1,0,0,1).
Die Multiplikatordichte bleibt

    lambda0_a^mu=rho_v (E0^-1)^mu_a,
    V_lambda0=-rho_v kappa h0 (K.n),
    K.n=-I+alpha_z.

Diese Felder erfüllen weiterhin die vollständigen Gleichungen des
deklarierten Parent-Modells. Die positive kinetische Zeitnorm der Probe
stammt dort vom FESTEN Referenzframe; die affine Geometrie wird nicht
nachträglich in den kinetischen Term eingesetzt.

## 3. Ein vollständig konsistenter linearer Kanal

Wähle w=(1,0,-1,0)/sqrt(2) und eine komplexe Amplitude a(t,z):

    delta Psi=a(t,z) w,
    delta h=0,   delta E=0,   delta lambda=0.

Direkte Matrixprodukte ergeben

    alpha_z w=-w,   (K.n)w=-2w,
    Psi0†K^a w=0 für alle a=0,1,2,3.

Deshalb ist delta j=0 für beliebiges komplexes a und auch
delta C=partial(delta j)/2+kappa h0 n delta j=0. Die vollständige
lineare Multiplikator-Nebenbedingung ist erfüllt. Da E,h und lambda
linear unverändert bleiben, erfüllen auch die Co-Frame- und h-Gleichung
ihre linearen Bedingungen; der Probe-Zusatz zur h-Gleichung enthält
delta j=0. Diese Prüfung geht über Stationarität einer lediglich auf
a eingeschränkten Wirkung hinaus.

Die einzige verbleibende Gleichung folgt aus der Probe-Gleichung und
ihrer Adjungierten. Mit D=rho_v kappa h0 lautet sie

    i(partial_t-partial_z)a + 2D a=0.

Für a=exp(-i omega t+i k z) ergibt sich

    omega=-k-2D.

Für reelles rho_v,kappa,h0 ist die Frequenz reell. Die allgemeine Lösung
ist a(t,z)=exp(2iDt)a_initial(z+t). Das Amplitudenprofil wird transportiert,
ohne in diesem Kanal exponentiell zu wachsen. Es relaxiert aber auch
nicht zum Hintergrund. Unter geeigneten Randbedingungen ist seine
L2-Norm in z erhalten. Die Aussage ist ein linearer 1+1-Kanal, kein
global endliches dreidimensionales Wellenpaket und kein Attraktorbeweis.

Der Frequenzterm ist mit der vorigen zweiten Variation konsistent:
Der zusätzliche quadratische Lagrange-Term ist +2D |a|². Zusammen mit
dem symmetrisierten kinetischen Term liefert er genau die obige
Bewegungsgleichung. Das Vorzeichen eines Potentialterms in einer
Lorentz-Wirkung allein hätte diese Stabilitätsaussage nicht erlaubt.

Für h0=0, kappa=0 oder rho_v=0 verschwindet dieser Zusatz; aus diesen
entarteten Fällen folgt kein Schutz für den nichtverschwindenden Fall.
Eine zeitabhängige Umphasung kann den Term aus der Darstellung dieses
isolierten Kanals verschieben, muss dann aber alle gekoppelten Kanäle
und Ausleseoperatoren mittransformieren. Sie ist keine Berechnung oder
Beseitigung eines absoluten gravitativen Energiebeitrags.

## 4. Warum das keine allgemeine Spinorstabilität ist

Transversale Ableitungen erzeugen alpha_x w und alpha_y w. Diese liegen
nicht im eindimensionalen w-Kanal. Die Wahl a(t,z) ist daher wesentlich;
ein räumlich lokalisiertes 3D-Paket benötigt weitere Kanäle und kann
zusätzlich Geometrie- und h-Störungen anregen. Auch der gekrümmte
Hintergrund h(x,y) wurde in dieser linearen Lösung nicht behandelt.

Das genaue Resultat ist: mindestens ein zulässiger linearer Kanal des
vollen vereinfachten Parent-Systems trägt den konstanten Beitrag als
Frequenzverschiebung. Die stärkere Aussage einer vollständigen
Konstantenentkopplung bleibt falsch, während eine allgemeine dynamische
Instabilität weiterhin unbewiesen ist.

### 4.1 Geschlossene Erweiterung auf zwei Komponenten

Die unabhängige Rechnung liefert einen zusätzlichen vollständig prüfbaren
Schritt. Mit v=alpha_x w=(0,-1,0,1)/sqrt(2) gilt ebenfalls
Psi0†K^a v=0 für alle a. Außerdem alpha_y w=i v, alpha_x v=w,
alpha_y v=-i w und alpha_z v=v. Der Zweikomponentenraum span(w,v)
ist somit unter allen räumlichen alpha-Matrizen invariant. Für
delta Psi=a w+b v verschwindet delta j weiterhin identisch. Alle
übrigen linearen Feldgleichungen bleiben bei delta E=delta h=delta
lambda=0 erfüllt, auch für transversale Abhängigkeit.

Die beiden vollständigen linearen Probe-Gleichungen in diesem Unterraum
lauten

    i(partial_t-partial_z)a+i(partial_x-i partial_y)b+2D a=0,
    i(partial_t+partial_z)b+i(partial_x+i partial_y)a=0.

Ihr hermitescher Fourier-Hamiltonoperator ist

    H_2=-D I+k_x sigma_x+k_y sigma_y-(k_z+D)sigma_z,
    omega_+/-=-D +/- sqrt(k_x²+k_y²+(k_z+D)²).

Alle Frequenzen sind reell; in diesem erweiterten linearen Sektor gibt
es ebenfalls keine exponentielle Fourier-Verstärkung. Ein gewöhnliches
L2-Wellenpaket kann nun alle drei räumlichen Richtungen umfassen. Eine
allgemeine nichtlineare oder vollständige gekoppelte Stabilität folgt
weiterhin nicht, weil der Strom erst in erster Ordnung unverändert ist.

Im isolierten Block entfernt delta Psi=exp[iD(t-z)]chi die konstanten
Verschiebungen. Daher sind die verschobenen Frequenzen allein kein
basisunabhängiger Massenspalt und keine Messung des absoluten
Vakuumbeitrags. Die in der vorherigen Notiz bewiesene Änderung der
vollen Wirkungsfunktion unter rho_v bleibt davon getrennt.

Der Name dieses Unterraums bedeutet hier ausschließlich delta j=0.
Er ist NICHT der Kern von K.n: w bleibt gerade empfindlich für diesen
Operator, während v in dessen Kern liegt. Diese Unterscheidung ist
für den nachfolgenden Schutztest wesentlich.

## 5. Wiederherstellung eines Massenterms

In der Standard-Dirac-Faktorisierung wirkt ein skalarer Massenterm im
Hamiltonoperator als m beta. Für die verwendeten Spinoren gilt

    beta Psi0=w,   beta w=Psi0.

Die bisher konstante Hintergrundprobe bekommt deshalb für m!=0 einen
Residualterm proportional zu m w. Die Vakuumreaktion kann ihn auf
dem UNVERÄNDERTEN Hintergrund nicht aufheben, denn
V_lambda0 Psi0=0 für jedes rho_v. Das bestätigt die ältere
Massenterm-Restaurationsgrenze und zeigt ihren konkreten Spinorkanal.
Eine veränderte gemeinsame Lösung ist dadurch nicht ausgeschlossen.

Für eine interne hermitesche Massen-/Kopplungsmatrix M lautet die
entsprechende Bedingung für f tensor Psi0: M f=0. Ein beliebiger
interner geschlossener Sektor genügt nicht; erforderlich wäre auf diesem
unveränderten Nullzweig eine tatsächliche Nullmode des Massenoperators.

## 6. Exakter Test des behaupteten Schutzsektors

Definiere die SPIN-Projektoren Pi_+=(I+alpha_z)/2 und Pi_-=I-Pi_+.
Der Hintergrund liegt in Pi_+, der Störungsspinor w in Pi_-.
Diese Projektoren sind nicht der interne Meta-Septum-Projektor P_C7.

Betrachte als getrennten Operator-Kompatibilitätstest den üblichen
faktorisierten Dirac-Hamiltonoperator bei festem Impuls, mit reeller
kinetischer Impulskomponente und hermiteschem internem M:

    H=alpha_z k_z + alpha_x k_x + alpha_y k_y + beta M
       -2D Pi_-.

Dies ist keine Behauptung, die volle Parent-Rückkopplung sei für jeden
Spinor eingefroren zulässig. Geprüft wird die Erhaltung des vorgeschlagenen
Spin-Unterraums durch diese üblichen Probe-Terme. Setze

    B=alpha_x k_x+alpha_y k_y+beta M.

Alle drei Summanden antikommutieren mit alpha_z, und die verschiedenen
Summanden antikommutieren untereinander. Daher

    Pi_- H Pi_+=B Pi_+,
    B²=(k_x²+k_y²)I+M²,
    ||B psi||²=(k_x²+k_y²)||psi||²+||M psi||².

Für einen nichtverschwindenden Zustand in Pi_+ verschwindet der Übergang
genau dann, wenn k_x=k_y=0 und M psi=0. Insbesondere können sich ein
gewöhnlicher Massenterm und transversaler Impuls in diesem hermiteschen
Standardfall nicht passend wegheben. D wählt daran nichts: Der
Vakuumterm ist bezüglich Pi_+/- bereits diagonal.

Das ist eine exakte Aussage im genannten faktorisierten Operatorbereich.
Weitere nichtstandardmäßige Kopplungen, eine bewegte Spinbasis oder ein
anderer Variationsvertrag erfordern eine erneute Prüfung; sie werden
nicht als ausgeschlossene native Möglichkeiten behandelt.

Ein vorhandener konkreter Kontrollfall lässt sich ohne neue Parameter
prüfen: `HC_Dirac_State_Gravity.md` benutzt die Vergleichsmatrix

    M=[[3/5,0,4],[0,3/5,7/10],[4,7/10,3/5]].

Ihre Eigenwerte sind 3/5 und 3/5 +/- sqrt(1649)/10;
det M=-4839/500!=0. Diese bereits verwendete Matrix hat also keine
Nullmode, die den gerade beschriebenen unveränderten Schutzsektor
besetzen könnte. Das betrifft diese deklarierte Vergleichsmatrix,
nicht das bisher nicht vollständig extrahierte native M16.

## 7. Was P_C7 hier leisten kann

Wenn P_C7 intern wirkt, ist der volle Projektor P_C7 tensor I_spin.
Für P_C7 f=f gilt zugleich

    (P_C7 tensor I)(f tensor Psi0)=f tensor Psi0,
    (P_C7 tensor I)(f tensor w)=f tensor w.

Die interne Closure entfernt den empfindlichen Spinorkanal also nicht
automatisch. Ihn durch P_C7 tensor Pi_+ auszuschließen wäre eine
zusätzliche physische Einschränkung. Der eben bewiesene Erhaltungstest
zeigt, warum diese Einschränkung mit allgemeinen massiven und räumlichen
Dirac-Proben nicht verträglich wäre. Eine native nichtfaktorisierte
Realisierung bleibt gesondert zu untersuchen.

## 8. Schluss des Arbeitspakets

Fortschritt: Die frühere zweite Variation wurde in einem erlaubten
linearen Kanal in eine echte Bewegungsgleichung übersetzt. Das Ergebnis
ist eine reelle Frequenzverschiebung mit erhaltenem Amplitudenprofil,
nicht ein exponentielles Weglaufen und nicht dynamische Rückkehr.
Der Übergang zur massiven Probe hat jetzt eine ausgeschriebene
Kompatibilitätsbedingung: Der bisher abgeschirmte unveränderte Zweig
braucht eine longitudinale masselose Untermenge; interne Closure allein
liefert sie nicht.

Nächste gemeinsame Pflicht: eine veränderte Lösung mit M f!=0 und
geometrischer Rückwirkung aufbauen, statt den unveränderten Nullzweig
als geschützten massiven Sektor zu behandeln. Ob ein solcher Zweig
existiert und seinen absoluten Beitrag auswählt, bleibt offen. Ebenso
fehlen das volle gekoppelte Stabilitätsspektrum, die native affine
Geometrieherleitung und Quanten-/Renormierungsschutz. OP5 bleibt offen.

Analytische unabhängige Kontrolle des linearen Kanals und seiner
vollständigen Gleichungen: OP5_Linear_Vacuum_Mode_Independent.md.
Die Operator-Normidentität und der interne Projektortest sind direkte
analytische Ableitungen dieser Notiz; keine numerische Simulation wird
als Beweis beansprucht.
Die unabhängige Notiz wurde vollständig gelesen; auch ihr zusätzlicher
Zweikomponentenraum wurde durch direkte alpha-Matrixprodukte,
Stromkreuzterme und das charakteristische Polynom von H_2 nachgeprüft.
