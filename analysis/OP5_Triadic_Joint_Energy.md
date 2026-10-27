# OP5: Gemeinsame Energie der triadischen Probe

Datum: 2026-10-26. Ausgangsrevision: a97e32d.
Status: exakte bedingte modale Ableitung; keine native Herleitung eines
Raumzeit-Energie-Impuls-Tensors und kein Abschluss von OP5.

## 1. Fragestellung und Quellenbindung

Die letzte Referenzprüfung (`OP5_Independent_Physical_References.md`)
liefert einen eindeutigen zeitartigen Nullfluss-Beobachter für zwei
positive, nicht parallele Nullströme. Ob die Probe-Komponenten tatsächlich
solche Ströme darstellen, ist eine eigene Eingabe.

`sources/research/parts/v470/10_sphaera_and_physics.tex`,
`prop:triadic-two-probe`, enthält drei gekoppelte Komponenten mit
Diagonalblöcken Omega_1, Omega_2, Omega_perp und Kopplungen
g_Y T_12, chi T_1perp, chi T_2perp samt Rückblöcken. Das dortige chi ist
ein Kopplungsparameter, keine relative Rapidität. Die folgende Wirkung
steht unter zusätzlichen Voraussetzungen; Omega_triangle ist ohne
Spinor-, Zeit- und Adjungiertenreduktion noch kein modaler Hamiltonoperator.

`HC_Real_Probe_Current_Closure.md` zeigt bereits, warum der gedruckte
HC-Transport nicht automatisch eine geschlossene reelle Wirkung mit
positiver Norm ergibt. `HC_Collective_Action_Reduction.md` enthält bereits
die bedingte konservative modale Wirkung und die Bedeutung verborgener
kanonischer Partner. Diese Ergebnisse werden hier benutzt, nicht als neu
beansprucht. Neu ausgewertet wird ihre gemeinsame triadische Energiebilanz
im Hinblick auf die vorgeschlagene physische Referenz.

## 2. Genau deklarierter Prüfbereich

Es seien f=(f_1,f_2,f_3) komplexe effektive Amplituden in einem festen
orthonormalen Modenraum; alternativ dürfen die f_i Vektoren sein.
Die kinetische Norm ist positiv und konstant. Mit hbar=1 sei

    L = i/2 (f† dot(f) - dot(f)† f) - f† H(t) f,
    H_ii = H_ii†,  H_ji = H_ij†.

Für skalare Moden schreibe H_ii=epsilon_i reell und H_ij=h_ij.
Variation nach f† ergibt i dot(f)=H f. Die Angaben sind klassische
effektive Modendaten, keine quantisierte Vakuumenergieberechnung.
Positivität der Norm impliziert nicht H>=0; falls positive Energien
benötigt werden, muss diese zusätzliche Eigenschaft geprüft werden.

Für eine native Identifikation sind insbesondere die Modenprofile,
kinetische Adjungierte, Rückkopplungsbedingungen und Hermitizität der
reduzierten Kopplungen erforderlich. Die gedruckten T_ij werden nicht
stillschweigend durch frei gewählte hermitesche Matrizen ersetzt.

## 3. Exakte Austausch- und Energiebilanz

Setze n_i=f_i†f_i und z_ij=f_i†H_ij f_j. Dann

    dot(n_i) = sum_(j != i) J_(i<-j),
    J_(i<-j) = 2 Im(z_ij) = -J_(j<-i),
    dot(N)=0,  N=sum_i n_i.

Beweis: dot(n_i)=2 Re[-i sum_j f_i†H_ij f_j]. Der Diagonalterm ist
reell, und z_ji=z_ij* liefert die Antisymmetrie. Ein Normstrom ist hier
noch kein Raumzeit-Energiefluss.

Die vollständige Energie ist

    E = f†Hf = E_diag + E_int,
    E_diag = sum_i f_i†H_ii f_i,
    E_int = 2 Re sum_(i<j) z_ij.

Durch Einsetzen von dot(f)=-iHf folgt ohne Näherung

    dot(E) = f† dot(H) f.

Bei konstantem H ist E erhalten. Für konstante skalare epsilon_i gilt

    dot(E_diag) = sum_(i<j) (epsilon_i-epsilon_j) J_(i<-j),
    dot(E_int) = -dot(E_diag)           [konstantes H].

