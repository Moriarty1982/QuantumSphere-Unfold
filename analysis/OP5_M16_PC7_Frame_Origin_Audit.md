# M16 und P_C7: Haben die Herleitungen einen falschen Frame mitgeschleppt?

26. Oktober 2026. Checkpoint `OP5-M16-PC7-FRAME-ORIGIN-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Fokussierte Quellen- und Herleitungsprüfung; keine Manuskriptänderung.

## 1. Urteil und Reichweite

**Primäres Urteil: unvollständig, mit fehlender gemeinsamer nativer
Realisierung und Transformationsvorschrift.**

Es gibt einen belegten Frame-Fehler bei der historischen physikalischen
Benennung: Der alte „Photon-Frame“ wird in r24 als reiner Referenzzustand R
identifiziert, während der Photon-Zustand der späteren Convention F
maximal gemischt ist. Dieser Fehler berührt die physische Interpretation
der auf ihn bezogenen Skalen, Zustände und des Frame-Terms.

Die geprüften Definitionen liefern dagegen keine ausgewerteten gemeinsamen
M16-/P_C7-Matrixeinträge, deren Entstehung sich auf diesen Frame zurückführen
und durch einen Frame-Wechsel numerisch korrigieren ließe. M16 wird
strukturell eingeführt; P_C7 durch Zulässigkeits-, Spur- und
Projektorbedingungen. Ihre physische Verbindung bleibt unvollständig.
„Beide Matrizen wurden nachweislich falsch berechnet“ wäre deshalb ebenso
unbelegt wie „beide sind nachweislich physikalisch frameunabhängig“.

Ein relational neu bestimmter Sektor kann relevant sein. Ein gemeinsamer
passiver Basiswechsel oder ein unkontrolliertes Mitteln von Projektoren
repariert die Lücke aber nicht. Die folgenden exakten Kontrollen trennen
diese Möglichkeiten.

Die Prüfung betrifft die vorhandene Forschungsquelle und ihre benannten
Entwicklungslagen, nicht eine lückenlose Rekonstruktion der privaten
historischen Entstehung oder aller veröffentlichten PDFs.

## 2. Die tatsächliche Abhängigkeitskette

| Ebene | Quelle / Locator | Tatsächliche Festlegung | Möglicher übernommener Fehler |
|---|---|---|---|
| Strukturelle Involution und HC | `v470/12_structural_core.tex`, `def:tensor-structural-kernel`, T1–T4 | J²=I, C²=C, [M,J]=[M,C]=0 als Zulässigkeitsbedingung | Die konkrete Darstellung von J und die physische Auswahl seiner Sektoren müssen gerechtfertigt werden. T4 leitet sie nicht unabhängig her. |
| Globale M16 | `v470/16_master_model.tex`, `sec:millennium-hc` | Transport desselben Objekts durch Schichten; formale vierteilige Layer-Zerlegung | Strukturtransport ist noch kein eindeutig bestimmter Hamiltonoperator, keine gemessene Frequenz und keine ausgewertete 16x16-Matrix. |
| Nullachse und Photon-Fixsektor | `v470/10_sphaera_and_physics.tex`, `sec:fractal`; `16_master_model.tex`, `thm:master-structural` | Eine strukturelle Nullachse wird als Lichtachse und terminaler Photonsektor gelesen | Der Übergang zur physischen Photoninterpretation benötigt eine gemeinsame Zustands-/Regimeabbildung. Ein Nullvektor oder struktureller Fixsektor ist nicht automatisch der spätere gemischte Doublet-Zustand. |
| Meta-Septum P_C7 | `10_sphaera_and_physics.tex`, „Meta-Septum closure“, `thm:dirac-probe`, „Probe--closure field content“ | Tr(M16 P_C7) modulo HC, P²=P, P Psi=Psi; Bezug zum phasenverschobenen GUE-Taktgeber | Keine expliziten gemeinsamen Eigenvektoren, keine berechnete relative Orientierung von P und Taktgeber, an dieser Stelle keine positive Orthogonalitätsherleitung. |
| Physikalische Probe | dieselbe Datei, `thm:master-field-equation` | Symbolische Summe aus m_0, P M P, Triad und H_C | Die Projektion kann fehlende Querblöcke unsichtbar machen. Die behauptete Kompatibilität ist nicht schon ihre Berechnung. |
| Gemeinsamer Generator | `v470/13_hc_hypotheses.tex`, `hyp:hc-meta-generator` | Eine gemeinsame Erzeugergleichung mit Frame-Projektionen ist ausdrücklich Hypothese | Die physikalischen Regime sind nicht bereits aus einer ausgewerteten Eltern-Gleichung gemeinsam abgeleitet. |
| Doublet-Matrix | `v490-post-release-layers.tex`, r05.1 | M=lambda_+ C+lambda_-(I-C) als Portgewichtung; volle M16 ausdrücklich nicht identifiziert | Doublet-Framebilder dürfen nicht ohne Einbettung auf M16/P_C7 übertragen werden. |
| Korrigierter Referenzframe | dieselbe Datei, r24.3 und F5–F7 | Historischer „Photon-Frame“ ist R mit Reinheit 1; Photon P hat b=0 | Konkrete historische Referenz-/Photon-Verwechslung. Sie ist kein bereits berechneter korrigierter P_C7. |

Diese Kette zeigt eine mögliche Vererbung von Interpretationsannahmen.
Sie liefert keine Beweiskette „Photon-Referenzwert -> konkrete M16-Einträge
-> konkrete P_C7-Eigenvektoren“. Gerade der mittlere Übergang fehlt.

## 3. Bereits vorhandene native Verknüpfungsprüfung einbezogen

`sources/research/parts/native-operator-link.tex` ist bereits über
`sources/research/v480-companion.tex` eingebunden. Die begleitende Notiz
`analysis/Native_Operator_Link_Audit.md` dokumentiert die gemeinsame
Operatorlücke schon vom 15. Oktober. Diese Quelle war in unserer letzten
Zusammenführung nicht berücksichtigt; mehrere jüngst rekonstruierte
Block- und Kovarianzergebnisse sind daher Bestätigungen vorhandener
Resultate, keine erstmaligen Entdeckungen.

Besonders relevant sind dort:

- `v480:native-source-link`: Projektorbedingung und Uhrspektrum bestimmen
  keine gemeinsamen Matrixelemente; keine Identifikation des Taktgebers
  mit M16 ist gegeben.
- `v480:native-isospectral-freedom`: Gleiches Uhrspektrum bei festem P
  kann durch relative Eigenvektordrehung andere Übergangsspektren liefern.
- `v480:native-frame-covariance`: Eine gemeinsame unitäre Transformation
  von Projektor, Uhr und normierten Seeds erhält die spektralen Verhältnisse
  der dort ausdrücklich bedingten Gram-Massengesetzgebung.
- `v480:native-penalty-identity`: Die beiden minimalen Closure-Terme
  stimmen im orthogonalen positiven Sektor überein; das ist schon bewiesen.
- `v480:native-block-mass-law`: Ein nach Elimination gekleideter leichter
  Spektralsektor kann invariant sein, ohne mit dem ursprünglichen strikten
  P-Sektor übereinzustimmen. Eine solche Neuwahl ist eine physische
  Modellentscheidung, keine passive Umbenennung.

Keine dieser Aussagen identifiziert eine tatsächliche Lorentztransformation
mit einer unitären Operation im gewählten positiven internen Skalarprodukt.

## 4. Exakter Test A: gemeinsamer Frame-Wechsel repariert keinen Defekt

Für unitäres U und ein gemeinsames positives Skalarprodukt transformiere

    M'=U M U†,    P'=U P U†,    J'=U J U†,    C'=U C U†.

Dann gelten

    [M',P']=U[M,P]U†,
    H_C'=U H_C U†,
    Tr(M'P')=Tr(MP).

Nullität, Rang und Spektrum des positiven Defekts bleiben erhalten.
Ein problematischer gemeinsamer passiver Frame kann deshalb nicht durch
eine gemeinsame unitäre Umbenennung eine Closure-Verletzung entfernen.
Bei einem invertierbaren nichtunitären Koordinatenwechsel bleibt der
Kommutator ähnlich transformiert; für Positivität und Normen muss dann
auch die Metrik und damit die Adjungierte mittransportiert werden.
Festhalten der alten Adjungierten wäre ein anderes Modell.

Für lokale Framewechsel gehört außerdem die inhomogene Transformation
der Verbindung dazu. Nur M und P umzurechnen, A_mu aber festzuhalten,
ist kein Nachweis der Kovarianz der ganzen Gleichung.

## 5. Exakter Test B: relative Frame-/Sektorwahl kann einen Fehler erzeugen

Nimm M=diag(1,-1), p_theta=(cos theta,sin theta)^T und
P_theta=|p_theta><p_theta| im gewöhnlichen positiven C². Dann

    H_C(M,P_theta)=(rho+sigma) sin²(2 theta) I_2.

Für theta=0 ist der Defekt null; für theta=pi/4 ist er maximal.
M hat dabei unverändert dieselben Eigenwerte. Rotiert man M zusammen
mit P_theta, verschwindet der Defekt dagegen weiterhin. Das zeigt exakt,
welcher Fehler prinzipiell mitgeschleppt sein kann: eine unberechtigt
festgelegte relative Lage des Projektors gegenüber M bzw. der Uhr.

Das Beispiel beweist nicht, dass der native P_C7 so gewählt wurde.
Es zeigt, warum die fehlenden gemeinsamen Eigenvektoren physikalisch
entscheidend und nicht durch ein bekanntes Spektrum ersetzbar sind.

Für selbstadjungiertes M könnte man nachträglich irgendeinen seiner
Spektralprojektoren als P wählen und so [M,P]=0 erzwingen. Ohne unabhängige
physikalische Auswahl wäre das zirkulär: Closure wird eingebaut und nicht
aus den ursprünglichen Sektorbedingungen hergeleitet.

## 6. Exakter Test C: frühe Projektion kann das Problem verbergen

Sei P=diag(1,0). Die beiden Operatoren M_1=0 und M_2=sigma_x besitzen
denselben projizierten Block P M_j P=0. Trotzdem

    H_C(M_1,P)=0,    H_C(M_2,P)=(rho+sigma) I_2.

Wer nur den projizierten Block liest, kann die völlig verschiedene
Off-Sektor-Dynamik nicht zurückgewinnen. Deshalb ist beim Zurückgehen
der Herleitung zu fragen, ob die physische Interpretation schon nach
einer Informationsreduktion angesetzt wurde. Ein erst danach berechneter
neutraler Frame rekonstruiert die verworfenen Querblöcke nicht automatisch.

Die native Form P M P macht diese Frage relevant, beweist aber allein
noch nicht, dass die vollständige Herleitung ihre Querblöcke tatsächlich
verworfen hat: Die Quelle führt M im Closure-Funktional weiterhin mit.

## 7. Exakter Test D: Mischen verändert die Art des Objekts

Ein Zustandsmittel sum_j w_j rho_j ist eine zulässige Dichtematrix.
Dagegen ist E=sum_j w_j P_j im Allgemeinen kein Projektor. Für zwei
orthogonale Rang-eins-Projektoren auf C² und gleiche Gewichte gilt

    E=I_2/2,    E²=I_2/4 != E.

Die neutrale gemischte Zustandsmatrix darf folglich nicht als neuer
idempotenter P_C7 in die geerbte Closure-Gleichung eingesetzt werden.
Eine neue Spektralauswahl aus E würde eine zusätzliche Regel benötigen;
beim neutralen E=I/2 gibt es keine ausgezeichnete Rang-eins-Richtung.
Ein neuer relationaler Projektor aus mindestens zwei Referenzen ist
denkbar, muss aber durch eine eigene kovariante Auswahlregel bestimmt sein.

Auch „erst mitteln, dann Closure prüfen“ ist nicht gleich „Closure mitteln“.
Für festes orthogonales P und K_j=[M_j,P] gilt mit K_bar=sum_j w_j K_j

    sum_j w_j K_j†K_j
      = K_bar†K_bar + sum_j w_j (K_j-K_bar)†(K_j-K_bar).

Mit M_+=sigma_x, M_-=-sigma_x und gleichen Gewichten ist M_bar=0 und
H_C(M_bar,P)=0; der gemittelte positive Defekt ist jedoch
(rho+sigma)I. Der neutrale Mittelwert verdeckt hier positive Fluktuationen.
Das ist eine exakte Algebra-Kontrolle und keine berechnete native
Vakuumenergie oder ein Beweis physischer Frame-Fluktuationen.

## 8. Was sich am Verdacht erhärtet und was offen bleibt

**Belegt:** Die historische Photon-/Referenzframe-Benennung war in der
späteren Zustandsdarstellung nicht konsistent; die Quelle korrigiert sie.
Die physische Gleichsetzung von strukturellem Fixsektor, Photon-Zustand,
P_C7 und positiver HC-Wirkung ist nicht vollständig durch eine gemeinsame
berechnete Operatorabbildung geschlossen.

**Ernsthaft zu prüfen:** Eine relative Sektorwahl oder vorzeitige Projektion
kann die späteren Probleme tatsächlich vorprägen. Das wurde oben durch
exakte, klar nichtnative Gegenbeispiele gezeigt. Die Quelle enthält mit
der isospektralen relativen Orientierung bereits denselben Warnhinweis.

**Nicht belegt:** Dass ein konkreter korrigierter Mischframe M16 und P_C7
eindeutig bestimmt oder ihre Defekte beseitigt. Ebenso wenig ist bewiesen,
dass alle Probleme nur aus dem Frame stammen. Fehlende gemeinsame
Operatoren, eine noch hypothetische Eltern-Gleichung, Norm-/Uhridentifikation
und der absolute gravitative Term bleiben eigenständige Verpflichtungen.

## 9. Präziser nächster Ansatz

Die nächste sinnvolle Konstruktion muss VOR der physischen Projektion
ansetzen. Auf einem gemeinsamen Träger sind mindestens J bzw. die
Referenztransformationen, M, die Uhr und die zulässigen Sektorbedingungen
anzugeben. Dann ist eine relationale Auswahlregel P=P[data_1,data_2,...]
zu fordern, die unter einem gemeinsamen passiven Wechsel kovariant ist:

    P[U data_1 U†, U data_2 U†,...]=U P[data_1,data_2,...] U†.

Zusätzlich müssen Idempotenz, positive Orthogonalität im richtigen
Skalarprodukt, Rang, physische Auswahl und Transportverträglichkeit
geprüft werden. Das betrifft auch relative Orientierung zu Uhr und Seeds;
das strukturelle C ist nicht stillschweigend P. Mehrere Referenzen allein
garantieren weder Existenz noch Eindeutigkeit eines solchen Projektors.

Erst dann lässt sich zwischen „dieselbe Closure in anderer Darstellung“
und „physikalisch anders hergeleiteter zulässiger Sektor“ entscheiden.
Diese Prüfung gehört vor den nächsten Versuch einer Lambda-Balance.

## 10. Validierung und Status der bisherigen Synthese

Die Tests A–D wurden analytisch durch Konjugation, zwei explizite
2x2-Blockprodukte, Idempotenzprüfung und die ausgeschriebene
Varianzidentität geprüft. Kein numerisches Experiment oder allgemeiner
Nachweis eines nativen falschen Frames wird behauptet.

Die gemeinsame 16-dimensionale Konstruktion der vorigen Synthese bleibt
ein konsistentes gewähltes Probe-Beispiel. Ihre Setzung P=C ist nach diesem
Audit gerade eine zu rechtfertigende Auswahl, keine beantwortete
Herleitungsfrage. Sie darf daher nicht als Nachweis gelten, dass der
historische Framefehler bereits behoben wurde. OP5 bleibt offen.
