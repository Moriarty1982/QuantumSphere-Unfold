# OP5: Gemeinsame Anpassung der zweiten und dritten Ableitungen

30.10.2026. Numerische endliche Jet-Verträglichkeit im bestehenden Vergleichsmodell, kein regionaler oder physikalischer Existenzbeweis. Ausgangsrevision f98b29b.

## Geändert und festgehalten

An den drei bisherigen Kontrollpunkten bleiben die Feldwerte und sämtliche erfolgreichen ersten Ableitungen aus joint-fit-result.json unverändert. Damit bleiben auch die Coframe, ihre punktweise zeitliche Fixierung, Determinante und Metrik am Punkt unverändert. Hintergrund, Kopplungen, Massenterm und deren symbolisch abgeleitete Ortsabhängigkeit bleiben gleich. Nur die 240 symmetrischen zweiten und 480 symmetrischen dritten Spinorableitungen werden neu bestimmt. Keine Ableitung der zeitlichen Coframe wird zusätzlich fixiert.

Bei festen Feldwerten/ersten Ableitungen ist der Operator A der dritten Ableitungen konstant. Seine vollständige linke Nullraum-Basis hat numerisch 25 Zeilen (A ist240x480, Rang215). Die freien dritten Ableitungen werden zunächst eliminiert. Der Optimierer löst gleichzeitig die96 Bedingungen dF=0 und die25 verbleibenden Quellbedingungen Lb(H)=0 für die zweiten Ableitungen H. Anschließend werden die dritten Ableitungen zurückgewonnen und sämtliche240 ddF-Komponenten im unprojizierten System geprüft. Die Quelle ist quadratisch in H. Ein kleines projiziertes Fitmaß allein wird nicht als Erfolg ausgegeben.

## Ergebnis

| Punkt | ddF bei eingefrorenen alten H | ddF nach gemeinsamem Fit | dF nach Fit | F unverändert |
|---|---:|---:|---:|---:|
| Zentrum | 29.37655 | 8.42e-12 | 1.23e-11 | 3.08e-14 |
| Rand | 30.06650 | 8.64e-12 | 1.41e-11 | 2.06e-15 |
| Innen | 29.04689 | 8.40e-12 | 1.15e-11 | 2.64e-15 |

Jeweils zwei akzeptierte gedämpfte Anpassungsschritte. Die erste Ableitungsordnung wird dabei nicht wieder freigegeben. Die zweiten Ableitungsnormen steigen von etwa7 auf20.88,21.46,20.57, ihre Änderungen betragen19.64,20.32,19.28; dritte Ableitungsnormen liegen bei80.07,79.69,79.71. Diese Werte gehören zur bisherigen unskalierten Koordinatenpackung. Sie sind keine physikalischen Skalen; daraus folgt keine gleichmäßige Kontrolle weiterer Ableitungsordnungen.

## Kontrollen

Die ursprüngliche eingefrorene Fehlprobe bleibt in third-check-result.json erhalten. Die vollständigen neuen Restnormen stimmen bei drei relativen SVD-Schwellen1e-8,1e-9,1e-11 überein. Die tatsächliche Hintergrund-Hesse-Matrix und alle Rückwirkungen der inversen Coframe sind enthalten. Alle Eingabedateien blieben während des Laufs unverändert; das Evidenzmanifest validiert.

Eine getrennte NumPy-Auswertung des ursprünglichen Feldresiduals auf einem gemeinsamen kubischen Taylorfeld bestätigt die Fortsetzungsrechnung. Zentrale zweite Differenzen ergeben bei Schritt1e-3 ungefähr1.3e-3 bis1.4e-3, bei3e-4 ungefähr1.2e-4 und bei1e-4 ungefähr1.3e-5 bis1.4e-5. Die Abweichung von AD fällt quadratisch. Diese Kontrolle stützt die Konsistenz des Fits, zertifiziert aber nicht die letzten Dezimalstellen der AD-Reste.

## Einordnung

Die neue Drittordnungsblockade ist an allen drei geprüften Keimen reparierbar, ohne die ersten Ableitungen oder das Vergleichsmodell zu ändern. Die zuvor gewählten zweiten Ableitungen waren also für die nächste Ordnung ungeeignet; sie lieferten keinen allgemeinen Unmöglichkeitsbeweis. Es gibt nun numerisch vollständige endliche Drittjets mit F,dF,ddF nahe null.

Die drei unabhängigen Keime sind weiterhin nicht als Ableitungen eines einzigen regionalen Lösungsfelds nachgewiesen. Die nächste Hürde sind symmetrische vierte Ableitungen beziehungsweise die daraus folgenden zusätzlichen Bedingungen an die niedrigeren Daten; ebenso fehlen regionale Fortpflanzung, Wachstumskontrolle, native Wirkung und physikalische Identifikation. OP5 bleibt offen. Aus einem weiteren endlichen Fit folgt keine Konvergenz einer Taylorreihe.

Artefakte: third_joint_fit.py (Reproduktion: python third_joint_fit.py), third-joint-fit-result.json, third-joint-fit-manifest.json, third-joint-inputs/. Zusätzliche getrennte Prüfartefakte werden in third-joint-review.md dokumentiert. Kein Repository-Edit, Commit oder Push.

Zusätzliche getrennte Prüfung aus Originalhintergrund und gespeicherten Ableitungen: g bleibt auf1e-15, dg unter3.4e-14, die zuvor großen zweiten Zustandsableitungen d²g sinken auf2.46e-11 bis3.08e-11. Bei diesen kleinen Resten müssen in der differenzierten Identität auch die Terme aus F und dF mitgeführt werden; die vorherige exakte Untergrenzeninterpretation bei idealem F=dF=0 wird hier nicht numerisch übertragen.