Damit sind die getrennten diagonalen Energien im Allgemeinen keine
abgeschlossenen Beiträge. Bei extern vorgegebenem H(t) beschreibt
f†dot(H)f die Leistung des steuernden Hintergrunds. Ist H selbst ein
dynamisches Feld, benötigt dessen Energie eine eigene Bilanz aus der
gemeinsamen Wirkung; die modale Formel ersetzt diese nicht.

## 4. Exakter Gegenbeleg: Gleiche Populationen, verschiedene Energie

Wähle drei echte gleiche Kopplungen h_12=h_13=h_23=g>0 und
epsilon_1=epsilon_2=epsilon_3=epsilon, mit epsilon>2g. Diese striktere
als nötige Bedingung garantiert positive Energie: Die Eigenwerte sind
epsilon+2g und zweimal epsilon-g.

    f_A=(1,1,1)/sqrt(3),       E_A=epsilon+2g,
    f_B=(1,1,-1)/sqrt(3),      E_B=epsilon-2g/3.

Beide Zustände haben N=1 und exakt n_1=n_2=n_3=1/3. Trotzdem
unterscheidet sich ihre Gesamtenergie um 8g/3. Alle Normströme sind
am betrachteten Zeitpunkt null, weil sämtliche z_ij reell sind.
Dies behauptet keine Stationarität von f_B: Es ist im Allgemeinen
kein Eigenzustand, und spätere Ströme können entstehen.

Allgemeiner ergibt f(theta)=(1,1,exp(i theta))/sqrt(3)

    E(theta)=epsilon+(2g/3)(1+2 cos(theta)).

Die relative Phase trägt somit Energieinformation, die in der bloßen
Population fehlt. Eine Auslese, die diese Kohärenzen wegwirft, kann
die gemeinsame Energiebilanz nicht rekonstruieren. Die Aussage betrifft
Populationen; sie behauptet nicht, jede vollständige QAM-Auslese verliere
genau diese Daten. Eine konkrete QAM-Abbildung muss darauf geprüft werden.

Die unabhängige Prüfung verschärft den Gegenbeleg auf eine vollständige
Zeitreihe: Für zeta=exp(2 pi i/3) ist

    f_C=(1,zeta,zeta²)/sqrt(3),  H f_C=(epsilon-g)f_C.

f_A und f_C sind beide Eigenzustände. Ihre drei Populationen bleiben
unter demselben H für alle Zeiten identisch, ihre Energien unterscheiden
sich dennoch um 3g. Bei f_C zirkulieren Normströme
J_(1<-2)=J_(2<-3)=J_(3<-1)=sqrt(3)g/3; an jedem Knoten ist die Summe
null. Auch eine vollständige Zeitreihe der Populationen beseitigt diese
Energie-Mehrdeutigkeit also nicht. Es handelt sich um verschiedene
Präparationen bei festem H, nicht um zwei passive Beschreibungen desselben
Zustands. Eine räumliche Strominterpretation wird nicht vorausgesetzt.

## 5. Welcher Frame wann ausliest: Generator und Energie unterscheiden

Die Unterscheidung wurde bereits in `OP5_Readout_Order_Timing.md`,
Abschnitten 5.1–5.2, behandelt. Hier wird sie für die triadische Bilanz
erneut ausgeschrieben, nicht als neues Resultat beansprucht.

Für einen differenzierbaren unitären Basiswechsel f'=U(t)f gilt

    i dot(f') = H_gen' f',
    H_gen' = U H U† + i dot(U) U†.

Das transformierte Energieobservable desselben Systems ist dagegen

    H_E' = U H U†,
    E = f'† H_E' f'.

Der zusätzliche Term i dot(U)U† beschreibt die bewegte Basis. Er ist
ohne weiteres physisches Modell keine zusätzliche Systemenergie.
Für A=i dot(U)U† ist

    dot(H_E') = U dot(H) U† - i[A,H_E'],
    dot(E) = f'†(dot(H_E') + i[H_gen',H_E'])f'
           = f'†U dot(H)U†f'.

