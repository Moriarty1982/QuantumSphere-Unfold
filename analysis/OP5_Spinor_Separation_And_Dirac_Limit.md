# OP5: Spinortrennung verschärft den Transporttest

26. Oktober 2026. Lokale Fortsetzung von
`OP5_Native_Projector_Transport_Test.md`. Keine Manuskriptänderung.

## Fragestellung und Urteil

Kann die zuvor gefundene Normalgleichung eine echte Kompensation zwischen
Projektorbewegung und triadischer Kopplung für jeden zulässigen Spinorzustand
liefern? Im üblichen faktorisierten Dirac-Sektor lautet das Urteil:
**nein, außer beide Queranteile verschwinden getrennt**. Dies ist ein
bedingter algebraischer Satz. Für spinabhängige interne Kopplungen oder
einen eingeschränkten Spinorraum ist die Behauptung nicht bewiesen.

Die native physikalische Realisierung dieser Faktorisierung ist weiterhin
offen. Sie wird bereits in `analysis/HC_Real_Probe_Current_Closure.md` und
`sources/research/parts/hc-dynamics-and-geometry.tex`, „Probe Reality,
Matrix Currents and Background Reactions“, als zusätzliche Annahme behandelt.

## 1. Genaue Voraussetzungen

Arbeite punktweise auf V_internal tensor S_Dirac. P ist ein glatter
orthogonaler interner Projektor, Q=I-P, A_mu ist intern hermitesch und
T wirkt ebenfalls nur intern. Gamma^mu wirkt nur auf dem vierdimensionalen
Dirac-Faktor. Seine Clifford-Form ist nichtentartet, mit Konvention

    {Gamma^mu,Gamma^nu}=2 epsilon g^{mu nu} I,
    epsilon=+1 oder -1,
    tr_spin Gamma^mu=0,
    tr_spin(Gamma^nu Gamma^mu)=4 epsilon g^{nu mu}.

Die Aussage verwendet den gesamten Dirac-Faktor, nicht bloß einen
ausgewählten Spinor. Die Clifford-Matrizen und g dürfen punktabhängig sein;
die Rechnung enthält keine Ableitungen von Gamma.

Definiere

    nabla_mu P=partial_mu P+i[A_mu,P],
    X_mu=Q(nabla_mu P)P,    Y=beta g_Y Q T P.

Die zuvor exakt hergeleitete Normalgleichung lautet als Operatorbedingung

    N=i sum_mu X_mu tensor Gamma^mu - Y tensor I = 0.

Sie ist die Forderung nach Normalverträglichkeit für jeden momentanen
Spinorzustand im P-Sektor. Eine einzelne Lösung N Psi=0 ist schwächer.

## 2. Beweis der getrennten Bedingungen

Die partielle Spinorspur der Gleichung N=0 ergibt -4Y=0, also Y=0.
Multipliziere N anschließend auf dem Spinorfaktor mit Gamma^nu und bilde
erneut die partielle Spur. Es folgt

    4 i epsilon sum_mu g^{nu mu} X_mu=0.

Da g nichtentartet ist, verschwinden alle X_mu. Umgekehrt implizieren
X_mu=0 und Y=0 unmittelbar N=0. Damit gilt exakt

    N=0  iff  X_mu=0 für alle mu und Y=0.

Aus P²=P folgt P(nabla_mu P)P=Q(nabla_mu P)Q=0. Weil P und A_mu
hermitesch sind, ist nabla_mu P hermitesch. Der zweite Querblock ist
deshalb X_mu†. Somit gilt unter den genannten Voraussetzungen sogar

    N=0  iff  nabla_mu P=0 für alle mu und beta g_Y Q T P=0.

Bei beta g_Y!=0 muss QTP=0 sein; bei verschwindendem Vorfaktor muss T
selbst nicht sektorverträglich sein. Falls T hermitesch ist, folgt aus
QTP=0 auch PTQ=0, also [T,P]=0.

Die in der vorherigen Notiz offengelassene direkte Kompensation ist somit
im uneingeschränkten faktorisierten Dirac-Sektor nicht verfügbar. Sie
bliebe eine gesonderte Möglichkeit bei spinabhängigem T, anderer
Clifford-Realisierung oder auf ausdrücklich eingeschränkten Zustandsräumen.
Das muss jeweils mit dem tatsächlichen Träger geprüft werden.

## 3. Projektortransport hat eine geometrische Integrabilitätsbedingung

Für nabla_mu=partial_mu+i[A_mu,.] gilt durch Ausmultiplizieren

    [nabla_mu,nabla_nu]P=i[F^A_mu nu,P],
    F^A_mu nu=partial_mu A_nu-partial_nu A_mu+i[A_mu,A_nu].

Aus nabla_mu P=0 folgt daher [F^A_mu nu,P]=0. Die Krümmung muss dieselbe
Sektorzerlegung erhalten. Krümmungskommutativität an einem einzelnen
Punkt ist umgekehrt kein Beweis für eine glatte parallele Projektorfamilie
in einer Region. Auch die gemeinsame Verträglichkeit entlang verschiedener
Transportwege ist zu prüfen.

