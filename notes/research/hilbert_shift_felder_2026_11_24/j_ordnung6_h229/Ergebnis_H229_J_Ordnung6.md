# Ergebnis H229 (k443): Das volle Quadrat N² wählt den Zweig richtig, legt den Winkel φ aber nicht fest

Stand 28.11.2026. Vorab-Notiz `Vorab_H229_J_Ordnung6.md` (Commit ae9db36, vor der Rechnung). Hauptrechnung `k443_test_h229.py` mit Ausgabe
`k443_out.txt`, Gegenprobe in Wolfram `k443b_gegenprobe.wl` mit Ausgabe `k443b_out.txt`.

## Frage

Der Autor hat gewählt, das Postulat J bei Ordnung 6 auf Probe zu lockern. Zugelassen wird der J-verbotene Teil in der Form, die ihn natürlich
erzeugt, nämlich das volle Quadrat der kubischen Norm λN² mit λ ≥ 0. Bei K = ⅔ ist sein δ-Teil 2r⁶ g(δ) mit g = −2√2 cos 3δ + cos 6δ, beide Terme also
mit festem Verhältnis. Gefragt war, ob dieser Term (a) in beiden Sektoren den Datenzweig wählt, (b) den Winkel φ als Minimum der gemeinsamen
Vakuumenergie auf den Messwert legt und (c) ohne Drehung die beiden Versätze aus einer Stärke w erklärt.

## Urteil: widerlegt

| Teil | Ergebnis | Entscheidung |
|---|---|---|
| a (nicht blind) | Für alle w von 10⁻⁴ bis 3 und φ von 0,01 bis 0,06 liegt das globale Minimum beider Sektoren auf dem Datenzweig | bestätigt, wie vorab erwartet |
| b (blind) | Globale Minima von E(φ; w): für w ≤ 0,03 das Paar **π/12 und π/6**, für w ≥ 0,1 genau **π/8**; feine Abtastung (60 Werte von 10⁻⁴ bis 10) zeigt nur diese beiden Lagen. Nächster Abstand zu x: 562 % | **kein Treffer**, auch nicht mit angepasstem w |
| c (blind) | Bei φ = 0 bleibt der Im-Versatz für jedes w exakt null (Wolfram: g′(5π/4) = 0, Reste unter 10⁻²⁰); nur der Re-Versatz wächst mit w (0,0021 bei w = 10⁻³, 0,0194 bei 10⁻², 0,110 bei 0,1) | **kein w** gibt den Im-Versatz x |

**Gesamturteil nach Vorab: widerlegt.**

## Lesart

- **Zweig:** Die Lockerung leistet, was H223 nachträglich gesehen hatte. Das volle Quadrat liefert über Stabilität (λ ≥ 0) das Vorzeichen, das die Daten
  verlangen, und das Zusammenspiel mit cos 6δ ändert daran im ganzen geprüften Bereich nichts. Die Setzung „q < 0“ aus H222 ließe sich so durch die
  Postulatsänderung ersetzen. Das ist aber ein Tausch: Eine gesetzte Zahl (Vorzeichen) wird gegen eine geänderte Regel (J bei Ordnung 6) getauscht.
- **Winkel:** Der Sektortausch V_Re(−δ; π/4 − φ) = V_Im(δ; φ) gilt für jedes q und r (H225), also auch für das feste Verhältnis aus N². Die Minima liegen
  deshalb symmetrisch um π/8, und hier sogar nur an den ausgezeichneten Stellen π/12, π/8 und π/6. Das neue Verhältnis der Terme verschiebt nur, welche
  dieser Stellen gewinnt; einen Zwischenwert wie x erzeugt es nicht.
- **Ohne Drehung:** Der Im-Datenzweig 5π/4 (Klasse von π/12) ist ein stationärer Punkt von g. N² kann ihn deshalb nicht verschieben, sondern nur den Re-Zweig.
  Die beiden Versätze, die in den Daten fast gleich sind, kommen so nicht aus einer gemeinsamen Stärke. Das bestätigt H221 mit anderem Ansatz: Der gemeinsame
  Versatz ist ein Winkel, keine Skala.

## Korrektur vor der Auswertung

In der ersten Fassung von Teil c setzten Skript und Gegenprobe den Im-Datenzweig direkt bei δ = π/12 − x an. Dort hat das Sektorpotential aber kein
Minimum. Der Datenzweig ist das Minimum bei 5π/4 + φ, das in der Spektralklasse π/12 − φ entspricht (4π/3 − δ, Konjugation). Ebenso entspricht im
Re-Sektor π/2 + φ der Klasse π/6 − φ. Beides wurde korrigiert, bevor Teil c ausgewertet war; Kriterium und Teile a/b blieben unverändert (a und b sind
im zweiten Lauf zeichengleich). Der verworfene erste Wolfram-Wert (w* = −3,09, ein Maximum) ist im Kopf von `k443b_out.txt` vermerkt.

## Gegenprobe

- N² und der δ-Teil g(δ) bei K = ⅔ symbolisch bestätigt.
- Teil c: g′(5π/4) = 0, g″(5π/4) = 18, g′(π/2) = −6√2; Im-Versatz bei φ = 0 für w = 10⁻³ bis 3 kleiner als 10⁻²⁰; Re-Versätze wie in Python (0,0021024,
  0,0194367, 0,1097906, 0,2213950).
- Teil b: globale Minima von E bei w = 0,001 an π/12, bei w = 0,1, 1, 3 an π/8, wie in Python. Warnungen von FindMinimum an flachen Stellen; die
  Gitterbesten stimmen überein.
- Qiskit war nicht geeignet.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt (Postulatsänderung auf Probe):** J gilt bei Ordnung 6 nicht für den Teil, der aus N² kommt; λ ≥ 0; Modell und Sektorvorzeichen aus H225/H168;
  K = ⅔; Zirkulantensektor, Baumniveau.
- **Gerechnet (blind):** Teile b und c. **Nicht blind:** Teil a.
- **Nachträglich bemerkt:** Der Im-Datenzweig ist ein stationärer Punkt des N²-Terms (g′(5π/4) = 0). Bei kleinem w gewinnt das Paar π/12/π/6 statt π/8.

## Folgerung

Die Lockerung von J bei Ordnung 6 klärt das Vorzeichen der Zweigwahl, nicht aber den Wert von φ. Ob der Autor die Lockerung wegen des Vorzeichens
behalten will, ist eine eigene Entscheidung: Sie ersetzt die Setzung q < 0 durch eine Regeländerung, und die Daten prüfen den Zweig weiterhin mit 51σ
(H222). Für φ ändert sich nichts, es bleibt die eine Messzahl des Leptonbilds. OP3 bleibt offen.

Vergeben: H229, k443. Nächste frei: H230, k444 (vor Vergabe gegen `main` prüfen).
