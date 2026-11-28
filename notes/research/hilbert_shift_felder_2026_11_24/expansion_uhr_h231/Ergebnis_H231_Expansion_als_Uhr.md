# Ergebnis H231 (k445): Die Expansion kann φ beim Messwert nicht einfrieren – sie lässt es heute rollen, und das verbieten die Atomuhren

Stand 28.11.2026. Vorab-Notiz `Vorab_H231_Expansion_als_Uhr.md` (Commit 3475170, vor der Rechnung). Hauptrechnung `k445_test_h231.py` mit Ausgabe
`k445_out.txt`, Gegenprobe in Wolfram `k445b_gegenprobe.wl` mit Ausgabe `k445b_out.txt`.

## Frage

Der Autor hatte die Idee eines Teilchens, das von einem Energieberg rollt, während sich der Raum ausdehnt. Für φ heißt das: φ ist ein Feld, das im Potential
der gemeinsamen Vakuumenergie (H225) von 0 zum Minimum π/8 rollt, gebremst von der Hubble-Reibung (φ̈ + 3Hφ̇ + V′ = 0). Liefert die Expansion die natürliche
Uhr, die in H228 fehlte, sodass φ beim Messwert x = 0,0395773 stehen bleibt?

## Urteil: widerlegt

| Teil | Ergebnis |
|---|---|
| Verlauf | Für m ≪ H₀ bleibt φ beim Startwert 0 eingefroren (bei μ = m/H₀ = 0,01 heute 4·10⁻⁶). Für m ≫ H₀ rollt es früh los und schwingt mit abnehmender Amplitude um π/8 (μ = 30: heute 0,393). Ein dauerhaftes Einfrieren bei einem Zwischenwert gibt es nicht |
| angepasstes μ* | Genau ein Wert, **μ* = 0,9721**, gibt heute φ = x. Dort rollt φ aber gerade: dφ/d ln a = 0,075 |
| Drift heute | d ln m_e/dφ = 51,5 (das Elektron sitzt nahe der Nullstelle der Brannen-Form). Daraus folgt \|d ln m_e/dt\| = **2,7·10⁻¹⁰ pro Jahr**, das 2,7-Millionenfache der Atomuhr-Grenze von etwa 10⁻¹⁶ pro Jahr |
| natürliche μ-Werte | √Ω_Λ (k251): φ = 0,0288 (−27 %); 1: 0,0418 (+5,7 %); β_sym: 0,0128; 3/2, γ_L, 1/β_sym: 0,09 bis 0,14. Kein Treffer, und alle hätten dieselbe verbotene Drift (2,6·10⁻¹⁰ pro Jahr) |

**Gesamturteil nach Vorab: widerlegt.**

## Lesart

- **Die Expansion bremst, aber sie hält nicht an.** Hubble-Reibung friert ein Feld nur ein, solange H groß gegen m ist, und zwar beim Startwert. Sobald H unter m
  fällt, rollt das Feld weiter zum Minimum. Weil H mit der Zeit abnimmt, wird die Bremse schwächer, nicht stärker. Ein Zwischenwert wie x wird nur durchlaufen.
- **Durchlaufen heißt: heute in Bewegung.** Damit φ gerade heute bei x steht, muss m ungefähr H₀ sein (μ* = 0,97). Das ist bemerkenswert nahe an 1, aber dann
  ändert sich φ heute merklich, und weil m_e an φ so empfindlich hängt, würde sich die Elektronmasse um 2,7·10⁻¹⁰ pro Jahr ändern. Atomuhren schließen das um
  mehr als sechs Größenordnungen aus.
- **Die Nähe von μ* zu 1 ist kein Befund.** Dass ein Feld mit m ≈ H₀ heute „unterwegs“ ist, ist die bekannte Bedingung für jedes heute rollende Feld. Für den Wert
  von x sagt sie nichts, und die Drift schließt den Fall ohnehin aus.

## Gegenprobe

Wolfram integriert die Feldgleichung unabhängig (NDSolve, 25 Stellen): φ(heute) bei μ* 0,03957734041 (Python 0,0395773407), dφ/d ln a 0,0752369; bei μ = 1 0,0418368;
bei μ = √Ω_Λ 0,0288241. d ln m_e/dφ = 51,4886, Drift 2,670·10⁻¹⁰ pro Jahr, wie in Python. Qiskit war nicht geeignet.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt (vorab offen gelegt):** φ als dynamisches Feld mit Potential aus H225; Start φ = 0 in Ruhe bei a = 10⁻⁸; ΛCDM-Hintergrund mit Planck-Werten ohne
  Rückwirkung; Skala μ_e fest; Atomuhr-Grenze 10⁻¹⁶ pro Jahr als Größenordnung aus dem Vorwissen.
- **Gerechnet (blind):** Verlauf für 1201 μ-Werte, μ*, Drift, die natürlichen Werte.
- **Grenzen:** Ein Start auf dem Berggipfel braucht eine freie Auslenkung und wurde nicht gerechnet. Er ändert aber nichts am Kernpunkt: Ein heute durchlaufener
  Zwischenwert rollt heute, und ein früh eingefrorener Wert ist der Startwert. Für ein Einfrieren bei x müsste der Startwert selbst x sein; das ist wieder eine
  Anfangsbedingung.

## Folgerung

Als dynamisches Feld in einem expandierenden Universum kann φ entweder seinen Startwert behalten oder ins Minimum π/8 laufen. Beim Messwert stehen bleibt es
nur, wenn der Messwert der Startwert ist. Wenn φ dagegen heute erst dort ankommt, ändert sich die Elektronmasse messbar, und das ist ausgeschlossen. Damit
gilt: φ = 0,0396 ist eingefroren und gehört zur Anfangsbedingung, oder es braucht einen echten Brecher des Sektortauschs. Der nächste vorgesehene Schritt ist die
Rückwärtssuche nach diesem Brecher. OP3 bleibt offen.

Vergeben: H231, k445. Nächste frei: H232, k446 (vor Vergabe gegen `main` prüfen).
