# OP5: native Projektoren und die vollständige Normalgleichung

26. Oktober 2026. Lokale Fortsetzung der triadischen Verträglichkeitsprüfung.
Keine Manuskriptänderung. OP5 bleibt offen.

Fortsetzungsbefund: `OP5_Spinor_Separation_And_Dirac_Limit.md` zeigt, dass
die in Abschnitt 4 offengelassene direkte Kompensation auf dem gesamten
faktorisierten Dirac-Träger mit rein internem T nur bei getrennt
verschwindenden Queranteilen möglich ist. Die allgemeinere Normalgleichung
bleibt gültig; ihr Lösungsraum wird dadurch unter diesen Voraussetzungen
präzisiert.

## Ergebnis

Der Quellenabgleich führt von den frei gewählten Beispielen zu einem
unmittelbaren Test der gedruckten Probe-Gleichung. Dazu müssen drei Objekte
auseinandergehalten werden: der strukturelle HC-Projektor C=(I+J)/2,
der physische Closure-Projektor P=P_C7 und der Ebenenprojektor S der letzten
Vergleichsmodelle. Ihre Gleichsetzung ist keine bereits nachgewiesene
Definition. Unter einer expliziten positiven internen Darstellung kann die
verbleibende Normalgleichung für den P-Sektor exakt angegeben werden.

## 1. Quellenabgleich und Typen

Untersuchte Quellen und genaue Anschlussstellen:

- `sources/research/parts/v470/12_structural_core.tex`,
  `def:tensor-structural-kernel`, Bedingung T4 und
  `prop:tensorial-intertwining-m`: Die Verträglichkeit von M mit J und C
  wird als Zulässigkeitsbedingung gesetzt. Der begleitende Text unterscheidet
  diese Definition von einer unabhängigen Herleitung aus T1–T3.
- Dieselbe Datei, `thm:hc-spectral-projector`: eine strukturelle
  Spektralprojektor-Aussage unter den dort angegebenen Spektral- und
  Traversalvoraussetzungen. Ihre gesamte Beweiskette wird hier nicht auditiert.
- `sources/research/parts/v490-post-release-layers.tex`,
  `subsec:v490-r05-millennium`, Theoremlet r05.1: Auf dem dortigen Doublet
  hat M die Form lambda_+ C + lambda_- (I-C). Der Text sagt ausdrücklich,
  dass dies nicht die volle M_16 identifiziert. Das ist Portgewichtung,
  keine allgemeine Lorentz- oder Zeitentwicklung.
- `sources/research/parts/v470/16_master_model.tex`, `sec:millennium-hc`:
  globaler Schichttransport und formale vierteilige Layer-Zerlegung.
- `sources/research/parts/v470/10_sphaera_and_physics.tex`,
  `thm:master-field-equation`, `prop:triadic-two-probe` und „Explicit closure
  functional“: physischer Probe-Ansatz mit P_C7, T und H_C. Die angegebene
  Projektorbedingung P²=P enthält an dieser Stelle nicht ausdrücklich P†=P.
- `sources/research/parts/v470/09_preclosure_memory.tex`,
  `def:working-shared-matrix-leakage`: [M,J] und (I-C)MC werden als
  provisorische gemeinsame OP1-/OP5-Diagnostik vorgeschlagen. Das ist noch
  keine Berechnung eines bestimmten physikalischen Leckagekanals.

Die folgenden Schlussfolgerungen verwenden daher nicht stillschweigend
C=P oder S=P. Ebenso sind Matrix des Schichttransports, Operator auf
Zuständen und Superoperator auf Dichtematrizen nicht ohne Abbildung
identisch. Der globale Träger und die gemeinsamen Darstellungen sind
weiterhin Eingaben, die zu konkretisieren sind.

## 2. Strukturkommutativität allein schließt den physischen Sektor nicht

Ein exaktes Beispiel zeigt die fehlende Implikation. Auf C² setze

    C=diag(1,0),    J=2C-I,    M=diag(lambda_1,lambda_2),
    p=(cos theta,sin theta)^T,    P=|p><p|.

Dann sind [M,C]=[M,J]=0. Für lambda_1 != lambda_2 und
sin theta cos theta != 0 gilt dennoch [M,P]!=0. In der orthonormalen
Basis p,(-sin theta,cos theta) lautet das minimale Closure-Funktional

    H_C=(rho+sigma)(lambda_2-lambda_1)²
         sin²(theta) cos²(theta) I.

Es kann also nicht aus T4 allein auf verschwindendes physisches
Closure-Mismatch geschlossen werden. Das Beispiel ist eine logische
Trennung der Projektoren, keine behauptete native Parametrisierung.
Wenn eine gemeinsame Darstellung tatsächlich P=C beweist, folgt aus T4
hingegen [M,P]=0 und damit H_C=0 für das minimale Funktional.

## 3. Exakte Normalgleichung der gedruckten Probe-Gleichung

Zusätzliche, ausdrücklich zu prüfende Voraussetzungen: P(x) ist ein glatter
orthogonaler interner Projektor in einem festen positiven Skalarprodukt;
Gamma^mu wirkt auf einem separaten Spinorfaktor und kommutiert mit P.
Die Felder und Zustände liegen in einem gemeinsamen Bereich, in dem die
folgenden Ableitungen definiert sind. Ein spacetimeabhängiges Skalarprodukt
mit veränderter Adjungierter ist damit nicht mitbehandelt.