In einer lokalen orthonormalen internen Basis, in der der glatte Projektor
konstant ist, reduziert sich nabla_mu P=0 auf [A_mu,P]=0. Der bewegte
Projektor ist daher in diesem Fall keine zusätzliche physikalische Quelle:
Die Verbindung transportiert eine gemeinsame Zerlegung. Eine solche Basis
kann lokal gewählt werden; globale Topologie ist damit nicht entschieden.

## 4. Konsequenz für die dritte Mode

Wenn zwei beibehaltene Moden im P-Sektor und die dritte im Q-Sektor liegen,
ist eine nichtverschwindende triadische Kopplung zwischen ihnen bei
beta g_Y!=0 mit dieser universellen geschlossenen P-Reduktion unvereinbar.
Eine dritte Mode kann aber ebenfalls innerhalb des P-Sektors liegen.
Dann ist ihre interne Kopplung erlaubt und ein dortiges Zweimodenmodell
eventuell eine zusätzliche Reduktion innerhalb eines größeren physischen
Sektors. Weder der Name C7 noch die bisherige Dreimodenzeichnung bestimmt
diese Einbettung oder den Rang des tatsächlich realisierten P hier allein.

Damit sind physische Closure und das Weglassen einer internen dritten
Mode unterschiedliche Anforderungen. Ihre Gleichsetzung hatte die
vorherigen Vergleichsmodelle zusätzlich eingeschränkt.

## 5. Ein fehlender Zusatz im gedruckten Dirac-Grenzfall

Quelle: `sources/research/parts/v470/10_sphaera_and_physics.tex`,
`prop:dirac-limit` bei „Controlled limiting regimes“. Genannt werden exakte
Closure R_C=0, A_mu=0 und skalares Omega auf dem geschlossenen Sektor.
Die dort angegebene Reduktion benötigt außerdem die Verträglichkeit des
möglicherweise x-abhängigen Projektors mit der Ableitung. Im hier
untersuchten faktorisierten Sektor ist das partial_mu P=0, wenn die
Reduktion für jeden P-Spinorzustand gelten soll.

Ein expliziter kinematischer Gegencheck der genannten Probe-Voraussetzungen:
M=0, daher R_C=H_C=0; A_mu=0; Omega=m I; räumlich homogene Zustände.
Wähle intern V=C² und

    p(t)=(cos(theta(t)),sin(theta(t)))^T,
    P(t)=|p(t)><p(t)|,    theta(0)=0.

Die freie Probe-Gleichung liefert bei Anfangszustand u_1 tensor s

    Psi(t)=u_1 tensor exp[-i m (Gamma^0)^(-1)t] s,

für konstantes invertierbares Gamma^0. Ihr interner Vektor bleibt u_1.
Er liegt für allgemeines theta(t) nicht mehr in ran P(t); der relative
interne Q-Anteil hat Normquadrat sin²(theta(t)). Alle genannten
Closure-/Skalarmassenbedingungen bleiben formal erfüllt, aber die
gleichzeitige Forderung P(t)Psi(t)=Psi(t) scheitert an der Projektorbewegung.

Das Gegenbeispiel betrifft die Suffizienz der aufgezählten Voraussetzungen
für eine universelle Probe-Reduktion. Es behauptet keine Lösung des vollen
gekoppelten Feldsystems mit willkürlich vorgeschriebenem P(t). Wenn andere
Feldgleichungen P bereits konstant oder kovariant parallel erzwingen,
wäre genau diese fehlende Voraussetzung nachzuliefern. Keine Korrektur
am Manuskript wurde vorgenommen.

## Ergebnis für OP5 und nächste konkrete Verpflichtung

Eine zeitabhängige Wahl des lesenden Frames repariert den offenen Übergang
im Standardfall nicht beliebig. Der physische Projektor muss kovariant
parallel sein und die triadische Kopplung muss seinen Sektor erhalten.
Das ist nun ein expliziter Test an den tatsächlichen nativen Feldern.

Für eine andere Lösung ist die tatsächlich nichtfaktorisierte Darstellung
oder der physisch zulässige eingeschränkte Spinorraum anzugeben. Selbst
erfolgreiche Closure bestimmt den skalaren Energieoffset nicht. OP5 bleibt
offen; die hier geprüfte Kompensationsroute ist unter den klar genannten
Standardannahmen ausgeschlossen.

## Validierung

Exakter analytischer Beweis durch partielle Spinorspuren, Projektorableitung
und Ausmultiplizieren des kovarianten Kommutators. Das rotierende
Projektorbeispiel wurde direkt in freie Evolution und Sektorbedingung
eingesetzt. Keine numerischen Stichproben, kein Anspruch auf einen
Ausschluss aller nativen Realisierungen.
