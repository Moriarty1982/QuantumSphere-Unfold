# H116: Phasenauslese und Rückkehrquelle des Spinorbands

22. November 2026. Nicht blind nach [Vorab-Notiz](Vorab_Notiz_H116_Spinorband_Phasenquelle.md), Commit 3c328ba60db61f68f7bdddc67fb30033a2795190. [Wolfram-Skript](h116_spinor_phase_source.wl) und [tatsächliche Ausgabe](h116_spinor_phase_source.txt).

## Was der Companion bereits unter Vernam versteht

[Abschnitt 19](../sources/research/parts/v470/19_local_op_entry.tex) nennt ausdrücklich eine Vernam-artige Persistenzheuristik. Wiederkehrende Hindernismuster sollen die lokale Quelle des beobachteten Stroms erschließen. Der vorhandene Strom quantisiert Closure- und \(\Theta/R\)-Größen, Admissibilität sowie aufeinanderfolgende Teichmüller-Verzerrungswerte und deren Änderung. Wiederholungen oder Übergänge wie NT→PF dienen der Suche nach der Regel für den Regimewechsel. Die Symboldefinition enthält keine gerichtete Rückkehrphase. Eine Abbildung dieser Symbole auf die Hopf-Phase ist in den geprüften Quellen offen.

[19K–19L und 19Q](../sources/research/parts/v470/24_computational_specification.tex) führen Bandzustand, Kopf, Steuerung, Routing und Closure-Zertifikat sowie die bedingte Rückkehrrolle des HC. Eine eindeutige zulässige Folgeroute soll die operationale Rückkehr ermöglichen. Die geprüften Abschnitte geben dafür weder den konkreten Pfad im projektiven Spinorraum noch dessen Phasenvergleich oder einen Zufallseingang vor. Auch [H114](Ergebnis_H114_Photon_Oktant.md) und [H115](Ergebnis_H115_Kompensator_Oktant.md) liefern diese Identifikation nicht.

## Exakte Gegenproben

Wolfram berechnet für \(x\to y\to z\to x\) und \(x\to z\to y\to x\) auf dem flachen Oktanten denselben Start- und Endstrahl und dreimal dieselbe Übergangswahrscheinlichkeit \(1/2\). Das geordnete Überlappungsprodukt ist im ersten Umlauf \((1+i)/4\), im zweiten sein Konjugiertes. Die Schritte sind also \(+45^\circ\) und \(-45^\circ\) in der verwendeten Bargmann-Konvention. Die Beträge und Endpunkte bestimmen das Vorzeichen nicht. H116a ist widerlegt; unabhängige Umphasungen der drei Spinorrepräsentanten ändern das geordnete Produkt exakt um null.

Die beiden Folgen \(q_n=\pm n\bmod8\) besuchen während eines Zyklus alle acht Phasen einmal. Ihre Schrittfolgen sind dennoch konstant, einmal \(+1\), einmal \(-1\). H116b ist widerlegt. Ein vollständiges Histogramm der akkumulierten Phasen sagt nichts über die Unabhängigkeit der Einzelschritte. Als Vernam-Vergleich wirkt eine relative Phase als Addition modulo acht. Einen Einmalschlüssel ergäbe in diesem idealisierten Kanal erst eine unabhängig gleichverteilte und geheime Schrittwahl. Die Rechnung identifiziert keine solche Quelle im Companion.

## Welcher Teil der Quelle zu untersuchen ist

Der Befund verweist auf die **Auswahl des geordneten Rückwegs** aus den zulässigen Fortsetzungen. Für jede native Rückkehr bräuchte man eine gemeinsame Spur aus Anfangszustand, Steuerung, ausgewählter Route, HC-/Closure-Zertifikat, Folgezustand und signiertem Phasenschritt. Sind die Zwischenstrahlen zugänglich, ist das geordnete Produkt ein phaseninvarianter Vergleichswert. Bei einer vergleichenden Amplitudenmessung muss dieselbe Referenz beide Wege verbinden. Verschwindet ein nötiger Überlapp oder eine Referenzamplitude, ist die Phase undefiniert.

Ein erster diskriminierender Vergleich wiederholt denselben sichtbaren Anfangszustand mit unterschiedlicher zulässiger Vorgeschichte und vergleicht die vorzeichenbehafteten Schritte. Verschiedene Schritte widerlegen eine Ein-Schritt-Regel auf dem sichtbaren Zustand. Ob das vollständige Routing- oder Closure-Zertifikat den Unterschied auflöst, lässt sich erst an einer solchen Spur prüfen. Gleiche Schritte allein beweisen keine vollständige Zustandsbeschreibung. Die direkte strukturelle Frage bleibt: Welcher Bestandteil der nativen Fortsetzung bestimmt den orientierten Rückweg?

Die exakten Kontrollen liefen in Wolfram Language. Es wurde keine Quantenschaltung oder Bandmaschinen-Übergangsregel modelliert. Die Phasenspuren sind analytische Vergleichsfolgen.
