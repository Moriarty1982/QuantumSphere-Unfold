# OP5: Closure-Verträglichkeit der triadischen Ebene

26. Oktober 2026. Fortsetzung von `OP5_Triadic_Invariant_Plane.md`.
Lokale Forschungsnotiz; keine Manuskriptänderung und kein OP5-Abschluss.

## Präziser Gegenstand und Ergebnis

Geprüft wird die zuvor konstruierte invariante Ebene eines hermiteschen
Dreimodengenerators. Jetzt wird das gedruckte minimale Closure-Funktional
mitgeführt. Die folgende zusätzliche Identifikation wird ausdrücklich
gemacht: Die für Closure verwendete Matrix ist M=m I+iA, und ihr orthogonaler
Closure-Projektor ist P=diag(1,1,0). Der native 16-Moden-Träger, dessen
Projektor und die physische Spinor-/Zeitableitung sind damit nicht hergeleitet.

**Ergebnis:** In dieser konkreten Einbettung zerstört ein nichtverschwindender
Closure-Zusatz die zuvor gefundene Ebene generisch. Mit dem projizierten
M-Term kann unter einer exakten Parameterbedingung eine andere feste Ebene
erhalten bleiben. Diese schwächere Invarianz erhält jedoch nicht automatisch
die reelle Bloch-Scheibe des bisherigen Zweiauslesungsmodells.

Die unten stehenden Aussagen sind vollständig endlichdimensional bewiesen.
Sie widerlegen keine beliebige native Einbettung; sie prüfen und begrenzen
den konkreten Kandidaten der vorangehenden Notiz.

## 1. Voraussetzungen und native Anschlussstelle

Gewöhnliches positives Skalarprodukt über C, orthogonales P, konstante
reelle Koeffizienten, hbar=1. Die native Formel lautet

    H_C = rho [M,P]†[M,P] + sigma R†R,
    R=(I-P)MP+PM(I-P),    rho,sigma>=0.

Sie steht in `sources/research/parts/v470/10_sphaera_and_physics.tex`,
„Explicit closure functional“. Dort enthält Omega neben m_0 I auch
alpha P M P, beta g_Y T und gamma H_C. Die Reduktion auf einen selbstadjungierten
endlichen Hamiltonoperator verlangt zusätzliche Annahmen an Gamma und
Transport; sie wird hier nur bedingt vorgenommen. Die allgemeine
Blockidentität aus `OP5_Native_Closure_Block_Reduction.md` wird verwendet.

Setze c=rho+sigma und

    A=[[0,-omega,-mu],[omega,0,-nu],[mu,nu,0]],
    M=m I+iA,    r²=mu²+nu²,
    a=(nu,-mu,omega),    Omega²=r²+omega²>0.

Die frühere Ebene ist die komplexe lineare Hülle von a^perp im reellen
Raum. Ihr orthogonaler Projektor ist S=I-aa^T/Omega².

## 2. Closure erhält die alte Ebene nur in Sonderfällen

Die Off-Sektor-Spalte von M ist B=(-i mu,-i nu)^T. Deshalb

    H_C = c [[mu²,mu nu,0],[mu nu,nu²,0],[0,0,r²]],
    H_C a = c (0,0,r² omega)^T.

Ein hermitescher Operator erhält a^perp genau dann, wenn er a auf dessen
eigene Gerade abbildet. Für c>0 ist dies hier genau dann der Fall, wenn

    omega=0 oder r=0.

Der Fall c=0 ist trivial: Dann fehlt Closure in diesem minimalen Funktional.
Für c>0, r>0 und omega!=0 gilt genauer mit n=a/Omega

    ||S H_C n|| = c r³ |omega| / Omega² > 0.

Beweis: H_C n zeigt in z-Richtung und hat Betrag c r²|omega|/Omega;
die Projektion des z-Einheitsvektors auf a^perp hat Länge r/Omega.
Für einen Zusatz gamma H_C ist die entsprechende Querblocknorm mit
|gamma| zu multiplizieren. Sie verschwindet nicht durch die ursprüngliche
Rotation, denn iA besitzt diesen Querblock gerade nicht.

Damit ist die frühere Ebene für H=M+gamma H_C bei gamma!=0 und c r omega!=0
keine geschlossene Ebene. Für einen geeigneten normierten Anfangszustand
in der Ebene entsteht eine Achsenwahrscheinlichkeit mit führendem Term

    p_axis(t)=gamma² c² r^6 omega² t² / Omega^4 + O(t³).

Der geeignete Zustand ist parallel zu S H_C n. Dies ist kohärente
Leckage innerhalb eines endlichen hermiteschen Systems, keine irreversible
Dämpfung und kein Energieverlust des Gesamtsystems.

## 3. Kann der projizierte native Term eine neue Ebene ermöglichen?

Um diese Frage konkret zu stellen, wähle zusätzlich den triadischen
Kopplungsoperator T=iA und absorbiere dessen reellen Vorfaktor in t_0.
Betrachte den nativen Termen nachgebildeten, konservativen Generator

    H_eff = m_0 I + alpha P M P + t_0 iA + gamma H_C.

Das ist eine explizite Parametrisierung, keine native Bestimmung von T.
Schreibe H_eff=K+iA_eff mit K reell symmetrisch und A_eff reell schiefsymmetrisch.
Die Rotationsachse von A_eff ist

    a_eff=(t_0 nu,-t_0 mu,(t_0+alpha)omega).

