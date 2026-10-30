# OP5: Fortsetzung in die dritte Ableitungsordnung

30.10.2026, Ausgangsrevision f98b29b. Erste und zweite Ableitungen aus dem erfolgreichen gemeinsamen Fit bleiben fest. Frei sind ausschließlich die 480 reellen vollständig symmetrischen dritten Spinorableitungen. Hintergrund/Kopplungen unverändert. Getestet werden die 240 reellen Komponenten der zweiten totalen Ableitung der Feldgleichung. Hintergrundableitungen bis zur zweiten Ordnung werden symbolisch berechnet; die vollständige inverse Coframe wird mitdifferenziert.

| Punkt | Feldrest F | erster Fortsetzungsrest dF | kleinster Rest ddF, symmetrische Drittjets |
|---|---:|---:|---:|
| Zentrum | 3.08e-14 | 9.27e-14 | 29.37655 |
| Rand | 2.06e-15 | 1.25e-14 | 30.06650 |
| Innen | 2.64e-15 | 1.48e-14 | 29.04689 |

Die neue lineare Matrix hat Dimension 240x480 und numerischen Rang 215 bei allen drei relativen SVD-Schwellen 1e-8, 1e-9, 1e-11. Die Restnormen bleiben bei allen drei Schwellen gleich. Selbst ohne volle Drittjetsymmetrie bleiben Restnormen 28.93533,29.63015,28.60225. Daher ist der Rest nicht ausschließlich der neuen Symmetrie zuzuschreiben. Normen verschiedener Ableitungsordnungen sind keine dimensionslosen physikalischen Fehlerquoten und nicht unmittelbar miteinander vergleichbar.

## Getrennt überprüfte notwendige Bedingung

Die Identität ell(Psi)F=g mit g=4-h Psi†ZbetaPsi/2 liefert bei F=dF=0 die notwendige Bedingung d²g=0. Diese hängt bereits von den ersten und zweiten Ableitungen ab, nicht von dritten Ableitungen. Die gespeicherten erfolgreichen Zweitjets verletzen diese Bedingung: Normen der zehn unabhängigen Komponenten 40.89869,41.83060,40.44562. Das wurde in einem getrennten Skript aus dem ursprünglichen h, dessen Ableitungen und den gespeicherten Daten berechnet, ohne die AD-Hesse-Matrix von F zu verwenden. Der Beitrag erklärt eine notwendige Blockade; eine vollständige Identifikation sämtlicher linker Bedingungen ist damit nicht beansprucht.

## Kontrollen und Bedeutung

Eine getrennte NumPy-Auswertung auf einem gemeinsamen kubischen Taylorfeld verwendet die ursprünglichen Hintergrundfunktionen und zentrale zweite Differenzen. Die Abweichung von der AD-Auswertung fällt von etwa 5.8e-4 bei Schritt1e-3 auf etwa 5.3e-5 bei3e-4 und6e-6 bei1e-4. Die großen Restnormen bleiben bestehen. Dieses Verhalten stützt die Auswertung und unterscheidet den Befund klar von Rundungsniveau; es ist keine exakte Rangzertifizierung.

Der vorige Erfolg bleibt gültig bis zur ersten Prolongation: F und dF sind erfüllt. Die dabei gewählten zweiten Ableitungen sind jedoch keine geeigneten Daten für die nächste Ordnung. Der Fit hatte d²g noch nicht verlangt. Freie dritte Ableitungen können diesen bereits in den niedrigeren Daten sitzenden Defekt nicht ändern.

Nächster gezielter Versuch: zweite Ableitungen erneut freigeben, F und dF erhalten und d²g sowie die vollständigen zweiten Prolongationsbedingungen gemeinsam aufnehmen. Falls nötig dürfen danach weitere erste Ableitungen variieren, mit klarer Kennzeichnung der Freigabe. Keine allgemeine Unlösbarkeit oder regionale Existenz, kein physikalischer No-go-Satz und keine OP5-Schließung folgt aus diesen drei eingefrorenen Keimen.

Artefakte: third_check.py (Reproduktion: python third_check.py), third-check-result.json, third-check-manifest.json, third-inputs/; getrennte Prüfung third_gate_review.py, third-order-scalar-gate.json, third-order-review.md. Manifest validiert, alle Eingaben während der Rechnung unverändert. Kein Repository-Edit, Commit oder Push.

Zusätzliche Attribution: Die unabhängig berechnete Untergrenze ||d²g||/||ell|| stimmt an allen drei Punkten bis etwa5e-14 mit dem Rest bei uneingeschränkten Drittjets überein. In der hier verwendeten ungewichteten euklidischen Packung erklärt sie etwa97% des quadrierten symmetrischen Restes. Das ist keine physikalische Prozentzahl; ein weiterer Symmetrieanteil bleibt. Siehe third-gate-review-result.json.
