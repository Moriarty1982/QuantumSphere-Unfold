# OP5: Suche nach einer Regel für den absoluten Beitrag

2026-10-26. Basis a97e32d25b4b66ec2d534bdbc142df7b51883057.
Forschungsauftrag: eine Regel suchen, welche den gravitativen konstanten
Volumenterm bestimmt oder seine Wirkung entfernt. Eine bloße Auswahl von
Frame, Phase oder relativem Energieminimum erfüllt diesen Auftrag nicht.

## 1. Quellenlage und Erfolgskriterium

Geprüfte lokale Anker: `OP5_Native_Pair_Potential_Audit.md`,
`HC_Induced_Gravity_Heat_Kernel.md`, `HC_Global_Flux_Selection.md`,
`OP5_Triadic_Stress_And_Neutral_Observer.md`, die native Variationsform und
Closure in `sources/research/parts/v470/10_sphaera_and_physics.tex`, sowie
r67 in `sources/research/parts/v490-post-release-layers.tex`.

r67 bezeichnet die alten kosmologischen Frame-Aussagen selbst als nicht
getragen und lässt die Abbildung von Zählanteilen auf Energiebudget und
Epoche offen. Eine vorhandene normierte Wahrscheinlichkeit ist daher
keine bereits hergeleitete gravitative Normierung. Die native operatorwertige
Closure-Funktion Lambda_cl ist weiterhin von Lambda_cos zu unterscheiden.

Eine brauchbare Regel muss ihren Variationsbereich, ihren absoluten
Maßstab bzw. ihren Mechanismus der Entkopplung und den Umgang mit
zusätzlichen konstanten Beiträgen angeben. Die folgenden drei Routen
wurden analytisch geprüft, nicht lediglich vorgeschlagen.

## 2. Route A: Closure und Energieminimierung

Für eine Wirkung bei unabhängigem metrischem Feld

    S_C[g,Phi]=S_0[g,Phi]-C integral sqrt(-g) d4x

und feldunabhängigem konstanten C gilt bei festem g

    delta S_C/delta Phi = delta S_0/delta Phi,
    T_C = T_0-Cg.

Alle Materie-Stationaritätsbedingungen und ihre Materie-Hesse-Matrix
bleiben gleich. Dasselbe gilt für erlaubte Projektor-Tangentialvariationen,
wenn der Volumenterm nicht von ihnen abhängt. Eine Regel aus genau
diesen Daten unterscheidet die Familie C nicht. Dies ist eine begrenzte
Unbestimmtheitsaussage, kein allgemeines Verbot von Anpassungsmechanismen.

Die nativen Strafen U_C7 und U_HC können bei Closure verschwinden.
Sie fixieren damit ihren eigenen Minimalwert, nicht automatisch den
gesamten konstanten Term der effektiven Wirkung. Die frühere
Determinantenrechnung erzeugt gerade zusätzliche Beiträge. Ihre
bosonisch/fermionische Vergleichskompensation benötigt tatsächliche
Feldstatistik und Spektralpaarung; eine interne Frameverdopplung liefert
diese Voraussetzungen nicht.

Auch die vorhandene Flussregel E_min=pi q²/(g² R²) legt nur einen
Beitrag bei vorausgesetztem q,g,R und harter Kompatibilität fest. Ein
zusätzlicher feldunabhängiger C bleibt möglich. Die dort gezeigte
Instabilität beim Freigeben der Kompatibilität wird nicht übergangen.

Wichtige Ausnahme: Ist g=g[Phi] eine zusammengesetzte Geometrie, wird
delta integral sqrt(-g[Phi])/delta Phi im Allgemeinen nicht null.
Dann kann C die Probe-Gleichung beeinflussen. Das bloße Einsetzen eines
zusammengesetzten Frames ist aber keine fertige Auswahlregel: Die
vollständige Kettenregel, erlaubten Variationen und Gleichungen sind nötig.
Die früheren gemeinsamen/zusammengesetzten Wirkungsprüfungen haben genau
diese offene Pflicht gezeigt. Diese Route bleibt deshalb offen, nicht
durch den obigen Satz widerlegt.

## 3. Route B: Eine dynamische Skala

Als Test eines zusätzlichen klassisch skalenhomogenen Potentials sei

    V(chi,theta)=chi^4 F(theta),   chi>0.

Stationarität verlangt F=0 und F'=0. Damit ist V=0, aber diese beiden
Bedingungen sind nicht automatisch erfüllt: Ein stationärer Winkel
benötigt zusätzlich einen verschwindenden Funktionswert. Für
F=lambda(theta²-v²)²+epsilon, lambda>0, ist an theta=+/-v der Wert
epsilon. Für epsilon!=0 ist dort keine nichtverschwindende stationäre
Skala möglich. Der Term epsilon chi^4 respektiert die angenommene
Homogenität; reine Skalenhomogenität verbietet ihn nicht.

