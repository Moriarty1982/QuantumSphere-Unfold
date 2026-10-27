# OP5: Explizite Vakuumreaktion einer geometrischen Nebenbedingung

2026-10-26. Basis a97e32d25b4b66ec2d534bdbc142df7b51883057.
Status: exakter lokaler Lösungszweig eines bereits ausdrücklich geänderten
Vergleichsmodells; keine native Auswahl von Lambda und kein Nachweis
allgemeiner Stabilität oder quantenmechanischen Schutzes.

## 1. Zwei untersuchte Wege

Die vorherige Suche ließ zwei konkrete Fortsetzungen offen: eine
Normierung der Wirkung aus der QAM und eine zusätzliche Reaktion bei
zusammengesetzter Geometrie. Die erste wird unten an der tatsächlich
vorliegenden Zustandsnormierung geprüft. Für die zweite gibt es hier
eine explizit durch alle Feldgleichungen geprüfte Lösung, einschließlich
einer Gegenprobe außerhalb des Lösungszweigs.

Die Grundlage ist ausschließlich die alternative reelle Parent-Wirkung
(12) und die lokale Lösung (13) aus `HC_Two_Frame_Action_Bridge.md`.
Sie enthält einen festen Referenzframe, eine neutrale masslose Probe,
einen skalaren HC-Vergleich und eine affine Co-Frame-Nebenbedingung.
Sie enthält NICHT die gesamte native massive/geladene C7/M16-Dynamik.
Die Quelle dokumentiert bereits, dass deren Wiederherstellung die
unveränderte alte Lösung verletzt. Diese Einschränkung bleibt bestehen.

## 2. Präziser Wirkungsvertrag

Unabhängig variiert werden eine reelle invertierbare Co-Frame E, ein
reelles h, eine komplexe kommutierende Vierkomponentenprobe Psi und
eine reelle Multiplikatordichte lambda_a^mu. Feste Daten sind
theta=I, n=(-1,0,0,1), K^a=(I,alpha_i), kappa und kappa_eff.
Metrik eta=diag(-1,1,1,1), g=E^T eta E, v=sqrt(|det g|).

    j^a=Psi† K^a Psi,
    C^a_mu=Re(Psi†K^a partial_mu Psi)+kappa h n_mu j^a
           =partial_mu j^a/2+kappa h n_mu j^a,
    F_mu,nu=kappa[(partial_mu h)n_nu-n_mu(partial_nu h)],

    S_rhov = S_micro[Psi;theta]
       + integral d4x v [R/(2 kappa_eff)-F_mu,nu F^mu,nu/4-rho_v]
       + integral d4x lambda_a^mu(E^a_mu-delta^a_mu-C^a_mu).

S_micro ist exakt der symmetrisierte masslose Referenz-Kinetikterm der
Quelle, mit festem Referenzvolumen. rho_v ist eine beliebige reelle
konstante Dichte. Der neue Term wird VOR Variation hinzugefügt.
Variationen sind lokal kompakt getragen. Die Orientierung von E bleibt
in der betrachteten offenen Umgebung fest.

## 3. Die alte lokale Lösung und ihre neue Reaktion

Setze

    Psi0=(1,0,1,0)/sqrt(2),   l=(1,0,0,1),   j=l,
    h=log(F0+b_x x+b_y y)/(kappa_eff kappa),
    F0+b_x x+b_y y>0,
    E=I+kappa h l n^T.

Die Konstanten und gültige lokale Patchwahl sind diejenigen der alten
Konstruktion. Für eine positive h-Auswahl kann ein entsprechender
Teilpatch gewählt werden. Es gilt

    n.l=0,    l^mu partial_mu h=0,
    E^-1=I-kappa h l n^T,    v=det E=1,
    (K.n)Psi0=(-I+alpha_z)Psi0=0.

Für rho_v=0 erfüllt dieser Zweig alle Gleichungen mit lambda=0, wie
in der Quelle analytisch gezeigt. Für beliebiges konstantes rho_v bleiben
E, h und Psi unverändert; nur die Reaktionsdichte wird ersetzt durch

    lambda_a^mu=rho_v v (E^-1)^mu_a
               =rho_v(delta^mu_a-kappa h l^mu n_a).

Dies ist kein frei nachträglich subtrahierter Energiegegenbeitrag. lambda
ist ein schon im deklarierten Variationsproblem enthaltener Multiplikator,
und sein Wert muss die unabhängigen Feldgleichungen erfüllen. Genau das
wird in den folgenden Schritten geprüft.

## 4. Alle zusätzlichen Euler-Lagrange-Terme