Für eine feste Ebene mit reellem Normalenvektor n_eff muss sowohl
K n_eff als auch A_eff n_eff auf dessen Gerade liegen. Für eine reelle
schiefsymmetrische Matrix ist der zweite Eigenwert notwendigerweise null.
Falls a_eff!=0, ist diese Gerade daher genau die Achse a_eff.

Der obere Anteil von a_eff ist orthogonal zu (mu,nu). K wirkt auf ihn
mit Eigenwert m_0+alpha m und auf den unteren Anteil mit Eigenwert
m_0+gamma c r². Wenn beide Anteile ungleich null sind, ist deshalb

    alpha m = gamma c r²

notwendig und hinreichend für eine feste invariante Ebene mit reeller
Normale. Die Aussage gilt unter t_0 r != 0 und (t_0+alpha)omega != 0.
Verschwindet einer dieser Anteile, ist die Achse schon in einem der
K-Eigenräume und die Bedingung ist nicht notwendig. Falls a_eff=0, liegt
ein rein reell symmetrisches Problem vor und diese Achsenklassifikation
ist nicht anzuwenden.

Es gibt also eine konkrete Abstimmung, unter der Projektion und Closure
die schwächere Ebeneninvarianz ermöglichen. Die Gleichung ist eine
zusätzliche Parameterbedingung; ihre Erfüllung, Erhaltung bei veränderlichen
Feldern und etwaige Symmetrieprotektion sind nicht aus dem Paper abgeleitet.

## 4. Ebeneninvarianz genügt nicht für die alte reelle Auslesescheibe

Angenommen, die Bedingung aus Abschnitt 3 gilt im nichtentarteten Fall.
Der reelle Vektor b=(mu,nu,0)/r liegt in der neuen Ebene und hat unter K
den Eigenwert

    k_b = m_0+alpha m+gamma c r².

Die dazu orthogonale reelle Ebenenrichtung liegt im Raum aufgespannt von
(nu,-mu,0) und der z-Achse und hat den Eigenwert

    k_d = m_0+alpha m.

Folglich hat der reduzierte Hamiltonoperator in einer reellen orthonormalen
Ebenenbasis die Form

    H_plane = m_eff I + Omega_eff sigma_y +/- (gamma c r²/2) sigma_z,

wobei das Vorzeichen von der Reihenfolge der Basisvektoren abhängt und
Omega_eff=||a_eff||. Für gamma c r² != 0 bleibt die reale Bloch-Scheibe
b_y=0 unter dieser Dynamik nicht für alle Anfangszustände erhalten.
Beispielsweise erzeugt der sigma_z-Anteil aus einer x-Komponente sofort
eine y-Komponente nach dot b=2 h cross b.

Äquivalent auf Amplitudenebene: Reelle Anfangsvektoren bleiben modulo einer
gemeinsamen Phase für alle Anfangsdaten nur dann reell, wenn der reelle
symmetrische Hamiltonanteil auf der Ebene skalar ist. K hat hier aber zwei
verschiedene Eigenwerte. Die Parameterbedingung aus Abschnitt 3 schließt
somit den Sektor, liefert jedoch nicht das unveränderte frühere Readoutmodell.

Dies verbietet kein anderes Zustandsmodell: Der reduzierte hermitesche
Hamiltonoperator ist auf der vollständigen Bloch-Kugel konsistent. Eine
andere Wahl reeller Struktur/Basis kann ebenfalls möglich sein, verlangt
aber eine entsprechende Übertragung der physischen Auslesungen. Das ist
nicht die bereits geprüfte ursprüngliche reelle Scheibe.

## 5. Bedeutung für die weitere native Untersuchung

Der vorherige Kopplungskandidat ist jetzt an einer konkreten Stelle
gescheitert: Seine ursprüngliche Ebene ist nicht gegen den gemeinsam
aus M gebildeten Closure-Zusatz invariant. Ein abgestimmter projizierter
Term kann eine neue Ebene erhalten, ohne automatisch deren ursprüngliche
Zustands- und Readoutstruktur zu erhalten.

Die nächste belastbare Frage ist daher, welche Relation zwischen dem
tatsächlichen M_16, dem triadischen T und dem nativen Projektor gilt.
Diese Identifikation kann den hier benutzten Ansatz bestätigen oder
ersetzen. Eine weitere beliebige Wahl von Matrizen würde diese fehlende
Information nicht liefern. Anschließend wären Gamma-/Verbindungsanteile,
positive Norm, Hintergrundgleichungen und zeitabhängige Projektoren zu
prüfen. Ein konstant frei verschiebbarer m_0 bleibt in der konservativen
Zustandsdynamik unsichtbar; eine kosmologische Energiedichte ist weiterhin
nicht hergeleitet. OP5 bleibt offen.

## Validierung

Analytische Überprüfung durch explizites Blockprodukt, Projektion von H_C a,
getrennte reelle und imaginäre Invarianzbedingungen sowie die zwei
Eigenwerte des symmetrischen Ebenenanteils. Die Fälle c=0, gamma=0,
r=0, omega=0 und a_eff=0 wurden ausdrücklich getrennt. Keine numerischen
Experimente oder allgemeine Aussagen über ungeprüfte native Sektoren.
