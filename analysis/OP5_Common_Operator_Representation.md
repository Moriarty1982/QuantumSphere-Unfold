# OP5: gemeinsame Operator-Darstellung und physikalischer Übergang

Checkpoint `OP5-COMMON-OPERATORS-2026-10-26`.
Git-Basis: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Lokaler Forschungsstand vom 26. Oktober 2026. Diese Notiz führt die
Operator-, Closure-, Frame- und Readout-Untersuchungen zusammen. Sie
ersetzt deren ausführliche Beweise nicht. Keine Änderung am Manuskript,
kein Release und keine Schließung von OP5.

## 1. Ergebnis vorweg

Eine gemeinsame konsistente Darstellung der bisher getrennten Operatoren
ist als **zusätzlich gewählter Probe-Sektor** möglich. Darin liegen alle
drei gekoppelten Moden innerhalb des physikalischen Closure-Sektors.
Eine invariante Zweimodenebene liegt innerhalb dieses Dreimodenraums.
Die dritte Mode muss also nicht aus dem physikalischen Sektor entfernt
werden. Die Darstellung erfüllt die algebraischen Strukturbedingungen
und eine klar angegebene konservative Probe-Gleichung.

Sie ist jedoch nicht aus dem vollständigen M_16 des Papers abgeleitet.
Insbesondere ist der dabei gewählte Hintergrund keine nachgewiesene
Lösung der rückgekoppelten Resonanz- und Geometriegleichungen. Sie liefert
keinen eindeutig ausgewählten neutralen Attraktor und keine absolute
Vakuumenergie. Diese Grenzen sind Teil des Ergebnisses.

## 2. Drei Projektoren und drei verschiedene Aufgaben

| Objekt | Träger und Aufgabe | Native Vorgabe bzw. offener Übergang |
|---|---|---|
| J, C=(I+J)/2 | Struktureller Träger: gerade/ungerade HC-Anteile | T4 fordert [M,J]=[M,C]=0 in einer zulässigen gemeinsamen Darstellung. |
| P=P_C7 | Interner Probe-Träger: physikalisch zugelassener Sektor | P²=P und P Psi=Psi sind angegeben; positive Adjungierte, konkrete Darstellung und Beziehung zu C sind zusätzlich zu bestimmen. |
| S | Innerhalb eines konkreten Modenmodells: beibehaltene Zweimodenebene | In den Beispielen konstruiert; weder nativ mit P noch mit C gleichgesetzt. |

Weitere typisierte Objekte: M transportiert Schicht-/interne Daten,
T koppelt interne Moden, H_C ist der minimale positive Closure-Operator,
Gamma^mu wirkt im faktorisierten Fall auf Spinoren, A_mu transportiert
interne Zustände. Ein Projektor auf Amplituden ist kein Quantenkanal auf
Dichtematrizen. Die Triad-Kopplung T ist auch nicht automatisch die in
anderen Kapiteln T genannte Frame- oder Zeitumkehrabbildung.

## 3. Gemeinsame native Gleichungen und exakte Prüfbedingungen

Die Quelle `v470/10_sphaera_and_physics.tex` gibt an:

    (i Gamma^mu D_mu - Omega) Psi=0,    P Psi=Psi,
    D_mu=partial_mu+i A_mu+kappa H_C n_mu+eta(I-P)n_mu,
    Omega=m_0 I+alpha P M P+beta g_Y T+gamma H_C,
    H_C=rho [M,P]†[M,P]+sigma R†R,
    R=(I-P)MP+PM(I-P),    rho,sigma>=0.

Unter orthogonalem P im festgelegten positiven internen Skalarprodukt,
mit M=[[A,B],[D,E]], ist exakt

    H_C=(rho+sigma)diag(D†D,B†B),    [H_C,P]=0.

Für hermitesches M ist D=B†. H_C misst die Kopplung über die P-Grenze;
es misst nicht jede Dynamik innerhalb von P. Insbesondere können innerhalb
eines exakt geschlossenen P-Sektors nichttriviale Kopplungen fortbestehen,
obwohl H_C=0 ist.

Wenn P,A_mu,T nur intern und Gamma^mu auf einem separaten vollständigen
Dirac-Träger wirken, lautet die Normalgleichung mit Q=I-P:

    N=i Gamma^mu Q(nabla_mu P)P-beta g_Y QTP,
    nabla_mu P=partial_mu P+i[A_mu,P].

