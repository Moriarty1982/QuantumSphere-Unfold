# OP5: Welche Ladung liest der Higgsradius in W2?

19. November 2026. Analytische Erkundung, nicht blind. Einordnung in OP5 und T9, mit W2 als begrenztem Wirkungsansatz. Alle Größen liegen in einem gemeinsamen statischen Materie-Ruhesystem. Teilchen-Antiteilchen-Vertauschung bezeichnet hier Ladungskonjugation im ersatzweise betrachteten Dirac-Sektor. Die Tachyon-Abbildung $z\mapsto iz$ aus Konvention F ist eine eigene Operation.

## Rückwärtsanforderung und Vorwissen

Ein Kandidat für die beiden Sonden müsste die signierte Belegung an jedem Brennpunkt unterscheiden. Die [Sondenform](Sondenform.md) bestimmt aus zwei separat kalibrierten Signalen die beiden Distanzen. Sie gibt kein Gesetz vor, das eine ungerade Ladungsvariation in diese Signale überträgt. [W2_Ladung](W2_Ladung.md) liefert im klassischen Dirac-Ansatz $B-L$ als globale Ladung, und [W2_Frame](W2_Frame.md) schließt ihre direkte Identifikation mit einer unter dem nativen M/T-Wechsel ungeraden Ladung in den geprüften Realisierungen aus. Geprüft wird hier die schwächere Frage, ob der vorhandene Higgsradius eine **räumliche** Trennung positiver und negativer globaler Ladung im gemeinsamen Chart lesen kann.

[Grenze_W2](Grenze_W2.md) prüft eine statische Higgswand und eine zusätzlich eingeführte neutrale Sonde. Hier wird stattdessen die vorhandene Dirac-Yukawa-Quelle des Higgsradius aus dem [W2-Ansatz](../v4_10_0_r82/Wirkung_W2_Higgs.md) ausgewertet. Der Abschnitt „Bereits beantwortet“ der [OP5-Anleitung](../../anleitungen/op5-vergleichsmodell-rechnen.md) betrifft das andere, eingefrorene Vergleichsmodell. Die [Q²-Bilanz](Quellkopplung.md) setzt eine lineare Quelle voraus. Der folgende Befund prüft, ob die radiale W2-Kopplung diese Quelle im beschriebenen Sektor überhaupt liefern kann.

## Die radiale Yukawa-Quelle enthält die Summe

Fixiere Higgswinkel und Hintergrundmetrik, setze Vektorhintergründe auf null und verwende die Dirac-Lesart ohne Majorana-Term. Schreibe $h=|\Phi|$, $m_i(h)=y_i h$ für eine Masseneigenart $i$ mit reellem nichtnegativem $y_i$ in dieser Normierung. Für eine statische, spinunaufgelöste lokale Gasreduktion mit festen Besetzungen $f_{i,+}(x,p)$ und $f_{i,-}(x,p)$ ist die Vakuum-subtrahierte Materieenergie

$$
E_{\mathrm{mat}}[h;f]
=\sum_i\int d^3x\,d\Pi\;
\sqrt{|p|^2+y_i^2 h(x)^2}\,(f_{i,+}+f_{i,-}).
$$

Hier ist $d\Pi$ das Impulsmaß mit konsistent mitgezähltem Spin. Die Variation nach $h$ bei festen Besetzungen ergibt

$$
\frac{\delta E_{\mathrm{mat}}}{\delta h(x)}
=\sum_i\int d\Pi\;\frac{y_i^2 h(x)}{\sqrt{|p|^2+y_i^2h(x)^2}}\,(f_{i,+}+f_{i,-}).
$$

Die globale Ladungsdichte hat demgegenüber die Form $\rho_X(x)=\sum_i q_i\int d\Pi\,(f_{i,+}-f_{i,-})$ mit $q_i=(B-L)_i$. Für jede Variation $\delta f_{i,+}=-\delta f_{i,-}$ innerhalb nichtnegativer Besetzungen ist das gesamte Materiefunktional für **jedes** vorgegebene $h(x)$ identisch. Damit bleiben die radiale Quelle, ihre Ableitungen nach $h$ und die radialen stationären Lösungen bei denselben Randdaten identisch. In dieser Reduktion bleibt die Entartung also auch bei einem nichtlinearen Higgs-Potential bestehen.

Der zugrunde liegende Vorzeichenbefund ist auch ohne lokale Gasnäherung sichtbar: Bei der Dirac-Lagrangedichte mit reellem skalarwertigem Massenprofil ist $\bar\psi\psi$ unter Ladungskonjugation gerade, der Vektorstrom $\bar\psi\gamma^\mu\psi$ ungerade. Das sichert bei gemeinsamem skalarem Hintergrund die Gleichheit der skalaren Quellen eines Zustands und seines ladungskonjugierten Partners. Die stärkere Aussage für beliebige punktweise Besetzungsvariationen oben benutzt die Gasnäherung.

## Zwei Foki mit gleichem Higgsprofil und entgegengesetztem Dipol

Wähle zwei gleiche, glatte, nicht überlappende Dichteprofile $n(x-F_\pm)$ um $F_\pm=\pm w\,e_1$ für eine Dirac-Art mit $q_i\ne0$. Nimm in beiden Profilen dieselbe Impulsverteilung. Zustand A hat Teilchen bei $F_+$ und Antiteilchen bei $F_-$. Zustand B vertauscht beide. Die Besetzungssumme im Orts- und Impulsraum und die globale Gesamtladung null stimmen überein. Bei $N=\int n(x)d^3x$ und zentriertem $n$ ist dagegen der räumliche Ladungsdipol

$$
\mathbf P_X(A)=2wq_iN\,e_1,\qquad
\mathbf P_X(B)=-2wq_iN\,e_1 .
$$

Auch eine getrennte Messung des Higgsradius an mehreren Stellen gibt für beide Konfigurationen dasselbe Signal, wenn dieselbe radiale Lösung gewählt wird. Das illustriert die fehlende Vorzeichenauslese auch bei bekannter Fokusgeometrie. Die Konfigurationen sind vorgegebene Quellenpaare, keine selbstkonsistenten stationären Lösungen des gesamten W2-Feldsystems. Insbesondere können Eichteile, Transport und zusätzliche dynamische Felder auf solche Zustände unterschiedlich reagieren. Der Vergleich behauptet kein allgemeines Verbot eines eich- oder phasenempfindlichen Kanals.

## Konsequenz für die Randkopplung

Der radiale W2-Kanal antwortet auf eine massengewichtete skalare Dichte. Im geprüften reinen Skalarkanal liefert er weder die gesuchte vorzeichenempfindliche Ladungsquelle noch ein aus der signierten Ladung gebundenes Randresiduum. Für eine weitere Rückwärtssuche ist eine vorhandene Kopplung nötig, die auf die Besetzungsdifferenz anspricht, deren Signal im gemeinsamen Chart getrennt zugänglich ist und die Formkoordinate tatsächlich variiert. I3 kann erst mit einer eigenständigen Überschussdynamik weiter geprüft werden. I4 wäre eine eigene Kondensatroute mit neuer Spezifikation der Quelle und der Frame-Abbildung. Die Energie eines vollständigen W2-Zustands, die native OP5-Randwirkung und H96 bleiben offen.
