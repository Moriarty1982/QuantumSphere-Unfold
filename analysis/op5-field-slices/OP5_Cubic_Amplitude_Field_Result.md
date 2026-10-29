# OP5: Gradvergleich zwei gegen drei

29.10.2026. Gleiche Region, keine exakte Feldlösung.

Kubische Amplituden besitzen35 statt15 Monome je Mode einschließlich aller gemischten Terme. Frequenzen, Normalisierung h Psi†ZbetaPsi=8, Vergleichskopplungen und Null-Lorentz-Spinverbindung bleiben gleich. Initialisierung beider Läufe aus demselben gespeicherten quadratischen Feld, kubische Koeffizienten zunächst0. Region weiterhin Hyperwürfel Radius .01 um (1,.6,0,0).

Verbesserte Anpassungsabdeckung: dieselben337 Punkte (81 Gitterpunkte und256 pseudorandom Innenpunkte, seed291028); dieselben128 unabhängigen Kontrollpunkte, seed291026. Beide Läufe600 L-BFGS-Iterationen. Keine Aussage über globale Minima; gleiche Iterationen sind keine identischen Rechenzeiten.

Ergebnis auf128 Kontrollpunkten: kubischer RMS .00207949, Maximum .00428749; quadratischer RMS .00198170, Maximum .00383443. Der zusätzliche Polynomgrad bringt damit in diesem Verfahren keinen Genauigkeitsgewinn. Beide verbessern den früheren quadratischen Lauf mit81 Trainingspunkten, aber daraus folgt kein Fortschritt allein durch höheren Grad. Eine Konvergenzfolge ist nicht nachgewiesen.

Zweiter unabhängiger Satz mit512 Punkten, seed291027: kubischer RMS .00212423, Maximum .00448825. Minimale absolute Coframe-Determinante11.8791, größtes g^{00}=-.35543, Q>5.4549. Gesonderter quadratischer Kontrollbericht liegt in OP5_Quadratic_Dense_Validation.json. Die Grenzen gelten ausschließlich an den geprüften Punkten.

Finite Differenzen der expliziten kubischen Feldfunktion und unabhängige NumPy-Residualauswertung an drei Kontrollpunkten bestätigen die analytisch kodierten Ableitungen: Differenzen bei Schritt1e-5 etwa1.2e-8, bei1e-6 unter2.3e-9. Dies ist konsistent mit dem erwarteten Differenzenfehler und deutlich kleiner als der PDE-Rest.

Ein kleiner, stabiler numerischer Rest ist keine bewiesene strukturelle Mindestabweichung. Mögliche Ursachen sind Optimierung/Konditionierung, beschränkte Frequenzwahl, unzureichende Amplitudenfamilie, die bisherige Auslese oder der festgehaltene Vergleichsoperator. Nächster sinnvoller Schritt ist eine Zerlegung des Restes in Gleichungskomponenten und projizierte notwendige Identitäten, samt skaliertem Fehlermaß, bevor weitere Freiheitsgrade eingeführt werden.

Artefakte: OP5_Cubic_Amplitude_Field_Check.py/.json; OP5_Quadratic_Dense_Field_Control.py/.json; OP5_Cubic_Field_Validation.py/.json; OP5_Quadratic_Dense_Validation.py/.json. Torch/NumPy/SymPy und bestehende Vorgängerdaten notwendig. Lokal gespeichert, nicht committed. Paper-Grafik nicht verändert; sie dokumentiert weiterhin den ursprünglichen affinen Stand. OP5 offen.