Schreibe Q=I-P und benutze wörtlich die native Form

    (i Gamma^mu D_mu - Omega) Psi=0,    P Psi=Psi,
    D_mu=partial_mu+i A_mu+kappa H_C n_mu+eta Q n_mu,
    Omega=m_0 I+alpha P M P+beta g_Y T+gamma H_C.

Die Blockidentität des minimalen Funktionals liefert [H_C,P]=0 auch dann,
wenn [M,P]!=0. Ferner ist [Q,P]=0. Somit ist der Queranteil des
kovarianten Projektortransports vollständig

    nabla_mu P := partial_mu P + i[A_mu,P].

Aus P Psi=Psi folgt durch Differenzieren

    Q partial_mu Psi = Q(partial_mu P)P Psi,
    Q D_mu Psi = Q(nabla_mu P)P Psi.

Multiplikation der Probe-Gleichung mit Q ergibt deshalb exakt

    N Psi=0,
    N := i Gamma^mu Q(nabla_mu P)P - beta g_Y Q T P.

Weder der skalare m_0-Term noch P M P noch der minimale H_C-Term erscheint
direkt in dieser Normalgleichung. Das ist eine algebraische Aussage
unter den genannten Voraussetzungen, keine Aussage über ihre indirekte
Wirkung auf Hintergrundfelder, P oder A_mu.

Soll die Reduktion für jeden zulässigen momentanen Spinorzustand im
P-Sektor gelten, muss N als Operator auf diesen Sektor verschwinden.
Für eine einzelne ausgewählte Lösung genügt dagegen N Psi=0; daraus
folgt nicht N=0. Existenz, Wohlgestelltheit und Erhaltung aller weiteren
Feldgleichungen sind separate Anforderungen.

## 4. Zwei konkrete Wege zur Sektorverträglichkeit

Ein einfacher hinreichender algebraischer Weg ist

    nabla_mu P=0 für alle mu,    Q T P=0.

Dann wird der Sektor kovariant transportiert, und die triadische Kopplung
führt ihn nicht nach außen. Für hermitesches T ist auch P T Q=0.
P selbst muss in einer beliebigen Eichdarstellung nicht konstant sein.

Allgemeiner können die kontrahierte Projektorbewegung/Verbindung und der
triadische Querblock einander kompensieren:

    i Gamma^mu Q(nabla_mu P)P = beta g_Y Q T P.

Das ist die genaue Stelle, an der die Frage „welcher Frame wann ausliest“
eine native mathematische Bedingung bekommt. Sie ist stark: Beide Seiten
müssen auf demselben Spinor-/internen Träger als Operatoren übereinstimmen,
nicht nur in einem passend gewählten skalaren Erwartungswert. Die Existenz
eines solchen gemeinsamen P,A_mu,T wird hier nicht angenommen oder bewiesen.

Ein Projektor kann für eine bekannte unitäre Dynamik immer mittransportiert
werden, indem man P(t)=U(t)P(0)U(t)† setzt. Das identifiziert lediglich einen
mitbewegten Sektor. Es erklärt für sich weder dessen physische Auswahl
noch Messapparatur, Zeitnormierung oder Hintergrundgleichungen. Die
Normalgleichung darf nicht durch einen nachträglich angepassten Projektor
als physikalisch gelöst ausgegeben werden.

## 5. Auswirkung auf den bisherigen Kandidaten und OP5

Die vorherige Identifikation des dreidimensionalen S mit dem Closure-P
war eine Testannahme. Der aktuelle Quellenabgleich liefert dafür keinen
Nachweis. Das Scheitern dieses Kandidaten ist deshalb kein allgemeines
Scheitern einer zusammengesetzten Referenz.

Jetzt gibt es einen engeren Arbeitsauftrag ohne weitere freie Matrixwahl:
Die konkrete Darstellung von P_C7, A_mu und T muss die Normalgleichung
N=0 erfüllen, und die strukturelle C-Darstellung muss mit dieser physischen
Darstellung in Beziehung gesetzt werden. Erst dann lässt sich das
verbleibende innere Dynamik- und Readoutproblem sinnvoll untersuchen.

Selbst eine erfolgreiche Sektorverträglichkeit legt m_0 nicht fest:
Der skalare Term fällt aus der Normalgleichung heraus. Eine Herleitung
der absoluten gravitativen Vakuumenergie benötigt daher weiterhin eine
eigene Wirkung und deren Energie-Impuls-Tensor. OP5 ist nicht geschlossen.

## Validierung und Reichweite

Analytisch geprüft: das Zweiprojektor-Gegenbeispiel, die Blockkommutativität
des minimalen H_C und jeder Schritt der Normalprojektion einschließlich
des Vorzeichens aus i Gamma^mu i A_mu. Kein numerisches Experiment,
keine behauptete Vollständigkeit über alle Paper-Versionen. Die Recherche
umfasst die oben genannten Definitions- und Entwicklungspassagen; sie
liefert keine vollständigen numerischen M_16-/T-/P-Daten auf einem gemeinsam
identifizierten physikalischen Träger.
