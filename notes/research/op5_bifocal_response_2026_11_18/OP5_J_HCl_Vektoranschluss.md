# OP5 – Gemeinsamer Vektorübergang in H³⁵Cl

20. November 2026. Analytische Erkundung im Materieframe M. Das Modell verwendet die bisherige OP5-Punktkern-Ladungstabelle. Die molekulare Zahlenschätzung verwendet einen harmonischen radialen Übergang und vernachlässigt Hyperfeinstruktur, Stöße und den Rückstoß des gesamten Moleküls durch das Strahlungsfeld. Der interne Elektronenbeitrag zur Schwerpunktsdefinition bleibt erhalten.

## Vorwissen geprüft

Die GitHub-Übergabe nach [PR #208](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/llm/Uebergabe.md) setzt den freien HD-Rotor mit getrennten Raman- und J-Paritäten als Ausgangspunkt. Die [Mehrkern-Identität](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Molekuelanschluesse.md) bestimmt die vom Elektronendipol unabhängige Kombination. Der [A/B-Vergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Sende_Empfangsports.md) braucht zwei stabile Anschlüsse an jedem Ende. In den lokalen Vorab-Notizen und unter analysis ergab die Suche nach HCl, LiH und polaren Molekülen keinen früheren einschlägigen Treffer. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt dieser Schritt bei der lokalen Auslese. Für I3 wäre anschließend eine eigene Populationsdynamik erforderlich.

## Gemeinsame Linie und relative Kopplung

Rückwärts verlangt die HD-Auswahlregel hier zwei Operatoren vom Rotationsrang eins. Beim polarisierten R(0)-Übergang $(v,N,M)=(0,0,0)\to(1,1,0)$ von H³⁵Cl besitzen der elektrische und der hypothetische J-Dipol denselben Winkelfaktor $1/\sqrt 3$. Beide sprechen denselben oberen Zustand ohne orientierendes Gleichfeld an. Die gemessene Linie liegt bei $2906{,}246352\,\mathrm{cm}^{-1}$ beziehungsweise $0{,}360329$ eV. Der aus gemessenen Intensitäten bestimmte radiale elektrische Matrixelementbetrag ist $0{,}0719426$ Debye (in Tabelle 2 mit 2 % Unsicherheit). [Linienlage, Tabelle II](https://diverdi.colostate.edu/C372/experiments/ro-vib%20spectra%20of%201HCl%20and%202HCl/references/j_mol_spect_1993_v159_p1274.pdf) · [Dipolmatrixelement für $m=1$, Tabelle 2](https://doi.org/10.1016/j.jqsrt.2011.03.014)

Setze $\mathbf r=\mathbf x_{\rm H}-\mathbf x_{\rm Cl}$ und $\mathbf d=\mathbf D_A/e$. Dann ist $\sum_e\mathbf x_e=\mathbf x_{\rm H}+17\mathbf x_{\rm Cl}-\mathbf d$. Die Schwerpunktbedingung lautet $w_{\rm H}\mathbf x_{\rm H}+w_{\rm Cl}\mathbf x_{\rm Cl}=m_e\mathbf d$ mit $w_i=M_i+Z_i m_e$, wobei $M_i$ die Kernmasse ist. Einsetzen in $\mathbf D_J/g_J+\mathbf d=4\mathbf x_{\rm H}+122\mathbf x_{\rm Cl}$ gibt die interne Operatoridentität
$$
\mathbf D_J/g_J=b\mathbf r+(c-1)\mathbf d,\qquad
b=\frac{4w_{\rm Cl}-122w_{\rm H}}{w_{\rm H}+w_{\rm Cl}},
\quad c=\frac{126m_e}{w_{\rm H}+w_{\rm Cl}}.
$$

Seien $r_{10}$ und $a_{10}$ die radialen Matrixelemente von $\mathbf r$ und $\mathbf d$ vor dem gemeinsamen Winkelfaktor. Dann ist die Anschlussrichtung
$$
v_{\rm HCl}=\frac1{\sqrt 3}\bigl(g_J[b r_{10}+(c-1)a_{10}],\,e\,a_{10}\bigr)^{\mathsf T}.
$$
Mit Kernmassen $1\,u$ und $35\,u$, $m_e\simeq u/1823$ und der harmonischen Wellenzahl $2990{,}9463\,\mathrm{cm}^{-1}$ ergibt sich $b\simeq0{,}49904$, $c\simeq0{,}001919$ und $|r_{10}|\simeq0{,}07614$ Å. Die gemessene elektrische Stärke entspricht $|a_{10}|\simeq0{,}01498$ Å. Die Intensität liefert den Betrag. Für gleiches beziehungsweise entgegengesetztes Vorzeichen der beiden radialen Matrixelemente sind die geschätzten Beträge $|D_J/D_A|$ rund $1{,}54\,|g_J/e|$ beziehungsweise $3{,}53\,|g_J/e|$. Die Zahlen verwenden die harmonische Näherung für das Kernmatrixelement. Sie geben das Verhältnis der Dipolamplituden bei gleicher Feldnorm in der ursprünglichen Kopplungsbasis. Eine Umwandlungsrate braucht zusätzlich Linienbreite, Besetzung, Modenüberlapp und die physische J-Kopplung. [Harmonische Spektroskopiekonstante](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7647010&Mask=1000)

## Zwei Anschlüsse bei derselben Frequenz

Die isolierte R(0)-Linie hat im Feldindex eine Suszeptibilität proportional zu $v_{\rm HCl}v_{\rm HCl}^{\dagger}$ und damit Rang eins. Weitere Polarisationen des gleichen Rotationsmultiplets ändern den Winkelanteil und behalten dieselbe Richtung im zweidimensionalen Feldraum.

Als Referenz bei derselben Frequenz dient in einem idealisierten zweiten, getrennt adressierten Volumen die unterhalb der ersten elektrischen Anregung angeregte Polarisation von atomarem Wasserstoff. Bei fixiertem H-Gesamtschwerpunkt hat sie bis auf einen gemeinsamen skalaren Faktor die Richtung $v_{\rm H}=(g_J(h-1),e)^{\mathsf T}$ mit $h=4m_e/(M_{\rm H}+m_e)$. Der spektrale Ausdruck der verlustfreien Coulomb-Polarisierbarkeit gewichtet jeden Beitrag zum statischen Wert bei Energie $E$ mit $1/[1-(E/\Delta E_n)^2]$. Alle Beiträge sind positiv und $\Delta E_n\ge 10{,}2$ eV im gerundeten Vergleich. Bei $0{,}360329$ eV ist die Abweichung vom statischen Wert daher höchstens rund $0{,}125\,\%$.

Für die beiden Spalten gilt
$$
\det[v_{\rm H},v_{\rm HCl}]=
-\frac{e g_J}{\sqrt 3}\,[b r_{10}+(c-h)a_{10}].
$$
Im Zahlenbeispiel erreicht der Betrag der Korrektur $(c-h)a_{10}$ etwa $1{,}08\cdot10^{-4}$ des führenden Terms. Beide Vorzeichen ergeben damit Rang zwei bei $e g_J\ne0$. Eine konstante invertierbare kinetische Normierung erhält diesen Rang. Die resonante HCl-Antwort und die off-resonante H-Antwort haben verschiedene frequenzabhängige Stärken und Phasen. Für die Matrixmessung müssen zwei Antriebe unabhängig auf die beiden lokalen Antworten zugreifen. Ist $S$ die Matrix ihrer Modenüberlappungen einschließlich der lokalen Antwort, gilt $\det([v_{\rm H},v_{\rm HCl}]S)=\det[v_{\rm H},v_{\rm HCl}]\det S$. Dieselbe Bedingung gilt entsprechend für zwei Empfangskanäle am anderen Ende. Ein räumlich gemeinsamer uniformer Antrieb liefert nur eine Spalte. Zwei separat adressierte Volumina erlauben im idealen lokalen Modell eine diagonale Überlappungsmatrix mit zwei nichtverschwindenden Einträgen. Die gemeinsame freie Streckenmode und die Stabilität beider Anschlussmatrizen beim Profilwechsel bleiben experimentelle Voraussetzungen.

Für einen frei propagierenden massiven J-Kanal muss die Ruheenergie unter der Linienenergie liegen. Das frühere MeV-Massenfenster liegt oberhalb dieser Kante. Die native J-Kopplung, kalibrierte absolute Anschlussstärken, die A/B-Endpunktkontrolle und H96 bleiben offen.

## Wolfram-Kontrolle

[Wolfram Language](op5_j_hcl_vektoranschluss.wl) prüft die Schwerpunktidentität, die Determinanten und den Rotationsfaktor und berechnet die Zahlen im angegebenen Modell. Qiskit wurde geprüft. Die Aufgabe beruht auf Operatoridentitäten und linearer Antwort. Eine Schaltung würde keine zusätzliche Information über die beiden räumlichen Antriebe oder das radiale Matrixelement liefern.

### Tatsächliche Wolfram-Ausgabe

```text
During evaluation of In[1]:= center-of-mass residual = 0
During evaluation of In[1]:= relative-coordinate residual = 0
During evaluation of In[1]:= two-column determinant = -(e g (c electricLength + b radial))
During evaluation of In[1]:= one-line Gram determinant = 0
During evaluation of In[1]:= drive determinant residual = 0
During evaluation of In[1]:=                            1
rotational projection = -------
                        Sqrt[3]
During evaluation of In[1]:= b and c (mass-number approximation) = {0.4990403, 0.001919386}
During evaluation of In[1]:= harmonic radial matrix element [angstrom] = 0.07613970
During evaluation of In[1]:= electric matrix element length [angstrom], magnitude = 0.01497804
During evaluation of In[1]:= absolute reduced J/A ratios for signs +,-, in units |g/e| = {1.53875, 3.53491}
During evaluation of In[1]:= R(0) energy [eV] = 0.36032862
During evaluation of In[1]:=                                  e g (-4 electricLength electronMass + c electricLength electronMass + c electricLength massH + b electronMass radial + b massH radial)
hydrogen and HCl determinant = -(--------------------------------------------------------------------------------------------------------------------------------------)
                                                                                          electronMass + massH
During evaluation of In[1]:= H recoil factor (mass-number approximation) = 0.002192982
During evaluation of In[1]:= fractional determinant correction bound for either dipole sign = 0.0001078497
During evaluation of In[1]:= upper bound on H dynamic/static dipole polarizability ratio = 1.00124951

Out[1]= Null
```
