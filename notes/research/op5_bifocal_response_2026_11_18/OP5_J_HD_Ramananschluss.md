# OP5 — Raman-Anschluss an den HD-Stretch

20. November 2026. Analytische Erkundung im Materieframe M. Untersucht wird eine kohärente Umwandlung zwischen einem optischen Seitenband und einem hypothetischen freien J-Feld über eine Molekülschwingung. Der Ansatz gilt im elektrischen Dipolterm für J und im symmetrischen, nichtresonanten Polarisierbarkeitsterm für Raman.

## Vorwissen geprüft

Der [Molekülvergleich](OP5_J_Molekuelanschluesse.md) ergibt im adiabatischen HD-Modell den körperfesten J-Stretch-Dipol $g_J b_{\rm HD}Q\,\mathbf n$, wobei $\mathbf n$ die orientierte Achse vom Deuteron zum Proton ist und $Q$ hier die Änderung der Bindungslänge bezeichnet. Die normierte Richtung ist von der elektronischen Richtung unabhängig. Der [kohärente A/B-Vergleich](OP5_J_Sende_Empfangsports.md) braucht eine stabile Anschlussmatrix mit Rang zwei an jedem Ende. Die [Endpunktdrift](OP5_J_Endpunktdrift.md) legt fest, was eine profilgebundene Phasenstörung nicht identifizierbar macht. Der [myonische Vergleich](OP5_J_Myonischer_Anschluss.md) schließt freie J-Ausbreitung unterhalb einer angenommenen MeV-Ruheenergie aus. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Rechnung zur lokalen Auslese. Die bei I3 fehlende Populationsdynamik bleibt offen.

## Raman und J-Dipol eines freien Rotors

