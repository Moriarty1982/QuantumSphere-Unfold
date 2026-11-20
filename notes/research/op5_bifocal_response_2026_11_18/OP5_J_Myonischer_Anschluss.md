# OP5 — Myonischer Wasserstoff als zweiter innerer Dipolanschluss

20. November 2026. Analytische Erkundung im Materieframe M. Aus der kleinen Winkeltrennung bei H und D wird rückwärts ein Paar mit deutlich verschiedenen Rückstoßfaktoren gesucht. Konditionierung und absolute Antwort werden getrennt berechnet.

## Vorwissen geprüft

Die [fixierten Isotopenanschlüsse](OP5_J_Fixierte_Isotopenanschluesse.md) bestimmen die Dipolrichtungen und ihre optimal erreichbare Konditionszahl im diagonal-kinetischen Modell. Das [Myonmoment](OP5_J_Myonmoment.md) begrenzt das frühere massive Kopplungsbeispiel mit unverändertem Myonvertex. Die [Neutron–Blei-Rechnung](OP5_J_Neutron_Blei.md) prüft die Variante mit elektromagnetischer Beimischung am Lepton-Nullpunkt. Der [gemeinsame J-Strom](OP5_J_Gemeinsamer_Strom.md) unterscheidet eine gemeinsame Ladungsprojektion von einem zusätzlichen unabhängigen Strom. Der [A/B-Vergleich](OP5_J_Sende_Empfangsports.md) setzt unabhängig zugängliche Anschlüsse an beiden Enden voraus. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale OP5-Auslese. Die bei I3 fehlende kosmologische Populationsdynamik bleibt offen.

## Der schwerere Leptonpartner trennt die Dipolrichtungen

Im Dirac-Ladungsmodell tragen die beiden negativen Leptonen dieselbe ursprüngliche J-Ladung und dieselbe elektrische Ladung. Bezeichne mit $\eta$ eine gemeinsame zusätzliche Vektorkopplung an den elektrischen Ladungsstrom in Einheiten der Elementarladung. In einem gegebenen Modell für den ausgelesenen J-Modus hat das Proton die Kopplung $3g_J+\eta$, das Lepton die Kopplung $g_J-\eta$. Bei fixiertem Schwerpunkt und $\mathbf r=\mathbf x_p-\mathbf x_\ell$ beträgt die Dipolrichtung dann
$$
v_\ell=\binom{a_\ell}{e},\qquad
a_\ell=g_J(-1+\epsilon_\ell)+\eta,\qquad
\epsilon_\ell=\frac{4m_\ell}{m_p+m_\ell}.
$$
Damit ist $\det(v_e,v_\mu)=e g_J(\epsilon_e-\epsilon_\mu)$ unabhängig von $\eta$. Dies gilt insbesondere am Lepton-Nullpunkt $\eta=g_J$, weil dort der rückstoßbedingte Anteil der Protonbewegung verbleibt. Wenn $\eta$ lediglich einen Feldkoordinatenwechsel bezeichnet, bleibt der Rang erhalten, und die Konditionszahl ist erst nach konsistenter Normierung der Kinetik zu bilden.

