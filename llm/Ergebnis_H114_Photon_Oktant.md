# H114: Photon-Eigenpunkt und Rangverlust des Oktanten

22. November 2026. Nicht blinder exakter Test nach [Vorab-Notiz](Vorab_Notiz_H114_Photon_Oktant.md), Commit 7e00f897495f53270abee7c9e6d1111c63f13c0b. [Wolfram-Skript](h114_photon_octant.wl) und [tatsächliche Ausgabe](h114_photon_octant.txt).

## H114a: Die Eingaben am Photonpunkt erzwingen keine Bargmann-Phase

Die [Konvention F](../notes/research/v4_10_0_base/rounds/v490_r22_round.tex) gibt \(b=0\) und \(\rho_P=I_2/2\). Das Dublett behält somit Rang zwei. Im Generationsraum hat die [r14.5-Gram-Matrix](../notes/research/v4_10_0_r14/rounds/v4100_r14_round.tex) Diagonaleinträge eins, paarweise Überlappungsbeträge \(1/\sqrt2\) und die zyklische Bargmann-Phase \(\varphi\). Wolfram bestätigt: bei \(\varphi=0\) und bei \(\varphi=\pi/4\) sind alle Hauptminoren nichtnegativ, die Beträge identisch, die Ränge drei bzw. zwei. Beide sind mit demselben unabhängig gegebenen Photon-Dublett verträglich. Damit ist die reine Folgerung aus diesen Eingaben widerlegt. Die Gegenprobe benutzt keine gemeinsame Wechselwirkung zwischen Dublett und Generationsraum.

Die ältere [Oktantkonstruktion auf der Photonseite](../notes/research/op3_helicity_axis_2026_11_15/README.md) verwendet ein reines Vergleichsfeld mit \(E=B\). Der zentrale Photon-Eigenpunkt aus Konvention F liegt bei \(b=0\) und ist davon zu unterscheiden.

## H114b: Bedingte Brücke über Bures

[r17.2](../notes/research/v4_9_0_r17_r19/rounds/v490_r17_round.tex) liefert in der Zustandsdisk für \(r=|b|\) den radialen Bures-Abstand vom reinen Rand \(d_{\mathrm B}(r)=\tfrac12\arccos r\). Das ergibt am Photonpunkt \(\pi/4\). **Wenn** eine generative Auslese die Bargmann-Phase mit diesem Abstand identifiziert und die r14.5-Überlappungen erhält, gilt exakt
\[
\det G(r)=\frac{\sqrt{1+r}-1}{2},\qquad
\lim_{r\downarrow0}\frac{\det G(r)}r=\frac14.
\]
Dann haben alle \(r>0\) im Vergleich vollen komplexen Rang drei und \(r=0\) exakt Rang zwei. H114b ist unter der gesetzten Identifikation bestätigt. Im r14.6-Kappenbild \(\varphi=\pi/4-\Omega_{\rm eff}/2\) entspricht dieselbe Annahme der Beziehung \(\Omega_{\rm eff}(r)=\arcsin r\). Alternativ genügt für den alleinigen Endpunkttest die schwächere native Bedingung \(\Omega_{\rm eff}(0)=0\) bei erhaltenen Überlappungen. Keine der geprüften Stellen leitet diese Verbindung her. Die Bures-Metrik ist im Photonpunkt regulär; die dort undefinierte polare Richtung liefert keinen Rangabfall des metrischen Tensors.

## H114c: Reeller Rang und Normalstabilität

Die Reellifizierung der Gram-Matrix ergibt exakt Rang sechs bzw. vier. Eine unter Multiplikation mit \(i\) abgeschlossene reelle Teilfläche hat gerade Dimension. Die ausdrücklich reelle Projektion auf die ersten fünf Koordinaten in der Reihenfolge \((\Re g_1,\Im g_1,\ldots)\) verletzt diese Struktur: Der Kommutator mit \(J\) hat Rang zwei. Die Projektion auf die ersten vier Koordinaten kommutiert mit \(J\). Ein reeller Fünfraum kann daher als eigenes Zwischenmodell formuliert werden, braucht aber eine zusätzliche Abbildung.

Für einen separat angenommenen Fünfraum mit Normalrichtung \(n\) besitzen beide Generatoren
\[
 L_\pm=\operatorname{diag}(-1,-1,-1,-1,\pm1)
\]
dieselbe invariante Viererebene und dasselbe stabile Verhalten auf ihr. Außerhalb der Ebene gilt \(n(t)=e^{\pm t}n(0)\). Im ersten Fall mit negativem Vorzeichen ist bereits der Fünfraum asymptotisch stabil. Im positiven Fall wachsen Normalabweichungen, auch wenn die formale Projektion eine stabile reduzierte Dynamik zeigt. Damit sind weder die Fünferzwischenstufe noch Stabilität durch Dimensionszählung erzwungen. Für eine native 5→4-Reduktion braucht es eine physische Zwangsbedingung oder abklingende Normalbewegung. Die gezählten Dimensionen gehören zum internen Zustandsraum; die separate r69-Coframe-Konstruktion liefert daraus keine Raumzeit-Identifikation.

Wolfram prüfte exakte Ränge, Minoren, algebraische Residuen und Spektren. Der erste Lauf lieferte die Grenzrate korrekt mit einer Zwischenwarnung zur ungekürzten Form. Der gespeicherte Kontrolllauf verwendet die rationalisierte Form und läuft ohne Meldungen. Eine Quantenschaltung war nicht Teil der Prüfung.
