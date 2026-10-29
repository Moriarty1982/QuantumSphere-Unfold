# OP5: Rückkopplung des Mischungsgradienten in den kinetischen Frame
28.10.2026. Fortsetzung von OP5_AB_Proportional_Dynamics_Result.md. Vergleichsmodell, keine native OP5-Schließung.

## Festgelegte Änderung
Die beiden lokalen Kandidaten stammen aus dem vorherigen Fit mit freiem reellem theta-Gradienten und einer relativen Phasenrate. Feldwerte, übrige u/w-Ableitungen und interne Verbindungswerte bleiben fest. Der neue Gradient q ersetzt q0=(theta_t,0,0,0).
Bei gleichem Coframe-Auslesegesetz ergibt sich
E^a_mu=delta^a_mu+a^a r_mu, a^a=Delta j_u^a/2, r=q-q0.
Die relative Phasenrate trägt am proportionalen Anfangswert direkt nichts zur reellen Coframe bei. Eine endliche relative Phase wurde nicht untersucht.

## Exakte algebraische Rückkopplung
D=1+r·a, det E=D, E^-1=I-a r^T/D.
Für D ungleich null bleibt g=E^T eta E lorentzsch. Dies sagt noch nicht, dass die alte t-Foliation räumlich ist.

Mit P^mu=sum_a (E^-1)^mu_a K^a gilt
sum_mu q_mu P^mu = [q0_a+(1-a·q0)r_a/D] K^a.
Für unsere Ausgangsfamilie j_u^0=N/2, a^0=N Delta/4 und theta_t=4/(N Delta), also a·q0=1. Daher exakt:
sum_mu q_mu P^mu = theta_t_base I.
Die neu freigegebenen theta-Ableitungen verschwinden aus diesem kontrahierten Ableitungsterm, sobald der inverse induzierte Frame eingesetzt wird. Dies gilt für beliebige r mit D ungleich null in dieser eingeschränkten Rank-eins-Änderung, nicht nur für die beiden numerischen Kandidaten. Ein generischer symbolischer Test und eine unabhängige Herleitung bestätigen die Identität.

## Zeitrichtung der beiden Kandidaten
| Diagnose | P1 | P2 |
|---|---:|---:|
| det E | 1 (numerisch) | 1 (numerisch) |
| g^{00} | 58.5 | 70.77894737 |
| Eigenwerte von P^0, jeweils doppelt | -13, 4.5 | -12.28685707, 5.76054128 |

Signaturkonvention eta=(-,+,+,+). Positive g^{00} bedeutet: Der Kovektor dt ist raumartig, die Flächen t=konstant sind zeitartig. Sie sind keine üblichen raumartigen Cauchy-Anfangsflächen. Die Matrix P^0 bleibt zwar invertierbar, aber indefinit. Invertierbarkeit allein begründet keine geeignete hyperbolische Zeitentwicklung.

Dies ist kein Verlust der Lorentzsignatur und kein Beweis einer physikalischen Überlichtgeschwindigkeit. Ein punktweise zeitartiger Kovektor ist beispielsweise die nullte Coframe-Zeile E^0; seine Norm unter g^-1 ist -1. Eine passende durchgängige Zeitfunktion/Anfangsfläche ist damit noch nicht konstruiert.

Bei linearer Interpolation der Jet-Änderung (kein zeitlicher Lösungsverlauf!) wird dt bereits bei Interpolationsparametern etwa 0.0714286 bzw. 0.0752623 null. Der bisherige flache Fit ist also keine kleine Korrektur innerhalb derselben zulässigen Zeitwahl.

## Zusätzlicher Test einer ausdrücklich gewählten kovarianten Fortsetzung
Um nicht nur den Ableitungsterm zu prüfen, wählen wir bedingt:
i P^mu partial_mu Psi - P^mu A_mu Psi - h (Y tensor beta) Psi =0,
mit den bisherigen internen Verbindungs-Einformen A_t=0, A_i=spin_i G als festen Koordinatenkomponenten und unverändertem h am Punkt. Das ist eine konkrete Vergleichsfortsetzung, keine Herleitung des nativen Operators aus M16/C7. Festhalten orthonormaler statt koordinatenbezogener Verbindungswerte wäre eine andere Fortsetzung.

Die transversale A/B-Bedingung einschließlich der zusätzlichen imaginären Rate lambda lautet dann
(sum q_mu P^mu)u+i lambda P^0 u-h beta u-i(dp-cq)(sum spin_i P^i)w=0.
Eine gemeinsame speziesdiagonale Spinverbindung fällt aus dieser A/B-Projektion am proportionalen Feldwert heraus. Sie ist dadurch nicht für die vollständigen Gleichungen bestimmt oder verzichtbar. Auch ihre mögliche Rückwirkung auf ein erweitertes Coframe-Auslesegesetz ist hier nicht gelöst.

Quadratische Restnormen dieser notwendigen Bedingung:
| Operator | P1 | P2 |
|---|---:|---:|
| alter flacher Operator | unter 1e-28 | unter 1e-28 |
| induzierter Operator der gewählten Fortsetzung | 32.6666667 | 118.0715789 |

Die zuletzt gefundenen beiden lokalen Fits überstehen diese Rückkopplung also nicht. Das ist ein negatives Resultat für diese Kandidaten, kein Ausschluss anderer selbstkonsistenter Jets. Insbesondere ändern sich auch die Verbindungs-Kontraktion und der Phasenterm; aus der exakten theta-Identität allein folgt kein allgemeines No-go.

## Bedeutung für die Fortsetzung
Der bisherige Erfolg kam vom Lösen der Mischungsbedingung im festgehaltenen flachen kinetischen Frame. Mit dem von denselben Ableitungen erzeugten Frame geht dieser Erfolg verloren. Ein Koordinatenwechsel kann eine bessere Zeitwahl liefern, aber eine nichtverschwindende kovariante Feldgleichung nicht allein heilen.

Nächster mathematischer Schritt: die induzierte transversale Bedingung direkt als selbstkonsistente Gleichung behandeln, geeignete Zeitkovektoren und Nichtentartung gleichzeitig prüfen; danach die übrigen Spinor- und Verbindungsbedingungen. Nicht zuerst im flachen Frame lösen und anschließend nur die Geometrie austauschen. Die gemeinsamen u/w-Entwicklungen und gegebenenfalls weitere Kopplungen müssen als explizite Freiheitsgrade geführt werden.

## Reproduzierbarkeit
OP5_Mixing_Coframe_Feedback_Check.py/.json, abhängig vom vorherigen lokalen JSON und dem Repository-Evaluator. Symbolische Rank-eins-Identität, numerische Matrixinverse, Signatur, Hauptmatrix-Determinante und beide Gate-Reste geprüft. Keine regionale Lösung, keine Krümmungsberechnung, keine native Wirkung und kein kosmologischer Lambda-Wert. Lokal gesichert, noch nicht committed.
