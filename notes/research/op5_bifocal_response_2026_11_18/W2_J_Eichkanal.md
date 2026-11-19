# OP5: Wie weit trägt der vorhandene J-Eichkanal?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im gemeinsamen statischen Materie-Ruhesystem. Die [radiale Yukawa-Rechnung](W2_Higgsquelle.md) lässt das Vorzeichen offen. Hier folgt die Rückwärtssuche dem zusätzlich vorhandenen W1-Maxwell-Feld in der W2-Dirac-Lesart. Die [W1-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) gibt seine Quelle vor. Die [Gauß-Prüfung](W1_Gauss.md) ergibt bereits die minimale Feldenergie auf einer periodischen Zelle. Neu geprüft werden die gemeinsame Auslese von Higgs- und J-Kanal sowie die Kraft bei getrennten Foki. Die [globale Ladungsprüfung](W2_Ladung.md), die [Frame-Prüfung](W2_Frame.md), die [direkte Randkopplung](Quellkopplung.md) und das eingefrorene Vergleichsmodell der [OP5-Anleitung](../../anleitungen/op5-vergleichsmodell-rechnen.md) bestimmen den Geltungsbereich.

## Der Eichkanal sieht ein Vorzeichen, aber welche Ladung?

In der linkshändigen Schreibweise hat $f_L$ die interne J-Ladung $+1$ und $f^c$ die Ladung $-1$. In der Dirac-Lesart ist $f_R$ das Konjugat von $f^c$ und hat deshalb ebenfalls $+1$. Der Dirac-Teilchenkanal trägt für jede Art dieselbe J-Ladung, der Antiteilchenkanal die Gegenladung. In den betrachteten nichtverschwindenden Yukawa-Monomialen heben sich die beiden Fermionladungen auf, sodass das Higgsdublett unter diesem U(1) neutral ist. In der statischen Dirac-Besetzungsreduktion mit masseneigenen Arten gilt daher

$$
d_i(x)=\int d\Pi\,(f_{i,+}-f_{i,-}),\qquad
\rho_J(x)=\sum_i d_i(x),\qquad
\rho_{B-L}(x)=\tfrac13\sum_{\rm Quarks}d_i(x)-\sum_{\rm Leptonen}d_i(x).
$$

Die Quarksumme zählt die Farben mit. Eichenorm $g_J$ separat: $\nabla\cdot\mathbf E=g_J\rho_J$. Für eine bekannte einzelne Art mit $B-L\ne0$ ist das Vorzeichen der lokalen $B-L$-Quelle so aus dem vorzeichenempfindlichen J-Kanal zugänglich. Mit mehreren Arten ergibt sich eine Mehrdeutigkeit.

**Gemeinsames Gegenbeispiel für beide Felder.** Wähle pro Art gleiche Teilchen-Antiteilchen-Summen für zwei Konfigurationen und eine momentensymmetrische Impulsverteilung. Wähle ein glattes signiertes Profil $s$ mit positiven und negativen Lappen an zwei getrennten Foki und $\int s=0$. Setze für eine Quarkart, über Farben gleich verteilt, $d_u=s$ und für einen geladenen Leptonkanal $d_e=-s$. In der zweiten Konfiguration kehren beide Differenzen ihr Vorzeichen um. Hinreichende Ausgangsbesetzungen erlauben diese Änderungen mit zulässigen Besetzungen. In beiden Fällen gilt punktweise $\rho_J=0$. Zugleich ist $\rho_{B-L}=\pm4s/3$. Damit sind die Quellen des radialen Higgsfelds und des J-Maxwell-Felds gemeinsam identisch, während der $B-L$-Dipol sein Vorzeichen wechselt. Bei gleichen Randdaten bleibt die Menge der Lösungen dieser beiden reduzierten Feldgleichungen gleich. Es handelt sich um einen Vergleich vorgegebener Besetzungen. Weitere Eichfelder und die vollständige W2-Zustandsdynamik werden dabei nicht mitgelöst.

## Kraft im J-Feld bei zwei kompakten Foki

Auf $\mathbb R^3$ mit verschwindendem Feld im Unendlichen und vorgegebenen glatten statischen Quellen folgt aus dem Gaußgesetz für den minimalen Feldbeitrag

$$
E_J[\rho_J]=\frac{g_J^2}{2}\langle\rho_J,K*\rho_J\rangle,\qquad K(r)=\frac1{4\pi r}.
$$

Setze $\rho_J=Q(n_+-n_-)$, mit zwei identischen normierten, kugelsymmetrischen und kompakt getragenen Profilen $n_\pm$, die als starre Kopien um den Abstand $R>0$ getrennt sind. Für disjunkte Träger ist die Wechselwirkung exakt $-g_J^2Q^2/(4\pi R)$. Der Außenwert des ersten Kugelprofils ist sein Monopolpotential. Dessen Mittel über jedes kugelsymmetrische Profil um den zweiten Mittelpunkt ist der Wert am Mittelpunkt, da das Potential dort harmonisch ist. Mit festem Profil ergibt sich

$$
E_J(R,Q)=E_{\rm selbst}(Q)-\frac{g_J^2Q^2}{4\pi R},
\qquad
-\partial_R E_J=-\frac{g_J^2Q^2}{4\pi R^2}.
$$

Die Foki ziehen sich an, und diese Kraft bleibt beim Umkehren des gesamten Dipols gleich. Allgemeiner hat der Feldenergieterm bei $\rho_J=Q\,s_\xi$ für eine beliebige Formkoordinate $\xi$ die Struktur $Q^2 C(\xi)$ unter denselben homogenen Randbedingungen. Seine Formkraft ist damit gerade in $Q$. Ein vorhandener Hintergrund $\rho_0$ würde bei $\rho_J=\rho_0+Q\,s_\xi$ den Kreuzterm $g_J^2Q\langle\rho_0,K*s_\xi\rangle$ erzeugen. Für eine lineare Kraft auf $\xi$ muss dieser Überlapp formabhängig sein. Ein solcher Referenzzustand samt Kopplung an den Rand ist in der betrachteten Reduktion nicht festgelegt.

## Konsequenz

Die dokumentierte Maxwell-Komponente liefert eine echte vorzeichenempfindliche Auslese der J-Ladung und eine mechanische Wechselwirkung für vorgegebene Ladungsträger. Im Mehrartenmodell ist die Kombination mit dem radialen Higgsfeld aber für einen $B-L$-Dipol nicht eindeutig. Die Eigenfeldkraft stellt unter den genannten Bedingungen keinen linearen Antrieb aus dem signierten Überschuss bereit. Für OP5 wäre entweder eine aus der Wirkung ausgewählte Artenbelegung samt begründeter Hintergrundkopplung oder ein zusätzlicher unabhängiger Ladungskanal mit einem eigenen Randgesetz zu bestimmen. Die Rechnung setzt keinen globalen Framewechsel mit Ladungskonjugation gleich. I3 bleibt an eine eigenständige Überschussdynamik gebunden. Native Randwirkung und H96 bleiben offen.