Bei einem gemeinsamen Nullpunkt F=F'=0 ist die chi-Richtung flach:
V_chichi=0 und V_chitheta=0. Eine endliche stabile Skala folgt daraus
noch nicht. Ein unabhängiger C würde V auf C verschieben, ohne diese
Stationaritätsgleichungen zu ändern; eine exakte Skalensymmetrie müsste
einen solchen Term in der ganzen Wirkung tatsächlich ausschließen.

Eine explizite logarithmische Vergleichskorrektur zeigt die Empfindlichkeit:

    V=chi^4[F(theta)+B log(chi/mu)]+C,
    V_stationaer=C-B chi^4/4,
    V_chichi=4B chi²                 [F'=0, B konstant].

Für B>0 ist die radiale Krümmung positiv, aber der Wert wird nicht
automatisch null. Die Gleichung C=B chi^4/4 wäre eine zusätzliche
Abstimmung; C kommt in den beiden Stationaritätsgleichungen nicht vor.
Der Logarithmus ist ein mathematischer Kontrollfall, keine berechnete
native Quantenkorrektur. Kein neuer Skalenpartner wird im Paper eingeführt.

Ergebnis: Diese konkrete Skalenregel liefert keine generische Auswahl
eines endlichen stabilen Nullvakuums aus den bisherigen Eingaben.

## 4. Route C: Normierung der gesamten Wirkung

Eine tatsächlich wirksame, aber zusätzliche Vorschrift lässt sich exakt
prüfen. Sei A konstant und ungleich null, auf einem Gebiet mit endlichem
positivem Raumzeitvolumen V4:

    I=integral sqrt(-g)[A R+L_m],
    V4=integral sqrt(-g),
    S_N=I/V4,    sigma=I/V4.

Für eine dimensionslose Wirkung kann S_N durch eine feste Dichteskala
geteilt werden; dieser konstante Faktor ändert die klassischen Extrema
nicht. Kompakt getragene Variationen bzw. geeignete Randdaten werden
vorausgesetzt. Bei jeder Variation gilt

    delta S_N=(delta I-sigma delta V4)/V4.

Mit T_mu,nu=-2/sqrt(-g) delta I_m/delta g^{mu nu} folgt

    2A G_mu,nu = T_mu,nu-sigma g_mu,nu.

sigma wird bei dieser ersten Variation nicht unabhängig variiert; es ist
der Wert des Quotienten auf der gesuchten Gesamtlösung. Eine vorherige
Ersetzung durch eine lokal beliebige Funktion wäre eine andere Theorie.

Bei L_m->L_m-C gilt T->T-Cg und sigma->sigma-C. Die rechte Seite
bleibt exakt gleich. Der Mechanismus ist somit eine Entkopplung des
konstanten Zusatzes, nicht eine Berechnung seines mikroskopischen Werts.

Für reines konstantes Vakuum L_m=-rho_v folgt sigma=A<R>-rho_v
und 2A G=-A<R>g. Die Spur ergibt R=2<R>; Mittelung derselben
Gleichung ergibt <R>=0, also R=0 und R_mu,nu=0. Dies gilt unter
den angegebenen globalen Integrabilitäts- und Randannahmen.

Mit zusätzlicher Materie bleibt die globale Konsistenzbedingung wichtig:

    2A<R>=<T>-4<L_m>,
    sigma=<T>/2-<L_m>.

Es wird daher nicht behauptet, jede materiegefüllte Lösung habe einen
verschwindenden effektiven kosmologischen Term. Ebenso wenig ergibt
dies eine Vorhersage des beobachteten positiven dunklen Energieanteils.

Diese Route ist keine neue Entdeckung: Davidson und Rubin,
*Zero Cosmological Constant from Normalized General Relativity*,
arXiv:0905.0661v3, insbesondere (4) und folgende Variationen, untersuchen
genau eine Volumennormierung. Ihre Krümmungs-/Vorzeichenkonvention ist
anders; oben steht die eigene Ableitung mit A R und T=-2delta I_m/delta g.
Quelle: https://arxiv.org/html/0905.0661v3

Die Normierung ist eine Änderung des Wirkungsprinzips. Eine unendliche
Raumzeit erfordert eine wohldefinierte Grenzwert-/Randvorschrift; ein
beliebig gewähltes Beobachtungsfenster ist kein Ersatz. Lokale Materie-
Gleichungen sind unter den Voraussetzungen unverändert, aber die
Gravitationsgleichung trägt eine globale Bedingung. Eine Quantisierung
oder radiative Stabilität des nativen Modells ist damit nicht bewiesen.

## 5. Scharfer Test einer möglichen QAM-Brücke

Man darf nicht jede Normierung mit Route C identifizieren. Für einen
anderen Nenner D[g,Phi], etwa integral sqrt(-g) w(Phi), ist

    S_D=I/D,    S_D[L_m-C]=S_D[L_m]-C V4/D.

Die Variation des Zusatzes verschwindet genau dann für alle erlaubten
Variationen, wenn delta(V4/D)=0. Ein hinreichender Fall ist D=k V4 mit
konstantem k innerhalb des zulässigen Variationsbereichs. Feldabhängige
Gewichte oder eine punktweise Norm Tr(rho)=1 erfüllen dies nicht allein.

Das ist der konkrete Test für eine native Auswahlregel: Gibt es eine aus
der QAM/Closure hergeleitete Wirkungsnormierung, deren Nenner bei den
wirklich erlaubten Feld- und Metrikvariationen proportional zum
Raumzeitvolumen ist? In den gezielt geprüften nativen Wirkungs-,
Closure- und r67-Passagen ist diese Identifikation nicht angegeben.
Die Suche belegt kein universelles Nichtvorhandensein in jeder denkbaren
Fortsetzung; sie dokumentiert den fehlenden Schritt in diesen Quellen.

Eine Alternative mit fest vorgeschriebenem Gesamtvolumen ist ebenfalls
nicht automatisch Route C: eingeschränkte Volumenvariationen machen
einen konstanten Term unsichtbar, lassen aber im Allgemeinen einen
Integrations-/Multiplikatorwert offen. Eine Nullauswahl muss dann aus
einer weiteren Bedingung folgen.

## 6. Stand der Suche und nächste entscheidende Eingabe

Die bisherigen Closure-/Frame-Regeln liefern keine absolute Auswahl
unter unabhängiger Metrikvariation. Der skalare Anpassungstest braucht
eine zusätzliche geschützte Nullstelle und eine Skalenfestlegung.
Die Volumennormierung liefert einen klaren klassischen Mechanismus der
Konstantenentkopplung, ist aber bisher eine externe Zusatzhypothese.

Die offene Forschungsroute ist jetzt präziser: Entweder die tatsächliche
zusammengesetzte Geometrie liefert durch ihre vollständige Variation eine
weitere Gleichung, oder das native Wirkungs-/Maßprinzip erzeugt eine
Normierung mit delta(V4/D)=0 bzw. einen anderen geschützten Mechanismus.
Ein bloßes Postulieren dieses Nenners wäre eine neue Theorieentscheidung.
Die native Herleitung und der beobachtete Rest bleiben ungelöst; OP5 wird
nicht geschlossen. Haupttext, Issues und Release bleiben unverändert.

Ein weiterer nativer Anknüpfungstest lässt sich bereits auswerten:
Für die nichtaffine bilineare Vergleichscoframe E=C[Psi,H] in
`HC_Two_Frame_Action_Bridge.md`, bei festem H, fester Verbindung und
festem Normierungsfaktor, liefert eine konstante reelle Skalierung
Psi->lambda Psi genau E->lambda²E. Auf einem nichtentarteten
orientierungsfesten vierdimensionalen Bereich folgt

    g->lambda^4 g,  sqrt(-g)->lambda^8 sqrt(-g),
    d V4/d log(lambda)=8 V4.

Wenn diese Skalierungsvariation erlaubt ist, trägt ein Zusatz -C V4
also -8C V4 zur globalen Skalengleichung bei. Die zusammengesetzte
Geometrie ist damit nicht automatisch gegen C unempfindlich. Dies lässt
eine zusätzliche Anpassungsgleichung prinzipiell zu, liefert sie aber
noch nicht gelöst: Die übrige Wirkung trägt ebenfalls zur Gleichung bei.
Die globale Variation setzt passende Randdaten voraus; lokale
Skalierungen bringen zusätzliche Ableitungsterme. Bei einer strikt
normierten Probe kann diese Variation ausgeschlossen sein, was aus dem
Variationsvertrag zu begründen wäre. Die affine alternative Co-Frame
E=theta+C folgt nicht demselben Homogenitätsgesetz. Eine native
Nullauswahl wird aus keinem dieser Fälle abgeleitet.

## 7. Prüfung

Analytische Nachrechnung der konstanten Verschiebung, Skalenableitungen,
Quotientenvariation, Vakuum-Spur/Mittelung und des allgemeinen Nennertests.
Unabhängige Prüfung der drei Kernrouten:
`OP5_Absolute_Selection_Independent.md`. Keine numerische Simulation wird
als Beweis verwendet. Die lokale Quellenbindung steht im Provenienz-Snapshot.
