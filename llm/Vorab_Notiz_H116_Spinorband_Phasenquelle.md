# Vorab-Notiz H116: Phasenauslese und Rückkehrquelle des Spinorbands

22. November 2026. Nicht blind. Anlass ist die Vernam-Analogie des Autors und die Frage, ob die strukturelle Quelle direkt untersucht werden muss. Geprüft wird eine ideale Oktant-Rückkehr, ohne Identifikation mit der nativen Banddynamik oder einem kryptographischen System.

## Vorwissen geprüft

- [Vernam-artige Persistenzheuristik](../sources/research/parts/v470/19_local_op_entry.tex), Abschnitte zum diskretisierten Teichmüller-Persistenzstrom und zur generatorbezogenen Suche. Sie fordert die Rekonstruktion einer strukturellen Quelle aus lokalen Persistenzmustern. Die aufgeführten Symbole kodieren Schwellwerte, keinen ausdrücklich orientierten Hopf-Phasenschritt.
- [Spinorband 19K–19L](../sources/research/parts/v470/24_computational_specification.tex): ein lokaler Wort-/Kopf-/Steuer-/Routing-/Closure-Zustand und eine bedingte Rückkehrrolle des HC. Der physische Weg und seine Relativphasenauslese sind nicht angegeben.
- [H114](Ergebnis_H114_Photon_Oktant.md), [H115](Ergebnis_H115_Kompensator_Oktant.md) und [r14](../notes/research/v4_10_0_r14/rounds/v4100_r14_round.tex): die Phase des flachen Oktanten ist π/4, die Identifikation mit dem Photonpunkt bleibt bedingt.
- [Gesamtbild](../wiki/Gesamtbild.md), T2/T5/T8. Die Vorarbeiten zu Closure, OP5 und dem Hopf-Fluss enthalten keine Gleichsetzung der Bandrückkehr mit dem orientierten Oktant-Umlauf.

## Kriterien

- **H116a, Identifizierbarkeit aus ungerichteten Daten:** In der idealen Oktant-Rückkehr soll der nächste Phasenschritt aus Start-/Endstrahl und den drei paarweisen Übergangswahrscheinlichkeiten folgen. Vergleiche den Oktant-Umlauf +x→+y→+z→+x mit demselben Weg in Gegenrichtung. Identische getestete Größen bei verschiedenem normiertem Bargmann-Produkt widerlegen die Folgerung.
- **H116b, Marginaldiagnose:** Acht gleich häufige akkumulierte Phasen sollen acht mögliche unabhängige Schritte belegen. Kontrolle durch je einen vollständigen Umlauf der acht Phasenzustände mit festem Schritt +1 und −1 modulo 8. Gleiche Phasenhistogramme bei konstanten, unterschiedlichen Schrittfolgen widerlegen den Schluss.
- **Positivkontrolle:** Das geordnete Bargmann-Produkt bleibt bei unabhängigen Phasenänderungen der drei Spinorrepräsentanten unverändert. So soll es in diesem Vergleich die Wegorientierung unterscheiden, anders als Betragsquadrate und Start-/Endstrahl.

Wolfram Language prüft exakte Identitäten für abstrakte Spinorprodukte und analytische Modulo-8-Beispielfolgen. Die Rechnung definiert keine Bandmaschinen-Übergangs-, Guard- oder Auswahlregel.
