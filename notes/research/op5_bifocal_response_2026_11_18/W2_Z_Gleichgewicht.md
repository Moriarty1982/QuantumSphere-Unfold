# OP5: Erhaltene Ladungen und thermische Fermionbesetzung

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [neutrale Teilchen-Loch-Belegung](W2_Z_Neutralbesetzung.md) blockiert im selben projizierten Dirac-Modenpaar einen Teil der negativen Fermionvariation, sofern ihre Besetzungen festgehalten werden. Geprüft wird hier, ob die ausgeschriebenen W2-Phasenladungen diese Festlegung begründen und welche Krümmung im thermischen Gleichgewicht desselben Modells übrig bleibt.

## Die vorhandenen Ladungen zählen Differenzen

Der [W2-Dirac-Kanal](W2_Ladung.md) verknüpft linkshändige Weyl-Felder paarweise über die Yukawa-Terme. Für die dort ausgewerteten Phasensymmetrien tragen die Weyl-Felder eines Dirac-Paars gegensinnige Gewichte. In der Dirac-Schreibweise ist dies eine Vektorladung. Sie zählt die gewichtete Differenz aus Teilchenzahl und Antiteilchenzahl. Das gilt ebenso für den in der [Maxwell-Prüfung](W2_Z_Nullmoden.md) verwendeten J-Kanal und die elektromagnetische Ladung der ergänzenden Referenz. Der [W2-Aufbau](../v4_10_0_r82/Wirkung_W2_Higgs.md) weist keinen zusätzlichen Erhaltungssatz aus, der in diesem Modenpaar Teilchen- und Lochanregungen addiert.

Die im vorigen Schritt präparierte Belegung und das Vakuum stimmen bei allen betrachteten Netto-Ladungen überein. Die Variante mit gegenläufig aufgeteilten Impulsintervallen kann auch denselben axialen Gesamtimpuls haben. Energieerhaltung in einem abgeschlossenen System bleibt davon getrennt. Die Anregung kann nur abgebaut werden, wenn andere Freiheitsgrade die Energie aufnehmen. Die folgende Rechnung setzt weder einen bestimmten Abbaukanal noch eine Zerfallsrate voraus.

## Gleichgewichtsantwort eines gegenläufigen Modenpaars

Verwende $H(p,a)=p\sigma_3+ga\sigma_1$ und $E=\sqrt{p^2+g^2a^2}$. Setze die chemischen Potentiale der Netto-Ladungen auf null, entsprechend dem ladungsneutralen thermischen Vergleich. Die Besetzungen sind $n_\pm=[1+\exp(\pm E/\Theta)]^{-1}$ bei Temperatur $\Theta>0$ in Energieeinheiten. Für $\pm p$ ist die Summe der diagonalen Erwartungswerte der projizierten Belegung gleich wie im ungestörten neutralen Referenzzustand. Die betrachteten Phasenladungen bleiben damit in diesem Vergleich neutral. Weitere radiale und bosonische Quellantworten gehören nicht zur Projektion.

Die freie Energie je Impulsblock ist $-2\Theta\log[2\cosh(E/(2\Theta))]$. Ihre Ableitung nach $E$ ist $-\tanh(E/(2\Theta))$. Bei festem $\Theta>0$ folgt für die Krümmung pro Länge bei $a=0$

$$
K_{\rm f}(\Theta,\Lambda)
=-\frac{g^2}{\pi}\int_0^\Lambda
 \frac{\tanh(p/(2\Theta))}{p}\,dp .
$$

Dabei ist $\Lambda$ die obere Impulsgrenze der Projektion. Der Integrand hat bei $p=0$ den endlichen Grenzwert $1/(2\Theta)$. Die Temperatur regularisiert den Infrarotlogarithmus. Der Beitrag bleibt für $g\ne0$ bei jeder endlichen Temperatur strikt negativ. Für $\Theta\ll\Lambda$ ist das Integral $\log(\Lambda/\Theta)+O(1)$. Für $\Theta\gg\Lambda$ beginnt es mit $\Lambda/(2\Theta)$. Der zweite Grenzfall beschreibt nur die abgeschnittene Projektion, da Moden oberhalb $\Lambda$ dann thermisch mitwirken können.

Dasselbe Vorzeichen gilt für die zweite Variation der thermischen inneren Energie bei festgehaltener Entropie im regulären thermischen Zweig. Schreibt man $U(S,a)=F(\Theta,a)+\Theta S$ und $S=-\partial_\Theta F$, dann ist $U_{aa}|_S=F_{aa}-F_{a\Theta}^2/F_{\Theta\Theta}$. Wegen der geraden Abhängigkeit von $a$ verschwindet $F_{a\Theta}$ bei $a=0$. Das setzt positive Wärmekapazität und dieselbe Thermodynamik für beide Beschreibungen voraus.

## Welche Art von Besetzung könnte positives Vorzeichen liefern?

Für festgehaltene, impulsweise diagonal besetzte Eigenzustände mit $n_\pm(p)$ trägt ein Block bei $p\ne0$ proportional zu $[n_+(p)-n_-(p)]/|p|$ zur Krümmung bei. Eine nach Energie nicht zunehmende Besetzung hat daher in diesem Kanal höchstens null Krümmung. Genau gleich besetzte Stufen liefern null, wie in der Blockierungsrechnung. Ein positiver Beitrag verlangt eine Besetzungsinversion in genügend stark gewichteten Impulsbereichen. Die betrachteten Netto-Ladungen erzwingen eine solche Inversion nicht.

Damit ist thermische Neutralbesetzung als Quelle einer positiven Fermionkrümmung im geprüften Modenpaar ausgeschlossen. Eine aus W2 hergeleitete stabile Endkonfiguration bräuchte weiterhin einen positiven Beitrag aus der übrigen Wirkung oder einen dynamisch begründeten Nichtgleichgewichtszustand. Die vollständige renormierte Krümmung, die Endpunktbindung und H96 bleiben offen. I3 braucht eigenständige Überschussdynamik.
