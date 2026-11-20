# OP5 — Molekülbewegung als zweite Dipolrichtung

20. November 2026. Analytische Erkundung im Materieframe M. Gesucht ist eine zweite innere Dipolrichtung in neutraler Materie aus gewöhnlichen Kernen und Elektronen. Der Gesamtschwerpunkt bleibt fixiert. Es geht um die elektrische Dipolnäherung und die bereits verwendete Punktkern-Ladungstabelle.

## Vorwissen geprüft

Die [fixierten Isotopenanschlüsse](OP5_J_Fixierte_Isotopenanschluesse.md) geben für alle inneren Dipole eines Atoms mit nur einem Punktkern dieselbe Richtung. Der [myonische Vergleich](OP5_J_Myonischer_Anschluss.md) trennt die normierten Richtungen, hat im gemeinsamen Coulomb-Teilfenster aber eine stark unterdrückte elektrische Antwort. Der [gemeinsame J-Strom](OP5_J_Gemeinsamer_Strom.md) gibt die Punktkernladung. Der [A/B-Vergleich](OP5_J_Sende_Empfangsports.md) verlangt unabhängige Ansteuerung und Auslese an beiden Enden. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Rechnung zur lokalen OP5-Auslese. Die bei I3 fehlende kosmologische Populationsdynamik bleibt offen.

## Ladungsidentität für mehrere Kerne

Für Kern $i$ mit Massenzahl $A_i$ und Protonenzahl $Z_i$ gelten die Ladungen $(3A_i g_J,Z_i e)$. Für jedes Elektron sind sie $(g_J,-e)$. In einer festen kartesischen Projektion gilt daher als Dipoloperatoridentität
$$
\frac{D_J}{g_J}+\frac{D_A}{e}=\sum_i(3A_i+Z_i)x_i.
$$
Die linke Seite enthält beide Dipole. Rechts bleibt die reine Kernprojektion, unabhängig von elektronischen Korrelationen und Umlagerungen. Für eine kleine Verschiebung entlang einer Koordinate $Q$ definiere $b=\sum_i(3A_i+Z_i)\partial_Q x_i$ und $z_*=\partial_Q D_A/e$. Der zweite Faktor ist die elektrische Dipolableitung einschließlich der elektronischen Polarisation. Die Feldrichtung der Schwingung lautet $(g_J(b-z_*),e z_*)^{\mathsf T}$. Eine rein elektronische Bewegung bei festgehaltenen Kernen hat Richtung $(-g_J,e)^{\mathsf T}$. Die Determinante beider Spalten ist $-e g_J b$. Für $e g_J\ne0$ entscheidet somit $b\ne0$ über die Unabhängigkeit gegenüber einer rein elektronischen Antwort. Eine gemeinsame Beimischung des elektrischen Stroms zur J-Kopplung und jede invertierbare kinetische Normierung erhalten den Rang.

Für zwei Kerne mit Massen $M_1,M_2$ und $Q=x_1-x_2$ hat die Kernbewegung bei fixiertem Kernschwerpunkt
$$
b_{\rm Kern}=\frac{(3A_1+Z_1)M_2-(3A_2+Z_2)M_1}{M_1+M_2}.
$$
Der Kernschwerpunkt dient hier nur als führende Näherung. Für den fixierten Gesamtschwerpunkt sind in der Identität die tatsächlichen Kernableitungen einzusetzen. Bei starren Fragmenten mit je einem Kern und fest zugeordneten Elektronen gilt dieselbe relative Formel mit den Fragmentmassen und den entsprechenden Fragmentladungen. Haben beide Fragmente zusammen elektrische Ladung null, ist $z_*$ in dieser starren Näherung die elektrische Ladung von Fragment 1 in Einheiten von $e$. Ein polarisierbares Molekül hat im Allgemeinen eine andere Dipolableitung. Die Kernidentität hält auch dann, wenn ein starres Ionenmodell $z_*$ falsch angibt.

## HD als Beispiel für einen elektrisch dipolstillen Stretch

