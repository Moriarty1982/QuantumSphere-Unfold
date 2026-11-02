# OP5: Spurbedingung und verbleibender zentraler Verbindungsanteil
29.10.2026. Fortsetzung von OP5_Sector_Preserving_Connection_Freedom_Result.md.

Vertrag unverändert: feste Spinoren und erste Ableitungen, kanonische Coframe E0=2dt, Ei=dxi+vi dt, sektorerhaltende hermitesche Zusatzverbindung, Lorentz-Spinverbindung null (torsionsbehafteter Vergleich). Keine neue native Zulässigkeitsbehauptung.

## Spurfreie Kontrolle
Die Zusatzverbindung hat 20 reelle Koeffizienten. Vier unabhängige Spurbedingungen reduzieren auf 16. Der Coframe-Beitrag bleibt auf der proportionalen Startfamilie null. Die Spur wurde als zusätzliche Vergleichsbedingung getestet, nicht als bereits nachgewiesene Forderung von M16/C7.

| Punkt | voller Rang | volle quadratische Restnorm | spurfreier Rang | spurfreier Rest |
|---|---:|---:|---:|---:|
| (1,.6,0,0) | 18 | unter 7e-27 | 16 | .5539983512 |
| (1,.4,.2,.2) | 18 | unter 3e-28 | 16 | .8836878748 |
| (.9,.3,.2,.1) | 18 | unter 8e-28 | 16 | .2463872544 |

Alle vollständigen Restvektoren wurden nach Rückeinsetzen kontrolliert. Die neue dritte Stichprobe erweitert die Evidenz, beweist aber keine regionale Existenz.

## Zentrale Anteile erst nach Elimination bestimmen
Die spurfreie Quellenmatrix wurde mit vollständigem linkem SVD-Nullraum eliminiert. Anschließend wurde C_mu=c_mu I als zusätzlicher zentraler Anteil eingesetzt. Die projizierte Quellenmatrix hat an allen drei Punkten Rang zwei, nicht vier. Ihre beiden nichtverschwindenden Singulärwerte liegen etwa zwischen 1.56 und 3.35; die übrigen unter 9e-15.

Die zwei sichtbaren Kombinationen des zentralen Kovektors beseitigen den verbliebenen Verträglichkeitsrest bis unter 2e-28 in quadratischer Norm. Zwei zentrale Richtungen bleiben im projizierten Kern und können durch Anpassung der spurfreien Komponenten kompensiert werden. Es wird keine Eindeutigkeit des zentralen Feldes behauptet; diese Kernrichtungen sind nicht automatisch Eichfreiheit.

Euklidisch minimale numerische Repräsentanten c_mu:
P1 etwa (0,0,0,0.2222222222).
P2 etwa (.41370095,-.22700770,-.11350385,.07107811).
P3 etwa (.28890319,-.10292348,-.06861566,-.00340320).
Diese Repräsentanten hängen von Koordinaten und Normwahl ab. Insbesondere ist der Wert nahe 2/9 kein Beleg einer Quantisierung oder eines physikalischen Primwerts.

## Aussage
Für diese festgehaltenen Felder lässt sich der volle lokale Erfolg nicht auf die getestete spurfreie sektorerhaltende Verbindungsfamilie beschränken. Ein nichtverschwindender Spuranteil wird benötigt, wenn alle anderen Vertragsbedingungen beibehalten werden. Die Rechnung bestimmt zwei lokale Bedingungen an diesen Anteil, keinen universellen Wert und keine vollständige Feldentwicklung.

Dies ist weder ein Nachweis eines elektromagnetischen Feldes noch eine Herleitung eines neuen U(1)-Sektors aus der nativen Theorie. Ein zentraler Verbindungsterm kann bei geeigneten gemeinsamen Transformationen mit Phasen zusammenhängen; ob die hier benötigten Komponenten regional rein eichartig sind, ist ungeprüft.

Nächste mathematische Aufgabe: die zwei projizierten Bedingungen als Funktionen des Orts ausdrücken und prüfen, ob ein glattes, ggf. geschlossenes zentrales Verbindungsfeld samt spurfreier Ergänzung existiert. Erst danach folgen dessen eigene Wirkungsgleichungen. Ein Minimum-Norm-Fit an drei Punkten ersetzt diese Prüfungen nicht.

Reproduktion: OP5_Sector_Traceless_Check.py/.json. Enthält die unveränderte Vollkontrolle, spurfreien Fit, vollständige linke Elimination und zentralen Quellen-Test. Lokal gesichert, nicht committed; OP5 offen.