N=0 auf dem ganzen P-Spinorraum ist unter den üblichen nichtentarteten
Clifford- und Hermitizitätsannahmen äquivalent zu

    nabla_mu P=0 für alle mu,    beta g_Y QTP=0.

Bei nichtverschwindender triadischer Kopplung muss also auch T den
physikalischen Sektor erhalten. Bewegung des Projektors und rein interne
T-Kopplung können sich auf dem ganzen Dirac-Träger nicht gegenseitig
kompensieren. Für eine ausgewählte Lösung N Psi=0, spinabhängiges T
oder eine andere Darstellung folgt dieser Ausschluss nicht automatisch.

Eine zusätzliche kleinere Ebene S verlangt ihrerseits

    (I-S) G S=0,

oder für bewegtes S(t): (I-S)GS=dot S S. Das ist ein weiterer Test innerhalb
des physischen Sektors, kein Ersatz für dessen Closure.

## 4. Eine vollständig angegebene gemeinsame Probe-Darstellung

Die folgenden Werte sind **eine Konstruktion**, keine aus dem Paper
ermittelten Matrixeinträge oder vorhergesagten physikalischen Parameter.
Sie zeigen, dass die oben genannten algebraischen Anforderungen zusammen
erfüllbar sind, und korrigieren die zu enge Annahme „zwei Moden physisch,
dritte Mode außerhalb“.

### 4.1 Gemeinsamer interner Träger

Wähle V=C^16 mit gewöhnlicher positiver Adjungierter und

    P=C=diag(I_3,0_13),    J=2P-I,
    M=lambda_+ P+lambda_- (I-P),
    lambda_+,lambda_- reell und verschieden.

Damit gelten P²=P=P†, J²=I, C=(I+J)/2 und [M,J]=[M,C]=[M,P]=0.
C ist tatsächlich der Spektralprojektor von M zu lambda_+.
Die Wahl Rang(P)=3 ist nur die minimale Einbettung für dieses Beispiel;
der native Rang von P_C7 wird damit nicht bestimmt. Die Dimension 16
allein identifiziert den Träger ebenfalls nicht mit der nativen M_16.

Der minimale Closure-Operator ist hier H_C=0. Das ist exakte Closure
in diesem algebraischen Modell, kein verschwindender gesamter Energieinhalt.

### 4.2 Alle drei gekoppelten Moden innerhalb von P

Setze auf ran(P)

    A=[[0,-omega,-mu],[omega,0,-nu],[mu,nu,0]],
    T_P=iA,    T=T_P direct_sum 0_13,
    a=(nu,-mu,omega),    Omega_a=||a||>0,
    k=beta g_Y.

Alle drei Parameter dürfen ungleich null sein. T ist hermitesch und
[T,P]=0. Das T-Muster entspricht einer hermiteschen skalaren Realisierung
der angegebenen triadischen Querblöcke; die konkrete Wahl rein imaginärer
Kopplungen bleibt eine zusätzliche Modellannahme. Der Resonanzoperator
auf P ist

    Omega_P=m_* I_3+k iA,    m_*=m_0+alpha lambda_+.

Bei m_*>|k|Omega_a sind alle drei Eigenwerte von Omega_P positiv.
Die M- und T-Matrizen sind hier ausdrücklich verschiedene Operatoren:
M gewichtet die Sektoren, T erzeugt die interne triadische Dynamik.
Damit wird die frühere Zusatzannahme M=mI+iA nicht weiter benötigt.

### 4.3 Spinor, positive Norm und Zeitgenerator

Nimm die konventionelle flache Dirac-Darstellung mit Signatur (+---),
(Gamma^0)²=I, Gamma^0 hermitesch und Gamma^a antihermitesch. Die
Adjungierte ist bar Psi=Psi† Gamma^0, somit K^0=I und die Zeitnorm positiv.
Gamma wirkt nur auf C^4_spin. Wähle konstantes P, A_mu=0 und H_C=0.
Auf P Psi=Psi verschwindet auch eta(I-P)n_mu Psi. Die Probe-Gleichung wird

    i partial_t Psi = H_D Psi,
    H_D=-i Gamma^0 Gamma^a partial_a+Gamma^0 Omega.

Auf dem räumlich homogenen festen Impulsmodus p=0 und dem positiven
Eigenraum von Gamma^0 reduziert sich die interne Gleichung exakt zu

    i dot f=Omega_P f.