**Co-Frame.** Die Determinantenvariation lautet

    delta v=v(E^-1)^mu_a delta E^a_mu.

Der neue geometrische Eulerterm ist somit
-rho_v v(E^-1)^mu_a. Er wird durch den neuen +lambda_a^mu in der
Co-Frame-Gleichung exakt aufgehoben. Die Multiplikatorgleichung
E-I-C=0 bleibt ebenfalls erfüllt.

**Probe und Adjungierte.** Die Quelle liefert nach partieller Integration

    -lambda.C = Psi† V_lambda Psi + Randterm,
    V_lambda=[partial_mu lambda_a^mu/2
                 -kappa h lambda_a^mu n_mu]K^a.

Auf dem Zweig gilt

    partial_mu lambda_a^mu=-rho_v kappa n_a l^mu partial_mu h=0,
    lambda_a^mu n_mu=rho_v n_a,
    V_lambda=-rho_v kappa h K.n.

V_lambda verschwindet nicht als Operator, annihiliert aber Psi0.
Der Probe-Eulerterm bleibt daher null. Da V_lambda hermitesch ist,
verschwindet die entsprechende adjungierte Gleichung ebenfalls. Diese
Unterscheidung ist für die Fluktuationsprüfung wesentlich.

**Skalar h.** Der zusätzliche Multiplikatorterm ist

    -kappa lambda_a^mu n_mu j^a=-rho_v kappa n.l=0.

Der ursprüngliche geometrische h-Term war bereits null. Der konstante
Volumenterm hat bei unabhängiger Variation von h und E keinen weiteren
h-Term. Damit sind alle zusätzlichen Feldgleichungen geprüft.

Ergebnis: Für jedes konstante rho_v existiert derselbe lokale gekrümmte
Geometrie-/Probe-Zweig mit angepasster Reaktionsdichte. Seine Krümmung
wird weiterhin vom ursprünglichen h-Profil getragen. Man darf NICHT
zusätzlich lambda=0 oder die unabhängige Einstein-Gleichung ohne
Multiplikatorreaktion verlangen; das wäre ein anderes Gleichungssystem.

## 5. Warum dies mehr ist als det E=1 auf einem Ansatz

Einsetzen eines volumenerhaltenden Ansatzes vor der Variation kann
fehlende Normalgleichungen verdecken. Hier wurde hingegen zuerst die
vollständige Wirkung mit unabhängigem E variiert. Anschließend wurden
sämtliche zusätzlichen Reaktionen auf Probe, h und E ausgewertet.
Erst ihre gemeinsamen Nullstellen erlauben die Schlussfolgerung.

Äquivalent kann man die Nebenbedingung eliminieren: E=I+C[Psi,h].
Die volle erste Variation von V4[Psi,h]=integral v(E[Psi,h]) verschwindet
auf dem geprüften Zweig für beliebige kompakt getragene Probe-/h-
Variationen. Das folgt aus der gerade ausgewerteten Kettenregel,
nicht daraus, dass V4 auf der kleinen Ansatzfamilie konstant ist.

## 6. Gegenprobe: Auch normierte Fluktuationen sehen rho_v

Wähle den konstanten normierten orthogonalen Spinor

    w=(1,0,-1,0)/sqrt(2),   K.n w=-2w,
    l_minus=(1,0,0,-1),
    Psi_epsilon=cos(epsilon f)Psi0+sin(epsilon f)w,

mit glattem reellem kompakt getragenem f. Psi_epsilon bleibt punktweise
normiert. Alle gemischten j-Bilineare zwischen Psi0 und w verschwinden,
also

    j_epsilon=cos²(epsilon f)l+sin²(epsilon f)l_minus,
    j'(0)=0,   j''(0)=2 f²(l_minus-l).

Setze auch bei dieser Variation E_epsilon=I+C[Psi_epsilon,h] und halte
h fest. Weil E'(0)=0, enthält die zweite Volumenvariation keinen
quadratischen E'-Term. Mit r=l_minus-l und E^-1 des Hintergrunds ist

    V4''(0)=integral (E^-1)^mu_a
              [r^a partial_mu(f²)+2 kappa h n_mu r^a f²].

Der Ableitungsterm integriert sich wegen
partial_mu(E^-1)^mu_a=0 zu null. Mit
(E^-1)^mu_a n_mu=n_a und n.r=-2 folgt

    V4''(0)=-4 kappa integral h f²,
    (-rho_v V4)''(0)=+4 rho_v kappa integral h f².

Auf einem Patch mit kappa h>0 ist dieser Koeffizient für rho_v!=0
nicht null. Er kann nicht durch bloße Normierung der Probe entfernt
werden. Damit ist die Fluktuationswirkung allgemein rho_v-abhängig,
obwohl der spezielle Hintergrund für jedes rho_v exakt gleich bleibt.

