# OP5 — Synthetische Kreuzspektren und Kalibriergrenzen

20. November 2026. Analytische und numerische Erkundung im Materieframe M auf Basis von [PR #202](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/202). Die nominale Zielantwort und die Störungsformen sind gesetzt.

## Vorwissen geprüft

Der [Gravitationsabgleich](OP5_J_Gravitationsabgleich.md) und die [Reichweitenkalibrierung](OP5_J_Gravitative_Reichweitenkalibrierung.md) bestimmen die nötigen Projektionen. Die [Kalibrierprofile](OP5_J_Kalibrierprofile.md) begrenzen die Abweichung des Quotienten über eine gemeinsame Eingabebox. Der [Minimax-Test](OP5_J_Minimax_Polreduktion.md#gemeinsame-kalibrierfehler) verwertet die dabei gekoppelten Fehler. Rückwärts braucht der Ausschluss eine positive Prüfmatrix an jeder Kalibrierecke und einen durchgehend von null getrennten Nenner. Diese Bedingungen bestimmen das zulässige Fehlerbudget. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt dies vor der absoluten Materieauslese und dem [H96-Vorabtest](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Kreuzspektren aus gemeinsamen Fourieramplituden

Verwendet werden sieben Stützstellen $x=q^2=(1,2,3,4,6,9,10)$ in Modellskalen. Pro Bin werden alle 32 Vorzeichenkombinationen unabhängiger Komponenten $S,B,E_1,E_2,E_G$ gleicher Varianz eins gemittelt. $B$ ist der beobachtete Tracer. Die Amplituden im gemeinsamen Phasenbezug sind reell. Sie modellieren Fourierdaten mit idealisierter Binmittelung. Setze $L(x)=\sum_{t\in\{4,9,16\}}1/(x+t)$ und
$$
U_1=L(S+B)+E_1/5,\qquad
U_2=(1+h)[L(S+B)+E_2/7],\qquad
G=(1+a)(S+3B+E_G)+rS.
$$
Die sechs Spektren nach Mittelung sind

| Spektrum | Wert |
| --- | --- |
| $P_{12}$ | $2(1+h)L^2$ |
| $P_{1G}$ | $(4+4a+r)L$ |
| $P_{1B}$ | $L$ |
| $P_{B2}$ | $(1+h)L$ |
| $P_{BG}$ | $3(1+a)$ |
| $P_{BB}$ | $1$ |

Wolfram Language hat diese Mittelung symbolisch gegen alle 32 Kombinationen geprüft. Die Projektion lässt $Y=(1+h)L^2$ und $X=(1+a+r)L$ übrig. Daher ist die Antwort $y=L(1+h)/(1+a+r)$. Der Term $3B$ und das unkorrelierte $E_G$ verschwinden aus dem partiellen Kreuzspektrum. Der Fehler $rS$ bleibt als mit dem D-Signal korrelierter Anteil erhalten. Beide Split-Eigenrauschen bleiben aus $P_{12}$ heraus. Beispielsweise ist bei $x=1$ und ungestörten Daten $L=61/170$ und $P_{1G}=122/85$.

## Zertifiziertes Fehlerbudget

Die drei Modellfehler sind $a=\eta_a\lambda/100$, $h=\eta_h\lambda x/100$ und $r=\eta_r\lambda x^2/100$. Jeder Koeffizient $\eta$ läuft gemeinsam über alle Bins in $[-1,1]$. Zusätzlich sei die unabhängige absolute Halbbreite des Quotienten $\sigma_j=(x_j+2)/(3\cdot 10^{10})$. Diese Halbbreiten sind als Eingaben gesetzt. Die 32 Vorzeichenkombinationen sind eine exakte synthetische Mittelung und begründen keine Stichprobenunsicherheit. Der Profilrechner umschließt den nichtlinearen Rest. Dessen obere Schranke wird zur unabhängigen Halbbreite addiert. Die drei linearen Profile bleiben über die Bins gekoppelt.

Bei $\lambda=10^{-5}$ sind alle acht Prüfmatrizen nach Abzug der ungünstigsten unabhängigen Fehler positiv definit. Damit sind höchstens zwei Pole plus beliebiger linearer Kontaktterm auf dem angegebenen Raster ausgeschlossen. Die erste Grenze dieser **Matrixprüfung mit Resthülle** liegt zwischen $0{,}0008749172277748584$ und $0{,}0008749172315001488$. Die genaue rationale Klammer lautet $46971761/53687091200$ und $117429403/134217728000$. Der zertifizierte Bereich ist monoton, weil mit $\lambda$ alle linearen Boxbreiten und die Resthülle wachsen. An der Obergrenze fällt mindestens eine Eckmatrix aus der positiven Definitheit. Daraus folgt keine Existenz eines Zweipol-Fits für die exakt nichtlineare Eingabebox.

Am unteren Rand der Klammer sind simultan rund $0{,}000875\,\%$ Gravitations-Gainabweichung, $0{,}00875\,\%$ Split-Transferabweichung und $0{,}0875\,\%$ korrelierte Gravitation pro Einheit der Signalamplitude bei $x=10$ erlaubt. Die exakte Klammer ist für die Prüfung maßgeblich. Die Grenzen gelten für das gesetzte Raster, die Formen $1,x,x^2$ und die oben definierte gemeinsame Skalierung. Unabhängige Kalibriermessungen und binweise OP5-Rohspektren fehlen weiterhin. H96 und die Zuordnung der Antwort zur kosmologischen Materiedichte bleiben offen.

## Reproduktion

```powershell
python op5_j_kreuzspektren.py
python op5_j_kreuzspektren.py --bracket
python op5_j_kreuzspektren.py --raw
```

Der erste Aufruf gibt alle Antwortwerte, Profilspalten und Resthalbbreiten als Brüche aus und prüft die Injektion an 27 Punkten pro Bin. Der zweite berechnet die rationale Klammer. Der dritte gibt JSON mit allen sechs Kreuz- und Autospektren je Bin und den Antwortänderungen der drei injizierten Moden aus. Das JSON ist direkt als Eingabe für `op5_j_kalibrierprofile.py` verwendbar.

[Die erzeugte Eingabedatei](op5_j_kreuzspektren_synthetisch.json) für $\lambda=10^{-5}$ durchläuft den bestehenden Profilrechner und liefert in allen sieben Bins dieselben exakten Profile und Resthalbbreiten wie die direkte Auswertung.