Dies ist eine Modenrechnung oder eine Rechnung pro räumlichem Volumen;
ein homogener Zustand auf ganz R³ ist nicht als normierbares Einzelpaket
behauptet. Für p!=0 ist der physische positive Energieoperator nicht
einfach Omega_P: Für einen internen Eigenwert lambda von Omega_P gilt
E²=|p|²+lambda². Die gewählte Zeiteinheit und die Parameterwerte sind
noch nicht nativ in Sekunden bzw. Energieeinheiten bestimmt.

### 4.4 Die kleinere Ebene und zwei Auslesungen

Auf ran(P) ist S_3=I_3-aa^T/Omega_a²; erweitere S=S_3 direct_sum 0_13.
Dann SP=S, [S,M]=[S,T]=0. S ist folglich eine erhaltene Zweimodenebene
innerhalb des geschlossenen Dreimodensektors. Mit reellen orthonormalen
e_1,e_2 in a^perp und e_2=(a/Omega_a) cross e_1 gilt

    Omega_S=m_* I_2+k Omega_a sigma_y.

Eine zusätzlich festgelegte physische Messung entlang e_1,e_2 liefert
für die reelle Bloch-Scheibe mit Koordinaten x,z

    p_1(t)=[1+z cos(2 k Omega_a t)-x sin(2 k Omega_a t)]/2.

Zwei Ensemble-Auslesungen bei 0 und tau rekonstruieren x,z genau dann,
wenn sin(2 k Omega_a tau)!=0. Die Wahl und Realisierung dieses Messgeräts
ist eine weitere Annahme. Die Formel beschreibt keine zweimalige
störungsfreie Messung desselben Exemplars und rekonstruiert keine dritte
Bloch-Komponente eines allgemeinen Zustands.

Die Mischung S_3/2 ist stationär. Sie ist kein eindeutiger Attraktor;
die Entwicklung ist unitär und andere stationäre Zustände existieren.
Der konstante Offset m_* fällt aus diesen Wahrscheinlichkeiten heraus.

## 5. Was diese Darstellung löst und was sie nicht löst

| Verpflichtung | Status in der Konstruktion | Status für das Paper |
|---|---|---|
| Gemeinsamer Träger und Adjungierte | Explizit gewählt, positiv | Native Identifikation offen |
| Beziehung C zu P | Explizit C=P gesetzt | Nicht aus den recherchierten Passagen hergeleitet |
| M, P, T auf demselben Träger | Vollständig angegeben und verträglich | Tatsächliche gemeinsame Matrixdaten fehlen in der vorliegenden Ableitung |
| Physischer Sektor bleibt erhalten | Ja, konstantes P, A=0, [T,P]=0 | An nativen Feldern nachzuweisen |
| Zwei-Modenebene innerhalb von P | Ja, explizites S | Entsprechenden nativen Sektor identifizieren |
| Positive Probe-Norm und Generator | Ja, deklarierter Dirac-Sektor | Native Gamma-/Adjungierten-/Zeitidentifikation offen |
| Readout | Binäres Instrument zusätzlich vorausgesetzt | Aus physischer Kopplung herzuleiten |
| Nichttriviale Relaxation | Nein; das Modell ist konservativ | Reservoir oder anderer begründeter Mechanismus nötig, falls Attraktion beansprucht wird |
| Rückgekoppelte Resonanzgleichung | Nicht gelöst | Zwingender nächster physikalischer Nachweis |
| Gravitative Vakuumenergie | Nicht berechnet oder festgelegt | Wirkung, Stress-Tensor und absoluter Term offen |

Insbesondere gilt bei A=0 und H_C=0: F=0. Die native Resonanzgleichung
D^mu F_mu nu=J_probe+J_C7+J_HC ist für einen nichtverschwindenden Probe-Strom
damit im Allgemeinen nicht erfüllt. Die Darstellung ist ausdrücklich
eine Probe auf vorgegebenem Hintergrund, keine selbstkonsistente Lösung
des gesamten Feldsystems. Diese Rückwirkung darf nicht nachträglich
als vernachlässigbar behauptet werden, ohne einen kontrollierten Grenzfall.

## 6. Konsolidierter physikalischer Befund zu OP5

Die Kombination von Frames kann Zustandsinformation ergänzen oder eine
gemeinsame Modenreferenz definieren. Sie legt damit noch keine gravitative
Energienull fest. Eine neutrale Auslesung, eine stationäre Mischung, exakte
interne Closure und verschwindende kosmologische Konstante sind vier
verschiedene Aussagen.