Für Proton und Deuteron ist $Z_1=Z_2=1$ und $(A_1,A_2)=(1,2)$. Hier gilt also $(3A_1+Z_1,3A_2+Z_2)=(4,7)$. Im adiabatischen Modell mit festgehaltenen Kernen hat der elektronische Grundzustand Symmetrie unter Inversion am geometrischen Mittelpunkt, da beide Kerne dieselbe elektrische Ladung haben. Das elektrische Dipolmoment und seine Streckableitung verschwinden in dieser Näherung. Die reale HD-Spektroskopie besitzt schwache elektrische Dipolübergänge durch nichtadiabatische Effekte. [Pachucki und Komasa](https://doi.org/10.1103/PhysRevA.78.052503)

Für $Q=x_p-x_d$ und einen festgehaltenen Gesamtschwerpunkt liefert der geometrische Mittelpunkt der Elektronendichte Gewicht $m_e$ an jeder Kernposition. Damit folgt mit derselben Punktkern-Identität
$$
b_{\rm HD}=\frac{4(M_d+m_e)-7(M_p+m_e)}{M_p+M_d+2m_e},\qquad
v_{\rm HD}=(g_J b_{\rm HD},0)^{\mathsf T}.
$$
In der Näherung $M_d\simeq2M_p$ und $m_e\ll M_p$ ist $b_{\rm HD}\simeq1/3$. Mit den [CODATA-Massenverhältnissen](https://physics.nist.gov/cuu/pdf/all.pdf) ergibt sich $b_{\rm HD}\simeq0{,}331455$. Die Streckbewegung gibt damit im Modell bei fixiertem Gesamtschwerpunkt eine reine J-Richtung in den ursprünglichen Kopplungskoordinaten. Für $K=I$ und $|g_J/e|=1$ hat sie zusammen mit der normierten elektronischen Richtung eine Konditionszahl $1+\sqrt2$. Das ist eine Aussage über die Richtung zweier normierter Antworten. Ihre tatsächlichen Amplituden hängen von Übergangsmatrixelementen, Suszeptibilitäten, Orientierung und Transduktion ab.

## Was der Rang für eine Apparatur bedeutet

Für zwei entkoppelte lineare Antworten $\chi_{\rm el}$ und $\chi_{\rm vib}$ hat die lokale Feld-zu-Dipol-Matrix in einem gemeinsamen Frequenzfenster die Form $\chi_{\rm el}v_{\rm el}v_{\rm el}^{\mathsf T}+\chi_{\rm vib}v_{\rm vib}v_{\rm vib}^{\mathsf T}$ und Determinante $e^2 g_J^2 b^2\chi_{\rm el}\chi_{\rm vib}$. Für endliche nichtverschwindende Antworten und $b\ne0$ ergibt das lokal Rang zwei, sofern beide Felder bereits als unabhängige Eingänge verfügbar sind. Ein einziges uniformes elektrisches Feld bei einer einzigen Frequenz liefert nur einen Antrieb. Es treibt den idealen HD-Stretch wegen $z_*=0$ im linearen elektrischen Dipolterm überhaupt nicht. Ein alternativer mechanischer oder optischer Transduktionskanal benötigt einen eigenen Antriebs- und Empfangsnachweis. Eine nichtlineare optische Ansteuerung mit Hilfsfeld hätte andere Endpunkt-Übertragungsfunktionen als ein direkter Dipolanschluss. Messband, freie J-Ausbreitung, reale Kopplungsstärke und profilgebundene Effekte bleiben offen.

## Rechenkontrolle

[Wolfram Language](op5_j_molekuelanschluesse.wl) prüft Ladungsidentität, Kernkoeffizient, beide Determinanten und die Konditionierung symbolisch sowie den HD-Koeffizienten numerisch. Die tatsächliche Print-Ausgabe lautet

```text
charge identity residual = 0
two-nucleus relative coefficient = (-3*a2*mass1 + 3*a1*mass2 + mass2*z1 - mass1*z2)/(mass1 + mass2)
clamped-electron and vibration determinant = -(bend*electric*g)
two-mode susceptibility determinant = bend^2*chiElectronic*chiVibration*electric^2*g^2
HD weighted midpoint coefficient = 4 - (11*(electronMass + mass1))/(2*electronMass + mass1 + mass2)
HD coefficient with CODATA masses = 0.331454697
balanced normalized condition for a purely J vibrational direction = 1 + Sqrt[2]
```

Der separate Rückgabewert war `Null`. Qiskit wurde geprüft. Die Rechnung verwendet Ladungsoperatoren und lineare Suszeptibilitäten. Eine Quantenschaltung würde die fehlende experimentelle Transduktion nicht bestimmen. H96 bleibt offen.