Die unabhängige Kontrolle liefert sogar die endliche Differenz auf
diesem Pfad: Mit r_vec=l_minus-l und r_scalar=sin²(epsilon f) ist
E_epsilon-E0 ein Rang-eins-Update
r_vec[partial r_scalar/2+kappa h n r_scalar]^T. Die
Determinantenformel und dieselben Randbedingungen ergeben exakt

    V4[Psi_epsilon]-V4[Psi0]
       =-2 kappa integral h sin²(epsilon f),

solange die Orientierung erhalten bleibt. Auf einem unendlichen Gebiet
ist diese kompakt getragene Differenz gemeint, nicht die Subtraktion
zweier unregulierter unendlicher Volumina. Ihre zweite Ableitung
bestätigt das Vorzeichen und den Faktor der obigen Gegenprobe.

Das Vorzeichen eines Terms in der Lorentz-Wirkung allein beweist weder
Stabilität noch Instabilität. Die vollständige quadratische Wirkung,
kinetische Struktur, Nebenbedingungen und alle übrigen Beiträge müssten
dafür gemeinsam ausgewertet werden. Insbesondere wird kein Schutz
gegen Quantenkorrekturen aus dieser Hintergrundlösung abgeleitet.

## 7. Der tatsächliche QAM-Normierungstest

In `v490-post-release-layers.tex`, r04.2, ist die Zustandsmatrix
rho=G/Tr G mit G=F^T F gegeben. Unter F->sF, s>0, bleibt rho gleich,
während G und Tr G mit s² wachsen. Eine lokale Zustandsnormierung
bestimmt somit nicht einmal die Intensität, geschweige denn von sich
aus ein gravitationswirksames Raumzeitvolumen.

Würde man etwa D=integral sqrt(-g) Tr G als Nenner einer Wirkung
vorschlagen, so gilt bei unabhängig festgehaltener Metrik D->s²D.
Der Test aus der vorigen Notiz verlangt aber delta(V4/D)=0 für alle
erlaubten Variationen. Hier ist d(V4/D)/d log s=-2V4/D!=0.
Dieser konkrete Nenner erfüllt die erforderliche Konstantenentkopplung
also nicht, sofern diese Amplitudenvariation erlaubt ist.

Das ist keine Behauptung, das Paper definiere diesen Nenner bereits.
Es ist ein Gegencheck gegen seine naheliegende Gleichsetzung mit einer
Volumennormierung. Eine zusätzliche Vorschrift könnte den Variationsraum
ändern; sie müsste explizit begründet werden. Die eben geprüfte affine
Nebenbedingungsreaktion ist ein anderer Mechanismus als I/V4.

## 8. Physikalischer Stand und nächste Pflicht

Es liegt jetzt ein konkreter klassischer Mechanismus auf einem besonderen
Lösungszweig vor: Die geometrische Nebenbedingung nimmt einen konstanten
Volumenbeitrag in ihrer Reaktionsdichte auf, ohne den Hintergrund zu ändern.
Das ist eine Entkopplung dieses Hintergrunds, keine Bestimmung eines
kleinen absoluten Energieparameters. Normierte Fluktuationen widerlegen
bereits die stärkere Behauptung einer allgemeinen Konstantenunempfindlichkeit.

Für die native Theorie fehlen weiterhin die Herleitung der affinen
Nebenbedingung und ihres festen Referenzframes sowie die gemeinsame
Wiederherstellung von Masse, Gauge-Quelle, C7 und HC-Matching. Der
Hintergrund-Ursprungscheck `HC_Background_Coframe_Origin.md` zeigt zudem,
dass eine Expansion der nativen Bilineare zusätzliche Kreuzterme erzeugt;
E=theta+C[Fluktuation] folgt daraus nicht automatisch.

Die Fortsetzung muss daher prüfen, ob eine native, durch ihre Dynamik
ausgewählte Untermenge diese Reaktion bewahrt und was die vollständige
Fluktuationswirkung daraus macht. Das bloße Verbieten des getesteten
Spinorkanals wäre eine neue Annahme. OP5 bleibt offen; der Haupttext wird
nicht geändert. Analytische unabhängige Prüfung steht in
`OP5_Affine_Vacuum_Response_Independent.md`; keine numerische Simulation
oder vollständige native Lösung wird behauptet.
Die unabhängige Notiz wurde vollständig gelesen; sämtliche zusätzlichen
Eulerterme und beide Varianten der Volumenkontrolle wurden abgeglichen.
