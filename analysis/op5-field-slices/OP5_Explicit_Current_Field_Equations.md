# Explizite Feldform des bisherigen OP5-Vergleichs

30.10.2026. Umformulierung existierender Vergleichsgleichungen, keine neu hergeleitete native Wirkung.

Setze Q_a=S tensor K_a, D_mu=partial_mu+i A_mu, M=h(Y tensor beta). Die gekoppelte Feldgleichung lautet

F[Psi]=i sum_{mu,a} (E^{-1})^{mu}_a (I tensor K_a) D_mu Psi - M Psi=0,
E^a_mu=Re(Psi†Q_a D_mu Psi), det E!=0.

Zusammen mit dem komplex Konjugierten ist dies ein reelles nichtlineares erstordentliches PDE-System. Die Coframe ist aus denselben Feldern und Ableitungen zusammengesetzt; ihr Einsetzen macht den Hauptteil nichtlinear in ersten Ableitungen. Multiplikation mit det E entfernt die inverse Matrix algebraisch, darf aber nicht die Nebenbedingung det E!=0 verlieren. Andernfalls entstehen unechte singuläre Lösungen.

## Stromform der Auslese

Für konstante hermitesche Q_a und hermitesche A_mu gilt exakt

E^a_mu=(1/2)partial_mu j_a+(i/2)Psi†[Q_a,A_mu]Psi,
j_a=Psi†Q_a Psi.

Der partielle Ableitungsteil ist also schon der Gradient eines reellen Stromskalaren. Der nicht-exakte Anteil stammt in diesem Vergleich aus dem Kommutator mit der internen Verbindung. Beweis: Produktregel für j und Re(i Psi†QA Psi)=(i/2)Psi†[Q,A]Psi. Wolfram bestätigte die Kommutatoridentität im unabhängigen allgemeinen hermiteschen2x2-Beispiel; die dimensionsunabhängige Identität folgt unmittelbar durch Konjugation.

Für unsere konkrete Verbindung A=G s mit s=(-y/rho)dx+(x/rho)dy=rho dphi auf dem Chart rho>0 folgt

E^a=(1/2)d j_a+b_a s=(1/2)d j_a+(rho b_a)dphi,
b_a=(i/2)Psi†[Q_a,G]Psi.

Damit gelten identisch

dE^a=d(rho b_a) wedge dphi,
dphi wedge dE^a=0,
dE^a wedge dE^b=0.

Diese Flächen-/Integrabilitätsstruktur folgt bereits aus der gewählten Verbindung und Auslese, nicht erst aus einem numerischen Fit. Sie ist daher eine sinnvolle weitere Quelle für die Attribution symmetrischer Fortsetzungsbedingungen. Dass sie genau den gesamten zuvor gefundenen Rest erklärt, wurde noch nicht gezeigt.

Bei fixiertem Winkel phi sind die zurückgezogenen Coframes exakte Gradienten d j_a/2; in azimutaler Richtung kommt der gemeinsame zusätzliche Kanal hinzu. Dies ist eine strukturelle Achsenunterscheidung unserer radial/azimutalen Vergleichswahl, keine universelle ausgezeichnete Raumrichtung. dE ist nicht automatisch Riemann-Krümmung. Bei einer zusätzlichen Lorentz-Verbindung wäre T^a=dE^a+omega^a_b wedge E^b zu verwenden.

## Überprüfbarer Nutzen und Grenzen

Feldlösungen sind weiterhin zu finden, aber die Geometrie kann in dieser Familie nicht beliebige lokale Curlkomponenten besitzen: alle dE^a teilen den Faktor dphi. Ein vorgeschriebener geometrischer Zielansatz muss diese Bedingung erfüllen. Das bietet einen strukturell begründeten Test, bevor weitere Optimierungsparameter ergänzt werden.

Unabhängige numerische Kontrolle des gespeicherten glatten gemischten Feldes an zwei Punkten und drei Schrittweiten in OP5_Current_Field_Form_Check.py/.json: Strom-Coframe-Identität und dphi wedge dE gegen direkte differenzierte Coframe geprüft. Keine vollständige Lösung der PDE und keine globale Phi-Karte an der ausgeschlossenen Achse beansprucht.

Wolfram kann die symbolische Umformulierung, Ableitungen und spezielle reduzierte Systeme unterstützen. Es kann aus diesen Vergleichsannahmen nicht automatisch eine physikalisch begründete Wirkung oder eine neue Naturgleichung bestimmen. Native M16/C7-Zuordnung, Spinverbindungsdynamik und Feldfortsetzung bleiben offen. Lokal gespeichert, nicht committed.
