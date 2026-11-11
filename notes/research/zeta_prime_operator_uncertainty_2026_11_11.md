# Zeta und Unschärfe: ein arithmetischer Partner zum HC

11. November 2026, Codex. Analytische Erkundung, ausdrücklich nicht blind.
Keine neue H-Nummer oder numerische Suche. Modell: komplexes L²(R,dt);
t ist dimensionslos. Kein nativer M/T/P-Frame wird identifiziert.

## Vorwissen und Rückwärtssuche

Ausgangspunkt: `zeta_hc_uncertainty_exploration_2026_11_11.md`.
Zur Parität R fehlt ein nativ begründeter selbstadjungierter Partner A mit
RA=-AR. Eine Eigenzustandsregel für -iRA könnte die HC-Balance auswählen.
Die vorige Signumwahl erzeugte eine generische Pauli-Algebra; Sättigung
der Unschärferelation allein selektierte dort keine Balance.

Geprüft: r04 in `sources/research/parts/v480-post-release-layers.tex`
(frühere globale Zeta-Spektralidentifikation nicht erhalten),
`analysis/HC_Lepton_Readout_Identification.md`, `analysis/HC_Root_Readout.md`
und die vorige Erkundung. Suche nach Mangoldt/logarithmischer Ableitung/
Primzahloperatoren in analysis und Forschungsnotizen lieferte keine native
Konstruktion des folgenden Multiplikators. QAM-Suche `prime`: kein Treffer;
kein MMA-Beleg beansprucht. Die zurückgestellte CRT-Idee I2 liefert keine
Identifikation mit dieser Dirichletreihe; kein neuer Auslöser von I1–I5.

Rückwärtssuche: Erst einen arithmetisch bestimmten ungeraden Operator
konstruieren, dann die Existenz der benötigten Auswahlzustände prüfen.
Keine Nullstellen-, Phasen- oder Massenfits.

## 1. Zeta liefert einen zweiten Operator

Für festes sigma>1 gilt

$$
-\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)}
=\sum_{n\geq2}\frac{\Lambda(n)}{n^\sigma}e^{-it\log n}.
$$

Lambda(p^k)=log p, sonst null. Quelle:
[NIST DLMF 27.4.12](https://dlmf.nist.gov/27.4#E12).
Setze

$$
a_\sigma(t)=\sum_{n\geq2}\frac{\Lambda(n)}{n^\sigma}\sin(t\log n)
=\operatorname{Im}\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)},
\qquad (A_\sigma f)(t)=a_\sigma(t)f(t).
$$

Die Reihe konvergiert für reelles t absolut und gleichmäßig, weil
Lambda(n)<=log n und Summe log(n)/n^sigma endlich ist. A_sigma ist daher
beschränkt und selbstadjungiert auf ganz L². Der Multiplikator ist reell
und ungerade, also RA_sigma=-A_sigma R für Rf(t)=f(-t).
Dies ist eine arithmetische Vergleichsoperation, keine hergeleitete
Kopplung der Companion-Wirkung.

Gemeinsam mit R gilt die Robertson-Unschärferelation

$$
\Delta R\,\Delta A_\sigma\geq|\langle RA_\sigma\rangle|.
$$

Die Anwendung folgt direkt aus [R,A_sigma]=2RA_sigma und Robertson;
siehe [Originalquelle](https://www2.unicamp.br/~chibeni/textosdidaticos/robertson-1929.pdf).
Für ein gerades normiertes Zeta-Profil bleiben <R>=1 und
<A_sigma>=<RA_sigma>=0. Die Relation fordert keinen Balancewechsel.

## 2. Die stärkere Auswahlregel scheitert hier an der Normalisierbarkeit

T_sigma=-iRA_sigma ist beschränkt selbstadjungiert, antikommutiert mit R
und erfüllt T_sigma²=A_sigma². Ein normierter Eigenzustand mit reellem
Eigenwert lambda ungleich null würde deshalb <R>=0 erfüllen.

Aber dieser konkrete T_sigma hat überhaupt keine nichtnulligen
L²-Eigenzustände, auch nicht zum Eigenwert null:

1. a_sigma ist reell-analytisch: Die Sinusreihe ist holomorph im Streifen
   |Im t|<sigma-1, auf kleineren Streifen normal konvergent.
2. a_sigma(0)=0 und a_sigma'(0)=Summe Lambda(n) log(n)/n^sigma>0.
   Also ist a_sigma² nicht konstant.
3. Die Eigenwertgleichung impliziert
   (a_sigma(t)²-lambda²)psi(t)=0 fast überall.
4. Jede solche Niveaumenge ist als Nullmenge einer nichttrivialen
   reell-analytischen Funktion diskret und hat Lebesgue-Maß null.
   Ein dort getragener L²-Zustand ist null.

Das schließt diese exakte Auswahlroute aus, nicht jede Kombination von
Zeta und Unschärfe. Ein diskretes Gitter könnte künstliche Eigenvektoren
anzeigen; es wäre kein Gegenbeleg zum kontinuierlichen Resultat.

## 3. Verbleibende Möglichkeiten und Grenzen

Wellenpakete nahe t0>0 plus ihre Spiegelbilder mit relativem Faktor ±i
können exakt paritätsbalanciert und bei geringer Variation von a_sigma
approximative T-Eigenzustände sein. Gewicht und Phase sind dann aber
bereits eingesetzt; keine unabhängige Auswahl oder Massenvorhersage.
Engere Lokalisierung geht mit wachsender Fourier-Streuung einher;
ein physikalischer Orts-/Impulsmaßstab ist nicht identifiziert.

S_sigma=sgn(A_sigma) ist wegen der maßnulligen Nullmenge eine
selbstadjungierte Involution und antikommutiert mit R. Dann besitzt
-iRS_sigma balancierte Eigenzustände wie im vorigen Spielmodell.
Diese spektrale Abflachung ist aber eine zusätzliche Operation und
verwirft die arithmetischen Beträge. An Vorzeichenwechseln können erneut
Sprünge und damit Impulsdomänenprobleme auftreten.

Der Bereich sigma>1 ist verbindlich. Zur kritischen Linie sigma=1/2
darf weder die konvergente Primzahlreihe noch die bewiesene beschränkte
Operatorrealisierung ungeprüft übertragen werden. Eine Fortsetzung
von zeta'/zeta braucht eine eigene Singularitäts- und Domänenanalyse.

## Ergebnis

Ein echter arithmetischer Partner mit HC-Antikommutation und gemeinsamer
Unschärferelation ist konstruiert. Die exakte Auswahl über T-Eigenzustände
ist in dieser Multiplikatorrealisierung ausgeschlossen. Zeta-Profil und
Unschärfe allein erzwingen weiterhin keine Balance.

Vor Simulationen ist nun eine native nichtlokale Kopplung oder ein Generator
mit normalisierbaren Auswahlzuständen zu suchen. Die fehlende Operation
darf nicht bloß zum Erzwingen von h=0 eingeführt werden. Native Abbildung B,
positive Generationenauslesung, Phase und Massenskala bleiben offen.

Validierung: direkte Herleitung und mathematische Selbstprüfung von
Vorzeichen, Konvergenz, Adjungiertheit und Eigenzustandsargument.
Keine numerischen Belege, QAM-Beweisfreigaben oder OP-Schließungen.