Mit [CODATA 2022](https://physics.nist.gov/cuu/pdf/all.pdf) ergeben sich $\epsilon_e\simeq0{,}0021773$ und $\epsilon_\mu\simeq0{,}40485$. In einem diagonal-kinetischen Vergleich, in dem die angegebenen Ladungen bereits kanonisch sind, liegt die beste normierte Konditionszahl für $\eta=0$ bei $7{,}78$. Am Lepton-Nullpunkt beträgt sie nach Optimierung des effektiven Kopplungsverhältnisses $1{,}16$. Das sind Geometriewerte nach Einzelnormierung der beiden Antworten. Sie setzen weder die tatsächliche Feldnormierung noch ein zulässiges Kopplungsverhältnis fest. Insbesondere rehabilitiert der verbleibende Dipol am Nullpunkt das frühere massive Parameterfenster nicht. Die Befunde zu Myonmoment und Kernstreuung gelten in ihren jeweiligen Modellannahmen weiter.

## Gemeinsames Frequenzfenster und Stärke der Antwort

Als Referenz für die Antwortstärke werden zwei ideale Punkt-Coulomb-Grundzustände mit derselben elektromagnetischen Kopplung verglichen. Die zusätzliche J-Kraft wird für die atomaren Wellenfunktionen und Energien vernachlässigt. Sei $\mu_\ell=m_p m_\ell/(m_p+m_\ell)$ die reduzierte Masse. Der Coulomb-Hamiltonoperator hat bei Reskalierung der Länge mit $a_\ell^{\rm B}=(\mu_\ell\alpha)^{-1}$ eine massenunabhängige dimensionslose Form. Dipolmatrixelemente skalieren wie $\mu_\ell^{-1}$ und die Übergangsenergien wie $\mu_\ell$. Für die elektrische Polarisierbarkeit in einer festen Raumrichtung gilt im idealen verlustfreien Modell
$$
\alpha_\ell(\omega)=2e^2\sum_{n\ne0}
\frac{\Delta E_{n\ell}|\langle n|r_z|0\rangle|^2}{(\Delta E_{n\ell})^2-(\hbar\omega)^2}.
$$
Die Summe schließt das Kontinuum als Integral ein. Hier bezeichnet $\alpha_\ell(\omega)$ die Polarisierbarkeit und $\alpha$ ohne Index die Feinstrukturkonstante. Bei $\omega=0$ folgt exakt $\alpha_\mu(0)/\alpha_e(0)=(\mu_e/\mu_\mu)^3\simeq1{,}56\times10^{-7}$. Für $|\hbar\omega|\le\Delta E_{\min,e}/2\approx5{,}10$ eV liegt jeder Term beider Spezies zwischen seinem statischen Wert und dem $4/3$-fachen Wert. Daher folgt im gemeinsamen Fenster
$$
\frac{3}{4}\left(\frac{\mu_e}{\mu_\mu}\right)^3
\le\frac{\alpha_\mu(\omega)}{\alpha_e(\omega)}
\le\frac{4}{3}\left(\frac{\mu_e}{\mu_\mu}\right)^3.
$$
Bei elektrisch getriebener innerer Polarisation ist die elektrische Komponente der Dipolantwort damit pro Atom um ungefähr sieben Größenordnungen kleiner. Der Faktor $-i\omega$ bei der Umrechnung in den integrierten Strom ist in beiden Referenzen gleich. Kanalverstärkung oder eine größere Zahl tragender Atome muss separat begründet werden. Eine Resonanz ist in dieser Abschätzung ausgeklammert. Für das fortgeführte MeV-Massenfenster kann zudem in diesem gemeinsamen Teilfenster kein freies massives J-Quant propagieren, da $\hbar\omega<m_Jc^2$. Die Rechnung für die lokale Polarisierbarkeit setzt keine solche Ausbreitung voraus. Auch die endliche Lebensdauer begrenzt eine reale Messung. Als Referenz beträgt die freie mittlere Myonlebensdauer rund $2{,}20\,\mu{\rm s}$. [PDG 2025](https://pdg.lbl.gov/2025/listings/rpp2025-list-muon.pdf)

## Rechenkontrolle

[Wolfram Language](op5_j_myonischer_anschluss.wl) prüft die Determinante und berechnet Konditionszahlen, Massenverhältnis und Polarisierbarkeitsgrenzen. Tatsächliche Print-Ausgabe

```text
common charge-shift determinant residual = 0
electronic recoil = 0.0021772823
muonic recoil = 0.404848327
normalized condition at unit coupling and zero shift = 8.04078255
best normalized condition at zero shift = 7.78356256
normalized condition at unit coupling and lepton null = 5.16482879
best normalized condition at lepton null = 1.15827722
reduced mass ratio = 185.942046
                                                      -7
static electric polarizability ratio = 1.55548985 × 10
                                                                           -7
common half-gap electric polarizability ratio lower bound = 1.16661738 × 10
                                                                           -7
common half-gap electric polarizability ratio upper bound = 2.07398646 × 10
electronic Coulomb gap [eV], using 13.605693123 eV = 10.1987154
```

Der separate Wolfram-Rückgabewert war `Null`. Qiskit wurde für diesen Schritt geprüft. Die Skalierung folgt aus dem kontinuierlichen Coulomb-Hamiltonoperator und der vollständigen Dipolsumme, sodass für die untersuchte Schranke keine modellierte Quantenschaltung nötig ist. Eine bei derselben Frequenz unabhängig adressierbare und kalibrierte Messanordnung ist weiterhin offen. H96 bleibt offen.