Die Basisbewegung hebt sich in der Energiebilanz exakt auf. Der Test
U=exp(i alpha(t))I verschiebt H_gen' um -dot(alpha)I, lässt H_E' aber
unverändert. Eine so erzeugte skalare Generatorverschiebung kann daher
nicht als berechnete absolute Energie oder kosmologische Konstante gelten.
Dies ist ein interner unitärer Basiswechsel; eine Identifikation mit
physikalischen Lorentz-Beobachtern wird damit nicht bewiesen.

Eine aktive Änderung von Kopplungen, eine Präparation oder ein Messgerät
ist anders zu behandeln: Dann sind Zustandsänderung, externe Leistung und
Geräterückwirkung zu bilanzieren. Das frühere Readout-Protokoll untersucht
einen solchen ausdrücklich vorgegebenen Gerätefall.

## 6. Grenze zum nativen HC-Transport

Falls eine tatsächlich hergeleitete Modengleichung stattdessen

    dot(f)=(-iH-D)f,  H=H†, D=D†,

lautet, ergibt direkte Differentiation

    dot(N)=-2 f†D f,
    dot(E)=f†dot(H)f-f†(DH+HD)f.

Selbst D>=0 und H>=0 machen DH+HD nicht allgemein positiv; ein
universelles Vorzeichen des Energieaustauschs wird nicht angenommen.
Auch ist D>=0 aus dem nativen gamma-geordneten HC-Term bisher nicht
bewiesen. Der Rückkanal oder die bewegte kinetische Metrik müsste
ausgewertet werden. Die konservative Bilanz oben darf diesen Schritt
nicht ersetzen.

## 7. Konsequenz für neutralen Frame und OP5

Die triadische Blockstruktur liefert eine konkrete Stelle für gemeinsame
physische Beiträge. Ihre bloßen Diagonalgewichte reichen jedoch bereits
im konservativen Prüfbereich nicht für die Energie. Für einen neutralen
Raumzeitbeobachter fehlt zusätzlich der gesamte Tensor: Impulsfluss,
Spannungen, räumliche Profile und die Wechselwirkung mit den übrigen
Feldern. Selbst die vollständige skalare Modenenergie bestimmt ihn nicht.

Ein Aufteilen der Kreuzenergie auf einzelne Komponenten benötigt eine
Zuordnungskonvention. Ein gemeinsamer konstanter unitärer Basiswechsel
erhält E, kann aber Diagonal- und Kreuzanteile verändern; in einer
Eigenbasis verschwinden die letzteren. Eine physische Komponentenwahl
braucht folglich zusätzliche Struktur oder konkrete Messkopplungen.

Nächster nativer Prüfpunkt ist eine reelle, konsistente kovariante Wirkung
mit ausgewerteter Adjungierter und erlaubten Feldvariationen. Aus dieser
muss der gesamte Energie-Impuls-Tensor einschließlich Wechselwirkung und
Hintergründen folgen. Erst seine Eigenstruktur prüft die Existenz und
Eindeutigkeit eines zeitartigen Nullfluss-Beobachters. Der bisherige
Zwei-Nullstrom-Satz bleibt ein bedingter Spezialfall.

Ein konstanter Zusatz cI zum modalen H verändert E um cN und die
gemeinsame Phase. Ein konstanter Hintergrundterm in einer gravitativen
Wirkung ist ein anderes Objekt. Diese beiden Freiheiten werden hier
weder identifiziert noch durch eine Framewahl festgelegt. OP5 bleibt offen.

## 8. Prüfstatus

Die Gleichungen folgen analytisch aus der deklarierten Wirkung bzw.
direkter Differentiation. Gegenbeleg, Eigenwerte, entgegengesetzte Ströme
und Basisverbindung sind ausgeschrieben; keine numerische Simulation,
kein Fit und keine native Vollfeldlösung wird als Beleg behauptet.
Die separate Prüfung steht in `OP5_Triadic_Energy_Independent.md`.
Sie wurde vollständig gelesen; insbesondere wurden der stationäre
zeta-Gegenbeleg, die drei Stromvorzeichen und die Basisverbindung direkt
nachgerechnet. Die Quellenfingerprints werden im begleitenden
Provenienz-Snapshot festgehalten. Der analytische Status bleibt auf den
deklarierten modalen Bereich beschränkt.
