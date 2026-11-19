# OP5: Neutralbesetzung und Pauli-Blockierung der Z-String-Mode

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [Maxwell-Schranke](W2_Z_Nullmoden.md) schließt einen signierten B−L-Überschuss in den isolierten chiralen Nullmoden bei endlicher Energie pro Länge aus. Sie lässt eine ladungs- und stromneutrale Besetzung mit Energie zu. Hier wird ihre zweite Energievariation in einem projizierten Modenpaar berechnet. Der negative logarithmische Beitrag des Fermionvakuums und die mögliche Rolle besetzter Zustände motivieren den Vergleich. [Naculich](https://doi.org/10.1103/PhysRevLett.75.998), [Perturbed electroweak strings and fermion zero modes](https://doi.org/10.1016/0550-3213(96)00158-7).

## Eine explizite neutrale Belegung

Setze für ein Paar gegenläufiger, masseloser Dirac-Moden den axialen Impuls $p$ und den projizierten Hamiltonoperator

$$
H(p,a)=p\,\sigma_3+g a\,\sigma_1,\qquad
E_\pm(p,a)=\pm\sqrt{p^2+g^2a^2}.
$$

Hier ist $a$ die reelle Amplitude einer symmetriebrechenden Verformung und $g a$ ihr Mischungsmatrixelement. Eine kompensierende bosonische Änderung der Eichladungsverteilung wäre im vollständigen System separat zu behandeln. Das folgende Modell prüft nur die projizierte Energie. Die Impulsdichte der Zustände pro Länge ist $dp/(2\pi)$. Wähle eine Grenze $\Lambda$ des projizierten Bereichs und $0<k_F<\Lambda$.

Im Diracvakuum ist pro $p$ genau die negative Stufe besetzt. Für jedes Paar $p,-p$ mit $0<p<k_F$ besetze im Zustand bei $p$ beide Stufen und bei $-p$ keine. Bei $a=0$ fügt dies für den rechtslaufenden Zweig bei $p$ ein Teilchen hinzu und nimmt bei $-p$ ein Teilchen derselben Art weg. Die integrierte Besetzungsdifferenz und ihr Längsstrom sind je Art null. Die Zustände außerhalb des Intervalls bleiben im Vakuum. Auch die Änderung der projizierten integrierten diagonalen Quellen unter Mischung hebt sich bei $\pm p$ auf, da die Diagonalen der beiden negativen Projektoren zu eins addieren. Die beiden Besetzungsmuster innerhalb des Intervalls haben zusammen dieselben diagonalen Summen. Lokale radiale Quellen und die bosonische Rückreaktion folgen daraus nicht.

Man kann bei $k_F/\sqrt2$ die Wahl der beiden Vorzeichen tauschen. Dann heben sich auch die zusätzlichen axialen Impulse auf, weil die beiden Teilintegrale von $p\,dp$ gleich sind. Die folgende Energiebilanz hängt von dieser Wahl nicht ab. Sie vergleicht festgehaltene Besetzungen, also einen angeregten Zustand mit eigenen Besetzungsdaten.

## Der blockierte Bereich und die verbleibende Krümmung

In einem Impulsblock mit zwei besetzten Zuständen ist die Energie $E_++E_-=0$. In einem leeren Block ist sie ebenfalls null. Die Verformung verändert daher die Energie der präparierten Belegung innerhalb von $|p|<k_F$ nicht. Außerhalb bleibt die Energieänderung des besetzten negativen Zweigs. Pro Längeneinheit ergibt sich exakt

$$
\Delta \mathcal E_{\rm proj}(a)
=-\frac1\pi\int_{k_F}^{\Lambda}
  \left(\sqrt{p^2+g^2a^2}-p\right)\,dp
=-\frac{g^2a^2}{2\pi}\log\frac{\Lambda}{k_F}+O(a^4).
$$

Die Entwicklung gilt bei festem $k_F>0$ und $|g a|\ll k_F$. Das Diracvakuum ohne Besetzung hat als Gegenprobe dasselbe Integral mit Untergrenze null. Für $\Delta=g a$ lautet der dortige führende Ausdruck $-\Delta^2\log(2\Lambda/|\Delta|)/(2\pi)+O(\Delta^2)$. Die neutrale Besetzung schneidet also die infrarote logarithmische Verstärkung ab. Sie lässt in diesem Kanal einen regulären negativen quadratischen Beitrag zurück.

Sei $K_{\rm rest}(\Lambda)$ der quadratische Koeffizient aller übrigen Beiträge in derselben Normierung, einschließlich bosonischer Variation, passender Gegenterme und Moden außerhalb der Projektion. Zusammen ist die Krümmung

$$
K_{\rm tot}=K_{\rm rest}(\Lambda)-\frac{g^2}{\pi}\log\frac{\Lambda}{k_F}.
$$

Für eine strikte positive Krümmung in dieser Richtung muss $K_{\rm rest}(\Lambda)$ positiv genug sein. Weder der Wechsel der Besetzung noch ein frei gewählter Projektionsschnitt setzt den passenden Wert von $K_{\rm rest}(\Lambda)$ fest. Bei verschwindender Gesamtkrümmung wäre die höhere Variation zu prüfen. Die verbleibende Krümmung entspricht auch im günstigsten Grenzfall $k_F\to\Lambda$ höchstens dem übrigen Koeffizienten. Die Rechnung enthält keine Variation anderer physischer Richtungen.

## Welche Erhaltung hält die Belegung fest?

Alle betrachteten Netto-Ladungen können sowohl im Diracvakuum als auch in der neutral angeregten Belegung null sein. Die Ladungsbedingungen allein unterscheiden die beiden Zustände daher nicht. Im freien projizierten Modell ist die Anregungsenergie gegenüber dem Vakuum positiv. Werden nur die Netto-Ladungen fixiert und darf die Besetzung variieren, ist das Vakuum energetisch günstiger. Das ist keine Aussage über Zerfallszeiten in einem isolierten System. Für die angenommene Blockierung braucht es eine zusätzliche Präparation, einen Erhaltungssatz für die relevant besetzten Moden oder eine begründete langlebige Nichtgleichgewichtsbelegung.

Damit ist ein konkreter Mechanismus zur Abschwächung des negativen Fermionvakuumterms gezeigt. Eine native W2-Stabilisierung, die Endpunktbindung und H96 folgen daraus nicht. Für OP5 fehlen die aus derselben Wirkung berechneten Mischungsmatrixelemente, die übrige Krümmung und eine dynamisch begründete Besetzung. I3 braucht weiterhin eine eigenständige Überschussdynamik.