Die alte spektrale Theta-R-Balance ist durch die Frame-Umdeutung nicht
repariert: Der frühere Prüfstand fand Vorzeichen-/Regularisierungs- und
Normierungsprobleme sowie eine erhebliche verbleibende Differenz. Diese
Befunde betreffen die konkrete alte Route, nicht jeden möglichen nativen
OP5-Ansatz. Die hier konstruierte Darstellung ersetzt jene Balance nicht
durch eine neue physikalisch hergeleitete Gleichung.

Für die absolute Energie reicht auch ein festgelegter Generator nicht:
Ein skalarer Offset bleibt in normierten Zustandswahrscheinlichkeiten
unsichtbar. Ob und wie er gravitativ wirksam ist, entscheidet eine
konsistente Wirkung samt Energie-Impuls-Tensor, nicht die Wahl einer
Auslesebasis. Der konstante reine Hintergrundterm einer solchen Wirkung
wird durch die hier geprüften Closure- und Transportbedingungen nicht
bestimmt.

## 7. Nächster Schritt mit klaren Erfolgskriterien

1. Die tatsächliche gemeinsame Darstellung von M_16,P_C7,T und Gamma samt
   positiver Adjungierter aus dem Paper extrahieren oder als fehlende
   physikalische Zusatzannahme kennzeichnen. Die vorstehende Konstruktion
   ist ein Vergleichsmaßstab, kein Ersatz für diese Extraktion.
2. Auf demselben Träger den Sektortest und die rückgekoppelten
   Resonanz-/Closure-Gleichungen gemeinsam lösen, oder einen kontrollierten
   Probe-Grenzfall begründen. Ein bloßes Erfüllen von N=0 reicht nicht.
3. Falls ein neutraler Zustand dynamisch ausgewählt werden soll, seine
   Existenz, Stabilität und Energiebilanz einschließlich Rückkanälen prüfen.
4. Erst für einen solchen physikalischen Zustand die gravitative Wirkung
   variieren und Dichte, Druck sowie den absoluten Hintergrundterm bestimmen.

Ein Erfolg bei 1–2 wäre ein belastbarer nativer Dynamiksektor. Ein Erfolg
bei 3 wäre eine physikalische Auswahlmechanik. Erst 4 könnte eine neue
Aussage zur kosmologischen Konstante tragen. Kein früherer Teilschritt
wird als OP5-Abschluss gewertet.

## 8. Quellen, Beweise und Reproduzierbarkeit

Primäre interne Quellpassagen: `v470/12_structural_core.tex` (T4),
`v470/16_master_model.tex` (Layer-Transport),
`v470/10_sphaera_and_physics.tex` (Mastergleichung, Triad, minimales H_C),
`v490-post-release-layers.tex` (r05 Portgewichtung, r28 korrigierte
Frame-Abbildung und explizites Austauschmodell),
`hc-dynamics-and-geometry.tex` (Autonomie, Realität und Geometriegrenzen).
Die Beschreibung von r28 ersetzt keine Ableitung seines Gerätemodells
aus dem vollen Feldsystem.

Ausführliche lokale Ableitungen und Grenzen:

- [Native Blockreduktion](OP5_Native_Closure_Block_Reduction.md)
- [Triadische Ebene](OP5_Triadic_Invariant_Plane.md)
- [Closure-Verträglichkeit des früheren Kandidaten](OP5_Triadic_Closure_Compatibility.md)
- [Projektor-Transporttest](OP5_Native_Projector_Transport_Test.md)
- [Spinortrennung und Dirac-Grenzfall](OP5_Spinor_Separation_And_Dirac_Limit.md)
- [Readout- und Energiebilanz](OP5_Readout_Protocol_Energy_Result.md)
- [Lambda- und Neutralitäts-Reassessment](OP5_Lambda_Neutral_Reassessment.md)

Die neue gemeinsame Darstellung wurde analytisch durch Blockkommutatoren,
Closure-Nullität, Dirac-Hamiltonreduktion und die explizite Rotationsebene
geprüft. Dafür ist kein numerischer Lauf behauptet. Ein begleitender
Provenienz-Snapshot pinnt die gelesenen lokalen Dateien und diese Notiz mit
SHA-256; die älteren Rechenmanifeste bleiben bei ihren historischen Läufen.