Für eine lineare Molekülachse hat der symmetrische Raman-Tensor die Form $\alpha_\perp I+(\alpha_\parallel-\alpha_\perp)\mathbf n\mathbf n^{\mathsf T}$. Seine Streckableitung zerfällt in Rotationsanteile vom Rang null und zwei. Für den freien linearen Rotor mit Drehimpuls $N$ erhält sie die Rotationsparität $(-1)^N$. Der J-Dipol ist dagegen zur Achse $\mathbf n$ proportional und ändert diese Parität. Aus $N=0$ erreicht der Raman-Term $N'=0$ oder $2$, der Dipolterm $N'=1$. Das bekannte HD-Grundband für $N=0\to0$ liegt bei $3632{,}16052\ {\rm cm}^{-1}$, entsprechend $0{,}45033$ eV. Dieses Band ist kein freier gemeinsamer Raman/J-Dipolübergang im geprüften Modell. [Rotationsauswahlregeln](https://web.mit.edu/course/6/6.734j/www/group-full.pdf) · [HD-Spektrum, Tabelle 4](https://www.few.vu.nl/~wimu/Publications/Niu-H2-2014.pdf)

Das Ergebnis gilt auch abseits der Resonanz für die lineare Kreuzantwort, wenn Rotor-Hamiltonoperator und Zustand die Parität erhalten. Der Kommutator aus einem geraden Raman- und einem ungeraden Dipoloperator ist dann ungerade und sein Erwartungswert null. Reine Ausrichtung der Achse mittels eines geraden Potentials wie $\cos^2\vartheta$ ändert diese Auswahlregel nicht. Sie unterscheidet die beiden Achsenrichtungen nicht. Auch die Anisotropie des symmetrischen Raman-Tensors genügt dafür nicht.

## Bedingte Umwandlung bei Orientierung

Ein richtungsgebender Zusatzterm $-f\cos\vartheta$ mit $\vartheta=\angle(\mathbf n,\mathbf e_z)$ bricht diese Symmetrie. Als Modell seien $B_0,B_1>0$ die Rotationskonstanten der beiden Vibrationsniveaus. Aus $\langle 1,0|\cos\vartheta|0,0\rangle=1/\sqrt3$ und der Rotationslücke $2B_v$ folgt für den jeweils überwiegend $N=0$-artigen Zustand die erstordentliche Beimischung $f/(2B_v\sqrt3)$ des Zustands $|1,0\rangle$. Die Dipolprojektion zwischen den beiden gekleideten Vibrationszuständen enthält somit den Faktor
$$
\langle\widetilde{N=0;v=1}|\cos\vartheta|\widetilde{N=0;v=0}\rangle
=\frac f6\left(\frac1{B_0}+\frac1{B_1}\right)+O(f^2),
$$
wobei ein gleicher, vibrationsdiagonaler orientierender Koeffizient angenommen wird und der Fehler relativ zu festen $B_v$ zu lesen ist. Der körperfeste Stretch-Matrixwert wird mit diesem Rotationsfaktor multipliziert. Der skalare Raman-Anteil bleibt in derselben Näherung erhalten, sofern sein Stretch-Matrixelement ungleich null ist. Entgegengesetzt orientierte, gleich gewichtete Teilpopulationen löschen die lineare Kreuzantwort durch Parität wieder aus. Eine tatsächlich erreichbare Orientierung und die hierzu nötige Kopplung sind zusätzliche Modellbedingungen. Speziell im adiabatischen neutralen Modell ergibt sich der orientierende Term nicht aus einem uniformen gewöhnlichen elektrischen Dipolfeld.

In der linearisierten Pumpenentwicklung sei $a$ ein oberes optisches Seitenband und $b$ die Schwingung. Für eine feste Pumpenamplitude $P$ dient
$$
H_{\rm int}/\hbar=G\,a b^\dagger+G^* a^\dagger b,\qquad G=\gamma P^*
$$
als Einband-Vergleich. Hier ist $\gamma$ ein fester Überlappungsfaktor. Ein eingehendes Seitenband treibt die Schwingung proportional zu $G$ und die kohärente Rückumwandlung proportional zu $G^*$. Bei Orientierung hat der modellierte J-Dipol dieselbe Übergangsfrequenz wie die Raman-Schwingung, sofern beide denselben gekleideten Übergang ansprechen. Mit einem separat adressierbaren Referenzanschluss entlang $(-g_J,e)$ und dem im adiabatischen Modell rein in J gerichteten Stretch-Anschluss gilt an jedem Ende Rang zwei genau dann, wenn beide Anschlussamplituden ungleich null sind. Diese Bedingung erfasst Pumpen- und Orientierungsfaktoren, Übergangsmatrixelemente und den Modenüberlapp. Die freie J-Ausbreitung bei rund $0{,}45$ eV wäre im früheren MeV-Massenfenster kinematisch ausgeschlossen.

## Pumpenphase im A/B-Vergleich

Im isolierten Umwandlungspfad trägt die Einspeisung $P_T^*$, die Auslese $P_R$. Bei der Phasenkonvention $e^{-i\omega t}$ ist daher mit einer Strecke $e^{i\omega\tau}$ die Steigung
$$
\partial_\omega\arg H=\tau+
\partial_\omega(\arg P_R-\arg P_T)+\partial_\omega\arg C,
$$
wobei $C$ die übrigen lokalen Faktoren einschließlich der Schwingungssuszeptibilitäten und optischen Referenzwege sammelt. $\omega$ ist die Differenzfrequenz. Frequenzunabhängige und während eines Sweeps stabile Pumpenphasen liefern für sich keine Steigung. Ändert der Profilwechsel die frequenzabhängige Pumpenphasendifferenz oder $C$, geht die Änderung in denselben A/B-Kontrast wie die Streckenlaufzeit ein. Eine phasenkohärente gemeinsame Referenz und ein lokaler Kontrollpfad mit unabhängig bekanntem Streckenkontrast wären Bedingungen für die Trennung. Der Ausdruck setzt einen isolierten Umwandlungspfad voraus, ohne additive Leckpfade und mit nichtverschwindender Übertragung.

## Rechenkontrollen

[Wolfram Language](op5_j_hd_ramananschluss.wl) prüft Parität, Überlappung, Phasensteigung und Energieumrechnung. Tatsächliche Print-Ausgabe

```text
Raman parity residual = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
dipole parity residual = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
unoriented cross overlap = 0
first-order oriented rotor overlap = ((b0 + b1)*f)/(6*b0*b1)
phase slope including both pump paths = dR - dT + tau
HD Q(0) energy in eV = 0.450330511
```

Der separate Wolfram-Rückgabewert war `Null`. [Qiskit](op5_j_hd_ramananschluss_qiskit.py) bildet mit einer Ein-Qubit-Zustandsrotation den abgeschnittenen Rotor $N=0,1$ bei $B_0=B_1$ nach. Die Ausgabe zeigt den Vorzeichenwechsel der Dipolprojektion beim Umkehren des Orientierungsfelds. Tatsächliche Python-Ausgabe

```text
f/B = +0.0, <cos(theta)> = +0.0000000000
f/B = +0.1, <cos(theta)> = +0.0332779163
f/B = -0.1, <cos(theta)> = -0.0332779163
```

Der Zweizustandsvergleich liefert keine reale Feldstärke, Ausrichtungseffizienz oder Transduktionsrate. Freie J-Ausbreitung, experimentell kontrollierte Anschlussphasen und H96 bleiben offen.
